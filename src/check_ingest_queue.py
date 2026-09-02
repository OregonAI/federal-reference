#!/usr/bin/env python3
"""Assert the #63 part-discovery ranking -- and #64's oregon-audits mention merge -- work,
against SYNTHETIC fixtures, never a real ERF or oregon-audits checkout.

    python3 src/check_ingest_queue.py

Run in CI (`generated` job, alongside check_citations.py, check_issuing_body.py,
check_extraction.py and check_section_split.py).

WHY THIS EXISTS. `src/scan_cited_sections.py --check` (see `check_queue()` there) proves the
COMMITTED `_meta/ingest-queue.yml` has not drifted from its own header and from what this
corpus's own instruments/ currently holds -- a no-regression check on the file that already
exists. It does NOT re-derive the queue from ERF's catalog or re-scan oregon-audits, because
that needs real sibling checkouts CI does not have (see scan_cited_sections.py's module
docstring). So nothing in CI ever exercises the RANKING/MERGE ALGORITHM ITSELF -- the
function that turns a catalog's `targets:` list, a held-set, and a set of audit mentions into
a sorted, held-filtered queue -- against more than one fixed, already-correct real answer.
That is exactly the gap check_section_split.py closes for the section splitter (#34) and
check_issuing_body.py closes for the issuer resolver (#33): every assertion below is a
SYNTHETIC catalog, held-set, audit-mentions map, or audits directory, built in memory or in a
temp directory, never touching the real corpus or a real sibling checkout.
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

    # --- audit_mentions merge (#64): additive into an existing row, a new zero-claim row --
    # for an audit-only part, and held-ness excludes an audit-cited part exactly like it
    # excludes a catalog one. Reuses FIXTURE_TARGETS/FIXTURE_HELD above so the catalog side
    # of the merge is the same fixture every other check here already trusts.
    AUDIT_FIXTURE = {("9", "71"): 3, ("9", "5"): 7, ("9", "40"): 6}
    ranked_audit = scanner.rank_targets(FIXTURE_TARGETS, FIXTURE_HELD, AUDIT_FIXTURE)
    by_id = {r["part_id"]: r for r in ranked_audit}

    check("audit mentions merge ADDITIVELY into a catalog row's own mentions, claims "
          "unchanged (#64)",
          by_id.get("9-cfr-71", {}).get("mentions") == 13
          and by_id.get("9-cfr-71", {}).get("authority_claims") == 4,
          f"got {by_id.get('9-cfr-71')}")
    check("a merged row's cited_in names both sources, sorted",
          by_id.get("9-cfr-71", {}).get("cited_in") == ["audits", "erf"],
          f"got {by_id.get('9-cfr-71', {}).get('cited_in')}")
    # #69: mentions alone throws away the erf/audits split once a row merges both sources
    # (9 CFR 71: 10 erf + 3 audits = 13) -- mentions_erf/mentions_audits carry the two
    # addends the merge above only checked the SUM of.
    check("a merged row's mentions_erf/mentions_audits carry the split mentions sums, "
          "not just their total (#69)",
          by_id.get("9-cfr-71", {}).get("mentions_erf") == 10
          and by_id.get("9-cfr-71", {}).get("mentions_audits") == 3,
          f"got {by_id.get('9-cfr-71')}")
    check("a HELD part cited only in audits (9 CFR 5, held) never reaches the queue -- "
          "held-ness is checked for audit-only rows exactly like catalog rows (#64)",
          "9-cfr-5" not in by_id, f"got {sorted(by_id)}")
    check("a part cited ONLY in audits, absent from the catalog entirely, becomes a new "
          "row at authority_claims: 0 (#64, the 42 CFR Part 2 shape), all its mentions "
          "attributed to audits (#69)",
          by_id.get("9-cfr-40") == {"part_id": "9-cfr-40", "citation": "9 CFR 40",
                                     "title": "9", "part": "40", "authority_claims": 0,
                                     "mentions": 6, "mentions_erf": 0, "mentions_audits": 6,
                                     "cited_in": ["audits"]},
          f"got {by_id.get('9-cfr-40')}")
    check("a catalog row audits never mention still carries erf-only cited_in, and its "
          "mentions are all attributed to erf (#69)",
          by_id.get("9-cfr-90", {}).get("cited_in") == ["erf"]
          and by_id.get("9-cfr-90", {}).get("mentions_erf") == 15
          and by_id.get("9-cfr-90", {}).get("mentions_audits") == 0,
          f"got {by_id.get('9-cfr-90')}")

    # --- "zero is a refusal, not a queue" (#63 Testing Decisions) --------------------------
    # build_queue_lines() is the PURE function discover_main() calls before deciding whether
    # to write anything -- see its own docstring for why the write is split out. Calling it
    # directly here (never discover_main(), which resolves the real QUEUE_OUT path) proves
    # the all-held case reports unheld_parts == 0 with no file I/O at all, which is what lets
    # the caller refuse to write -- or delete -- the committed queue on this path.
    all_held_catalog = {"targets": [{"citation": "9 CFR 5", "authority_claims": 1,
                                      "mentions": 1}]}
    _lines, unheld_n, total_n, audit_only_n = scanner.build_queue_lines(
        all_held_catalog, FIXTURE_HELD)
    check("an all-held catalog reports zero unheld parts -- the caller's cue to refuse "
          "rather than write an empty queue",
          unheld_n == 0 and total_n == 1 and audit_only_n == 0,
          f"got unheld_n={unheld_n}, total_n={total_n}, audit_only_n={audit_only_n}")

    # --- build_queue_lines() with the same AUDIT_FIXTURE: the summary numbers reconcile --
    # scanned_targets stays the catalog-only CFR subset (4: 71/90/2/5); audit_only_parts (1,
    # 9 CFR 40) sits OUTSIDE it, so unheld_parts is catalog-unheld (3) + audit_only (1).
    _lines2, unheld_n2, total_n2, audit_only_n2 = scanner.build_queue_lines(
        {"targets": FIXTURE_TARGETS}, FIXTURE_HELD, AUDIT_FIXTURE)
    check("audit-only parts are counted separately from the catalog CFR subset",
          audit_only_n2 == 1, f"got {audit_only_n2}")
    check("unheld_parts (queue length) = catalog-unheld (3) + audit-only (1)",
          unheld_n2 == 4 and total_n2 == 4,
          f"got unheld_n2={unheld_n2}, total_n2={total_n2}")

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

    # --- scan_audit_mentions() / AUDIT_CFR_RE: a SYNTHETIC audits checkout, never the ------
    # real oregon-audits -- proves the general-shape regex against the citation forms #64's
    # own measurement found in real audit reports, not the regex read in isolation.
    with tempfile.TemporaryDirectory() as td:
        audits = pathlib.Path(td)
        (audits / "reports").mkdir()
        (audits / "reports" / "a.md").write_text(
            "Subject to 2 CFR 200 and, later in the same finding, 2 C.F.R. § 200 "
            "again. Also 7 CFR Part 273. Lowercase 'part' too: 45 CFR part 155.\n",
            encoding="utf-8")
        (audits / "reports" / "b.md").write_text(
            "A letter-suffixed part: 7 CFR 1c. And a title-only false alarm: CFR 200 "
            "(no title digits) should not match. A truncated section citation, "
            "2 CFR 331(d), should not mint a false part either.\n", encoding="utf-8")
        (audits / "reports" / "_meta").mkdir()
        (audits / "reports" / "_meta" / "excluded.md").write_text(
            "45 CFR 265 should never be counted -- _meta is excluded.\n", encoding="utf-8")
        # Code review of #64: a repository-root file is not a corpus document -- a bare
        # `audits.rglob("*.md")` used to count this. Real oregon-audits AGENTS.md/
        # CHANGELOG.md/README.md/etc. carry no CFR mention today, but nothing enforced
        # that; this one does, and must never be counted.
        (audits / "CHANGELOG.md").write_text(
            "24 CFR 576 changed in this release.\n", encoding="utf-8")

        audit_counts, audit_files = scanner.scan_audit_mentions(audits)
        check("scan_audit_mentions() counts a plain full citation",
              audit_counts[("2", "200")] == 2, f"got {audit_counts[('2', '200')]}")
        check("scan_audit_mentions() counts a 'CFR Part N' citation",
              audit_counts[("7", "273")] == 1, f"got {audit_counts[('7', '273')]}")
        check("scan_audit_mentions() handles a letter-suffixed part (mirrors ERF's FED)",
              audit_counts[("7", "1c")] == 1, f"got {audit_counts[('7', '1c')]}")
        check("a bare 'CFR 200' with no title digits does not match",
              ("", "200") not in audit_counts, f"got {dict(audit_counts)}")
        check("_meta/ is excluded from the audit scan, same SKIP_PARTS as scan()",
              ("45", "265") not in audit_counts, f"got {dict(audit_counts)}")
        check("a repository file outside reports/ is never scanned (#64 review: "
              "measures the corpus, not the repository)",
              ("24", "576") not in audit_counts, f"got {dict(audit_counts)}")
        check("'Part' is matched case-insensitively (#64 review: '45 CFR part 155' "
              "used to match nothing at all)",
              audit_counts[("45", "155")] == 1, f"got {audit_counts[('45', '155')]}")
        check("a part number immediately followed by a lowercase-letter subsection "
              "marker is refused, not counted as a bare part (#64 review: '2 CFR "
              "331(d)' is a truncated section citation, not a real part)",
              ("2", "331") not in audit_counts, f"got {dict(audit_counts)}")
        check("scan_audit_mentions() counts files the same way scan() does (SKIP_PARTS "
              "excludes _meta, so 2 files, not 3), scoped to reports/ only",
              audit_files == 2, f"got {audit_files}")

    # --- check_queue() (#69 / #70): the COMMITTED-file gate itself, against a synthetic ----
    # queue file in a temp dir -- QUEUE_OUT is monkeypatched to it for the duration of this
    # block, so this can never corrupt the real committed _meta/ingest-queue.yml. Builds one
    # hand-written, internally-correct file with a single-source row and a merged
    # (erf+audits) row, confirms --check passes it, then corrupts one field -- or cited_in
    # itself -- at a time and confirms --check catches every one. This is the reproduction
    # both issues' own review demonstrated (a hand-edit passing silently), turned into a
    # standing regression instead of a one-time manual check.
    with tempfile.TemporaryDirectory() as td:
        fixture_queue = pathlib.Path(td) / "ingest-queue.yml"
        header = scanner.queue_header()
        body = [
            "",
            "catalog_targets_total: 7",
            "catalog_non_cfr_targets: 5",
            "scanned_targets: 2",
            "held_parts: 0",
            "audit_only_parts: 0",
            "unheld_parts: 2",
            "total_authority_claims_all_parts: 1",
            "total_authority_claims_held: 0",
            "total_authority_claims_unheld: 1",
            "",
            "queue:",
            '  - part_id: "1-cfr-9999"',
            '    citation: "1 CFR 9999"',
            "    authority_claims: 1",
            "    mentions: 2",
            "    mentions_erf: 2",
            "    mentions_audits: 0",
            '    cited_in: ["erf"]',
            '  - part_id: "2-cfr-8888"',
            '    citation: "2 CFR 8888"',
            "    authority_claims: 0",
            "    mentions: 15",
            "    mentions_erf: 8",
            "    mentions_audits: 7",
            '    cited_in: ["audits", "erf"]',
        ]
        base_lines = header + body

        def run_check(lines: list[str]) -> int:
            fixture_queue.write_text("\n".join(lines) + "\n", encoding="utf-8")
            return scanner.check_queue()

        real_queue_out = scanner.QUEUE_OUT
        scanner.QUEUE_OUT = fixture_queue
        try:
            check("a hand-built, internally-correct fixture file passes --check",
                  run_check(base_lines) == 0, "expected exit 0")

            # #70's own reproduction: catalog_targets_total edited UPWARD used to pass (the
            # old check was a one-directional `<`) -- now caught in both directions, the
            # same as every other declared number here.
            up = list(base_lines)
            up[up.index("catalog_targets_total: 7")] = "catalog_targets_total: 8"
            check("catalog_targets_total hand-edited UPWARD fails --check (#70's own "
                  "reproduction, previously silent)", run_check(up) == 1, "expected exit 1")
            down = list(base_lines)
            down[down.index("catalog_targets_total: 7")] = "catalog_targets_total: 6"
            check("catalog_targets_total hand-edited DOWNWARD fails --check",
                  run_check(down) == 1, "expected exit 1")
            noncfr = list(base_lines)
            noncfr[noncfr.index("catalog_non_cfr_targets: 5")] = \
                "catalog_non_cfr_targets: 4"
            check("catalog_non_cfr_targets hand-edited fails --check too -- the new field "
                  "that reconciles catalog_targets_total is itself checked, not merely "
                  "used to check the other one (#70)",
                  run_check(noncfr) == 1, "expected exit 1")

            # #70 PROVE IT: a brand-new declared summary number, added with no equation
            # naming it, must fail --check STRUCTURALLY -- by enumeration -- not because its
            # own value happens to be wrong. Its value (0) is trivially self-consistent, so
            # the only thing that can be failing it is the coverage scan itself.
            synthetic = list(base_lines)
            idx = synthetic.index("total_authority_claims_unheld: 1")
            synthetic.insert(idx + 1, "synthetic_unrelated_number: 0")
            check("a brand-new declared summary number with no --check equation fails the "
                  "gate on that fact alone (#70 PROVE IT), even though its own value is "
                  "internally harmless -- the structural half of the fix, not a name-by-"
                  "name comparison that would miss it",
                  run_check(synthetic) == 1, "expected exit 1")

            # #69's own reproduction: cited_in hand-edited to erase a source's contribution
            # while that source's mentions_* stays in place used to pass --check silently
            # (replacing ["audits", "erf"] with ["erf"] on a merged row). Now caught.
            drop_audits = list(base_lines)
            i = drop_audits.index('    cited_in: ["audits", "erf"]')
            drop_audits[i] = '    cited_in: ["erf"]'
            check("cited_in hand-edited to erase a source while mentions_audits stays "
                  "nonzero fails --check (#69's own reproduction, previously silent)",
                  run_check(drop_audits) == 1, "expected exit 1")

            bad_erf = list(base_lines)
            i = bad_erf.index("    mentions_erf: 8")
            bad_erf[i] = "    mentions_erf: 9"
            check("mentions_erf hand-edited so mentions_erf + mentions_audits != mentions "
                  "fails --check (#69)", run_check(bad_erf) == 1, "expected exit 1")

            bad_audits = list(base_lines)
            i = bad_audits.index("    mentions_audits: 7")
            bad_audits[i] = "    mentions_audits: 6"
            check("mentions_audits hand-edited so the split no longer sums to mentions "
                  "fails --check (#69)", run_check(bad_audits) == 1, "expected exit 1")
        finally:
            scanner.QUEUE_OUT = real_queue_out

    print()
    if fails:
        print(f"FAILED: {len(fails)} assertion(s): {'; '.join(fails)}", file=sys.stderr)
        return 1
    print("The #63 ranking algorithm sorts by claim, carries mentions alongside without "
          "dropping zero-claim parts, and excludes held parts; #64's audit-mention merge "
          "adds additively to a catalog row and creates a new zero-claim row for an "
          "audit-only part, excluding held parts from either source -- against a "
          "synthetic catalog, held set, and audits directory, never the real corpus or a "
          "real sibling checkout.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
