---
schema_version: 1
corpus: federal-reference
jurisdiction: us
id: nist-sp-800-53-r5.au-9
title: NIST SP 800-53 Rev. 5 AU-9 — PROTECTION OF AUDIT INFORMATION
doc_type: federal_instrument
citation: NIST SP 800-53 Rev. 5 AU-9
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

**NIST SP 800-53 Rev. 5 AU-9** — PROTECTION OF AUDIT INFORMATION

- Issued by: National Institute of Standards and Technology
- Publication: NIST SP 800-53 Rev. 5 — Security and Privacy Controls for Information Systems and Organizations ([nist-sp-800-53-r5](./nist-sp-800-53-r5.md))
- Version: Rev. 5 (September 2020, includes updates as of 2020-12-10)
- Text as of: 2026-11-12
- Cited by held documents: 21 times (cjis-sp-6-1 ×17, irs-pub-1075-11-2021 ×3, 6-cfr-37 ×1)
- Reproduction basis: 17 U.S.C. § 105 — work of the U.S. government (NIST). Determined per document on 2026-11-12 against the publication itself, not assumed from its issuer: its Authority statement (PDF page 3) reads "This publication may be used by nongovernmental organizations on a voluntary basis and is not subject to copyright in the United States. Attribution would, however, be appreciated by NIST." Held here: the front matter and Chapter Three (the control catalog) only. Chapter Three names ISO/IEC standards solely as bibliographic references and reproduces none of their text. NOT mirrored: the References bibliography and Appendices A-C; Appendix A (glossary) adapts third-party definitions (ISO/IEC 15026, ISO 25237, ISO/IEC 29100, ISO 15288, IETF RFC 4949), which ADR-0002 treats as not reproducible by being incorporated, and whose reproducibility has not been determined.


_NON-AUTHORITATIVE copy of one control, cut from the SP 800-53 Rev. 5 snapshot this corpus holds. Whether and how this binds a given agency depends on the instrument that incorporates it — read it at the source URL before relying on it. This copy is the Rev. 5 text of record, which is not necessarily the text a citing document meant (a document citing Rev. 4 is not answered by it)._


## Full text

### AU-9 PROTECTION OF AUDIT INFORMATION
Control:
a. Protect audit information and audit logging tools from unauthorized access, modification,
and deletion; and
b. Alert [Assignment: organization-defined personnel or roles] upon detection of unauthorized
access, modification, or deletion of audit information.
Discussion:  Audit information includes all information needed to successfully audit system
activity, such as audit records, audit log settings, audit reports, and personally identifiable
information. Audit logging tools are those programs and devices used to conduct system audit
and logging activities. Protection of audit information focuses on technical protection and limits
the ability to access and execute audit logging tools to authorized individuals. Physical protection
of audit information is addressed by both media protection controls and physical and
environmental protection controls.
Related Controls:  AC-3, AC-6, AU-6, AU-11, AU-14, AU-15, MP-2, MP-4, PE-2, PE-3, PE-6, SA-8,
SC-8, SI-4.
Control Enhancements:
(1) PROTECTION OF AUDIT INFORMATION | HARDWARE WRITE-ONCE MEDIA
Write audit trails to hardware-enforced, write-once media.
Discussion:  Writing audit trails to hardware-enforced, write-once media applies to the initial
generation of audit trails (i.e., the collection of audit records that represents the information
to be used for detection, analysis, and reporting purposes) and to the backup of those audit
trails. Writing audit trails to hardware-enforced, write-once media does not apply to the
initial generation of audit records prior to being written to an audit trail. Write-once, read-
many (WORM) media includes Compact Disc-Recordable (CD-R), Blu-Ray Disc Recordable
(BD-R), and Digital Versatile Disc-Recordable (DVD-R). In contrast, the use of switchable
write-protection media, such as tape cartridges, Universal Serial Bus (USB) drives, Compact
Disc Re-Writeable (CD-RW), and Digital Versatile Disc-Read Write (DVD-RW) results in write-
protected but not write-once media.
Related Controls:  AU-4, AU-5.
(2) PROTECTION OF AUDIT INFORMATION | STORE ON SEPARATE PHYSICAL SYSTEMS OR COMPONENTS
Store audit records [Assignment: organization-defined frequency] in a repository that is
part of a physically different system or system component than the system or component
being audited.
Discussion:  Storing audit records in a repository separate from the audited system or system
component helps to ensure that a compromise of the system being audited does not also
result in a compromise of the audit records. Storing audit records on separate physical
systems or components also preserves the confidentiality and integrity of audit records and
facilitates the management of audit records as an organization-wide activity. Storing audit
records on separate systems or components applies to initial generation as well as backup or
long-term storage of audit records.
Related Controls:  AU-4, AU-5.
(3) PROTECTION OF AUDIT INFORMATION | CRYPTOGRAPHIC PROTECTION
CHAPTER THREE   PAGE 75
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
Implement cryptographic mechanisms to protect the integrity of audit information and
audit tools.
Discussion:  Cryptographic mechanisms used for protecting the integrity of audit information
include signed hash functions using asymmetric cryptography. This enables the distribution
of the public key to verify the hash information while maintaining the confidentiality of the
secret key used to generate the hash.
Related Controls:  AU-10, SC-12, SC-13.
(4) PROTECTION OF AUDIT INFORMATION | ACCESS BY SUBSET OF PRIVILEGED USERS
Authorize access to management of audit logging functionality to only [Assignment:
organization-defined subset of privileged users or roles].
Discussion:  Individuals or roles with privileged access to a system and who are also the
subject of an audit by that system may affect the reliability of the audit information by
inhibiting audit activities or modifying audit records. Requiring privileged access to be
further defined between audit-related privileges and other privileges limits the number of
users or roles with audit-related privileges.
Related Controls:  AC-5.
(5) PROTECTION OF AUDIT INFORMATION | DUAL AUTHORIZATION
Enforce dual authorization for [Selection (one or more): movement; deletion] of
[Assignment: organization-defined audit information].
Discussion:  Organizations may choose different selection options for different types of audit
information. Dual authorization mechanisms (also known as two-person control) require the
approval of two authorized individuals to execute audit functions. To reduce the risk of
collusion, organizations consider rotating dual authorization duties to other individuals.
Organizations do not require dual authorization mechanisms when immediate responses are
necessary to ensure public and environmental safety.
Related Controls:  AC-3.
(6) PROTECTION OF AUDIT INFORMATION | READ-ONLY ACCESS
Authorize read-only access to audit information to [Assignment: organization-defined
subset of privileged users or roles].
Discussion:  Restricting privileged user or role authorizations to read-only helps to limit the
potential damage to organizations that could be initiated by such users or roles, such as
deleting audit records to cover up malicious activity.
Related Controls:  None.
(7) PROTECTION OF AUDIT INFORMATION | STORE ON COMPONENT WITH DIFFERENT OPERATING
SYSTEM
Store audit information on a component running a different operating system than the
system or component being audited.
Discussion:  Storing auditing information on a system component running a different
operating system reduces the risk of a vulnerability specific to the system, resulting in a
compromise of the audit records.
Related controls:  AU-4, AU-5, AU-11, SC-29.
References:  [FIPS 140-3], [FIPS 180-4], [FIPS 202].
CHAPTER THREE   PAGE 76
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
