---
schema_version: 1
corpus: federal-reference
jurisdiction: us
id: nist-sp-800-53-r5.mp-2
title: NIST SP 800-53 Rev. 5 MP-2 — MEDIA ACCESS
doc_type: federal_instrument
citation: NIST SP 800-53 Rev. 5 MP-2
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

**NIST SP 800-53 Rev. 5 MP-2** — MEDIA ACCESS

- Issued by: National Institute of Standards and Technology
- Publication: NIST SP 800-53 Rev. 5 — Security and Privacy Controls for Information Systems and Organizations ([nist-sp-800-53-r5](./nist-sp-800-53-r5.md))
- Version: Rev. 5 (September 2020, includes updates as of 2020-12-10)
- Text as of: 2026-11-12
- Cited by held documents: 24 times (cjis-sp-6-1 ×16, arc-ampe ×3, irs-pub-1075-11-2021 ×3, 6-cfr-37 ×2)
- Reproduction basis: 17 U.S.C. § 105 — work of the U.S. government (NIST). Determined per document on 2026-11-12 against the publication itself, not assumed from its issuer: its Authority statement (PDF page 3) reads "This publication may be used by nongovernmental organizations on a voluntary basis and is not subject to copyright in the United States. Attribution would, however, be appreciated by NIST." Held here: the front matter and Chapter Three (the control catalog) only. Chapter Three names ISO/IEC standards solely as bibliographic references and reproduces none of their text. NOT mirrored: the References bibliography and Appendices A-C; Appendix A (glossary) adapts third-party definitions (ISO/IEC 15026, ISO 25237, ISO/IEC 29100, ISO 15288, IETF RFC 4949), which ADR-0002 treats as not reproducible by being incorporated, and whose reproducibility has not been determined.


_NON-AUTHORITATIVE copy of one control, cut from the SP 800-53 Rev. 5 snapshot this corpus holds. Whether and how this binds a given agency depends on the instrument that incorporates it — read it at the source URL before relying on it. This copy is the Rev. 5 text of record, which is not necessarily the text a citing document meant (a document citing Rev. 4 is not answered by it)._


## Full text

### MP-2 MEDIA ACCESS
Control:  Restrict access to [Assignment: organization-defined types of digital and/or non-digital
media] to [Assignment: organization-defined personnel or roles].
Discussion:  System media includes digital and non-digital media. Digital media includes flash
drives, diskettes, magnetic tapes, external or removable hard disk drives (e.g., solid state,
magnetic), compact discs, and digital versatile discs. Non-digital media includes paper and
microfilm. Denying access to patient medical records in a community hospital unless the
individuals seeking access to such records are authorized healthcare providers is an example of
restricting access to non-digital media. Limiting access to the design specifications stored on
compact discs in the media library to individuals on the system development team is an example
of restricting access to digital media.
Related Controls:  AC-19, AU-9, CP-2, CP-9, CP-10, MA-5, MP-4, MP-6, PE-2, PE-3, SC-12, SC-13,
SC-34, SI-12.
Control Enhancements:
(1) MEDIA ACCESS | AUTOMATED RESTRICTED ACCESS
[Withdrawn: Incorporated into MP-4(2).]
(2) MEDIA ACCESS | CRYPTOGRAPHIC PROTECTION
[Withdrawn: Incorporated into SC-28(1).]
References:  [OMB A-130], [FIPS 199], [SP 800-111].
