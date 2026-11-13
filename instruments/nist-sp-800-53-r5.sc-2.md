---
schema_version: 1
corpus: federal-reference
jurisdiction: us
id: nist-sp-800-53-r5.sc-2
title: NIST SP 800-53 Rev. 5 SC-2 — SEPARATION OF SYSTEM AND USER FUNCTIONALITY
doc_type: federal_instrument
citation: NIST SP 800-53 Rev. 5 SC-2
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

**NIST SP 800-53 Rev. 5 SC-2** — SEPARATION OF SYSTEM AND USER FUNCTIONALITY

- Issued by: National Institute of Standards and Technology
- Publication: NIST SP 800-53 Rev. 5 — Security and Privacy Controls for Information Systems and Organizations ([nist-sp-800-53-r5](./nist-sp-800-53-r5.md))
- Version: Rev. 5 (September 2020, includes updates as of 2020-12-10)
- Text as of: 2026-11-12
- Cited by held documents: 13 times (cjis-sp-6-1 ×9, irs-pub-1075-11-2021 ×3, 6-cfr-37 ×1)
- Reproduction basis: 17 U.S.C. § 105 — work of the U.S. government (NIST). Determined per document on 2026-11-12 against the publication itself, not assumed from its issuer: its Authority statement (PDF page 3) reads "This publication may be used by nongovernmental organizations on a voluntary basis and is not subject to copyright in the United States. Attribution would, however, be appreciated by NIST." Held here: the front matter and Chapter Three (the control catalog) only. Chapter Three names ISO/IEC standards solely as bibliographic references and reproduces none of their text. NOT mirrored: the References bibliography and Appendices A-C; Appendix A (glossary) adapts third-party definitions (ISO/IEC 15026, ISO 25237, ISO/IEC 29100, ISO 15288, IETF RFC 4949), which ADR-0002 treats as not reproducible by being incorporated, and whose reproducibility has not been determined.


_NON-AUTHORITATIVE copy of one control, cut from the SP 800-53 Rev. 5 snapshot this corpus holds. Whether and how this binds a given agency depends on the instrument that incorporates it — read it at the source URL before relying on it. This copy is the Rev. 5 text of record, which is not necessarily the text a citing document meant (a document citing Rev. 4 is not answered by it)._


## Full text

### SC-2 SEPARATION OF SYSTEM AND USER FUNCTIONALITY
Control:  Separate user functionality, including user interface services, from system management
functionality.
Discussion:  System management functionality includes functions that are necessary to
administer databases, network components, workstations, or servers. These functions typically
require privileged user access. The separation of user functions from system management
functions is physical or logical. Organizations may separate system management functions from
user functions by using different computers, instances of operating systems, central processing
units, or network addresses; by employing virtualization techniques; or some combination of
these or other methods. Separation of system management functions from user functions
includes web administrative interfaces that employ separate authentication methods for users of
any other system resources. Separation of system and user functions may include isolating
administrative interfaces on different domains and with additional access controls. The
separation of system and user functionality can be achieved by applying the systems security
engineering design principles in SA-8, including SA-8(1), SA-8(3), SA-8(4), SA-8(10), SA-8(12), SA-
8(13), SA-8(14), and SA-8(18).
Related Controls:  AC-6, SA-4, SA-8, SC-3, SC-7, SC-22, SC-32, SC-39.
Control Enhancements:
(1) SEPARATION OF SYSTEM AND USER FUNCTIONALITY | INTERFACES FOR NON-PRIVILEGED USERS
Prevent the presentation of system management functionality at interfaces to non-
privileged users.
Discussion:  Preventing the presentation of system management functionality at interfaces
to non-privileged users ensures that system administration options, including administrator
privileges, are not available to the general user population. Restricting user access also
prohibits the use of the grey-out option commonly used to eliminate accessibility to such
information. One potential solution is to withhold system administration options until users
establish sessions with administrator privileges.
Related Controls:  AC-3.
(2) SEPARATION OF SYSTEM AND USER FUNCTIONALITY | DISASSOCIABILITY
Store state information from applications and software separately.
Discussion:  If a system is compromised, storing applications and software separately from
state information about users’ interactions with an application may better protect
individuals’ privacy.
Related Controls:  None.
References:  None.
