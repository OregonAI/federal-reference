#!/usr/bin/env python3
"""Which sections of 2 CFR 200 does Oregon actually cite? -> _meta/cited-sections.yml

    python3 src/scan_cited_sections.py --erf ../oregon-policy-repo --audits ../oregon-audits

The operator decision for this corpus was "split only what is cited", so the split list is
DERIVED rather than chosen. This script derives it and writes it to `_meta/cited-sections.yml`,
which is committed and reviewed.

WHY COMMIT THE RESULT INSTEAD OF COMPUTING IT AT BUILD TIME: CI for this repo cannot reach
executive-regulatory-frameworks or oregon-audits -- they are separate repositories and are not
checked out. A build-time scan would silently find zero citations there and split nothing,
which is the failure mode this platform keeps producing: a step that reports success while
doing nothing. So the scan runs on a developer machine, against real checkouts, and its output
is a reviewable artifact.

A CITED SECTION THAT NO LONGER EXISTS IS A FINDING, NOT A DROP. Two of the 29 (200.53 and
200.62) were REMOVED from the CFR. Silently omitting them would leave four real citations in
Oregon's own audits pointing at nothing, and quietly resolving them to current text would
answer a compliance question with law that was not in force. Both are classified here from
eCFR's own version record -- `removed: true` plus an amendment date -- and carried into the
corpus as superseded documents holding their last-in-force text.
"""
from __future__ import annotations

import argparse
import collections
import json
import pathlib
import re
import sys
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "_meta" / "cited-sections.yml"

# "2 CFR 200.303", "2 C.F.R. § 200.303", "2 CFR Part 200.303", "2 CFR §§ 200.303".
# Deliberately anchored on the literal part number: this corpus splits ONE part, and a
# general CFR-citation regex here would quietly collect sections of parts we do not hold.
SECTION_RE = re.compile(r"\b2\s+C\.?\s?F\.?\s?R\.?\s*(?:Part\s+)?§{0,2}\s*200\.(\d+)\b")

SKIP_PARTS = ("/.git/", "/_meta/", "/snapshots/", "/node_modules/")


def scan(root: pathlib.Path, label: str, counts, sources) -> int:
    """Count section citations under `root`. Returns files scanned."""
    n = 0
    # SORTED walk. An unsorted rglob in the ERF citation scan produced a catalog that
    # differed between machines while every count matched -- only CI could see it.
    for path in sorted(root.rglob("*.md")):
        s = str(path)
        if any(p in s for p in SKIP_PARTS):
            continue
        n += 1
        for sec in SECTION_RE.findall(path.read_text(errors="ignore")):
            counts[sec] += 1
            sources[sec].add(label)
    return n


def ecfr_versions(title: int, part: int) -> dict[str, dict]:
    """eCFR's own version record per section: {'200.53': {...}}.

    This is the authority for whether a section still exists. Reading it beats inferring
    absence from the current text: absence tells you a section is gone, this tells you WHEN
    it went and whether it was removed or merely renumbered.
    """
    url = f"https://www.ecfr.gov/api/versioner/v1/versions/title-{title}.json?part={part}"
    data = json.loads(urllib.request.urlopen(url, timeout=180).read())
    out: dict[str, dict] = {}
    for rec in data.get("content_versions") or data.get("versions") or []:
        ident = rec.get("identifier")
        if not ident:
            continue
        prev = out.get(ident)
        # Keep the LATEST record per section -- that is the one that says whether it is
        # still here. Records arrive oldest-first but that is not promised, so compare.
        if prev is None or (rec.get("amendment_date") or "") >= (prev.get("amendment_date") or ""):
            out[ident] = rec
    return out


def q(s: str) -> str:
    return json.dumps(str(s), ensure_ascii=False)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--erf", required=True, type=pathlib.Path)
    ap.add_argument("--audits", required=True, type=pathlib.Path)
    args = ap.parse_args()

    counts: collections.Counter = collections.Counter()
    sources: dict[str, set] = collections.defaultdict(set)
    total_files = 0
    for root, label in ((args.erf, "erf"), (args.audits, "audits")):
        if not root.is_dir():
            print(f"error: {root} is not a directory", file=sys.stderr)
            return 1
        got = scan(root, label, counts, sources)
        total_files += got
        print(f"  scanned {got:>5} files in {root}  ({label})")

    if not counts:
        # A scan that finds nothing is a broken scan, not an empty answer: this list is
        # known to be non-empty. Failing loudly here is the whole point of the file.
        print("error: no section citations found -- check the paths", file=sys.stderr)
        return 1

    print(f"  {sum(counts.values())} citations across {len(counts)} distinct sections")
    vers = ecfr_versions(2, 200)
    print(f"  eCFR version record: {len(vers)} sections")

    current, removed = [], []
    for sec, n in sorted(counts.items(), key=lambda kv: (-kv[1], int(kv[0]))):
        rec = vers.get(f"200.{sec}")
        entry = {"section": f"200.{sec}", "citations": n,
                 "cited_in": sorted(sources[sec])}
        if rec is None:
            print(f"error: 200.{sec} has no eCFR version record at all", file=sys.stderr)
            return 1
        if rec.get("removed"):
            entry["removed_on"] = rec["amendment_date"]
            entry["name_when_in_force"] = " ".join(str(rec.get("name") or "").split())
            removed.append(entry)
        else:
            current.append(entry)

    lines = [
        "# GENERATED by src/scan_cited_sections.py -- do not hand-edit.",
        "#",
        "# Which sections of 2 CFR 200 get their own document, and why each one is here.",
        "# Regenerate with:",
        "#   python3 src/scan_cited_sections.py --erf ../oregon-policy-repo --audits ../oregon-audits",
        "#",
        "# Committed rather than computed during the build because CI cannot reach the sibling",
        "# repositories this is derived from; a build-time scan would find zero and split nothing.",
        "",
        f"scanned_files: {total_files}",
        f"total_citations: {sum(counts.values())}",
        "",
        "# Sections still in force. Text comes from the committed 2026 part snapshot.",
        "current:",
    ]
    for e in current:
        lines += [f"  - section: {q(e['section'])}",
                  f"    citations: {e['citations']}",
                  f"    cited_in: [{', '.join(q(c) for c in e['cited_in'])}]"]
    lines += [
        "",
        "# REMOVED from the CFR, but still cited by Oregon material. These carry their",
        "# LAST-IN-FORCE text from a point-in-time snapshot, marked superseded. Resolving one",
        "# of these to current text would answer with law that was not in force when it was",
        "# cited -- a wrong answer wearing a right answer's clothes.",
        "removed:",
    ]
    for e in removed:
        lines += [f"  - section: {q(e['section'])}",
                  f"    citations: {e['citations']}",
                  f"    cited_in: [{', '.join(q(c) for c in e['cited_in'])}]",
                  f"    removed_on: {q(e['removed_on'])}",
                  f"    name_when_in_force: {q(e['name_when_in_force'])}"]
    OUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"  wrote {OUT.relative_to(ROOT)}: {len(current)} current, {len(removed)} removed")
    for e in removed:
        print(f"      removed {e['section']} on {e['removed_on']} ({e['citations']} citations)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
