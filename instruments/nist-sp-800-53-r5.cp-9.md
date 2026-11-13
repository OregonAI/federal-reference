---
schema_version: 1
corpus: federal-reference
jurisdiction: us
id: nist-sp-800-53-r5.cp-9
title: NIST SP 800-53 Rev. 5 CP-9 — SYSTEM BACKUP
doc_type: federal_instrument
citation: NIST SP 800-53 Rev. 5 CP-9
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

**NIST SP 800-53 Rev. 5 CP-9** — SYSTEM BACKUP

- Issued by: National Institute of Standards and Technology
- Publication: NIST SP 800-53 Rev. 5 — Security and Privacy Controls for Information Systems and Organizations ([nist-sp-800-53-r5](./nist-sp-800-53-r5.md))
- Version: Rev. 5 (September 2020, includes updates as of 2020-12-10)
- Text as of: 2026-11-12
- Cited by held documents: 26 times (cjis-sp-6-1 ×20, irs-pub-1075-11-2021 ×3, 6-cfr-37 ×2, arc-ampe ×1)
- Reproduction basis: 17 U.S.C. § 105 — work of the U.S. government (NIST). Determined per document on 2026-11-12 against the publication itself, not assumed from its issuer: its Authority statement (PDF page 3) reads "This publication may be used by nongovernmental organizations on a voluntary basis and is not subject to copyright in the United States. Attribution would, however, be appreciated by NIST." Held here: the front matter and Chapter Three (the control catalog) only. Chapter Three names ISO/IEC standards solely as bibliographic references and reproduces none of their text. NOT mirrored: the References bibliography and Appendices A-C; Appendix A (glossary) adapts third-party definitions (ISO/IEC 15026, ISO 25237, ISO/IEC 29100, ISO 15288, IETF RFC 4949), which ADR-0002 treats as not reproducible by being incorporated, and whose reproducibility has not been determined.


_NON-AUTHORITATIVE copy of one control, cut from the SP 800-53 Rev. 5 snapshot this corpus holds. Whether and how this binds a given agency depends on the instrument that incorporates it — read it at the source URL before relying on it. This copy is the Rev. 5 text of record, which is not necessarily the text a citing document meant (a document citing Rev. 4 is not answered by it)._


## Full text

