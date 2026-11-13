---
schema_version: 1
corpus: federal-reference
jurisdiction: us
id: nist-sp-800-53-r5.cm-5
title: NIST SP 800-53 Rev. 5 CM-5 — ACCESS RESTRICTIONS FOR CHANGE
doc_type: federal_instrument
citation: NIST SP 800-53 Rev. 5 CM-5
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

**NIST SP 800-53 Rev. 5 CM-5** — ACCESS RESTRICTIONS FOR CHANGE

- Issued by: National Institute of Standards and Technology
- Publication: NIST SP 800-53 Rev. 5 — Security and Privacy Controls for Information Systems and Organizations ([nist-sp-800-53-r5](./nist-sp-800-53-r5.md))
- Version: Rev. 5 (September 2020, includes updates as of 2020-12-10)
- Text as of: 2026-11-12
- Cited by held documents: 27 times (cjis-sp-6-1 ×22, irs-pub-1075-11-2021 ×3, 6-cfr-37 ×1, arc-ampe ×1), 1 of them naming an enhancement of this control
- Reproduction basis: 17 U.S.C. § 105 — work of the U.S. government (NIST). Determined per document on 2026-11-12 against the publication itself, not assumed from its issuer: its Authority statement (PDF page 3) reads "This publication may be used by nongovernmental organizations on a voluntary basis and is not subject to copyright in the United States. Attribution would, however, be appreciated by NIST." Held here: the front matter and Chapter Three (the control catalog) only. Chapter Three names ISO/IEC standards solely as bibliographic references and reproduces none of their text. NOT mirrored: the References bibliography and Appendices A-C; Appendix A (glossary) adapts third-party definitions (ISO/IEC 15026, ISO 25237, ISO/IEC 29100, ISO 15288, IETF RFC 4949), which ADR-0002 treats as not reproducible by being incorporated, and whose reproducibility has not been determined.


_NON-AUTHORITATIVE copy of one control, cut from the SP 800-53 Rev. 5 snapshot this corpus holds. Whether and how this binds a given agency depends on the instrument that incorporates it — read it at the source URL before relying on it. This copy is the Rev. 5 text of record, which is not necessarily the text a citing document meant (a document citing Rev. 4 is not answered by it)._


## Full text

### CM-5 ACCESS RESTRICTIONS FOR CHANGE
Control:  Define, document, approve, and enforce physical and logical access restrictions
associated with changes to the system.
Discussion:  Changes to the hardware, software, or firmware components of systems or the
operational procedures related to the system can potentially have significant effects on the
security of the systems or individuals’ privacy. Therefore, organizations permit only qualified and
authorized individuals to access systems for purposes of initiating changes. Access restrictions
include physical and logical access controls (see AC-3 and PE-3), software libraries, workflow
automation, media libraries, abstract layers (i.e., changes implemented into external interfaces
rather than directly into systems), and change windows (i.e., changes occur only during specified
times).
Related Controls:  AC-3, AC-5, AC-6, CM-9, PE-3, SC-28, SC-34, SC-37, SI-2, SI-10.
Control Enhancements:
(1) ACCESS RESTRICTIONS FOR CHANGE | AUTOMATED ACCESS ENFORCEMENT AND AUDIT RECORDS
(a) Enforce access restrictions using [Assignment: organization-defined automated
mechanisms]; and
(b) Automatically generate audit records of the enforcement actions.
Discussion:  Organizations log system accesses associated with applying configuration
changes to ensure that configuration change control is implemented and to support after-
the-fact actions should organizations discover any unauthorized changes.
Related Controls:  AU-2, AU-6, AU-7, AU-12, CM-6, CM-11, SI-12.
(2) ACCESS RESTRICTIONS FOR CHANGE | REVIEW SYSTEM CHANGES
[Withdrawn: Incorporated into CM-3(7).]
(3) ACCESS RESTRICTIONS FOR CHANGE | SIGNED COMPONENTS
[Withdrawn: Moved to CM-14.]
(4) ACCESS RESTRICTIONS FOR CHANGE | DUAL AUTHORIZATION
Enforce dual authorization for implementing changes to [Assignment: organization-
defined system components and system-level information].
Discussion:  Organizations employ dual authorization to help ensure that any changes to
selected system components and information cannot occur unless two qualified individuals
approve and implement such changes. The two individuals possess the skills and expertise to
determine if the proposed changes are correct implementations of approved changes. The
individuals are also accountable for the changes. Dual authorization may also be known as
two-person control. To reduce the risk of collusion, organizations consider rotating dual
authorization duties to other individuals. System-level information includes operational
procedures.
Related Controls:  AC-2, AC-5, CM-3.
CHAPTER THREE   PAGE 103
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
(5) ACCESS RESTRICTIONS FOR CHANGE | PRIVILEGE LIMITATION FOR PRODUCTION AND OPERATION
(a) Limit privileges to change system components and system-related information within
a production or operational environment; and
(b) Review and reevaluate privileges [Assignment: organization-defined frequency].
Discussion:  In many organizations, systems support multiple mission and business functions.
Limiting privileges to change system components with respect to operational systems is
necessary because changes to a system component may have far-reaching effects on mission
and business processes supported by the system. The relationships between systems and
mission/business processes are, in some cases, unknown to developers. System-related
information includes operational procedures.
Related Controls:  AC-2.
(6) ACCESS RESTRICTIONS FOR CHANGE | LIMIT LIBRARY PRIVILEGES
Limit privileges to change software resident within software libraries.
Discussion:  Software libraries include privileged programs.
Related Controls:  AC-2.
(7) ACCESS RESTRICTIONS FOR CHANGE | AUTOMATIC IMPLEMENTATION OF SECURITY SAFEGUARDS
[Withdrawn: Incorporated into SI-7.]
References:  [FIPS 140-3];  [FIPS 186-4].
