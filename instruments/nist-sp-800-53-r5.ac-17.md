---
schema_version: 1
corpus: federal-reference
jurisdiction: us
id: nist-sp-800-53-r5.ac-17
title: NIST SP 800-53 Rev. 5 AC-17 — REMOTE ACCESS
doc_type: federal_instrument
citation: NIST SP 800-53 Rev. 5 AC-17
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

**NIST SP 800-53 Rev. 5 AC-17** — REMOTE ACCESS

- Issued by: National Institute of Standards and Technology
- Publication: NIST SP 800-53 Rev. 5 — Security and Privacy Controls for Information Systems and Organizations ([nist-sp-800-53-r5](./nist-sp-800-53-r5.md))
- Version: Rev. 5 (September 2020, includes updates as of 2020-12-10)
- Text as of: 2026-11-12
- Cited by held documents: 53 times (cjis-sp-6-1 ×43, irs-pub-1075-11-2021 ×5, arc-ampe ×3, 6-cfr-37 ×2), 1 of them naming an enhancement of this control
- Reproduction basis: 17 U.S.C. § 105 — work of the U.S. government (NIST). Determined per document on 2026-11-12 against the publication itself, not assumed from its issuer: its Authority statement (PDF page 3) reads "This publication may be used by nongovernmental organizations on a voluntary basis and is not subject to copyright in the United States. Attribution would, however, be appreciated by NIST." Held here: the front matter and Chapter Three (the control catalog) only. Chapter Three names ISO/IEC standards solely as bibliographic references and reproduces none of their text. NOT mirrored: the References bibliography and Appendices A-C; Appendix A (glossary) adapts third-party definitions (ISO/IEC 15026, ISO 25237, ISO/IEC 29100, ISO 15288, IETF RFC 4949), which ADR-0002 treats as not reproducible by being incorporated, and whose reproducibility has not been determined.


_NON-AUTHORITATIVE copy of one control, cut from the SP 800-53 Rev. 5 snapshot this corpus holds. Whether and how this binds a given agency depends on the instrument that incorporates it — read it at the source URL before relying on it. This copy is the Rev. 5 text of record, which is not necessarily the text a citing document meant (a document citing Rev. 4 is not answered by it)._


## Full text

