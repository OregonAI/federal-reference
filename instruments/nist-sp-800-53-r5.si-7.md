---
schema_version: 1
corpus: federal-reference
jurisdiction: us
id: nist-sp-800-53-r5.si-7
title: NIST SP 800-53 Rev. 5 SI-7 — SOFTWARE, FIRMWARE, AND INFORMATION INTEGRITY
doc_type: federal_instrument
citation: NIST SP 800-53 Rev. 5 SI-7
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

**NIST SP 800-53 Rev. 5 SI-7** — SOFTWARE, FIRMWARE, AND INFORMATION INTEGRITY

- Issued by: National Institute of Standards and Technology
- Publication: NIST SP 800-53 Rev. 5 — Security and Privacy Controls for Information Systems and Organizations ([nist-sp-800-53-r5](./nist-sp-800-53-r5.md))
- Version: Rev. 5 (September 2020, includes updates as of 2020-12-10)
- Text as of: 2026-11-12
- Cited by held documents: 32 times (cjis-sp-6-1 ×27, irs-pub-1075-11-2021 ×3, 6-cfr-37 ×1, arc-ampe ×1), 1 of them naming an enhancement of this control
- Reproduction basis: 17 U.S.C. § 105 — work of the U.S. government (NIST). Determined per document on 2026-11-12 against the publication itself, not assumed from its issuer: its Authority statement (PDF page 3) reads "This publication may be used by nongovernmental organizations on a voluntary basis and is not subject to copyright in the United States. Attribution would, however, be appreciated by NIST." Held here: the front matter and Chapter Three (the control catalog) only. Chapter Three names ISO/IEC standards solely as bibliographic references and reproduces none of their text. NOT mirrored: the References bibliography and Appendices A-C; Appendix A (glossary) adapts third-party definitions (ISO/IEC 15026, ISO 25237, ISO/IEC 29100, ISO 15288, IETF RFC 4949), which ADR-0002 treats as not reproducible by being incorporated, and whose reproducibility has not been determined.


_NON-AUTHORITATIVE copy of one control, cut from the SP 800-53 Rev. 5 snapshot this corpus holds. Whether and how this binds a given agency depends on the instrument that incorporates it — read it at the source URL before relying on it. This copy is the Rev. 5 text of record, which is not necessarily the text a citing document meant (a document citing Rev. 4 is not answered by it)._


