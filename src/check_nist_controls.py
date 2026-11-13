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
(2) ACCOUNT MANAGEMENT | USAGE CONDITIONS
[Withdrawn: Incorporated into AC-2k.]
AC-13 SUPERVISION AND REVIEW \u2014 ACCESS CONTROL
[Withdrawn: Incorporated into AC-2 and AU-6.]
AC-20 USE OF EXTERNAL SYSTEMS
Control: a. Establish terms.
SC-7  BOUNDARY PROTECTION
Control: a. Monitor communications.
SR-12 COMPONENT DISPOSAL
Control: Dispose of components.
REFERENCES   PAGE 374
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
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
          and ac2.rstrip().endswith("[Withdrawn: Incorporated into AC-2k.]"), repr(ac2[-80:]))
    check("`ac-2` does not also match AC-20 or AC-13", "AC-20" not in ac2 and "AC-13" not in ac2)
    check("`ac-2` slice does not start at a prefix-sharing heading",
          sl("ac-20").startswith("### AC-20 ") and "AC-2 ACCOUNT" not in sl("ac-20"))
    check("the double-space heading (SC-7  BOUNDARY PROTECTION) is found",
          sl("sc-7").startswith("### SC-7  BOUNDARY PROTECTION"))
    sr12 = sl("sr-12")
    check("the last control stops at the REFERENCES anchor, not end of file",
          "Dispose of components." in sr12 and "OMB A-130" not in sr12
          and "APPENDIX C" not in sr12, repr(sr12))
    from nist_controls import held_scope
    scoped, _ = anchor_text(held_scope(FIXTURE), rule["match"], rule.get("region"))
    sr12s = slicing.slice(f"{pub}.sr-12", pub, scoped)
    check("on the held (scoped) text the last control ends at the end of the text",
          sr12s.rstrip().endswith("Dispose of components.") and "REFERENCES" not in sr12s,
          repr(sr12s))
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


def _synthetic_parent():
    from anchor_sections import RULES, anchor_text

    rule = RULES["nist-sp-800-53-r5"]
    from nist_controls import held_scope
    text, _ = anchor_text(held_scope(FIXTURE), rule["match"], rule.get("region"))
    fm = {"id": "nist-sp-800-53-r5", "version": "Rev. 5", "as_of": "2026-11-12",
          "retrieved": "2026-11-12", "amended_on": "2025-08-27", "source_sha256": "ab" * 32,
          "source_url": "https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-53r5.pdf",
          "issuing_body": "National Institute of Standards and Technology",
          "reproduction_basis": "basis under test"}
    cited = {"controls": [
        {"id": "ac-2", "control": "AC-2", "citations": 5, "enhancement_citations": 2,
         "documents": {"cjis-sp-6-1": 3, "6-cfr-37": 2}},
        {"id": "ac-13", "control": "AC-13", "citations": 1, "enhancement_citations": 0,
         "documents": {"cjis-sp-6-1": 1}},
        {"id": "sc-7", "control": "SC-7", "citations": 2, "enhancement_citations": 0,
         "documents": {"6-cfr-37": 2}},
        {"id": "ac-1", "control": "AC-1", "citations": 1, "enhancement_citations": 0,
         "documents": {"6-cfr-37": 1}},
        {"id": "pm-99", "control": "PM-99", "citations": 1, "enhancement_citations": 0,
         "documents": {"6-cfr-37": 1}},
    ]}
    release = {"release": "5.2.0", "issued": "2025-08-27",
               "source_url": "https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final",
               "changes_summary_url": "https://csrc.nist.gov/files/example-changes.pdf",
               "new_controls_or_enhancements": [], "revised": [],
               "discussion_updated": ["ac-2", "ac-2(1)"], "related_controls_updated": [],
               "related_controls_updated_all_dash_01": True}
    return fm, text, cited, release


