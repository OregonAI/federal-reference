---
schema_version: 1
corpus: federal-reference
jurisdiction: us
id: nist-sp-800-53-r5.pm-7
title: NIST SP 800-53 Rev. 5 PM-7 — ENTERPRISE ARCHITECTURE
doc_type: federal_instrument
citation: NIST SP 800-53 Rev. 5 PM-7
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

**NIST SP 800-53 Rev. 5 PM-7** — ENTERPRISE ARCHITECTURE

- Issued by: National Institute of Standards and Technology
- Publication: NIST SP 800-53 Rev. 5 — Security and Privacy Controls for Information Systems and Organizations ([nist-sp-800-53-r5](./nist-sp-800-53-r5.md))
- Version: Rev. 5 (September 2020, includes updates as of 2020-12-10)
- Text as of: 2026-11-12
- Cited by held documents: 7 times (irs-pub-1075-11-2021 ×5, arc-ampe ×2)
- Reproduction basis: 17 U.S.C. § 105 — work of the U.S. government (NIST). Determined per document on 2026-11-12 against the publication itself, not assumed from its issuer: its Authority statement (PDF page 3) reads "This publication may be used by nongovernmental organizations on a voluntary basis and is not subject to copyright in the United States. Attribution would, however, be appreciated by NIST." Held here: the front matter and Chapter Three (the control catalog) only. Chapter Three names ISO/IEC standards solely as bibliographic references and reproduces none of their text. NOT mirrored: the References bibliography and Appendices A-C; Appendix A (glossary) adapts third-party definitions (ISO/IEC 15026, ISO 25237, ISO/IEC 29100, ISO 15288, IETF RFC 4949), which ADR-0002 treats as not reproducible by being incorporated, and whose reproducibility has not been determined.


_NON-AUTHORITATIVE copy of one control, cut from the SP 800-53 Rev. 5 snapshot this corpus holds. Whether and how this binds a given agency depends on the instrument that incorporates it — read it at the source URL before relying on it. This copy is the Rev. 5 text of record, which is not necessarily the text a citing document meant (a document citing Rev. 4 is not answered by it)._


## Full text

### PM-7 ENTERPRISE ARCHITECTURE
Control:  Develop and maintain an enterprise architecture with consideration for information
security, privacy, and the resulting risk to organizational operations and assets, individuals, other
organizations, and the Nation.
Discussion:  The integration of security and privacy requirements and controls into the enterprise
architecture helps to ensure that security and privacy considerations are addressed throughout
the system development life cycle and are explicitly related to the organization’s mission and
business processes. The process of security and privacy requirements integration also embeds
into the enterprise architecture and the organization’s security and privacy architectures
consistent with the organizational risk management strategy. For PM-7, security and privacy
architectures are developed at a system-of-systems level, representing all organizational
CHAPTER THREE    PAGE 207
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
systems. For PL-8, the security and privacy architectures are developed at a level that represents
an individual system. The system-level architectures are consistent with the security and privacy
architectures defined for the organization. Security and privacy requirements and control
integration are most effectively accomplished through the rigorous application of the Risk
Management Framework [SP 800-37] and supporting security standards and guidelines.
Related Controls:  AU-6, PL-2, PL-8, PM-11, RA-2, SA-3, SA-8, SA-17.
Control Enhancements:
(1) ENTERPRISE ARCHITECTURE | OFFLOADING
Offload [Assignment: organization-defined non-essential functions or services] to other
systems, system components, or an external provider.
Discussion:  Not every function or service that a system provides is essential to
organizational mission or business functions. Printing or copying is an example of a non-
essential but supporting service for an organization. Whenever feasible, such supportive but
non-essential functions or services are not co-located with the functions or services that
support essential mission or business functions. Maintaining such functions on the same
system or system component increases the attack surface of the organization’s mission-
essential functions or services. Moving supportive but non-essential functions to a non-
critical system, system component, or external provider can also increase efficiency by
putting those functions or services under the control of individuals or providers who are
subject matter experts in the functions or services.
Related Controls:  SA-8.
References:  [OMB A-130], [SP 800-37], [SP 800-39], [SP 800-160-1], [SP 800-160-2].
