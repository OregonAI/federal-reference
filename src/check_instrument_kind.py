#!/usr/bin/env python3
"""Assert every document's `instrument_kind` is one of this corpus's five known values.

    python3 src/check_instrument_kind.py

Run in CI (`generated` job, alongside check_citations.py and check_issuing_body.py).

WHY THIS EXISTS. `instrument_kind` is declared in `_meta/corpus.yml`'s
`mcp.extra_document_fields` as a bare field name -- corpus-toolkit's schema layer has no
enum mechanism for an extra field's values (verified: grepped `corpus_toolkit/config.py`
and the validator modules; there is none). `_held_cfr_parts()` in `src/citation_schemes.py`
gates held-ness on the literal string `"cfr_part"`, so a document whose frontmatter spells
this field `"CFR_PART"`, `"cfr-part"`, or anything else is schema-valid, is served by every
other tool (`get_document`, `search_corpus`), and is refused BY NAME when cited -- the exact
"could not check" reported as "is not there" class #35 exists to close, one field over
(#56).

This is a corpus-local check, not a corpus-toolkit schema feature, because the enum is this
corpus's own convention (`_meta/source-manifest.yml`'s intake note documents the four intake
kinds; `cfr_section` is the fifth, produced by `split_cfr_sections.py`) -- other corpora use
`extra_document_fields` for values with no fixed vocabulary.
"""
from __future__ import annotations

import pathlib
import sys

import yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent
INSTRUMENTS = ROOT / "instruments"

KNOWN_INSTRUMENT_KINDS = {
    "cfr_part",
    "cfr_section",
    "irs_publication",
    "fbi_policy",
    "public_law",
}


def main() -> int:
    fails: list[str] = []

    def check(desc: str, ok: bool, detail: str = "") -> None:
        print(f"  {'ok  ' if ok else 'FAIL'}  {desc}")
        if not ok:
            fails.append(f"{desc}{': ' + detail if detail else ''}")

    paths = sorted(INSTRUMENTS.glob("*.md"))
    if not paths:
        check(f"instruments found under {INSTRUMENTS}", False, "no documents found")
    for path in paths:
        head = path.read_text(encoding="utf-8").split("---", 2)
        if len(head) < 3:
            check(f"{path.name}: has frontmatter", False)
            continue
        fm = yaml.safe_load(head[1]) or {}
        doc_id = fm.get("id", path.stem)
        kind = fm.get("instrument_kind")
        check(
            f"{doc_id}: instrument_kind {kind!r} is one of "
            f"{sorted(KNOWN_INSTRUMENT_KINDS)}",
            kind in KNOWN_INSTRUMENT_KINDS,
            f"{doc_id} declares instrument_kind={kind!r}, which is not a recognized kind "
            f"-- allowed values are {sorted(KNOWN_INSTRUMENT_KINDS)}",
        )

    print()
    if fails:
        print(f"FAILED: {len(fails)} assertion(s): {'; '.join(fails)}", file=sys.stderr)
        return 1
    print("Every document's instrument_kind is one of the five known values.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
