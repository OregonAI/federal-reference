#!/usr/bin/env python3
"""Promote the cited sections of 2 CFR 200 into their own documents.

    python3 src/split_cfr_sections.py            # use committed snapshots
    python3 src/split_cfr_sections.py --refetch   # re-fetch the historical snapshot

Reads `_meta/cited-sections.yml` (produced by src/scan_cited_sections.py) and writes one
`instruments/2-cfr-200.NNN.md` per cited section. Run AFTER ingest_instruments.py.

WHY SPLIT AT ALL. 85% of the section-or-part citations Oregon makes to the Uniform Guidance
are section-level (256 of 300), and § 200.303 alone accounts for 58. A corpus holding only the
part answers "2 CFR 200" and misses every one of those, so the sibling edges built in Stage 4
would resolve the least-cited form of the citation and nothing else.

NO REFETCH FOR CURRENT SECTIONS. Their text is sliced out of the part snapshot already
committed by Stage 1, and each document points at it with `snapshot_id: 2-cfr-200` -- the
field exists for exactly this ("documents split from, or sharing, one source file"). That
means a section document cannot disagree with the part it came from: there is one source of
truth on disk and provenance verifies both against it.

THE TWO REMOVED SECTIONS ARE THE INTERESTING CASE. 200.53 and 200.62 were removed by the
2021-02-22 amendment, which consolidated Subpart A's definitions into a single § 200.1. Oregon
audits 2020-14, 2021-13 and 2022-18 cite them anyway, because they were in force for the
fiscal years under audit. They are ingested from a point-in-time snapshot of the day BEFORE
removal -- their last-in-force text -- with status `superseded` and `superseded_by` pointing
at § 200.1. Resolving them to current text would hand back law that was not in force when it
was cited; dropping them would leave four real citations pointing at nothing.
"""
from __future__ import annotations

import argparse
import pathlib
import re
import sys
import urllib.request
import xml.etree.ElementTree as ET

import yaml

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from ingest_instruments import _flatten  # noqa: E402  (same extraction, by construction)

ROOT = pathlib.Path(__file__).resolve().parent.parent
SNAPSHOTS = ROOT / "_meta" / "snapshots"
INSTRUMENTS = ROOT / "instruments"
CITED = ROOT / "_meta" / "cited-sections.yml"

PART_ID = "2-cfr-200"
# The day BEFORE the amendment that removed them -- the last date their text was in force.
LAST_IN_FORCE = "2021-02-21"
HIST_ID = f"{PART_ID}-{LAST_IN_FORCE}"
HIST_URL = (f"https://www.ecfr.gov/api/versioner/v1/full/{LAST_IN_FORCE}"
            f"/title-2.xml?part=200")


def guard(text: str) -> str:
    """Never let extracted text start a line with `## `.

    corpus_toolkit.repo.FULLTEXT_RE ends the body at the first such line. This has cost this
    platform a truncated document three times now -- twice from source text, once from a
    heading we emitted ourselves -- and each time the file looked perfectly well-formed. CFR
    prose is very unlikely to trip it; the guard costs nothing and the failure is silent.
    """
    return re.sub(r"^(#{1,6}\s)", r" \1", text, flags=re.M)


def sections_from(raw: bytes) -> dict[str, tuple[str, str]]:
    """{'200.303': (heading, body_text)} for every SECTION in a part XML.

    Mirrors extract_cfr()'s per-element logic exactly, so a section's text here is the same
    run of lines the part document holds -- which is what makes provenance against the shared
    snapshot come out whole rather than approximately.
    """
    out: dict[str, tuple[str, str]] = {}
    for el in ET.fromstring(raw).iter():
        if el.get("TYPE") != "SECTION":
            continue
        head_el = el.find("HEAD")
        head = _flatten(head_el) if head_el is not None else (el.get("N") or "")
        m = re.search(r"200\.(\d+)\b", head or "")
        if not m:
            continue
        body = [f"### {head}"]
        for child in el:
            if child is head_el:
                continue
            # Guard the EXTRACTED text only, never the heading we emit ourselves. Applying it
            # to the assembled body rewrote `### § 200.53 …` to ` ### § 200.53 …`, which broke
            # the slicer's `^### ` anchor and, worse, made the section text stop matching the
            # part it was cut from — the one property this file exists to preserve.
            t = guard(_flatten(child))
            if t:
                body.append(t)
        out[f"200.{m.group(1)}"] = (head, "\n".join(body))
    return out


