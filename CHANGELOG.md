# Changelog — Federal Reference — instruments Oregon must comply with

Keep a Changelog format; ISO dates. Change types: Added, Source-Updated,
Superseded, Repealed, Removed, Verified, Fixed, Security.
Repo-curation dates only — official effective dates live in frontmatter.

## [Unreleased]

### Fixed
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
