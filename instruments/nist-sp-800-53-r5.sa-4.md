---
schema_version: 1
corpus: federal-reference
jurisdiction: us
id: nist-sp-800-53-r5.sa-4
title: NIST SP 800-53 Rev. 5 SA-4 — ACQUISITION PROCESS
doc_type: federal_instrument
citation: NIST SP 800-53 Rev. 5 SA-4
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

**NIST SP 800-53 Rev. 5 SA-4** — ACQUISITION PROCESS

- Issued by: National Institute of Standards and Technology
- Publication: NIST SP 800-53 Rev. 5 — Security and Privacy Controls for Information Systems and Organizations ([nist-sp-800-53-r5](./nist-sp-800-53-r5.md))
- Version: Rev. 5 (September 2020, includes updates as of 2020-12-10)
- Text as of: 2026-11-12
- Cited by held documents: 32 times (cjis-sp-6-1 ×25, irs-pub-1075-11-2021 ×4, arc-ampe ×2, 6-cfr-37 ×1)
- Reproduction basis: 17 U.S.C. § 105 — work of the U.S. government (NIST). Determined per document on 2026-11-12 against the publication itself, not assumed from its issuer: its Authority statement (PDF page 3) reads "This publication may be used by nongovernmental organizations on a voluntary basis and is not subject to copyright in the United States. Attribution would, however, be appreciated by NIST." Held here: the front matter and Chapter Three (the control catalog) only. Chapter Three names ISO/IEC standards solely as bibliographic references and reproduces none of their text. NOT mirrored: the References bibliography and Appendices A-C; Appendix A (glossary) adapts third-party definitions (ISO/IEC 15026, ISO 25237, ISO/IEC 29100, ISO 15288, IETF RFC 4949), which ADR-0002 treats as not reproducible by being incorporated, and whose reproducibility has not been determined.


_NON-AUTHORITATIVE copy of one control, cut from the SP 800-53 Rev. 5 snapshot this corpus holds. Whether and how this binds a given agency depends on the instrument that incorporates it — read it at the source URL before relying on it. This copy is the Rev. 5 text of record, which is not necessarily the text a citing document meant (a document citing Rev. 4 is not answered by it)._


