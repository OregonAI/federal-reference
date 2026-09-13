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
the last section proves that directly, by calling `build()` the way the pre-#77 code always did
(no `status`/`superseded_by` arguments at all) over 45 CFR 75's own real text, and checking that
THAT reproduces the bug this script exists to catch.
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

        malformed = scratch / "fixture-malformed.md"
        malformed.write_text("---\nsome scalar, not a mapping\n---\nbody\n", encoding="utf-8")
        check("a hand-mangled frontmatter (not a mapping) is tolerated, not a crash",
              ii.existing_supersession(malformed) == ("current", None, None),
              f"got {ii.existing_supersession(malformed)}")

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

    # --- _id_to_citation(): the successor-naming helper -----------------------------------
    check("_id_to_citation() turns a bare CFR part id into its citation form",
          ii._id_to_citation("2-cfr-200") == "2 CFR 200",
          ii._id_to_citation("2-cfr-200"))
    check("...and leaves a non-CFR-part id alone rather than guessing a shape for it",
          ii._id_to_citation("check-fixture-successor") == "check-fixture-successor",
          ii._id_to_citation("check-fixture-successor"))

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

        # THE FIX, applied exactly as main() applies it: status/superseded_by threaded
        # through from the document just read back.
        fixed = ii.build(src75, text, "fixturesha", stats, None, "2025-09-30", "2026-09-01",
                          status=real_status, superseded_by=real_superseded_by)
        fixed_fm = yaml.safe_load(fixed.split("---")[1])
        check("re-ingesting 45 CFR 75 WITH THE FIX leaves it status: superseded",
              fixed_fm.get("status") == "superseded", repr(fixed_fm.get("status")))
        check("...superseded_by: 2-cfr-200, not null",
              fixed_fm.get("superseded_by") == "2-cfr-200", repr(fixed_fm.get("superseded_by")))
        check("...and the body still says the part no longer exists",
              "no longer exists" in fixed, "removal note missing after re-ingest")

        # THE BUG, reproduced on demand: build() called the way every caller called it
        # before #77 -- no status/superseded_by at all -- over the SAME real text. If this
        # assertion ever passes, the fixture above stopped proving anything.
        broken = ii.build(src75, text, "fixturesha", stats, None, "2025-09-30", "2026-09-01")
        broken_fm = yaml.safe_load(broken.split("---")[1])
        check("the PRE-#77 call shape reproduces the bug on the same real text (status: "
              "current) -- confirms the assertions above are not vacuous",
              broken_fm.get("status") == "current", repr(broken_fm.get("status")))

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
