---
schema_version: 1
corpus: federal-reference
jurisdiction: us
id: nist-sp-800-53-r5.pe-14
title: NIST SP 800-53 Rev. 5 PE-14 — ENVIRONMENTAL CONTROLS
doc_type: federal_instrument
citation: NIST SP 800-53 Rev. 5 PE-14
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

**NIST SP 800-53 Rev. 5 PE-14** — ENVIRONMENTAL CONTROLS

- Issued by: National Institute of Standards and Technology
- Publication: NIST SP 800-53 Rev. 5 — Security and Privacy Controls for Information Systems and Organizations ([nist-sp-800-53-r5](./nist-sp-800-53-r5.md))
- Version: Rev. 5 (September 2020, includes updates as of 2020-12-10)
- Text as of: 2026-11-12
- Cited by held documents: 7 times (cjis-sp-6-1 ×6, 6-cfr-37 ×1)
- Reproduction basis: 17 U.S.C. § 105 — work of the U.S. government (NIST). Determined per document on 2026-11-12 against the publication itself, not assumed from its issuer: its Authority statement (PDF page 3) reads "This publication may be used by nongovernmental organizations on a voluntary basis and is not subject to copyright in the United States. Attribution would, however, be appreciated by NIST." Held here: the front matter and Chapter Three (the control catalog) only. Chapter Three names ISO/IEC standards solely as bibliographic references and reproduces none of their text. NOT mirrored: the References bibliography and Appendices A-C; Appendix A (glossary) adapts third-party definitions (ISO/IEC 15026, ISO 25237, ISO/IEC 29100, ISO 15288, IETF RFC 4949), which ADR-0002 treats as not reproducible by being incorporated, and whose reproducibility has not been determined.


_NON-AUTHORITATIVE copy of one control, cut from the SP 800-53 Rev. 5 snapshot this corpus holds. Whether and how this binds a given agency depends on the instrument that incorporates it — read it at the source URL before relying on it. This copy is the Rev. 5 text of record, which is not necessarily the text a citing document meant (a document citing Rev. 4 is not answered by it)._


## Full text

### PE-14 ENVIRONMENTAL CONTROLS
Control:
a. Maintain [Selection (one or more): temperature; humidity; pressure; radiation; [Assignment:
organization-defined environmental control]] levels within the facility where the system
resides at [Assignment: organization-defined acceptable levels]; and
b. Monitor environmental control levels [Assignment: organization-defined frequency].
Discussion:  The provision of environmental controls applies primarily to organizational facilities
that contain concentrations of system resources (e.g., data centers, mainframe computer rooms,
and server rooms). Insufficient environmental controls, especially in very harsh environments,
can have a significant adverse impact on the availability of systems and system components that
are needed to support organizational mission and business functions.
Related Controls:  AT-3, CP-2.
Control Enhancements:
(1) ENVIRONMENTAL CONTROLS | AUTOMATIC CONTROLS
CHAPTER THREE   PAGE 190
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
Employ the following automatic environmental controls in the facility to prevent
fluctuations potentially harmful to the system: [Assignment: organization-defined
automatic environmental controls].
Discussion:  The implementation of automatic environmental controls provides an
immediate response to environmental conditions that can damage, degrade, or destroy
organizational systems or systems components.
Related Controls:  None.
(2) ENVIRONMENTAL CONTROLS | MONITORING WITH ALARMS AND NOTIFICATIONS
Employ environmental control monitoring that provides an alarm or notification of
changes potentially harmful to personnel or equipment to [Assignment: organization-
defined personnel or roles].
Discussion:  The alarm or notification may be an audible alarm or a visual message in real
time to personnel or roles defined by the organization. Such alarms and notifications can
help minimize harm to individuals and damage to organizational assets by facilitating a
timely incident response.
Related Controls:  None.
References:  None.
