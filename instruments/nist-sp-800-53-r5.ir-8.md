---
schema_version: 1
corpus: federal-reference
jurisdiction: us
id: nist-sp-800-53-r5.ir-8
title: NIST SP 800-53 Rev. 5 IR-8 — INCIDENT RESPONSE PLAN
doc_type: federal_instrument
citation: NIST SP 800-53 Rev. 5 IR-8
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

**NIST SP 800-53 Rev. 5 IR-8** — INCIDENT RESPONSE PLAN

- Issued by: National Institute of Standards and Technology
- Publication: NIST SP 800-53 Rev. 5 — Security and Privacy Controls for Information Systems and Organizations ([nist-sp-800-53-r5](./nist-sp-800-53-r5.md))
- Version: Rev. 5 (September 2020, includes updates as of 2020-12-10)
- Text as of: 2026-11-12
- Cited by held documents: 29 times (cjis-sp-6-1 ×19, arc-ampe ×5, irs-pub-1075-11-2021 ×4, 6-cfr-37 ×1)
- Reproduction basis: 17 U.S.C. § 105 — work of the U.S. government (NIST). Determined per document on 2026-11-12 against the publication itself, not assumed from its issuer: its Authority statement (PDF page 3) reads "This publication may be used by nongovernmental organizations on a voluntary basis and is not subject to copyright in the United States. Attribution would, however, be appreciated by NIST." Held here: the front matter and Chapter Three (the control catalog) only. Chapter Three names ISO/IEC standards solely as bibliographic references and reproduces none of their text. NOT mirrored: the References bibliography and Appendices A-C; Appendix A (glossary) adapts third-party definitions (ISO/IEC 15026, ISO 25237, ISO/IEC 29100, ISO 15288, IETF RFC 4949), which ADR-0002 treats as not reproducible by being incorporated, and whose reproducibility has not been determined.


_NON-AUTHORITATIVE copy of one control, cut from the SP 800-53 Rev. 5 snapshot this corpus holds. Whether and how this binds a given agency depends on the instrument that incorporates it — read it at the source URL before relying on it. This copy is the Rev. 5 text of record, which is not necessarily the text a citing document meant (a document citing Rev. 4 is not answered by it)._


> **Release 5.2.0 postdates this text.** NIST's listing of record ([https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final)) says that on 2025-08-27 it issued release 5.2.0 of SP 800-53, which updates the related controls for this control. The text below is the Rev. 5 PDF of record and does NOT include that change; read NIST's own list of the changes ([summary](https://csrc.nist.gov/files/projects/Risk-Management/800-53%20Comment%20Site/SP800-53-r5.2.0-changes.pdf)) before relying on this control's text.


## Full text

### IR-8 INCIDENT RESPONSE PLAN
Control:
a. Develop an incident response plan that:
1. Provides the organization with a roadmap for implementing its incident response
capability;
2. Describes the structure and organization of the incident response capability;
3. Provides a high-level approach for how the incident response capability fits into the
overall organization;
4. Meets the unique requirements of the organization, which relate to mission, size,
structure, and functions;
5. Defines reportable incidents;
CHAPTER THREE   PAGE 159
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
6. Provides metrics for measuring the incident response capability within the organization;
7. Defines the resources and management support needed to effectively maintain and
mature an incident response capability;
8. Addresses the sharing of incident information;
9. Is reviewed and approved by [Assignment: organization-defined personnel or roles]
[Assignment: organization-defined frequency]; and
10. Explicitly designates responsibility for incident response to [Assignment: organization-
defined entities, personnel, or roles].
b. Distribute copies of the incident response plan to [Assignment: organization-defined incident
response personnel (identified by name and/or by role) and organizational elements];
c. Update the incident response plan to address system and organizational changes or
problems encountered during plan implementation, execution, or testing;
d. Communicate incident response plan changes to [Assignment: organization-defined incident
response personnel (identified by name and/or by role) and organizational elements]; and
e. Protect the incident response plan from unauthorized disclosure and modification.
Discussion:  It is important that organizations develop and implement a coordinated approach to
incident response. Organizational mission and business functions determine the structure of
incident response capabilities. As part of the incident response capabilities, organizations
consider the coordination and sharing of information with external organizations, including
external service providers and other organizations involved in the supply chain. For incidents
involving personally identifiable information (i.e., breaches), include a process to determine
whether notice to oversight organizations or affected individuals is appropriate and provide that
notice accordingly.
Related Controls:  AC-2, CP-2, CP-4, IR-4, IR-7, IR-9, PE-6, PL-2, SA-15, SI-12, SR-8.
Control Enhancements:
(1) INCIDENT RESPONSE PLAN | BREACHES
Include the following in the Incident Response Plan for breaches involving personally
identifiable information:
(a) A process to determine if notice to individuals or other organizations, including
oversight organizations, is needed;
(b) An assessment process to determine the extent of the harm, embarrassment,
inconvenience, or unfairness to affected individuals and any mechanisms to mitigate
such harms; and
(c) Identification of applicable privacy requirements.
Discussion:  Organizations may be required by law, regulation, or policy to follow specific
procedures relating to breaches, including notice to individuals, affected organizations, and
oversight bodies; standards of harm; and mitigation or other specific requirements.
Related Controls:  PT-1, PT-2, PT-3, PT-4, PT-5, PT-7.
References:  [OMB A-130], [SP 800-61], [OMB M-17-12].
