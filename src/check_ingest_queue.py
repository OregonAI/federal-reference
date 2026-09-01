#!/usr/bin/env python3
"""Assert the #63 part-discovery ranking works, against a SYNTHETIC catalog, never ERF's real
one.

    python3 src/check_ingest_queue.py

Run in CI (`generated` job, alongside check_citations.py, check_issuing_body.py,
check_extraction.py and check_section_split.py).

WHY THIS EXISTS. `src/scan_cited_sections.py --check` (see `check_queue()` there) proves the
COMMITTED `_meta/ingest-queue.yml` has not drifted from its own header and from what this
corpus's own instruments/ currently holds -- a no-regression check on the file that already
exists. It does NOT re-derive the queue from ERF's catalog, because that needs a real
executive-regulatory-frameworks checkout CI does not have (see scan_cited_sections.py's
module docstring). So nothing in CI ever exercises the RANKING ALGORITHM ITSELF -- the
function that turns a catalog's `targets:` list plus a held-set into a sorted, held-filtered
queue -- against more than one fixed, already-correct real answer. That is exactly the gap
check_section_split.py closes for the section splitter (#34) and check_issuing_body.py closes
for the issuer resolver (#33): every assertion below is a SYNTHETIC catalog and a SYNTHETIC
held-set, built in memory or in a temp `instruments/` directory, never touching the real
corpus or the real ERF checkout.
"""
from __future__ import annotations

import pathlib
import sys
import tempfile

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import scan_cited_sections as scanner  # noqa: E402

fails: list[str] = []


def check(desc: str, ok: bool, detail: str = "") -> None:
    print(f"  {'ok  ' if ok else 'FAIL'}  {desc}")
    if not ok:
        fails.append(f"{desc}{': ' + detail if detail else ''}")


# A fixture catalog shaped exactly like ERF's real `_meta/catalog/external-citations.yml`
# `targets:` list -- see that file's own header for the schema. Deliberately includes:
#   * two CFR parts with ordinary claims > 0, out of sort order, to prove the ranking sorts
#   * a THIRD with claims == 0 but mentions > 0 -- the 42 CFR Part 2 shape (#63 story 3):
#     zero claims must not mean dropped from the queue, only sunk to the bottom of it
#   * a fourth CFR part that IS held, to prove held-ness excludes it (#63 story 4)
#   * a non-CFR entry (USC), to prove it is excluded from a CFR-part ranking, not crashed on
FIXTURE_TARGETS = [
    {"citation": "9 CFR 71", "authority_claims": 4, "mentions": 10},
    {"citation": "9 CFR 90", "authority_claims": 12, "mentions": 15},
    {"citation": "9 CFR 2", "authority_claims": 0, "mentions": 22},
    {"citation": "9 CFR 5", "authority_claims": 9, "mentions": 9},   # held -- see below
    {"citation": "16 USC 544", "authority_claims": 50, "mentions": 60},
]
FIXTURE_HELD = {("9", "5")}


