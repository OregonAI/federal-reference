---
schema_version: 1
corpus: federal-reference
jurisdiction: us
id: nist-sp-800-53-r5.cm-9
title: NIST SP 800-53 Rev. 5 CM-9 — CONFIGURATION MANAGEMENT PLAN
doc_type: federal_instrument
citation: NIST SP 800-53 Rev. 5 CM-9
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

**NIST SP 800-53 Rev. 5 CM-9** — CONFIGURATION MANAGEMENT PLAN

- Issued by: National Institute of Standards and Technology
- Publication: NIST SP 800-53 Rev. 5 — Security and Privacy Controls for Information Systems and Organizations ([nist-sp-800-53-r5](./nist-sp-800-53-r5.md))
- Version: Rev. 5 (September 2020, includes updates as of 2020-12-10)
- Text as of: 2026-11-12
- Cited by held documents: 20 times (cjis-sp-6-1 ×14, irs-pub-1075-11-2021 ×3, arc-ampe ×2, 6-cfr-37 ×1), 1 of them naming an enhancement of this control
- Reproduction basis: 17 U.S.C. § 105 — work of the U.S. government (NIST). Determined per document on 2026-11-12 against the publication itself, not assumed from its issuer: its Authority statement (PDF page 3) reads "This publication may be used by nongovernmental organizations on a voluntary basis and is not subject to copyright in the United States. Attribution would, however, be appreciated by NIST." Held here: the front matter and Chapter Three (the control catalog) only. Chapter Three names ISO/IEC standards solely as bibliographic references and reproduces none of their text. NOT mirrored: the References bibliography and Appendices A-C; Appendix A (glossary) adapts third-party definitions (ISO/IEC 15026, ISO 25237, ISO/IEC 29100, ISO 15288, IETF RFC 4949), which ADR-0002 treats as not reproducible by being incorporated, and whose reproducibility has not been determined.


_NON-AUTHORITATIVE copy of one control, cut from the SP 800-53 Rev. 5 snapshot this corpus holds. Whether and how this binds a given agency depends on the instrument that incorporates it — read it at the source URL before relying on it. This copy is the Rev. 5 text of record, which is not necessarily the text a citing document meant (a document citing Rev. 4 is not answered by it)._


## Full text

### CM-9 CONFIGURATION MANAGEMENT PLAN
Control:  Develop, document, and implement a configuration management plan for the system
that:
a. Addresses roles, responsibilities, and configuration management processes and procedures;
b. Establishes a process for identifying configuration items throughout the system
development life cycle and for managing the configuration of the configuration items;
c. Defines the configuration items for the system and places the configuration items under
configuration management;
d. Is reviewed and approved by [Assignment: organization-defined personnel or roles]; and
e. Protects the configuration management plan from unauthorized disclosure and
modification.
Discussion:  Configuration management activities occur throughout the system development life
cycle. As such, there are developmental configuration management activities (e.g., the control of
code and software libraries) and operational configuration management activities (e.g., control
of installed components and how the components are configured). Configuration management
plans satisfy the requirements in configuration management policies while being tailored to
CHAPTER THREE   PAGE 111
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
individual systems. Configuration management plans define processes and procedures for how
configuration management is used to support system development life cycle activities.
Configuration management plans are generated during the development and acquisition stage of
the system development life cycle. The plans describe how to advance changes through change
management processes; update configuration settings and baselines; maintain component
inventories; control development, test, and operational environments; and develop, release, and
update key documents.
Organizations can employ templates to help ensure the consistent and timely development and
implementation of configuration management plans. Templates can represent a configuration
management plan for the organization with subsets of the plan implemented on a system by
system basis. Configuration management approval processes include the designation of key
stakeholders responsible for reviewing and approving proposed changes to systems, and
personnel who conduct security and privacy impact analyses prior to the implementation of
changes to the systems. Configuration items are the system components, such as the hardware,
software, firmware, and documentation to be configuration-managed. As systems continue
through the system development life cycle, new configuration items may be identified, and some
existing configuration items may no longer need to be under configuration control.
Related Controls:  CM-2, CM-3, CM-4, CM-5, CM-8, PL-2, RA-8, SA-10, SI-12.
Control Enhancements:
(1) CONFIGURATION MANAGEMENT PLAN | ASSIGNMENT OF RESPONSIBILITY
Assign responsibility for developing the configuration management process to
organizational personnel that are not directly involved in system development.
Discussion: In the absence of dedicated configuration management teams assigned within
organizations, system developers may be tasked with developing configuration management
processes using personnel who are not directly involved in system development or system
integration. This separation of duties ensures that organizations establish and maintain a
sufficient degree of independence between the system development and integration
processes and configuration management processes to facilitate quality control and more
effective oversight.
Related Controls:  None.
References:  [SP 800-128].
