# ADR-0006 — Hold the U.S. Code sections Oregon cites, and say how many

**Status:** Accepted, 2026-08-31. **Supersedes [ADR-0004](0004-no-codified-us-code.md)**,
which held enacted public laws and refused the codified U.S. Code.

## Context

ADR-0004 refused the codified U.S. Code on a good argument: the codified section and the
enacted text are different documents that diverge as later acts amend the code, so aliasing
one onto the other resolves a citation to a document that is not what was cited. That
argument is correct and this ADR does not dispute it.

ADR-0004 recorded its own cost honestly: **349 of 916 authority claims — 38% — across 742
distinct U.S.C. targets** resolve to a refusal, including the largest single unresolved
claims in the catalog (16 USC 544 at 89, 544c at 55, 544m at 51). It also named the shape of
the damage: *"an authority chain can be half-resolvable: 28 CFR Part 35 is ingestable while
42 USC 12131, the statute it implements, is not."*

It marked itself **"Accepted, and under active challenge,"** and said the decision should
turn on the boundary rather than on volume. This is that decision.

## Decision

**This corpus holds the U.S. Code sections Oregon cites as authority, section by section, on
demand.** It does not hold titles, does not hold the Code speculatively, and still never
maps a U.S.C. section onto a public law.

Three things follow, and each is a separate commitment:

**1. The unit is the section, and the trigger is a claim.** This is [ADR-0003](0003-split-only-what-is-cited.md)'s
rule applied to a second body of law: split only what is cited, and derive the list rather
than curating it. A section is ingested because an Oregon rule names it as authority, never
because it is nearby.

**2. Current text, not a version in the id.** A U.S.C. section is held the way CFR is held
under [ADR-0001](0001-hold-current-text-only.md) — one document, current text, `as_of` and
`amended_on` — **plus a `currency` field** carrying OLRC's own stamp, *"current through Pub.
L. 119-N"*.

`CONTEXT.md` says version belongs in the document id, and this is a deliberate exception
with a reason. That rule exists *"because sibling resolution is exact-id lookup… a version
that is not in the id cannot be seen by a sibling"* — it is about **siblings**, and IRS Pub
1075 has siblings a reader must not confuse. A U.S.C. section does not have siblings; it has
a history. Putting the P.L. in the id would fragment `20 USC 1232g` into documents no
citation ever names, because Oregon rules cite `20 USC 1232g` and never `20 USC 1232g as of
Pub. L. 119-4`. The currency stamp is therefore recorded as a field, which is strictly more
than a CFR document carries.

**3. The refusal changes in the same commit as the first section, never after.** This is the
part ADR-0004 flagged as hard, and `CONTEXT.md` already rules on it: *"A refusal that denies
holding something we do hold is worse than a crash: it is a wrong answer wearing a right
answer's clothes."*

Today `usc-section` answers *"this corpus does not hold the U.S. Code."* The day the first
section lands, that sentence becomes false. The new refusal states the partial hold — how
many sections are held, and that the cited one is not among them — so that "we hold the U.S.
Code" and "we hold four sections of it" are never served by the same words.

## Source of truth

**OLRC (`uscode.house.gov`)**, the official codifier, which publishes USLM XML per title and
stamps each release with the Public Law it is current through — the stamp decision 2 needs.

**govinfo is the recorded fallback**, not a second source: it is already a known-good host
here (both held public laws come from it), but its annual-edition-plus-supplements model fits
an as-of-a-date corpus worse than a continuously-current one.

**Cornell LII is refused.** It is convenient and well-formed and it is not authoritative. A
corpus whose first principle is *"this corpus is never a source of truth. Every answer cites
and defers"* cannot cite a university mirror as the thing it defers to.

## Considered and rejected

**Keeping ADR-0004.** Defensible, and it was nearly the answer. The refusal is *true*, and
ADR-0004 is right that its argument is not weakened by volume — aliasing returns the wrong
document whether it does so once or 349 times. What moved the decision is not volume but
**ADR-0001**: this corpus already holds current text of everything else and already accepts
that sharp edge in writing. Refusing U.S.C. alone means an authority chain stops halfway for
38% of claims, in a corpus whose purpose is answering what binds an Oregon agency. That is
failing at the stated job, not being rigorous about it.

**Holding the enacted public laws instead**, which needs no scope change since two are
already held. Rejected on measurement, not principle: FERPA is Pub. L. 93-380 § 513 plus
roughly a dozen amending acts, so the enacted texts do not give a reader the operative
provision. That is what codification is for. It is the option that looks like a compromise
and delivers neither thing.

**Deciding on FERPA's numbers.** #36 measures 20 USC 1232g at **1** authority claim against
34 CFR 99's 27, and concludes there is no urgency. That is true and unrepresentative: for
HIPAA the demand inverts, with 42 USC 1320d carrying **6** authority claims against 45 CFR
160 and 164's **2 combined**. Deciding the boundary on the weakest instance would have got
the boundary wrong.

## Consequences

**The manifest cost lands on a hand-authored file.** [ADR-0005](0005-source-manifest-is-hand-authored.md)
makes the source manifest hand-authored deliberately. Demand-triggered ingest means one
hand-authored entry per cited section: comfortable at four, unpleasant at forty, and 742
distinct targets are cited. This ADR does not solve that, and the follow-up it will force is
whether U.S.C. entries are derived from the cited-sections scan the way ADR-0003 derives its
list. Recorded here so the day it bites is a known cost rather than a surprise.

**A partial hold is now the normal state, permanently.** There is no version of this where
the corpus holds the U.S. Code. It holds some sections of it, and the count moves. Every
refusal, every coverage claim and every count in prose has to be written to survive that.

**ADR-0004's central rule survives unchanged.** A U.S.C. section is still never mapped onto a
public law. This ADR widens what may be *held*; it does not license aliasing what is not.
