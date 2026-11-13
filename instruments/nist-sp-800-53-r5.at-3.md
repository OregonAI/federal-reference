---
schema_version: 1
corpus: federal-reference
jurisdiction: us
id: nist-sp-800-53-r5.at-3
title: NIST SP 800-53 Rev. 5 AT-3 — ROLE-BASED TRAINING
doc_type: federal_instrument
citation: NIST SP 800-53 Rev. 5 AT-3
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

**NIST SP 800-53 Rev. 5 AT-3** — ROLE-BASED TRAINING

- Issued by: National Institute of Standards and Technology
- Publication: NIST SP 800-53 Rev. 5 — Security and Privacy Controls for Information Systems and Organizations ([nist-sp-800-53-r5](./nist-sp-800-53-r5.md))
- Version: Rev. 5 (September 2020, includes updates as of 2020-12-10)
- Text as of: 2026-11-12
- Cited by held documents: 52 times (cjis-sp-6-1 ×37, arc-ampe ×8, irs-pub-1075-11-2021 ×6, 6-cfr-37 ×1), 3 of them naming an enhancement of this control
- Reproduction basis: 17 U.S.C. § 105 — work of the U.S. government (NIST). Determined per document on 2026-11-12 against the publication itself, not assumed from its issuer: its Authority statement (PDF page 3) reads "This publication may be used by nongovernmental organizations on a voluntary basis and is not subject to copyright in the United States. Attribution would, however, be appreciated by NIST." Held here: the front matter and Chapter Three (the control catalog) only. Chapter Three names ISO/IEC standards solely as bibliographic references and reproduces none of their text. NOT mirrored: the References bibliography and Appendices A-C; Appendix A (glossary) adapts third-party definitions (ISO/IEC 15026, ISO 25237, ISO/IEC 29100, ISO 15288, IETF RFC 4949), which ADR-0002 treats as not reproducible by being incorporated, and whose reproducibility has not been determined.


_NON-AUTHORITATIVE copy of one control, cut from the SP 800-53 Rev. 5 snapshot this corpus holds. Whether and how this binds a given agency depends on the instrument that incorporates it — read it at the source URL before relying on it. This copy is the Rev. 5 text of record, which is not necessarily the text a citing document meant (a document citing Rev. 4 is not answered by it)._


## Full text

### AT-3 ROLE-BASED TRAINING
Control:
a. Provide role-based security and privacy training to personnel with the following roles and
responsibilities: [Assignment: organization-defined roles and responsibilities]:
1. Before authorizing access to the system, information, or performing assigned duties,
and [Assignment: organization-defined frequency] thereafter; and
2. When required by system changes;
b. Update role-based training content [Assignment: organization-defined frequency] and
following [Assignment: organization-defined events]; and
c. Incorporate lessons learned from internal or external security incidents or breaches into
role-based training.
Discussion:  Organizations determine the content of training based on the assigned roles and
responsibilities of individuals as well as the security and privacy requirements of organizations
and the systems to which personnel have authorized access, including technical training
specifically tailored for assigned duties. Roles that may require role-based training include senior
leaders or management officials (e.g., head of agency/chief executive officer, chief information
officer, senior accountable official for risk management, senior agency information security
officer, senior agency official for privacy), system owners; authorizing officials; system security
officers; privacy officers; acquisition and procurement officials; enterprise architects; systems
engineers; software developers; systems security engineers; privacy engineers; system, network,
and database administrators; auditors; personnel conducting configuration management
activities; personnel performing verification and validation activities; personnel with access to
system-level software; control assessors; personnel with contingency planning and incident
response duties; personnel with privacy management responsibilities; and personnel with access
to personally identifiable information.
Comprehensive role-based training addresses management, operational, and technical roles and
responsibilities covering physical, personnel, and technical controls. Role-based training also
includes policies, procedures, tools, methods, and artifacts for the security and privacy roles
defined. Organizations provide the training necessary for individuals to fulfill their responsibilities
related to operations and supply chain risk management within the context of organizational
security and privacy programs. Role-based training also applies to contractors who provide
services to federal agencies. Types of training include web-based and computer-based training,
classroom-style training, and hands-on training (including micro-training). Updating role-based
CHAPTER THREE   PAGE 63
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
training on a regular basis helps to ensure that the content remains relevant and effective.
Events that may precipitate an update to role-based training content include, but are not limited
to, assessment or audit findings, security incidents or breaches, or changes in applicable laws,
executive orders, directives, regulations, policies, standards, and guidelines.
Related Controls:  AC-3, AC-17, AC-22, AT-2, AT-4, CP-3, IR-2, IR-4, IR-7, IR-9, PL-4, PM-13, PM-23,
PS-7, PS-9, SA-3, SA-8, SA-11, SA-16, SR-5, SR-6, SR-11.
Control Enhancements:
(1) ROLE-BASED TRAINING | ENVIRONMENTAL CONTROLS
Provide [Assignment: organization-defined personnel or roles] with initial and
[Assignment: organization-defined frequency] training in the employment and operation
of environmental controls.
Discussion:  Environmental controls include fire suppression and detection devices or
systems, sprinkler systems, handheld fire extinguishers, fixed fire hoses, smoke detectors,
temperature or humidity, heating, ventilation, air conditioning, and power within the facility.
Related Controls:  PE-1, PE-11, PE-13, PE-14, PE-15.
(2) ROLE-BASED TRAINING | PHYSICAL SECURITY CONTROLS
Provide [Assignment: organization-defined personnel or roles] with initial and
[Assignment: organization-defined frequency] training in the employment and operation
of physical security controls.
Discussion:  Physical security controls include physical access control devices, physical
intrusion and detection alarms, operating procedures for facility security guards, and
monitoring or surveillance equipment.
Related Controls:  PE-2, PE-3, PE-4.
(3) ROLE-BASED TRAINING | PRACTICAL EXERCISES
Provide practical exercises in security and privacy training that reinforce training
objectives.
Discussion:  Practical exercises for security include training for software developers that
addresses simulated attacks that exploit common software vulnerabilities or spear or whale
phishing attacks targeted at senior leaders or executives. Practical exercises for privacy
include modules with quizzes on identifying and processing personally identifiable
information in various scenarios or scenarios on conducting privacy impact assessments.
Related Controls:  None.
(4) ROLE-BASED TRAINING | SUSPICIOUS COMMUNICATIONS AND ANOMALOUS SYSTEM BEHAVIOR
[Withdrawn: Moved to AT-2(4)].
(5) ROLE-BASED TRAINING | PROCESSING PERSONALLY IDENTIFIABLE INFORMATION
Provide [Assignment: organization-defined personnel or roles] with initial and
[Assignment: organization-defined frequency] training in the employment and operation
of personally identifiable information processing and transparency controls.
Discussion:  Personally identifiable information processing and transparency controls include
the organization’s authority to process personally identifiable information and personally
identifiable information processing purposes. Role-based training for federal agencies
addresses the types of information that may constitute personally identifiable information
and the risks, considerations, and obligations associated with its processing. Such training
also considers the authority to process personally identifiable information documented in
privacy policies and notices, system of records notices, computer matching agreements and
CHAPTER THREE   PAGE 64
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
notices, privacy impact assessments, [PRIVACT] statements, contracts, information sharing
agreements, memoranda of understanding, and/or other documentation.
Related Controls:  PT-2, PT-3, PT-5, PT-6.
References:  [OMB A-130], [SP 800-50], [SP 800-181].