def test_split() -> None:
    import yaml
    import slicing
    from split_nist_controls import build_documents

    fm, text, cited, release = _synthetic_parent()
    docs, missing = build_documents(fm, text, cited, release)
    pub = "nist-sp-800-53-r5"
    check("one document per cited control that the catalog has",
          set(docs) == {f"{pub}.{c}" for c in ("ac-1", "ac-2", "ac-13", "sc-7")}, str(sorted(docs)))
    check("a cited id the catalog lacks is REPORTED, not written and not dropped silently",
          missing == ["pm-99"], str(missing))

    def parts(md):
        _, head, body = md.split("---\n", 2)
        return yaml.safe_load(head), body

    f, body = parts(docs[f"{pub}.ac-2"])
    check("frontmatter: identity", f["id"] == f"{pub}.ac-2"
          and f["citation"] == "NIST SP 800-53 Rev. 5 AC-2" and f["version"] == "Rev. 5"
          and f["instrument_kind"] == "nist_control" and f["doc_type"] == "federal_instrument"
          and f["title"] == "NIST SP 800-53 Rev. 5 AC-2 \u2014 ACCOUNT MANAGEMENT", str(f))
    check("frontmatter: provenance is the publication's, shared via snapshot_id",
          f["snapshot_id"] == pub and f["source_sha256"] == fm["source_sha256"]
          and f["source_url"] == fm["source_url"] and f["as_of"] == "2026-11-12"
          and f["amended_on"] == "2025-08-27" and f["source_format"] == "pdf", str(f))
    check("frontmatter: verbatim, current, related to the publication, never self-verified",
          f["content_mode"] == "verbatim" and f["status"] == "current"
          and f["relationships"] == {"related": [pub]}
          and f["last_verified"] == "" and f["verified_by"] == "", str(f))
    check("frontmatter: the reproduction basis is the publication's own determination",
          f["reproduction_basis"] == "basis under test")
    full = body.split("## Full text\n\n", 1)[1].rstrip("\n")
    check("Full text is EXACTLY the slice of the snapshot (verbatim, nothing added)",
          full == slicing.slice(f"{pub}.ac-2", pub, text).rstrip("\n"), repr(full[-60:]))
    check("the NON-AUTHORITATIVE disclaimer is present", "NON-AUTHORITATIVE" in body)
    check("demand is stated as counts per citing document, not adjectives",
          "5 time" in body and "cjis-sp-6-1" in body and "6-cfr-37" in body)
    check("release 5.2.0 caveat names the control NIST lists and says the held text lacks it",
          "5.2.0" in body and "does NOT include" in body)
    _, sc7 = parts(docs[f"{pub}.sc-7"])
    check("a control NIST does not list gets no 5.2.0 caveat", "5.2.0" not in sc7)
    _, ac1 = parts(docs[f"{pub}.ac-1"])
    check("`All -01 controls` puts the related-controls caveat on every -1 control",
          "5.2.0" in ac1 and "related controls" in ac1.lower())
    _, ac13 = parts(docs[f"{pub}.ac-13"])
    check("a control with a withdrawn ENHANCEMENT is not itself marked withdrawn",
          "withdrawn" not in parts(docs[f"{pub}.ac-2"])[1].split("## Full text")[0].lower())
    check("a withdrawn control says so, from the notice the source prints",
          "withdrawn" in ac13.lower().split("## full text")[0])
    check("no line of any Full text starts with `## ` (the toolkit would truncate there)",
          all(not l.startswith("## ") for d in docs.values()
              for l in d.split("## Full text\n\n", 1)[1].splitlines()))


def test_derive() -> None:
    from nist_controls import catalog_ids
    from scan_cited_controls import derive

    fm, text, _, _ = _synthetic_parent()
    cat = catalog_ids(text)
    check("catalog ids are the anchored control headings (not REFERENCES, not Appendix C)",
          cat == {"ac-1", "ac-2", "ac-13", "ac-20", "sc-7", "sr-12"}, str(sorted(cat)))

    held = {
        "a": ("agency_guidance", "NIST SP 800-53 Rev. 5: AC-2, AC-2(1), AC-2, SC-7 and PM-99; "
                                 "CSF PR.AC-3 is not a control."),
        "b": ("cfr_part", "no mention of the publication here, but AC-20 appears."),
        "c": ("nist_control", "NIST SP 800-53 AC-1 AC-1 AC-1 is the publication talking to itself."),
        "d": ("fbi_policy", "Per 800-53: AC-1; also AC-2(3)."),
    }
    out = derive(held, cat)
    byid = {c["id"]: c for c in out["controls"]}
    check("only documents that mention 800-53 are scanned, and never the NIST documents",
          out["documents_scanned"] == ["a", "d"], str(out["documents_scanned"]))
    check("base counts fold enhancements in; per-document counts are kept",
          byid["ac-2"]["citations"] == 4 and byid["ac-2"]["documents"] == {"a": 3, "d": 1}
          and byid["ac-2"]["enhancement_citations"] == 2, str(byid.get("ac-2")))
    check("a control only a non-mentioning document cites is not demanded",
          "ac-20" not in byid and "ac-1" in byid and byid["ac-1"]["citations"] == 1)
    check("CSF subcategories are not demand", "ac-3" not in byid)
    check("a token the catalog lacks is reported under not_in_catalog, not demanded",
          "pm-99" not in byid and out["not_in_catalog"] == {"pm-99": 1}, str(out["not_in_catalog"]))
    check("controls are in a stable, natural order (ac-1 before ac-2)",
          [c["id"] for c in out["controls"]] == ["ac-1", "ac-2", "sc-7"],
          str([c["id"] for c in out["controls"]]))
    check("totals are the sums of what is listed",
          out["distinct_controls"] == 3 and out["total_citations"] == 6, str(out))


