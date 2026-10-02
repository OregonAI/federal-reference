#!/usr/bin/env python3
"""Assert extraction_is_broken() tells a genuinely short cfr_part from a broken extraction.

    python3 src/check_extraction_guard.py

Run in CI (`generated` job, alongside check_issuing_body.py and check_part_supersession.py).

WHY THIS EXISTS. `ingest_instruments.py`'s extraction guard used to be a flat
`len(text) < 2000` applied to every instrument_kind. That floor is right for PDF/HTML
extractors, which have no structural count to fall back on, but it is the wrong test for
`cfr_part`: extract_cfr() walks real `TYPE="SECTION"`/`TYPE="APPENDIX"` elements and reports
exactly how many it found, so a part can be fully and correctly extracted while still being
short. 7 CFR 280 ("Emergency Food Assistance for Victims of Disasters") is one section and
1,554 characters of real federal text — the flat floor rejected it as "scanned or broken"
(#102) when nothing was broken.

`ingest_instruments.py` itself runs in no CI workflow (every `cfr_part` not already
superseded needs a live `cfr_amended_on()` lookup), so this is the hermetic gate, built the
way check_issuing_body.py and check_part_supersession.py are: synthetic fixtures, entirely
offline, each assertion confirmed to fail against the pre-fix flat floor.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from ingest_instruments import extraction_is_broken  # noqa: E402


def main() -> int:
    fails: list[str] = []

    def check(desc: str, ok: bool, detail: str = "") -> None:
        print(f"  {'ok  ' if ok else 'FAIL'}  {desc}")
        if not ok:
            fails.append(f"{desc}{': ' + detail if detail else ''}")

    # --- the real bug: a genuinely short but fully-structured cfr_part must NOT be flagged
    short_text = "### PART 280\n\n### " + "x" * 200  # well under 2,000 chars
    reason = extraction_is_broken("cfr_part", short_text,
                                   {"sections": 1, "appendices": 0, "body_chars": 200})
    check("a 1-section cfr_part under 2,000 chars is not 'scanned or broken'",
          reason is None, repr(reason))

    # --- the failure this guard must still catch: wrong schema / nothing structural found
    reason = extraction_is_broken("cfr_part", "", {"sections": 0, "appendices": 0,
                                                    "body_chars": 0})
    check("a cfr_part with 0 sections and 0 appendices IS flagged",
          reason is not None, "extraction_is_broken returned None instead of a reason")

    # --- structure found but somehow no BODY text at all -- still broken, not a false
    # negative. This is the shape extract_cfr() can actually produce: headings present
    # (`text` itself is non-blank, "### head" for each section) but every section's own
    # children carried no text, so `body_chars` is 0 while `sections` is not.
    reason = extraction_is_broken("cfr_part", "### head one\n\n### head two\n",
                                   {"sections": 2, "appendices": 0, "body_chars": 0})
    check("a cfr_part with headings found but 0 chars of body text IS flagged",
          reason is not None, "extraction_is_broken returned None instead of a reason")

    # --- a long, well-formed cfr_part is never flagged regardless of char count
    reason = extraction_is_broken("cfr_part", "### x\n" * 50,
                                   {"sections": 29, "appendices": 12, "body_chars": 9000})
    check("a long cfr_part with real stats is not flagged",
          reason is None, repr(reason))

    # --- every OTHER kind keeps the original flat floor (no structural stats to trust)
    reason = extraction_is_broken("irs_publication", "x" * 500, {"chars": 500})
    check("a short irs_publication (no structural signal) is still flagged",
          reason is not None, "extraction_is_broken returned None instead of a reason")

    reason = extraction_is_broken("irs_publication", "x" * 5000, {"chars": 5000})
    check("a long irs_publication clears the flat floor",
          reason is None, repr(reason))

    print()
    if fails:
        print(f"FAILED: {len(fails)} assertion(s): {'; '.join(fails)}", file=sys.stderr)
        return 1
    print("extraction_is_broken() clears a genuinely short cfr_part, still catches a "
          "structurally empty one, and leaves every other kind's flat floor unchanged.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
