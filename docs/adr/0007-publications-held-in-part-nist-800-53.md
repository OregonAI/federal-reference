# ADR-0007 — A publication can be held in part: NIST SP 800-53 Rev. 5

**Status:** Accepted, 2026-11-12 (#42). Applies [ADR-0002](0002-copyright-decided-per-document.md)
and [ADR-0003](0003-split-only-what-is-cited.md) to a publication rather than a CFR part or a
statute.

## Context

Documents already held cite NIST SP 800-53 by control (4,252 control citations across five
documents when this was written) and every one resolved to nothing. The operator ruled on #42
(2026-09-12) that material required by held documents is imported, with no new intake signal.

SP 800-53 Rev. 5 is a 492-page PDF. Three facts shaped the hold:

- **The citations are control-shaped** (`AC-2`, `SC-7(3)`), like 2 CFR 200's are section-shaped.
- **The publication is not uniformly reproducible.** Its own Authority statement says it "is not
  subject to copyright in the United States", and Chapter Three (the control catalog) names
  ISO/IEC standards only as bibliographic references. But Appendix A (glossary) *adapts*
  third-party definitions (`[ISO/IEC 15026, Adapted]`, `[ISO 25237]`, `[ISO/IEC 29100, Adapted]`,
  `[ISO 15288]`, `[IETF 4949]`). ADR-0002: incorporated third-party text is not reproducible by
  being incorporated, and that determination is a human step nobody has taken.
- **Version is identity.** Rev. 4 and Rev. 5 differ in what controls exist; NIST's later minor
  releases (5.1.x, 5.2.0) change control text but are distributed as OSCAL, not as a PDF.

## Decision

1. **Held in part.** `nist-sp-800-53-r5` reproduces the front matter and Chapter Three, verbatim,
   and nothing after the catalog (bibliography, Appendices A-C). The document says so, and says
   why, in its first paragraphs. `src/check_extraction.py` proves the committed text is an exact
   prefix of the raw PDF's token stream ending at the catalog-closing `REFERENCES` heading, so the
   boundary is checked against the source and not against the function that drew it.
2. **One document per cited base control.** Enhancements stay inside their base control, as the
   source prints them. The list is derived from this repository's own held documents
   (`src/scan_cited_controls.py`, `_meta/cited-controls/`), and, unlike the CFR scan, can be
   re-derived in CI because it needs no sibling checkout.
3. **The revision is in the id** (`nist-sp-800-53-r5`, `…-r5.ac-2`). A Rev. 4 citation derives an
   id that is absent from the index, and the in-corpus resolver refuses it by name. A release
   number (`5.2.0`) is not answered by the PDF that predates it, and 800-53A/B are different
   publications.
4. **What NIST says it changed after the held text is stated beside the text.** The control list
   of release 5.2.0 is read from NIST's listing of record into
   `_meta/nist-sp-800-53-r5-release-5-2-0.yml`; each listed control's document says the held text
   does not include that change. `amended_on` is the date of the held text (2020-12-10, as the PDF prints it), not a release date; later releases (5.1.x, 5.2.0) are named in the note beside the text.
5. **Resolution never widens.** A catalog control with no document resolves to the publication
   with a note naming its `### ` heading; a control the catalog lacks, or an enhancement the Rev. 5
   text lacks, resolves to nothing and says so.

## Consequences

- Extending the hold to the rest of the publication is a decision about Appendix A (and whether
  the bibliography and Appendices B-C may be mirrored), not an engineering task.
- `federal_ids.py` gained a NIST branch. It is the three-repo parity-locked contract file:
  executive-regulatory-frameworks and oregon-audits must receive it verbatim before a sibling can
  derive `nist-sp-800-53-r5.*` ids; until then siblings resolve NIST citations to nothing, exactly
  as before.
- FIPS 140 and SP 800-63 (also named by #42) are not held by this change.
