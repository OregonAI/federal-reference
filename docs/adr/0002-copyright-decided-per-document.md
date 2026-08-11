# ADR-0002 — Copyright is decided per document and recorded, never assumed

**Status:** Accepted. Recorded here 2026-08-11 from `AGENTS.md` and from the
`reproduction_basis` entries in `_meta/source-manifest.yml`.

## Context

Most instruments in this corpus are works of the U.S. government and not subject to
copyright (17 U.S.C. § 105) — federal statutes, the CFR, IRS publications. That makes a
corpus-wide assumption tempting, and a corpus-wide assumption is exactly what goes wrong
quietly.

Two failure modes are specific enough to name:

- **"Federal, therefore publishable" is not an argument.** A government work can carry
  distribution restrictions independent of copyright.
- **Incorporation by reference.** Federal documents routinely bind third-party standards.
  The incorporated text does not become free because the incorporating document is.

## Decision

Every document records `reproduction` (`full` | `excerpt` | `summary`) and
`reproduction_basis` — the specific determination, per document, in the manifest entry and
carried into the document.

The basis records **what was checked**, not what was inferred. CJIS 6.1 is the worked
example: its basis states that distribution terms for that specific version were reviewed
by the operator on a named date and found not to restrict redistribution — rather than
resting on "it is federal".

`doc_type` does half the work: `external_reference` is reserved for material we may not
reproduce and the schema forces `content_mode: summary` on it. `federal_instrument` is for
material we may.

## Consequences

Ingesting an instrument whose reproducibility has not been determined is not blocked by
tooling — the determination is a human step, and skipping it produces a schema-valid
document with an unearned basis string. Reviewers check this; nothing else can.

Third-party standards bound by reference (WCAG 2.1 into 28 CFR 35.200; ISO and commercial
material into NIST profiles) are summarized and linked, never mirrored, however freely the
incorporating regulation may be reproduced.

Instruments that turn out to be `summary`-only are still worth holding. A summary plus the
official link resolves a citation that otherwise resolves to nothing — provided the summary
is never phrased as the requirement.
