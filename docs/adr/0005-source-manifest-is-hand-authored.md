# ADR-0005 — The source manifest is hand-authored and human-approved, not generated

**Status:** Accepted. Recorded here 2026-08-11 from the note at the top of
`_meta/source-manifest.yml`.

## Context

Every other corpus on this platform generates its source list by walking an upstream index
— a legislature's measure list, an agency's rule chapters. This corpus has no such index.

**The federal government does not publish "the list of instruments Oregon must comply
with."** That list is a judgement about which federal obligations bind a particular state,
and no upstream authority makes it.

## Decision

`_meta/source-manifest.yml` is hand-authored and approved by a human via PR. It is
deliberately not generated.

Each entry records **which signal** put it there — `audited`, `authority`, or `named` (see
`CONTEXT.md`) — and a `why` stating the evidence, because the signals disagree and the
disagreement is the most useful thing this corpus knows.

Intake is therefore a **decision**, not a ranking. An agent may measure demand and propose
an instrument; accepting it into the manifest is a human step.

## Consequences

A high-ranking instrument is not automatically in scope, and a low-ranking one is not
automatically out. IRS Pub 1075 entered at 7 mentions and 0 authority claims; Perkins V at
2 mentions, "included because the money is real and the conditions bind, which citation
count does not measure."

**Ranking by a single signal produces a materially different corpus.** Ranking intake by
what Oregon rules cite would have put IDEA first and never reached the Uniform Guidance,
which binds every federal dollar the state receives. The manifest note records this as the
reason the signal is stored per entry rather than collapsed into one number.

`format` is declared on every entry rather than inferred. The eCFR URL ends in `?part=200`,
so an inferred format would be `html`, and drift detection would run an HTML-to-text
converter over XML and report a change on every run.

Where Oregon cites versions we do not hold, the entry says so
(`known_cited_versions_not_held`) rather than letting the current one quietly stand in.
