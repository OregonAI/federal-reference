---
schema_version: 1
corpus: federal-reference
jurisdiction: us
id: nist-sp-800-53-r5.ps-4
title: NIST SP 800-53 Rev. 5 PS-4 — PERSONNEL TERMINATION
doc_type: federal_instrument
citation: NIST SP 800-53 Rev. 5 PS-4
authority_level: federal
issuing_body: National Institute of Standards and Technology
instrument_kind: nist_control
version: Rev. 5
as_of: '2026-11-12'
amended_on: '2020-12-10'
reproduction_basis: '17 U.S.C. § 105 — work of the U.S. government (NIST). Determined per document on
  2026-11-12 against the publication itself, not assumed from its issuer: its Authority statement (PDF
  page 3) reads "This publication may be used by nongovernmental organizations on a voluntary basis and
  is not subject to copyright in the United States. Attribution would, however, be appreciated by NIST."
  Held here: the front matter and Chapter Three (the control catalog) only. Chapter Three names ISO/IEC
  standards solely as bibliographic references and reproduces none of their text. NOT mirrored: the References
  bibliography and Appendices A-C; Appendix A (glossary) adapts third-party definitions (ISO/IEC 15026,
  ISO 25237, ISO/IEC 29100, ISO 15288, IETF RFC 4949), which ADR-0002 treats as not reproducible by being
  incorporated, and whose reproducibility has not been determined.'
superseded_by: null
source_url: https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-53r5.pdf
source_format: pdf
snapshot_id: nist-sp-800-53-r5
retrieved: '2026-11-12'
source_sha256: b95751a224e7e518338b7c19a541c4be4dbe261305ca6834fce3e3251bd391ee
status: current
content_mode: verbatim
relationships:
  related:
  - nist-sp-800-53-r5
maintainer: '@morficflux'
last_verified: ''
verified_by: ''
---

## At a glance

**NIST SP 800-53 Rev. 5 PS-4** — PERSONNEL TERMINATION

- Issued by: National Institute of Standards and Technology
- Publication: NIST SP 800-53 Rev. 5 — Security and Privacy Controls for Information Systems and Organizations ([nist-sp-800-53-r5](./nist-sp-800-53-r5.md))
- Version: Rev. 5 (September 2020, includes updates as of 2020-12-10)
- Text as of: 2026-11-12
- Cited by held documents: 16 times (cjis-sp-6-1 ×8, irs-pub-1075-11-2021 ×5, 6-cfr-37 ×3)
- Reproduction basis: 17 U.S.C. § 105 — work of the U.S. government (NIST). Determined per document on 2026-11-12 against the publication itself, not assumed from its issuer: its Authority statement (PDF page 3) reads "This publication may be used by nongovernmental organizations on a voluntary basis and is not subject to copyright in the United States. Attribution would, however, be appreciated by NIST." Held here: the front matter and Chapter Three (the control catalog) only. Chapter Three names ISO/IEC standards solely as bibliographic references and reproduces none of their text. NOT mirrored: the References bibliography and Appendices A-C; Appendix A (glossary) adapts third-party definitions (ISO/IEC 15026, ISO 25237, ISO/IEC 29100, ISO 15288, IETF RFC 4949), which ADR-0002 treats as not reproducible by being incorporated, and whose reproducibility has not been determined.


_NON-AUTHORITATIVE copy of one control, cut from the SP 800-53 Rev. 5 snapshot this corpus holds. Whether and how this binds a given agency depends on the instrument that incorporates it — read it at the source URL before relying on it. This copy is the Rev. 5 text of record, which is not necessarily the text a citing document meant (a document citing Rev. 4 is not answered by it)._


## Full text

### PS-4 PERSONNEL TERMINATION
Control:  Upon termination of individual employment:
a. Disable system access within [Assignment: organization-defined time period];
b. Terminate or revoke any authenticators and credentials associated with the individual;
c. Conduct exit interviews that include a discussion of [Assignment: organization-defined
information security topics];
d. Retrieve all security-related organizational system-related property; and
e. Retain access to organizational information and systems formerly controlled by terminated
individual.
Discussion:  System property includes hardware authentication tokens, system administration
technical manuals, keys, identification cards, and building passes. Exit interviews ensure that
terminated individuals understand the security constraints imposed by being former employees
and that proper accountability is achieved for system-related property. Security topics at exit
interviews include reminding individuals of nondisclosure agreements and potential limitations
on future employment. Exit interviews may not always be possible for some individuals, including
CHAPTER THREE    PAGE 225
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
in cases related to the unavailability of supervisors, illnesses, or job abandonment. Exit
interviews are important for individuals with security clearances. The timely execution of
termination actions is essential for individuals who have been terminated for cause. In certain
situations, organizations consider disabling the system accounts of individuals who are being
terminated prior to the individuals being notified.
Related Controls:  AC-2, IA-4, PE-2, PM-12, PS-6, PS-7.
Control Enhancements:
(1) PERSONNEL TERMINATION | POST-EMPLOYMENT REQUIREMENTS
(a) Notify terminated individuals of applicable, legally binding post-employment
requirements for the protection of organizational information; and
(b) Require terminated individuals to sign an acknowledgment of post-employment
requirements as part of the organizational termination process.
Discussion:  Organizations consult with the Office of the General Counsel regarding matters
of post-employment requirements on terminated individuals.
Related Controls:  None.
(2) PERSONNEL TERMINATION | AUTOMATED ACTIONS
Use [Assignment: organization-defined automated mechanisms] to [Selection (one or
more): notify [Assignment: organization-defined personnel or roles] of individual
termination actions; disable access to system resources].
Discussion:  In organizations with many employees, not all personnel who need to know
about termination actions receive the appropriate notifications, or if such notifications are
received, they may not occur in a timely manner. Automated mechanisms can be used to
send automatic alerts or notifications to organizational personnel or roles when individuals
are terminated. Such automatic alerts or notifications can be conveyed in a variety of ways,
including via telephone, electronic mail, text message, or websites. Automated mechanisms
can also be employed to quickly and thoroughly disable access to system resources after an
employee is terminated.
Related Controls:  None.
References:  None.
