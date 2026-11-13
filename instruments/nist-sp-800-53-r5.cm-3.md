---
schema_version: 1
corpus: federal-reference
jurisdiction: us
id: nist-sp-800-53-r5.cm-3
title: NIST SP 800-53 Rev. 5 CM-3 — CONFIGURATION CHANGE CONTROL
doc_type: federal_instrument
citation: NIST SP 800-53 Rev. 5 CM-3
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

**NIST SP 800-53 Rev. 5 CM-3** — CONFIGURATION CHANGE CONTROL

- Issued by: National Institute of Standards and Technology
- Publication: NIST SP 800-53 Rev. 5 — Security and Privacy Controls for Information Systems and Organizations ([nist-sp-800-53-r5](./nist-sp-800-53-r5.md))
- Version: Rev. 5 (September 2020, includes updates as of 2020-12-10)
- Text as of: 2026-11-12
- Cited by held documents: 38 times (cjis-sp-6-1 ×24, arc-ampe ×8, 6-cfr-37 ×3, irs-pub-1075-11-2021 ×3), 1 of them naming an enhancement of this control
- Reproduction basis: 17 U.S.C. § 105 — work of the U.S. government (NIST). Determined per document on 2026-11-12 against the publication itself, not assumed from its issuer: its Authority statement (PDF page 3) reads "This publication may be used by nongovernmental organizations on a voluntary basis and is not subject to copyright in the United States. Attribution would, however, be appreciated by NIST." Held here: the front matter and Chapter Three (the control catalog) only. Chapter Three names ISO/IEC standards solely as bibliographic references and reproduces none of their text. NOT mirrored: the References bibliography and Appendices A-C; Appendix A (glossary) adapts third-party definitions (ISO/IEC 15026, ISO 25237, ISO/IEC 29100, ISO 15288, IETF RFC 4949), which ADR-0002 treats as not reproducible by being incorporated, and whose reproducibility has not been determined.


_NON-AUTHORITATIVE copy of one control, cut from the SP 800-53 Rev. 5 snapshot this corpus holds. Whether and how this binds a given agency depends on the instrument that incorporates it — read it at the source URL before relying on it. This copy is the Rev. 5 text of record, which is not necessarily the text a citing document meant (a document citing Rev. 4 is not answered by it)._


## Full text

