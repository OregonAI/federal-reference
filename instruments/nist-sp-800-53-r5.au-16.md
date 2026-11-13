---
schema_version: 1
corpus: federal-reference
jurisdiction: us
id: nist-sp-800-53-r5.au-16
title: NIST SP 800-53 Rev. 5 AU-16 — CROSS-ORGANIZATIONAL AUDIT LOGGING
doc_type: federal_instrument
citation: NIST SP 800-53 Rev. 5 AU-16
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

**NIST SP 800-53 Rev. 5 AU-16** — CROSS-ORGANIZATIONAL AUDIT LOGGING

- Issued by: National Institute of Standards and Technology
- Publication: NIST SP 800-53 Rev. 5 — Security and Privacy Controls for Information Systems and Organizations ([nist-sp-800-53-r5](./nist-sp-800-53-r5.md))
- Version: Rev. 5 (September 2020, includes updates as of 2020-12-10)
- Text as of: 2026-11-12
- Cited by held documents: 4 times (irs-pub-1075-11-2021 ×3, cjis-sp-6-1 ×1)
- Reproduction basis: 17 U.S.C. § 105 — work of the U.S. government (NIST). Determined per document on 2026-11-12 against the publication itself, not assumed from its issuer: its Authority statement (PDF page 3) reads "This publication may be used by nongovernmental organizations on a voluntary basis and is not subject to copyright in the United States. Attribution would, however, be appreciated by NIST." Held here: the front matter and Chapter Three (the control catalog) only. Chapter Three names ISO/IEC standards solely as bibliographic references and reproduces none of their text. NOT mirrored: the References bibliography and Appendices A-C; Appendix A (glossary) adapts third-party definitions (ISO/IEC 15026, ISO 25237, ISO/IEC 29100, ISO 15288, IETF RFC 4949), which ADR-0002 treats as not reproducible by being incorporated, and whose reproducibility has not been determined.


_NON-AUTHORITATIVE copy of one control, cut from the SP 800-53 Rev. 5 snapshot this corpus holds. Whether and how this binds a given agency depends on the instrument that incorporates it — read it at the source URL before relying on it. This copy is the Rev. 5 text of record, which is not necessarily the text a citing document meant (a document citing Rev. 4 is not answered by it)._


## Full text

### AU-16 CROSS-ORGANIZATIONAL AUDIT LOGGING
Control:  Employ [Assignment: organization-defined methods] for coordinating [Assignment:
organization-defined audit information] among external organizations when audit information is
transmitted across organizational boundaries.
Discussion:  When organizations use systems or services of external organizations, the audit
logging capability necessitates a coordinated, cross-organization approach. For example,
maintaining the identity of individuals who request specific services across organizational
boundaries may often be difficult, and doing so may prove to have significant performance and
privacy ramifications. Therefore, it is often the case that cross-organizational audit logging simply
captures the identity of individuals who issue requests at the initial system, and subsequent
systems record that the requests originated from authorized individuals. Organizations consider
including processes for coordinating audit information requirements and protection of audit
information in information exchange agreements.
Related Controls:  AU-3, AU-6, AU-7, CA-3, PT-7.
Control Enhancements:
(1) CROSS-ORGANIZATIONAL AUDIT LOGGING | IDENTITY PRESERVATION
Preserve the identity of individuals in cross-organizational audit trails.
Discussion:  Identity preservation is applied when there is a need to be able to trace actions
that are performed across organizational boundaries to a specific individual.
Related Controls:  IA-2, IA-4, IA-5, IA-8.
(2) CROSS-ORGANIZATIONAL AUDIT LOGGING | SHARING OF AUDIT INFORMATION
Provide cross-organizational audit information to [Assignment: organization-defined
organizations] based on [Assignment: organization-defined cross-organizational sharing
agreements].
Discussion:  Due to the distributed nature of the audit information, cross-organization
sharing of audit information may be essential for effective analysis of the auditing being
performed. For example, the audit records of one organization may not provide sufficient
information to determine the appropriate or inappropriate use of organizational information
resources by individuals in other organizations. In some instances, only individuals’ home
organizations have the appropriate knowledge to make such determinations, thus requiring
the sharing of audit information among organizations.
Related Controls:  IR-4, SI-4.
(3) CROSS-ORGANIZATIONAL AUDITING | DISASSOCIABILITY
Implement [Assignment: organization-defined measures] to disassociate individuals from
audit information transmitted across organizational boundaries.
Discussion:  Preserving identities in audit trails could have privacy ramifications, such as
enabling the tracking and profiling of individuals, but may not be operationally necessary.
These risks could be further amplified when transmitting information across organizational
boundaries. Implementing privacy-enhancing cryptographic techniques can disassociate
individuals from audit information and reduce privacy risk while maintaining accountability.
CHAPTER THREE   PAGE 82
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
Related Controls:  None.
References:  None.
