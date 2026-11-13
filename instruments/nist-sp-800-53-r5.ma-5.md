---
schema_version: 1
corpus: federal-reference
jurisdiction: us
id: nist-sp-800-53-r5.ma-5
title: NIST SP 800-53 Rev. 5 MA-5 — MAINTENANCE PERSONNEL
doc_type: federal_instrument
citation: NIST SP 800-53 Rev. 5 MA-5
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

**NIST SP 800-53 Rev. 5 MA-5** — MAINTENANCE PERSONNEL

- Issued by: National Institute of Standards and Technology
- Publication: NIST SP 800-53 Rev. 5 — Security and Privacy Controls for Information Systems and Organizations ([nist-sp-800-53-r5](./nist-sp-800-53-r5.md))
- Version: Rev. 5 (September 2020, includes updates as of 2020-12-10)
- Text as of: 2026-11-12
- Cited by held documents: 23 times (cjis-sp-6-1 ×16, irs-pub-1075-11-2021 ×4, 6-cfr-37 ×2, arc-ampe ×1)
- Reproduction basis: 17 U.S.C. § 105 — work of the U.S. government (NIST). Determined per document on 2026-11-12 against the publication itself, not assumed from its issuer: its Authority statement (PDF page 3) reads "This publication may be used by nongovernmental organizations on a voluntary basis and is not subject to copyright in the United States. Attribution would, however, be appreciated by NIST." Held here: the front matter and Chapter Three (the control catalog) only. Chapter Three names ISO/IEC standards solely as bibliographic references and reproduces none of their text. NOT mirrored: the References bibliography and Appendices A-C; Appendix A (glossary) adapts third-party definitions (ISO/IEC 15026, ISO 25237, ISO/IEC 29100, ISO 15288, IETF RFC 4949), which ADR-0002 treats as not reproducible by being incorporated, and whose reproducibility has not been determined.


_NON-AUTHORITATIVE copy of one control, cut from the SP 800-53 Rev. 5 snapshot this corpus holds. Whether and how this binds a given agency depends on the instrument that incorporates it — read it at the source URL before relying on it. This copy is the Rev. 5 text of record, which is not necessarily the text a citing document meant (a document citing Rev. 4 is not answered by it)._


## Full text

### MA-5 MAINTENANCE PERSONNEL
Control:
a. Establish a process for maintenance personnel authorization and maintain a list of
authorized maintenance organizations or personnel;
b. Verify that non-escorted personnel performing maintenance on the system possess the
required access authorizations; and
c. Designate organizational personnel with required access authorizations and technical
competence to supervise the maintenance activities of personnel who do not possess the
required access authorizations.
Discussion:  Maintenance personnel refers to individuals who perform hardware or software
maintenance on organizational systems, while PE-2 addresses physical access for individuals
whose maintenance duties place them within the physical protection perimeter of the systems.
Technical competence of supervising individuals relates to the maintenance performed on the
systems, while having required access authorizations refers to maintenance on and near the
systems. Individuals not previously identified as authorized maintenance personnel—such as
information technology manufacturers, vendors, systems integrators, and consultants—may
require privileged access to organizational systems, such as when they are required to conduct
maintenance activities with little or no notice. Based on organizational assessments of risk,
organizations may issue temporary credentials to these individuals. Temporary credentials may
be for one-time use or for very limited time periods.
Related Controls:  AC-2, AC-3, AC-5, AC-6, IA-2, IA-8, MA-4, MP-2, PE-2, PE-3, PS-7, RA-3.
Control Enhancements:
(1) MAINTENANCE PERSONNEL | INDIVIDUALS WITHOUT APPROPRIATE ACCESS
(a) Implement procedures for the use of maintenance personnel that lack appropriate
security clearances or are not U.S. citizens, that include the following requirements:
(1) Maintenance personnel who do not have needed access authorizations,
clearances, or formal access approvals are escorted and supervised during the
performance of maintenance and diagnostic activities on the system by approved
organizational personnel who are fully cleared, have appropriate access
authorizations, and are technically qualified; and
(2) Prior to initiating maintenance or diagnostic activities by personnel who do not
have needed access authorizations, clearances or formal access approvals, all
CHAPTER THREE   PAGE 168
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
volatile information storage components within the system are sanitized and all
nonvolatile storage media are removed or physically disconnected from the
system and secured; and
(b) Develop and implement [Assignment: organization-defined alternate controls] in the
event a system component cannot be sanitized, removed, or disconnected from the
system.
Discussion:  Procedures for individuals who lack appropriate security clearances or who are
not U.S. citizens are intended to deny visual and electronic access to classified or controlled
unclassified information contained on organizational systems. Procedures for the use of
maintenance personnel can be documented in security plans for the systems.
Related Controls:  MP-6, PL-2.
(2) MAINTENANCE PERSONNEL | SECURITY CLEARANCES FOR CLASSIFIED SYSTEMS
Verify that personnel performing maintenance and diagnostic activities on a system
processing, storing, or transmitting classified information possess security clearances and
formal access approvals for at least the highest classification level and for compartments
of information on the system.
Discussion:  Personnel who conduct maintenance on organizational systems may be exposed
to classified information during the course of their maintenance activities. To mitigate the
inherent risk of such exposure, organizations use maintenance personnel that are cleared
(i.e., possess security clearances) to the classification level of the information stored on the
system.
Related Controls:  PS-3.
(3) MAINTENANCE PERSONNEL | CITIZENSHIP REQUIREMENTS FOR CLASSIFIED SYSTEMS
Verify that personnel performing maintenance and diagnostic activities on a system
processing, storing, or transmitting classified information are U.S. citizens.
Discussion:  Personnel who conduct maintenance on organizational systems may be exposed
to classified information during the course of their maintenance activities. If access to
classified information on organizational systems is restricted to U.S. citizens, the same
restriction is applied to personnel performing maintenance on those systems.
Related Controls:  PS-3.
(4) MAINTENANCE PERSONNEL | FOREIGN NATIONALS
Ensure that:
(a) Foreign nationals with appropriate security clearances are used to conduct
maintenance and diagnostic activities on classified systems only when the systems are
jointly owned and operated by the United States and foreign allied governments, or
owned and operated solely by foreign allied governments; and
(b) Approvals, consents, and detailed operational conditions regarding the use of foreign
nationals to conduct maintenance and diagnostic activities on classified systems are
fully documented within Memoranda of Agreements.
Discussion:  Personnel who conduct maintenance and diagnostic activities on organizational
systems may be exposed to classified information. If non-U.S. citizens are permitted to
perform maintenance and diagnostics activities on classified systems, then additional vetting
is required to ensure agreements and restrictions are not being violated.
Related Controls:  PS-3.
(5) MAINTENANCE PERSONNEL | NON-SYSTEM MAINTENANCE
CHAPTER THREE   PAGE 169
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
Ensure that non-escorted personnel performing maintenance activities not directly
associated with the system but in the physical proximity of the system, have required
access authorizations.
Discussion:  Personnel who perform maintenance activities in other capacities not directly
related to the system include physical plant personnel and custodial personnel.
Related Controls:  None.
References:  None.
