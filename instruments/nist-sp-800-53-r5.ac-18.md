---
schema_version: 1
corpus: federal-reference
jurisdiction: us
id: nist-sp-800-53-r5.ac-18
title: NIST SP 800-53 Rev. 5 AC-18 — WIRELESS ACCESS
doc_type: federal_instrument
citation: NIST SP 800-53 Rev. 5 AC-18
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

**NIST SP 800-53 Rev. 5 AC-18** — WIRELESS ACCESS

- Issued by: National Institute of Standards and Technology
- Publication: NIST SP 800-53 Rev. 5 — Security and Privacy Controls for Information Systems and Organizations ([nist-sp-800-53-r5](./nist-sp-800-53-r5.md))
- Version: Rev. 5 (September 2020, includes updates as of 2020-12-10)
- Text as of: 2026-11-12
- Cited by held documents: 31 times (cjis-sp-6-1 ×26, irs-pub-1075-11-2021 ×3, 6-cfr-37 ×1, arc-ampe ×1), 1 of them naming an enhancement of this control
- Reproduction basis: 17 U.S.C. § 105 — work of the U.S. government (NIST). Determined per document on 2026-11-12 against the publication itself, not assumed from its issuer: its Authority statement (PDF page 3) reads "This publication may be used by nongovernmental organizations on a voluntary basis and is not subject to copyright in the United States. Attribution would, however, be appreciated by NIST." Held here: the front matter and Chapter Three (the control catalog) only. Chapter Three names ISO/IEC standards solely as bibliographic references and reproduces none of their text. NOT mirrored: the References bibliography and Appendices A-C; Appendix A (glossary) adapts third-party definitions (ISO/IEC 15026, ISO 25237, ISO/IEC 29100, ISO 15288, IETF RFC 4949), which ADR-0002 treats as not reproducible by being incorporated, and whose reproducibility has not been determined.


_NON-AUTHORITATIVE copy of one control, cut from the SP 800-53 Rev. 5 snapshot this corpus holds. Whether and how this binds a given agency depends on the instrument that incorporates it — read it at the source URL before relying on it. This copy is the Rev. 5 text of record, which is not necessarily the text a citing document meant (a document citing Rev. 4 is not answered by it)._


## Full text

### AC-18 WIRELESS ACCESS
Control:
a. Establish configuration requirements, connection requirements, and implementation
guidance for each type of wireless access; and
b. Authorize each type of wireless access to the system prior to allowing such connections.
Discussion:  Wireless technologies include microwave, packet radio (ultra-high frequency or very
high frequency), 802.11x, and Bluetooth. Wireless networks use authentication protocols that
provide authenticator protection and mutual authentication.
Related Controls:  AC-2, AC-3, AC-17, AC-19, CA-9, CM-7, IA-2, IA-3, IA-8, PL-4, SC-40, SC-43, SI-4.
Control Enhancements:
(1) WIRELESS ACCESS | AUTHENTICATION AND ENCRYPTION
Protect wireless access to the system using authentication of [Selection (one or more):
users; devices] and encryption.
Discussion:  Wireless networking capabilities represent a significant potential vulnerability
that can be exploited by adversaries. To protect systems with wireless access points, strong
authentication of users and devices along with strong encryption can reduce susceptibility to
threats by adversaries involving wireless technologies.
Related Controls:  SC-8, SC-12, SC-13.
(2) WIRELESS ACCESS | MONITORING UNAUTHORIZED CONNECTIONS
[Withdrawn: Incorporated into SI-4.]
(3) WIRELESS ACCESS | DISABLE WIRELESS NETWORKING
Disable, when not intended for use, wireless networking capabilities embedded within
system components prior to issuance and deployment.
CHAPTER THREE   PAGE 51
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
Discussion:  Wireless networking capabilities that are embedded within system components
represent a significant potential vulnerability that can be exploited by adversaries. Disabling
wireless capabilities when not needed for essential organizational missions or functions can
reduce susceptibility to threats by adversaries involving wireless technologies.
Related Controls:  None.
(4) WIRELESS ACCESS | RESTRICT CONFIGURATIONS BY USERS
Identify and explicitly authorize users allowed to independently configure wireless
networking capabilities.
Discussion:  Organizational authorizations to allow selected users to configure wireless
networking capabilities are enforced, in part, by the access enforcement mechanisms
employed within organizational systems.
Related Controls:  SC-7, SC-15.
(5) WIRELESS ACCESS | ANTENNAS AND TRANSMISSION POWER LEVELS
Select radio antennas and calibrate transmission power levels to reduce the probability
that signals from wireless access points can be received outside of organization-controlled
boundaries.
Discussion:  Actions that may be taken to limit unauthorized use of wireless communications
outside of organization-controlled boundaries include reducing the power of wireless
transmissions so that the transmissions are less likely to emit a signal that can be captured
outside of the physical perimeters of the organization, employing measures such as
emissions security to control wireless emanations, and using directional or beamforming
antennas that reduce the likelihood that unintended receivers will be able to intercept
signals. Prior to taking such mitigating actions, organizations can conduct periodic wireless
surveys to understand the radio frequency profile of organizational systems as well as other
systems that may be operating in the area.
Related Controls:  PE-19.
References:  [SP 800-94], [SP 800-97].
