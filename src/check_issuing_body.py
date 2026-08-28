#!/usr/bin/env python3
"""Assert resolve_issuing_body() proves the thing #33 actually needed proving.

    python3 src/check_issuing_body.py

Run in CI (`generated` job, alongside check_citations.py and check_extraction.py).

WHY THIS EXISTS. #33's own evidence for its fix was the weaker of two things it needed to
prove. Regenerating 2 CFR 200 byte-identically is a no-regression check on the FIRST part --
it reads the same whether `cfr_part` issuers are still keyed off `instrument_kind` (the bug)
or read per-source (the fix), because 2 CFR 200 is OMB's either way. Nothing before this
script exercised a SECOND part through `resolve_issuing_body()` at all: `ingest_instruments.py`
runs in no CI workflow (grep `.github/` -- it appears only in a comment), and no other
check_*.py reads `issuing_body`. The five ingests #33 exists to unblock (#21, #26, #27, #37,
#41) each hand a real second part through this exact function, so this is that somewhere --
same reason check_citations.py exists for resolution and check_extraction.py exists for
extraction: "mostly negative assertions, each confirmed to fail when the behaviour it guards
is removed."
"""
from __future__ import annotations

import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
from ingest_instruments import ISSUING_BODY_BY_KIND, resolve_issuing_body  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
MANIFEST = ROOT / "_meta" / "source-manifest.yml"


def main() -> int:
    fails: list[str] = []

    def check(desc: str, ok: bool, detail: str = "") -> None:
        print(f"  {'ok  ' if ok else 'FAIL'}  {desc}")
        if not ok:
            fails.append(f"{desc}{': ' + detail if detail else ''}")

    # --- the second part: the one thing "2 CFR 200 regenerates byte-identically" cannot show
    doj = {"id": "check-fixture-doj-part", "instrument_kind": "cfr_part",
           "issuing_body": "Department of Justice"}
    omb = {"id": "check-fixture-omb-part", "instrument_kind": "cfr_part",
           "issuing_body": "Office of Management and Budget"}
    try:
        got_doj, got_omb = resolve_issuing_body(doj), resolve_issuing_body(omb)
        check("a second cfr_part resolves to ITS OWN declared issuer, not the first part's",
              got_doj == "Department of Justice" and got_doj != got_omb,
              f"got {got_doj!r} for the DOJ fixture, {got_omb!r} for the OMB fixture")
    except Exception as e:                                        # noqa: BLE001
        check("a second cfr_part resolves to its own declared issuer", False, repr(e))

    # --- the missing-issuer refusal: must raise, must name the entry, must not default -----
    missing = {"id": "check-fixture-missing-issuer", "instrument_kind": "cfr_part"}
    try:
        resolve_issuing_body(missing)
        check("a cfr_part with no declared issuer raises rather than defaulting", False,
              "resolve_issuing_body returned a value instead of raising")
    except ValueError as e:
        check("a cfr_part with no declared issuer raises ValueError naming the entry",
              "check-fixture-missing-issuer" in str(e), str(e))
    except Exception as e:                                        # noqa: BLE001
        check("a cfr_part with no declared issuer raises ValueError naming the entry", False,
              f"raised {type(e).__name__} instead: {e}")

    # --- the other three kinds stay table-driven, unaffected by the cfr_part special-case ---
    for kind, expected in ISSUING_BODY_BY_KIND.items():
        got = resolve_issuing_body({"id": f"check-fixture-{kind}", "instrument_kind": kind})
        check(f"{kind} still resolves from the per-kind table", got == expected,
              f"got {got!r}, expected {expected!r}")

    # --- every cfr_part manifest entry actually declares one, spelled out per the note ------
    for src in yaml.safe_load(MANIFEST.read_text())["sources"]:
        if src["instrument_kind"] != "cfr_part":
            continue
        body = src.get("issuing_body")
        check(f"{src['id']}: manifest declares issuing_body", bool(body))
        if body:
            check(f"{src['id']}: issuing_body is spelled out, not an all-caps abbreviation",
                  not (body.isupper() and " " not in body), repr(body))

    print()
    if fails:
        print(f"FAILED: {len(fails)} assertion(s): {'; '.join(fails)}", file=sys.stderr)
        return 1
    print("resolve_issuing_body() separates a second cfr_part's issuer from the first's, "
          "refuses one with none declared, and every held cfr_part declares one.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
