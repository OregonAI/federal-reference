---
schema_version: 1
corpus: federal-reference
jurisdiction: us
id: nist-sp-800-53-r5.ac-3
title: NIST SP 800-53 Rev. 5 AC-3 — ACCESS ENFORCEMENT
doc_type: federal_instrument
citation: NIST SP 800-53 Rev. 5 AC-3
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

**NIST SP 800-53 Rev. 5 AC-3** — ACCESS ENFORCEMENT

- Issued by: National Institute of Standards and Technology
- Publication: NIST SP 800-53 Rev. 5 — Security and Privacy Controls for Information Systems and Organizations ([nist-sp-800-53-r5](./nist-sp-800-53-r5.md))
- Version: Rev. 5 (September 2020, includes updates as of 2020-12-10)
- Text as of: 2026-11-12
- Cited by held documents: 67 times (cjis-sp-6-1 ×49, arc-ampe ×10, 6-cfr-37 ×5, irs-pub-1075-11-2021 ×3), 4 of them naming an enhancement of this control
- Reproduction basis: 17 U.S.C. § 105 — work of the U.S. government (NIST). Determined per document on 2026-11-12 against the publication itself, not assumed from its issuer: its Authority statement (PDF page 3) reads "This publication may be used by nongovernmental organizations on a voluntary basis and is not subject to copyright in the United States. Attribution would, however, be appreciated by NIST." Held here: the front matter and Chapter Three (the control catalog) only. Chapter Three names ISO/IEC standards solely as bibliographic references and reproduces none of their text. NOT mirrored: the References bibliography and Appendices A-C; Appendix A (glossary) adapts third-party definitions (ISO/IEC 15026, ISO 25237, ISO/IEC 29100, ISO 15288, IETF RFC 4949), which ADR-0002 treats as not reproducible by being incorporated, and whose reproducibility has not been determined.


_NON-AUTHORITATIVE copy of one control, cut from the SP 800-53 Rev. 5 snapshot this corpus holds. Whether and how this binds a given agency depends on the instrument that incorporates it — read it at the source URL before relying on it. This copy is the Rev. 5 text of record, which is not necessarily the text a citing document meant (a document citing Rev. 4 is not answered by it)._


## Full text

