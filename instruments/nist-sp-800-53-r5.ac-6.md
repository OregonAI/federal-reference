---
schema_version: 1
corpus: federal-reference
jurisdiction: us
id: nist-sp-800-53-r5.ac-6
title: NIST SP 800-53 Rev. 5 AC-6 — LEAST PRIVILEGE
doc_type: federal_instrument
citation: NIST SP 800-53 Rev. 5 AC-6
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

**NIST SP 800-53 Rev. 5 AC-6** — LEAST PRIVILEGE

- Issued by: National Institute of Standards and Technology
- Publication: NIST SP 800-53 Rev. 5 — Security and Privacy Controls for Information Systems and Organizations ([nist-sp-800-53-r5](./nist-sp-800-53-r5.md))
- Version: Rev. 5 (September 2020, includes updates as of 2020-12-10)
- Text as of: 2026-11-12
- Cited by held documents: 49 times (cjis-sp-6-1 ×35, 6-cfr-37 ×7, irs-pub-1075-11-2021 ×4, arc-ampe ×3), 2 of them naming an enhancement of this control
- Reproduction basis: 17 U.S.C. § 105 — work of the U.S. government (NIST). Determined per document on 2026-11-12 against the publication itself, not assumed from its issuer: its Authority statement (PDF page 3) reads "This publication may be used by nongovernmental organizations on a voluntary basis and is not subject to copyright in the United States. Attribution would, however, be appreciated by NIST." Held here: the front matter and Chapter Three (the control catalog) only. Chapter Three names ISO/IEC standards solely as bibliographic references and reproduces none of their text. NOT mirrored: the References bibliography and Appendices A-C; Appendix A (glossary) adapts third-party definitions (ISO/IEC 15026, ISO 25237, ISO/IEC 29100, ISO 15288, IETF RFC 4949), which ADR-0002 treats as not reproducible by being incorporated, and whose reproducibility has not been determined.


_NON-AUTHORITATIVE copy of one control, cut from the SP 800-53 Rev. 5 snapshot this corpus holds. Whether and how this binds a given agency depends on the instrument that incorporates it — read it at the source URL before relying on it. This copy is the Rev. 5 text of record, which is not necessarily the text a citing document meant (a document citing Rev. 4 is not answered by it)._


## Full text