def subject(head: str) -> str:
    """'§ 200.303 Internal controls.' -> 'Internal controls'."""
    s = re.sub(r"^\s*§*\s*200\.\d+\s*", "", head or "").strip()
    return s.rstrip(".").strip() or "Untitled section"


def part_dates() -> tuple[str, str]:
    """(as_of, retrieved) from the part document.

    Inherited rather than restated. A section carries the SAME bytes as the part it was cut
    from, so a section claiming a different as_of than its part would be asserting two
    different dates for one piece of text -- and in a corpus where the whole argument is
    "the version is part of the identity", that is the last field to let drift.
    """
    fm = yaml.safe_load((INSTRUMENTS / f"{PART_ID}.md").read_text().split("---")[1])
    return str(fm["as_of"]), str(fm["retrieved"])


def build(sec: str, head: str, body: str, meta: dict, sha: str,
          amended_on: str | None, superseded_by: str | None) -> str:
    live = superseded_by is None
    doc_id = f"{PART_ID}.{sec.split('.', 1)[1]}"
    fm = {
        "schema_version": 1,
        "corpus": "federal-reference",
        "jurisdiction": "us",
        "id": doc_id,
        # THE TITLE CARRIES THE SUPERSESSION, and that is load-bearing rather than cosmetic.
        # A sibling corpus resolves into this one through `corpus-index.json`, whose rows are
        # [title, doc_type, path] -- no `status`, no `version`. So an audit resolving
        # `2 CFR 200.53` gets back a title and nothing else, and without the marker it reads
        # as current law. Frontmatter `status: superseded` is invisible across that boundary.
        "title": (f"2 CFR {sec} — {subject(head)}" if live else
                  f"2 CFR {sec} — {subject(head)} (SUPERSEDED {meta['removed_on']})"),
        "doc_type": "federal_instrument",
        "citation": f"2 CFR {sec}",
        "authority_level": "federal",
        "issuing_body": "Office of Management and Budget",
        "instrument_kind": "cfr_section",
        "version": None,
        "as_of": PART_AS_OF if live else LAST_IN_FORCE,
        "amended_on": amended_on,
        "reproduction_basis":
            "17 U.S.C. § 105 — edition of the CFR published by the U.S. government",
        "superseded_by": superseded_by,
        "source_url": (f"https://www.ecfr.gov/current/title-2/section-{sec}" if live
                       else HIST_URL),
        "source_format": "xml",
        # Shared with the part document rather than duplicated. One source of truth on disk,
        # so a section cannot silently drift from the part it was cut out of.
        "snapshot_id": PART_ID if live else HIST_ID,
        "retrieved": PART_RETRIEVED if live else HIST_RETRIEVED,
        "source_sha256": sha,
        "status": "current" if live else "superseded",
        "content_mode": "verbatim",
        "relationships": {"related": [PART_ID]},
        "maintainer": "@morficflux",
        # Left EMPTY on purpose; a human sets them at PR approval. An ingester that stamps a
        # verification it did not perform is worse than a blank.
        "last_verified": "",
        "verified_by": "",
    }
    if sec == "200.1":
        fm["relationships"]["supersedes"] = [f"{PART_ID}.53", f"{PART_ID}.62"]

    head_yaml = yaml.safe_dump(fm, sort_keys=False, allow_unicode=True, width=100).rstrip()
    cites = meta["citations"]
    parts = [f"---\n{head_yaml}\n---\n", "## At a glance\n",
             f"**2 CFR {sec}** — {subject(head)}\n\n"
             f"- Issued by: Office of Management and Budget\n"
             f"- Part: 2 CFR 200 (Uniform Guidance)\n"
             f"- Text as of: {fm['as_of']}"
             + (f" (section last amended {amended_on})" if amended_on else "")
             + f"\n- Cited by Oregon material: {cites} time{'s' if cites != 1 else ''} "
               f"({', '.join(meta['cited_in'])})\n"
             f"- Reproduction basis: {fm['reproduction_basis']}\n"]

    if live:
        parts.append(
            "\n_NON-AUTHORITATIVE copy of one section, cut from the 2 CFR 200 snapshot this "
            "corpus holds. This is a federal requirement and carries penalties state policy "
            "does not — read it at the source URL before relying on it. This copy is CURRENT "
            "text, which is not necessarily the text in force when a document citing it was "
            "written._\n")
    else:
        parts.append(
            f"\n> **This section no longer exists.** It was removed from the CFR on "
            f"**{meta['removed_on']}**, when the definitions in Subpart A were consolidated "
            f"into [§ 200.1](./{PART_ID}.1.md). The text below is its **last-in-force** text, "
            f"as of {LAST_IN_FORCE}.\n>\n"
            f"> It is held because Oregon material still cites it {cites} "
            f"time{'s' if cites != 1 else ''} — those citations were made for fiscal years "
            f"when this section was in force. **The current definition may differ.** Do not "
            f"read this as current law, and do not treat § 200.1 as a drop-in replacement "
            f"without comparing them.\n"
            f"\n_NON-AUTHORITATIVE copy of one section, as it stood on {LAST_IN_FORCE}. Read "
            f"it at the source URL before relying on it. This is **superseded** text and is "
            f"NOT current law._\n")

    parts.append("\n## Full text\n\n" + body + "\n")
    return "\n".join(parts)


