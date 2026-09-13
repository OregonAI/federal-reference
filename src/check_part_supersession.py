#!/usr/bin/env python3
"""Assert `ingest_instruments.py` no longer republishes a wholly superseded part as current.

    python3 src/check_part_supersession.py

Run in CI (`generated` job, alongside check_issuing_body.py and check_section_split.py).

WHY THIS EXISTS. #77: `ingest_instruments.build()` hardcoded `"status": "current"` and
`"superseded_by": None` for every part, so re-running the ingester over 45 CFR 75 -- removed
from the CFR in its entirety on 2025-10-01, hand-published `status: superseded` in dcd0d41 --
would republish it as current law. Nothing caught this: `split_cfr_sections.py --check` gates
the SECTION documents (#78's fix), never the part document, and `ingest_instruments.py` itself
has no gate at all and runs in no CI workflow (grep `.github/` -- it appears only in comments;
every source it ingests needs a live fetch and, for a `cfr_part` not yet superseded, a live
`cfr_amended_on()` lookup, so a hermetic CI step cannot drive it end to end).

This is that gate, built the way check_issuing_body.py and check_section_split.py are: against
synthetic fixtures and the real 45 CFR 75 snapshot already committed to this repo, entirely
offline. It cannot replace `ingest_instruments.py --check` (which DOES need the network for a
live part, on purpose -- ADR-0001's "current text" model means a live part's `amended_on`
should be verified against eCFR, not trusted from disk) but it can run on every PR, which that
flag cannot.

Mostly negative assertions, each confirmed to fail when the behaviour it guards is removed --
confirmed by actually applying the pre-#77 mutation (re-hardcoding `"status": "current"` and
`"superseded_by": None` inside `build()`'s own fm dict, ignoring the parameters) and observing
several of the checks below go red, then reverting it. An earlier version of this script also
called `build()` the pre-#77 way (no `status`/`superseded_by` at all) and asserted THAT
reproduced `status: current`, as its own claimed proof of non-vacuity -- a #77-review finding
(S3) found that check was a tautology over `build()`'s own DEFAULT PARAMETER VALUES (which are
literally "current"/None), so it passed unconditionally whether the mutation above was applied
or not, and removed it rather than leave a check that cannot fail stand in for one that can.
"""
from __future__ import annotations

import sys
import tempfile
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
import ingest_instruments as ii  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent


