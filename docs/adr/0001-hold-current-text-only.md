# ADR-0001 — Hold current text only, dated with `as_of` and `amended_on`

**Status:** Accepted. Recorded here 2026-08-11 from `AGENTS.md`, where this decision has
been in force since the corpus was created.

## Context

Federal instruments are amended constantly — Title 29 was amended the day this corpus was
created. A corpus mirroring them must decide what "the text" means: the current text, every
historical revision, or the revision in force at some reference date.

Oregon rules cite federal instruments and then sit unchanged for years. **A rule written in
2019 implements the text that existed in 2019.**

## Decision

One document per instrument, holding the **current** text, carrying:

- `as_of` — when our copy was current
- `amended_on` — when upstream last amended it

Historical revisions are not pinned, with one exception: a section Oregon cites that has
since been **removed** is ingested from a point-in-time snapshot of its last-in-force text
and marked `superseded` (see ADR-0003).

## Consequences

**The sharp edge is accepted, not solved.** Resolving a 2019 rule's citation to today's
text is a wrong answer that looks like a right one. This is the known cost.

**The mitigation lives on the edge, not in `resolve_citation`.** `resolve_citation("2 CFR
200")` does not know who is citing, so it cannot compare dates. `authority_chain` and
`graph_neighbors` walking from an Oregon rule know both ends and can. So:

- every document carries `as_of` and `amended_on`, both served over MCP
- every document states plainly that it holds current text, not necessarily the text in
  force when a citing rule was written
- the specific warning belongs where the citing rule's date and `amended_on` can actually
  be compared

**A pending rulemaking is not the CFR.** Anticipating a proposed rule in `amended_on`, or
quoting proposed text, violates this decision. Record what the version record reports.

## Alternatives rejected

**Pin every historical revision.** Storage model becomes complex, and the eCFR is amended
too often for the cost to be bounded.

**Refuse to answer undated citations.** Correct in principle, useless in practice — nearly
every Oregon citation is undated.
