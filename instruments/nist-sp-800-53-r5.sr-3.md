---
schema_version: 1
corpus: federal-reference
jurisdiction: us
id: nist-sp-800-53-r5.sr-3
title: NIST SP 800-53 Rev. 5 SR-3 — SUPPLY CHAIN CONTROLS AND PROCESSES
doc_type: federal_instrument
citation: NIST SP 800-53 Rev. 5 SR-3
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

**NIST SP 800-53 Rev. 5 SR-3** — SUPPLY CHAIN CONTROLS AND PROCESSES

- Issued by: National Institute of Standards and Technology
- Publication: NIST SP 800-53 Rev. 5 — Security and Privacy Controls for Information Systems and Organizations ([nist-sp-800-53-r5](./nist-sp-800-53-r5.md))
- Version: Rev. 5 (September 2020, includes updates as of 2020-12-10)
- Text as of: 2026-11-12
- Cited by held documents: 28 times (cjis-sp-6-1 ×16, arc-ampe ×7, irs-pub-1075-11-2021 ×3, 6-cfr-37 ×2)
- Reproduction basis: 17 U.S.C. § 105 — work of the U.S. government (NIST). Determined per document on 2026-11-12 against the publication itself, not assumed from its issuer: its Authority statement (PDF page 3) reads "This publication may be used by nongovernmental organizations on a voluntary basis and is not subject to copyright in the United States. Attribution would, however, be appreciated by NIST." Held here: the front matter and Chapter Three (the control catalog) only. Chapter Three names ISO/IEC standards solely as bibliographic references and reproduces none of their text. NOT mirrored: the References bibliography and Appendices A-C; Appendix A (glossary) adapts third-party definitions (ISO/IEC 15026, ISO 25237, ISO/IEC 29100, ISO 15288, IETF RFC 4949), which ADR-0002 treats as not reproducible by being incorporated, and whose reproducibility has not been determined.


_NON-AUTHORITATIVE copy of one control, cut from the SP 800-53 Rev. 5 snapshot this corpus holds. Whether and how this binds a given agency depends on the instrument that incorporates it — read it at the source URL before relying on it. This copy is the Rev. 5 text of record, which is not necessarily the text a citing document meant (a document citing Rev. 4 is not answered by it)._


## Full text

### SR-3 SUPPLY CHAIN CONTROLS AND PROCESSES
Control:
a. Establish a process or processes to identify and address weaknesses or deficiencies in the
supply chain elements and processes of [Assignment: organization-defined system or system
component] in coordination with [Assignment: organization-defined supply chain personnel];
b. Employ the following controls to protect against supply chain risks to the system, system
component, or system service and to limit the harm or consequences from supply chain-
related events: [Assignment: organization-defined supply chain controls]; and
c. Document the selected and implemented supply chain processes and controls in [Selection:
security and privacy plans; supply chain risk management plan; [Assignment: organization-
defined document]].
Discussion:  Supply chain elements include organizations, entities, or tools employed for the
research and development, design, manufacturing, acquisition, delivery, integration, operations
and maintenance, and disposal of systems and system components. Supply chain processes
include hardware, software, and firmware development processes; shipping and handling
procedures; personnel security and physical security programs; configuration management tools,
techniques, and measures to maintain provenance; or other programs, processes, or procedures
associated with the development, acquisition, maintenance and disposal of systems and system
components. Supply chain elements and processes may be provided by organizations, system
integrators, or external providers. Weaknesses or deficiencies in supply chain elements or
processes represent potential vulnerabilities that can be exploited by adversaries to cause harm
to the organization and affect its ability to carry out its core missions or business functions.
Supply chain personnel are individuals with roles and responsibilities in the supply chain.
Related Controls:  CA-2, MA-2, MA-6, PE-3, PE-16, PL-8, PM-30, SA-2, SA-3, SA-4, SA-5, SA-8, SA-9,
SA-10, SA-15, SC-7, SC-29, SC-30, SC-38, SI-7, SR-6, SR-9, SR-11.
Control Enhancements:
CHAPTER THREE   PAGE 366
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
(1) SUPPLY CHAIN CONTROLS AND PROCESSES | DIVERSE SUPPLY BASE
Employ a diverse set of sources for the following system components and services:
[Assignment: organization-defined system components and services].
Discussion:  Diversifying the supply of systems, system components, and services can reduce
the probability that adversaries will successfully identify and target the supply chain and can
reduce the impact of a supply chain event or compromise. Identifying multiple suppliers for
replacement components can reduce the probability that the replacement component will
become unavailable. Employing a diverse set of developers or logistics service providers can
reduce the impact of a natural disaster or other supply chain event. Organizations consider
designing the system to include diverse materials and components.
Related Controls:  None.
(2) SUPPLY CHAIN PROTECTION CONTROLS AND PROCESSES | LIMITATION OF HARM
Employ the following controls to limit harm from potential adversaries identifying and
targeting the organizational supply chain: [Assignment: organization-defined controls].
Discussion:  Controls that can be implemented to reduce the probability of adversaries
successfully identifying and targeting the supply chain include avoiding the purchase of
custom or non-standardized configurations, employing approved vendor lists with standing
reputations in industry, following pre-agreed maintenance schedules and update and patch
delivery mechanisms, maintaining a contingency plan in case of a supply chain event, using
procurement carve-outs that provide exclusions to commitments or obligations, using
diverse delivery routes, and minimizing the time between purchase decisions and delivery.
Related Controls:  None.
(3) SUPPLY CHAIN PROTECTION CONTROLS AND PROCESSES | SUB-TIER FLOW DOWN
Ensure that the controls included in the contracts of prime contractors are also included in
the contracts of subcontractors.
Discussion:  To manage supply chain risk effectively and holistically, it is important that
organizations ensure that supply chain risk management controls are included at all tiers in
the supply chain. This includes ensuring that Tier 1 (prime) contractors have implemented
processes to facilitate the “flow down” of supply chain risk management controls to sub-tier
contractors. The controls subject to flow down are identified in SR-3b.
Related Controls:  SR-5, SR-8.
References:  [FASC18], [41 CFR 201], [EO 13873], [ISO 20243], [SP 800-30], [SP 800-161], [IR
7622].