def test_scope() -> None:
    """What the publication document reproduces: front matter through the control catalog."""
    from nist_controls import held_scope

    kept = held_scope(FIXTURE)
    check("the held text ends with the last control and nothing after it -- not even the "
          "REFERENCES page's running header",
          kept.rstrip().endswith("Dispose of components.") and "REFERENCES" not in kept
          and "available free of charge" not in kept
          and "OMB A-130" not in kept and "APPENDIX C" not in kept, repr(kept[-80:]))
    check("the front matter and chapter text before the catalog are kept",
          kept.startswith("FIGURE 1: CONTROL STRUCTURE") and "AC-1 POLICY AND PROCEDURES" in kept)
    check("the kept text is a strict prefix of the extraction (nothing reordered or rewritten)",
          FIXTURE.startswith(kept))
    for desc, bad in (("no catalog at all", "FIGURE 1\nREFERENCES\n"),
                      ("a catalog that never closes", FIXTURE.replace("\nREFERENCES\n", "\n"))):
        try:
            held_scope(bad)
            check(f"{desc} raises rather than holding the whole document", False)
        except ValueError:
            check(f"{desc} raises rather than holding the whole document", True)


def test_extraction_prefix() -> None:
    from check_extraction import prefix_problem

    raw = "a b c REFERENCES x y".split()
    check("a committed text that is exactly the raw prefix up to REFERENCES passes",
          prefix_problem(raw, ["a", "b", "c"]) is None)
    check("a dropped token inside the held span is caught",
          prefix_problem(raw, ["a", "c"]) is not None)
    check("an altered token is caught", prefix_problem(raw, ["a", "B", "c"]) is not None)
    check("a cut that stops early (not at REFERENCES) is caught",
          prefix_problem(raw, ["a", "b"]) is not None)
    check("a cut that runs past REFERENCES is caught",
          prefix_problem(raw, ["a", "b", "c", "REFERENCES"]) is not None)


def test_publication_build() -> None:
    import yaml
    from ingest_instruments import build, resolve_issuing_body
    from nist_controls import held_scope

    nist = "National Institute of Standards and Technology"
    check("both NIST kinds are issued by NIST (a constant of the kind, like irs_publication)",
          resolve_issuing_body({"id": "x", "instrument_kind": "nist_publication"}) == nist
          and resolve_issuing_body({"id": "x", "instrument_kind": "nist_control"}) == nist)
    src = {"id": "nist-sp-800-53-r5", "url": "https://example.test/x.pdf", "format": "pdf",
           "instrument_kind": "nist_publication", "citation": "NIST SP 800-53 Rev. 5",
           "title": "Security and Privacy Controls for Information Systems and Organizations",
           "version": "Rev. 5", "amended_on": "2025-08-27",
           "reproduction_basis": "basis under test"}
    md = build(src, held_scope(FIXTURE), "cd" * 32, {"pages": 492}, "Rev. 5",
               "2026-11-12", "2026-11-12")
    f = yaml.safe_load(md.split("---\n", 2)[1])
    check("the publication document: id carries the revision, citation is not suffixed again",
          f["id"] == "nist-sp-800-53-r5" and f["citation"] == "NIST SP 800-53 Rev. 5"
          and f["version"] == "Rev. 5" and f["issuing_body"] == nist
          and f["instrument_kind"] == "nist_publication", str(f))
    glance = md.split("## Full text", 1)[0]
    check("it says plainly what is held and what is not (front matter + catalog; REFERENCES and "
          "the appendices are not mirrored) so a partial hold is never read as the whole",
          "NOT mirrored" in glance and "Appendix A" in glance and "Chapter Three" in glance,
          glance[-600:])
    check("it carries the release 5.2.0 caveat read from the release file",
          "5.2.0" in glance and "does NOT include" in glance)
    check("the Full text is the scoped text, verbatim",
          md.split("## Full text\n\n", 1)[1].rstrip("\n") == held_scope(FIXTURE))


