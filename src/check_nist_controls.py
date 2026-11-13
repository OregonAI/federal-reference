#!/usr/bin/env python3
"""Tests for the NIST SP 800-53 intake (#42): citation ids, scan, anchors, slicing, splitting.

    python3 src/check_nist_controls.py

Run in CI (`generated` job). Same shape as check_section_split.py / check_citations.py:
mostly NEGATIVE assertions (a Rev. 4 citation must not be answered by Rev. 5 text), each
written and watched FAIL before the code that satisfies it existed.
"""
from __future__ import annotations

import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "src"))

FAILS: list[str] = []


def check(desc: str, ok: bool, detail: str = "") -> None:
    print(f"  {'ok  ' if ok else 'FAIL'}  {desc}")
    if not ok:
        FAILS.append(f"{desc}{': ' + detail if detail else ''}")


def test_federal_ids() -> None:
    """The cross-corpus contract: a sibling derives an id from the citation string alone."""
    from federal_ids import candidates

    pub = "nist-sp-800-53-r5"
    check("Rev. 5 names the held publication",
          candidates("NIST SP 800-53 Rev. 5") == [pub], str(candidates("NIST SP 800-53 Rev. 5")))
    check("a control derives the control document, not the publication",
          candidates("NIST SP 800-53 Rev. 5 AC-2") == [f"{pub}.ac-2"],
          str(candidates("NIST SP 800-53 Rev. 5 AC-2")))
    check("an enhancement derives its BASE control (it lives inside it)",
          candidates("SP 800-53 Rev. 5, AC-2(1)") == [f"{pub}.ac-2"],
          str(candidates("SP 800-53 Rev. 5, AC-2(1)")))
    check("a control list derives every control",
          candidates("NIST 800-53 Rev. 5, AC-1, AT-1 and AU-1")
          == [f"{pub}.ac-1", f"{pub}.at-1", f"{pub}.au-1"],
          str(candidates("NIST 800-53 Rev. 5, AC-1, AT-1 and AU-1")))
    check("Revision / Rev / r5 spellings all name revision 5",
          all(candidates(s) == [pub] for s in (
              "NIST SP 800-53, Revision 5", "NIST SP 800-53 Rev 5", "SP 800-53r5",
              "NIST Special Publication 800-53 Rev.5")),
          str([candidates(s) for s in ("NIST SP 800-53, Revision 5", "SP 800-53r5")]))
    check("Rev. 4 derives an id that is NOT the Rev. 5 id (a correct miss, never a substitution)",
          candidates("NIST Special Publication 800-53 rev. 4 AC-2") == ["nist-sp-800-53-r4.ac-2"],
          str(candidates("NIST Special Publication 800-53 rev. 4 AC-2")))
    check("an unversioned citation derives nothing (the sibling cannot pick a revision)",
          candidates("NIST SP 800-53") == [] and candidates("NIST SP 800-53 AC-2") == [])
    check("800-53A / 800-53B are different publications and derive nothing",
          candidates("NIST SP 800-53B") == [] and candidates("NIST SP 800-53A Rev. 5") == []
          and candidates("SP 800-53B, Rev. 5") == [])
    check("a bare `800-53 Rev. 5` (no NIST/SP prefix, as 6 CFR 37 prints it) names Rev. 5",
          candidates("800-53 Rev. 5") == [pub] and candidates("x800-53 Rev. 5") == [])
    check("CSF subcategories (PR.AC-3) and CJIS's own `IA-0` heading are not controls",
          candidates("NIST SP 800-53 Rev. 5 PR.AC-3, IA-0, AC-2") == [f"{pub}.ac-2"],
          str(candidates("NIST SP 800-53 Rev. 5 PR.AC-3, IA-0, AC-2")))
    check("a control list stops at the next publication named",
          candidates("NIST SP 800-53 Rev. 5 AC-2 and FIPS 140-3 SC-13") == [f"{pub}.ac-2"],
          str(candidates("NIST SP 800-53 Rev. 5 AC-2 and FIPS 140-3 SC-13")))
    check("a release number (5.2.0) is not the held edition and derives nothing",
          candidates("NIST SP 800-53 Rev. 5.2.0") == [])


# --- the synthetic publication every later check runs against -----------------------------
# Shaped like the real extracted SP 800-53 Rev. 5 text, including each hazard measured on it:
#   * a control-looking heading BEFORE the catalog (the Figure 1 example, `AU-4 ...`)
#   * a double space after the id (`SC-7  BOUNDARY PROTECTION`; pypdf emits this for 7 controls)
#   * a withdrawn control with no body
#   * a prefix-sharing id (`AC-2` vs `AC-20`)
#   * the Appendix C summary table, whose lines start with the same ids in mixed case
#   * the line `REFERENCES` that closes the catalog (the last control would otherwise run to EOF)
FIXTURE = """FIGURE 1: CONTROL STRUCTURE
AU-4 AUDIT STORAGE CAPACITY
Control: example only.
CHAPTER THREE THE CONTROLS
AC-1 POLICY AND PROCEDURES
Control: a. Develop policy.
Related Controls:  IA-1, PM-9.
AC-2 ACCOUNT MANAGEMENT
Control: a. Define account types.
Control Enhancements:
(1) ACCOUNT MANAGEMENT | AUTOMATED SYSTEM ACCOUNT MANAGEMENT
Support automated mechanisms.
AC-13 SUPERVISION AND REVIEW \u2014 ACCESS CONTROL
[Withdrawn: Incorporated into AC-2 and AU-6.]
AC-20 USE OF EXTERNAL SYSTEMS
Control: a. Establish terms.
SC-7  BOUNDARY PROTECTION
Control: a. Monitor communications.
SR-12 COMPONENT DISPOSAL
Control: Dispose of components.
REFERENCES
[OMB A-130] Circular A-130.
APPENDIX C CONTROL SUMMARIES
AC-1 Policy and Procedures O
AC-2 Account Management O
"""


