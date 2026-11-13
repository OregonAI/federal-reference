---
schema_version: 1
corpus: federal-reference
jurisdiction: us
id: nist-sp-800-53-r5.ac-7
title: NIST SP 800-53 Rev. 5 AC-7 — UNSUCCESSFUL LOGON ATTEMPTS
doc_type: federal_instrument
citation: NIST SP 800-53 Rev. 5 AC-7
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

**NIST SP 800-53 Rev. 5 AC-7** — UNSUCCESSFUL LOGON ATTEMPTS

- Issued by: National Institute of Standards and Technology
- Publication: NIST SP 800-53 Rev. 5 — Security and Privacy Controls for Information Systems and Organizations ([nist-sp-800-53-r5](./nist-sp-800-53-r5.md))
- Version: Rev. 5 (September 2020, includes updates as of 2020-12-10)
- Text as of: 2026-11-12
- Cited by held documents: 15 times (cjis-sp-6-1 ×11, irs-pub-1075-11-2021 ×3, 6-cfr-37 ×1)
- Reproduction basis: 17 U.S.C. § 105 — work of the U.S. government (NIST). Determined per document on 2026-11-12 against the publication itself, not assumed from its issuer: its Authority statement (PDF page 3) reads "This publication may be used by nongovernmental organizations on a voluntary basis and is not subject to copyright in the United States. Attribution would, however, be appreciated by NIST." Held here: the front matter and Chapter Three (the control catalog) only. Chapter Three names ISO/IEC standards solely as bibliographic references and reproduces none of their text. NOT mirrored: the References bibliography and Appendices A-C; Appendix A (glossary) adapts third-party definitions (ISO/IEC 15026, ISO 25237, ISO/IEC 29100, ISO 15288, IETF RFC 4949), which ADR-0002 treats as not reproducible by being incorporated, and whose reproducibility has not been determined.


_NON-AUTHORITATIVE copy of one control, cut from the SP 800-53 Rev. 5 snapshot this corpus holds. Whether and how this binds a given agency depends on the instrument that incorporates it — read it at the source URL before relying on it. This copy is the Rev. 5 text of record, which is not necessarily the text a citing document meant (a document citing Rev. 4 is not answered by it)._


## Full text

### AC-7 UNSUCCESSFUL LOGON ATTEMPTS
Control:
a. Enforce a limit of [Assignment: organization-defined number] consecutive invalid logon
attempts by a user during a [Assignment: organization-defined time period]; and
b. Automatically [Selection (one or more): lock the account or node for an [Assignment:
organization-defined time period]; lock the account or node until released by an
administrator; delay next logon prompt per [Assignment: organization-defined delay
algorithm]; notify system administrator; take other [Assignment: organization-defined
action]] when the maximum number of unsuccessful attempts is exceeded.
Discussion:  The need to limit unsuccessful logon attempts and take subsequent action when the
maximum number of attempts is exceeded applies regardless of whether the logon occurs via a
local or network connection. Due to the potential for denial of service, automatic lockouts
initiated by systems are usually temporary and automatically release after a predetermined,
organization-defined time period. If a delay algorithm is selected, organizations may employ
different algorithms for different components of the system based on the capabilities of those
components. Responses to unsuccessful logon attempts may be implemented at the operating
system and the application levels. Organization-defined actions that may be taken when the
number of allowed consecutive invalid logon attempts is exceeded include prompting the user to
answer a secret question in addition to the username and password, invoking a lockdown mode
with limited user capabilities (instead of full lockout), allowing users to only logon from specified
Internet Protocol (IP) addresses, requiring a CAPTCHA to prevent automated attacks, or applying
user profiles such as location, time of day, IP address, device, or Media Access Control (MAC)
address. If automatic system lockout or execution of a delay algorithm is not implemented in
support of the availability objective, organizations consider a combination of other actions to
help prevent brute force attacks. In addition to the above, organizations can prompt users to
respond to a secret question before the number of allowed unsuccessful logon attempts is
exceeded. Automatically unlocking an account after a specified period of time is generally not
permitted. However, exceptions may be required based on operational mission or need.
Related Controls:  AC-2, AC-9, AU-2, AU-6, IA-5.
Control Enhancements:
(1) UNSUCCESSFUL LOGON ATTEMPTS | AUTOMATIC ACCOUNT LOCK
[Withdrawn: Incorporated into AC-7.]
(2) UNSUCCESSFUL LOGON ATTEMPTS | PURGE OR WIPE MOBILE DEVICE
Purge or wipe information from [Assignment: organization-defined mobile devices] based
on [Assignment: organization-defined purging or wiping requirements and techniques]
after [Assignment: organization-defined number] consecutive, unsuccessful device logon
attempts.
Discussion:  A mobile device is a computing device that has a small form factor such that it
can be carried by a single individual; is designed to operate without a physical connection;
possesses local, non-removable or removable data storage; and includes a self-contained
power source. Purging or wiping the device applies only to mobile devices for which the
organization-defined number of unsuccessful logons occurs. The logon is to the mobile
CHAPTER THREE   PAGE 40
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
device, not to any one account on the device. Successful logons to accounts on mobile
devices reset the unsuccessful logon count to zero. Purging or wiping may be unnecessary if
the information on the device is protected with sufficiently strong encryption mechanisms.
Related Controls:  AC-19, MP-5, MP-6.
(3) UNSUCCESSFUL LOGON ATTEMPTS | BIOMETRIC ATTEMPT LIMITING
Limit the number of unsuccessful biometric logon attempts to [Assignment: organization-
defined number].
Discussion:  Biometrics are probabilistic in nature. The ability to successfully authenticate
can be impacted by many factors, including matching performance and presentation attack
detection mechanisms. Organizations select the appropriate number of attempts for users
based on organizationally-defined factors.
Related Controls:  IA-3.
(4) UNSUCCESSFUL LOGON ATTEMPTS | USE OF ALTERNATE AUTHENTICATION FACTOR
(a) Allow the use of [Assignment: organization-defined authentication factors] that are
different from the primary authentication factors after the number of organization-
defined consecutive invalid logon attempts have been exceeded; and
(b) Enforce a limit of [Assignment: organization-defined number] consecutive invalid
logon attempts through use of the alternative factors by a user during a [Assignment:
organization-defined time period].
Discussion:  The use of alternate authentication factors supports the objective of availability
and allows a user who has inadvertently been locked out to use additional authentication
factors to bypass the lockout.
Related Controls:  IA-3.
References:   [SP 800-63-3], [SP 800-124].
