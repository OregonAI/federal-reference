---
schema_version: 1
corpus: federal-reference
jurisdiction: us
id: nist-sp-800-53-r5.ia-4
title: NIST SP 800-53 Rev. 5 IA-4 — IDENTIFIER MANAGEMENT
doc_type: federal_instrument
citation: NIST SP 800-53 Rev. 5 IA-4
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

**NIST SP 800-53 Rev. 5 IA-4** — IDENTIFIER MANAGEMENT

- Issued by: National Institute of Standards and Technology
- Publication: NIST SP 800-53 Rev. 5 — Security and Privacy Controls for Information Systems and Organizations ([nist-sp-800-53-r5](./nist-sp-800-53-r5.md))
- Version: Rev. 5 (September 2020, includes updates as of 2020-12-10)
- Text as of: 2026-11-12
- Cited by held documents: 31 times (cjis-sp-6-1 ×22, arc-ampe ×4, irs-pub-1075-11-2021 ×3, 6-cfr-37 ×2)
- Reproduction basis: 17 U.S.C. § 105 — work of the U.S. government (NIST). Determined per document on 2026-11-12 against the publication itself, not assumed from its issuer: its Authority statement (PDF page 3) reads "This publication may be used by nongovernmental organizations on a voluntary basis and is not subject to copyright in the United States. Attribution would, however, be appreciated by NIST." Held here: the front matter and Chapter Three (the control catalog) only. Chapter Three names ISO/IEC standards solely as bibliographic references and reproduces none of their text. NOT mirrored: the References bibliography and Appendices A-C; Appendix A (glossary) adapts third-party definitions (ISO/IEC 15026, ISO 25237, ISO/IEC 29100, ISO 15288, IETF RFC 4949), which ADR-0002 treats as not reproducible by being incorporated, and whose reproducibility has not been determined.


_NON-AUTHORITATIVE copy of one control, cut from the SP 800-53 Rev. 5 snapshot this corpus holds. Whether and how this binds a given agency depends on the instrument that incorporates it — read it at the source URL before relying on it. This copy is the Rev. 5 text of record, which is not necessarily the text a citing document meant (a document citing Rev. 4 is not answered by it)._


## Full text

### IA-4 IDENTIFIER MANAGEMENT
Control:  Manage system identifiers by:
a. Receiving authorization from [Assignment: organization-defined personnel or roles] to assign
an individual, group, role, service, or device identifier;
b. Selecting an identifier that identifies an individual, group, role, service, or device;
c. Assigning the identifier to the intended individual, group, role, service, or device; and
d. Preventing reuse of identifiers for [Assignment: organization-defined time period].
Discussion:  Common device identifiers include Media Access Control (MAC) addresses, Internet
Protocol (IP) addresses, or device-unique token identifiers. The management of individual
identifiers is not applicable to shared system accounts. Typically, individual identifiers are the
usernames of the system accounts assigned to those individuals. In such instances, the account
management activities of AC-2 use account names provided by IA-4. Identifier management also
addresses individual identifiers not necessarily associated with system accounts. Preventing the
reuse of identifiers implies preventing the assignment of previously used individual, group, role,
service, or device identifiers to different individuals, groups, roles, services, or devices.
Related Controls:  AC-5, IA-2, IA-3, IA-5, IA-8, IA-9, IA-12, MA-4, PE-2, PE-3, PE-4, PL-4, PM-12, PS-
3, PS-4, PS-5, SC-37.
Control Enhancements:
(1) IDENTIFIER MANAGEMENT | PROHIBIT ACCOUNT IDENTIFIERS AS PUBLIC IDENTIFIERS
Prohibit the use of system account identifiers that are the same as public identifiers for
individual accounts.
Discussion:  Prohibiting account identifiers as public identifiers applies to any publicly
disclosed account identifier used for communication such as, electronic mail and instant
CHAPTER THREE   PAGE 137
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
messaging. Prohibiting the use of systems account identifiers that are the same as some
public identifier, such as the individual identifier section of an electronic mail address, makes
it more difficult for adversaries to guess user identifiers. Prohibiting account identifiers as
public identifiers without the implementation of other supporting controls only complicates
guessing of identifiers. Additional protections are required for authenticators and credentials
to protect the account.
Related Controls:  AT-2, PT-7.
(2) IDENTIFIER MANAGEMENT | SUPERVISOR AUTHORIZATION
[Withdrawn: Incorporated into IA-12(1).]
(3) IDENTIFIER MANAGEMENT | MULTIPLE FORMS OF CERTIFICATION
[Withdrawn: Incorporated into IA-12(2).]
(4) IDENTIFIER MANAGEMENT | IDENTIFY USER STATUS
Manage individual identifiers by uniquely identifying each individual as [Assignment:
organization-defined characteristic identifying individual status].
Discussion:  Characteristics that identify the status of individuals include contractors, foreign
nationals, and non-organizational users. Identifying the status of individuals by these
characteristics provides additional information about the people with whom organizational
personnel are communicating. For example, it might be useful for a government employee
to know that one of the individuals on an email message is a contractor.
Related Controls:  None.
(5) IDENTIFIER MANAGEMENT | DYNAMIC MANAGEMENT
Manage individual identifiers dynamically in accordance with [Assignment: organization-
defined dynamic identifier policy].
Discussion:  In contrast to conventional approaches to identification that presume static
accounts for preregistered users, many distributed systems establish identifiers at runtime
for entities that were previously unknown. When identifiers are established at runtime for
previously unknown entities, organizations can anticipate and provision for the dynamic
establishment of identifiers. Pre-established trust relationships and mechanisms with
appropriate authorities to validate credentials and related identifiers are essential.
Related Controls:  AC-16.
(6) IDENTIFIER MANAGEMENT | CROSS-ORGANIZATION MANAGEMENT
Coordinate with the following external organizations for cross-organization management
of identifiers: [Assignment: organization-defined external organizations].
Discussion:  Cross-organization identifier management provides the capability to identify
individuals, groups, roles, or devices when conducting cross-organization activities involving
the processing, storage, or transmission of information.
Related Controls:  AU-16, IA-2, IA-5.
(7) IDENTIFIER MANAGEMENT | IN-PERSON REGISTRATION
[Withdrawn: Incorporated into IA-12(4).]
(8) IDENTIFIER MANAGEMENT | PAIRWISE PSEUDONYMOUS IDENTIFIERS
Generate pairwise pseudonymous identifiers.
Discussion:  A pairwise pseudonymous identifier is an opaque unguessable subscriber
identifier generated by an identity provider for use at a specific individual relying party.
Generating distinct pairwise pseudonymous identifiers with no identifying information about
a subscriber discourages subscriber activity tracking and profiling beyond the operational
CHAPTER THREE   PAGE 138
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
requirements established by an organization. The pairwise pseudonymous identifiers are
unique to each relying party except in situations where relying parties can show a
demonstrable relationship justifying an operational need for correlation, or all parties
consent to being correlated in such a manner.
Related Controls:  IA-5.
(9) IDENTIFIER MANAGEMENT | ATTRIBUTE MAINTENANCE AND PROTECTION
Maintain the attributes for each uniquely identified individual, device, or service in
[Assignment: organization-defined protected central storage].
Discussion:  For each of the entities covered in IA-2, IA-3, IA-8, and IA-9
, it is important to
maintain the attributes for each authenticated entity on an ongoing basis in a central
(protected) store.
Related Controls:  None.
References:  [FIPS 201-2], [SP 800-63-3], [SP 800-73-4], [SP 800-76-2], [SP 800-78-4].
