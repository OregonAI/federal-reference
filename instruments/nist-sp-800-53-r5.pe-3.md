---
schema_version: 1
corpus: federal-reference
jurisdiction: us
id: nist-sp-800-53-r5.pe-3
title: NIST SP 800-53 Rev. 5 PE-3 — PHYSICAL ACCESS CONTROL
doc_type: federal_instrument
citation: NIST SP 800-53 Rev. 5 PE-3
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

**NIST SP 800-53 Rev. 5 PE-3** — PHYSICAL ACCESS CONTROL

- Issued by: National Institute of Standards and Technology
- Publication: NIST SP 800-53 Rev. 5 — Security and Privacy Controls for Information Systems and Organizations ([nist-sp-800-53-r5](./nist-sp-800-53-r5.md))
- Version: Rev. 5 (September 2020, includes updates as of 2020-12-10)
- Text as of: 2026-11-12
- Cited by held documents: 40 times (cjis-sp-6-1 ×31, irs-pub-1075-11-2021 ×6, 6-cfr-37 ×2, arc-ampe ×1)
- Reproduction basis: 17 U.S.C. § 105 — work of the U.S. government (NIST). Determined per document on 2026-11-12 against the publication itself, not assumed from its issuer: its Authority statement (PDF page 3) reads "This publication may be used by nongovernmental organizations on a voluntary basis and is not subject to copyright in the United States. Attribution would, however, be appreciated by NIST." Held here: the front matter and Chapter Three (the control catalog) only. Chapter Three names ISO/IEC standards solely as bibliographic references and reproduces none of their text. NOT mirrored: the References bibliography and Appendices A-C; Appendix A (glossary) adapts third-party definitions (ISO/IEC 15026, ISO 25237, ISO/IEC 29100, ISO 15288, IETF RFC 4949), which ADR-0002 treats as not reproducible by being incorporated, and whose reproducibility has not been determined.


_NON-AUTHORITATIVE copy of one control, cut from the SP 800-53 Rev. 5 snapshot this corpus holds. Whether and how this binds a given agency depends on the instrument that incorporates it — read it at the source URL before relying on it. This copy is the Rev. 5 text of record, which is not necessarily the text a citing document meant (a document citing Rev. 4 is not answered by it)._


## Full text

