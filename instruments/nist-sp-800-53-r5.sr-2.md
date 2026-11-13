---
schema_version: 1
corpus: federal-reference
jurisdiction: us
id: nist-sp-800-53-r5.sr-2
title: NIST SP 800-53 Rev. 5 SR-2 — SUPPLY CHAIN RISK MANAGEMENT PLAN
doc_type: federal_instrument
citation: NIST SP 800-53 Rev. 5 SR-2
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

**NIST SP 800-53 Rev. 5 SR-2** — SUPPLY CHAIN RISK MANAGEMENT PLAN

- Issued by: National Institute of Standards and Technology
- Publication: NIST SP 800-53 Rev. 5 — Security and Privacy Controls for Information Systems and Organizations ([nist-sp-800-53-r5](./nist-sp-800-53-r5.md))
- Version: Rev. 5 (September 2020, includes updates as of 2020-12-10)
- Text as of: 2026-11-12
- Cited by held documents: 22 times (cjis-sp-6-1 ×13, arc-ampe ×4, irs-pub-1075-11-2021 ×3, 6-cfr-37 ×2)
- Reproduction basis: 17 U.S.C. § 105 — work of the U.S. government (NIST). Determined per document on 2026-11-12 against the publication itself, not assumed from its issuer: its Authority statement (PDF page 3) reads "This publication may be used by nongovernmental organizations on a voluntary basis and is not subject to copyright in the United States. Attribution would, however, be appreciated by NIST." Held here: the front matter and Chapter Three (the control catalog) only. Chapter Three names ISO/IEC standards solely as bibliographic references and reproduces none of their text. NOT mirrored: the References bibliography and Appendices A-C; Appendix A (glossary) adapts third-party definitions (ISO/IEC 15026, ISO 25237, ISO/IEC 29100, ISO 15288, IETF RFC 4949), which ADR-0002 treats as not reproducible by being incorporated, and whose reproducibility has not been determined.


_NON-AUTHORITATIVE copy of one control, cut from the SP 800-53 Rev. 5 snapshot this corpus holds. Whether and how this binds a given agency depends on the instrument that incorporates it — read it at the source URL before relying on it. This copy is the Rev. 5 text of record, which is not necessarily the text a citing document meant (a document citing Rev. 4 is not answered by it)._


## Full text

### SR-2 SUPPLY CHAIN RISK MANAGEMENT PLAN
Control:
a. Develop a plan for managing supply chain risks associated with the research and
development, design, manufacturing, acquisition, delivery, integration, operations and
maintenance, and disposal of the following systems, system components or system services:
[Assignment: organization-defined systems, system components, or system services];
b. Review and update the supply chain risk management plan [Assignment: organization-
defined frequency] or as required, to address threat, organizational or environmental
changes; and
c. Protect the supply chain risk management plan from unauthorized disclosure and
modification.
Discussion:  The dependence on products, systems, and services from external providers, as well
as the nature of the relationships with those providers, present an increasing level of risk to an
organization. Threat actions that may increase security or privacy risks include unauthorized
production, the insertion or use of counterfeits, tampering, theft, insertion of malicious software
and hardware, and poor manufacturing and development practices in the supply chain. Supply
chain risks can be endemic or systemic within a system element or component, a system, an
organization, a sector, or the Nation. Managing supply chain risk is a complex, multifaceted
undertaking that requires a coordinated effort across an organization to build trust relationships
and communicate with internal and external stakeholders. Supply chain risk management
(SCRM) activities include identifying and assessing risks, determining appropriate risk response
actions, developing SCRM plans to document response actions, and monitoring performance
against plans. The SCRM plan (at the system-level) is implementation specific, providing policy
implementation, requirements, constraints and implications. It can either be stand-alone, or
incorporated into system security and privacy plans. The SCRM plan addresses managing,
implementation, and monitoring of SCRM controls and the development/sustainment of systems
across the SDLC to support mission and business functions.
Because supply chains can differ significantly across and within organizations, SCRM plans are
tailored to the individual program, organizational, and operational contexts. Tailored SCRM plans
provide the basis for determining whether a technology, service, system component, or system is
fit for purpose, and as such, the controls need to be tailored accordingly. Tailored SCRM plans
help organizations focus their resources on the most critical mission and business functions
based on mission and business requirements and their risk environment. Supply chain risk
management plans include an expression of the supply chain risk tolerance for the organization,
acceptable supply chain risk mitigation strategies or controls, a process for consistently
evaluating and monitoring supply chain risk, approaches for implementing and communicating
the plan, a description of and justification for supply chain risk mitigation measures taken, and
associated roles and responsibilities. Finally, supply chain risk management plans address
requirements for developing trustworthy, secure, privacy-protective, and resilient system
components and systems, including the application of the security design principles implemented
as part of life cycle-based systems security engineering processes (see SA-8
).
Related Controls:  CA-2, CP-4, IR-4, MA-2, MA-6, PE-16, PL-2, PM-9, PM-30, RA-3, RA-7, SA-8, SI-4.
Control Enhancements:
(1) SUPPLY CHAIN RISK MANAGEMENT PLAN | ESTABLISH SCRM TEAM
CHAPTER THREE   PAGE 365
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
Establish a supply chain risk management team consisting of [Assignment: organization-
defined personnel, roles, and responsibilities] to lead and support the following SCRM
activities: [Assignment: organization-defined supply chain risk management activities].
Discussion: To implement supply chain risk management plans, organizations establish a
coordinated, team-based approach to identify and assess supply chain risks and manage
these risks by using programmatic and technical mitigation techniques. The team approach
enables organizations to conduct an analysis of their supply chain, communicate with
internal and external partners or stakeholders, and gain broad consensus regarding the
appropriate resources for SCRM. The SCRM team consists of organizational personnel with
diverse roles and responsibilities for leading and supporting SCRM activities, including risk
executive, information technology, contracting, information security, privacy, mission or
business, legal, supply chain and logistics, acquisition, business continuity, and other
relevant functions. Members of the SCRM team are involved in various aspects of the SDLC
and, collectively, have an awareness of and provide expertise in acquisition processes, legal
practices, vulnerabilities, threats, and attack vectors, as well as an understanding of the
technical aspects and dependencies of systems. The SCRM team can be an extension of the
security and privacy risk management processes or be included as part of an organizational
risk management team.
Related Controls:  None.
References: [FASC18], [41 CFR 201], [EO 13873], [CNSSD 505], [SP 800-30], [SP 800-39], [SP-800-
160-1], [SP 800-161], [SP 800-181], [IR 7622], [IR 8272].
