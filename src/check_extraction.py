#!/usr/bin/env python3
"""Assert the committed text still matches the RAW source. Run in CI.

    python3 src/check_extraction.py

WHY THIS EXISTS, and why corpus-verify-provenance is not enough.

Provenance compares each document's `## Full text` against `_meta/snapshots/<id>.txt`, and
`source_sha256` is the sha256 of that same `.txt` (corpus_toolkit.repo.hash_snapshot hashes
the normalized text, not the raw bytes). But the `.txt` is WRITTEN BY THE EXTRACTOR from the
identical string that goes into the document. So the whole chain compares the extractor's
output against itself:

    raw PDF/XML --extract--> text --+--> instruments/<id>.md
                                    +--> _meta/snapshots/<id>.txt --> source_sha256

Nothing in that loop ever reads the PDF or XML again. If the extractor drops a line, the
document, the snapshot and the hash all agree about the text that is missing, and every
check passes. That is not theoretical -- it is exactly how CJIS SP 6.1 shipped with the year
"2006" and the standard number "124" deleted from its incorporated-references appendix while
five green checks reported the corpus healthy.

The toolkit's choice is defensible on its own terms (re-extracting at verification time is
machine- and version-dependent, so hashing raw bytes there would be flaky). It just means
fidelity to the SOURCE has to be checked somewhere, and this is that somewhere.

WHAT IT CHECKS. Every content token in the raw source must survive into the committed text.
Tokens are compared as a multiset, so duplicates and reordering are caught too, and page
furniture is excluded the same way the extractor excludes it -- by asking the extractor,
rather than by reimplementing the rule and hoping the two agree.

Requires the raw snapshots, which this corpus commits (tens of MB, dominated by the
per-title USLM snapshots ADR-0006 introduced -- one title alone is ~22 MB, since OLRC
serves USLM only per title, not per section). A corpus on
`snapshot_policy: hash-only` cannot run this, and should say so rather than imply provenance
covers it.
"""
from __future__ import annotations

import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
from ingest_instruments import (  # noqa: E402
    SNAPSHOTS, extract_cfr, extract_pdf, extract_usc, is_page_number, page_furniture,
)

from nist_controls import PUBLICATION_ID  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
INSTRUMENTS = ROOT / "instruments"

# A "content token": anything with a letter or digit in it. Punctuation-only fragments are
# ignored because whitespace normalization legitimately moves them around.
TOKEN = re.compile(r"[0-9A-Za-z][0-9A-Za-z._/§-]*")


def tokens(text: str) -> list[str]:
    return TOKEN.findall(text)


def raw_tokens_pdf(path: Path, engine: str = "pypdf") -> list[str]:
    """Tokens in the raw PDF, minus only what page furniture legitimately removes.

    Furniture is identified with the SAME functions the extractor uses, restricted to the
    same band, so this check cannot pass by accidentally sharing a bug with the extractor in
    the other direction: if the band logic is wrong, the counts diverge and this fails.
    """
    from ingest_instruments import FURNITURE_BAND, pdf_pages

    pages = pdf_pages(path, engine)
    head, foot = page_furniture(pages)
    kept: list[str] = []
    for lines in pages:
        stripped = [l.strip() for l in lines]
        filled = [i for i, s in enumerate(stripped) if s]
        band = set(filled[:FURNITURE_BAND]) | set(filled[-FURNITURE_BAND:])
        for i, s in enumerate(stripped):
            if not s:
                continue
            if i in band and (s in head or s in foot or is_page_number(s, len(pages))):
                continue
            kept.extend(tokens(s))
    return kept


def prefix_problem(expect: list[str], got: list[str]) -> str | None:
    """None if `got` is exactly the raw token stream up to its `REFERENCES` heading.

    For the one publication this corpus holds only in part (nist_publication: the front matter
    and the control catalog, see nist_controls.held_scope). The committed text must be a strict
    PREFIX of the raw PDF's token stream AND the next raw token must be the catalog-closing
    `REFERENCES` -- so an altered or dropped token fails, a cut that stops early fails, and a cut
    that runs on into the bibliography/glossary fails. The cut is thereby checked against the raw
    source, not against the function that made it.
    """
    n = len(got)
    if expect[:n] != got:
        i = next((k for k, (a, b) in enumerate(zip(expect, got)) if a != b), min(n, len(expect)))
        return (f"committed text diverges from the raw source at token {i}: raw "
                f"{expect[i:i + 3]!r} vs committed {got[i:i + 3]!r}")
    if n >= len(expect) or expect[n] != "REFERENCES":
        return (f"committed text stops at token {n}, where the raw source continues "
                f"{expect[n:n + 3]!r} instead of the catalog-closing REFERENCES heading")
    return None


def split_word_problems(py_lines: list[str], pop_lines: list[str]) -> list[str]:
    """Adjacent words on one held line whose concatenation poppler reads as ONE word on the same
    page while neither half is a word poppler read -- a word still split in the committed text.
    Independent of repair_split_words (it asks poppler's word set, not the repair's alignment), so
    a repair that missed a split is caught here instead of agreeing with itself."""
    pop_words = {w for line in pop_lines for w in line.split()}
    found = []
    for line in py_lines:
        ws = line.split()
        for a, b in zip(ws, ws[1:]):
            if a + b in pop_words and a not in pop_words and b not in pop_words:
                found.append(f"{a!r} {b!r} -> {a + b!r}")
    return found