### CM-3 CONFIGURATION CHANGE CONTROL
Control:
a. Determine and document the types of changes to the system that are configuration-
controlled;
b. Review proposed configuration-controlled changes to the system and approve or disapprove
such changes with explicit consideration for security and privacy impact analyses;
c. Document configuration change decisions associated with the system;
d. Implement approved configuration-controlled changes to the system;
CHAPTER THREE   PAGE 99
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
e. Retain records of configuration-controlled changes to the system for [Assignment:
organization-defined time period];
f. Monitor and review activities associated with configuration-controlled changes to the
system; and
g. Coordinate and provide oversight for configuration change control activities through
[Assignment: organization-defined configuration change control element] that convenes
[Selection (one or more): [Assignment: organization-defined frequency]; when [Assignment:
organization-defined configuration change conditions]].
Discussion:  Configuration change control for organizational systems involves the systematic
proposal, justification, implementation, testing, review, and disposition of system changes,
including system upgrades and modifications. Configuration change control includes changes to
baseline configurations, configuration items of systems, operational procedures, configuration
settings for system components, remediate vulnerabilities, and unscheduled or unauthorized
changes. Processes for managing configuration changes to systems include Configuration Control
Boards or Change Advisory Boards that review and approve proposed changes. For changes that
impact privacy risk, the senior agency official for privacy updates privacy impact assessments and
system of records notices. For new systems or major upgrades, organizations consider including
representatives from the development organizations on the Configuration Control Boards or
Change Advisory Boards. Auditing of changes includes activities before and after changes are
made to systems and the auditing activities required to implement such changes. See also SA-10.
Related Controls:  CA-7, CM-2, CM-4, CM-5, CM-6, CM-9, CM-11, IA-3, MA-2, PE-16, PT-6, RA-8,
SA-8, SA-10, SC-28, SC-34, SC-37, SI-2, SI-3, SI-4, SI-7, SI-10, SR-11.
Control Enhancements:
(1) CONFIGURATION CHANGE CONTROL | AUTOMATED DOCUMENTATION, NOTIFICATION, AND
PROHIBITION OF CHANGES
Use [Assignment: organization-defined automated mechanisms] to:
(a) Document proposed changes to the system;
(b) Notify [Assignment: organization-defined approval authorities] of proposed changes
to the system and request change approval;
(c) Highlight proposed changes to the system that have not been approved or
disapproved within [Assignment: organization-defined time period];
(d) Prohibit changes to the system until designated approvals are received;
(e) Document all changes to the system; and
(f) Notify [Assignment: organization-defined personnel] when approved changes to the
system are completed.
Discussion:  None.
Related Controls:  None.
(2) CONFIGURATION CHANGE CONTROL | TESTING, VALIDATION, AND DOCUMENTATION OF CHANGES
Test, validate, and document changes to the system before finalizing the implementation
of the changes.
Discussion:  Changes to systems include modifications to hardware, software, or firmware
components and configuration settings defined in CM-6. Organizations ensure that testing
does not interfere with system operations that support organizational mission and business
functions. Individuals or groups conducting tests understand security and privacy policies
and procedures, system security and privacy policies and procedures, and the health, safety,
and environmental risks associated with specific facilities or processes. Operational systems
CHAPTER THREE   PAGE 100
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
may need to be taken offline, or replicated to the extent feasible, before testing can be
conducted. If systems must be taken offline for testing, the tests are scheduled to occur
during planned system outages whenever possible. If the testing cannot be conducted on
operational systems, organizations employ compensating controls.
Related Controls:  None.
(3) CONFIGURATION CHANGE CONTROL | AUTOMATED CHANGE IMPLEMENTATION
Implement changes to the current system baseline and deploy the updated baseline across
the installed base using [Assignment: organization-defined automated mechanisms].
Discussion:  Automated tools can improve the accuracy, consistency, and availability of
configuration baseline information. Automation can also provide data aggregation and data
correlation capabilities, alerting mechanisms, and dashboards to support risk-based
decision-making within the organization.
Related Controls:  None.
(4) CONFIGURATION CHANGE CONTROL | SECURITY AND PRIVACY REPRESENTATIVES
Require [Assignment: organization-defined security and privacy representatives] to be
members of the [Assignment: organization-defined configuration change control element].
Discussion:  Information security and privacy representatives include system security
officers, senior agency information security officers, senior agency officials for privacy, or
system privacy officers. Representation by personnel with information security and privacy
expertise is important because changes to system configurations can have unintended side
effects, some of which may be security- or privacy-relevant. Detecting such changes early in
the process can help avoid unintended, negative consequences that could ultimately affect
the security and privacy posture of systems. The configuration change control element
referred to in the second organization-defined parameter reflects the change control
elements defined by organizations in CM-3g.
Related Controls:  None.
(5) CONFIGURATION CHANGE CONTROL | AUTOMATED SECURITY RESPONSE
Implement the following security responses automatically if baseline configurations are
changed in an unauthorized manner: [Assignment: organization-defined security
responses].
Discussion:  Automated security responses include halting selected system functions, halting
system processing, and issuing alerts or notifications to organizational personnel when there
is an unauthorized modification of a configuration item.
Related Controls:  None.
(6) CONFIGURATION CHANGE CONTROL | CRYPTOGRAPHY MANAGEMENT
Ensure that cryptographic mechanisms used to provide the following controls are under
configuration management: [Assignment: organization-defined controls].
Discussion:  The controls referenced in the control enhancement refer to security and
privacy controls from the control catalog. Regardless of the cryptographic mechanisms
employed, processes and procedures are in place to manage those mechanisms. For
example, if system components use certificates for identification and authentication, a
process is implemented to address the expiration of those certificates.
Related Controls:  SC-12.
(7) CONFIGURATION CHANGE CONTROL | REVIEW SYSTEM CHANGES
CHAPTER THREE   PAGE 101
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
Review changes to the system [Assignment: organization-defined frequency] or when
[Assignment: organization-defined circumstances] to determine whether unauthorized
changes have occurred.
Discussion:  Indications that warrant a review of changes to the system and the specific
circumstances justifying such reviews may be obtained from activities carried out by
organizations during the configuration change process or continuous monitoring process.
Related Controls:  AU-6, AU-7, CM-3.
(8) CONFIGURATION CHANGE CONTROL | PREVENT OR RESTRICT CONFIGURATION CHANGES
Prevent or restrict changes to the configuration of the system under the following
circumstances: [Assignment: organization-defined circumstances].
Discussion:  System configuration changes can adversely affect critical system security and
privacy functionality. Change restrictions can be enforced through automated mechanisms.
Related Controls:  None.
References:  [SP 800-124], [SP 800-128], [IR 8062].
