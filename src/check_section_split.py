#!/usr/bin/env python3
"""Assert the demand-driven section split works for a SECOND cfr_part, not just the first.

    python3 src/check_section_split.py

Run in CI (`generated` job, alongside check_citations.py, check_issuing_body.py and
check_extraction.py).

WHY THIS EXISTS. #34 generalized four files away from a literal "2 CFR 200": the citation
scanner's regexes (src/scan_cited_sections.py), the section splitter's part id, fetch URL,
and heading regexes (src/split_cfr_sections.py), the provenance slicer's document-id pattern
(src/slicing.py), and the part-document edge builder (src/ingest_instruments.py). #34's own
queued instrument (6 CFR 37, per its addendum on #33) is not ingested yet, so -- exactly as
#35 did for citation_schemes.py -- every assertion below is a SYNTHETIC second part, built
and torn down in a temp directory or by direct monkeypatch, never touching the real corpus.
Regenerating 2 CFR 200 byte-identically (split_cfr_sections.py --check, in the same CI job)
is a no-regression check on the FIRST part; it reads the same whether these four files still
assume there is only one part or not, because 2 CFR 200 is that one part either way. This is
the check that actually exercises a second one, the same reason check_issuing_body.py exists
for #33.
"""
from __future__ import annotations

import pathlib
import sys
import tempfile

import yaml

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import ingest_instruments  # noqa: E402
import scan_cited_sections as scanner  # noqa: E402
import slicing  # noqa: E402
import split_cfr_sections as splitter  # noqa: E402
from cfr_consolidations import CONSOLIDATIONS  # noqa: E402

fails: list[str] = []


def check(desc: str, ok: bool, detail: str = "") -> None:
    print(f"  {'ok  ' if ok else 'FAIL'}  {desc}")
    if not ok:
        fails.append(f"{desc}{': ' + detail if detail else ''}")