def held_split_words(raw_path: Path, engine: str) -> str | None:
    """For an entry that opts into poppler's reading (`pdf_engine: pypdf+pdftotext`): None if no
    word on a held page is still split where poppler reads it whole, else a description. Pages
    after the catalog-closing REFERENCES heading are not held and not checked."""
    if engine == "pypdf":
        return None
    from ingest_instruments import pdf_pages
    from nist_controls import CATALOG_START, is_catalog_end
    pages, pop = pdf_pages(raw_path, engine), pdf_pages(raw_path, "pdftotext")
    started = False
    bad: list[str] = []
    for n, (py, pp) in enumerate(zip(pages, pop), 1):
        started = started or any(CATALOG_START.match(l.strip()) for l in py)
        if started and any(is_catalog_end(l) for l in py):
            break
        bad += [f"p.{n}: {x}" for x in split_word_problems(py, pp)]
    return (f"{len(bad)} word(s) still split where pdftotext reads them whole: "
            f"{'; '.join(bad[:5])}") if bad else None


def uses_catalog_prefix_check(doc_id: str, kind: str) -> bool:
    """The prefix check is written for SP 800-53's catalog cut; another nist_publication (FIPS 140,
    SP 800-63) is held whole and is checked token-for-token like any other PDF."""
    return kind == "nist_publication" and doc_id == PUBLICATION_ID


def main() -> int:
    manifest = yaml.safe_load((ROOT / "_meta" / "source-manifest.yml").read_text())
    docs = {}
    for path in sorted(INSTRUMENTS.glob("*.md")):
        fm = yaml.safe_load(path.read_text().split("---", 2)[1])
        docs.setdefault(fm.get("snapshot_id") or fm["id"], []).append((fm["id"], path))

    fails = []
    for src in manifest["sources"]:
        sid = src["id"]
        fmt = src["format"]
        kind = src["instrument_kind"]
        raw_path = SNAPSHOTS / f"{sid}.{fmt}"
        if not raw_path.is_file():
            print(f"  SKIP  {sid}: raw snapshot not committed")
            continue

        # DISPATCHED ON instrument_kind, NEVER ON `fmt` -- the same rule ingest_instruments.py
        # follows, and for the same reason. USLM and eCFR are BOTH `format: xml`; keying on
        # `fmt` alone would run a USLM title through extract_cfr, which reads
        # `TYPE="SECTION"` attributes USLM does not have and returns silently EMPTY text
        # (confirmed against Title 20's own XML: 0 chars, no exception) rather than raising --
        # a checker that "asks the extractor what the extractor did" only holds if BOTH sides
        # ask the SAME extractor the ingest actually used.
        if kind == "cfr_part":
            expect = tokens(extract_cfr(raw_path.read_bytes())[0])
        elif kind == "usc_section":
            usc_title, usc_sec = sid.split("-usc-", 1)
            root = ET.fromstring(raw_path.read_bytes())
            expect = tokens(extract_usc(root, usc_title, usc_sec)[0])
        else:
            expect = raw_tokens_pdf(raw_path, src.get("pdf_engine", "pypdf"))

        # The document that owns this snapshot whole (the part, or the publication itself);
        # section documents carry only a slice and are covered by provenance's slice check.
        owner = next((p for i, p in docs.get(sid, []) if "." not in i.replace(sid, "")), None)
        if owner is None:
            if sid not in docs:
                print(f"  FAIL  {sid}: raw snapshot committed but no document claims it "
                      f"(id or snapshot_id) -- ingestion may have failed partway")
                fails.append(sid)
                continue
            owner = docs[sid][0][1]
        body = owner.read_text().split("## Full text\n\n", 1)[-1]
        got = tokens(body)

        if uses_catalog_prefix_check(sid, kind):
            problem = prefix_problem(expect, got)
            if problem is None:
                problem = held_split_words(raw_path, src.get("pdf_engine", "pypdf"))
            if problem is None:
                print(f"  ok    {sid}: {len(got):>7,} of {len(expect):,} raw tokens, an exact "
                      f"prefix ending at the catalog (REFERENCES onward deliberately not held)")
                continue
            print(f"  FAIL  {sid}: {problem}")
            fails.append(sid)
            continue
        if got == expect:
            print(f"  ok    {sid}: {len(expect):>7,} tokens match the raw {fmt}")
            continue

        from collections import Counter
        missing = Counter(expect) - Counter(got)
        extra = Counter(got) - Counter(expect)
        print(f"  FAIL  {sid}: {sum(missing.values())} token(s) missing, "
              f"{sum(extra.values())} unexpected")
        for t, n in list(missing.items())[:8]:
            print(f"           missing {n}x {t!r}")
        fails.append(sid)

    print()
    if fails:
        print(f"FAILED: {len(fails)} document(s) do not match their raw source: "
              f"{', '.join(fails)}", file=sys.stderr)
        return 1
    print("Every document matches its raw source token-for-token.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
