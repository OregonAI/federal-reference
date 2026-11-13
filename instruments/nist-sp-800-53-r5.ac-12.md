---
schema_version: 1
corpus: federal-reference
jurisdiction: us
id: nist-sp-800-53-r5.ac-12
title: NIST SP 800-53 Rev. 5 AC-12 — SESSION TERMINATION
doc_type: federal_instrument
citation: NIST SP 800-53 Rev. 5 AC-12
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

**NIST SP 800-53 Rev. 5 AC-12** — SESSION TERMINATION

- Issued by: National Institute of Standards and Technology
- Publication: NIST SP 800-53 Rev. 5 — Security and Privacy Controls for Information Systems and Organizations ([nist-sp-800-53-r5](./nist-sp-800-53-r5.md))
- Version: Rev. 5 (September 2020, includes updates as of 2020-12-10)
- Text as of: 2026-11-12
- Cited by held documents: 10 times (cjis-sp-6-1 ×4, irs-pub-1075-11-2021 ×3, 6-cfr-37 ×2, arc-ampe ×1)
- Reproduction basis: 17 U.S.C. § 105 — work of the U.S. government (NIST). Determined per document on 2026-11-12 against the publication itself, not assumed from its issuer: its Authority statement (PDF page 3) reads "This publication may be used by nongovernmental organizations on a voluntary basis and is not subject to copyright in the United States. Attribution would, however, be appreciated by NIST." Held here: the front matter and Chapter Three (the control catalog) only. Chapter Three names ISO/IEC standards solely as bibliographic references and reproduces none of their text. NOT mirrored: the References bibliography and Appendices A-C; Appendix A (glossary) adapts third-party definitions (ISO/IEC 15026, ISO 25237, ISO/IEC 29100, ISO 15288, IETF RFC 4949), which ADR-0002 treats as not reproducible by being incorporated, and whose reproducibility has not been determined.


_NON-AUTHORITATIVE copy of one control, cut from the SP 800-53 Rev. 5 snapshot this corpus holds. Whether and how this binds a given agency depends on the instrument that incorporates it — read it at the source URL before relying on it. This copy is the Rev. 5 text of record, which is not necessarily the text a citing document meant (a document citing Rev. 4 is not answered by it)._


## Full text

### AC-12 SESSION TERMINATION
Control:  Automatically terminate a user session after [Assignment: organization-defined
conditions or trigger events requiring session disconnect].
Discussion:  Session termination addresses the termination of user-initiated logical sessions (in
contrast to SC-10, which addresses the termination of network connections associated with
communications sessions (i.e., network disconnect)). A logical session (for local, network, and
remote access) is initiated whenever a user (or process acting on behalf of a user) accesses an
organizational system. Such user sessions can be terminated without terminating network
sessions. Session termination ends all processes associated with a user’s logical session except
for those processes that are specifically created by the user (i.e., session owner) to continue after
the session is terminated. Conditions or trigger events that require automatic termination of the
session include organization-defined periods of user inactivity, targeted responses to certain
types of incidents, or time-of-day restrictions on system use.
Related Controls:  MA-4, SC-10, SC-23.
Control Enhancements:
(1) SESSION TERMINATION | USER-INITIATED LOGOUTS
Provide a logout capability for user-initiated communications sessions whenever
authentication is used to gain access to [Assignment: organization-defined information
resources].
Discussion:  Information resources to which users gain access via authentication include local
workstations, databases, and password-protected websites or web-based services.
Related Controls:  None.
(2) SESSION TERMINATION | TERMINATION MESSAGE
Display an explicit logout message to users indicating the termination of authenticated
communications sessions.
Discussion:  Logout messages for web access can be displayed after authenticated sessions
have been terminated. However, for certain types of sessions, including file transfer protocol
(FTP) sessions, systems typically send logout messages as final messages prior to terminating
sessions.
Related Controls:  None.
(3) SESSION TERMINATION | TIMEOUT WARNING MESSAGE
Display an explicit message to users indicating that the session will end in [Assignment:
organization-defined time until end of session].
Discussion:  To increase usability, notify users of pending session termination and prompt
users to continue the session. The pending session termination time period is based on the
parameters defined in the AC-12 base control.
Related Controls:  None.
References:  None.
CHAPTER THREE   PAGE 44
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
