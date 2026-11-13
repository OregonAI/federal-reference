---
schema_version: 1
corpus: federal-reference
jurisdiction: us
id: nist-sp-800-53-r5.sc-8
title: NIST SP 800-53 Rev. 5 SC-8 — TRANSMISSION CONFIDENTIALITY AND INTEGRITY
doc_type: federal_instrument
citation: NIST SP 800-53 Rev. 5 SC-8
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

**NIST SP 800-53 Rev. 5 SC-8** — TRANSMISSION CONFIDENTIALITY AND INTEGRITY

- Issued by: National Institute of Standards and Technology
- Publication: NIST SP 800-53 Rev. 5 — Security and Privacy Controls for Information Systems and Organizations ([nist-sp-800-53-r5](./nist-sp-800-53-r5.md))
- Version: Rev. 5 (September 2020, includes updates as of 2020-12-10)
- Text as of: 2026-11-12
- Cited by held documents: 25 times (cjis-sp-6-1 ×18, irs-pub-1075-11-2021 ×4, arc-ampe ×2, 6-cfr-37 ×1)
- Reproduction basis: 17 U.S.C. § 105 — work of the U.S. government (NIST). Determined per document on 2026-11-12 against the publication itself, not assumed from its issuer: its Authority statement (PDF page 3) reads "This publication may be used by nongovernmental organizations on a voluntary basis and is not subject to copyright in the United States. Attribution would, however, be appreciated by NIST." Held here: the front matter and Chapter Three (the control catalog) only. Chapter Three names ISO/IEC standards solely as bibliographic references and reproduces none of their text. NOT mirrored: the References bibliography and Appendices A-C; Appendix A (glossary) adapts third-party definitions (ISO/IEC 15026, ISO 25237, ISO/IEC 29100, ISO 15288, IETF RFC 4949), which ADR-0002 treats as not reproducible by being incorporated, and whose reproducibility has not been determined.


_NON-AUTHORITATIVE copy of one control, cut from the SP 800-53 Rev. 5 snapshot this corpus holds. Whether and how this binds a given agency depends on the instrument that incorporates it — read it at the source URL before relying on it. This copy is the Rev. 5 text of record, which is not necessarily the text a citing document meant (a document citing Rev. 4 is not answered by it)._


## Full text

### SC-8 TRANSMISSION CONFIDENTIALITY AND INTEGRITY
Control:  Protect the [Selection (one or more): confidentiality; integrity] of transmitted
information.
Discussion:  Protecting the confidentiality and integrity of transmitted information applies to
internal and external networks as well as any system components that can transmit information,
including servers, notebook computers, desktop computers, mobile devices, printers, copiers,
scanners, facsimile machines, and radios. Unprotected communication paths are exposed to the
possibility of interception and modification. Protecting the confidentiality and integrity of
information can be accomplished by physical or logical means. Physical protection can be
achieved by using protected distribution systems. A protected distribution system is a wireline or
fiber-optics telecommunications system that includes terminals and adequate electromagnetic,
CHAPTER THREE   PAGE 305
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
acoustical, electrical, and physical controls to permit its use for the unencrypted transmission of
classified information. Logical protection can be achieved by employing encryption techniques.
Organizations that rely on commercial providers who offer transmission services as commodity
services rather than as fully dedicated services may find it difficult to obtain the necessary
assurances regarding the implementation of needed controls for transmission confidentiality and
integrity. In such situations, organizations determine what types of confidentiality or integrity
services are available in standard, commercial telecommunications service packages. If it is not
feasible to obtain the necessary controls and assurances of control effectiveness through
appropriate contracting vehicles, organizations can implement appropriate compensating
controls.
Related Controls:  AC-17, AC-18, AU-10, IA-3, IA-8, IA-9, MA-4, PE-4, SA-4, SA-8, SC-7, SC-16,
SC-
20, SC-23, SC-28.
Control Enhancements:
(1) TRANSMISSION CONFIDENTIALITY AND INTEGRITY | CRYPTOGRAPHIC PROTECTION
Implement cryptographic mechanisms to [Selection (one or more): prevent unauthorized
disclosure of information; detect changes to information] during transmission.
Discussion:  Encryption protects information from unauthorized disclosure and modification
during transmission. Cryptographic mechanisms that protect the confidentiality and integrity
of information during transmission include TLS and IPSec. Cryptographic mechanisms used to
protect information integrity include cryptographic hash functions that have applications in
digital signatures, checksums, and message authentication codes.
Related Controls:  SC-12,  SC-13.
(2) TRANSMISSION CONFIDENTIALITY AND INTEGRITY | PRE- AND POST-TRANSMISSION HANDLING
Maintain the [Selection (one or more): confidentiality; integrity] of information during
preparation for transmission and during reception.
Discussion:  Information can be unintentionally or maliciously disclosed or modified during
preparation for transmission or during reception, including during aggregation, at protocol
transformation points, and during packing and unpacking. Such unauthorized disclosures or
modifications compromise the confidentiality or integrity of the information.
Related Controls:  None.
(3) TRANSMISSION CONFIDENTIALITY AND INTEGRITY | CRYPTOGRAPHIC PROTECTION FOR MESSAGE
EXTERNALS
Implement cryptographic mechanisms to protect message externals unless otherwise
protected by [Assignment: organization-defined alternative physical controls].
Discussion:  Cryptographic protection for message externals addresses protection from the
unauthorized disclosure of information. Message externals include message headers and
routing information. Cryptographic protection prevents the exploitation of message
externals and applies to internal and external networks or links that may be visible to
individuals who are not authorized users. Header and routing information is sometimes
transmitted in clear text (i.e., unencrypted) because the information is not identified by
organizations as having significant value or because encrypting the information can result in
lower network performance or higher costs. Alternative physical controls include protected
distribution systems.
Related Controls:  SC-12, SC-13.
(4) TRANSMISSION CONFIDENTIALITY AND INTEGRITY | CONCEAL OR RANDOMIZE COMMUNICATIONS
CHAPTER THREE   PAGE 306
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
Implement cryptographic mechanisms to conceal or randomize communication patterns
unless otherwise protected by [Assignment: organization-defined alternative physical
controls].
Discussion:  Concealing or randomizing communication patterns addresses protection from
unauthorized disclosure of information. Communication patterns include frequency, periods,
predictability, and amount. Changes to communications patterns can reveal information
with intelligence value, especially when combined with other available information related
to the mission and business functions of the organization. Concealing or randomizing
communications prevents the derivation of intelligence based on communications patterns
and applies to both internal and external networks or links that may be visible to individuals
who are not authorized users. Encrypting the links and transmitting in continuous, fixed, or
random patterns prevents the derivation of intelligence from the system communications
patterns. Alternative physical controls include protected distribution systems.
Related Controls:  SC-12, SC-13.
(5) TRANSMISSION CONFIDENTIALITY AND INTEGRITY | PROTECTED DISTRIBUTION SYSTEM
Implement [Assignment: organization-defined protected distribution system] to [Selection
(one or more): prevent unauthorized disclosure of information; detect changes to
information] during transmission.
Discussion:  The purpose of a protected distribution system is to deter, detect, and/or make
difficult physical access to the communication lines that carry national security information.
Related Controls:  None.
References:  [FIPS 140-3], [FIPS 197], [SP 800-52], [SP 800-77], [SP 800-81-2], [SP 800-113], [SP
800-177], [IR 8023].
