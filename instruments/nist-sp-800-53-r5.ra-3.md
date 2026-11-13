---
schema_version: 1
corpus: federal-reference
jurisdiction: us
id: nist-sp-800-53-r5.ra-3
title: NIST SP 800-53 Rev. 5 RA-3 — RISK ASSESSMENT
doc_type: federal_instrument
citation: NIST SP 800-53 Rev. 5 RA-3
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

**NIST SP 800-53 Rev. 5 RA-3** — RISK ASSESSMENT

- Issued by: National Institute of Standards and Technology
- Publication: NIST SP 800-53 Rev. 5 — Security and Privacy Controls for Information Systems and Organizations ([nist-sp-800-53-r5](./nist-sp-800-53-r5.md))
- Version: Rev. 5 (September 2020, includes updates as of 2020-12-10)
- Text as of: 2026-11-12
- Cited by held documents: 41 times (cjis-sp-6-1 ×28, arc-ampe ×9, irs-pub-1075-11-2021 ×3, 6-cfr-37 ×1)
- Reproduction basis: 17 U.S.C. § 105 — work of the U.S. government (NIST). Determined per document on 2026-11-12 against the publication itself, not assumed from its issuer: its Authority statement (PDF page 3) reads "This publication may be used by nongovernmental organizations on a voluntary basis and is not subject to copyright in the United States. Attribution would, however, be appreciated by NIST." Held here: the front matter and Chapter Three (the control catalog) only. Chapter Three names ISO/IEC standards solely as bibliographic references and reproduces none of their text. NOT mirrored: the References bibliography and Appendices A-C; Appendix A (glossary) adapts third-party definitions (ISO/IEC 15026, ISO 25237, ISO/IEC 29100, ISO 15288, IETF RFC 4949), which ADR-0002 treats as not reproducible by being incorporated, and whose reproducibility has not been determined.


_NON-AUTHORITATIVE copy of one control, cut from the SP 800-53 Rev. 5 snapshot this corpus holds. Whether and how this binds a given agency depends on the instrument that incorporates it — read it at the source URL before relying on it. This copy is the Rev. 5 text of record, which is not necessarily the text a citing document meant (a document citing Rev. 4 is not answered by it)._


## Full text

