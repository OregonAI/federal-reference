---
schema_version: 1
corpus: federal-reference
jurisdiction: us
id: nist-sp-800-53-r5.pe-6
title: NIST SP 800-53 Rev. 5 PE-6 — MONITORING PHYSICAL ACCESS
doc_type: federal_instrument
citation: NIST SP 800-53 Rev. 5 PE-6
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

**NIST SP 800-53 Rev. 5 PE-6** — MONITORING PHYSICAL ACCESS

- Issued by: National Institute of Standards and Technology
- Publication: NIST SP 800-53 Rev. 5 — Security and Privacy Controls for Information Systems and Organizations ([nist-sp-800-53-r5](./nist-sp-800-53-r5.md))
- Version: Rev. 5 (September 2020, includes updates as of 2020-12-10)
- Text as of: 2026-11-12
- Cited by held documents: 22 times (cjis-sp-6-1 ×14, irs-pub-1075-11-2021 ×5, arc-ampe ×2, 6-cfr-37 ×1)
- Reproduction basis: 17 U.S.C. § 105 — work of the U.S. government (NIST). Determined per document on 2026-11-12 against the publication itself, not assumed from its issuer: its Authority statement (PDF page 3) reads "This publication may be used by nongovernmental organizations on a voluntary basis and is not subject to copyright in the United States. Attribution would, however, be appreciated by NIST." Held here: the front matter and Chapter Three (the control catalog) only. Chapter Three names ISO/IEC standards solely as bibliographic references and reproduces none of their text. NOT mirrored: the References bibliography and Appendices A-C; Appendix A (glossary) adapts third-party definitions (ISO/IEC 15026, ISO 25237, ISO/IEC 29100, ISO 15288, IETF RFC 4949), which ADR-0002 treats as not reproducible by being incorporated, and whose reproducibility has not been determined.


_NON-AUTHORITATIVE copy of one control, cut from the SP 800-53 Rev. 5 snapshot this corpus holds. Whether and how this binds a given agency depends on the instrument that incorporates it — read it at the source URL before relying on it. This copy is the Rev. 5 text of record, which is not necessarily the text a citing document meant (a document citing Rev. 4 is not answered by it)._


## Full text

### PE-6 MONITORING PHYSICAL ACCESS
Control:
a. Monitor physical access to the facility where the system resides to detect and respond to
physical security incidents;
b. Review physical access logs [Assignment: organization-defined frequency] and upon
occurrence of [Assignment: organization-defined events or potential indications of events];
and
c. Coordinate results of reviews and investigations with the organizational incident response
capability.
Discussion:  Physical access monitoring includes publicly accessible areas within organizational
facilities. Examples of physical access monitoring include the employment of guards, video
surveillance equipment (i.e., cameras), and sensor devices. Reviewing physical access logs can
help identify suspicious activity, anomalous events, or potential threats. The reviews can be
supported by audit logging controls, such as AU-2, if the access logs are part of an automated
system. Organizational incident response capabilities include investigations of physical security
incidents and responses to the incidents. Incidents include security violations or suspicious
physical access activities. Suspicious physical access activities include accesses outside of normal
work hours, repeated accesses to areas not normally accessed, accesses for unusual lengths of
time, and out-of-sequence accesses.
Related Controls:  AU-2, AU-6, AU-9, AU-12, CA-7, CP-10, IR-4, IR-8.
Control Enhancements:
(1) MONITORING PHYSICAL ACCESS | INTRUSION ALARMS AND SURVEILLANCE EQUIPMENT
Monitor physical access to the facility where the system resides using physical intrusion
alarms and surveillance equipment.
Discussion:  Physical intrusion alarms can be employed to alert security personnel when
unauthorized access to the facility is attempted. Alarm systems work in conjunction with
physical barriers, physical access control systems, and security guards by triggering a
response when these other forms of security have been compromised or breached. Physical
intrusion alarms can include different types of sensor devices, such as motion sensors,
contact sensors, and broken glass sensors. Surveillance equipment includes video cameras
installed at strategic locations throughout the facility.
Related Controls:  None.
(2) MONITORING PHYSICAL ACCESS | AUTOMATED INTRUSION RECOGNITION AND RESPONSES
Recognize [Assignment: organization-defined classes or types of intrusions] and initiate
[Assignment: organization-defined response actions] using [Assignment: organization-
defined automated mechanisms].
Discussion:  Response actions can include notifying selected organizational personnel or law
enforcement personnel. Automated mechanisms implemented to initiate response actions
include system alert notifications, email and text messages, and activating door locking
mechanisms. Physical access monitoring can be coordinated with intrusion detection
CHAPTER THREE   PAGE 185
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
systems and system monitoring capabilities to provide integrated threat coverage for the
organization.
Related Controls:  SI-4.
(3) MONITORING PHYSICAL ACCESS | VIDEO SURVEILLANCE
(a) Employ video surveillance of [Assignment: organization-defined operational areas];
(b) Review video recordings [Assignment: organization-defined frequency]; and
(c) Retain video recordings for [Assignment: organization-defined time period].
Discussion:  Video surveillance focuses on recording activity in specified areas for the
purposes of subsequent review, if circumstances so warrant. Video recordings are typically
reviewed to detect anomalous events or incidents. Monitoring the surveillance video is not
required, although organizations may choose to do so. There may be legal considerations
when performing and retaining video surveillance, especially if such surveillance is in a public
location.
Related Controls:  None.
(4) MONITORING PHYSICAL ACCESS | MONITORING PHYSICAL ACCESS TO SYSTEMS
Monitor physical access to the system in addition to the physical access monitoring of the
facility at [Assignment: organization-defined physical spaces containing one or more
components of the system].
Discussion:  Monitoring physical access to systems provides additional monitoring for those
areas within facilities where there is a concentration of system components, including server
rooms, media storage areas, and communications centers. Physical access monitoring can be
coordinated with intrusion detection systems and system monitoring capabilities to provide
comprehensive and integrated threat coverage for the organization.
Related Controls:  None.
References:  None.
