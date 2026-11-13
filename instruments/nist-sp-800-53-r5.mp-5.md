---
schema_version: 1
corpus: federal-reference
jurisdiction: us
id: nist-sp-800-53-r5.mp-5
title: NIST SP 800-53 Rev. 5 MP-5 — MEDIA TRANSPORT
doc_type: federal_instrument
citation: NIST SP 800-53 Rev. 5 MP-5
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

**NIST SP 800-53 Rev. 5 MP-5** — MEDIA TRANSPORT

- Issued by: National Institute of Standards and Technology
- Publication: NIST SP 800-53 Rev. 5 — Security and Privacy Controls for Information Systems and Organizations ([nist-sp-800-53-r5](./nist-sp-800-53-r5.md))
- Version: Rev. 5 (September 2020, includes updates as of 2020-12-10)
- Text as of: 2026-11-12
- Cited by held documents: 23 times (cjis-sp-6-1 ×15, irs-pub-1075-11-2021 ×4, arc-ampe ×3, 6-cfr-37 ×1)
- Reproduction basis: 17 U.S.C. § 105 — work of the U.S. government (NIST). Determined per document on 2026-11-12 against the publication itself, not assumed from its issuer: its Authority statement (PDF page 3) reads "This publication may be used by nongovernmental organizations on a voluntary basis and is not subject to copyright in the United States. Attribution would, however, be appreciated by NIST." Held here: the front matter and Chapter Three (the control catalog) only. Chapter Three names ISO/IEC standards solely as bibliographic references and reproduces none of their text. NOT mirrored: the References bibliography and Appendices A-C; Appendix A (glossary) adapts third-party definitions (ISO/IEC 15026, ISO 25237, ISO/IEC 29100, ISO 15288, IETF RFC 4949), which ADR-0002 treats as not reproducible by being incorporated, and whose reproducibility has not been determined.


_NON-AUTHORITATIVE copy of one control, cut from the SP 800-53 Rev. 5 snapshot this corpus holds. Whether and how this binds a given agency depends on the instrument that incorporates it — read it at the source URL before relying on it. This copy is the Rev. 5 text of record, which is not necessarily the text a citing document meant (a document citing Rev. 4 is not answered by it)._


## Full text

### MP-5 MEDIA TRANSPORT
Control:
a. Protect and control [Assignment: organization-defined types of system media] during
transport outside of controlled areas using [Assignment: organization-defined controls];
b. Maintain accountability for system media during transport outside of controlled areas;
c. Document activities associated with the transport of system media; and
d. Restrict the activities associated with the transport of system media to authorized
personnel.
Discussion:  System media includes digital and non-digital media. Digital media includes flash
drives, diskettes, magnetic tapes, external or removable hard disk drives (e.g., solid state and
magnetic), compact discs, and digital versatile discs. Non-digital media includes microfilm and
paper. Controlled areas are spaces for which organizations provide physical or procedural
controls to meet requirements established for protecting information and systems. Controls to
protect media during transport include cryptography and locked containers. Cryptographic
CHAPTER THREE   PAGE 174
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
mechanisms can provide confidentiality and integrity protections depending on the mechanisms
implemented. Activities associated with media transport include releasing media for transport,
ensuring that media enters the appropriate transport processes, and the actual transport.
Authorized transport and courier personnel may include individuals external to the organization.
Maintaining accountability of media during transport includes restricting transport activities to
authorized personnel and tracking and/or obtaining records of transport activities as the media
moves through the transportation system to prevent and detect loss, destruction, or tampering.
Organizations establish documentation requirements for activities associated with the transport
of system media in accordance with organizational assessments of risk. Organizations maintain
the flexibility to define record-keeping methods for the different types of media transport as part
of a system of transport-related records.
Related Controls:  AC-7, AC-19, CP-2, CP-9, MP-3, MP-4, PE-16, PL-2, SC-12, SC-13, SC-28, SC-34.
Control Enhancements:
(1) MEDIA TRANSPORT | PROTECTION OUTSIDE OF CONTROLLED AREAS
[Withdrawn: Incorporated into MP-5.]
(2) MEDIA TRANSPORT | DOCUMENTATION OF ACTIVITIES
[Withdrawn: Incorporated into MP-5.]
(3) MEDIA TRANSPORT | CUSTODIANS
Employ an identified custodian during transport of system media outside of controlled
areas.
Discussion:  Identified custodians provide organizations with specific points of contact during
the media transport process and facilitate individual accountability. Custodial responsibilities
can be transferred from one individual to another if an unambiguous custodian is identified.
Related Controls:  None.
(4) MEDIA TRANSPORT | CRYPTOGRAPHIC PROTECTION
[Withdrawn: Incorporated into SC-28(1).]
References:  [FIPS 199], [SP 800-60-1], [SP 800-60-2].