def test_resolution() -> None:
    """The REAL resolver over the REAL held documents. Mostly refusals: the dangerous answer is
    the plausible wrong one (Rev. 5 text handed back for a Rev. 4 citation)."""
    from corpus_toolkit import config as cfg
    from corpus_toolkit.mcp.framework import CorpusFramework

    fw = CorpusFramework(cfg.load("_meta/corpus.yml"))
    pub = "nist-sp-800-53-r5"

    def resolve(c: str):
        r = fw.resolve_citation(c)
        return [m["id"] for m in r.get("matches", [])], (r.get("note") or "")

    ids, note = resolve("NIST SP 800-53 Rev. 5 AC-2")
    check("a held control resolves to its own document", ids == [f"{pub}.ac-2"], f"{ids} {note}")
    ids, note = resolve("NIST SP 800-53 Rev. 5, AC-1, AT-1")
    check("a list of held controls resolves to each",
          ids == [f"{pub}.ac-1", f"{pub}.at-1"], f"{ids} {note}")
    ids, note = resolve("NIST SP 800-53 Rev. 5 AC-2(1)")
    check("an enhancement resolves to its base control and the note says so",
          ids == [f"{pub}.ac-2"] and "enhancement" in note.lower(), f"{ids} {note}")
    ids, note = resolve("NIST SP 800-53 Rev. 5 AC-2(99)")
    check("an enhancement the Rev. 5 text does not have is NOT answered by the base control",
          ids == [] and "AC-2(99)" in note and "no enhancement" in note.lower(), f"{ids} {note}")
    ids, note = resolve("NIST SP 800-53 Rev. 5 AC-13")
    check("a catalog control with no document of its own resolves to the publication, and the "
          "note names the heading to read",
          ids == [pub] and "### AC-13" in note, f"{ids} {note}")
    ids, note = resolve("NIST SP 800-53 Rev. 5 AC-99")
    check("a control the catalog does not have does NOT resolve, and says so",
          ids == [] and "AC-99" in note and "catalog" in note.lower(), f"{ids} {note}")
    ids, note = resolve("NIST SP 800-53 Rev. 5")
    check("the bare publication resolves to the publication", ids == [pub], f"{ids} {note}")
    ids, note = resolve("NIST SP 800-53")
    check("an unversioned citation resolves WITH a note naming the revision returned",
          ids == [pub] and "no revision" in note and "Rev. 5" in note, f"{ids} {note}")
    for c in ("NIST Special Publication 800-53 rev. 4 AC-2", "NIST SP 800-53 Rev. 4"):
        ids, note = resolve(c)
        check(f"Rev. 4 is NOT answered by Rev. 5 text ({c!r})",
              ids == [] and "Rev. 4" in note and "NOT held" in note, f"{ids} {note}")
    ids, note = resolve("NIST SP 800-53 Rev. 5.2.0 SA-8")
    check("a release number is not answered by the PDF that predates it",
          ids == [] and "5.2.0" in note and "predates" in note, f"{ids} {note}")
    for c in ("NIST SP 800-53B", "NIST SP 800-53A Rev. 5", "NIST SP 800-53B Rev. 5 AC-2"):
        ids, note = resolve(c)
        check(f"a different publication is not answered by 800-53 ({c!r})",
              not any(i.startswith("nist-sp-800-53-r5") for i in ids), f"{ids} {note}")


def main() -> int:
    test_federal_ids()
    test_scan()
    test_anchors()
    test_slicing()
    test_split()
    test_derive()
    test_scope()
    test_extraction_prefix()
    test_publication_build()
    test_resolution()
    print()
    if FAILS:
        print(f"FAILED: {len(FAILS)} assertion(s):\n  " + "\n  ".join(FAILS), file=sys.stderr)
        return 1
    print("NIST control intake checks passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
