---
schema_version: 1
corpus: federal-reference
jurisdiction: us
id: nist-sp-800-53-r5.ca-8
title: NIST SP 800-53 Rev. 5 CA-8 — PENETRATION TESTING
doc_type: federal_instrument
citation: NIST SP 800-53 Rev. 5 CA-8
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

**NIST SP 800-53 Rev. 5 CA-8** — PENETRATION TESTING

- Issued by: National Institute of Standards and Technology
- Publication: NIST SP 800-53 Rev. 5 — Security and Privacy Controls for Information Systems and Organizations ([nist-sp-800-53-r5](./nist-sp-800-53-r5.md))
- Version: Rev. 5 (September 2020, includes updates as of 2020-12-10)
- Text as of: 2026-11-12
- Cited by held documents: 5 times (irs-pub-1075-11-2021 ×4, 6-cfr-37 ×1)
- Reproduction basis: 17 U.S.C. § 105 — work of the U.S. government (NIST). Determined per document on 2026-11-12 against the publication itself, not assumed from its issuer: its Authority statement (PDF page 3) reads "This publication may be used by nongovernmental organizations on a voluntary basis and is not subject to copyright in the United States. Attribution would, however, be appreciated by NIST." Held here: the front matter and Chapter Three (the control catalog) only. Chapter Three names ISO/IEC standards solely as bibliographic references and reproduces none of their text. NOT mirrored: the References bibliography and Appendices A-C; Appendix A (glossary) adapts third-party definitions (ISO/IEC 15026, ISO 25237, ISO/IEC 29100, ISO 15288, IETF RFC 4949), which ADR-0002 treats as not reproducible by being incorporated, and whose reproducibility has not been determined.


_NON-AUTHORITATIVE copy of one control, cut from the SP 800-53 Rev. 5 snapshot this corpus holds. Whether and how this binds a given agency depends on the instrument that incorporates it — read it at the source URL before relying on it. This copy is the Rev. 5 text of record, which is not necessarily the text a citing document meant (a document citing Rev. 4 is not answered by it)._


## Full text

### CA-8 PENETRATION TESTING
Control:  Conduct penetration testing [Assignment: organization-defined frequency] on
[Assignment: organization-defined systems or system components].
Discussion:  Penetration testing is a specialized type of assessment conducted on systems or
individual system components to identify vulnerabilities that could be exploited by adversaries.
Penetration testing goes beyond automated vulnerability scanning and is conducted by agents
and teams with demonstrable skills and experience that include technical expertise in network,
operating system, and/or application level security. Penetration testing can be used to validate
vulnerabilities or determine the degree of penetration resistance of systems to adversaries
within specified constraints. Such constraints include time, resources, and skills. Penetration
testing attempts to duplicate the actions of adversaries and provides a more in-depth analysis of
security- and privacy-related weaknesses or deficiencies. Penetration testing is especially
important when organizations are transitioning from older technologies to newer technologies
(e.g., transitioning from IPv4 to IPv6 network protocols).
Organizations can use the results of vulnerability analyses to support penetration testing
activities. Penetration testing can be conducted internally or externally on the hardware,
software, or firmware components of a system and can exercise both physical and technical
controls. A standard method for penetration testing includes a pretest analysis based on full
knowledge of the system, pretest identification of potential vulnerabilities based on the pretest
analysis, and testing designed to determine the exploitability of vulnerabilities. All parties agree
to the rules of engagement before commencing penetration testing scenarios. Organizations
correlate the rules of engagement for the penetration tests with the tools, techniques, and
procedures that are anticipated to be employed by adversaries. Penetration testing may result in
the exposure of information that is protected by laws or regulations, to individuals conducting
the testing. Rules of engagement, contracts, or other appropriate mechanisms can be used to
communicate expectations for how to protect this information. Risk assessments guide the
decisions on the level of independence required for the personnel conducting penetration
testing.
Related Controls:  RA-5, RA-10, SA-11, SR-5, SR-6.
Control Enhancements:
(1) PENETRATION TESTING | INDEPENDENT PENETRATION TESTING AGENT OR TEAM
Employ an independent penetration testing agent or team to perform penetration testing
on the system or system components.
Discussion:  Independent penetration testing agents or teams are individuals or groups who
conduct impartial penetration testing of organizational systems. Impartiality implies that
penetration testing agents or teams are free from perceived or actual conflicts of interest
with respect to the development, operation, or management of the systems that are the
targets of the penetration testing. CA-2(1) provides additional information on independent
assessments that can be applied to penetration testing.
Related Controls:  CA-2.
(2) PENETRATION TESTING | RED TEAM EXERCISES
Employ the following red-team exercises to simulate attempts by adversaries to
compromise organizational systems in accordance with applicable rules of engagement:
[Assignment: organization-defined red team exercises].
Discussion:  Red team exercises extend the objectives of penetration testing by examining
the security and privacy posture of organizations and the capability to implement effective
cyber defenses. Red team exercises simulate attempts by adversaries to compromise
mission and business functions and provide a comprehensive assessment of the security and
CHAPTER THREE   PAGE 94
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
privacy posture of systems and organizations. Such attempts may include technology-based
attacks and social engineering-based attacks. Technology-based attacks include interactions
with hardware, software, or firmware components and/or mission and business processes.
Social engineering-based attacks include interactions via email, telephone, shoulder surfing,
or personal conversations. Red team exercises are most effective when conducted by
penetration testing agents and teams with knowledge of and experience with current
adversarial tactics, techniques, procedures, and tools. While penetration testing may be
primarily laboratory-based testing, organizations can use red team exercises to provide more
comprehensive assessments that reflect real-world conditions. The results from red team
exercises can be used by organizations to improve security and privacy awareness and
training and to assess control effectiveness.
Related Controls:  None.
(3) PENETRATION TESTING | FACILITY PENETRATION TESTING
Employ a penetration testing process that includes [Assignment: organization-defined
frequency] [Selection: announced; unannounced] attempts to bypass or circumvent
controls associated with physical access points to the facility.
Discussion:  Penetration testing of physical access points can provide information on critical
vulnerabilities in the operating environments of organizational systems. Such information
can be used to correct weaknesses or deficiencies in physical controls that are necessary to
protect organizational systems.
Related Controls:  CA-2, PE-3.
References:  None.
