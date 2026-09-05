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

Requires the raw snapshots, which this corpus commits (12 MB). A corpus on
`snapshot_policy: hash-only` cannot run this, and should say so rather than imply provenance
covers it.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
from ingest_instruments import (  # noqa: E402
    SNAPSHOTS, extract_cfr, extract_pdf, is_page_number, page_furniture,
)

ROOT = Path(__file__).resolve().parent.parent
INSTRUMENTS = ROOT / "instruments"

# A "content token": anything with a letter or digit in it. Punctuation-only fragments are
# ignored because whitespace normalization legitimately moves them around.
TOKEN = re.compile(r"[0-9A-Za-z][0-9A-Za-z._/§-]*")


def tokens(text: str) -> list[str]:
    return TOKEN.findall(text)


def raw_tokens_pdf(path: Path) -> list[str]:
    """Tokens in the raw PDF, minus only what page furniture legitimately removes.

    Furniture is identified with the SAME functions the extractor uses, restricted to the
    same band, so this check cannot pass by accidentally sharing a bug with the extractor in
    the other direction: if the band logic is wrong, the counts diverge and this fails.
    """
    from pypdf import PdfReader
    from ingest_instruments import FURNITURE_BAND

    reader = PdfReader(str(path))
    pages = [(p.extract_text() or "").splitlines() for p in reader.pages]
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
        raw_path = SNAPSHOTS / f"{sid}.{fmt}"
        if not raw_path.is_file():
            print(f"  SKIP  {sid}: raw snapshot not committed")
            continue

        if fmt == "xml":
            expect = tokens(extract_cfr(raw_path.read_bytes())[0])
        else:
            expect = raw_tokens_pdf(raw_path)

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
