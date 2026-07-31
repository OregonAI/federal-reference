# AGENTS.md — Federal Reference — instruments Oregon must comply with

Corpus of the OregonAI civic corpus platform. Archetype: document.
Read `_meta/corpus.yml` for configuration; the platform rules live in
OregonAI/corpus-toolkit `docs/`.

## Purpose

Non-authoritative, AI-friendly mirror of the federal instruments Oregon agencies must
comply with and cite as legal authority — the Uniform Guidance, program regulations, and
the named publications that carry compliance obligations.

Never a source of truth. Every answer must cite and link the authoritative source.

Every other corpus on this platform stops at the Oregon border. An OAR citing a federal
requirement resolved to nothing, so the authority chain ran statute → rule → policy and
then hit a wall exactly where the binding constraint lives. This corpus is that ceiling.

## THIS CORPUS IS THE ONE MOST LIKELY TO BE MISTAKEN FOR LEGAL ADVICE

Federal compliance requirements carry penalties Oregon policy does not. A reader who takes
a summary here as the requirement may act on it and be wrong in a way that costs money.
The non-authoritative disclaimer is not decoration in this repository.

Three rules follow, and none is optional:

1. **A summary is never phrased as the requirement.** Not "agencies must retain records for
   three years" but "the cited section states a three-year retention period — read it."
2. **Every document carries its official source URL and its version or revision.** A
   federal requirement without a version is not a citation, it is a rumour.
3. **Never present a superseded version as current**, and never let an Oregon rule's
   citation silently resolve to a revision published after that rule was written.

## WE HOLD CURRENT TEXT. THAT IS A DECISION WITH A KNOWN SHARP EDGE

One document per instrument, holding the current text with an `as_of` date and the
upstream `amended_on`. Chosen over pinning every historical revision because the storage
model stays simple and the eCFR is amended constantly — Title 29 was amended the day this
corpus was created.

The sharp edge: **an Oregon rule written in 2019 implements the text that existed in 2019.**
Resolving its citation to today's text is a wrong answer that looks like a right one.

The mitigation is NOT in `resolve_citation`, and the reason is worth understanding.
`resolve_citation("2 CFR 200")` has no idea who is citing, so it cannot compare anything.
`authority_chain` and `graph_neighbors` walking from an Oregon rule DO know both ends. So:

- every document carries `as_of` and `amended_on`, and both are served over MCP
- every document states plainly that it is current text, not necessarily the text in force
  when a citing rule was written
- the SPECIFIC warning belongs on the edge, where the citing rule's date and `amended_on`
  can actually be compared

## Copyright is decided per document and recorded, never assumed

Most instruments here are works of the U.S. government and not subject to copyright
(17 U.S.C. § 105), which covers federal statutes, the CFR, and IRS publications. Two things
that must be checked rather than reasoned past:

- **"Federal, therefore publishable" is not an argument.** A government work can carry
  distribution restrictions independent of copyright. Read the specific version's terms.
- **Incorporation by reference.** Federal documents routinely bind third-party standards —
  a NIST profile pulling in ISO, a control catalogue referencing commercial material. The
  incorporated text does not become free because the incorporating document is. Summarize
  and link; never mirror.

Each document records `reproduction` (full | excerpt | summary) and `reproduction_basis`,
so the determination is auditable per document. A corpus-wide assumption is exactly what
goes wrong quietly.

Note the doc_type does half this work already: `external_reference` is reserved for
material we may NOT reproduce and the schema forces `content_mode: summary` on it.
`federal_instrument` is for material we may.

## Hard rules (anti-fabrication)
1. Never write content that does not exist in the pinned source. Source
   unreachable or unparseable → insert
   `<!-- TODO: human verification required -->` and stop. Never
   reconstruct from model knowledge.
2. `## Full text` sections are verbatim only. Curator content is confined
   to `## At a glance`, `## Curator notes`, `## Cross-references`.
3. Third-party copyrighted material: summary + official link only.
4. Never invent or infer a citation. Unresolvable → say so.
5. Live-data answers (api/hybrid) must carry the executed query and
   timestamp.
6. All changes via PR. Do not set `last_verified`/`verified_by` to a real
   value — the human reviewer does that at approval. The schema REQUIRES both
   keys, so ingestion writes them as empty strings: schema-valid, and read
   downstream as "never verified", which is exactly true. Never write a date or
   a handle you did not earn; a fabricated verification stamp is worse than an
   obviously-empty one.
7. Update this knowledge body's CHANGELOG.md in the same PR as content
   changes.

## Found a bug you are not fixing right now? Open an issue. Period.

This is not optional and has no size threshold.

If you discover a defect and do not fix it in the change you are working on, **open a
GitHub issue before you finish the task**. Not a note in the commit message, not a
paragraph in the PR body, not a line in your summary to the user. Those are not a work
queue — nobody greps closed PRs six months later, and the next agent rediscovers the same
bug from scratch, usually the expensive way.

This applies to every one of these, not just crashes:

- a check that passes without checking anything
- a documented command, flag, or path that does not exist or does not work
- a claim in a README, docstring, or catalog note that is no longer true
- data known to be wrong, stale, or incomplete
- a guard that cannot fire, or fires on the wrong condition
- something you worked around instead of fixing

**File it in the repo that owns the fix, which may not be the repo you are in.** A parser
defect here, a registry gap in a sibling corpus, and a validator gap in `corpus-toolkit`
are three different issues in three different repos. Say plainly in each which repo the
work belongs to.

An issue must answer four things, because an issue that only says "X is broken" costs the
next person the whole investigation again:

1. **What is wrong** — the specific behaviour, not a category
2. **How it was found** — the command, the data, the failing case
3. **What it breaks** — who or what gets a wrong answer, and how silently
4. **What would fix it**, or what still needs measuring before anyone can know

Prefer counts and reproductions over adjectives. "126 appropriations unjoined, of which 59
are an extraction gap and 41 are correct" is actionable; "agency matching needs work" is
not, and will be re-derived by someone else.

If you genuinely cannot open one — no network, no permission — say so explicitly in your
final message to the user and hand them the text to file. Silently dropping it is the one
outcome that is never acceptable.

## Workflow
Discovery → human-approved source manifest → ingestion → human-reviewed
PR. See toolkit `docs/replication-guide.md`.

## Generated files — never hand-edit

| file | generated by | gate |
|---|---|---|
| `_meta/graph.json` | `src/build_graph.py` | `generated` job, every PR |
| `STATUS.md` | `corpus-generate-status` | `generated` job, every PR (plus a weekly repair in the `drift` job) |

Regenerate at the source and commit the result.

`_meta/corpus-index.json` is generated too but is **not committed**: `publish-index.yml`
builds it at deploy time. A committed copy can silently fall behind its own corpus, and
the damage lands in a SIBLING repo whose citation resolution reads it. Publish it; do
not commit it.

**Every generated file you commit needs a step in the `generated` job.** One without a
step is exactly the failure that job exists to prevent, and it is silent by construction
— the toolkit only READS these artifacts, so nothing anywhere notices when one goes
stale. A corpus that ships `joins:` owes itself the same treatment: the toolkit resolves
each `joins[].document_id`, but only this corpus can check that a `{dataset, key}` pair
selects any rows at all.
