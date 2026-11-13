---
schema_version: 1
corpus: federal-reference
jurisdiction: us
id: nist-sp-800-53-r5.pm-1
title: NIST SP 800-53 Rev. 5 PM-1 — INFORMATION SECURITY PROGRAM PLAN
doc_type: federal_instrument
citation: NIST SP 800-53 Rev. 5 PM-1
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

**NIST SP 800-53 Rev. 5 PM-1** — INFORMATION SECURITY PROGRAM PLAN

- Issued by: National Institute of Standards and Technology
- Publication: NIST SP 800-53 Rev. 5 — Security and Privacy Controls for Information Systems and Organizations ([nist-sp-800-53-r5](./nist-sp-800-53-r5.md))
- Version: Rev. 5 (September 2020, includes updates as of 2020-12-10)
- Text as of: 2026-11-12
- Cited by held documents: 5 times (irs-pub-1075-11-2021 ×3, 6-cfr-37 ×1, arc-ampe ×1)
- Reproduction basis: 17 U.S.C. § 105 — work of the U.S. government (NIST). Determined per document on 2026-11-12 against the publication itself, not assumed from its issuer: its Authority statement (PDF page 3) reads "This publication may be used by nongovernmental organizations on a voluntary basis and is not subject to copyright in the United States. Attribution would, however, be appreciated by NIST." Held here: the front matter and Chapter Three (the control catalog) only. Chapter Three names ISO/IEC standards solely as bibliographic references and reproduces none of their text. NOT mirrored: the References bibliography and Appendices A-C; Appendix A (glossary) adapts third-party definitions (ISO/IEC 15026, ISO 25237, ISO/IEC 29100, ISO 15288, IETF RFC 4949), which ADR-0002 treats as not reproducible by being incorporated, and whose reproducibility has not been determined.


_NON-AUTHORITATIVE copy of one control, cut from the SP 800-53 Rev. 5 snapshot this corpus holds. Whether and how this binds a given agency depends on the instrument that incorporates it — read it at the source URL before relying on it. This copy is the Rev. 5 text of record, which is not necessarily the text a citing document meant (a document citing Rev. 4 is not answered by it)._


> **Release 5.2.0 postdates this text.** NIST's listing of record ([https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final)) says that on 2025-08-27 it issued release 5.2.0 of SP 800-53, which updates the related controls for this control. The text below is the Rev. 5 PDF of record and does NOT include that change; read NIST's own list of the changes ([summary](https://csrc.nist.gov/files/projects/Risk-Management/800-53%20Comment%20Site/SP800-53-r5.2.0-changes.pdf)) before relying on this control's text.


## Full text

### PM-1 INFORMATION SECURITY PROGRAM PLAN
Control:
a. Develop and disseminate an organization-wide information security program plan that:
1. Provides an overview of the requirements for the security program and a description of
the security program management controls and common controls in place or planned
for meeting those requirements;
2. Includes the identification and assignment of roles, responsibilities, management
commitment, coordination among organizational entities, and compliance;
3. Reflects the coordination among organizational entities responsible for information
security; and
4. Is approved by a senior official with responsibility and accountability for the risk being
incurred to organizational operations (including mission, functions, image, and
reputation), organizational assets, individuals, other organizations, and the Nation;
b. Review and update the organization-wide information security program plan [Assignment:
organization-defined frequency] and following [Assignment: organization-defined events];
and
c. Protect the information security program plan from unauthorized disclosure and
modification.
Discussion:  An information security program plan is a formal document that provides an
overview of the security requirements for an organization-wide information security program
PROGRAM MANAGEMENT CONTROLS
[FISMA], [ PRIVACT], and [ OMB A -130] require federal agencies to develop, implement, and
provide oversight for organization-wide information security and privacy p rograms to help
ensure the confidentiality, integrity, and availability of federal information processed, stored,
and transmitted by federal information systems and to protect individual privacy. The program
management (PM) controls described in this section are implemented at the organization level
and not direct ed at individual information  systems. The PM  controls have been designed to
facilitate organizational compliance with applicable federal laws, e xecutive orders, directives,
policies, regulations, and standards. The controls are independent of [ FIPS 200] impact levels
and, therefore, are not associated with the control baselines described in [SP 800-53B].
Organizations document program management controls in the information security and privacy
program plans. The organization-wide information security program plan (see PM-1) and privacy
program plan (see PM-18) supplement system security and privacy plans (see PL-2) developed
for organizational information systems. Together, the system security and privacy plans for the
individual information systems and the information security and privacy program  plans cover
the totality of security and privacy controls employed by the organization.
CHAPTER THREE    PAGE 204
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
and describes the program management controls and common controls in place or planned for
meeting those requirements. An information security program plan can be represented in a
single document or compilations of documents. Privacy program plans and supply chain risk
management plans are addressed separately in PM-18 and SR-2, respectively.
An information security program plan documents implementation details about program
management and common controls. The plan provides sufficient information about the controls
(including specification of parameters for assignment and selection operations, explicitly or by
reference) to enable implementations that are unambiguously compliant with the intent of the
plan and a determination of the risk to be incurred if the plan is implemented as intended.
Updates to information security program plans include organizational changes and problems
identified during plan implementation or control assessments.
Program management controls may be implemented at the organization level or the mission or
business process level, and are essential for managing the organization’s information security
program. Program management controls are distinct from common, system-specific, and hybrid
controls because program management controls are independent of any particular system.
Together, the individual system security plans and the organization-wide information security
program plan provide complete coverage for the security controls employed within the
organization.
Common controls available for inheritance by organizational systems are documented in an
appendix to the organization’s information security program plan unless the controls are
included in a separate security plan for a system. The organization-wide information security
program plan indicates which separate security plans contain descriptions of common controls.
Events that may precipitate an update to the information security program plan include, but are
not limited to, organization-wide assessment or audit findings, security incidents or breaches, or
changes in laws, executive orders, directives, regulations, policies, standards, and guidelines.
Related Controls:  PL-2, PM-18, PM-30, RA-9, SI-12, SR-2.
Control Enhancements:  None.
References:  [FISMA], [OMB A-130], [SP 800-37], [SP 800-39].
