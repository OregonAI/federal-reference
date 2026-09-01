# CONTEXT — Federal Reference

The vocabulary this corpus uses, and what each term means *here*. Terms are recorded
because they are already load-bearing in the manifest, the schema or the code — this file
names them, it does not invent them.

Where a term has a tempting synonym that means something subtly different, the difference
is stated. Drift between these terms is the most common way a wrong answer gets produced
in this repo, because several of them are near-synonyms in ordinary English and are not
near-synonyms here.

## The corpus

**Instrument** — a federal document that carries compliance obligations for Oregon: a CFR
part, an enacted public law, or a named agency publication. The unit of intake. Not every
federal document is an instrument; the test is whether it binds or is cited as binding.

**Document** — one file in `instruments/`, holding one instrument (or one section of one,
where a part has been split). The unit of storage and retrieval. One instrument normally
produces one document; see **section document**.

**Part document** — the document holding a whole CFR part, with its sections as headings.

**Section document** — a document holding a single CFR section, split out of a part
because Oregon cites that section specifically. See ADR-0003.

**Held / unheld** — whether this corpus has a document for an instrument. "Unheld" is the
state most of the federal ceiling is in, and saying so accurately is a deliverable: an
unheld instrument must produce a refusal that names what *is* held, never a silent miss.

## The three intake signals

The source manifest records **which signal** put each instrument in the corpus, because
the signals disagree and the disagreement is the most useful thing this corpus knows.
Ranking intake by any one of them alone produces a different and worse corpus.

**`audited`** — cited in Oregon's single audits. What the state is audited *against*. The
compliance surface. 2 CFR 200 leads this at ~178 citations.

**`authority`** — claimed as legal authority by an Oregon rule, via `legal_authority` or
`statutes_implemented` in executive-regulatory-frameworks. 34 CFR 300 leads this at 105
claims.

**`named`** — a high-stakes instrument named in the seed or argued for on its penalties,
regardless of citation count. IRS Pub 1075 (7 mentions, 0 authority claims) and CJIS (8
mentions, 0 authority claims) are both here. This signal exists precisely because citation
count does not measure stakes.

**Authority claim vs mention** — a *claim* is a rule naming the instrument as its legal
authority; a *mention* is any reference in prose. They rank instruments very differently
and must never be conflated. 45 CFR 164 has 101 mentions and 2 authority claims;
34 CFR 99 has 38 mentions and 27 claims. Writing "most-cited" without naming the signal
is how that conflation happens.

**Internal edge density** — how often instruments this corpus *already holds* cite an
unheld document. A fourth measure, and not one of the three intake signals: it measures
this corpus's own dangling edges rather than Oregon's citation behaviour. FIPS 140 (47
references from held documents) and NIST SP 800-53 (31) are the current leaders. Named
here because it has been used in argument and needs a stable name; whether it becomes an
intake signal is undecided.

## Text and provenance

**`as_of`** — the date the text this corpus holds was current. A property of our snapshot.

**`amended_on`** — the date upstream last amended the instrument. A property of the
instrument. Both are required; neither substitutes for the other.

**Version is identity, not metadata.** For anything publishing discrete revisions, the
version belongs *in the document id* — `irs-pub-1075-11-2021`, `cjis-sp-6-1` — because
sibling resolution is exact-id lookup against an index of `[title, doc_type, path]` with
no version field. A version that is not in the id cannot be seen by a sibling.

**Current text** — what this corpus holds: the instrument as it stands now, not as it
stood when a citing rule was written. See ADR-0001 for the sharp edge this creates.

**Codified section** — one section of the U.S. Code, held because an Oregon rule claims it
as authority (ADR-0006). Held as *current text* like a CFR section, with one addition: a
`currency` field carrying OLRC's own stamp, "current through Pub. L. N". The version is
deliberately NOT in the id — see ADR-0006 for why this is an exception to *version is
identity* rather than a violation of it.
_Avoid_: Statute, U.S.C. entry, public law — the first two are vague about codified versus
enacted, and a **public law** is a different document this corpus also holds. The codified
section and the enacted text diverge as later acts amend the code, and neither is ever
served in answer to a citation naming the other.

**Partial hold** — the permanent condition of this corpus with respect to the U.S. Code: it
holds *some sections*, and the count moves. There is no state in which it holds the Code. A
refusal, a coverage claim or a count in prose that reads as "we hold the U.S. Code" is wrong
on the day it is written, not merely at risk of going stale.
_Avoid_: Coverage, completeness — both invite a percentage against a denominator nobody has
measured; what is held is a list, and the honest statement names its length

**Superseded** — a document holding text that was in force and no longer is, retained
because Oregon cited it. Carries `superseded_by`. Distinct from *removed* (gone from the
CFR) and from *stale* (our copy is behind upstream, which is a defect, not a state).

**Snapshot** — the raw upstream bytes on disk under `_meta/snapshots/`, hashed as
`source_sha256`. Documents are derived from snapshots; provenance verifies both against
the same file, so a part and the sections split from it cannot disagree.

**`reproduction` / `reproduction_basis`** — whether we may publish the text
(`full` | `excerpt` | `summary`) and the specific determination that says so, recorded per
document. See ADR-0002.

**Incorporation by reference** — a federal document binding third-party material (WCAG 2.1
into 28 CFR 35.200; ISO and commercial standards into NIST profiles). The incorporating
text is federal and reproducible; the incorporated text is not, and does not become
reproducible by being pointed at. Summarize and link, never mirror.

## Answering

**Non-authoritative** — this corpus is never a source of truth. Every answer cites and
links the official source. Not decoration: a reader who takes a summary here as the
requirement may act on it and be wrong in a way that costs money.

**A summary is never phrased as the requirement.** Not "agencies must retain records for
three years" but "the cited section states a three-year retention period — read it."

**Resolution** — turning a citation string into held documents. Lives in
`src/citation_schemes.py`. A scheme that matches and then refuses is often better than no
scheme, because "not held" is a true answer and "unrecognized format" invites the reader
to think we merely failed to parse.

**Refusal** — the answer given for a well-formed citation to an unheld instrument. It must
be true and specific. A refusal that names the wrong held instrument, or that denies
holding something we do hold, is worse than a crash: it is a wrong answer wearing a right
answer's clothes.

## Terms that collide

Recorded because each has already produced, or nearly produced, a wrong measurement.

**ORS chapter N vs `N CFR`** — Oregon Revised Statutes chapter numbers collide with CFR
part numbers in short-form citations. `§ 164.377` is ORS computer crime, not the HIPAA
Privacy Rule; ORS chapter 200 collides with 2 CFR 200. Bare short-form section references
are only countable in a document that also carries the full citation.

**CISA** — the Cybersecurity and Infrastructure Security Agency, *and* Certified
Information Systems Auditor. In `oregon-audits` the second meaning dominates by roughly 50
to 1, because it appears in auditor signature blocks.

**SNAP** — the nutrition program, and a substring of "snapshot", which is boilerplate in
every audit report. Case-insensitive matching without a word boundary returns every file.

**NIST** — a substring of "administration" and "administrative". Case-insensitive matching
without a word boundary returns tens of thousands of false hits.
