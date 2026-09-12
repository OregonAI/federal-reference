#!/usr/bin/env python3
"""Assert every document's `instrument_kind` is one of this corpus's known values.

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
kinds; `cfr_section` is the fifth, produced by `split_cfr_sections.py`; `usc_section` is the
sixth, ADR-0006's U.S. Code sections Oregon cites) -- other corpora use
`extra_document_fields` for values with no fixed vocabulary.

ALSO CHECKED HERE: every `usc_section` document declares a non-empty `currency` (OLRC's own
"current through Pub. L. N" stamp -- ADR-0006's deliberate exception to *version is
identity*, since a U.S.C. section has no siblings to disambiguate, only a history). A
document whose `currency` is missing or empty is schema-valid and silently uncurrent -- the
same "could not check" class this file already exists to close, one field over.

NON-VACUITY OF THE CURRENCY RULE IS NOT THIS SCRIPT'S JOB. It iterates documents that
exist, so with zero usc_section documents it would pass by saying nothing. The corpus-level
"at least one usc_section is held" assertion -- the one that keeps the refusal's derived
count from agreeing with zero -- lives in check_citations.py, where it can also see the
refusal it protects.
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
    "usc_section",
    # #95: security and doctrine instruments that are none of the above -- CMS's ARC-AMPE,
    # CISA's CPGs, and the others the operator admitted under `signal: named`. Deliberately
    # ONE broad kind rather than one per issuer: the issuer is already declared per entry
    # (ingest_instruments.ISSUER_IS_PER_ENTRY), so a kind per publisher would encode the
    # issuer twice and still have to be read from the manifest. It is also the first kind
    # that spans formats, which is why extraction consults `format` for it.
    "agency_guidance",
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
        if kind == "usc_section":
            currency = fm.get("currency")
            check(
                f"{doc_id}: usc_section declares a non-empty currency",
                bool(currency),
                f"{doc_id} is a usc_section with currency={currency!r} -- ADR-0006 requires "
                f"OLRC's own 'current through Pub. L. N' stamp on every usc_section document",
            )

    print()
    if fails:
        print(f"FAILED: {len(fails)} assertion(s): {'; '.join(fails)}", file=sys.stderr)
        return 1
    print(f"Every document's instrument_kind is one of the "
          f"{len(KNOWN_INSTRUMENT_KINDS)} known values.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