> **Release 5.2.0 postdates this text.** NIST's listing of record ([https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final)) says that on 2025-08-27 it issued release 5.2.0 of SP 800-53, which revises an existing control or enhancement and updates the related controls for this control. The text below is the Rev. 5 PDF of record and does NOT include that change; read NIST's own list of the changes ([summary](https://csrc.nist.gov/files/projects/Risk-Management/800-53%20Comment%20Site/SP800-53-r5.2.0-changes.pdf)) before relying on this control's text.


## Full text

### SI-7 SOFTWARE, FIRMWARE, AND INFORMATION INTEGRITY
Control:
a. Employ integrity verification tools to detect unauthorized changes to the following software,
firmware, and information: [Assignment: organization-defined software, firmware, and
information]; and
b. Take the following actions when unauthorized changes to the software, firmware, and
information are detected: [Assignment: organization-defined actions].
Discussion:  Unauthorized changes to software, firmware, and information can occur due to
errors or malicious activity. Software includes operating systems (with key internal components,
such as kernels or drivers), middleware, and applications. Firmware interfaces include Unified
Extensible Firmware Interface (UEFI) and Basic Input/Output System (BIOS). Information includes
personally identifiable information and metadata that contains security and privacy attributes
associated with information. Integrity-checking mechanisms—including parity checks, cyclical
redundancy checks, cryptographic hashes, and associated tools—can automatically monitor the
integrity of systems and hosted applications.
Related Controls:  AC-4, CM-3, CM-7, CM-8, MA-3, MA-4, RA-5, SA-8, SA-9, SA-10, SC-8, SC-12,
SC-13, SC-28, SC-37, SI-3, SR-3, SR-4, SR-5, SR-6, SR-9, SR-10, SR-11.
Control Enhancements:
(1) SOFTWARE, FIRMWARE, AND INFORMATION INTEGRITY | INTEGRITY CHECKS
Perform an integrity check of [Assignment: organization-defined software, firmware, and
information] [Selection (one or more): at startup; at [Assignment: organization-defined
transitional states or security-relevant events]; [Assignment: organization-defined
frequency]].
Discussion:  Security-relevant events include the identification of new threats to which
organizational systems are susceptible and the installation of new hardware, software, or
firmware. Transitional states include system startup, restart, shutdown, and abort.
Related Controls:  None.
(2) SOFTWARE, FIRMWARE, AND INFORMATION INTEGRITY | AUTOMATED NOTIFICATIONS OF INTEGRITY
VIOLATIONS
Employ automated tools that provide notification to [Assignment: organization-defined
personnel or roles] upon discovering discrepancies during integrity verification.
CHAPTER THREE   PAGE 346
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
Discussion:  The employment of automated tools to report system and information integrity
violations and to notify organizational personnel in a timely matter is essential to effective
risk response. Personnel with an interest in system and information integrity violations
include mission and business owners, system owners, senior agency information security
official, senior agency official for privacy, system administrators, software developers,
systems integrators, information security officers, and privacy officers.
Related Controls:  None.
(3) SOFTWARE, FIRMWARE, AND INFORMATION INTEGRITY | CENTRALLY MANAGED INTEGRITY TOOLS
Employ centrally managed integrity verification tools.
Discussion:  Centrally managed integrity verification tools provides greater consistency in the
application of such tools and can facilitate more comprehensive coverage of integrity
verification actions.
Related Controls:  AU-3, SI-2, SI-8.
(4) SOFTWARE, FIRMWARE, AND INFORMATION INTEGRITY | TAMPER-EVIDENT PACKAGING
[Withdrawn: Incorporated into SR-9.]
(5) SOFTWARE, FIRMWARE, AND INFORMATION INTEGRITY | AUTOMATED RESPONSE TO INTEGRITY
VIOLATIONS
Automatically [Selection (one or more): shut the system down; restart the system;
implement [Assignment: organization-defined controls]] when integrity violations are
discovered.
Discussion:  Organizations may define different integrity-checking responses by type of
information, specific information, or a combination of both. Types of information include
firmware, software, and user data. Specific information includes boot firmware for certain
types of machines. The automatic implementation of controls within organizational systems
includes reversing the changes, halting the system, or triggering audit alerts when
unauthorized modifications to critical security files occur.
Related Controls:  None.
(6) SOFTWARE, FIRMWARE, AND INFORMATION INTEGRITY | CRYPTOGRAPHIC PROTECTION
Implement cryptographic mechanisms to detect unauthorized changes to software,
firmware, and information.
Discussion:  Cryptographic mechanisms used to protect integrity include digital signatures
and the computation and application of signed hashes using asymmetric cryptography,
protecting the confidentiality of the key used to generate the hash, and using the public key
to verify the hash information. Organizations that employ cryptographic mechanisms also
consider cryptographic key management solutions.
Related Controls:  SC-12, SC-13.
(7) SOFTWARE, FIRMWARE, AND INFORMATION INTEGRITY | INTEGRATION OF DETECTION AND
RESPONSE
Incorporate the detection of the following unauthorized changes into the organizational
incident response capability: [Assignment: organization-defined security-relevant changes
to the system].
Discussion:  Integrating detection and response helps to ensure that detected events are
tracked, monitored, corrected, and available for historical purposes. Maintaining historical
records is important for being able to identify and discern adversary actions over an
extended time period and for possible legal actions. Security-relevant changes include
CHAPTER THREE   PAGE 347
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
unauthorized changes to established configuration settings or the unauthorized elevation of
system privileges.
Related Controls:  AU-2, AU-6, IR-4, IR-5, SI-4.
(8) SOFTWARE, FIRMWARE, AND INFORMATION INTEGRITY | AUDITING CAPABILITY FOR SIGNIFICANT
EVENTS
Upon detection of a potential integrity violation, provide the capability to audit the event
and initiate the following actions: [Selection (one or more): generate an audit record; alert
current user; alert [Assignment: organization-defined personnel or roles]; [Assignment:
organization-defined other actions]].
Discussion:  Organizations select response actions based on types of software, specific
software, or information for which there are potential integrity violations.
Related Controls:  AU-2, AU-6, AU-12.
(9) SOFTWARE, FIRMWARE, AND INFORMATION INTEGRITY | VERIFY BOOT PROCESS
Verify the integrity of the boot process of the following system components: [Assignment:
organization-defined system components].
Discussion:  Ensuring the integrity of boot processes is critical to starting system components
in known, trustworthy states. Integrity verification mechanisms provide a level of assurance
that only trusted code is executed during boot processes.
Related Controls:  SI-6.
(10) SOFTWARE, FIRMWARE, AND INFORMATION INTEGRITY | PROTECTION OF BOOT FIRMWARE
Implement the following mechanisms to protect the integrity of boot firmware in
[Assignment: organization-defined system components]: [Assignment: organization-
defined mechanisms].
Discussion:  Unauthorized modifications to boot firmware may indicate a sophisticated,
targeted attack. These types of targeted attacks can result in a permanent denial of service
or a persistent malicious code presence. These situations can occur if the firmware is
corrupted or if the malicious code is embedded within the firmware. System components
can protect the integrity of boot firmware in organizational systems by verifying the integrity
and authenticity of all updates to the firmware prior to applying changes to the system
component and preventing unauthorized processes from modifying the boot firmware.
Related Controls:  SI-6.
(11) SOFTWARE, FIRMWARE, AND INFORMATION INTEGRITY | CONFINED ENVIRONMENTS WITH LIMITED
PRIVILEGES
[Withdrawn: Moved to CM-7(6).]
(12) SOFTWARE, FIRMWARE, AND INFORMATION INTEGRITY | INTEGRITY VERIFICATION
Require that the integrity of the following user-installed software be verified prior to
execution: [Assignment: organization-defined user-installed software].
Discussion:  Organizations verify the integrity of user-installed software prior to execution to
reduce the likelihood of executing malicious code or programs that contains errors from
unauthorized modifications. Organizations consider the practicality of approaches to
verifying software integrity, including the availability of trustworthy checksums from
software developers and vendors.
Related Controls:  CM-11.
(13) SOFTWARE, FIRMWARE, AND INFORMATION INTEGRITY | CODE EXECUTION IN PROTECTED
ENVIRONMENTS
CHAPTER THREE   PAGE 348
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
[Withdrawn: Moved to CM-7(7).]
(14) SOFTWARE, FIRMWARE, AND INFORMATION INTEGRITY | BINARY OR MACHINE EXECUTABLE CODE
[Withdrawn: Moved to CM-7(8).]
(15) SOFTWARE, FIRMWARE, AND INFORMATION INTEGRITY | CODE AUTHENTICATION
Implement cryptographic mechanisms to authenticate the following software or firmware
components prior to installation: [Assignment: organization-defined software or firmware
components].
Discussion:  Cryptographic authentication includes verifying that software or firmware
components have been digitally signed using certificates recognized and approved by
organizations. Code signing is an effective method to protect against malicious code.
Organizations that employ cryptographic mechanisms also consider cryptographic key
management solutions.
Related Controls:  CM-5, SC-12, SC-13.
(16) SOFTWARE, FIRMWARE, AND INFORMATION INTEGRITY | TIME LIMIT ON PROCESS EXECUTION
WITHOUT SUPERVISION
Prohibit processes from executing without supervision for more than [Assignment:
organization-defined time period].
Discussion:  Placing a time limit on process execution without supervision is intended to
apply to processes for which typical or normal execution periods can be determined and
situations in which organizations exceed such periods. Supervision includes timers on
operating systems, automated responses, and manual oversight and response when system
process anomalies occur.
Related Controls:  None.
(17) SOFTWARE, FIRMWARE, AND INFORMATION INTEGRITY | RUNTIME APPLICATION SELF-PROTECTION
Implement [Assignment: organization-defined controls] for application self-protection at
runtime.
Discussion:  Runtime application self-protection employs runtime instrumentation to detect
and block the exploitation of software vulnerabilities by taking advantage of information
from the software in execution. Runtime exploit prevention differs from traditional
perimeter-based protections such as guards and firewalls which can only detect and block
attacks by using network information without contextual awareness. Runtime application
self-protection technology can reduce the susceptibility of software to attacks by monitoring
its inputs and blocking those inputs that could allow attacks. It can also help protect the
runtime environment from unwanted changes and tampering. When a threat is detected,
runtime application self-protection technology can prevent exploitation and take other
actions (e.g., sending a warning message to the user, terminating the user's session,
terminating the application, or sending an alert to organizational personnel). Runtime
application self-protection solutions can be deployed in either a monitor or protection
mode.
Related Controls:  SI-16.
References:  [OMB A-130], [FIPS 140-3], [FIPS 180-4], [FIPS 186-4], [FIPS 202], [SP 800-70], [SP
800-147].