### PE-3 PHYSICAL ACCESS CONTROL
Control:
a. Enforce physical access authorizations at [Assignment: organization-defined entry and exit
points to the facility where the system resides] by:
1. Verifying individual access authorizations before granting access to the facility; and
2. Controlling ingress and egress to the facility using [Selection (one or more): [Assignment:
organization-defined physical access control systems or devices]; guards];
b. Maintain physical access audit logs for [Assignment: organization-defined entry or exit
points];
c. Control access to areas within the facility designated as publicly accessible by implementing
the following controls: [Assignment: organization-defined physical access controls];
d. Escort visitors and control visitor activity [Assignment: organization-defined circumstances
requiring visitor escorts and control of visitor activity];
e. Secure keys, combinations, and other physical access devices;
f. Inventory [Assignment: organization-defined physical access devices] every [Assignment:
organization-defined frequency]; and
g. Change combinations and keys [Assignment: organization-defined frequency] and/or when
keys are lost, combinations are compromised, or when individuals possessing the keys or
combinations are transferred or terminated.
Discussion:  Physical access control applies to employees and visitors. Individuals with permanent
physical access authorizations are not considered visitors. Physical access controls for publicly
accessible areas may include physical access control logs/records, guards, or physical access
devices and barriers to prevent movement from publicly accessible areas to non-public areas.
Organizations determine the types of guards needed, including professional security staff, system
users, or administrative staff. Physical access devices include keys, locks, combinations, biometric
readers, and card readers. Physical access control systems comply with applicable laws, executive
orders, directives, policies, regulations, standards, and guidelines. Organizations have flexibility in
the types of audit logs employed. Audit logs can be procedural, automated, or some combination
thereof. Physical access points can include facility access points, interior access points to systems
that require supplemental access controls, or both. Components of systems may be in areas
designated as publicly accessible with organizations controlling access to the components.
Related Controls:  AT-3, AU-2, AU-6, AU-9, AU-13, CP-10, IA-3, IA-8, MA-5, MP-2, MP-4, PE-2, PE-
4, PE-5, PE-8, PS-2, PS-3, PS-6, PS-7, RA-3, SC-28, SI-4, SR-3.
Control Enhancements:
(1) PHYSICAL ACCESS CONTROL | SYSTEM ACCESS
Enforce physical access authorizations to the system in addition to the physical access
controls for the facility at [Assignment: organization-defined physical spaces containing
one or more components of the system].
Discussion:  Control of physical access to the system provides additional physical security for
those areas within facilities where there is a concentration of system components.
Related Controls:  None.
(2) PHYSICAL ACCESS CONTROL | FACILITY AND SYSTEMS
CHAPTER THREE   PAGE 182
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
Perform security checks [Assignment: organization-defined frequency] at the physical
perimeter of the facility or system for exfiltration of information or removal of system
components.
Discussion:  Organizations determine the extent, frequency, and/or randomness of security
checks to adequately mitigate risk associated with exfiltration.
Related Controls:  AC-4, SC-7.
(3) PHYSICAL ACCESS CONTROL | CONTINUOUS GUARDS
Employ guards to control [Assignment: organization-defined physical access points] to the
facility where the system resides 24 hours per day, 7 days per week.
Discussion:  Employing guards at selected physical access points to the facility provides a
more rapid response capability for organizations. Guards also provide the opportunity for
human surveillance in areas of the facility not covered by video surveillance.
Related Controls:  CP-6, CP-7, PE-6.
(4) PHYSICAL ACCESS CONTROL | LOCKABLE CASINGS
Use lockable physical casings to protect [Assignment: organization-defined system
components] from unauthorized physical access.
Discussion:  The greatest risk from the use of portable devices—such as smart phones,
tablets, and notebook computers—is theft. Organizations can employ lockable, physical
casings to reduce or eliminate the risk of equipment theft. Such casings come in a variety of
sizes, from units that protect a single notebook computer to full cabinets that can protect
multiple servers, computers, and peripherals. Lockable physical casings can be used in
conjunction with cable locks or lockdown plates to prevent the theft of the locked casing
containing the computer equipment.
Related Controls:  None.
(5) PHYSICAL ACCESS CONTROL | TAMPER PROTECTION
Employ [Assignment: organization-defined anti-tamper technologies] to [Selection (one or
more): detect; prevent] physical tampering or alteration of [Assignment: organization-
defined hardware components] within the system.
Discussion:  Organizations can implement tamper detection and prevention at selected
hardware components or implement tamper detection at some components and tamper
prevention at other components. Detection and prevention activities can employ many
types of anti-tamper technologies, including tamper-detection seals and anti-tamper
coatings. Anti-tamper programs help to detect hardware alterations through counterfeiting
and other supply chain-related risks.
Related Controls:  SA-16, SR-9, SR-11.
(6) PHYSICAL ACCESS CONTROL | FACILITY PENETRATION TESTING
[Withdrawn: Incorporated into CA-8.]
(7) PHYSICAL ACCESS CONTROL | PHYSICAL BARRIERS
Limit access using physical barriers.
Discussion:  Physical barriers include bollards, concrete slabs, jersey walls, and hydraulic
active vehicle barriers.
Related Controls:  None.
(8) PHYSICAL ACCESS CONTROL | ACCESS CONTROL VESTIBULES
Employ access control vestibules at [Assignment: organization-defined locations within the
facility].
CHAPTER THREE   PAGE 183
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
Discussion:  An access control vestibule is part of a physical access control system that
typically provides a space between two sets of interlocking doors. Vestibules are designed to
prevent unauthorized individuals from following authorized individuals into facilities with
controlled access. This activity, also known as piggybacking or tailgating, results in
unauthorized access to the facility. Interlocking door controllers can be used to limit the
number of individuals who enter controlled access points and to provide containment areas
while authorization for physical access is verified. Interlocking door controllers can be fully
automated (i.e., controlling the opening and closing of the doors) or partially automated
(i.e., using security guards to control the number of individuals entering the containment
area).
Related Controls:  None.
References:  [FIPS 201-2], [SP 800-73-4], [SP 800-76-2], [SP 800-78-4], [SP 800-116].