PART_AS_OF = PART_RETRIEVED = HIST_RETRIEVED = ""


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--refetch", action="store_true",
                    help="re-fetch the historical snapshot even if committed")
    ap.add_argument("--check", action="store_true",
                    help="verify the committed section documents match what this would write")
    args = ap.parse_args()

    from corpus_toolkit.repo import hash_snapshot

    if not CITED.is_file():
        print(f"error: {CITED} missing — run src/scan_cited_sections.py first", file=sys.stderr)
        return 1
    cited = yaml.safe_load(CITED.read_text())

    part_xml = SNAPSHOTS / f"{PART_ID}.xml"
    if not part_xml.is_file():
        print(f"error: {part_xml} missing — run src/ingest_instruments.py first", file=sys.stderr)
        return 1
    global PART_AS_OF, PART_RETRIEVED, HIST_RETRIEVED
    PART_AS_OF, PART_RETRIEVED = part_dates()
    HIST_RETRIEVED = PART_RETRIEVED
    current = sections_from(part_xml.read_bytes())
    print(f"  part snapshot: {len(current)} sections")

    hist_xml = SNAPSHOTS / f"{HIST_ID}.xml"
    if args.refetch or not hist_xml.is_file():
        print(f"  fetching {LAST_IN_FORCE} point-in-time snapshot …")
        raw = urllib.request.urlopen(HIST_URL, timeout=300).read()
        hist_xml.write_bytes(raw)
    hist = sections_from(hist_xml.read_bytes())
    print(f"  {LAST_IN_FORCE} snapshot: {len(hist)} sections")

    # The historical .txt is what provenance matches the superseded sections against, so it
    # must be the SAME extraction the documents were cut from, not a re-derivation.
    hist_text = re.sub(r"\n{3,}", "\n\n",
                       "\n\n".join(hist[k][1] for k in sorted(hist, key=lambda s: (
                           int(s.split(".")[1]),))) ).strip()
    (SNAPSHOTS / f"{HIST_ID}.txt").write_text(hist_text, encoding="utf-8")

    # THE INVARIANT, CHECKED RATHER THAN ASSERTED IN A COMMENT. Every current section's text
    # must appear verbatim in the part snapshot it shares. A comment in Stage 1 claimed a
    # guard the code did not implement and 2 CFR 200 shipped 1 character of 633,121 looking
    # perfectly well-formed; the lesson is to make the claim executable. This catches any
    # divergence between this extractor and extract_cfr(), including whitespace.
    part_txt = (SNAPSHOTS / f"{PART_ID}.txt").read_text(encoding="utf-8")
    for entry in cited["current"]:
        sec = entry["section"]
        if sec in current and current[sec][1] not in part_txt:
            print(f"error: {sec} text does not appear verbatim in {PART_ID}.txt — this "
                  f"extractor has diverged from extract_cfr()", file=sys.stderr)
            return 1
    print(f"  verified: all {len(cited['current'])} current sections appear verbatim in the "
          f"part snapshot")

    part_sha = hash_snapshot(PART_ID, "xml", SNAPSHOTS)
    hist_sha = hash_snapshot(HIST_ID, "xml", SNAPSHOTS)

    # Per-section amendment dates from the version record the scan already consulted.
    from scan_cited_sections import ecfr_versions
    vers = ecfr_versions(2, 200)

    stale: list[str] = []

    def emit(path, text: str) -> None:
        """Write, or in --check mode record a mismatch.

        WITHOUT --check THESE FILES WERE UNGATED. _meta/cited-sections.yml says "GENERATED
        -- do not hand-edit" and the 38 section documents are generated from it, but nothing
        compared them: edit either side and CI stayed green, which is the exact failure the
        `generated` job exists to prevent and which this repo's own AGENTS.md forbids.
        """
        if args.check:
            if not path.is_file() or path.read_text(encoding="utf-8") != text:
                stale.append(path.name)
        else:
            path.write_text(text, encoding="utf-8")

    written = 0
    for entry in cited["current"]:
        sec = entry["section"]
        if sec not in current:
            print(f"error: {sec} is listed as current but absent from the part snapshot",
                  file=sys.stderr)
            return 1
        head, body = current[sec]
        amended = (vers.get(sec) or {}).get("amendment_date")
        out = INSTRUMENTS / f"{PART_ID}.{sec.split('.', 1)[1]}.md"
        emit(out, build(sec, head, body, entry, part_sha, amended, None))
        written += 1

    for entry in cited["removed"]:
        sec = entry["section"]
        if sec in current:
            print(f"error: {sec} is listed as removed but IS in the current part snapshot",
                  file=sys.stderr)
            return 1
        if sec not in hist:
            print(f"error: {sec} absent from the {LAST_IN_FORCE} snapshot too", file=sys.stderr)
            return 1
        head, body = hist[sec]
        out = INSTRUMENTS / f"{PART_ID}.{sec.split('.', 1)[1]}.md"
        emit(out, build(sec, head, body, entry, hist_sha, entry["removed_on"], f"{PART_ID}.1"))
        written += 1
        print(f"    {sec} superseded -> {PART_ID}.1  ({entry['citations']} citations)")

    if args.check:
        # An EXTRA section document nobody generates is drift too -- a hand-added file, or one
        # left behind when a section drops out of the citation list.
        expected = {f"{PART_ID}.{e['section'].split('.', 1)[1]}.md"
                    for e in cited["current"] + cited["removed"]}
        orphans = sorted(p.name for p in INSTRUMENTS.glob(f"{PART_ID}.*.md")
                         if p.name not in expected)
        if stale or orphans:
            for n in stale:
                print(f"  STALE    {n}", file=sys.stderr)
            for n in orphans:
                print(f"  ORPHAN   {n} — not in _meta/cited-sections.yml", file=sys.stderr)
            print("\nRe-run: python3 src/split_cfr_sections.py", file=sys.stderr)
            return 1
        print(f"  {written} section documents are current")
        return 0

    print(f"  wrote {written} section documents")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
