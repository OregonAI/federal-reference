# ADR-0004 — Hold enacted public laws, not the codified U.S. Code

**Status:** Accepted, and under active challenge. Recorded here 2026-08-11 from the
`usc-section` scheme in `src/citation_schemes.py`.

## Context

Oregon rules cite the U.S. Code constantly. A corpus of federal instruments could hold
enacted public laws (as passed, from govinfo), the codified U.S. Code (as maintained, by
title and section), or both.

The original seed proposed holding public laws "with the U.S.C. sections it created as
aliases" — resolving a U.S.C. citation to the public law that created it.

## Decision

This corpus holds **enacted public laws and named federal publications, not the codified
U.S. Code.**

The `usc-section` scheme is registered anyway, as a deliberate exception to the rule that a
scheme resolving nothing is worse than none. Left unmatched, a U.S.C. citation returns "no
citation scheme recognized this format", which invites the reader to conclude we merely
failed to parse it. Matched, it returns the true and more useful statement: this corpus does
not hold the U.S. Code, and here are the public laws it does hold.

**A U.S.C. section is never mapped onto a public law.** The codified section and the
enacted text are different documents, and they diverge as later acts amend the code. The
seed's aliasing was not implemented, because it would resolve a citation to a document that
is not what was cited.

## Consequences

Every U.S.C. citation from Oregon resolves to a refusal. Measured against ERF's
external-citations catalog, that is **349 of 916 authority claims — 38% — across 742
distinct U.S.C. targets**, including the largest single unresolved claims in the catalog
(16 USC 544 at 89, 544c at 55, 544m at 51).

It also means an authority chain can be half-resolvable: 28 CFR Part 35 is ingestable while
42 USC 12131, the statute it implements, is not.

## Status of the challenge

Reversing this is under consideration, driven by instruments where the statute rather than
the regulation is what Oregon claims as authority (42 USC 1320d carries 6 authority claims
against 45 CFR 160 and 164's 2 combined). The demand numbers point in opposite directions
per instrument, so the decision should turn on the boundary itself rather than on volume.

The reasoning above is **not weakened by volume**. Aliasing a codified section to enacted
text returns the wrong document whether it does so once or 349 times. A reversal would have
to hold the U.S. Code properly, and decide what a partial hold reports — "we hold the U.S.
Code" and "we hold four sections of it" require very different correct refusals.
