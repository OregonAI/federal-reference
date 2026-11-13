---
schema_version: 1
corpus: federal-reference
jurisdiction: us
id: nist-sp-800-53-r5.sc-37
title: NIST SP 800-53 Rev. 5 SC-37 — OUT-OF-BAND CHANNELS
doc_type: federal_instrument
citation: NIST SP 800-53 Rev. 5 SC-37
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

**NIST SP 800-53 Rev. 5 SC-37** — OUT-OF-BAND CHANNELS

- Issued by: National Institute of Standards and Technology
- Publication: NIST SP 800-53 Rev. 5 — Security and Privacy Controls for Information Systems and Organizations ([nist-sp-800-53-r5](./nist-sp-800-53-r5.md))
- Version: Rev. 5 (September 2020, includes updates as of 2020-12-10)
- Text as of: 2026-11-12
- Cited by held documents: 1 time (arc-ampe ×1)
- Reproduction basis: 17 U.S.C. § 105 — work of the U.S. government (NIST). Determined per document on 2026-11-12 against the publication itself, not assumed from its issuer: its Authority statement (PDF page 3) reads "This publication may be used by nongovernmental organizations on a voluntary basis and is not subject to copyright in the United States. Attribution would, however, be appreciated by NIST." Held here: the front matter and Chapter Three (the control catalog) only. Chapter Three names ISO/IEC standards solely as bibliographic references and reproduces none of their text. NOT mirrored: the References bibliography and Appendices A-C; Appendix A (glossary) adapts third-party definitions (ISO/IEC 15026, ISO 25237, ISO/IEC 29100, ISO 15288, IETF RFC 4949), which ADR-0002 treats as not reproducible by being incorporated, and whose reproducibility has not been determined.


_NON-AUTHORITATIVE copy of one control, cut from the SP 800-53 Rev. 5 snapshot this corpus holds. Whether and how this binds a given agency depends on the instrument that incorporates it — read it at the source URL before relying on it. This copy is the Rev. 5 text of record, which is not necessarily the text a citing document meant (a document citing Rev. 4 is not answered by it)._


## Full text

### SC-37 OUT-OF-BAND CHANNELS
Control:  Employ the following out-of-band channels for the physical delivery or electronic
transmission of [Assignment: organization-defined information, system components, or devices]
to [Assignment: organization-defined individuals or systems]: [Assignment: organization-defined
out-of-band channels].
Discussion:  Out-of-band channels include local, non-network accesses to systems; network paths
physically separate from network paths used for operational traffic; or non-electronic paths, such
as the U.S. Postal Service. The use of out-of-band channels is contrasted with the use of in-band
channels (i.e., the same channels) that carry routine operational traffic. Out-of-band channels do
not have the same vulnerability or exposure as in-band channels. Therefore, the confidentiality,
integrity, or availability compromises of in-band channels will not compromise or adversely affect
the out-of-band channels. Organizations may employ out-of-band channels in the delivery or
transmission of organizational items, including authenticators and credentials; cryptographic key
management information; system and data backups; configuration management changes for
hardware, firmware, or software; security updates; maintenance information; and malicious
code protection updates.
Related Controls:  AC-2, CM-3, CM-5, CM-7, IA-2, IA-4, IA-5, MA-4, SC-12, SI-3, SI-4, SI-7.
Control Enhancements:
(1) OUT-OF-BAND CHANNELS | ENSURE DELIVERY AND TRANSMISSION
Employ [Assignment: organization-defined controls] to ensure that only [Assignment:
organization-defined individuals or systems] receive the following information, system
components, or devices: [Assignment: organization-defined information, system
components, or devices].
Discussion:  Techniques employed by organizations to ensure that only designated systems
or individuals receive certain information, system components, or devices include sending
authenticators via an approved courier service but requiring recipients to show some form
of government-issued photographic identification as a condition of receipt.
Related Controls:  None.
References:  [SP 800-57-1], [SP 800-57-2], [SP 800-57-3].