### RA-3 RISK ASSESSMENT
Control:
a. Conduct a risk assessment, including:
1. Identifying threats to and vulnerabilities in the system;
2. Determining the likelihood and magnitude of harm from unauthorized access, use,
disclosure, disruption, modification, or destruction of the system, the information it
processes, stores, or transmits, and any related information; and
3. Determining the likelihood and impact of adverse effects on individuals arising from the
processing of personally identifiable information;
b. Integrate risk assessment results and risk management decisions from the organization and
mission or business process perspectives with system-level risk assessments;
c. Document risk assessment results in [Selection: security and privacy plans; risk assessment
report; [Assignment: organization-defined document]];
d. Review risk assessment results [Assignment: organization-defined frequency];
e. Disseminate risk assessment results to [Assignment: organization-defined personnel or
roles]; and
f. Update the risk assessment [Assignment: organization-defined frequency] or when there are
significant changes to the system, its environment of operation, or other conditions that may
impact the security or privacy state of the system.
Discussion:  Risk assessments consider threats, vulnerabilities, likelihood, and impact to
organizational operations and assets, individuals, other organizations, and the Nation. Risk
assessments also consider risk from external parties, including contractors who operate systems
on behalf of the organization, individuals who access organizational systems, service providers,
and outsourcing entities.
Organizations can conduct risk assessments at all three levels in the risk management hierarchy
(i.e., organization level, mission/business process level, or information system level) and at any
stage in the system development life cycle. Risk assessments can also be conducted at various
steps in the Risk Management Framework, including preparation, categorization, control
selection, control implementation, control assessment, authorization, and control monitoring.
Risk assessment is an ongoing activity carried out throughout the system development life cycle.
Risk assessments can also address information related to the system, including system design,
the intended use of the system, testing results, and supply chain-related information or artifacts.
Risk assessments can play an important role in control selection processes, particularly during
the application of tailoring guidance and in the earliest phases of capability determination.
Related Controls:  CA-3, CA-6, CM-4, CM-13, CP-6, CP-7, IA-8, MA-5, PE-3, PE-8, PE-18, PL-2, PL-
10, PL-11, PM-8, PM-9, PM-28, PT-2, PT-7, RA-2, RA-5, RA-7, SA-8, SA-9, SC-38, SI-12.
Control Enhancements:
(1) RISK ASSESSMENT | SUPPLY CHAIN RISK ASSESSMENT
CHAPTER THREE   PAGE 241
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
(a) Assess supply chain risks associated with [Assignment: organization-defined systems,
system components, and system services]; and
(b) Update the supply chain risk assessment [Assignment: organization-defined
frequency], when there are significant changes to the relevant supply chain, or when
changes to the system, environments of operation, or other conditions may
necessitate a change in the supply chain.
Discussion:  Supply chain-related events include disruption, use of defective components,
insertion of counterfeits, theft, malicious development practices, improper delivery
practices, and insertion of malicious code. These events can have a significant impact on the
confidentiality, integrity, or availability of a system and its information and, therefore, can
also adversely impact organizational operations (including mission, functions, image, or
reputation), organizational assets, individuals, other organizations, and the Nation. The
supply chain-related events may be unintentional or malicious and can occur at any point
during the system life cycle. An analysis of supply chain risk can help an organization identify
systems or components for which additional supply chain risk mitigations are required.
Related Controls:  RA-2, RA-9, PM-17, PM-30, SR-2.
(2) RISK ASSESSMENT | USE OF ALL-SOURCE INTELLIGENCE
Use all-source intelligence to assist in the analysis of risk.
Discussion:  Organizations employ all-source intelligence to inform engineering, acquisition,
and risk management decisions. All-source intelligence consists of information derived from
all available sources, including publicly available or open-source information, measurement
and signature intelligence, human intelligence, signals intelligence, and imagery intelligence.
All-source intelligence is used to analyze the risk of vulnerabilities (both intentional and
unintentional) from development, manufacturing, and delivery processes, people, and the
environment. The risk analysis may be performed on suppliers at multiple tiers in the supply
chain sufficient to manage risks. Organizations may develop agreements to share all-source
intelligence information or resulting decisions with other organizations, as appropriate.
Related Controls:  None.
(3) RISK ASSESSMENT | DYNAMIC THREAT AWARENESS
Determine the current cyber threat environment on an ongoing basis using [Assignment:
organization-defined means].
Discussion:  The threat awareness information that is gathered feeds into the organization’s
information security operations to ensure that procedures are updated in response to the
changing threat environment. For example, at higher threat levels, organizations may
change the privilege or authentication thresholds required to perform certain operations.
Related Controls:  AT-2.
(4) RISK ASSESSMENT | PREDICTIVE CYBER ANALYTICS
Employ the following advanced automation and analytics capabilities to predict and
identify risks to [Assignment: organization-defined systems or system components]:
[Assignment: organization-defined advanced automation and analytics capabilities].
Discussion:  A properly resourced Security Operations Center (SOC) or Computer Incident
Response Team (CIRT) may be overwhelmed by the volume of information generated by the
proliferation of security tools and appliances unless it employs advanced automation and
analytics to analyze the data. Advanced automation and analytics capabilities are typically
supported by artificial intelligence concepts, including machine learning. Examples include
Automated Threat Discovery and Response (which includes broad-based collection, context-
based analysis, and adaptive response capabilities), automated workflow operations, and
machine assisted decision tools.
Note, however, that sophisticated adversaries may be able
CHAPTER THREE   PAGE 242
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
to extract information related to analytic parameters and retrain the machine learning to
classify malicious activity as benign. Accordingly, machine learning is augmented by human
monitoring to ensure that sophisticated adversaries are not able to conceal their activities.
Related Controls:  None.
References:  [OMB A-130], [SP 800-30], [SP 800-39], [SP 800-161], [IR 8023], [IR 8062], [IR 8272].
