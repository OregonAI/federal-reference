---
schema_version: 1
corpus: federal-reference
jurisdiction: us
id: nist-sp-800-53-r5.si-12
title: NIST SP 800-53 Rev. 5 SI-12 — INFORMATION MANAGEMENT AND RETENTION
doc_type: federal_instrument
citation: NIST SP 800-53 Rev. 5 SI-12
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

**NIST SP 800-53 Rev. 5 SI-12** — INFORMATION MANAGEMENT AND RETENTION

- Issued by: National Institute of Standards and Technology
- Publication: NIST SP 800-53 Rev. 5 — Security and Privacy Controls for Information Systems and Organizations ([nist-sp-800-53-r5](./nist-sp-800-53-r5.md))
- Version: Rev. 5 (September 2020, includes updates as of 2020-12-10)
- Text as of: 2026-11-12
- Cited by held documents: 53 times (cjis-sp-6-1 ×46, arc-ampe ×3, irs-pub-1075-11-2021 ×3, 6-cfr-37 ×1), 1 of them naming an enhancement of this control
- Reproduction basis: 17 U.S.C. § 105 — work of the U.S. government (NIST). Determined per document on 2026-11-12 against the publication itself, not assumed from its issuer: its Authority statement (PDF page 3) reads "This publication may be used by nongovernmental organizations on a voluntary basis and is not subject to copyright in the United States. Attribution would, however, be appreciated by NIST." Held here: the front matter and Chapter Three (the control catalog) only. Chapter Three names ISO/IEC standards solely as bibliographic references and reproduces none of their text. NOT mirrored: the References bibliography and Appendices A-C; Appendix A (glossary) adapts third-party definitions (ISO/IEC 15026, ISO 25237, ISO/IEC 29100, ISO 15288, IETF RFC 4949), which ADR-0002 treats as not reproducible by being incorporated, and whose reproducibility has not been determined.


_NON-AUTHORITATIVE copy of one control, cut from the SP 800-53 Rev. 5 snapshot this corpus holds. Whether and how this binds a given agency depends on the instrument that incorporates it — read it at the source URL before relying on it. This copy is the Rev. 5 text of record, which is not necessarily the text a citing document meant (a document citing Rev. 4 is not answered by it)._


## Full text

### SI-12 INFORMATION MANAGEMENT AND RETENTION
Control:  Manage and retain information within the system and information output from the
system in accordance with applicable laws, executive orders, directives, regulations, policies,
standards, guidelines and operational requirements.
CHAPTER THREE   PAGE 352
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
Discussion:  Information management and retention requirements cover the full life cycle of
information, in some cases extending beyond system disposal. Information to be retained may
also include policies, procedures, plans, reports, data output from control implementation, and
other types of administrative information. The National Archives and Records Administration
(NARA) provides federal policy and guidance on records retention and schedules.
If organizations
have a records management office, consider coordinating with records management personnel.
Records produced from the output of implemented controls that may require management and
retention include, but are not limited to: All XX-1, AC-6(9), AT-4, AU-12, CA-2, CA-3, CA-5, CA-6,
CA-7, CA-8, CA-9, CM-2, CM-3, CM-4, CM-6, CM-8, CM-9, CM-12, CM-13, CP-2, IR-6, IR-8, MA-2,
MA-4, PE-2, PE-8, PE-16, PE-17, PL-2, PL-4, PL-7, PL-8, PM-5, PM-8, PM-9, PM-18, PM-21, PM-27,
PM-28, PM-30, PM-31, PS-2, PS-6, PS-7, PT-2, PT-3, PT-7, RA-2, RA-3, RA-5, RA-8, SA-4, SA-5, SA-8,
SA-10, SI-4, SR-2, SR-4, SR-8.
Related Controls:  All XX-1 Controls, AC-16, AU-5, AU-11, CA-2, CA-3, CA-5, CA-6, CA-7, CA-9, CM-
5, CM-9, CP-2, IR-8, MP-2, MP-3, MP-4, MP-6, PL-2, PL-4, PM-4, PM-8, PM-9, PS-2, PS-6, PT-2, PT-
3, RA-2, RA-3, SA-5, SA-8, SR-2.
Control Enhancements:
(1) INFORMATION MANAGEMENT AND RETENTION | LIMIT PERSONALLY IDENTIFIABLE INFORMATION
ELEMENTS
Limit personally identifiable information being processed in the information life cycle to
the following elements of personally identifiable information: [Assignment: organization-
defined elements of personally identifiable information].
Discussion:  Limiting the use of personally identifiable information throughout the
information life cycle when the information is not needed for operational purposes helps to
reduce the level of privacy risk created by a system. The information life cycle includes
information creation, collection, use, processing, storage, maintenance, dissemination,
disclosure, and disposition. Risk assessments as well as applicable laws, regulations, and
policies can provide useful inputs to determining which elements of personally identifiable
information may create risk.
Related Controls:  PM-25.
(2) INFORMATION MANAGEMENT AND RETENTION | MINIMIZE PERSONALLY IDENTIFIABLE
INFORMATION IN TESTING, TRAINING, AND RESEARCH
Use the following techniques to minimize the use of personally identifiable information for
research, testing, or training: [Assignment: organization-defined techniques].
Discussion:  Organizations can minimize the risk to an individual’s privacy by employing
techniques such as de-identification or synthetic data. Limiting the use of personally
identifiable information throughout the information life cycle when the information is not
needed for research, testing, or training helps reduce the level of privacy risk created by a
system. Risk assessments as well as applicable laws, regulations, and policies can provide
useful inputs to determining the techniques to use and when to use them.
Related Controls:  PM-22, PM-25, SI-19.
(3) INFORMATION MANAGEMENT AND RETENTION | INFORMATION DISPOSAL
Use the following techniques to dispose of, destroy, or erase information following the
retention period: [Assignment: organization-defined techniques].
Discussion:  Organizations can minimize both security and privacy risks by disposing of
information when it is no longer needed. The disposal or destruction of information applies
to originals as well as copies and archived records, including system logs that may contain
personally identifiable information.
CHAPTER THREE   PAGE 353
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
Related Controls:  None.
References:  [USC 2901], [OMB A-130].