def main() -> int:
    # --- scan_cited_sections.patterns(): built per (title, part), not hardcoded to 200 -----
    sec_re, short_re, part_re = scanner.patterns(6, 37)
    text_full = "Under 6 CFR 37.72, agencies must post notice. §37.73 also applies."
    check("full form matches the anchor citation for a second part",
          sec_re.findall(text_full) == ["72"], f"got {sec_re.findall(text_full)!r}")
    check("short form matches the bare § continuation for the same second part",
          short_re.findall(text_full) == ["73"], f"got {short_re.findall(text_full)!r}")
    check("the second part's part_re licenses its own short form",
          bool(part_re.search(text_full)), "part_re did not match its own part citation")

    # A bare short form must not leak across parts -- a scan for (2, 200) must not count a
    # bare §37.NN, and one for (6, 37) must not count a bare §200.NN naming a different part.
    sec200_re, short200_re, part200_re = scanner.patterns(2, 200)
    text_37_only = "6 CFR 37.72 is the anchor. §37.73 elsewhere in the same file."
    check("a (2, 200) scan finds nothing in a file that only cites 6 CFR 37",
          not sec200_re.findall(text_37_only) and not part200_re.search(text_37_only),
          f"sec={sec200_re.findall(text_37_only)!r}")

    # The disambiguation guard: a bare short form with NO full citation anywhere in the file
    # must not be counted -- this is the ORS-collision guard from ADR-0003, and #27's own
    # triage found it is not marginal for every part (45 CFR 164 collides with ORS chapter
    # 164, the MORE common meaning of a bare `164.NNN`). Proven here for the general
    # mechanism, independent of which part.
    text_bare_only = "See §37.72 for the notice requirement."
    hits = short_re.findall(text_bare_only) if part_re.search(text_bare_only) else []
    check("a bare short form with no full citation in the file is not licensed",
          hits == [], f"got {hits}")

    # --- slicing.slice(): DOC_ID pattern generalized from a literal 2-cfr-200 -------------
    raw37 = "### 37.72 Notice.\nsection 72 text\n### 37.73 Recordkeeping.\nsection 73 text\n"
    got = slicing.slice("6-cfr-37.72", "6-cfr-37", raw37)
    check("a second part's section slices to ONLY its own span, not the whole snapshot",
          got == "### 37.72 Notice.\nsection 72 text\n" and got != raw37,
          f"got {got!r}")
    check("the bare second-part id (no section) owns its whole snapshot",
          slicing.slice("6-cfr-37", "6-cfr-37", raw37) == raw37, "bare part id was sliced")
    raw200 = "### 200.303 Internal controls.\nfoo\n### 200.304 Bar.\nbaz\n"
    check("2 CFR 200 sections still slice correctly (no regression)",
          slicing.slice("2-cfr-200.303", "2-cfr-200", raw200)
          == "### 200.303 Internal controls.\nfoo\n",
          "regression in the first part's slicing")

    # --- split_cfr_sections.sections_from() / subject(): parameterized by `part` -----------
    xml37 = (
        b'<PART><SECTION TYPE="SECTION" N="37.72"><HEAD>&#167; 37.72 Notice.</HEAD>'
        b'<P>Agencies shall post notice.</P></SECTION>'
        b'<SECTION TYPE="SECTION" N="37.99"><HEAD>&#167; 37.99 Repealed rule.</HEAD>'
        b'<P>text.</P></SECTION></PART>'
    )
    secs = splitter.sections_from(xml37, "37")
    check("sections_from() keys a second part's sections by ITS OWN part number",
          set(secs) == {"37.72", "37.99"}, f"got {sorted(secs)}")
    check("sections_from() does not also pick up a DIFFERENT part's numbering",
          "200.72" not in secs and "72" not in secs, f"got {sorted(secs)}")
    subj = splitter.subject(secs["37.72"][0], "37")
    check("subject() strips the second part's own prefix, not 200's",
          subj == "Notice", f"got {subj!r}")

    # --- split_cfr_sections.build(): the second part must not inherit the first's facts ----
    ctx37 = splitter.PartCtx(
        part_id="6-cfr-37", title="6", part="37",
        part_title="Nondiscrimination on the Basis of Disability Fixture Act",
        issuing_body="Department of Justice",
        part_as_of="2026-01-01", part_retrieved="2026-01-02")
    meta = {"citations": 5, "cited_in": ["audits"]}
    live_doc = splitter.build(ctx37, "37.72", secs["37.72"][0], secs["37.72"][1], meta,
                               sha="deadbeef", amended_on=None, superseded_by=None)
    fm = yaml.safe_load(live_doc.split("---")[1])
    check("a second part's section document declares ITS OWN issuing_body, not OMB's",
          fm["issuing_body"] == "Department of Justice", f"got {fm['issuing_body']!r}")
    check("a second part's section document id is prefixed with ITS OWN part id",
          fm["id"] == "6-cfr-37.72", f"got {fm['id']!r}")
    check("a second part's section citation reads '6 CFR 37.72', not '2 CFR ...'",
          fm["citation"] == "6 CFR 37.72", f"got {fm['citation']!r}")
    check("the 'At a glance' Part line names the second part's OWN manifest title",
          "6 CFR 37 — Nondiscrimination on the Basis of Disability Fixture Act" in live_doc,
          "manifest title not found in body")
    check("the 'At a glance' Part line does not carry over 2 CFR 200's own text",
          "Uniform Guidance" not in live_doc and "2 CFR 200" not in live_doc,
          "first part's text leaked into the second part's document")

    # --- removed-section prose: consolidation record present, WITH scope -------------------
    saved = dict(CONSOLIDATIONS)
    try:
        CONSOLIDATIONS["6-cfr-37"] = {"date": "2024-05-01", "into": "37.5",
                                       "scope": "Subpart X's grievance procedures"}
        removed_doc = splitter.build(
            ctx37, "37.99", secs["37.99"][0], secs["37.99"][1],
            {"citations": 2, "cited_in": ["erf"], "removed_on": "2024-05-01"},
            sha="cafebabe", amended_on="2024-05-01",
            superseded_by="6-cfr-37.5",
            hist=splitter.HistCtx(hist_id="6-cfr-37-2024-04-30",
                                  hist_url="https://example.invalid/hist",
                                  hist_retrieved="2026-01-03",
                                  last_in_force="2024-04-30"),
            consolidation=CONSOLIDATIONS["6-cfr-37"])
        check("a removed section with a recorded scope names WHAT moved, for ITS OWN part",
              "Subpart X's grievance procedures were consolidated into [§ 37.5]" in removed_doc,
              "expected consolidation clause not found")
        check("it does not fabricate 2 CFR 200's own Subpart A note",
              "Subpart A" not in removed_doc, "2 CFR 200's own scope text leaked in")

        # --- removed-section prose: NO consolidation record for this part at all ------------
        removed_doc_bare = splitter.build(
            ctx37, "37.98", "§ 37.98 Another repealed rule.", "### § 37.98\ntext.",
            {"citations": 1, "cited_in": ["erf"], "removed_on": "2024-05-01"},
            sha="babecafe", amended_on="2024-05-01",
            superseded_by="6-cfr-37",  # falls back to the part itself -- no specific target
            hist=splitter.HistCtx(hist_id="6-cfr-37-2024-04-30",
                                  hist_url="https://example.invalid/hist",
                                  hist_retrieved="2026-01-03",
                                  last_in_force="2024-04-30"),
            consolidation=None)
        check("a removed section with NO consolidation record does not fabricate one",
              "consolidated" not in removed_doc_bare.lower()
              and "drop-in replacement" not in removed_doc_bare,
              "invented a consolidation target with nothing recorded")
        check("...but still states plainly that the section is gone",
              "no longer exists" in removed_doc_bare, "removal was not stated")
    finally:
        CONSOLIDATIONS.clear()
        CONSOLIDATIONS.update(saved)

    # --- ingest_instruments.cited_section_ids(): per-part file, not the one global path ----
    saved_root = ingest_instruments.ROOT
    tmp = tempfile.TemporaryDirectory()
    try:
        scratch = pathlib.Path(tmp.name)
        (scratch / "_meta" / "cited-sections").mkdir(parents=True)
        (scratch / "_meta" / "cited-sections" / "6-cfr-37.yml").write_text(
            "current:\n  - section: \"37.72\"\n"
            "removed:\n  - section: \"37.99\"\n",
            encoding="utf-8")
        ingest_instruments.ROOT = scratch

        ids = ingest_instruments.cited_section_ids("6-cfr-37")
        check("cited_section_ids() reads the SECOND part's own file, not 2-cfr-200's",
              ids == ["6-cfr-37.72", "6-cfr-37.99"], f"got {ids}")

        ids_missing = ingest_instruments.cited_section_ids("9-cfr-1")
        check("a part with no cited-sections file yet returns [] rather than raising",
              ids_missing == [], f"got {ids_missing}")

        # The call-site gate in build(): keyed on instrument_kind == 'cfr_part', not on the
        # literal id "2-cfr-200" -- #34's own bug, one field over from #33's. Exercised
        # through build() itself (no file I/O of its own; extraction happens in main()).
        src37 = {"id": "6-cfr-37", "title": "Disability Fixture Act",
                 "citation": "6 CFR 37", "instrument_kind": "cfr_part",
                 "issuing_body": "Department of Justice",
                 "url": "https://example.invalid/title-6/part-37.xml", "format": "xml",
                 "reproduction_basis": "17 U.S.C. § 105"}
        part_doc = ingest_instruments.build(
            src37, "full text of the part", "sha000", {"pages": 1}, None,
            "2026-01-01", "2026-01-02")
        part_fm = yaml.safe_load(part_doc.split("---")[1])
        check("a second cfr_part document carries relationships to ITS OWN split sections",
              part_fm.get("relationships", {}).get("related") == ["6-cfr-37.72", "6-cfr-37.99"],
              f"got {part_fm.get('relationships')}")

        # A non-cfr_part kind must NOT gain a relationships block from this same code path.
        src_pdf = {"id": "irs-pub-9999", "title": "Fixture Publication",
                   "citation": "IRS Pub 9999", "instrument_kind": "irs_publication",
                   "url": "https://example.invalid/pub9999.pdf", "format": "pdf",
                   "reproduction_basis": "17 U.S.C. § 105"}
        pdf_doc = ingest_instruments.build(
            src_pdf, "full text", "sha111", {"pages": 1}, "01-2026",
            "2026-01-01", "2026-01-02")
        pdf_fm = yaml.safe_load(pdf_doc.split("---")[1])
        check("a non-cfr_part kind gets no relationships from the section-edge gate",
              "relationships" not in pdf_fm, f"got {pdf_fm.get('relationships')}")
    finally:
        ingest_instruments.ROOT = saved_root
        tmp.cleanup()

    print()
    if fails:
        print(f"FAILED: {len(fails)} assertion(s): {'; '.join(fails)}", file=sys.stderr)
        return 1
    print("A second cfr_part splits, slices, and links correctly -- none of it inherited from "
          "2 CFR 200.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
