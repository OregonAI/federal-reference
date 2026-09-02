# Changelog — Federal Reference — instruments Oregon must comply with

Keep a Changelog format; ISO dates. Change types: Added, Source-Updated,
Superseded, Repealed, Removed, Verified, Fixed, Security.
Repo-curation dates only — official effective dates live in frontmatter.

## [Unreleased]

### Fixed
- 2026-09-01 — `split_cfr_sections.py --check` could reach the network and mutate the working
  tree (#58). Two call sites in `run_part()` did the same thing, one layer under the other:
  the historical-snapshot fetch/write for a removed section whose `_meta/snapshots/<id>.xml`
  was not yet committed (`urlopen` + `hist_xml.write` + an unconditional `.txt` write of the
  re-derived text), and `ecfr_versions()` — a live fetch of eCFR's versions endpoint, called
  unconditionally for every part to compute each current section's `amended_on`, found while
  proving the first fix (a fully offline `--check` run crashed inside it). Neither call
  branched on `args.check` before reaching the network. `--check` now refuses instead of
  fetching: a missing historical snapshot is reported as `MISSING SNAPSHOT` (the same
  STALE/ORPHAN/STALE-HEADER shape the rest of `--check` already uses) rather than fetched,
  the historical `.txt` derivation is routed through the same `emit()` every other generated
  file already uses instead of writing unconditionally, and `ecfr_versions()` is skipped
  entirely under `--check` — `amended_on` is instead read back from the section's own
  already-committed document (`committed_amended_on()`, the same "trust what is on disk"
  shape `hist_retrieved()` already uses one field over). `--check --refetch` together is
  rejected outright in `main()` as the nonsensical request it is, rather than defining what
  it would mean. Proved with the network genuinely unreachable (`urlopen` monkeypatched to
  raise) and the working tree made read-only (`chmod`, real `_meta`/`instruments`
  directories): the real corpus (`2-cfr-200`, `34-cfr-300`) still passes `--check` cleanly,
  0 files touched; a synthetic second part with an uncommitted historical snapshot refuses
  cleanly (`rc=1`, `MISSING SNAPSHOT` printed), 0 files written, 0 files mutated, 0 network
  calls, in both cases.
- 2026-09-01 — A per-part `CONSOLIDATIONS` record was attributed to every removed section in
  the part regardless of which amendment actually removed it (#57). `run_part()` groups
  removed sections `by_date` (their own `removed_on`, generalized by #34 for a part whose
  removals span more than one amendment) but looked up `CONSOLIDATIONS.get(part_id)` once and
  passed the same record — and, for the `supersedes` back-edge, *every* removed section from
  *every* date — to `build()` regardless of the record's own `date` field. Not reachable with
  today's data (2 CFR 200's two removed sections and its one consolidation record share the
  same date, 2021-02-22 — confirmed: both the frontmatter `supersedes` on `2-cfr-200.1.md`
  and the "consolidated into" prose on `2-cfr-200.53.md`/`.62.md` are identical before and
  after this fix, 2/2 removed sections attributed both times), but a section removed by a
  *different* amendment than the one the record describes would fabricate which amendment
  moved what. `run_part()` now compares each removed entry's own `removed_on` against
  `consolidation["date"]` before attributing the record to it (and filters the `supersedes`
  sweep to `by_date.get(consolidation["date"], [])`, not every date); a mismatch falls back
  to the generic "no successor section is recorded here" clause `_removal_clause()` already
  gives a part with no record at all. Proved with a synthetic record dated 2021-02-22 and a
  removal dated 2024-05-01: before the fix, the section's prose read "...when Subpart A's
  definitions were consolidated into [§ 1.1]..." — a real amendment's record attached to a
  removal it did not describe; after, "...and no successor section is recorded here." A
  matching-date control (same record, a 2021-02-22 removal) still gets the record's own
  scope/target, confirming no regression on the case #34 already covered.
- 2026-09-01 — Verified #52 (`issuing_body` hardcoded to OMB in `split_cfr_sections.py`, the
  same bug #33 fixed for the part document) is already closed by #34's own generalization
  (`resolve_issuing_body(src)` off the part's manifest entry, not a literal) — #52 was filed
  against a pre-#34 commit and never closed. Measured rather than assumed: all 69 committed
  `34-cfr-300.*.md` documents (68 sections + the part document, the Department of
  Education's IDEA Part B, landed by #66 — a real second, non-OMB part) declare
  `issuing_body: Department of Education`; none say OMB. Satisfies #52's own acceptance
  criterion of verification against a real second part now that one is ingested. No code or
  document change was needed for this one; closed with this measurement as evidence.

### Added
- 2026-09-01 — Scan `oregon-audits` itself in part-discovery mode (#64), not just ERF's
  catalog. `--audits` was required on the CLI since #63 but never read; ranking and every
  `mentions` count came from ERF's catalog alone, which never sees `oregon-audits` at all.
  `scan_audit_mentions()` walks the corpus with its own general CFR-part regex
  (`AUDIT_CFR_RE`, mirroring the shape of ERF's own `FED` pattern) and merges additively
  into a catalog row's `mentions`; a part audits cite that the catalog never does becomes a
  new zero-claim row (`authority_claims` stays 0 throughout — audits carry no
  `legal_authority`/`statutes_implemented` concept, measured across all 255 documents in a
  real checkout, so ranking-by-claim is unaffected). Every row's `cited_in` now names which
  source(s) — `"erf"`, `"audits"` — contributed its `mentions`. `_meta/ingest-queue.yml`
  regenerated with two new fields (`cited_in`, `audit_only_parts`) and `check_ingest_queue.py`
  and `check_queue()`'s `--check` extended to verify both.

  Immediately followed by its own code review, both addressed in this same commit rather
  than filed, since fixing them was cheap in the file the review was already reading:

  `AUDIT_CFR_RE`'s `Part` literal was case-sensitive while every other token in it is
  punctuation/space-tolerant, so lowercase `part` — as in "45 CFR part 155", oregon-audits'
  SECOND-most-cited part — matched nothing. Confirmed: the committed (pre-fix) regex found
  45 distinct parts / 380 mentions across the corpus; `45-cfr-155` was entirely absent from
  the resulting 13 audit-only rows despite 92 real occurrences. A bare case-insensitive
  `[Pp]art` over-corrects, though: it turns an OCR-broken "45 CFR part 1 55"
  (`reports/2020-02.md`) into a spurious `45-cfr-1` row. Fixed with a narrower pattern, not
  a post-hoc filter: `[Pp]art` plus a negative lookahead refusing a part number immediately
  followed by a single space and another digit (that exact OCR split, and nothing else
  matched across the corpus) and another refusing a part number immediately followed by a
  lowercase-letter subsection marker like `(d)`/`(a)` — CFR grammar only attaches those to a
  SECTION citation (`200.331(d)`), never a bare part, and the only two matches this shape
  reaches corpus-wide are two audits' own dropped-"200." typos (`2 CFR 331(d)` in
  `reports/2021-13.md`, `2 CFR 303(a)` in `reports/2024-14.md`, the latter writing the same
  citation in full elsewhere as "2 CFR § 200.303") that the unfixed regex had faithfully
  turned into two more of the 13 audit-only rows. Net: `audit_only_parts` 13 → 11,
  `45-cfr-155` now correctly merged (`mentions: 117` = 25 erf + 92 audits,
  `cited_in: ["audits", "erf"]`, rank 53 → 49), `unheld_parts` 586 → 584.

  `scan_audit_mentions()` walked `audits.rglob("*.md")` from the repository root, so it
  measured the oregon-audits REPOSITORY, not its corpus — AGENTS.md, CHANGELOG.md,
  README.md, STATUS.md and the `.github/`/`docs/agents/` templates (12 non-report files)
  all got counted as "files scanned" alongside the 242 real reports under `reports/`. None
  of the 12 carried a CFR-part mention today (measured), so no live number was wrong, but
  ERF's own `scan_external_citations.py` already hit and fixed the identical bug (its
  comment: "how committing an ADR turned this gate red for nine days", #158 there). Scoped
  the walk to `audits / "reports"`.

  Pointing `--audits` at an empty directory, or one whose `reports/` carries files but no
  CFR-shaped citation, passed `is_dir()` and proceeded to silently overwrite the committed
  queue with an audits-blind one — reproduced against the then-committed 586-row queue: an
  empty `--audits` directory dropped it to 573 rows, every audit-only row and every merged
  audit mention gone, exit 0, and the mutilated file then PASSING `--check` (which only
  verifies self-consistency, not agreement with a fresh scan). The ERF side of the same
  function already refuses this shape of failure (`catalog_path.is_file()`); `discover_main()`
  now refuses identically when the audits scan finds zero files or zero mentions, before
  `write_queue()` ever runs — confirmed against all three broken-path shapes (empty
  directory, one file with no CFR citation, nonexistent path): each now exits 1 with the
  committed queue's md5 unchanged.

  `check_ingest_queue.py`'s synthetic audits fixture updated to exercise all of the above —
  a lowercase "part", the truncated-citation false match, and a file outside `reports/` —
  against the real corpus's own citation shapes rather than the regex read in isolation.

  Two findings filed rather than fixed here, both needing a schema decision this diff's own
  scope doesn't cover: a merged row's `mentions` sums the erf/audits split and discards it,
  so `--check` cannot notice a `cited_in` corruption that erases one source's contribution
  (demonstrated: hand-erasing `"audits"` from a merged row's `cited_in` still passes
  `--check` clean) — federal-reference#69. `catalog_targets_total` is the only one of eight
  declared summary numbers `--check` cannot catch a hand-edit of in either direction
  (pre-existing since #63, not new to this branch) — federal-reference#70.

  Gates re-run clean: `anchor_sections.py --check`, `build_graph.py --check`,
  `build_site.py`, `check_citations.py`, `check_extraction.py`, `check_issuing_body.py`,
  `check_ingest_queue.py`, `check_section_split.py`, `check_source_urls.py`,
  `refresh_source_hashes.py`, `split_cfr_sections.py --check`, `scan_cited_sections.py
  --erf . --audits . --check`.

- 2026-08-31 — Ingest 34 CFR 300, the IDEA Part B (special education) regulations
  (#66) — the first instrument chosen by `_meta/ingest-queue.yml` (#63) rather than by
  curation: rank 1 of 574 unheld CFR parts at 105 authority claims and 129 mentions, three
  times the next-ranked part and never named in any of #22–#25's hand-picked candidates.
  Manifest entry added to `_meta/source-manifest.yml` (`issuing_body: "Department of
  Education"`, `signal: "authority"`) per ADR-0005. `scan_cited_sections.py --title 34
  --part 300` found 244 section-shaped citations across 69 distinct sections; 68 graduated
  to their own document per ADR-0003, sharing the part's snapshot via `snapshot_id`. One
  citation, `34 CFR 300.344`, has NO eCFR version record at all — not current, not a
  recorded removal — almost certainly a pre-2006 section number left over from before this
  part's own SOURCE recodification (71 FR 46753, Aug. 14, 2006) that OAR 581-015-2210 was
  never updated past. Named rather than silently dropped in a new `unresolvable:` bucket
  (see the "Fixed" entry below); not split, since there is no snapshot to cut a document
  from without fabricating text. Zero sections were removed. Citations concentrate in two
  subparts rather than one: Subpart B (State Eligibility, 27 sections cited, 75 citations)
  and Subpart E (Procedural Safeguards, 17 sections, 68 citations) together account for 59%
  of the 242 current-section citations; Subparts G and H (funding/allotment, preschool
  grants) drew zero. `_meta/ingest-queue.yml` regenerated: 34 CFR 300 left the queue,
  `held_parts` 1 → 2, `total_authority_claims_held` 15 → 120 (15 + 105).

  **Not fixed, reported precisely per #66's own instruction to surface rather than work
  around any place the generalized pipeline still assumes 2 CFR 200:** `_cfr()` in
  `src/citation_schemes.py` only expands a multi-section citation ("34 CFR 300.344, 300.321,
  300.324") into all its members when the part is literally `2-cfr-200` (`PART_ID`) — a gate
  filed as #55 during #35, before any second part was held. `34 CFR 300.344, 300.321,
  300.324(a)(3) & (b)(3)` is exactly this shape and is the stated authority for OAR
  581-015-2210; resolving it today returns nothing, because `_cfr_one()` fails on the first,
  unresolvable member (`300.344`, see above) and the gate prevents falling through to try
  `300.321`/`300.324`, both of which this change holds as their own documents. #55's own
  "what would fix it" already names the reason this PR does not: `RANGE`/`LIST_SEC` live in
  `src/federal_ids.py`, a parity-locked cross-corpus contract file copied verbatim into
  sibling repos, so generalizing the expansion is a coordinated multi-repo change and not
  this ingest's file. Filed as a fact against #55 rather than reopened, since #55 already
  states this precisely; not routed around in `_cfr()` here.

  Copyright determined per ADR-0002, not assumed from "federal, therefore reproducible":
  `reproduction_basis: "17 U.S.C. § 105 — edition of the CFR published by the U.S.
  government"`, the same basis already checked and recorded for 2 CFR 200 — the CFR itself
  carries no separate distribution restriction independent of that determination.

  Gates re-run clean: `anchor_sections.py --check`, `build_graph.py --check`,
  `build_site.py`, `check_citations.py`, `check_extraction.py` (6/6 documents),
  `check_issuing_body.py`, `check_section_split.py`, `split_cfr_sections.py --check`,
  `scan_cited_sections.py --erf . --audits . --check`, `check_ingest_queue.py`,
  `corpus-validate-frontmatter` and `corpus-verify-provenance` (112/112 documents).
  `check_source_urls.py` now passes too: it was hitting the same 406 as the fetch bug below,
  from the identical cause (no `Accept-Encoding` header on the same eCFR endpoint), so the
  fix is the same fix — see the "Fixed" entry.

### Fixed
- 2026-08-31 — eCFR's `/full/<date>/title-N.xml` endpoint now rejects a request with no
  `Accept-Encoding` header (`406 Not Acceptable: This endpoint requires response
  compression`), which surfaced the moment #66 needed a REAL fetch — `ingest_instruments.py
  --only 34-cfr-300` failed outright, and 2 CFR 200's identical code path had gone
  untested since its snapshot was already cached. `ingest_instruments.fetch()` now sends
  `Accept-Encoding: gzip` and decompresses the response by hand (`urllib` never does this on
  its own even when a request declares it can accept a compressed body).
  `split_cfr_sections.py`'s historical-snapshot fetch hit the same endpoint shape with the
  same bug; it now calls the fixed `fetch()` instead of a second raw `urlopen()`, so the fix
  lives in one place. `src/check_source_urls.py` sends its own independent request and had
  the identical gap, so it was failing this fetch too, not just the two pre-existing 2 CFR
  200 URLs main already fails on — now sends the same `Accept-Encoding: gzip` header and
  decompresses the same way. Confirmed: `ingest_instruments.py --only 34-cfr-300` now
  succeeds, `check_extraction.py` passes for the resulting document, and
  `check_source_urls.py` now exits 0 (0 of 111 source URLs unreachable, was 3).

  `scan_cited_sections.py` treated a section citation with NO eCFR version record at all
  (distinct from a RECORDED removal) as a hard failure (`return 1`), which blocked #66 from
  producing `_meta/cited-sections/34-cfr-300.yml` at all once `34 CFR 300.344` turned up
  with no record. Added a third `unresolvable:` bucket alongside `current:`/`removed:`,
  written to the committed YAML and printed as a named warning rather than crashing the
  scan — never split into a document, since there is no snapshot to cut one from.
  `split_cfr_sections.py --check`'s header-staleness check verified the `current:`/
  `removed:` comment blocks but not this new one, so a file regenerated before the
  `unresolvable:` key existed (`_meta/cited-sections/2-cfr-200.yml`, untouched by #66 until
  now) passed `--check` while silently missing it; the check now verifies the
  `unresolvable:` block too, and `2-cfr-200.yml` is regenerated to carry it (0 entries —
  none of 2 CFR 200's cited sections are unresolvable, only removed or current).

  `scan()` counted the same citation twice whenever it was written `34 CFR § 300.NNN`:
  `section_re` already permits the `§`, so `short_re` then re-matched the identical span a
  second time as a "bare short form." Fixed to skip a short-form hit whose span falls inside
  a full-citation match. This was already live for 2 CFR 200 (26 double counts across 9
  sections) and is not new to this change, but it sits in a file #66 already edits, so fixed
  here rather than filed: `total_citations` for 34 CFR 300 moves 255 → 244 (`2-cfr-200.yml`:
  257 → 231), and both cited-sections files and every section document whose stated
  "Cited by Oregon material" count changed have been regenerated to match.

- 2026-08-31 — Address code review of #63 (the derived ingest queue). Four HARD findings,
  each confirmed to reproduce before its fix.

  `discover_main()`'s zero-unheld-parts refusal wrote the queue first and then
  `unlink(missing_ok=True)`'d the committed `_meta/ingest-queue.yml` — an error path
  destroying a reviewed artifact as a side effect. Reproduced: pointed `--erf` at a
  synthetic catalog with `targets: []`; the script printed its refusal to stderr, exited 1,
  and the committed file was gone (`ls` → no such file). `write_queue()` is now split into a
  pure `build_queue_lines()` (computes, touches no path) and `write_queue(lines)` (the only
  place `QUEUE_OUT` is written); `discover_main()` calls the former, checks `unheld_n == 0`,
  and returns before the latter ever runs. Confirmed fixed with the same repro: the
  committed file's md5 is now identical before and after a zero-target run.
  `check_ingest_queue.py` gained a real assertion for this ("zero is a refusal" — #63's own
  Testing Decisions named this required and nothing exercised it) calling
  `build_queue_lines()` directly on an all-held fixture catalog and checking `unheld_n == 0`
  — and its comment falsely claiming `write_queue()`/`discover_main()` were "exercised
  below" (they were called nowhere in the file) is now accurate.

  `check_queue()`'s `--check` never verified `total_authority_claims_all_parts` or
  `total_authority_claims_held` against anything — only `total_authority_claims_unheld`,
  `unheld_parts`, and `scanned_targets` were checked. Confirmed by hand-corrupting each of
  the two unchecked fields in turn and re-running `--check`: both passed silently
  ("574 entries internally consistent"). `check_queue()` now asserts
  `total_authority_claims_all_parts == total_authority_claims_held +
  total_authority_claims_unheld` against the committed file's own declared numbers (the one
  fact checkable without a sibling checkout); re-run against both corruptions, both now
  fail with the exact arithmetic that's wrong.

  The header's "Regenerate with:" command named `--erf ../oregon-policy-repo`, a path that
  does not exist and never has in this checkout (`ls ../oregon-policy-repo` → no such
  directory; the real sibling is `../executive-regulatory-frameworks`, confirmed by its own
  `git remote -v`). Fixed in `scan_cited_sections.py` (module docstring, `static_header()`,
  `queue_header()`, and `check_queue()`'s re-run hint) and regenerated both committed
  artifacts that carry the printed command (`_meta/ingest-queue.yml` and
  `_meta/cited-sections/2-cfr-200.yml`, the latter changing only its two header lines — same
  257 citations, 38 sections, 2 removed, confirming the path was the only thing stale).
  `split_cfr_sections.py` and `README.md` carry the same stale path in files this change
  does not otherwise touch; left alone rather than chased, since fixing them needs no
  regeneration and widens this diff for no behavior change (`split_cfr_sections.py`'s is an
  unchecked stderr hint; `README.md`'s is untested prose).

  Alongside: `scanned_targets` (575) silently reported only the CFR-shaped subset of ERF's
  catalog (1358 targets total — 783 USC citations and named instruments discarded with no
  field naming the discard). Added `catalog_targets_total`, checked against `scanned_targets`
  by `--check` (the subset can never exceed the whole), and a header comment clarifying that
  `held_parts` similarly counts held parts only among the CFR-shaped catalog subset, not
  every CFR part this corpus holds.

  One HARD finding filed rather than fixed here, per this repo's own standard (needs a
  scope decision, and fixing it would grow this diff past what one review should cover):
  `--audits` is a required CLI flag in part-discovery mode but its content is never scanned
  — only ERF's catalog is read. Measured directly against the real `oregon-audits` checkout:
  380 CFR-part mentions across 45 distinct parts, 13 of them (2 CFR 170, 45 CFR 265, 45 CFR
  264, ...) absent from ERF's catalog and therefore absent from the queue entirely, and
  several catalog parts undercounted on `mentions` by up to 9x (45 CFR 75: queue says 3,
  audits alone carry 28). Does not change the ranking of what to ingest next — audits carry
  no `legal_authority`, so no part's `authority_claims` are affected — but degrades story 3's
  visibility promise for audit-only-cited parts. Filed as federal-reference#64.

  Gates re-run clean: `anchor_sections.py --check`, `build_graph.py --check`,
  `build_site.py`, `check_citations.py` (138 assertions), `check_extraction.py` (5/5
  documents), `check_issuing_body.py`, `check_section_split.py`, `split_cfr_sections.py
  --check`, `scan_cited_sections.py --erf . --audits . --check`, `check_ingest_queue.py`
  (15 assertions).

- 2026-08-28 — Address code review of #34 (`git diff 3961413f22d25192816cd0d450d52e7e78adb8c3
  ...HEAD`). Three HARD findings, all confirmed to reproduce before their fix and quoted below.

  `split_cfr_sections.py`'s `run_part()` crashed on the FIRST real second part. A part with no
  removed sections gets a bare `removed:` key from `scan_cited_sections.py`, which YAML loads
  as `None`, and `run_part()` iterated it unguarded. Reproduced end to end: scanned the real
  citing corpora for 6 CFR 37 (`--title 6 --part 37` → 8 current, 0 removed, matching the
  §37.11/§37.3 ranking the issue predicted), built a synthetic 6-cfr-37 snapshot + manifest
  entry + part document, and ran the splitter against it — `TypeError: 'NoneType' object is
  not iterable` at the `for entry in cited["removed"]` line. `cited["current"]`/`cited["removed"]`
  are now normalized with `cited.get(key) or []` right after load, the same guard
  `ingest_instruments.cited_section_ids()` already used one file over; the same repro now
  writes 8 correct section documents, each carrying `issuing_body: Department of Homeland
  Security`.

  AC5 ("a test covers the short-form disambiguation guard using the ORS chapter 164 collision
  as its fixture") was unmet, and worse: `check_section_split.py`'s assertion re-implemented
  the guard's gating logic inline instead of calling `scan()`, so it tested two regexes and
  never the production code. Confirmed by mutation: removing the guard from `scan()` entirely
  (`hits = hits + short_re.findall(text)`, unconditional) left the assertion printing `ok` and
  every gate green. The assertion now builds the exact fixture AC5 asks for — a temp file
  citing ORS 164.377 (computer crime) and ORS 164.140 (criminal possession), the two sections
  #27's own triage named, with bare `§164.NNN` references and no "45 CFR" anywhere — and calls
  `scanner.scan()` on it directly, asserting zero counts; a positive-control fixture (a file
  that DOES carry "45 CFR 164") proves the assertion isn't vacuously trivial. Confirmed to
  fail against the mutated guard and pass against the real one.

  The committed `_meta/cited-sections/2-cfr-200.yml` had been `git mv`'d (100% similarity) but
  never regenerated, so its own "Regenerate with:" line printed a command missing
  `--title`/`--part` and its comment still said "the committed 2026 part snapshot". Confirmed
  by running the printed command verbatim (argparse exit 2) and then regenerating for real
  with `--title 2 --part 200`: the section list and both removed entries (200.53, 200.62)
  reproduce with identical eCFR evidence; the only deltas are the two header lines plus
  genuine corpus growth since the last scan (scanned_files 75555→76701, and 200.333's citation
  count 2→3, which `split_cfr_sections.py --part-id 2-cfr-200` then propagated to
  `instruments/2-cfr-200.333.md`'s "Cited by Oregon material" line — its only change).
  `scan_cited_sections.py` now exposes the static, scan-independent header lines
  (`static_header()`, `CURRENT_COMMENT`, `REMOVED_COMMENT`) as a single source of truth
  instead of duplicated string literals, and `split_cfr_sections.py --check` compares a
  committed file's header against them for its own part id, offline, every PR — the "generated
  file with no step in the `generated` job" gap the review named as contributing cause, closed
  without adding a new CI step (the existing `--check` step now covers it). Confirmed the new
  check fails against the pre-regeneration header and passes against the regenerated one.

  AC3 ("re-running the splitter for 2 CFR 200 reproduces all existing section documents
  byte-identically") was flagged HARD as unmet-but-undecided: 43 documents changed, disclosed
  and argued in this file and the splitter's own docstring, but the review asked for an
  explicit accept/renegotiate decision rather than a green `--check` standing in for one.
  Decision recorded on #34: accepted as documented — every frontmatter field and the `## Full
  text` payload are unchanged (`check_extraction.py` token-for-token), and the two prose
  deltas are a direct, intended consequence of removing the same two hardcodes this branch
  exists to remove.

  Three JUDGEMENT findings fixed alongside. `sections_from()`'s heading regex was missing its
  leading `\b`, so a short part number could match inside a longer one — part "1" matched
  "§ 21.5" at "1.5" (confirmed by direct regex test); harmless for 200/37/35/99, not harmless
  once the part number is an input. The `target_doc` derivation (which document a recorded
  consolidation's `into` section lands in) was written three times with a DIFFERENT fallback
  in each copy — now one `_target_doc(part_id, consolidation, default)` helper, the fallback
  argument making the divergence visible instead of implicit. `discover_part_ids()` globbed
  every `*.yml` in `_meta/cited-sections/` and handed it straight to an unguarded 2-tuple
  unpack; a stray file there (confirmed with a `README.yml` fixture) crashed CI with a bare
  `ValueError` traceback instead of this file's usual named error — now filtered by shape with
  a named refusal.

  Two JUDGEMENT findings filed rather than fixed here, per this repo's own standard: #57 —
  `CONSOLIDATIONS` is looked up once per PART and applied to every removed section regardless
  of that section's own `removed_on`, so a section removed by one amendment could be
  attributed to a different one's recorded target (not reachable with today's single-date
  data, but the same shape of latent hardcode #34 exists to remove); #58 — `run_part()`'s
  historical-snapshot fetch reaches the network and writes to disk even under `--check`,
  which should be a pure read-and-compare step.

  Gates re-run clean: `split_cfr_sections.py --check`, `anchor_sections.py --check`,
  `build_graph.py --check`, `check_citations.py` (138 assertions), `check_extraction.py`
  (5/5 documents, token-for-token), `check_section_split.py`, `check_issuing_body.py`.

- 2026-08-27 — Generalized the demand-driven CFR section split beyond 2 CFR 200 (#34), the
  last of the three hardcodes this branch removes (#33 for issuing_body, #35 for citation
  resolution). Four files assumed there was exactly one part:

  `src/scan_cited_sections.py`'s citation regexes and eCFR version lookup took `--title` and
  `--part` instead of the literal `2`/`200`, and its output moved from one committed file to
  one per part (`_meta/cited-sections/<title>-cfr-<part>.yml`) — a second part's cited
  sections used to have no file to live in at all.

  `src/split_cfr_sections.py`'s part id, fetch URL, section-number regex, and
  heading-stripping regex were all module-level constants true only of 2 CFR 200; all four
  are now derived from `--part-id` (or discovered from every committed cited-sections file).
  Historical (removed-section) snapshots are now fetched per DISTINCT removal date rather
  than one hardcoded date for the whole part, and the `supersedes` back-edge on a
  consolidation target is computed from the removed entries actually pointing at it instead
  of a literal pair of section numbers. Two more hardcodes travelled alongside these and are
  fixed here, both flagged by #33's own review: `issuing_body` was the literal "Office of
  Management and Budget" in this file too (fixed for `ingest_instruments.py` by #33, not
  here) and now reads the part's own manifest entry; the removed-section note's "consolidated
  into" claim was a second, independently-worded hardcode of the same fact #35 already
  recorded once in `citation_schemes.py` — both callers now read one shared record
  (`src/cfr_consolidations.py`), so they cannot describe an amendment two different ways.
  Regenerating 2 CFR 200 is NOT byte-identical as a result: two prose sentences ("- Part: 2
  CFR 200 (Uniform Guidance)" and the consolidation clause) now read from the manifest/shared
  record instead of a literal, and both are still true. Every field is unchanged.

  `src/slicing.py`'s `SECTION_ID` pattern matched only `2-cfr-200.NNN`, so a second part's
  section document fell through to the identity slice and had its provenance coverage
  measured against the WHOLE part — the exact near-0% failure this file's own docstring says
  it exists to prevent, live for any part ingested since it was written, not merely latent.
  Generalized to any `{title}-cfr-{part}.{section}`.

  `src/ingest_instruments.py`'s `cited_section_ids()` read one hardcoded file and prefixed
  every id with the literal `"2-cfr-200."`; its call site gated on `rid == "2-cfr-200"`
  rather than `instrument_kind == "cfr_part"` — so a second part's document would silently
  publish `relationships: {}`, indistinguishable from a part genuinely cited at zero
  sections. Both now read/gate per part.

  All four are proven against a SYNTHETIC second part (6 CFR 37) in the new
  `src/check_section_split.py`, wired into the `generated` CI job — the same reason
  `check_issuing_body.py` exists for #33: regenerating 2 CFR 200 (`split_cfr_sections.py
  --check`, above) is a no-regression check on the FIRST part, which passes the same whether
  these files still assume one part or not, since 2 CFR 200 is that one part either way, and
  #34's own queued second instrument is not ingested yet. Confirmed
  every new assertion fails against the pre-fix code (`git stash` of the five changed
  modules; `scan_cited_sections.patterns` does not exist at all, `split_cfr_sections --check`
  cannot find the migrated cited-sections file).

  `_meta/cited-sections.yml` moved to `_meta/cited-sections/2-cfr-200.yml`; README.md and
  ADR-0003 updated to match.

- 2026-08-27 — Follow-up to the CFR resolver fix below, from review of #35
  (`git diff acd8622f8995be193f4bde9123555093b1e86477...HEAD`). Two HARD findings, both
  confirmed to reproduce before the fix and quoted below, and neither latent — one live in
  the committed fixture, one reachable the moment a document's frontmatter `id` diverges
  from its filename.

  The generalized consolidation note fabricated a fact for any part other than 2 CFR 200:
  `_CONSOLIDATIONS` recorded only `date` and `into`, but the message asserted WHAT was
  consolidated — "Subpart A's definitions" — hardcoded from 2 CFR 200 into a now-per-part
  sentence. Reproduced: giving a synthetic 6 CFR 37 a `_CONSOLIDATIONS` entry with no
  `scope` key produced "...which consolidated Subpart A's definitions into § 37.5" — a fact
  nothing recorded about 6 CFR 37. `_CONSOLIDATIONS` entries now carry a `scope` (2 CFR
  200's is "Subpart A's definitions", the only part that record was ever true for); the
  clause is only interpolated when a `scope` is actually recorded, and a part with an entry
  but no `scope` gets the same true, less specific note as a part with no entry at all.

  AC5 — "a check exists that the resolver's 'does not hold' claims agree with the corpus
  index" — was unmet: the committed fixture asserted one synthetic part by hand but nothing
  compared resolver output against the index generally. `check_citations.py` now walks
  every part `_held_cfr_parts()` says is held and asserts each resolves to itself, run
  against both the real corpus and the fixture's synthetic second part, through the module
  the framework actually serves from (see below) — confirmed to fail (6 assertions) when
  `_cfr_one`'s held-check is reverted to a `(title, part)` literal comparison.

  Two JUDGEMENT findings fixed alongside: the fixture wrote its state into
  `src.citation_schemes`, a plain import distinct in `sys.modules` from the
  corpus-root-hashed alias `CorpusFramework` actually registers (`corpus_toolkit/plugins.py`
  namespaces it precisely so sibling corpora sharing the `src.citations` convention do not
  collide) — confirmed distinct (`sys.modules` holds two objects for one file) and that
  patching only the plain import left `fw.resolve_citation("6 CFR 37")` still refusing.
  Fixture assertions now patch the module `CorpusFramework` actually loaded, located via the
  same alias formula `_collect_schemes` uses. The fixture also proved only the split-section
  case (case 1) for a second part; extended to exercise all four section cases — including a
  second `_CONSOLIDATIONS` entry with no `scope`, the exact shape that reproduced the
  fabrication above — each confirmed to fail when its guarded behaviour is reverted.

  One more HARD finding, not in the fixture but reproduced directly: `_current_section_numbers`
  converted a loud import-time failure into a silent `frozenset()` on a missing part document.
  Reproduced: a `HELD` entry for a `cfr_part` with no matching `instruments/*.md` file made
  `_cfr_one("9", "1", "5")` answer "there is no § 1.5 in 9 CFR 1" — a confident claim about
  contents made without being able to consult them, on a part being simultaneously served,
  exactly the class #35 exists to close, one field over. Unreachable today (every `HELD` id
  currently matches its filename) but not exercised by anything before this. Now raises,
  naming the mismatched id and path; `check_citations.py` gained a fixture for it, confirmed
  to fail (silently returns rather than raising) when the guard is reverted.

  Two further true-but-cosmetic-looking findings, both real: the "never existed" refusal
  had dropped the clause that distinguishes it from "removed" — restored, naming the
  snapshot date(s) actually consulted (diffed old vs. new output on `2 CFR 200.9999`:
  "...as of 2026-07-29" now reads "...as of 2026-07-29, and none in the 2021-02-21 text
  either", matching pre-#35 wording). And `_former_section_numbers`'s docstring promised
  "any DATED snapshot" while its glob (`{base}-*.txt`) would silently absorb a same-prefix
  non-snapshot file (`2-cfr-200-draft.txt`) into the historical union — now filtered through
  a `-\d{4}-\d{2}-\d{2}\.txt$` pattern; confirmed a synthetic `-draft.txt` snapshot is now
  excluded where it previously would not have been.

  `_current_section_numbers`/`_former_section_numbers` also dropped their redundant `part`
  parameter — `part` is always `base.split("-cfr-", 1)[1]`, so the pair could disagree with
  nothing to catch it; now derived from `base` alone. `check_citations.py`'s duplicated
  mid-function `import src.citation_schemes` was reduced from two to one — NOT hoisted to
  module scope as the review suggested: verified that breaks the script outright
  (`ModuleNotFoundError: No module named 'src'`), because it is invoked as
  `python3 src/check_citations.py`, which puts only `src/`'s own directory on `sys.path[0]`;
  the repo root only reaches `sys.path` as a side effect of `CorpusFramework.__init__`
  loading the citation module, which runs after any top-level import would already have
  failed.

  Declined: routing every fixture assertion through `fw.resolve_citation()` rather than
  calling `_cfr_one` on the located served module directly. That path additionally requires
  `self.backend.exists(id)` or a graph node, both reading the REAL `instruments/` and
  `_meta/graph.json` — faking those for a synthetic part is mocking framework internals this
  file does not own, disproportionate to what the finding asked for; the module-identity fix
  above closes the actual gap (state written into the module the framework serves from).

  Filed as its own issue rather than fixed here: #56 — `instrument_kind` (the field
  `_held_cfr_parts()` gates held-ness on) is free-text in `_meta/corpus.yml`'s
  `extra_document_fields`, with no enum enforcement anywhere in `corpus_toolkit`'s schema
  layer (verified: no such mechanism exists). A held part whose `instrument_kind` is spelled
  differently from the literal `"cfr_part"` would be refused by name while being served, and
  nothing added here — including the new AC5 loop — can catch it, because the loop only ever
  sees documents `_held_cfr_parts()`'s own filter already agrees are held.

  Gates re-run clean: `split_cfr_sections.py --check`, `anchor_sections.py --check`,
  `build_graph.py --check`, `check_citations.py` (138 assertions, up from 129),
  `check_extraction.py` (5/5 documents, token-for-token).

- 2026-08-27 — The CFR citation resolver (`_cfr_one` in `src/citation_schemes.py`) compared
  every citation's `(title, part)` against a literal `("2", "200")` and refused everything
  else with "this corpus holds 2 CFR 200 ... and does not hold {title} CFR {part}" — a claim
  about corpus contents made without consulting corpus contents (#35). A newly ingested part
  would sit in `HELD`, loaded from its own document's frontmatter exactly like 2 CFR 200 is,
  and still be reported not held: "could not check" reported as "is not there" in the field a
  consumer trusts most. Reproduced with a fixture per #35's own AC ("must not depend on any
  queued ingest having landed"): a synthetic 6 CFR 37 part-and-section pair written directly
  into `HELD` and resolved through `_cfr_one`, confirmed to fail against the old literal
  before the fix and pass after. Held-ness is now read from `HELD` for any `(title, part)`,
  the refusal for a genuinely unheld part now lists what IS held instead of hardcoding
  2 CFR 200, and the four section-level cases (split document, unsplit-but-current, never
  existed, removed/superseded) generalize per part — section-heading matching and the
  former-vs-current snapshot diff are computed per part id rather than once at import for
  2 CFR 200 alone. The one piece of section history that cannot be derived from a snapshot
  diff — WHERE a consolidated section's content went — stays hand-recorded per part
  (`_CONSOLIDATIONS`), so 2 CFR 200's "consolidated into § 200.1" note is unchanged and a
  part with no such record gets a true, less specific note instead of an invented one.
  `_cfr()`'s multi-section range/list expansion stays gated to 2 CFR 200 only, because it
  depends on `federal_ids.py`'s `RANGE`/`LIST_SEC` patterns, which are hardcoded to a literal
  `200.` and are a parity-locked cross-corpus contract file — generalizing those is a larger,
  coordinated cross-repo change, filed separately as #55 rather than folded in here.
  `check_citations.py` gained the fixture assertions above, wired into the existing
  `generated` CI step it already runs in.

- 2026-08-27 — Follow-up to the `issuing_body` fix below, from review of #33
  (`git diff 75db04f4...HEAD`). The commit landed a real, minimal fix but left AC7
  ("any defect discovered and not fixed here is filed as its own issue") unmet: the
  identical OMB literal in `split_cfr_sections.py` (frontmatter + prose, both unconditional)
  was recorded only as a comment on #34, whose body lists `issuing_body` under Out of
  scope — exactly the mitigation AGENTS.md rules out by name. Filed as its own issue, #52,
  and #34's Out-of-scope line and acceptance criteria corrected to point at it rather than
  disclaim it, since #34's own AC1 (6 CFR 37, DHS's) would otherwise reproduce #33's bug at
  the section-document layer the moment the splitter is parameterized. `ingest_instruments.py`
  also reordered: `resolve_issuing_body()` is now called before any side effect, not only
  before `build()`, because a manifest entry missing its issuer used to still get its raw
  text snapshot written and its manifest `sha256` line recorded before the `ValueError` fired
  — reproduced directly (`_meta/snapshots/<id>.txt` written, 5,280 bytes; manifest sha256
  line edited) and confirmed it crashes `check_extraction.py` with an unhandled `KeyError`
  instead of a clean `FAIL` (filed separately as #53, since that fragility is general, not
  specific to this path, and is a different review surface). The manifest's `issuing_body`
  authoring note modeled abbreviated examples ("DOJ", "HHS/SAMHSA") against a corpus where
  every issuer today is spelled out in full — corrected, and the convention stated
  explicitly, so the five queued ingests (#21, #26, #27, #37, #41) do not each hand-fill it
  inconsistently; the duplicate copy of that note inline on the 2-cfr-200 entry now points at
  the top-of-file note instead of restating it. Added `src/check_issuing_body.py`
  (wired into the `generated` CI job): the only prior evidence for the fix was 2 CFR 200
  regenerating byte-identically, which is a no-regression check on the FIRST part and reads
  the same whether the bug is fixed or not — nothing exercised a SECOND part through
  `resolve_issuing_body()` at all, since `ingest_instruments.py` runs in no workflow. The new
  check asserts a synthetic DOJ fixture resolves independently of an OMB fixture, that a
  missing issuer raises naming the entry, and is confirmed to fail when the old per-kind
  dict behavior is reintroduced. CONTRIBUTING.md's `Assisted-by:` trailer, missing from
  3dd6b4b (the #33 commit — not amended; declined per this task's explicit instruction not
  to rewrite that commit), is applied to this commit and filed as #54: the convention has
  no CI enforcement, so it will keep being missed silently otherwise.

### Fixed
- 2026-08-27 — `issuing_body` for `cfr_part` was a dict literal keyed on `instrument_kind`,
  so every CFR part was stamped `"Office of Management and Budget"` regardless of which
  agency actually issued it — correct for 2 CFR 200, wrong the moment a second part
  (42 CFR 2 is HHS/SAMHSA's, 28 CFR 35 is DOJ's) is ingested (#33). `resolve_issuing_body()`
  now reads the value from the source's own manifest entry for `cfr_part` — data a reviewer
  can see and check at PR time — and raises, naming the offending entry, when a `cfr_part`
  omits it; the other three kinds (`irs_publication`, `fbi_policy`, `public_law`) are
  genuinely constant per kind and stay table-driven. 2 CFR 200's manifest entry now declares
  `issuing_body: "Office of Management and Budget"` explicitly; its regenerated document
  is byte-identical to the one this replaces (verified: `diff` against the pre-change copy
  exits 0).

### Added
- 2026-08-11 — `CONTEXT.md` and `docs/adr/0001`–`0005`. Domain vocabulary and five
  load-bearing decisions that were previously recorded only in docstrings and manifest
  notes: current-text-only storage, per-document copyright determination, demand-driven
  section splitting, the no-codified-U.S.-Code boundary, and the hand-authored manifest.
  Nothing here is a new decision — each ADR cites where the decision already lived. Written
  because the decisions were being re-derived from source comments during triage, and
  ADR-0004 is now under active challenge with nowhere to record the challenge. `CONTEXT.md`
  also names two things the code knew but had not named: the mention-vs-authority-claim
  distinction, and the acronym collisions (ORS chapter numbers vs CFR parts, CISA, SNAP,
  NIST) that have each produced a wrong measurement.

### Fixed
- 2026-08-02 — `llms.txt` was still the template stub (#10): the `## Contents`
  section carried the placeholder comment with zero entries, the preamble
  claimed third-party materials are "summarized with links" when every document
  here is `content_mode: verbatim`, and the description line ended in a stray
  `..`. Contents now indexes `instruments/`, the cited-sections derivation, the
  source manifest, and the authority graph; the preamble states the verbatim
  reality. (The CHANGELOG half of #10 was resolved by earlier entries.)

### Added
- 2026-08-03 — Section anchors for the big PDF instruments: WIOA (157), Perkins V
  (29), IRS Pub 1075 (69) — `### ` prefixes on the documents' own heading lines,
  in both snapshot and body, adding no words (check_extraction still passes
  token-for-token). With toolkit v1.21.0 these serve as navigable subsections:
  get_document lists them and `part='SEC. 188.'` returns one section of a 900 KB
  statute alone. CJIS deferred with the reason recorded (two incompatible
  numbering systems; incorporated-standards reproduction question). Section
  DOCUMENTS were deliberately not minted: zero of ~300 Oregon mentions are
  section-shaped (2 CFR 200's split answered the opposite measurement); the
  demand trigger is recorded in scan_cited_sections.py.
- 2026-08-03 — `federal-act-name` citation scheme: bare `WIOA` / `Perkins V` /
  full act names (previously resolving to NOTHING) now resolve to their
  documents with a navigation note; `Title N` qualifiers return the title's
  section range, derived from the anchors, never hand-maintained.

### Fixed

- `as_of` and `retrieved` are now taken from the source rather than the wall clock
  (#8). `as_of` for the CFR part comes from the point-in-time date pinned in the eCFR
  URL — the document claimed 2026-07-30 while its own `source_url` said 2026-07-29.
  `retrieved` advances only when bytes were actually fetched; it previously moved
  forward on every re-run, so the older a cached snapshot got, the fresher it claimed
  to be. The superseded sections 200.53 and 200.62 no longer inherit the part's
  retrieval date: they are cut from a separately fetched point-in-time snapshot and
  now carry its date.
- `extract_cfr` no longer drops the part's own AUTHORITY block, SOURCE note, part
  heading and six subpart headings (#9). 2 CFR 200 gains 517 characters, including
  `31 U.S.C. 503; 31 U.S.C. 6101-6106; 31 U.S.C. 6307; 31 U.S.C. 7501-7507.` — the
  statutory basis for the entire part, previously absent from a corpus whose purpose
  is recording what a requirement rests on.
