---
schema_version: 1
corpus: federal-reference
jurisdiction: us
id: nist-sp-800-53-r5.pe-9
title: NIST SP 800-53 Rev. 5 PE-9 — POWER EQUIPMENT AND CABLING
doc_type: federal_instrument
citation: NIST SP 800-53 Rev. 5 PE-9
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

**NIST SP 800-53 Rev. 5 PE-9** — POWER EQUIPMENT AND CABLING

- Issued by: National Institute of Standards and Technology
- Publication: NIST SP 800-53 Rev. 5 — Security and Privacy Controls for Information Systems and Organizations ([nist-sp-800-53-r5](./nist-sp-800-53-r5.md))
- Version: Rev. 5 (September 2020, includes updates as of 2020-12-10)
- Text as of: 2026-11-12
- Cited by held documents: 8 times (cjis-sp-6-1 ×5, arc-ampe ×2, 6-cfr-37 ×1)
- Reproduction basis: 17 U.S.C. § 105 — work of the U.S. government (NIST). Determined per document on 2026-11-12 against the publication itself, not assumed from its issuer: its Authority statement (PDF page 3) reads "This publication may be used by nongovernmental organizations on a voluntary basis and is not subject to copyright in the United States. Attribution would, however, be appreciated by NIST." Held here: the front matter and Chapter Three (the control catalog) only. Chapter Three names ISO/IEC standards solely as bibliographic references and reproduces none of their text. NOT mirrored: the References bibliography and Appendices A-C; Appendix A (glossary) adapts third-party definitions (ISO/IEC 15026, ISO 25237, ISO/IEC 29100, ISO 15288, IETF RFC 4949), which ADR-0002 treats as not reproducible by being incorporated, and whose reproducibility has not been determined.


_NON-AUTHORITATIVE copy of one control, cut from the SP 800-53 Rev. 5 snapshot this corpus holds. Whether and how this binds a given agency depends on the instrument that incorporates it — read it at the source URL before relying on it. This copy is the Rev. 5 text of record, which is not necessarily the text a citing document meant (a document citing Rev. 4 is not answered by it)._


## Full text

### PE-9 POWER EQUIPMENT AND CABLING
Control:  Protect power equipment and power cabling for the system from damage and
destruction.
Discussion:  Organizations determine the types of protection necessary for the power equipment
and cabling employed at different locations that are both internal and external to organizational
facilities and environments of operation. Types of power equipment and cabling include internal
cabling and uninterruptable power sources in offices or data centers, generators and power
cabling outside of buildings, and power sources for self-contained components such as satellites,
vehicles, and other deployable systems.
Related Controls:  PE-4.
Control Enhancements:
(1) POWER EQUIPMENT AND CABLING | REDUNDANT CABLING
Employ redundant power cabling paths that are physically separated by [Assignment:
organization-defined distance].
Discussion:  Physically separate and redundant power cables ensure that power continues to
flow in the event that one of the cables is cut or otherwise damaged.
Related Controls:  None.
(2) POWER EQUIPMENT AND CABLING | AUTOMATIC VOLTAGE CONTROLS
Employ automatic voltage controls for [Assignment: organization-defined critical system
components].
Discussion:  Automatic voltage controls can monitor and control voltage. Such controls
include voltage regulators, voltage conditioners, and voltage stabilizers.
Related Controls:  None.
References:  None.
CHAPTER THREE   PAGE 187
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