def main() -> int:
    # --- parse_cfr_citation(): format check against ERF's normalized shape --------------
    check("a bare CFR-part citation parses to (title, part)",
          scanner.parse_cfr_citation("34 CFR 300") == ("34", "300"),
          f"got {scanner.parse_cfr_citation('34 CFR 300')!r}")
    check("a letter-suffixed part parses too (real catalog has '7 CFR 1c', '8 CFR 274a')",
          scanner.parse_cfr_citation("7 CFR 1c") == ("7", "1c"),
          f"got {scanner.parse_cfr_citation('7 CFR 1c')!r}")
    check("a USC citation does not parse as CFR",
          scanner.parse_cfr_citation("16 USC 544") is None,
          f"got {scanner.parse_cfr_citation('16 USC 544')!r}")
    check("a named-instrument catalog entry (no citation string) does not parse as CFR",
          scanner.parse_cfr_citation("") is None, "expected None for an empty citation")

    # --- rank_targets(): the algorithm itself, against the fixture above -----------------
    ranked = scanner.rank_targets(FIXTURE_TARGETS, FIXTURE_HELD)
    ranked_ids = [r["part_id"] for r in ranked]

    check("the USC entry never appears in a CFR-part ranking",
          "16-usc-544" not in ranked_ids and len(ranked) == 3,
          f"got {ranked_ids}")
    check("the HELD CFR part (9 CFR 5) is excluded, not just sunk in rank (AC: story 4)",
          "9-cfr-5" not in ranked_ids, f"got {ranked_ids}")
    check("the remaining three are sorted by authority_claims DESC",
          ranked_ids == ["9-cfr-90", "9-cfr-71", "9-cfr-2"], f"got {ranked_ids}")

    zero_claim = next(r for r in ranked if r["part_id"] == "9-cfr-2")
    check("a part with ZERO claims is not dropped from the queue -- it sinks to the "
          "bottom (story 3's 42 CFR Part 2 shape) but its mentions are still reported",
          zero_claim["authority_claims"] == 0 and zero_claim["mentions"] == 22,
          f"got {zero_claim}")
    check("mentions never outrank claims: the zero-claim, highest-mention entry (22) still "
          "sorts LAST, behind two lower-mention but higher-claim entries",
          ranked_ids[-1] == "9-cfr-2",
          f"got {ranked_ids}")

    # Positive control on the sort key's own tie-break: two equal-claims entries sort by
    # mentions next, then by part_id -- proven directly against the sort key, not re-derived,
    # so this asserts the TIE-BREAK RULE rather than merely re-checking the case above.
    tie_fixture = [
        {"citation": "5 CFR 20", "authority_claims": 3, "mentions": 1},
        {"citation": "5 CFR 10", "authority_claims": 3, "mentions": 5},
    ]
    tie_ranked = [r["part_id"] for r in scanner.rank_targets(tie_fixture, set())]
    check("equal claims break the tie on mentions DESC, not on catalog order",
          tie_ranked == ["5-cfr-10", "5-cfr-20"], f"got {tie_ranked}")

    # --- rank_targets() on an ALL-HELD catalog: the caller's refusal to make, not this ---
    # function's -- rank_targets() itself returns an empty list.
    check("a catalog whose only CFR part is held ranks to an empty list, not a crash",
          scanner.rank_targets([{"citation": "9 CFR 5", "authority_claims": 1,
                                  "mentions": 1}], FIXTURE_HELD) == [],
          "expected an empty ranking")

    # --- "zero is a refusal, not a queue" (#63 Testing Decisions) --------------------------
    # build_queue_lines() is the PURE function discover_main() calls before deciding whether
    # to write anything -- see its own docstring for why the write is split out. Calling it
    # directly here (never discover_main(), which resolves the real QUEUE_OUT path) proves
    # the all-held case reports unheld_parts == 0 with no file I/O at all, which is what lets
    # the caller refuse to write -- or delete -- the committed queue on this path.
    all_held_catalog = {"targets": [{"citation": "9 CFR 5", "authority_claims": 1,
                                      "mentions": 1}]}
    _lines, unheld_n, total_n = scanner.build_queue_lines(all_held_catalog, FIXTURE_HELD)
    check("an all-held catalog reports zero unheld parts -- the caller's cue to refuse "
          "rather than write an empty queue",
          unheld_n == 0 and total_n == 1, f"got unheld_n={unheld_n}, total_n={total_n}")

    # --- held_cfr_parts(): read from a SYNTHETIC instruments/, not the real corpus --------
    with tempfile.TemporaryDirectory() as td:
        instruments = pathlib.Path(td)

        (instruments / "6-cfr-37.md").write_text(
            "---\nid: 6-cfr-37\ninstrument_kind: cfr_part\n---\nfixture part\n",
            encoding="utf-8")
        (instruments / "6-cfr-37.72.md").write_text(
            "---\nid: 6-cfr-37.72\ninstrument_kind: cfr_section\n---\nfixture section\n",
            encoding="utf-8")
        # A held SECTION with no bare part document at all -- ADR-0003's own scenario (a
        # part fully split loses its bare-part id). Must still mark the PART held.
        (instruments / "45-cfr-164.512.md").write_text(
            "---\nid: 45-cfr-164.512\ninstrument_kind: cfr_section\n---\nfixture section\n",
            encoding="utf-8")
        # A non-CFR document must not contribute a bogus (title, part) key.
        (instruments / "irs-pub-1075.md").write_text(
            "---\nid: irs-pub-1075\ninstrument_kind: irs_publication\n---\nfixture\n",
            encoding="utf-8")

        held = scanner.held_cfr_parts(instruments)
        check("a held cfr_part document marks its part held",
              ("6", "37") in held, f"got {held}")
        check("a held cfr_section with NO bare part document still marks the PART held "
              "(ADR-0003: a fully-split part can lose its own bare-part document)",
              ("45", "164") in held, f"got {held}")
        check("a non-cfr document contributes no (title, part) key at all",
              len(held) == 2, f"got {held}")

    print()
    if fails:
        print(f"FAILED: {len(fails)} assertion(s): {'; '.join(fails)}", file=sys.stderr)
        return 1
    print("The #63 ranking algorithm sorts by claim, carries mentions alongside without "
          "dropping zero-claim parts, and excludes held parts -- against a synthetic "
          "catalog and a synthetic instruments/, never the real corpus or a real ERF "
          "checkout.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