### AC-3 ACCESS ENFORCEMENT
Control:  Enforce approved authorizations for logical access to information and system resources
in accordance with applicable access control policies.
Discussion:  Access control policies control access between active entities or subjects (i.e., users
or processes acting on behalf of users) and passive entities or objects (i.e., devices, files, records,
domains) in organizational systems. In addition to enforcing authorized access at the system level
and recognizing that systems can host many applications and services in support of mission and
business functions, access enforcement mechanisms can also be employed at the application and
service level to provide increased information security and privacy. In contrast to logical access
controls that are implemented within the system, physical access controls are addressed by the
controls in the Physical and Environmental Protection (
PE) family.
Related Controls:  AC-2, AC-4, AC-5, AC-6, AC-16, AC-17, AC-18, AC-19, AC-20, AC-21, AC-22, AC-
24, AC-25, AT-2, AT-3, AU-9, CA-9, CM-5, CM-11, IA-2, IA-5, IA-6, IA-7, IA-11, MA-3, MA-4, MA-5,
MP-4, PM-2, PS-3, PT-2, PT-3, SA-17, SC-2, SC-3, SC-4, SC-12, SC-13, SC-28, SC-31, SC-34, SI-4, SI-8.
Control Enhancements:
(1) ACCESS ENFORCEMENT | RESTRICTED ACCESS TO PRIVILEGED FUNCTIONS
[Withdrawn: Incorporated into AC-6.]
(2) ACCESS ENFORCEMENT | DUAL AUTHORIZATION
Enforce dual authorization for [Assignment: organization-defined privileged commands
and/or other organization-defined actions].
Discussion:  Dual authorization, also known as two-person control, reduces risk related to
insider threats. Dual authorization mechanisms require the approval of two authorized
individuals to execute. To reduce the risk of collusion, organizations consider rotating dual
authorization duties. Organizations consider the risk associated with implementing dual
authorization mechanisms when immediate responses are necessary to ensure public and
environmental safety.
Related Controls:  CP-9, MP-6.
(3) ACCESS ENFORCEMENT | MANDATORY ACCESS CONTROL
CHAPTER THREE   PAGE 24
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
Enforce [Assignment: organization-defined mandatory access control policy] over the set
of covered subjects and objects specified in the policy, and where the policy:
(a) Is uniformly enforced across the covered subjects and objects within the system;
(b) Specifies that a subject that has been granted access to information is constrained
from doing any of the following;
(1) Passing the information to unauthorized subjects or objects;
(2) Granting its privileges to other subjects;
(3) Changing one or more security attributes (specified by the policy) on subjects,
objects, the system, or system components;
(4) Choosing the security attributes and attribute values (specified by the policy) to
be associated with newly created or modified objects; and
(5) Changing the rules governing access control; and
(c) Specifies that [Assignment: organization-defined subjects] may explicitly be granted
[Assignment: organization-defined privileges] such that they are not limited by any
defined subset (or all) of the above constraints.
Discussion:  Mandatory access control is a type of nondiscretionary access control.
Mandatory access control policies constrain what actions subjects can take with information
obtained from objects for which they have already been granted access. This prevents the
subjects from passing the information to unauthorized subjects and objects. Mandatory
access control policies constrain actions that subjects can take with respect to the
propagation of access control privileges; that is, a subject with a privilege cannot pass that
privilege to other subjects. The policy is uniformly enforced over all subjects and objects to
which the system has control. Otherwise, the access control policy can be circumvented. This
enforcement is provided by an implementation that meets the reference monitor concept as
described in AC-25. The policy is bounded by the system (i.e., once the information is passed
outside of the control of the system, additional means may be required to ensure that the
constraints on the information remain in effect).
The trusted subjects described above are granted privileges consistent with the concept of
least privilege (see AC-6). Trusted subjects are only given the minimum privileges necessary
for satisfying organizational mission/business needs relative to the above policy. The control
is most applicable when there is a mandate that establishes a policy regarding access to
controlled unclassified information or classified information and some users of the system
are not authorized access to all such information resident in the system. Mandatory access
control can operate in conjunction with discretionary access control as described in AC-3(4).
A subject constrained in its operation by mandatory access control policies can still operate
under the less rigorous constraints of AC-3(4), but mandatory access control policies take
precedence over the less rigorous constraints of AC-3(4). For example, while a mandatory
access control policy imposes a constraint that prevents a subject from passing information
to another subject operating at a different impact or classification level, AC-3(4) permits the
subject to pass the information to any other subject with the same impact or classification
level as the subject. Examples of mandatory access control policies include the Bell-LaPadula
policy to protect confidentiality of information and the Biba policy to protect the integrity of
information.
Related Controls:  SC-7.
(4) ACCESS ENFORCEMENT | DISCRETIONARY ACCESS CONTROL
Enforce [Assignment: organization-defined discretionary access control policy] over the set
of covered subjects and objects specified in the policy, and where the policy specifies that
a subject that has been granted access to information can do one or more of the following:
(a) Pass the information to any other subjects or objects;
CHAPTER THREE   PAGE 25
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
(b) Grant its privileges to other subjects;
(c) Change security attributes on subjects, objects, the system, or the system’s
components;
(d) Choose the security attributes to be associated with newly created or revised objects;
or
(e) Change the rules governing access control.
Discussion:  When discretionary access control policies are implemented, subjects are not
constrained with regard to what actions they can take with information for which they have
already been granted access. Thus, subjects that have been granted access to information
are not prevented from passing the information to other subjects or objects (i.e., subjects
have the discretion to pass). Discretionary access control can operate in conjunction with
mandatory access control as described in AC-3(3) and AC-3(15). A subject that is constrained
in its operation by mandatory access control policies can still operate under the less rigorous
constraints of discretionary access control. Therefore, while AC-3(3) imposes constraints that
prevent a subject from passing information to another subject operating at a different
impact or classification level, AC-3(4) permits the subject to pass the information to any
subject at the same impact or classification level. The policy is bounded by the system. Once
the information is passed outside of system control, additional means may be required to
ensure that the constraints remain in effect. While traditional definitions of discretionary
access control require identity-based access control, that limitation is not required for this
particular use of discretionary access control.
Related Controls:  None.
(5) ACCESS ENFORCEMENT | SECURITY-RELEVANT INFORMATION
Prevent access to [Assignment: organization-defined security-relevant information] except
during secure, non-operable system states.
Discussion:  Security-relevant information is information within systems that can potentially
impact the operation of security functions or the provision of security services in a manner
that could result in failure to enforce system security and privacy policies or maintain the
separation of code and data. Security-relevant information includes access control lists,
filtering rules for routers or firewalls, configuration parameters for security services, and
cryptographic key management information. Secure, non-operable system states include the
times in which systems are not performing mission or business-related processing, such as
when the system is offline for maintenance, boot-up, troubleshooting, or shut down.
Related Controls:  CM-6, SC-39.
(6) ACCESS ENFORCEMENT | PROTECTION OF USER AND SYSTEM INFORMATION
[Withdrawn: Incorporated into MP-4 and SC-28.]
(7) ACCESS ENFORCEMENT | ROLE-BASED ACCESS CONTROL
Enforce a role-based access control policy over defined subjects and objects and control
access based upon [Assignment: organization-defined roles and users authorized to
assume such roles].
Discussion:  Role-based access control (RBAC) is an access control policy that enforces access
to objects and system functions based on the defined role (i.e., job function) of the subject.
Organizations can create specific roles based on job functions and the authorizations (i.e.,
privileges) to perform needed operations on the systems associated with the organization-
defined roles. When users are assigned to specific roles, they inherit the authorizations or
privileges defined for those roles. RBAC simplifies privilege administration for organizations
because privileges are not assigned directly to every user (which can be a large number of
individuals) but are instead acquired through role assignments. RBAC can also increase
CHAPTER THREE   PAGE 26
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
privacy and security risk if individuals assigned to a role are given access to information
beyond what they need to support organizational missions or business functions. RBAC can
be implemented as a mandatory or discretionary form of access control. For organizations
implementing RBAC with mandatory access controls, the requirements in AC-3(3) define the
scope of the subjects and objects covered by the policy.
Related Controls:  None.
(8) ACCESS ENFORCEMENT | REVOCATION OF ACCESS AUTHORIZATIONS
Enforce the revocation of access authorizations resulting from changes to the security
attributes of subjects and objects based on [Assignment: organization-defined rules
governing the timing of revocations of access authorizations].
Discussion:  Revocation of access rules may differ based on the types of access revoked. For
example, if a subject (i.e., user or process acting on behalf of a user) is removed from a
group, access may not be revoked until the next time the object is opened or the next time
the subject attempts to access the object. Revocation based on changes to security labels
may take effect immediately. Organizations provide alternative approaches on how to make
revocations immediate if systems cannot provide such capability and immediate revocation
is necessary.
Related Controls:  None.
(9) ACCESS ENFORCEMENT | CONTROLLED RELEASE
Release information outside of the system only if:
(a) The receiving [Assignment: organization-defined system or system component]
provides [Assignment: organization-defined controls]; and
(b) [Assignment: organization-defined controls] are used to validate the appropriateness
of the information designated for release.
Discussion:  Organizations can only directly protect information when it resides within the
system. Additional controls may be needed to ensure that organizational information is
adequately protected once it is transmitted outside of the system. In situations where the
system is unable to determine the adequacy of the protections provided by external entities,
as a mitigation measure, organizations procedurally determine whether the external systems
are providing adequate controls. The means used to determine the adequacy of controls
provided by external systems include conducting periodic assessments (inspections/tests),
establishing agreements between the organization and its counterpart organizations, or
some other process. The means used by external entities to protect the information received
need not be the same as those used by the organization, but the means employed are
sufficient to provide consistent adjudication of the security and privacy policy to protect the
information and individuals’ privacy.
Controlled release of information requires systems to implement technical or procedural
means to validate the information prior to releasing it to external systems. For example, if
the system passes information to a system controlled by another organization, technical
means are employed to validate that the security and privacy attributes associated with the
exported information are appropriate for the receiving system. Alternatively, if the system
passes information to a printer in organization-controlled space, procedural means can be
employed to ensure that only authorized individuals gain access to the printer.
Related Controls:  CA-3, PT-7, PT-8, SA-9, SC-16.
(10) ACCESS ENFORCEMENT | AUDITED OVERRIDE OF ACCESS CONTROL MECHANISMS
Employ an audited override of automated access control mechanisms under [Assignment:
organization-defined conditions] by [Assignment: organization-defined roles].
CHAPTER THREE   PAGE 27
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
Discussion:  In certain situations, such as when there is a threat to human life or an event
that threatens the organization’s ability to carry out critical missions or business functions,
an override capability for access control mechanisms may be needed. Override conditions
are defined by organizations and used only in those limited circumstances. Audit events are
defined in AU-2. Audit records are generated in AU-12.
Related Controls:  AU-2, AU-6, AU-10, AU-12, AU-14.
(11) ACCESS ENFORCEMENT | RESTRICT ACCESS TO SPECIFIC INFORMATION TYPES
Restrict access to data repositories containing [Assignment: organization-defined
information types].
Discussion:  Restricting access to specific information is intended to provide flexibility
regarding access control of specific information types within a system. For example, role-
based access could be employed to allow access to only a specific type of personally
identifiable information within a database rather than allowing access to the database in its
entirety. Other examples include restricting access to cryptographic keys, authentication
information, and selected system information.
Related Controls:  CM-8, CM-12, CM-13, PM-5.
(12) ACCESS ENFORCEMENT | ASSERT AND ENFORCE APPLICATION ACCESS
(a) Require applications to assert, as part of the installation process, the access needed to
the following system applications and functions: [Assignment: organization-defined
system applications and functions];
(b) Provide an enforcement mechanism to prevent unauthorized access; and
(c) Approve access changes after initial installation of the application.
Discussion:  Asserting and enforcing application access is intended to address applications
that need to access existing system applications and functions, including user contacts,
global positioning systems, cameras, keyboards, microphones, networks, phones, or other
files.
Related Controls:  CM-7.
(13) ACCESS ENFORCEMENT | ATTRIBUTE-BASED ACCESS CONTROL
Enforce attribute-based access control policy over defined subjects and objects and control
access based upon [Assignment: organization-defined attributes to assume access
permissions].
Discussion:  Attribute-based access control is an access control policy that restricts system
access to authorized users based on specified organizational attributes (e.g., job function,
identity), action attributes (e.g., read, write, delete), environmental attributes (e.g., time of
day, location), and resource attributes (e.g., classification of a document). Organizations can
create rules based on attributes and the authorizations (i.e., privileges) to perform needed
operations on the systems associated with organization-defined attributes and rules. When
users are assigned to attributes defined in attribute-based access control policies or rules,
they can be provisioned to a system with the appropriate privileges or dynamically granted
access to a protected resource. Attribute-based access control can be implemented as either
a mandatory or discretionary form of access control. When implemented with mandatory
access controls, the requirements in
AC-3(3) define the scope of the subjects and objects
covered by the policy.
Related Controls:  None.
(14) ACCESS ENFORCEMENT | INDIVIDUAL ACCESS
CHAPTER THREE   PAGE 28
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
Provide [Assignment: organization-defined mechanisms] to enable individuals to have
access to the following elements of their personally identifiable information: [Assignment:
organization-defined elements].
Discussion:  Individual access affords individuals the ability to review personally identifiable
information about them held within organizational records, regardless of format. Access
helps individuals to develop an understanding about how their personally identifiable
information is being processed. It can also help individuals ensure that their data is accurate.
Access mechanisms can include request forms and application interfaces. For federal
agencies, [PRIVACT] processes can be located in systems of record notices and on agency
websites. Access to certain types of records may not be appropriate (e.g., for federal
agencies, law enforcement records within a system of records may be exempt from
disclosure under the [PRIVACT]) or may require certain levels of authentication assurance.
Organizational personnel consult with the senior agency official for privacy and legal counsel
to determine appropriate mechanisms and access rights or limitations.
Related Controls:  IA-8, PM-22, PM-20, PM-21, PT-6.
(15) ACCESS ENFORCEMENT | DISCRETIONARY AND MANDATORY ACCESS CONTROL
(a) Enforce [Assignment: organization-defined mandatory access control policy] over the
set of covered subjects and objects specified in the policy; and
(b) Enforce [Assignment: organization-defined discretionary access control policy] over
the set of covered subjects and objects specified in the policy.
Discussion:  Simultaneously implementing a mandatory access control policy and a
discretionary access control policy can provide additional protection against the
unauthorized execution of code by users or processes acting on behalf of users. This helps
prevent a single compromised user or process from compromising the entire system.
Related Controls:  SC-2, SC-3, AC-4.
References:  [PRIVACT], [OMB A-130], [SP 800-57-1], [SP 800-57-2], [SP 800-57-3], [SP 800-162],
[SP 800-178], [IR 7874].