### AC-17 REMOTE ACCESS
Control:
a. Establish and document usage restrictions, configuration/connection requirements, and
implementation guidance for each type of remote access allowed; and
b. Authorize each type of remote access to the system prior to allowing such connections.
Discussion:  Remote access is access to organizational systems (or processes acting on behalf of
users) that communicate through external networks such as the Internet. Types of remote access
include dial-up, broadband, and wireless. Organizations use encrypted virtual private networks
(VPNs) to enhance confidentiality and integrity for remote connections. The use of encrypted
VPNs provides sufficient assurance to the organization that it can effectively treat such
connections as internal networks if the cryptographic mechanisms used are implemented in
accordance with applicable laws, executive orders, directives, regulations, policies, standards,
and guidelines. Still, VPN connections traverse external networks, and the encrypted VPN does
not enhance the availability of remote connections. VPNs with encrypted tunnels can also affect
the ability to adequately monitor network communications traffic for malicious code. Remote
access controls apply to systems other than public web servers or systems designed for public
access.
Authorization of each remote access type addresses authorization prior to allowing
remote access without specifying the specific formats for such authorization. While organizations
may use information exchange and system connection security agreements to manage remote
access connections to other systems, such agreements are addressed as part of CA-3. Enforcing
access restrictions for remote access is addressed via AC-3.
Related Controls:  AC-2, AC-3, AC-4, AC-18, AC-19, AC-20, CA-3, CM-10, IA-2, IA-3, IA-8, MA-4, PE-
17, PL-2, PL-4, SC-10, SC-12, SC-13, SI-4.
Control Enhancements:
(1) REMOTE ACCESS | MONITORING AND CONTROL
Employ automated mechanisms to monitor and control remote access methods.
Discussion:  Monitoring and control of remote access methods allows organizations to
detect attacks and help ensure compliance with remote access policies by auditing the
connection activities of remote users on a variety of system components, including servers,
CHAPTER THREE   PAGE 49
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
notebook computers, workstations, smart phones, and tablets. Audit logging for remote
access is enforced by AU-2. Audit events are defined in AU-2a.
Related Controls:  AU-2, AU-6, AU-12, AU-14.
(2) REMOTE ACCESS | PROTECTION OF CONFIDENTIALITY AND INTEGRITY USING ENCRYPTION
Implement cryptographic mechanisms to protect the confidentiality and integrity of
remote access sessions.
Discussion:  Virtual private networks can be used to protect the confidentiality and integrity
of remote access sessions. Transport Layer Security (TLS) is an example of a cryptographic
protocol that provides end-to-end communications security over networks and is used for
Internet communications and online transactions.
Related Controls:  SC-8, SC-12, SC-13.
(3) REMOTE ACCESS | MANAGED ACCESS CONTROL POINTS
Route remote accesses through authorized and managed network access control points.
Discussion:  Organizations consider the Trusted Internet Connections (TIC) initiative [DHS
TIC] requirements for external network connections since limiting the number of access
control points for remote access reduces attack surfaces.
Related Controls:  SC-7.
(4) REMOTE ACCESS | PRIVILEGED COMMANDS AND ACCESS
(a) Authorize the execution of privileged commands and access to security-relevant
information via remote access only in a format that provides assessable evidence and
for the following needs: [Assignment: organization-defined needs]; and
(b) Document the rationale for remote access in the security plan for the system.
Discussion:  Remote access to systems represents a significant potential vulnerability that
can be exploited by adversaries. As such, restricting the execution of privileged commands
and access to security-relevant information via remote access reduces the exposure of the
organization and the susceptibility to threats by adversaries to the remote access capability.
Related Controls:  AC-6, SC-12, SC-13.
(5) REMOTE ACCESS | MONITORING FOR UNAUTHORIZED CONNECTIONS
[Withdrawn: Incorporated into SI-4.]
(6) REMOTE ACCESS | PROTECTION OF MECHANISM INFORMATION
Protect information about remote access mechanisms from unauthorized use and
disclosure.
Discussion:  Remote access to organizational information by non-organizational entities can
increase the risk of unauthorized use and disclosure about remote access mechanisms. The
organization considers including remote access requirements in the information exchange
agreements with other organizations, as applicable. Remote access requirements can also be
included in rules of behavior (see PL-4) and access agreements (see PS-6).
Related Controls:  AT-2, AT-3, PS-6.
(7) REMOTE ACCESS | ADDITIONAL PROTECTION FOR SECURITY FUNCTION ACCESS
[Withdrawn: Incorporated into AC-3(10).]
(8) REMOTE ACCESS | DISABLE NONSECURE NETWORK PROTOCOLS
[Withdrawn: Incorporated into CM-7.]
(9) REMOTE ACCESS | DISCONNECT OR DISABLE ACCESS
CHAPTER THREE   PAGE 50
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
Provide the capability to disconnect or disable remote access to the system within
[Assignment: organization-defined time period].
Discussion:  The speed of system disconnect or disablement varies based on the criticality of
missions or business functions and the need to eliminate immediate or future remote access
to systems.
Related Controls:  None.
(10) REMOTE ACCESS | AUTHENTICATE REMOTE COMMANDS
Implement [Assignment: organization-defined mechanisms] to authenticate [Assignment:
organization-defined remote commands].
Discussion:  Authenticating remote commands protects against unauthorized commands and
the replay of authorized commands. The ability to authenticate remote commands is
important for remote systems for which loss, malfunction, misdirection, or exploitation
would have immediate or serious consequences, such as injury, death, property damage,
loss of high value assets, failure of mission or business functions, or compromise of classified
or controlled unclassified information. Authentication mechanisms for remote commands
ensure that systems accept and execute commands in the order intended, execute only
authorized commands, and reject unauthorized commands. Cryptographic mechanisms can
be used, for example, to authenticate remote commands.
Related Controls:  SC-12, SC-13, SC-23.
References:  [SP 800-46], [SP 800-77], [SP 800-113], [SP 800-114], [SP 800-121], [IR 7966].