def main() -> int:
    fails: list[str] = []

    def check(desc: str, ok: bool, detail: str = "") -> None:
        print(f"  {'ok  ' if ok else 'FAIL'}  {desc}")
        if not ok:
            fails.append(f"{desc}{': ' + detail if detail else ''}")

    # --- existing_supersession(): the reader itself, against synthetic committed documents ---
    with tempfile.TemporaryDirectory() as tmp:
        scratch = Path(tmp)

        missing = scratch / "not-ingested-yet.md"
        check("a part never committed yet reads as current, not superseded",
              ii.existing_supersession(missing) == ("current", None, None),
              f"got {ii.existing_supersession(missing)}")

        live_doc = scratch / "fixture-live.md"
        live_doc.write_text(
            "---\nstatus: current\nsuperseded_by: null\namended_on: '2024-01-01'\n---\n"
            "## Full text\nfixture\n", encoding="utf-8")
        check("a committed LIVE part reads back as current with no successor",
              ii.existing_supersession(live_doc) == ("current", None, "2024-01-01"),
              f"got {ii.existing_supersession(live_doc)}")

        superseded_doc = scratch / "fixture-superseded.md"
        superseded_doc.write_text(
            "---\nstatus: superseded\nsuperseded_by: fixture-successor\n"
            "amended_on: '2025-10-01'\n---\n## Full text\nfixture\n", encoding="utf-8")
        check("a committed SUPERSEDED part reads back its own status/successor/date",
              ii.existing_supersession(superseded_doc)
              == ("superseded", "fixture-successor", "2025-10-01"),
              f"got {ii.existing_supersession(superseded_doc)}")

        # #77 review (S5): a hand-mangled frontmatter used to be TOLERATED here, reading back
        # as ("current", None, None) -- the exact wrong direction. `part_facts()` (this
        # function's own named model) does not tolerate a document it cannot read; a part
        # document this ingester cannot parse is not one it can safely call current. Same
        # refusal for all three unreadable shapes: no delimiter, invalid YAML, non-mapping.
        no_delim = scratch / "fixture-no-delimiter.md"
        no_delim.write_text("no frontmatter delimiter at all\nbody\n", encoding="utf-8")
        try:
            ii.existing_supersession(no_delim)
            check("a document with no '---' delimiter refuses rather than reading as current",
                  False, "did not raise")
        except ValueError:
            check("a document with no '---' delimiter refuses rather than reading as current",
                  True)

        bad_yaml = scratch / "fixture-bad-yaml.md"
        bad_yaml.write_text("---\nstatus: [unterminated\n---\nbody\n", encoding="utf-8")
        try:
            ii.existing_supersession(bad_yaml)
            check("invalid YAML frontmatter refuses rather than reading as current",
                  False, "did not raise")
        except ValueError:
            check("invalid YAML frontmatter refuses rather than reading as current", True)

        malformed = scratch / "fixture-malformed.md"
        malformed.write_text("---\nsome scalar, not a mapping\n---\nbody\n", encoding="utf-8")
        try:
            ii.existing_supersession(malformed)
            check("a hand-mangled frontmatter (not a mapping) refuses rather than reading "
                  "as current", False, "did not raise")
        except ValueError:
            check("a hand-mangled frontmatter (not a mapping) refuses rather than reading "
                  "as current", True)

    # --- build(): status/superseded_by/relationships/title/note, for a SYNTHETIC part ---------
    src37 = {"id": "check-fixture-6-cfr-37", "title": "Disability Fixture Act",
             "citation": "6 CFR 37", "instrument_kind": "cfr_part",
             "issuing_body": "Department of Justice",
             "url": "https://example.invalid/title-6/part-37.xml", "format": "xml",
             "reproduction_basis": "17 U.S.C. § 105", "amended_on": "2025-10-01"}

    default_doc = ii.build(src37, "full text", "sha000", {"pages": 1}, None,
                            "2026-01-01", "2026-01-02")
    default_fm = yaml.safe_load(default_doc.split("---")[1])
    check("build() with no status/superseded_by argument still defaults to current "
          "(no regression for every other part)",
          default_fm.get("status") == "current" and default_fm.get("superseded_by") is None,
          f"got status={default_fm.get('status')!r} "
          f"superseded_by={default_fm.get('superseded_by')!r}")
    check("...and its title carries no SUPERSEDED marker",
          "SUPERSEDED" not in default_fm["title"], repr(default_fm["title"]))
    check("...and the disclaimer still says the copy is CURRENT text",
          "is CURRENT text" in default_doc, "CURRENT-text disclaimer missing")

    superseded_doc_body = ii.build(src37, "full text", "sha000", {"pages": 1}, None,
                                    "2026-01-01", "2026-01-02",
                                    status="superseded", superseded_by="check-fixture-successor")
    superseded_fm = yaml.safe_load(superseded_doc_body.split("---")[1])
    check("build(status='superseded') publishes status: superseded, not current",
          superseded_fm.get("status") == "superseded", repr(superseded_fm.get("status")))
    check("...and names the successor in superseded_by",
          superseded_fm.get("superseded_by") == "check-fixture-successor",
          repr(superseded_fm.get("superseded_by")))
    check("...and the title carries the SUPERSEDED marker with its amended_on date",
          superseded_fm["title"] == "Disability Fixture Act (SUPERSEDED 2025-10-01)",
          repr(superseded_fm["title"]))
    check("...and relationships.related points at the SUCCESSOR, not this part's own "
          "(equally superseded) split sections",
          superseded_fm.get("relationships", {}).get("related") == ["check-fixture-successor"],
          f"got {superseded_fm.get('relationships')}")
    check("...and the body states the part no longer exists",
          "no longer exists" in superseded_doc_body, "removal note missing")
    check("...and the body no longer claims the copy is CURRENT text",
          "is CURRENT text" not in superseded_doc_body,
          "stale CURRENT-text disclaimer still present")
    check("...and the disclaimer instead says the text is superseded",
          "**superseded** text" in superseded_doc_body, "superseded disclaimer missing")

    # A superseded part with NO recorded successor (PART_REMOVALS entry absent, or an entry
    # with no `into`) must still publish plainly rather than fabricate one.
    orphan_doc = ii.build(src37, "full text", "sha000", {"pages": 1}, None,
                           "2026-01-01", "2026-01-02", status="superseded", superseded_by=None)
    check("a superseded part with NO recorded successor does not fabricate one",
          "drop-in replacement" not in orphan_doc,
          "invented a successor with nothing recorded")
    check("...but still states plainly that the part is gone",
          "no longer exists" in orphan_doc, "removal was not stated")
    orphan_fm = yaml.safe_load(orphan_doc.split("---")[1])
    check("...and relationships.related is empty rather than pointing nowhere useful",
          orphan_fm.get("relationships", {}).get("related") == [],
          f"got {orphan_fm.get('relationships')}")

    # --- #77 review (S2): a superseded part with NO amended_on must refuse, not fabricate ---
    src37_no_date = {**src37, "amended_on": None}
    try:
        ii.build(src37_no_date, "full text", "sha000", {"pages": 1}, None,
                 "2026-01-01", "2026-01-02", status="superseded",
                 superseded_by="check-fixture-successor")
        check("a superseded part with no amended_on refuses rather than publishing a "
              "fabricated 'None' as its removal date", False, "did not raise")
    except ValueError:
        check("a superseded part with no amended_on refuses rather than publishing a "
              "fabricated 'None' as its removal date", True)

    # --- _id_to_citation(): the successor-naming helper -----------------------------------
    check("_id_to_citation() turns a bare CFR part id into its citation form",
          ii._id_to_citation("2-cfr-200") == "2 CFR 200",
          ii._id_to_citation("2-cfr-200"))
    check("...and leaves a non-CFR-part id alone rather than guessing a shape for it",
          ii._id_to_citation("check-fixture-successor") == "check-fixture-successor",
          ii._id_to_citation("check-fixture-successor"))

    # --- #77 review (P1/P2/P3): the curator-note read-back/preservation seam ---------------
    with tempfile.TemporaryDirectory() as tmp:
        scratch = Path(tmp)

        check("existing_curator_note() on a part never committed yet returns None "
              "(nothing to preserve, not an empty string)",
              ii.existing_curator_note(scratch / "not-ingested-yet.md") is None,
              repr(ii.existing_curator_note(scratch / "not-ingested-yet.md")))

        hand_wrapped = scratch / "fixture-hand-wrapped.md"
        hand_wrapped.write_text(
            "---\nstatus: superseded\n---\n## At a glance\n\n"
            "> **This part no longer exists.** It was removed from the CFR on\n"
            "> **2024-01-01**.\n"
            ">\n"
            "> It is held because a fixture says so — 9 citations, all from a\n"
            "> made-up signal. **The current definition may differ.** Do not read this\n"
            "> as current law.\n",
            encoding="utf-8")
        check("existing_curator_note() recovers a hand-WRAPPED (multi-line) curator "
              "paragraph as one logical sentence, boundary phrase stripped",
              ii.existing_curator_note(hand_wrapped)
              == "It is held because a fixture says so — 9 citations, all from a "
                 "made-up signal.",
              repr(ii.existing_curator_note(hand_wrapped)))

        no_note_yet = scratch / "fixture-no-note.md"
        no_note_yet.write_text(
            "---\nstatus: superseded\n---\n## At a glance\n\nno blockquote at all\n",
            encoding="utf-8")
        check("existing_curator_note() on a document with no whole-part blockquote yet "
              "returns None rather than an empty string",
              ii.existing_curator_note(no_note_yet) is None,
              repr(ii.existing_curator_note(no_note_yet)))

    check("citation_signal_counts() on a part never scanned returns {} (absence, not a "
          "fabricated zero)",
          ii.citation_signal_counts("check-fixture-6-cfr-37") == {},
          repr(ii.citation_signal_counts("check-fixture-6-cfr-37")))
    check("...and _default_curator_note() for that part states plainly it is held, with "
          "no invented count",
          ii._default_curator_note("check-fixture-6-cfr-37")
          == "It is held because Oregon material cites sections within it.",
          repr(ii._default_curator_note("check-fixture-6-cfr-37")))

    real_counts = ii.citation_signal_counts("45-cfr-75")
    check("citation_signal_counts(45-cfr-75) sums _meta/cited-sections/45-cfr-75.yml's own "
          "per-section citations, split by signal, not a single unsignaled total",
          real_counts == {"audits": 27, "erf": 3}, f"got {real_counts}")
    real_default_note = ii._default_curator_note("45-cfr-75")
    check("...and _default_curator_note() for the real part names BOTH signals rather "
          "than conflating them into one adjective (CONTEXT.md's 'three intake signals')",
          "Oregon's single audits" in real_default_note and "Oregon rules" in real_default_note,
          real_default_note)
    check("...and states the true 30-citation total across all 7 held sections, not the "
          "unmeasured '28' the original hand-written note carried",
          "30" in real_default_note and "7" in real_default_note, real_default_note)

    # --- THE REAL CASE: 45 CFR 75, from the actual committed snapshot, fully offline -------
    real_snap = ii.SNAPSHOTS / "45-cfr-75.xml"
    real_doc_path = ii.OUT_DIR / "45-cfr-75.md"
    if not real_snap.is_file() or not real_doc_path.is_file():
        check("45 CFR 75's committed snapshot and document are both present", False,
              f"{real_snap} or {real_doc_path} missing")
    else:
        real_status, real_superseded_by, real_amended_on = \
            ii.existing_supersession(real_doc_path)
        check("45 CFR 75's committed document reads back as superseded (dcd0d41)",
              real_status == "superseded", f"got status={real_status!r}")
        check("...naming 2 CFR 200 as its successor",
              real_superseded_by == "2-cfr-200", f"got {real_superseded_by!r}")

        raw = real_snap.read_bytes()
        text, stats = ii.extract_cfr(raw)
        src75 = {"id": "45-cfr-75", "title": "Uniform Administrative Requirements, Cost "
                 "Principles, and Audit Requirements for HHS Awards",
                 "citation": "45 CFR 75", "instrument_kind": "cfr_part",
                 "issuing_body": "Department of Health and Human Services",
                 "url": "https://www.ecfr.gov/api/versioner/v1/full/2025-09-30/"
                        "title-45.xml?part=75",
                 "format": "xml", "reproduction_basis": "17 U.S.C. § 105",
                 "amended_on": real_amended_on}

        # THE FIX, applied exactly as main() applies it: status/superseded_by/curator_note
        # all threaded through from the document just read back.
        real_note = ii.existing_curator_note(real_doc_path)
        fixed = ii.build(src75, text, "fixturesha", stats, None, "2025-09-30", "2026-09-01",
                          status=real_status, superseded_by=real_superseded_by,
                          curator_note=real_note)
        fixed_fm = yaml.safe_load(fixed.split("---")[1])
        check("re-ingesting 45 CFR 75 WITH THE FIX leaves it status: superseded",
              fixed_fm.get("status") == "superseded", repr(fixed_fm.get("status")))
        check("...superseded_by: 2-cfr-200, not null",
              fixed_fm.get("superseded_by") == "2-cfr-200", repr(fixed_fm.get("superseded_by")))
        check("...and the body still says the part no longer exists",
              "no longer exists" in fixed, "removal note missing after re-ingest")

        # #77 review (P1/P2/P3): re-ingesting the REAL, committed 45 CFR 75 must PRESERVE its
        # curator note verbatim -- the measured "30 citations... 27... 3..." figure, signal-
        # named -- not regenerate the unmeasured, unsignaled sentence the original #77 fix
        # wrote ("Oregon material cites sections within it for periods when they were in
        # force"). This is the actual non-vacuity proof for the note-preservation seam: it
        # reads real committed content, not a synthetic fixture, and fails if
        # existing_curator_note()/build() stop wiring together correctly.
        check("re-ingesting 45 CFR 75 preserves its curator note's measured citation count",
              "30 times" in fixed and "27 from Oregon's single audits" in fixed
              and "3 from Oregon rules" in fixed,
              "measured citation figures missing from re-ingested body")
        check("...and does NOT regenerate the unsignaled '28 audit citations' figure the "
              "original hand-written note carried (known wrong the day it was written)",
              "28 audit citations" not in fixed, "stale '28' figure present")
        check("...and does NOT regenerate the CONTEXT.md-conflating phrase the #77 fix's "
              "first pass wrote in its place",
              "for periods when they were in force" not in fixed,
              "unsignaled conflated phrase present")

        # THE MUTATION THAT WOULD BREAK ALL OF THE ABOVE, applied and reverted by hand during
        # this review rather than kept as a permanently-green "control": re-hardcoding
        # `"status": "current"` / `"superseded_by": None` inside build()'s own fm dict
        # (instead of using the `status`/`superseded_by` parameters) turned the "publishes
        # status: superseded" and "names the successor" checks above red, and left this
        # real-case block red too (`real_status`/`real_superseded_by` threaded through
        # correctly but ignored by the mutated fm dict) -- see the module docstring's S3 note
        # for why a synthetic "control" asserting the OPPOSITE was removed instead of kept.

    # --- #77 review (P7): the UN-supersession direction is pinned to 45 CFR 75 ALONE; catch
    # the OPPOSITE latch -- a single frontmatter edit setting `status: superseded` on any
    # OTHER cfr_part would, before this check existed, latch PERMANENTLY: main() stops
    # consulting eCFR for that part forever (existing_supersession() sees `superseded` and
    # trusts the committed amended_on), build() emits a SUPERSEDED title/note/successor edge,
    # and --check passes because it diffs the document against a build derived from that same
    # document. Bounded and partly speculative (it requires a bad edit to survive CODEOWNER
    # review), but #77's own issue cites PR #75's hand edit to _meta/cited-sections/
    # 45-cfr-75.yml as proof such edits DO reach main and are caught by a gate, not by a
    # reviewer reading closely.
    superseded_parts = []
    for doc in sorted(ii.OUT_DIR.glob("*.md")):
        if "." in doc.stem:                       # a split SECTION document, not a part
            continue
        try:
            doc_fm = yaml.safe_load(doc.read_text(encoding="utf-8").split("---")[1])
        except (IndexError, yaml.YAMLError):
            continue
        if (isinstance(doc_fm, dict) and doc_fm.get("instrument_kind") == "cfr_part"
                and doc_fm.get("status") == "superseded"):
            superseded_parts.append(doc.stem)
    check("no cfr_part document OTHER than 45-cfr-75 is committed status: superseded",
          superseded_parts == ["45-cfr-75"], f"got {superseded_parts}")

    print()
    if fails:
        print(f"FAILED: {len(fails)} assertion(s): {'; '.join(fails)}", file=sys.stderr)
        return 1
    print("existing_supersession() reads status/superseded_by/amended_on back from a "
          "committed part document, build() renders them (title, relationships, body note) "
          "instead of hardcoding current/null, and 45 CFR 75 stays superseded across a "
          "re-ingest of its real, committed snapshot.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
