---
schema_version: 1
corpus: federal-reference
jurisdiction: us
id: nist-sp-800-53-r5.pe-13
title: NIST SP 800-53 Rev. 5 PE-13 — FIRE PROTECTION
doc_type: federal_instrument
citation: NIST SP 800-53 Rev. 5 PE-13
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

**NIST SP 800-53 Rev. 5 PE-13** — FIRE PROTECTION

- Issued by: National Institute of Standards and Technology
- Publication: NIST SP 800-53 Rev. 5 — Security and Privacy Controls for Information Systems and Organizations ([nist-sp-800-53-r5](./nist-sp-800-53-r5.md))
- Version: Rev. 5 (September 2020, includes updates as of 2020-12-10)
- Text as of: 2026-11-12
- Cited by held documents: 5 times (cjis-sp-6-1 ×4, 6-cfr-37 ×1)
- Reproduction basis: 17 U.S.C. § 105 — work of the U.S. government (NIST). Determined per document on 2026-11-12 against the publication itself, not assumed from its issuer: its Authority statement (PDF page 3) reads "This publication may be used by nongovernmental organizations on a voluntary basis and is not subject to copyright in the United States. Attribution would, however, be appreciated by NIST." Held here: the front matter and Chapter Three (the control catalog) only. Chapter Three names ISO/IEC standards solely as bibliographic references and reproduces none of their text. NOT mirrored: the References bibliography and Appendices A-C; Appendix A (glossary) adapts third-party definitions (ISO/IEC 15026, ISO 25237, ISO/IEC 29100, ISO 15288, IETF RFC 4949), which ADR-0002 treats as not reproducible by being incorporated, and whose reproducibility has not been determined.


_NON-AUTHORITATIVE copy of one control, cut from the SP 800-53 Rev. 5 snapshot this corpus holds. Whether and how this binds a given agency depends on the instrument that incorporates it — read it at the source URL before relying on it. This copy is the Rev. 5 text of record, which is not necessarily the text a citing document meant (a document citing Rev. 4 is not answered by it)._


## Full text

### PE-13 FIRE PROTECTION
Control:  Employ and maintain fire detection and suppression systems that are supported by an
independent energy source.
Discussion:  The provision of fire detection and suppression systems applies primarily to
organizational facilities that contain concentrations of system resources, including data centers,
server rooms, and mainframe computer rooms. Fire detection and suppression systems that may
require an independent energy source include sprinkler systems and smoke detectors. An
independent energy source is an energy source, such as a microgrid, that is separate, or can be
separated, from the energy sources providing power for the other parts of the facility.
Related Controls:  AT-3.
Control Enhancements:
(1) FIRE PROTECTION | DETECTION SYSTEMS — AUTOMATIC ACTIVATION AND NOTIFICATION
Employ fire detection systems that activate automatically and notify [Assignment:
organization-defined personnel or roles] and [Assignment: organization-defined
emergency responders] in the event of a fire.
Discussion:  Organizations can identify personnel, roles, and emergency responders if
individuals on the notification list need to have access authorizations or clearances (e.g., to
enter to facilities where access is restricted due to the classification or impact level of
CHAPTER THREE   PAGE 189
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
information within the facility). Notification mechanisms may require independent energy
sources to ensure that the notification capability is not adversely affected by the fire.
Related Controls:  None.
(2) FIRE PROTECTION | SUPPRESSION SYSTEMS — AUTOMATIC ACTIVATION AND NOTIFICATION
(a) Employ fire suppression systems that activate automatically and notify [Assignment:
organization-defined personnel or roles] and [Assignment: organization-defined
emergency responders]; and
(b) Employ an automatic fire suppression capability when the facility is not staffed on a
continuous basis.
Discussion:  Organizations can identify specific personnel, roles, and emergency responders
if individuals on the notification list need to have appropriate access authorizations and/or
clearances (e.g., to enter to facilities where access is restricted due to the impact level or
classification of information within the facility). Notification mechanisms may require
independent energy sources to ensure that the notification capability is not adversely
affected by the fire.
Related Controls:  None.
(3) FIRE PROTECTION | AUTOMATIC FIRE SUPPRESSION
[Withdrawn: Incorporated into PE-13(2).]
(4) FIRE PROTECTION | INSPECTIONS
Ensure that the facility undergoes [Assignment: organization-defined frequency] fire
protection inspections by authorized and qualified inspectors and identified deficiencies
are resolved within [Assignment: organization-defined time period].
Discussion:  Authorized and qualified personnel within the jurisdiction of the organization
include state, county, and city fire inspectors and fire marshals. Organizations provide
escorts during inspections in situations where the systems that reside within the facilities
contain sensitive information.
Related Controls:  None.
References:  None.
