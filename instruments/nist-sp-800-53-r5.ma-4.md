---
schema_version: 1
corpus: federal-reference
jurisdiction: us
id: nist-sp-800-53-r5.ma-4
title: NIST SP 800-53 Rev. 5 MA-4 — NONLOCAL MAINTENANCE
doc_type: federal_instrument
citation: NIST SP 800-53 Rev. 5 MA-4
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

**NIST SP 800-53 Rev. 5 MA-4** — NONLOCAL MAINTENANCE

- Issued by: National Institute of Standards and Technology
- Publication: NIST SP 800-53 Rev. 5 — Security and Privacy Controls for Information Systems and Organizations ([nist-sp-800-53-r5](./nist-sp-800-53-r5.md))
- Version: Rev. 5 (September 2020, includes updates as of 2020-12-10)
- Text as of: 2026-11-12
- Cited by held documents: 38 times (cjis-sp-6-1 ×32, irs-pub-1075-11-2021 ×4, 6-cfr-37 ×1, arc-ampe ×1), 1 of them naming an enhancement of this control
- Reproduction basis: 17 U.S.C. § 105 — work of the U.S. government (NIST). Determined per document on 2026-11-12 against the publication itself, not assumed from its issuer: its Authority statement (PDF page 3) reads "This publication may be used by nongovernmental organizations on a voluntary basis and is not subject to copyright in the United States. Attribution would, however, be appreciated by NIST." Held here: the front matter and Chapter Three (the control catalog) only. Chapter Three names ISO/IEC standards solely as bibliographic references and reproduces none of their text. NOT mirrored: the References bibliography and Appendices A-C; Appendix A (glossary) adapts third-party definitions (ISO/IEC 15026, ISO 25237, ISO/IEC 29100, ISO 15288, IETF RFC 4949), which ADR-0002 treats as not reproducible by being incorporated, and whose reproducibility has not been determined.


_NON-AUTHORITATIVE copy of one control, cut from the SP 800-53 Rev. 5 snapshot this corpus holds. Whether and how this binds a given agency depends on the instrument that incorporates it — read it at the source URL before relying on it. This copy is the Rev. 5 text of record, which is not necessarily the text a citing document meant (a document citing Rev. 4 is not answered by it)._


## Full text

### MA-4 NONLOCAL MAINTENANCE
Control:
a. Approve and monitor nonlocal maintenance and diagnostic activities;
b. Allow the use of nonlocal maintenance and diagnostic tools only as consistent with
organizational policy and documented in the security plan for the system;
c. Employ strong authentication in the establishment of nonlocal maintenance and diagnostic
sessions;
d. Maintain records for nonlocal maintenance and diagnostic activities; and
e. Terminate session and network connections when nonlocal maintenance is completed.
Discussion:  Nonlocal maintenance and diagnostic activities are conducted by individuals who
communicate through either an external or internal network. Local maintenance and diagnostic
activities are carried out by individuals who are physically present at the system location and not
communicating across a network connection. Authentication techniques used to establish
nonlocal maintenance and diagnostic sessions reflect the network access requirements in IA-2.
Strong authentication requires authenticators that are resistant to replay attacks and employ
multi-factor authentication. Strong authenticators include PKI where certificates are stored on a
token protected by a password, passphrase, or biometric. Enforcing requirements in MA-4 is
accomplished, in part, by other controls. [SP 800-63B] provides additional guidance on strong
authentication and authenticators.
Related Controls:  AC-2, AC-3, AC-6, AC-17, AU-2, AU-3, IA-2, IA-4, IA-5, IA-8, MA-2, MA-5, PL-2,
SC-7, SC-10.
Control Enhancements:
(1) NONLOCAL MAINTENANCE | LOGGING AND REVIEW
(a) Log [Assignment: organization-defined audit events] for nonlocal maintenance and
diagnostic sessions; and
CHAPTER THREE   PAGE 166
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
(b) Review the audit records of the maintenance and diagnostic sessions to detect
anomalous behavior.
Discussion:  Audit logging for nonlocal maintenance is enforced by AU-2. Audit events are
defined in AU-2a.
Related Controls:  AU-6, AU-12.
(2) NONLOCAL MAINTENANCE | DOCUMENT NONLOCAL MAINTENANCE
[Withdrawn: Incorporated into MA-1 and MA-4.]
(3) NONLOCAL MAINTENANCE | COMPARABLE SECURITY AND SANITIZATION
(a) Require that nonlocal maintenance and diagnostic services be performed from a
system that implements a security capability comparable to the capability
implemented on the system being serviced; or
(b) Remove the component to be serviced from the system prior to nonlocal maintenance
or diagnostic services; sanitize the component (for organizational information); and
after the service is performed, inspect and sanitize the component (for potentially
malicious software) before reconnecting the component to the system.
Discussion:  Comparable security capability on systems, diagnostic tools, and equipment
providing maintenance services implies that the implemented controls on those systems,
tools, and equipment are at least as comprehensive as the controls on the system being
serviced.
Related Controls:  MP-6, SI-3, SI-7.
(4) NONLOCAL MAINTENANCE | AUTHENTICATION AND SEPARATION OF MAINTENANCE SESSIONS
Protect nonlocal maintenance sessions by:
(a) Employing [Assignment: organization-defined authenticators that are replay
resistant]; and
(b) Separating the maintenance sessions from other network sessions with the system by
either:
(1) Physically separated communications paths; or
(2) Logically separated communications paths.
Discussion:  Communications paths can be logically separated using encryption.
Related Controls:  None.
(5) NONLOCAL MAINTENANCE | APPROVALS AND NOTIFICATIONS
(a) Require the approval of each nonlocal maintenance session by [Assignment:
organization-defined personnel or roles]; and
(b) Notify the following personnel or roles of the date and time of planned nonlocal
maintenance: [Assignment: organization-defined personnel or roles].
Discussion:  Notification may be performed by maintenance personnel. Approval of nonlocal
maintenance is accomplished by personnel with sufficient information security and system
knowledge to determine the appropriateness of the proposed maintenance.
Related Controls:  None.
(6) NONLOCAL MAINTENANCE | CRYPTOGRAPHIC PROTECTION
Implement the following cryptographic mechanisms to protect the integrity and
confidentiality of nonlocal maintenance and diagnostic communications: [Assignment:
organization-defined cryptographic mechanisms].
Discussion:  Failure to protect nonlocal maintenance and diagnostic communications can
result in unauthorized individuals gaining access to organizational information. Unauthorized
CHAPTER THREE   PAGE 167
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
access during remote maintenance sessions can result in a variety of hostile actions,
including malicious code insertion, unauthorized changes to system parameters, and
exfiltration of organizational information. Such actions can result in the loss or degradation
of mission or business capabilities.
Related Controls:  SC-8, SC-12, SC-13.
(7) NONLOCAL MAINTENANCE | DISCONNECT VERIFICATION
Verify session and network connection termination after the completion of nonlocal
maintenance and diagnostic sessions.
Discussion:  Verifying the termination of a connection once maintenance is completed
ensures that connections established during nonlocal maintenance and diagnostic sessions
have been terminated and are no longer available for use.
Related Controls:  AC-12.
References:  [FIPS 140-3], [FIPS 197], [FIPS 201-2], [SP 800-63-3], [SP 800-88].
