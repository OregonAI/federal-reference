#!/usr/bin/env python3
"""Which sections of a CFR part does Oregon actually cite? -> _meta/cited-sections/<part>.yml

    python3 src/scan_cited_sections.py --erf ../oregon-policy-repo --audits ../oregon-audits \
        --title 2 --part 200

The operator decision for this corpus was "split only what is cited", so the split list is
DERIVED rather than chosen. This script derives it, per PART, and writes it to
`_meta/cited-sections/<title>-cfr-<part>.yml`, which is committed and reviewed.

#34: `--title`/`--part` used to be implicit -- a literal `2` and `200.` baked into every
regex here, so the only part this script could ever measure was 2 CFR 200. Every big
instrument gets the identical demand-driven treatment now (see the STANDING TRIGGER note
below): the regexes are BUILT from whatever (title, part) is passed, and the short-form
disambiguation guard -- count `§NNN.MM` only in a file that also carries the full citation
elsewhere -- is the same per-part-derived mechanism it always was, now actually applied per
part instead of hardcoded to 200's collision with ORS chapter 200. #27's own triage (see
that issue) found the SAME guard is not marginal for 45 CFR 164: ORS chapter 164 (theft and
burglary) is the MORE common meaning of a bare `164.NNN` in Oregon material, and a scanner
that merely counted short forms without this guard would rank an Oregon criminal statute as
the most-demanded section of the HIPAA Privacy Rule.

WHY COMMIT THE RESULT INSTEAD OF COMPUTING IT AT BUILD TIME: CI for this repo cannot reach
executive-regulatory-frameworks or oregon-audits -- they are separate repositories and are
not checked out. A build-time scan would silently find zero citations there and split nothing,
which is the failure mode this platform keeps producing: a step that reports success while
doing nothing. So the scan runs on a developer machine, against real checkouts, and its output
is a reviewable artifact.

A CITED SECTION THAT NO LONGER EXISTS IS A FINDING, NOT A DROP. Two of 2 CFR 200's 29 (200.53
and 200.62) were REMOVED from the CFR. Silently omitting them would leave four real citations
in Oregon's own audits pointing at nothing, and quietly resolving them to current text would
answer a compliance question with law that was not in force. Both are classified here from
eCFR's own version record -- `removed: true` plus an amendment date -- and carried into the
corpus as superseded documents holding their last-in-force text.

STANDING TRIGGER FOR THE OTHER BIG INSTRUMENTS (recorded 2026-08-03): WIOA,
Perkins V, CJIS and Pub 1075 were measured at ZERO section-shaped citations,
so they got `### ` anchors (src/anchor_sections.py) instead of section
documents. The day a scan like this one finds section-shaped citations to any
of them in the citing corpora, that instrument graduates to the demand-driven
split exactly as it did for 2 CFR 200 -- same pipeline, same review gate.
Anchors first, documents when demanded. (This is a CFR-part-shaped scan; WIOA and
Perkins V are public laws with `SEC. N.` numbering, not `title CFR part.section`, so
graduating one of those needs a citation-shape scan of its own, not this script.)
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
OUT_DIR = ROOT / "_meta" / "cited-sections"

SKIP_PARTS = ("/.git/", "/_meta/", "/snapshots/", "/node_modules/")


def patterns(title: int, part: int) -> tuple[re.Pattern, re.Pattern, re.Pattern]:
    """(section_re, short_re, part_re) for one (title, part) -- built, not hardcoded.

    section_re: "2 CFR 200.303", "2 C.F.R. § 200.303", "2 CFR Part 200.303", "2 CFR §§ 200.303".
    Anchored on the literal title and part: a general CFR-citation regex here would quietly
    collect sections of parts this corpus does not hold.

    short_re: THE SHORT FORM, which section_re cannot see and which is how real documents
    actually cite. A report names "2 CFR 200" once and then writes "§200.414" for the rest of
    the section. Requiring the literal "N CFR" on every hit hid 42 citations across 18
    sections for 2 CFR 200 alone, NINE of which had no document at all.

    part_re: a full part citation anywhere in the file, which licenses the short form above.
    ONLY COUNTED IN FILES THAT ALSO CARRY A FULL CITATION -- a bare `§NNN.MM` is ambiguous on
    its own (Oregon's own ORS numbering collides with plenty of CFR part numbers -- chapter
    200, chapter 164 -- see this file's module docstring), so the full citation elsewhere in
    the same document is what establishes which title/part the short form refers to.
    """
    t, p = re.escape(str(title)), re.escape(str(part))
    section_re = re.compile(
        rf"\b{t}\s+C\.?\s?F\.?\s?R\.?\s*(?:Part\s+)?§{{0,2}}\s*{p}\.(\d+)\b")
    short_re = re.compile(rf"§{{1,2}}\s*{p}\.(\d+)\b")
    part_re = re.compile(rf"\b{t}\s+C\.?\s?F\.?\s?R\.?\s*(?:Part\s+)?§{{0,2}}\s*{p}\b")
    return section_re, short_re, part_re


def scan(root: pathlib.Path, label: str, section_re, short_re, part_re, counts, sources) -> int:
    """Count section citations under `root`. Returns files scanned."""
    n = 0
    # SORTED walk. An unsorted rglob in the ERF citation scan produced a catalog that
    # differed between machines while every count matched -- only CI could see it.
    for path in sorted(root.rglob("*.md")):
        s = str(path)
        if any(p in s for p in SKIP_PARTS):
            continue
        n += 1
        text = path.read_text(errors="ignore")
        hits = section_re.findall(text)
        if hits or part_re.search(text):
            # The short form only counts once this file has established the part.
            hits = hits + short_re.findall(text)
        for sec in hits:
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
    ap = argparse.ArgumentParser(description=__doc__,
                                  formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--erf", required=True, type=pathlib.Path)
    ap.add_argument("--audits", required=True, type=pathlib.Path)
    ap.add_argument("--title", required=True, type=int, help="CFR title, e.g. 2")
    ap.add_argument("--part", required=True, type=int, help="CFR part, e.g. 200")
    args = ap.parse_args()

    part_id = f"{args.title}-cfr-{args.part}"
    out = OUT_DIR / f"{part_id}.yml"
    section_re, short_re, part_re = patterns(args.title, args.part)
    part_prefix = str(args.part)

    counts: collections.Counter = collections.Counter()
    sources: dict[str, set] = collections.defaultdict(set)
    total_files = 0
    for root, label in ((args.erf, "erf"), (args.audits, "audits")):
        if not root.is_dir():
            print(f"error: {root} is not a directory", file=sys.stderr)
            return 1
        got = scan(root, label, section_re, short_re, part_re, counts, sources)
        total_files += got
        print(f"  scanned {got:>5} files in {root}  ({label})")

    if not counts:
        # A scan that finds nothing is either a broken scan or a part that graduates no
        # further than the anchors it already has -- the caller decides which; this script
        # only reports the fact rather than writing an empty artifact that looks derived.
        print(f"error: no {args.title} CFR {args.part} section citations found -- check the "
              f"paths, or this part does not (yet) meet the demand-driven split trigger",
              file=sys.stderr)
        return 1

    print(f"  {sum(counts.values())} citations across {len(counts)} distinct sections")
    vers = ecfr_versions(args.title, args.part)
    print(f"  eCFR version record: {len(vers)} sections")

    current, removed = [], []
    for sec, n in sorted(counts.items(), key=lambda kv: (-kv[1], int(kv[0]))):
        rec = vers.get(f"{part_prefix}.{sec}")
        entry = {"section": f"{part_prefix}.{sec}", "citations": n,
                 "cited_in": sorted(sources[sec])}
        if rec is None:
            print(f"error: {part_prefix}.{sec} has no eCFR version record at all",
                  file=sys.stderr)
            return 1
        if rec.get("removed"):
            entry["removed_on"] = rec["amendment_date"]
            entry["name_when_in_force"] = " ".join(str(rec.get("name") or "").split())
            removed.append(entry)
        else:
            current.append(entry)

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    lines = [
        "# GENERATED by src/scan_cited_sections.py -- do not hand-edit.",
        "#",
        f"# Which sections of {args.title} CFR {args.part} get their own document, and why "
        f"each one is here.",
        "# Regenerate with:",
        f"#   python3 src/scan_cited_sections.py --erf ../oregon-policy-repo "
        f"--audits ../oregon-audits --title {args.title} --part {args.part}",
        "#",
        "# Committed rather than computed during the build because CI cannot reach the sibling",
        "# repositories this is derived from; a build-time scan would find zero and split nothing.",
        "",
        f"scanned_files: {total_files}",
        f"total_citations: {sum(counts.values())}",
        "",
        "# Sections still in force. Text comes from the committed current part snapshot.",
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
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"  wrote {out.relative_to(ROOT)}: {len(current)} current, {len(removed)} removed")
    for e in removed:
        print(f"      removed {e['section']} on {e['removed_on']} ({e['citations']} citations)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
