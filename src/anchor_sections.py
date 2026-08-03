#!/usr/bin/env python3
"""Insert `### ` section anchors into the big PDF-sourced instruments.

  python3 src/anchor_sections.py            # anchor snapshots + documents, update hashes
  python3 src/anchor_sections.py --check    # exit 1 if any anchor/hash is stale (CI)

WHY ANCHORS AND NOT SECTION DOCUMENTS. Measured 2026-08-03: zero of ~300 Oregon
mentions of WIOA / Perkins V / CJIS / Pub 1075 are section-shaped (2 CFR 200's split
was justified by the opposite measurement — 85% sectioned — and by an XML source
carrying per-section dates and point-in-time text, which these PDFs cannot supply).
What agents actually lacked was NAVIGATION: get_document on a 900 KB body was a
glance-or-everything binary. Toolkit ≥ v1.21.0 serves `### ` subsections and lists
them on big-doc responses — so the fix is anchors in the text, not new documents.
The demand trigger stays cheap: the day section-shaped citations appear in the
citing corpora, scan_cited_sections.py's approach mints section docs exactly as it
did for 2 CFR 200.

MECHANICS. Anchoring PREFIXES existing heading lines with `### ` — it never adds,
removes, or reorders a word. Three invariants that keeps:
  * check_extraction.py still passes untouched: its TOKEN regex starts at an
    alphanumeric, so `###` contributes no token and the raw-PDF multiset is
    unchanged (this is why NOTHING here deletes the WIOA page-furniture lines —
    removing them would break that check; they stay, as noise the anchors now let
    a reader skip past).
  * provenance's in-order full-text check passes because the anchors live in BOTH
    the snapshot .txt and the document body — the 2-cfr-200 arrangement.
  * idempotent: an already-anchored line is never re-anchored, so --check is
    "running again changes nothing".

PER-INSTRUMENT RULES (each measured before being written):
  pl-113-128 (WIOA, 298 pp): `^SEC\\. \\d+\\.` — exact case matters: the table of
    contents uses `Sec. 1.` and the body `SEC. 1.`, so case IS the TOC filter.
    TITLE anchors are deliberately absent: title ranges derive arithmetically from
    section numbers (Title I = SEC. 1xx) in citation_schemes.py.
  pl-115-224 (Perkins V, 61 pp): same rule; the cleanest parse in the corpus.
  irs-pub-1075-11-2021 (216 pp): numbered headings up to four levels deep,
    excluding TOC lines (they carry `____` dot-leaders) and long lines (real
    headings measured short; cross-references live mid-paragraph). The NIST
    control-id grain is NOT anchored — measured 41-byte median = the regex mostly
    matches cross-references, not headings.
  cjis-sp-6-1: DEFERRED, with the reason on the record: two incompatible numbering
    systems (5.x front matter, then 626 KB of NIST control catalog), every control
    id appearing at least three times (TOC, summary table, body), and incorporated
    third-party standards raising a per-section reproduction question nobody has
    determined. A two-phase region-aware parser is a real project; do it when a
    CJIS citation with any specificity actually arrives (today all five
    version-qualified ones cite versions this corpus refuses anyway).
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SNAPSHOTS = ROOT / "_meta" / "snapshots"
INSTRUMENTS = ROOT / "instruments"

sys.path.insert(0, str(ROOT / "src"))


def _pub1075_heading(line: str) -> bool:
    if "____" in line or len(line) > 90:
        return False
    # up to four levels: real headings run 1.7.1.1 Termination Documentation
    return bool(re.match(r"^\d+(?:\.\d+){1,3}\s+\S", line))


RULES: dict[str, dict] = {
    "pl-113-128": {"doc": "pl-113-128",
                   "match": lambda l: bool(re.match(r"^SEC\. \d+\.", l))},
    "pl-115-224": {"doc": "pl-115-224",
                   "match": lambda l: bool(re.match(r"^SEC\. \d+\.", l))},
    "irs-pub-1075": {"doc": "irs-pub-1075-11-2021", "match": _pub1075_heading},
}


def anchor_text(text: str, match) -> tuple[str, int]:
    out, n = [], 0
    for line in text.splitlines():
        if not line.startswith("### ") and match(line):
            out.append("### " + line)
            n += 1
        else:
            out.append(line)
    return "\n".join(out) + ("\n" if text.endswith("\n") else ""), n


def process(check: bool) -> int:
    from corpus_toolkit.repo import hash_snapshot

    stale = []
    for snap_id, rule in RULES.items():
        txt_path = SNAPSHOTS / f"{snap_id}.txt"
        md_path = INSTRUMENTS / f"{rule['doc']}.md"
        txt = txt_path.read_text(encoding="utf-8")
        new_txt, n_new = anchor_text(txt, rule["match"])
        n_total = sum(1 for l in new_txt.splitlines() if l.startswith("### "))

        md = md_path.read_text(encoding="utf-8")
        head, sep, body = md.partition("\n## Full text\n")
        new_body, _ = anchor_text(body, rule["match"])
        new_md = head + sep + new_body

        if check:
            if n_new or new_md != md:
                stale.append(f"{snap_id}: {n_new} unanchored heading(s)")
            continue

        if n_new == 0 and new_md == md:
            print(f"  ok   {snap_id}: {n_total} anchors already present")
            continue
        txt_path.write_text(new_txt, encoding="utf-8")
        md_path.write_text(new_md, encoding="utf-8")

        # hash + conversion note: the snapshot's normalized text changed, so the
        # recorded hash must follow it (hash_snapshot's txt branch).
        fmt = re.search(r"^source_format:\s*(\w+)", new_md, re.M).group(1)
        sha = hash_snapshot(snap_id, fmt, SNAPSHOTS)
        new_md = md_path.read_text(encoding="utf-8")
        new_md = re.sub(r"^source_sha256:\s*\S+$", f"source_sha256: {sha}",
                        new_md, count=1, flags=re.M)
        note = (f'conversion_notes: "{n_total} section anchors (### ) inserted at '
                f'extraction for navigability — the anchor prefixes existing heading '
                f'lines and adds no words; see src/anchor_sections.py"')
        if re.search(r"^conversion_notes:", new_md, re.M):
            new_md = re.sub(r"^conversion_notes:.*$", note, new_md, count=1, flags=re.M)
        else:
            new_md = re.sub(r"^content_mode: verbatim$",
                            f"content_mode: verbatim\n{note}", new_md, count=1, flags=re.M)
        md_path.write_text(new_md, encoding="utf-8")
        print(f"  anchored {snap_id}: {n_new} new, {n_total} total; sha -> {sha[:12]}…")

    if check:
        if stale:
            print("STALE: " + "; ".join(stale) + " — re-run src/anchor_sections.py",
                  file=sys.stderr)
            return 1
        print("section anchors are current.")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()
    return process(args.check)


if __name__ == "__main__":
    sys.exit(main())