def test_scan() -> None:
    from nist_controls import scan_text

    base, enh = scan_text("Use AC-2, AC-2(1), AC-2(1) and SC-7(3); not PR.AC-3, IA-0, XX-1, AC-2x.")
    check("scan counts base controls, folding enhancements into their base",
          dict(base) == {"ac-2": 3, "sc-7": 1}, str(dict(base)))
    check("scan keeps enhancement counts separately",
          dict(enh) == {"ac-2(1)": 2, "sc-7(3)": 1}, str(dict(enh)))
    check("scan ignores CSF subcategories, the `-0` heading, non-families",
          "ac-3" not in base and "ia-0" not in base and "xx-1" not in base)


def _anchored(text: str) -> list[str]:
    from anchor_sections import RULES, anchor_text

    rule = RULES["nist-sp-800-53-r5"]
    out, _ = anchor_text(text, rule["match"], rule.get("region"))
    return [l for l in out.splitlines() if l.startswith("### ")]


def test_anchors() -> None:
    got = _anchored(FIXTURE)
    check("only catalog controls are anchored, plus the REFERENCES line that closes the catalog",
          got == ["### AC-1 POLICY AND PROCEDURES", "### AC-2 ACCOUNT MANAGEMENT",
                  "### AC-13 SUPERVISION AND REVIEW \u2014 ACCESS CONTROL",
                  "### AC-20 USE OF EXTERNAL SYSTEMS", "### SC-7  BOUNDARY PROTECTION",
                  "### SR-12 COMPONENT DISPOSAL", "### REFERENCES"], str(got))
    check("the Figure 1 example before the catalog is not anchored",
          "### AU-4 AUDIT STORAGE CAPACITY" not in got)
    check("Appendix C's mixed-case summary lines are not anchored",
          "### AC-1 Policy and Procedures O" not in got)
    again = "\n".join(_anchored(FIXTURE))
    from anchor_sections import RULES, anchor_text
    rule = RULES["nist-sp-800-53-r5"]
    once, _ = anchor_text(FIXTURE, rule["match"], rule.get("region"))
    twice, n2 = anchor_text(once, rule["match"], rule.get("region"))
    check("anchoring is idempotent", twice == once and n2 == 0)
    check("anchoring adds no words (strip the prefix and the text is the original)",
          once.replace("### ", "") == FIXTURE)


def test_slicing() -> None:
    from anchor_sections import RULES, anchor_text
    import slicing

    rule = RULES["nist-sp-800-53-r5"]
    raw, _ = anchor_text(FIXTURE, rule["match"], rule.get("region"))
    pub = "nist-sp-800-53-r5"

    def sl(cid):
        return slicing.slice(f"{pub}.{cid}", pub, raw)

    ac2 = sl("ac-2")
    check("a control slice runs from its heading to the next heading",
          ac2.startswith("### AC-2 ACCOUNT MANAGEMENT") and "(1) ACCOUNT MANAGEMENT" in ac2
          and ac2.rstrip().endswith("Support automated mechanisms."), repr(ac2[-80:]))
    check("`ac-2` does not also match AC-20 or AC-13", "AC-20" not in ac2 and "AC-13" not in ac2)
    check("`ac-2` slice does not start at a prefix-sharing heading",
          sl("ac-20").startswith("### AC-20 ") and "AC-2 ACCOUNT" not in sl("ac-20"))
    check("the double-space heading (SC-7  BOUNDARY PROTECTION) is found",
          sl("sc-7").startswith("### SC-7  BOUNDARY PROTECTION"))
    sr12 = sl("sr-12")
    check("the last control stops at the REFERENCES anchor, not end of file",
          "Dispose of components." in sr12 and "OMB A-130" not in sr12
          and "APPENDIX C" not in sr12, repr(sr12))
    check("a withdrawn control is a slice of its own (heading + withdrawal notice)",
          sl("ac-13").strip().splitlines()[-1].startswith("[Withdrawn:"))
    check("the publication itself owns its whole snapshot",
          slicing.slice(pub, pub, raw) == raw)
    check("the CFR slicer is unaffected", slicing.slice("6-cfr-37", "6-cfr-37", "x") == "x")
    try:
        sl("pm-99")
        check("a control with no heading raises rather than widening to the whole text", False)
    except LookupError:
        check("a control with no heading raises rather than widening to the whole text", True)


def main() -> int:
    test_federal_ids()
    test_scan()
    test_anchors()
    test_slicing()
    print()
    if FAILS:
        print(f"FAILED: {len(FAILS)} assertion(s):\n  " + "\n  ".join(FAILS), file=sys.stderr)
        return 1
    print("NIST control intake checks passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