> **Release 5.2.0 postdates this text.** NIST's listing of record ([https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final)) says that on 2025-08-27 it issued release 5.2.0 of SP 800-53, which updates the control discussion for this control. The text below is the Rev. 5 PDF of record and does NOT include that change; read NIST's own list of the changes ([summary](https://csrc.nist.gov/files/projects/Risk-Management/800-53%20Comment%20Site/SP800-53-r5.2.0-changes.pdf)) before relying on this control's text.


## Full text

### SA-4 ACQUISITION PROCESS
Control:  Include the following requirements, descriptions, and criteria, explicitly or by reference,
using [Selection (one or more): standardized contract language; [Assignment: organization-
defined contract language]] in the acquisition contract for the system, system component, or
system service:
a. Security and privacy functional requirements;
b. Strength of mechanism requirements;
c. Security and privacy assurance requirements;
d. Controls needed to satisfy the security and privacy requirements.
e. Security and privacy documentation requirements;
f. Requirements for protecting security and privacy documentation;
g. Description of the system development environment and environment in which the system
is intended to operate;
h. Allocation of responsibility or identification of parties responsible for information security,
privacy, and supply chain risk management; and
i. Acceptance criteria.
Discussion:  Security and privacy functional requirements are typically derived from the high-
level security and privacy requirements described in SA-2. The derived requirements include
security and privacy capabilities, functions, and mechanisms. Strength requirements associated
with such capabilities, functions, and mechanisms include degree of correctness, completeness,
resistance to tampering or bypass, and resistance to direct attack. Assurance requirements
include development processes, procedures, and methodologies as well as the evidence from
development and assessment activities that provide grounds for confidence that the required
functionality is implemented and possesses the required strength of mechanism. [SP 800-160-1]
describes the process of requirements engineering as part of the system development life cycle.
Controls can be viewed as descriptions of the safeguards and protection capabilities appropriate
for achieving the particular security and privacy objectives of the organization and for reflecting
the security and privacy requirements of stakeholders. Controls are selected and implemented in
order to satisfy system requirements and include developer and organizational responsibilities.
Controls can include technical, administrative, and physical aspects. In some cases, the selection
and implementation of a control may necessitate additional specification by the organization in
the form of derived requirements or instantiated control parameter values. The derived
requirements and control parameter values may be necessary to provide the appropriate level of
implementation detail for controls within the system development life cycle.
Security and privacy documentation requirements address all stages of the system development
life cycle. Documentation provides user and administrator guidance for the implementation and
operation of controls. The level of detail required in such documentation is based on the security
categorization or classification level of the system and the degree to which organizations depend
on the capabilities, functions, or mechanisms to meet risk response expectations. Requirements
can include mandated configuration settings that specify allowed functions, ports, protocols, and
services. Acceptance criteria for systems, system components, and system services are defined in
the same manner as the criteria for any organizational acquisition or procurement.
Related Controls:  CM-6, CM-8, PS-7, SA-3, SA-5, SA-8, SA-11, SA-15, SA-16, SA-17, SA-21, SR-3
,
SR-5.
Control Enhancements:
CHAPTER THREE   PAGE 253
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
(1) ACQUISITION PROCESS | FUNCTIONAL PROPERTIES OF CONTROLS
Require the developer of the system, system component, or system service to provide a
description of the functional properties of the controls to be implemented.
Discussion:  Functional properties of security and privacy controls describe the functionality
(i.e., security or privacy capability, functions, or mechanisms) visible at the interfaces of the
controls and specifically exclude functionality and data structures internal to the operation
of the controls.
Related Controls:  None.
(2) ACQUISITION PROCESS | DESIGN AND IMPLEMENTATION INFORMATION FOR CONTROLS
Require the developer of the system, system component, or system service to provide
design and implementation information for the controls that includes: [Selection (one or
more): security-relevant external system interfaces; high-level design; low-level design;
source code or hardware schematics; [Assignment: organization-defined design and
implementation information]] at [Assignment: organization-defined level of detail].
Discussion:  Organizations may require different levels of detail in the documentation for the
design and implementation of controls in organizational systems, system components, or
system services based on mission and business requirements, requirements for resiliency
and trustworthiness, and requirements for analysis and testing. Systems can be partitioned
into multiple subsystems. Each subsystem within the system can contain one or more
modules. The high-level design for the system is expressed in terms of subsystems and the
interfaces between subsystems providing security-relevant functionality. The low-level
design for the system is expressed in terms of modules and the interfaces between modules
providing security-relevant functionality. Design and implementation documentation can
include manufacturer, version, serial number, verification hash signature, software libraries
used, date of purchase or download, and the vendor or download source. Source code and
hardware schematics are referred to as the implementation representation of the system.
Related Controls:  None.
(3) ACQUISITION PROCESS | DEVELOPMENT METHODS, TECHNIQUES, AND PRACTICES
Require the developer of the system, system component, or system service to
demonstrate the use of a system development life cycle process that includes:
(a) [Assignment: organization-defined systems engineering methods];
(b) [Assignment: organization-defined [Selection (one or more): systems security; privacy]
engineering methods]; and
(c) [Assignment: organization-defined software development methods; testing,
evaluation, assessment, verification, and validation methods; and quality control
processes].
Discussion:  Following a system development life cycle that includes state-of-the-practice
software development methods, systems engineering methods, systems security and privacy
engineering methods, and quality control processes helps to reduce the number and severity
of latent errors within systems, system components, and system services. Reducing the
number and severity of such errors reduces the number of vulnerabilities in those systems,
components, and services. Transparency in the methods and techniques that developers
select and implement for systems engineering, systems security and privacy engineering,
software development, component and system assessments, and quality control processes
provides an increased level of assurance in the trustworthiness of the system, system
component, or system service being acquired.
Related Controls:  None.
(4) ACQUISITION PROCESS | ASSIGNMENT OF COMPONENTS TO SYSTEMS
CHAPTER THREE   PAGE 254
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
[Withdrawn: Incorporated into CM-8(9).]
(5) ACQUISITION PROCESS | SYSTEM, COMPONENT, AND SERVICE CONFIGURATIONS
Require the developer of the system, system component, or system service to:
(a) Deliver the system, component, or service with [Assignment: organization-defined
security configurations] implemented; and
(b) Use the configurations as the default for any subsequent system, component, or
service reinstallation or upgrade.
Discussion:  Examples of security configurations include the U.S. Government Configuration
Baseline (USGCB), Security Technical Implementation Guides (STIGs), and any limitations on
functions, ports, protocols, and services. Security characteristics can include requiring that
default passwords have been changed.
Related Controls:  None.
(6) ACQUISITION PROCESS | USE OF INFORMATION ASSURANCE PRODUCTS
(a) Employ only government off-the-shelf or commercial off-the-shelf information
assurance and information assurance-enabled information technology products that
compose an NSA-approved solution to protect classified information when the
networks used to transmit the information are at a lower classification level than the
information being transmitted; and
(b) Ensure that these products have been evaluated and/or validated by NSA or in
accordance with NSA-approved procedures.
Discussion:  Commercial off-the-shelf IA or IA-enabled information technology products used
to protect classified information by cryptographic means may be required to use NSA-
approved key management. See [NSA CSFC].
Related Controls:  SC-8, SC-12, SC-13.
(7) ACQUISITION PROCESS | NIAP-APPROVED PROTECTION PROFILES
(a) Limit the use of commercially provided information assurance and information
assurance-enabled information technology products to those products that have been
successfully evaluated against a National Information Assurance partnership (NIAP)-
approved Protection Profile for a specific technology type, if such a profile exists; and
(b) Require, if no NIAP-approved Protection Profile exists for a specific technology type
but a commercially provided information technology product relies on cryptographic
functionality to enforce its security policy, that the cryptographic module is FIPS-
validated or NSA-approved.
Discussion:  See [NIAP CCEVS] for additional information on NIAP. See [NIST CMVP
] for
additional information on FIPS-validated cryptographic modules.
Related Controls:  IA-7, SC-12, SC-13.
(8) ACQUISITION PROCESS | CONTINUOUS MONITORING PLAN FOR CONTROLS
Require the developer of the system, system component, or system service to produce a
plan for continuous monitoring of control effectiveness that is consistent with the
continuous monitoring program of the organization.
Discussion:  The objective of continuous monitoring plans is to determine if the planned,
required, and deployed controls within the system, system component, or system service
continue to be effective over time based on the inevitable changes that occur. Developer
continuous monitoring plans include a sufficient level of detail such that the information can
be incorporated into continuous monitoring programs implemented by organizations.
Continuous monitoring plans can include the types of control assessment and monitoring
CHAPTER THREE   PAGE 255
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
activities planned, frequency of control monitoring, and actions to be taken when controls
fail or become ineffective.
Related Controls:  CA-7.
(9) ACQUISITION PROCESS | FUNCTIONS, PORTS, PROTOCOLS, AND SERVICES IN USE
Require the developer of the system, system component, or system service to identify the
functions, ports, protocols, and services intended for organizational use.
Discussion:  The identification of functions, ports, protocols, and services early in the system
development life cycle (e.g., during the initial requirements definition and design stages)
allows organizations to influence the design of the system, system component, or system
service. This early involvement in the system development life cycle helps organizations
avoid or minimize the use of functions, ports, protocols, or services that pose unnecessarily
high risks and understand the trade-offs involved in blocking specific ports, protocols, or
services or requiring system service providers to do so. Early identification of functions,
ports, protocols, and services avoids costly retrofitting of controls after the system,
component, or system service has been implemented. SA-9 describes the requirements for
external system services. Organizations identify which functions, ports, protocols, and
services are provided from external sources.
Related Controls:  CM-7, SA-9.
(10) ACQUISITION PROCESS | USE OF APPROVED PIV PRODUCTS
Employ only information technology products on the FIPS 201-approved products list for
Personal Identity Verification (PIV) capability implemented within organizational systems.
Discussion:  Products on the FIPS 201-approved products list meet NIST requirements for
Personal Identity Verification (PIV) of Federal Employees and Contractors. PIV cards are used
for multi-factor authentication in systems and organizations.
Related Controls:  IA-2, IA-8, PM-9.
(11) ACQUISITION PROCESS | SYSTEM OF RECORDS
Include [Assignment: organization-defined Privacy Act requirements] in the acquisition
contract for the operation of a system of records on behalf of an organization to
accomplish an organizational mission or function.
Discussion: When, by contract, an organization provides for the operation of a system of
records to accomplish an organizational mission or function, the organization, consistent
with its authority, causes the requirements of the [PRIVACT] to be applied to the system of
records.
Related Controls:  PT-6.
(12) ACQUISITION PROCESS | DATA OWNERSHIP
(a) Include organizational data ownership requirements in the acquisition contract; and
(b) Require all data to be removed from the contractor’s system and returned to the
organization within [Assignment: organization-defined time frame].
Discussion: Contractors who operate a system that contains data owned by an organization
initiating the contract have policies and procedures in place to remove the data from their
systems and/or return the data in a time frame defined by the contract.
Related Controls:  None.
References:  [PRIVACT], [OMB A-130], [ISO 15408-1], [ISO 15408-2], [ISO 15408-3], [ISO 29148],
[FIPS 140-3], [FIPS 201-2], [SP 800-35], [SP 800-37], [SP 800-70], [SP 800-73-4], [SP 800-137], [SP
800-160-1], [SP 800-161], [IR 7539], [IR 7622], [IR 7676], [IR 7870], [IR 8062], [NIAP CCEVS], [NSA
CSFC].
CHAPTER THREE   PAGE 256
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
