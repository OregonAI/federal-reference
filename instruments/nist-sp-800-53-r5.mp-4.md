---
schema_version: 1
corpus: federal-reference
jurisdiction: us
id: nist-sp-800-53-r5.mp-4
title: NIST SP 800-53 Rev. 5 MP-4 — MEDIA STORAGE
doc_type: federal_instrument
citation: NIST SP 800-53 Rev. 5 MP-4
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

**NIST SP 800-53 Rev. 5 MP-4** — MEDIA STORAGE

- Issued by: National Institute of Standards and Technology
- Publication: NIST SP 800-53 Rev. 5 — Security and Privacy Controls for Information Systems and Organizations ([nist-sp-800-53-r5](./nist-sp-800-53-r5.md))
- Version: Rev. 5 (September 2020, includes updates as of 2020-12-10)
- Text as of: 2026-11-12
- Cited by held documents: 32 times (cjis-sp-6-1 ×25, arc-ampe ×3, irs-pub-1075-11-2021 ×3, 6-cfr-37 ×1), 1 of them naming an enhancement of this control
- Reproduction basis: 17 U.S.C. § 105 — work of the U.S. government (NIST). Determined per document on 2026-11-12 against the publication itself, not assumed from its issuer: its Authority statement (PDF page 3) reads "This publication may be used by nongovernmental organizations on a voluntary basis and is not subject to copyright in the United States. Attribution would, however, be appreciated by NIST." Held here: the front matter and Chapter Three (the control catalog) only. Chapter Three names ISO/IEC standards solely as bibliographic references and reproduces none of their text. NOT mirrored: the References bibliography and Appendices A-C; Appendix A (glossary) adapts third-party definitions (ISO/IEC 15026, ISO 25237, ISO/IEC 29100, ISO 15288, IETF RFC 4949), which ADR-0002 treats as not reproducible by being incorporated, and whose reproducibility has not been determined.


_NON-AUTHORITATIVE copy of one control, cut from the SP 800-53 Rev. 5 snapshot this corpus holds. Whether and how this binds a given agency depends on the instrument that incorporates it — read it at the source URL before relying on it. This copy is the Rev. 5 text of record, which is not necessarily the text a citing document meant (a document citing Rev. 4 is not answered by it)._


## Full text

### MP-4 MEDIA STORAGE
Control:
CHAPTER THREE   PAGE 173
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
a. Physically control and securely store [Assignment: organization-defined types of digital
and/or non-digital media] within [Assignment: organization-defined controlled areas]; and
b. Protect system media types defined in MP-4a until the media are destroyed or sanitized
using approved equipment, techniques, and procedures.
Discussion:  System media includes digital and non-digital media. Digital media includes flash
drives, diskettes, magnetic tapes, external or removable hard disk drives (e.g., solid state,
magnetic), compact discs, and digital versatile discs. Non-digital media includes paper and
microfilm. Physically controlling stored media includes conducting inventories, ensuring
procedures are in place to allow individuals to check out and return media to the library, and
maintaining accountability for stored media. Secure storage includes a locked drawer, desk, or
cabinet or a controlled media library. The type of media storage is commensurate with the
security category or classification of the information on the media. Controlled areas are spaces
that provide physical and procedural controls to meet the requirements established for
protecting information and systems. Fewer controls may be needed for media that contains
information determined to be in the public domain, publicly releasable, or have limited adverse
impacts on organizations, operations, or individuals if accessed by other than authorized
personnel. In these situations, physical access controls provide adequate protection.
Related Controls:  AC-19, CP-2, CP-6, CP-9, CP-10, MP-2, MP-7, PE-3, PL-2, SC-12, SC-13, SC-28,
SC-34, SI-12.
Control Enhancements:
(1) MEDIA STORAGE | CRYPTOGRAPHIC PROTECTION
[Withdrawn: Incorporated into SC-28(1).]
(2) MEDIA STORAGE | AUTOMATED RESTRICTED ACCESS
Restrict access to media storage areas and log access attempts and access granted using
[Assignment: organization-defined automated mechanisms].
Discussion:  Automated mechanisms include keypads, biometric readers, or card readers on
the external entries to media storage areas.
Related Controls:  AC-3, AU-2, AU-6, AU-9, AU-12, PE-3.
References:  [FIPS 199], [SP 800-56A], [SP 800-56B], [SP 800-56C], [SP 800-57-1], [SP 800-57-2],
[SP 800-57-3], [SP 800-111].
