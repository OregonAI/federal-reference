# ADR-0003 — Split only the sections Oregon actually cites, and derive that list

**Status:** Accepted. Recorded here 2026-08-11 from the docstrings in
`src/scan_cited_sections.py` and `src/split_cfr_sections.py`, and from
`_meta/cited-sections.yml` (since #34, one file per part under `_meta/cited-sections/`).

## Context

A CFR part holds hundreds of sections. Oregon rarely cites the part — 85% of the
section-or-part citations to the Uniform Guidance are section-level (256 of 300), and
§ 200.303 alone accounts for 58. A corpus holding only the part answers "2 CFR 200" and
misses every one of those, so sibling edges resolve the least-cited form of the citation
and nothing else.

Splitting every section of every part is the other extreme: hundreds of documents, most
never cited by anyone.

## Decision

**Anchors first, documents when demanded.** A part is ingested whole, with its sections as
headings. A section is promoted to its own document only when measurement shows Oregon
citing it.

The split list is **derived, not chosen**: `src/scan_cited_sections.py` scans the citing
corpora and writes `_meta/cited-sections.yml`, which is committed and reviewed.

**A cited section that no longer exists is a finding, not a drop.** Two of the 29 (200.53,
200.62) were removed from the CFR. Omitting them silently would leave four real audit
citations pointing at nothing; resolving them to current text would answer a compliance
question with law that was not in force. Both are ingested from a point-in-time snapshot of
the day before removal, marked `superseded`, with `superseded_by` naming § 200.1.

**The scan runs on a developer machine, and its output is committed.** CI cannot reach
executive-regulatory-frameworks or oregon-audits — they are separate repositories and are
not checked out. A build-time scan would find zero citations and split nothing, reporting
success while doing nothing.

## Consequences

Sections are sliced from the part snapshot already on disk, with `snapshot_id` pointing at
it, so a section document cannot disagree with its part.

**The disambiguation guard is per-instrument reasoning, not a constant.** Bare `§200.NNN`
is counted only in files that also carry a full `2 CFR 200` citation, because ORS has a
chapter 200 too. This guard must be re-derived for every instrument, not inherited: for
45 CFR 164 the colliding namespace is ORS chapter 164 (theft and burglary), and it is the
*more* common meaning of a bare `164.NNN` reference in Oregon material.

The standing trigger — that any instrument measured with section-shaped citations graduates
to this treatment — currently cannot fire, because the pipeline is hardcoded to
2 CFR 200. That gap is tracked as an issue, not a change to this decision.

**Update (#34):** the pipeline is generalized — `scan_cited_sections.py` takes `--title` and
`--part`, `split_cfr_sections.py` processes any part with a committed cited-sections file, and
the demand-driven trigger (measured citations, not part size) is unchanged; this note records
that the gap above is closed, not a change to the decision itself.

**Update (#63):** the same demand-driven logic is applied one level up, at the PART. `--title`
and `--part` become optional on `scan_cited_sections.py`: passing neither switches it to a
part-discovery mode that ranks unheld CFR parts by authority claim (mentions carried
alongside) and writes `_meta/ingest-queue.yml`, committed for the identical reason
`_meta/cited-sections/<part>.yml` is. Which *part* to hold was previously curated by hand in
issues #22–#25; #63's own measurement found none of those four candidates carried a single
authority claim, while the largest unheld part (34 CFR 300, 105 claims) appeared in none of
them. "Anchors first, documents when demanded" now governs the choice of part as well as the
choice of section within one — this is not a change to the decision, only its scope.
