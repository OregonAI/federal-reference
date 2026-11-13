---
schema_version: 1
corpus: federal-reference
jurisdiction: us
id: nist-sp-800-53-r5.au-3
title: NIST SP 800-53 Rev. 5 AU-3 — CONTENT OF AUDIT RECORDS
doc_type: federal_instrument
citation: NIST SP 800-53 Rev. 5 AU-3
authority_level: federal
issuing_body: National Institute of Standards and Technology
instrument_kind: nist_control
version: Rev. 5
as_of: '2026-11-12'
amended_on: '2025-08-27'
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
source_sha256: f401769fe5982296eb56237f92333d1c729ebe2a0e5bc94fb33627207f2f88e7
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

**NIST SP 800-53 Rev. 5 AU-3** — CONTENT OF AUDIT RECORDS

- Issued by: National Institute of Standards and Technology
- Publication: NIST SP 800-53 Rev. 5 — Security and Privacy Controls for Information Systems and Organizations ([nist-sp-800-53-r5](./nist-sp-800-53-r5.md))
- Version: Rev. 5 (September 2020, includes updates as of 2020-12-10)
- Text as of: 2026-11-12
- Cited by held documents: 24 times (cjis-sp-6-1 ×16, irs-pub-1075-11-2021 ×5, 6-cfr-37 ×3)
- Reproduction basis: 17 U.S.C. § 105 — work of the U.S. government (NIST). Determined per document on 2026-11-12 against the publication itself, not assumed from its issuer: its Authority statement (PDF page 3) reads "This publication may be used by nongovernmental organizations on a voluntary basis and is not subject to copyright in the United States. Attribution would, however, be appreciated by NIST." Held here: the front matter and Chapter Three (the control catalog) only. Chapter Three names ISO/IEC standards solely as bibliographic references and reproduces none of their text. NOT mirrored: the References bibliography and Appendices A-C; Appendix A (glossary) adapts third-party definitions (ISO/IEC 15026, ISO 25237, ISO/IEC 29100, ISO 15288, IETF RFC 4949), which ADR-0002 treats as not reproducible by being incorporated, and whose reproducibility has not been determined.


_NON-AUTHORITATIVE copy of one control, cut from the SP 800-53 Rev. 5 snapshot this corpus holds. Whether and how this binds a given agency depends on the instrument that incorporates it — read it at the source URL before relying on it. This copy is the Rev. 5 text of record, which is not necessarily the text a citing document meant (a document citing Rev. 4 is not answered by it)._


> **Release 5.2.0 postdates this text.** NIST's listing of record ([https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final)) says that on 2025-08-27 it issued release 5.2.0 of SP 800-53, which updates the related controls for this control. The text below is the Rev. 5 PDF of record and does NOT include that change; read NIST's own list of the changes ([summary](https://csrc.nist.gov/files/projects/Risk-Management/800-53%20Comment%20Site/SP800-53-r5.2.0-changes.pdf)) before relying on this control's text.


## Full text

### AU-3 CONTENT OF AUDIT RECORDS
Control:  Ensure that audit records contain information that establishes the following:
a. What type of event occurred;
b. When the event occurred;
c. Where the event occurred;
d. Source of the event;
e. Outcome of the event; and
f. Identity of any individuals, subjects, or objects/entities associated with the event.
Discussion:  Audit record content that may be necessary to support the auditing function
includes event descriptions (item a), time stamps (item b), source and destination addresses
(item c), user or process identifiers (items d and f), success or fail indications (item e), and
filenames involved (items a, c, e, and f) . Event outcomes include indicators of event success or
failure and event-specific results, such as the system security and privacy posture after the event
occurred. Organizations consider how audit records can reveal information about individuals that
may give rise to privacy risks and how best to mitigate such risks. For example, there is the
potential to reveal personally identifiable information in the audit trail, especially if the trail
records inputs or is based on patterns or time of usage.
Related Controls:  AU-2, AU-8, AU-12, AU-14, MA-4, PL-9, SA-8, SI-7, SI-11.
Control Enhancements:
(1) CONTENT OF AUDIT RECORDS | ADDITIONAL AUDIT INFORMATION
Generate audit records containing the following additional information: [Assignment:
organization-defined additional information].
Discussion:  The ability to add information generated in audit records is dependent on
system functionality to configure the audit record content. Organizations may consider
additional information in audit records including, but not limited to, access control or flow
control rules invoked and individual identities of group account users. Organizations may
also consider limiting additional audit record information to only information that is
explicitly needed for audit requirements. This facilitates the use of audit trails and audit logs
by not including information in audit records that could potentially be misleading, make it
more difficult to locate information of interest, or increase the risk to individuals' privacy.
Related Controls:  None.
CHAPTER THREE   PAGE 68
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
(2) CONTENT OF AUDIT RECORDS | CENTRALIZED MANAGEMENT OF PLANNED AUDIT RECORD CONTENT
[Withdrawn: Incorporated into PL-9.]
(3) CONTENT OF AUDIT RECORDS | LIMIT PERSONALLY IDENTIFIABLE INFORMATION ELEMENTS
Limit personally identifiable information contained in audit records to the following
elements identified in the privacy risk assessment: [Assignment: organization-defined
elements].
Discussion:  Limiting personally identifiable information in audit records when such
information is not needed for operational purposes helps reduce the level of privacy risk
created by a system.
Related Controls:  RA-3.
References:  [OMB A-130], [IR 8062].
