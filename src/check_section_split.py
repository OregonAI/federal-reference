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

WHAT ELSE IS PROVED HERE. The file has since taken on a second, unrelated-to-#34 proof: that
a WHOLLY SUPERSEDED part -- one removed from the CFR in its entirety, so its current snapshot
and its last-in-force snapshot are the same bytes -- still splits, and that a `current:` entry
for such a part is an error rather than a publishable section. That block lives at the end of
this file and states its own reasoning in a header comment. It is here, and not in a file of
its own, because it needs exactly the machinery the #34 proof already builds: the same
constraint holds for it unchanged -- synthetic part, temp directory and monkeypatch, restored
in `finally`, never touching the real corpus.
"""
from __future__ import annotations

import argparse
import collections
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

    # The disambiguation guard, exercised through scanner.scan() ITSELF -- not by
    # re-implementing its gating logic inline, which would test two regexes and never the
    # production guard. AC5's own fixture: ORS chapter 164 (theft and burglary) collides with
    # 45 CFR 164 (the HIPAA Privacy Rule), and #27's triage on this issue measured the
    # collision as the MAJORITY case for a bare `164.NNN` in Oregon material -- ORS 164.377
    # (computer crime) and ORS 164.140 (criminal possession), the two sections named there.
    sec45_re, short45_re, part45_re = scanner.patterns(45, 164)
    with tempfile.TemporaryDirectory() as td:
        root = pathlib.Path(td)

        ors_only = (root / "ors-only.md")
        ors_only.write_text(
            "This policy addresses computer crime under ORS chapter 164. See ORS 164.377 "
            "(Computer Crime) and ORS 164.140 (Criminal possession). A related provision, "
            "§164.377(5), governs unauthorized computer use, and §164.140(4) must "
            "be reviewed before granting system access. Nothing here concerns HIPAA.\n",
            encoding="utf-8")
        counts_ors: collections.Counter = collections.Counter()
        sources_ors: dict[str, set] = collections.defaultdict(set)
        scanner.scan(root, "fixture", sec45_re, short45_re, part45_re, counts_ors, sources_ors)
        check("ORS chapter 164 collision: a file citing ORS 164 throughout and never "
              "mentioning 45 CFR contributes zero counts (AC5)",
              not counts_ors, f"got {dict(counts_ors)}")
        ors_only.unlink()

        # Positive control -- proves the assertion above is testing the guard and not just an
        # empty scan. A file that DOES carry the full 45 CFR 164 citation still licenses its
        # own bare short forms, the case the guard exists to allow.
        hipaa = (root / "hipaa.md")
        hipaa.write_text(
            "Covered entities must comply with 45 CFR 164.512(j) before disclosing PHI in "
            "administrative proceedings. See also §164.512(i) for law-enforcement "
            "disclosures.\n",
            encoding="utf-8")
        counts_hipaa: collections.Counter = collections.Counter()
        sources_hipaa: dict[str, set] = collections.defaultdict(set)
        scanner.scan(root, "fixture", sec45_re, short45_re, part45_re,
                     counts_hipaa, sources_hipaa)
        check("...but a file that DOES carry the full 45 CFR 164 citation still licenses "
              "its own bare short forms",
              counts_hipaa == {"512": 2}, f"got {dict(counts_hipaa)}")

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

    # --- split_cfr_sections.run_part(): END TO END, not just build()'s per-section pieces ----
    # #58's read-only/offline `--check` contract and #57's date-scoped consolidation
    # attribution both live in run_part() itself -- the network refusal, the by_date
    # grouping, and the KeyError-safety of `by_date.get(consolidation.get("date"), [])`
    # (found by this same review) are none of them reachable through build() alone, which
    # every check above this one calls directly, bypassing run_part() entirely. Synthetic
    # second part, module globals monkeypatched and restored, same shape as the
    # ingest_instruments.ROOT swap above, one file over.
    saved_globals = {name: getattr(splitter, name)
                      for name in ("ROOT", "SNAPSHOTS", "INSTRUMENTS", "CITED_DIR", "MANIFEST")}
    saved_ecfr_versions = scanner.ecfr_versions
    tmp2 = tempfile.TemporaryDirectory()
    try:
        root2 = pathlib.Path(tmp2.name)
        (root2 / "_meta" / "snapshots").mkdir(parents=True)
        (root2 / "_meta" / "cited-sections").mkdir(parents=True)
        (root2 / "instruments").mkdir(parents=True)
        splitter.ROOT = root2
        splitter.SNAPSHOTS = root2 / "_meta" / "snapshots"
        splitter.INSTRUMENTS = root2 / "instruments"
        splitter.CITED_DIR = root2 / "_meta" / "cited-sections"
        splitter.MANIFEST = root2 / "_meta" / "source-manifest.yml"
        # run_part() imports ecfr_versions FROM scan_cited_sections at call time (a local
        # import inside the function body), so patching the module attribute here -- not the
        # name `scanner.ecfr_versions` some earlier `from` import already bound -- is what
        # keeps every run below off the network without touching scan_cited_sections.py
        # itself, which is out of scope for this repo's split-side fixes.
        scanner.ecfr_versions = lambda title, part: {}

        part_id2 = "6-cfr-38"
        splitter.MANIFEST.write_text(yaml.safe_dump({"sources": [
            {"id": part_id2, "title": "Nondiscrimination Fixture Act II",
             "citation": "6 CFR 38", "instrument_kind": "cfr_part",
             "issuing_body": "Department of Justice",
             "url": "https://example.invalid/title-6/part-38.xml", "format": "xml",
             "reproduction_basis": "17 U.S.C. § 105"}]}), encoding="utf-8")
        (splitter.INSTRUMENTS / f"{part_id2}.md").write_text(
            "---\nas_of: '2026-01-01'\nretrieved: '2026-01-02'\n---\n\n## Full text\n",
            encoding="utf-8")

        part_xml2 = (
            b'<PART><SECTION TYPE="SECTION" N="38.10"><HEAD>&#167; 38.10 Current rule.</HEAD>'
            b'<P>Agencies shall comply.</P></SECTION></PART>'
        )
        (splitter.SNAPSHOTS / f"{part_id2}.xml").write_bytes(part_xml2)
        secs2 = splitter.sections_from(part_xml2, "38")
        (splitter.SNAPSHOTS / f"{part_id2}.txt").write_text(secs2["38.10"][1], encoding="utf-8")

        def write_cited(current, removed):
            # Mirrors scan_cited_sections.main()'s own line-building exactly (read, not
            # reimplemented from scratch) so --check's header-staleness comparison, which
            # diffs against `static_header()`/`CURRENT_COMMENT`/etc. verbatim, sees a file
            # shaped the way the real generator writes one.
            lines = scanner.static_header(6, 38) + [
                "", "scanned_files: 1", "total_citations: 1", "",
                scanner.CURRENT_COMMENT, "current:",
            ]
            for e in current:
                lines += [f"  - section: {scanner.q(e['section'])}",
                          f"    citations: {e['citations']}",
                          f"    cited_in: [{', '.join(scanner.q(c) for c in e['cited_in'])}]"]
            lines += [""] + scanner.REMOVED_COMMENT + ["removed:"]
            for e in removed:
                lines += [f"  - section: {scanner.q(e['section'])}",
                          f"    citations: {e['citations']}",
                          f"    cited_in: [{', '.join(scanner.q(c) for c in e['cited_in'])}]",
                          f"    removed_on: {scanner.q(e['removed_on'])}",
                          f"    name_when_in_force: {scanner.q(e['name_when_in_force'])}"]
            lines += [""] + scanner.UNRESOLVABLE_COMMENT + ["unresolvable:"]
            (splitter.CITED_DIR / f"{part_id2}.yml").write_text(
                "\n".join(lines) + "\n", encoding="utf-8")

        write_cited(
            current=[{"section": "38.10", "citations": 1, "cited_in": ["audits"]}],
            removed=[{"section": "38.99", "citations": 1, "cited_in": ["erf"],
                      "removed_on": "2024-05-01", "name_when_in_force": "Old rule."}])

        # #58, END TO END: --check over a part whose removed section's historical snapshot was
        # never committed must refuse, not fetch -- and nothing gets created anywhere under
        # root2 while refusing.
        before = sorted(str(p.relative_to(root2)) for p in root2.rglob("*") if p.is_file())
        rc_check = splitter.run_part(
            part_id2, argparse.Namespace(check=True, refetch=False))
        after = sorted(str(p.relative_to(root2)) for p in root2.rglob("*") if p.is_file())
        check("run_part() --check over a part missing its removed section's historical "
              "snapshot refuses (rc=1) rather than fetching it",
              rc_check == 1, f"got rc={rc_check}")
        check("...and creates NOTHING on disk while doing so",
              before == after, f"before={before}\n         after={after}")

        # #57, END TO END, plus the KeyError this review found one line over: a
        # CONSOLIDATIONS record whose own `date` does not match this removed section's
        # `removed_on` must not attribute its scope/target -- and a record with NO `date`
        # key at all (legal per cfr_consolidations.py's own docstring, which requires only
        # `scope`) must not crash run_part() either.
        saved_cons = dict(CONSOLIDATIONS)
        try:
            hist_id2 = f"{part_id2}-2024-04-30"
            hist_xml2 = (
                b'<PART><SECTION TYPE="SECTION" N="38.99"><HEAD>&#167; 38.99 Old rule.</HEAD>'
                b'<P>Superseded text.</P></SECTION></PART>'
            )
            (splitter.SNAPSHOTS / f"{hist_id2}.xml").write_bytes(hist_xml2)
            args_write = argparse.Namespace(check=False, refetch=False)

            CONSOLIDATIONS.clear()
            CONSOLIDATIONS[part_id2] = {"date": "2099-01-01", "into": "38.10",
                                         "scope": "Subpart Z's fixture procedures"}
            rc_mismatch = splitter.run_part(part_id2, args_write)
            removed_doc2 = (splitter.INSTRUMENTS / f"{part_id2}.99.md").read_text(
                encoding="utf-8")
            check("run_part() end to end: a consolidation record dated DIFFERENTLY than the "
                  "removal it would attach to does not fabricate the attribution (#57)",
                  rc_mismatch == 0 and "Subpart Z" not in removed_doc2
                  and "no successor section is recorded here" in removed_doc2,
                  f"rc={rc_mismatch}, doc={removed_doc2!r}")

            # Positive control -- same shape, matching date: the record DOES apply. Proves
            # the mismatch case above is testing the date comparison, not a broken code path.
            CONSOLIDATIONS.clear()
            CONSOLIDATIONS[part_id2] = {"date": "2024-05-01", "into": "38.10",
                                         "scope": "Subpart Z's fixture procedures"}
            rc_match = splitter.run_part(part_id2, args_write)
            removed_doc3 = (splitter.INSTRUMENTS / f"{part_id2}.99.md").read_text(
                encoding="utf-8")
            current_doc2 = (splitter.INSTRUMENTS / f"{part_id2}.10.md").read_text(
                encoding="utf-8")
            check("...and a MATCHING date does attribute it",
                  rc_match == 0 and "Subpart Z's fixture procedures were consolidated into "
                  "[§ 38.10]" in removed_doc3,
                  f"rc={rc_match}, doc={removed_doc3!r}")
            fm2 = yaml.safe_load(current_doc2.split("---")[1])
            got_supersedes = (fm2.get("relationships") or {}).get("supersedes")
            check("...and the target section's own document gets the `supersedes` back-edge",
                  got_supersedes == [f"{part_id2}.99"], f"got {got_supersedes}")

            # The KeyError this review found: `into`/`scope` with no `date` key must not
            # crash run_part() -- it used to subscript `consolidation["date"]` unguarded.
            CONSOLIDATIONS.clear()
            CONSOLIDATIONS[part_id2] = {"into": "38.10",
                                         "scope": "Subpart Z's fixture procedures"}
            nodate_exc = None
            try:
                rc_nodate = splitter.run_part(part_id2, args_write)
            except Exception as exc:  # noqa: BLE001 -- proving THIS does not raise, whatever it is
                rc_nodate, nodate_exc = None, exc
            check("a consolidation record with no `date` key does not crash run_part() "
                  "(KeyError, found by this review)",
                  nodate_exc is None and rc_nodate == 0,
                  f"raised {nodate_exc!r}" if nodate_exc else f"rc={rc_nodate}")
        finally:
            CONSOLIDATIONS.clear()
            CONSOLIDATIONS.update(saved_cons)
    finally:
        for name, val in saved_globals.items():
            setattr(splitter, name, val)
        scanner.ecfr_versions = saved_ecfr_versions
        tmp2.cleanup()

    # --- A WHOLLY SUPERSEDED PART: the whole part gone, not two sections out of a live one --
    # 45 CFR 75 was removed from the CFR IN ITS ENTIRETY on 2025-10-01 -- eCFR 404s for it --
    # so the part is pinned at its last-in-force date and `_meta/snapshots/45-cfr-75.xml` is
    # BYTE-IDENTICAL to `_meta/snapshots/45-cfr-75-2025-09-30.xml`. run_part()'s removed-section
    # branch asserted "a removed section must NOT be in the current part snapshot", which is
    # right for the 2 CFR 200 case it was written for and vacuous here: every removed section is
    # in that snapshot BY CONSTRUCTION. The fixture below reproduces exactly that shape -- the
    # two snapshots are the same bytes, written from one variable. A fixture whose snapshots
    # DIFFERED would pass whether or not the splitter understands superseded parts, and would
    # prove nothing.
    saved_globals3 = {name: getattr(splitter, name)
                      for name in ("ROOT", "SNAPSHOTS", "INSTRUMENTS", "CITED_DIR", "MANIFEST")}
    saved_ecfr_versions3 = scanner.ecfr_versions
    tmp3 = tempfile.TemporaryDirectory()
    try:
        root3 = pathlib.Path(tmp3.name)
        (root3 / "_meta" / "snapshots").mkdir(parents=True)
        (root3 / "_meta" / "cited-sections").mkdir(parents=True)
        (root3 / "instruments").mkdir(parents=True)
        splitter.ROOT = root3
        splitter.SNAPSHOTS = root3 / "_meta" / "snapshots"
        splitter.INSTRUMENTS = root3 / "instruments"
        splitter.CITED_DIR = root3 / "_meta" / "cited-sections"
        splitter.MANIFEST = root3 / "_meta" / "source-manifest.yml"
        scanner.ecfr_versions = lambda title, part: {}

        def cited_file(part_id, title, part, current, removed):
            """The same line-building scan_cited_sections.main() does -- see write_cited()
            above; repeated here rather than reached across two temp-directory scopes."""
            lines = scanner.static_header(title, part) + [
                "", "scanned_files: 1", "total_citations: 1", "",
                scanner.CURRENT_COMMENT, "current:",
            ]
            for e in current:
                lines += [f"  - section: {scanner.q(e['section'])}",
                          f"    citations: {e['citations']}",
                          f"    cited_in: [{', '.join(scanner.q(c) for c in e['cited_in'])}]"]
            lines += [""] + scanner.REMOVED_COMMENT + ["removed:"]
            for e in removed:
                lines += [f"  - section: {scanner.q(e['section'])}",
                          f"    citations: {e['citations']}",
                          f"    cited_in: [{', '.join(scanner.q(c) for c in e['cited_in'])}]",
                          f"    removed_on: {scanner.q(e['removed_on'])}",
                          f"    name_when_in_force: {scanner.q(e['name_when_in_force'])}"]
            lines += [""] + scanner.UNRESOLVABLE_COMMENT + ["unresolvable:"]
            (splitter.CITED_DIR / f"{part_id}.yml").write_text(
                "\n".join(lines) + "\n", encoding="utf-8")

        def manifest_for(*entries):
            splitter.MANIFEST.write_text(yaml.safe_dump({"sources": list(entries)}),
                                          encoding="utf-8")

        def part_doc(part_id, **fm):
            (splitter.INSTRUMENTS / f"{part_id}.md").write_text(
                "---\n" + yaml.safe_dump(fm, sort_keys=False) + "---\n\n## Full text\n",
                encoding="utf-8")

        # (a) ---------------------------------------------------------------------------
        gone_id, gone_title, gone_part = "9-cfr-12", 9, 12
        manifest_for(
            {"id": gone_id, "title": "Retired Fixture Requirements",
             "citation": "9 CFR 12", "instrument_kind": "cfr_part",
             "issuing_body": "Department of Fixtures",
             "url": "https://example.invalid/title-9/part-12.xml", "format": "xml",
             "reproduction_basis": "17 U.S.C. § 105"},
            {"id": "9-cfr-14", "title": "Retired Fixture Requirements II",
             "citation": "9 CFR 14", "instrument_kind": "cfr_part",
             "issuing_body": "Department of Fixtures",
             "url": "https://example.invalid/title-9/part-14.xml", "format": "xml",
             "reproduction_basis": "17 U.S.C. § 105"})
        part_doc(gone_id, as_of="2025-09-30", amended_on="2025-10-01",
                 superseded_by="9-cfr-13", status="superseded", retrieved="2026-01-02")

        gone_xml = (
            b'<PART><SECTION TYPE="SECTION" N="12.99"><HEAD>&#167; 12.99 Retired rule.</HEAD>'
            b'<P>Recipients shall have complied.</P></SECTION></PART>'
        )
        # THE WHOLE POINT: one variable, written to both paths. The "current" snapshot of a
        # part that no longer exists IS its last-in-force snapshot.
        (splitter.SNAPSHOTS / f"{gone_id}.xml").write_bytes(gone_xml)
        (splitter.SNAPSHOTS / f"{gone_id}-2025-09-30.xml").write_bytes(gone_xml)
        gone_secs = splitter.sections_from(gone_xml, "12")
        (splitter.SNAPSHOTS / f"{gone_id}.txt").write_text(gone_secs["12.99"][1],
                                                            encoding="utf-8")
        check("fixture check: the wholly-superseded part's current and last-in-force "
              "snapshots are the SAME bytes (as 45 CFR 75's are)",
              (splitter.SNAPSHOTS / f"{gone_id}.xml").read_bytes()
              == (splitter.SNAPSHOTS / f"{gone_id}-2025-09-30.xml").read_bytes(),
              "the fixture would pass by construction if these differed")
        cited_file(gone_id, gone_title, gone_part, current=[],
                   removed=[{"section": "12.99", "citations": 4, "cited_in": ["audits"],
                             "removed_on": "2025-10-01",
                             "name_when_in_force": "Retired rule."}])

        rc_gone = splitter.run_part(gone_id, argparse.Namespace(check=False, refetch=False))
        gone_doc_path = splitter.INSTRUMENTS / f"{gone_id}.99.md"
        check("a WHOLLY SUPERSEDED part splits: a removed section that is (necessarily) "
              "still in the pinned current snapshot is not an error",
              rc_gone == 0, f"got rc={rc_gone}")
        gone_doc = gone_doc_path.read_text(encoding="utf-8") if gone_doc_path.is_file() else ""
        gone_fm = yaml.safe_load(gone_doc.split("---")[1]) if gone_doc else {}
        # (a)'s second half, and the reason the relaxation is not a licence: the section must
        # still be published as SUPERSEDED, cut from the point-in-time snapshot. The wrong fix
        # this repo already reverted made --check pass by publishing removed federal law as
        # current text; these four assertions are what makes that fix fail here.
        check("...and it is still published as SUPERSEDED, not quietly promoted to live text",
              gone_fm.get("status") == "superseded", f"got status={gone_fm.get('status')!r}")
        check("...still cut from the point-in-time snapshot, not the current one",
              gone_fm.get("snapshot_id") == f"{gone_id}-2025-09-30",
              f"got snapshot_id={gone_fm.get('snapshot_id')!r}")
        check("...still dated at its last-in-force date, not the part's live as_of",
              gone_fm.get("as_of") == "2025-09-30" and gone_fm.get("amended_on") == "2025-10-01",
              f"got as_of={gone_fm.get('as_of')!r} amended_on={gone_fm.get('amended_on')!r}")
        check("...still titled so a corpus-index row alone cannot read as current law",
              str(gone_fm.get("title", "")).endswith("(SUPERSEDED 2025-10-01)"),
              f"got title={gone_fm.get('title')!r}")
        check("...and points at the successor the PART document names, not back at the "
              "superseded part itself",
              gone_fm.get("superseded_by") == "9-cfr-13",
              f"got superseded_by={gone_fm.get('superseded_by')!r}")
        check("...and its note says the whole part is gone, not just this section",
              "9 CFR 12 itself was removed from the CFR in its entirety" in gone_doc,
              "whole-part removal not stated in the section's own note")
        rc_gone_check = splitter.run_part(gone_id,
                                          argparse.Namespace(check=True, refetch=False))
        check("...and --check verifies what it just wrote (the round trip a green CI needs)",
              rc_gone_check == 0, f"got rc={rc_gone_check}")

        # (b) THE CONVERSE GATE -----------------------------------------------------------
        # Without this, (a) is a hole: relaxing "removed sections may appear in the current
        # snapshot" for a superseded part, and stopping there, leaves the checker unable to
        # object when the SAME identical-snapshot coincidence is used to call those sections
        # current. That is precisely the reverted edit -- all 7 cited sections of 45 CFR 75
        # hand-moved from `removed:` to `current:` in the GENERATED cited-sections file, which
        # turned the gate green by publishing removed federal law as current text. A part that
        # no longer exists has no sections in force, so a `current:` entry must FAIL.
        live_id = "9-cfr-14"
        part_doc(live_id, as_of="2025-09-30", amended_on="2025-10-01",
                 superseded_by="9-cfr-13", status="superseded", retrieved="2026-01-02")
        live_xml = (
            b'<PART><SECTION TYPE="SECTION" N="14.10"><HEAD>&#167; 14.10 Retired rule II.</HEAD>'
            b'<P>Recipients shall have complied.</P></SECTION></PART>'
        )
        (splitter.SNAPSHOTS / f"{live_id}.xml").write_bytes(live_xml)
        (splitter.SNAPSHOTS / f"{live_id}-2025-09-30.xml").write_bytes(live_xml)
        live_secs = splitter.sections_from(live_xml, "14")
        (splitter.SNAPSHOTS / f"{live_id}.txt").write_text(live_secs["14.10"][1],
                                                            encoding="utf-8")
        cited_file(live_id, 9, 14,
                   current=[{"section": "14.10", "citations": 4, "cited_in": ["audits"]}],
                   removed=[])
        rc_live = splitter.run_part(live_id, argparse.Namespace(check=False, refetch=False))
        check("a section listed as CURRENT in a wholly superseded part is an error",
              rc_live == 1, f"got rc={rc_live}")
        check("...and no document claiming it is current law was written",
              not (splitter.INSTRUMENTS / f"{live_id}.10.md").is_file(),
              "a status: current document was published for a part that no longer exists")
    finally:
        for name, val in saved_globals3.items():
            setattr(splitter, name, val)
        scanner.ecfr_versions = saved_ecfr_versions3
        tmp3.cleanup()

    print()
    if fails:
        print(f"FAILED: {len(fails)} assertion(s): {'; '.join(fails)}", file=sys.stderr)
        return 1
    print("A second cfr_part splits, slices, and links correctly -- none of it inherited from "
          "2 CFR 200. run_part() end to end: --check stays offline/read-only (#58) and "
          "consolidation attribution stays date-scoped without crashing (#57).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
