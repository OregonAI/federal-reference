---
schema_version: 1
corpus: federal-reference
jurisdiction: us
id: nist-sp-800-53-r5.sc-15
title: NIST SP 800-53 Rev. 5 SC-15 — COLLABORATIVE COMPUTING DEVICES AND APPLICATIONS
doc_type: federal_instrument
citation: NIST SP 800-53 Rev. 5 SC-15
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

**NIST SP 800-53 Rev. 5 SC-15** — COLLABORATIVE COMPUTING DEVICES AND APPLICATIONS

- Issued by: National Institute of Standards and Technology
- Publication: NIST SP 800-53 Rev. 5 — Security and Privacy Controls for Information Systems and Organizations ([nist-sp-800-53-r5](./nist-sp-800-53-r5.md))
- Version: Rev. 5 (September 2020, includes updates as of 2020-12-10)
- Text as of: 2026-11-12
- Cited by held documents: 12 times (cjis-sp-6-1 ×5, irs-pub-1075-11-2021 ×3, 6-cfr-37 ×2, arc-ampe ×2)
- Reproduction basis: 17 U.S.C. § 105 — work of the U.S. government (NIST). Determined per document on 2026-11-12 against the publication itself, not assumed from its issuer: its Authority statement (PDF page 3) reads "This publication may be used by nongovernmental organizations on a voluntary basis and is not subject to copyright in the United States. Attribution would, however, be appreciated by NIST." Held here: the front matter and Chapter Three (the control catalog) only. Chapter Three names ISO/IEC standards solely as bibliographic references and reproduces none of their text. NOT mirrored: the References bibliography and Appendices A-C; Appendix A (glossary) adapts third-party definitions (ISO/IEC 15026, ISO 25237, ISO/IEC 29100, ISO 15288, IETF RFC 4949), which ADR-0002 treats as not reproducible by being incorporated, and whose reproducibility has not been determined.


_NON-AUTHORITATIVE copy of one control, cut from the SP 800-53 Rev. 5 snapshot this corpus holds. Whether and how this binds a given agency depends on the instrument that incorporates it — read it at the source URL before relying on it. This copy is the Rev. 5 text of record, which is not necessarily the text a citing document meant (a document citing Rev. 4 is not answered by it)._


## Full text

### SC-15 COLLABORATIVE COMPUTING DEVICES AND APPLICATIONS
Control:
a. Prohibit remote activation of collaborative computing devices and applications with the
following exceptions: [Assignment: organization-defined exceptions where remote activation
is to be allowed]; and
b. Provide an explicit indication of use to users physically present at the devices.
Discussion:  Collaborative computing devices and applications include remote meeting devices
and applications, networked white boards, cameras, and microphones. The explicit indication of
use includes signals to users when collaborative computing devices and applications are
activated.
Related Controls:  AC-21, SC-42.
Control Enhancements:
CHAPTER THREE   PAGE 310
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
(1) COLLABORATIVE COMPUTING DEVICES | PHYSICAL OR LOGICAL DISCONNECT
Provide [Selection (one or more): physical; logical] disconnect of collaborative computing
devices in a manner that supports ease of use.
Discussion:  Failing to disconnect from collaborative computing devices can result in
subsequent compromises of organizational information. Providing easy methods to
disconnect from such devices after a collaborative computing session ensures that
participants carry out the disconnect activity without having to go through complex and
tedious procedures. Disconnect from collaborative computing devices can be manual or
automatic.
Related Controls:  None.
(2) COLLABORATIVE COMPUTING DEVICES | BLOCKING INBOUND AND OUTBOUND COMMUNICATIONS
TRAFFIC
[Withdrawn: Incorporated into SC-7.]
(3) COLLABORATIVE COMPUTING DEVICES | DISABLING AND REMOVAL IN SECURE WORK AREAS
Disable or remove collaborative computing devices and applications from [Assignment:
organization-defined systems or system components] in [Assignment: organization-defined
secure work areas].
Discussion:  Failing to disable or remove collaborative computing devices and applications
from systems or system components can result in compromises of information, including
eavesdropping on conversations. A Sensitive Compartmented Information Facility (SCIF) is
an example of a secure work area.
Related Controls:  None.
(4) COLLABORATIVE COMPUTING DEVICES | EXPLICITLY INDICATE CURRENT PARTICIPANTS
Provide an explicit indication of current participants in [Assignment: organization-defined
online meetings and teleconferences].
Discussion:  Explicitly indicating current participants prevents unauthorized individuals from
participating in collaborative computing sessions without the explicit knowledge of other
participants.
Related Controls:  None.
References:  None.