### CP-9 SYSTEM BACKUP
Control:
a. Conduct backups of user-level information contained in [Assignment: organization-defined
system components] [Assignment: organization-defined frequency consistent with recovery
time and recovery point objectives];
b. Conduct backups of system-level information contained in the system [Assignment:
organization-defined frequency consistent with recovery time and recovery point objectives];
CHAPTER THREE   PAGE 126
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
c. Conduct backups of system documentation, including security- and privacy-related
documentation [Assignment: organization-defined frequency consistent with recovery time
and recovery point objectives]; and
d. Protect the confidentiality, integrity, and availability of backup information.
Discussion:  System-level information includes system state information, operating system
software, middleware, application software, and licenses. User-level information includes
information other than system-level information. Mechanisms employed to protect the integrity
of system backups include digital signatures and cryptographic hashes. Protection of system
backup information while in transit is addressed by MP-5 and SC-8. System backups reflect the
requirements in contingency plans as well as other organizational requirements for backing up
information. Organizations may be subject to laws, executive orders, directives, regulations, or
policies with requirements regarding specific categories of information (e.g., personal health
information). Organizational personnel consult with the senior agency official for privacy and
legal counsel regarding such requirements.
Related Controls:  CP-2, CP-6, CP-10, MP-4, MP-5, SC-8, SC-12, SC-13, SI-4, SI-13.
Control Enhancements:
(1) SYSTEM BACKUP | TESTING FOR RELIABILITY AND INTEGRITY
Test backup information [Assignment: organization-defined frequency] to verify media
reliability and information integrity.
Discussion:  Organizations need assurance that backup information can be reliably retrieved.
Reliability pertains to the systems and system components where the backup information is
stored, the operations used to retrieve the information, and the integrity of the information
being retrieved. Independent and specialized tests can be used for each of the aspects of
reliability. For example, decrypting and transporting (or transmitting) a random sample of
backup files from the alternate storage or backup site and comparing the information to the
same information at the primary processing site can provide such assurance.
Related Controls:  CP-4.
(2) SYSTEM BACKUP | TEST RESTORATION USING SAMPLING
Use a sample of backup information in the restoration of selected system functions as part
of contingency plan testing.
Discussion:  Organizations need assurance that system functions can be restored correctly
and can support established organizational missions. To ensure that the selected system
functions are thoroughly exercised during contingency plan testing, a sample of backup
information is retrieved to determine whether the functions are operating as intended.
Organizations can determine the sample size for the functions and backup information
based on the level of assurance needed.
Related Controls:  CP-4.
(3) SYSTEM BACKUP | SEPARATE STORAGE FOR CRITICAL INFORMATION
Store backup copies of [Assignment: organization-defined critical system software and
other security-related information] in a separate facility or in a fire rated container that is
not collocated with the operational system.
Discussion:  Separate storage for critical information applies to all critical information
regardless of the type of backup storage media. Critical system software includes operating
systems, middleware, cryptographic key management systems, and intrusion detection
systems. Security-related information includes inventories of system hardware, software,
and firmware components. Alternate storage sites, including geographically distributed
architectures, serve as separate storage facilities for organizations. Organizations may
CHAPTER THREE   PAGE 127
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
provide separate storage by implementing automated backup processes at alternative
storage sites (e.g., data centers). The General Services Administration (GSA) establishes
standards and specifications for security and fire rated containers.
Related Controls:  CM-2, CM-6, CM-8.
(4) SYSTEM BACKUP | PROTECTION FROM UNAUTHORIZED MODIFICATION
[Withdrawn: Incorporated into CP-9.]
(5) SYSTEM BACKUP | TRANSFER TO ALTERNATE STORAGE SITE
Transfer system backup information to the alternate storage site [Assignment:
organization-defined time period and transfer rate consistent with the recovery time and
recovery point objectives].
Discussion:  System backup information can be transferred to alternate storage sites either
electronically or by the physical shipment of storage media.
Related Controls:  CP-7, MP-3, MP-4, MP-5.
(6) SYSTEM BACKUP | REDUNDANT SECONDARY SYSTEM
Conduct system backup by maintaining a redundant secondary system that is not
collocated with the primary system and that can be activated without loss of information
or disruption to operations.
Discussion:  The effect of system backup can be achieved by maintaining a redundant
secondary system that mirrors the primary system, including the replication of information.
If this type of redundancy is in place and there is sufficient geographic separation between
the two systems, the secondary system can also serve as the alternate processing site.
Related Controls:  CP-7.
(7) SYSTEM BACKUP | DUAL AUTHORIZATION FOR DELETION OR DESTRUCTION
Enforce dual authorization for the deletion or destruction of [Assignment: organization-
defined backup information].
Discussion:  Dual authorization ensures that deletion or destruction of backup information
cannot occur unless two qualified individuals carry out the task. Individuals deleting or
destroying backup information possess the skills or expertise to determine if the proposed
deletion or destruction of information reflects organizational policies and procedures. Dual
authorization may also be known as two-person control. To reduce the risk of collusion,
organizations consider rotating dual authorization duties to other individuals.
Related Controls:  AC-3, AC-5, MP-2.
(8) SYSTEM BACKUP | CRYPTOGRAPHIC PROTECTION
Implement cryptographic mechanisms to prevent unauthorized disclosure and
modification of [Assignment: organization-defined backup information].
Discussion:  The selection of cryptographic mechanisms is based on the need to protect the
confidentiality and integrity of backup information. The strength of mechanisms selected is
commensurate with the security category or classification of the information. Cryptographic
protection applies to system backup information in storage at both primary and alternate
locations. Organizations that implement cryptographic mechanisms to protect information
at rest also consider cryptographic key management solutions.
Related Controls:  SC-12, SC-13, SC-28.
References:  [FIPS 140-3], [FIPS 186-4], [SP 800-34], [SP 800-130], [SP 800-152].
CHAPTER THREE   PAGE 128
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