### AC-6 LEAST PRIVILEGE
Control:  Employ the principle of least privilege, allowing only authorized accesses for users (or
processes acting on behalf of users) that are necessary to accomplish assigned organizational
tasks.
Discussion:  Organizations employ least privilege for specific duties and systems. The principle of
least privilege is also applied to system processes, ensuring that the processes have access to
systems and operate at privilege levels no higher than necessary to accomplish organizational
missions or business functions. Organizations consider the creation of additional processes, roles,
and accounts as necessary to achieve least privilege. Organizations apply least privilege to the
development, implementation, and operation of organizational systems.
Related Controls:  AC-2, AC-3, AC-5, AC-16, CM-5, CM-11, PL-2, PM-12, SA-8, SA-15, SA-17, SC-38.
Control Enhancements:
(1) LEAST PRIVILEGE | AUTHORIZE ACCESS TO SECURITY FUNCTIONS
Authorize access for [Assignment: organization-defined individuals or roles] to:
(a) [Assignment: organization-defined security functions (deployed in hardware, software,
and firmware)]; and
(b) [Assignment: organization-defined security-relevant information].
CHAPTER THREE   PAGE 37
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
Discussion:  Security functions include establishing system accounts, configuring access
authorizations (i.e., permissions, privileges), configuring settings for events to be audited,
and establishing intrusion detection parameters. Security-relevant information includes
filtering rules for routers or firewalls, configuration parameters for security services,
cryptographic key management information, and access control lists. Authorized personnel
include security administrators, system administrators, system security officers, system
programmers, and other privileged users.
Related Controls:  AC-17, AC-18, AC-19, AU-9, PE-2.
(2) LEAST PRIVILEGE | NON-PRIVILEGED ACCESS FOR NONSECURITY FUNCTIONS
Require that users of system accounts (or roles) with access to [Assignment: organization-
defined security functions or security-relevant information] use non-privileged accounts or
roles, when accessing nonsecurity functions.
Discussion:  Requiring the use of non-privileged accounts when accessing nonsecurity
functions limits exposure when operating from within privileged accounts or roles. The
inclusion of roles addresses situations where organizations implement access control
policies, such as role-based access control, and where a change of role provides the same
degree of assurance in the change of access authorizations for the user and the processes
acting on behalf of the user as would be provided by a change between a privileged and non-
privileged account.
Related Controls:  AC-17, AC-18, AC-19, PL-4.
(3) LEAST PRIVILEGE | NETWORK ACCESS TO PRIVILEGED COMMANDS
Authorize network access to [Assignment: organization-defined privileged commands]
only for [Assignment: organization-defined compelling operational needs] and document
the rationale for such access in the security plan for the system.
Discussion:  Network access is any access across a network connection in lieu of local access
(i.e., user being physically present at the device).
Related Controls:  AC-17, AC-18, AC-19.
(4) LEAST PRIVILEGE | SEPARATE PROCESSING DOMAINS
Provide separate processing domains to enable finer-grained allocation of user privileges.
Discussion:  Providing separate processing domains for finer-grained allocation of user
privileges includes using virtualization techniques to permit additional user privileges within
a virtual machine while restricting privileges to other virtual machines or to the underlying
physical machine, implementing separate physical domains, and employing hardware or
software domain separation mechanisms.
Related Controls:  AC-4, SC-2, SC-3, SC-30, SC-32, SC-39.
(5) LEAST PRIVILEGE | PRIVILEGED ACCOUNTS
Restrict privileged accounts on the system to [Assignment: organization-defined personnel
or roles].
Discussion:  Privileged accounts, including super user accounts, are typically described as
system administrator for various types of commercial off-the-shelf operating systems.
Restricting privileged accounts to specific personnel or roles prevents day-to-day users from
accessing privileged information or privileged functions. Organizations may differentiate in
the application of restricting privileged accounts between allowed privileges for local
accounts and for domain accounts provided that they retain the ability to control system
configurations for key parameters and as otherwise necessary to sufficiently mitigate risk.
Related Controls:  IA-2, MA-3, MA-4.
CHAPTER THREE   PAGE 38
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
(6) LEAST PRIVILEGE | PRIVILEGED ACCESS BY NON-ORGANIZATIONAL USERS
Prohibit privileged access to the system by non-organizational users.
Discussion:  An organizational user is an employee or an individual considered by the
organization to have the equivalent status of an employee. Organizational users include
contractors, guest researchers, or individuals detailed from other organizations. A non-
organizational user is a user who is not an organizational user. Policies and procedures for
granting equivalent status of employees to individuals include a need-to-know, citizenship,
and the relationship to the organization.
Related Controls:  AC-18, AC-19, IA-2, IA-8.
(7) LEAST PRIVILEGE | REVIEW OF USER PRIVILEGES
(a) Review [Assignment: organization-defined frequency] the privileges assigned to
[Assignment: organization-defined roles or classes of users] to validate the need for
such privileges; and
(b) Reassign or remove privileges, if necessary, to correctly reflect organizational mission
and business needs.
Discussion:  The need for certain assigned user privileges may change over time to reflect
changes in organizational mission and business functions, environments of operation,
technologies, or threats. A periodic review of assigned user privileges is necessary to
determine if the rationale for assigning such privileges remains valid. If the need cannot be
revalidated, organizations take appropriate corrective actions.
Related Controls:  CA-7.
(8) LEAST PRIVILEGE | PRIVILEGE LEVELS FOR CODE EXECUTION
Prevent the following software from executing at higher privilege levels than users
executing the software: [Assignment: organization-defined software].
Discussion:  In certain situations, software applications or programs need to execute with
elevated privileges to perform required functions. However, depending on the software
functionality and configuration, if the privileges required for execution are at a higher level
than the privileges assigned to organizational users invoking such applications or programs,
those users may indirectly be provided with greater privileges than assigned.
Related Controls:  None.
(9) LEAST PRIVILEGE | LOG USE OF PRIVILEGED FUNCTIONS
Log the execution of privileged functions.
Discussion:  The misuse of privileged functions, either intentionally or unintentionally by
authorized users or by unauthorized external entities that have compromised system
accounts, is a serious and ongoing concern and can have significant adverse impacts on
organizations. Logging and analyzing the use of privileged functions is one way to detect
such misuse and, in doing so, help mitigate the risk from insider threats and the advanced
persistent threat.
Related Controls:  AU-2, AU-3, AU-12.
(10) LEAST PRIVILEGE | PROHIBIT NON-PRIVILEGED USERS FROM EXECUTING PRIVILEGED FUNCTIONS
Prevent non-privileged users from executing privileged functions.
Discussion:  Privileged functions include disabling, circumventing, or altering implemented
security or privacy controls, establishing system accounts, performing system integrity
checks, and administering cryptographic key management activities. Non-privileged users
are individuals who do not possess appropriate authorizations. Privileged functions that
require protection from non-privileged users include circumventing intrusion detection and
CHAPTER THREE   PAGE 39
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
prevention mechanisms or malicious code protection mechanisms. Preventing non-
privileged users from executing privileged functions is enforced by AC-3.
Related Controls:  None.
References:  None.
