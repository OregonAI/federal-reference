---
schema_version: 1
corpus: federal-reference
jurisdiction: us
id: nist-sp-800-53-r5.pl-2
title: NIST SP 800-53 Rev. 5 PL-2 — SYSTEM SECURITY AND PRIVACY PLANS
doc_type: federal_instrument
citation: NIST SP 800-53 Rev. 5 PL-2
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

**NIST SP 800-53 Rev. 5 PL-2** — SYSTEM SECURITY AND PRIVACY PLANS

- Issued by: National Institute of Standards and Technology
- Publication: NIST SP 800-53 Rev. 5 — Security and Privacy Controls for Information Systems and Organizations ([nist-sp-800-53-r5](./nist-sp-800-53-r5.md))
- Version: Rev. 5 (September 2020, includes updates as of 2020-12-10)
- Text as of: 2026-11-12
- Cited by held documents: 34 times (cjis-sp-6-1 ×30, irs-pub-1075-11-2021 ×3, 6-cfr-37 ×1)
- Reproduction basis: 17 U.S.C. § 105 — work of the U.S. government (NIST). Determined per document on 2026-11-12 against the publication itself, not assumed from its issuer: its Authority statement (PDF page 3) reads "This publication may be used by nongovernmental organizations on a voluntary basis and is not subject to copyright in the United States. Attribution would, however, be appreciated by NIST." Held here: the front matter and Chapter Three (the control catalog) only. Chapter Three names ISO/IEC standards solely as bibliographic references and reproduces none of their text. NOT mirrored: the References bibliography and Appendices A-C; Appendix A (glossary) adapts third-party definitions (ISO/IEC 15026, ISO 25237, ISO/IEC 29100, ISO 15288, IETF RFC 4949), which ADR-0002 treats as not reproducible by being incorporated, and whose reproducibility has not been determined.


_NON-AUTHORITATIVE copy of one control, cut from the SP 800-53 Rev. 5 snapshot this corpus holds. Whether and how this binds a given agency depends on the instrument that incorporates it — read it at the source URL before relying on it. This copy is the Rev. 5 text of record, which is not necessarily the text a citing document meant (a document citing Rev. 4 is not answered by it)._


## Full text

### PL-2 SYSTEM SECURITY AND PRIVACY PLANS
Control:
a. Develop security and privacy plans for the system that:
1. Are consistent with the organization’s enterprise architecture;
2. Explicitly define the constituent system components;
3. Describe the operational context of the system in terms of mission and business
processes;
4. Identify the individuals that fulfill system roles and responsibilities;
5. Identify the information types processed, stored, and transmitted by the system;
6. Provide the security categorization of the system, including supporting rationale;
7. Describe any specific threats to the system that are of concern to the organization;
8. Provide the results of a privacy risk assessment for systems processing personally
identifiable information;
9. Describe the operational environment for the system and any dependencies on or
connections to other systems or system components;
10. Provide an overview of the security and privacy requirements for the system;
11. Identify any relevant control baselines or overlays, if applicable;
12. Describe the controls in place or planned for meeting the security and privacy
requirements, including a rationale for any tailoring decisions;
13. Include risk determinations for security and privacy architecture and design decisions;
14. Include security- and privacy-related activities affecting the system that require planning
and coordination with [Assignment: organization-defined individuals or groups]; and
15. Are reviewed and approved by the authorizing official or designated representative
prior to plan implementation.
b. Distribute copies of the plans and communicate subsequent changes to the plans to
[Assignment: organization-defined personnel or roles];
c. Review the plans [Assignment: organization-defined frequency];
d. Update the plans to address changes to the system and environment of operation or
problems identified during plan implementation or control assessments; and
e. Protect the plans from unauthorized disclosure and modification.
Discussion:  System security and privacy plans are scoped to the system and system components
within the defined authorization boundary and contain an overview of the security and privacy
requirements for the system and the controls selected to satisfy the requirements. The plans
describe the intended application of each selected control in the context of the system with a
sufficient level of detail to correctly implement the control and to subsequently assess the
effectiveness of the control. The control documentation describes how system-specific and
hybrid controls are implemented and the plans and expectations regarding the functionality of
the system. System security and privacy plans can also be used in the design and development of
systems in support of life cycle-based security and privacy engineering processes. System security
and privacy plans are living documents that are updated and adapted throughout the system
development life cycle (e.g., during capability determination, analysis of alternatives, requests for
proposal, and design reviews).
Section 2.1 describes the different types of requirements that are
CHAPTER THREE   PAGE 196
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
relevant to organizations during the system development life cycle and the relationship between
requirements and controls.
Organizations may develop a single, integrated security and privacy plan or maintain separate
plans. Security and privacy plans relate security and privacy requirements to a set of controls and
control enhancements. The plans describe how the controls and control enhancements meet the
security and privacy requirements but do not provide detailed, technical descriptions of the
design or implementation of the controls and control enhancements. Security and privacy plans
contain sufficient information (including specifications of control parameter values for selection
and assignment operations explicitly or by reference) to enable a design and implementation
that is unambiguously compliant with the intent of the plans and subsequent determinations of
risk to organizational operations and assets, individuals, other organizations, and the Nation if
the plan is implemented.
Security and privacy plans need not be single documents. The plans can be a collection of various
documents, including documents that already exist. Effective security and privacy plans make
extensive use of references to policies, procedures, and additional documents, including design
and implementation specifications where more detailed information can be obtained. The use of
references helps reduce the documentation associated with security and privacy programs and
maintains the security- and privacy-related information in other established management and
operational areas, including enterprise architecture, system development life cycle, systems
engineering, and acquisition. Security and privacy plans need not contain detailed contingency
plan or incident response plan information but can instead provide—explicitly or by reference—
sufficient information to define what needs to be accomplished by those plans.
Security- and privacy-related activities that may require coordination and planning with other
individuals or groups within the organization include assessments, audits, inspections, hardware
and software maintenance, acquisition and supply chain risk management, patch management,
and contingency plan testing. Planning and coordination include emergency and nonemergency
(i.e., planned or non-urgent unplanned) situations. The process defined by organizations to plan
and coordinate security- and privacy-related activities can also be included in other documents,
as appropriate.
Related Controls:  AC-2, AC-6, AC-14, AC-17, AC-20, CA-2, CA-3, CA-7, CM-9, CM-13, CP-2, CP-4,
IR-4, IR-8, MA-4, MA-5, MP-4, MP-5, PL-7, PL-8, PL-10, PL-11, PM-1, PM-7, PM-8, PM-9, PM-10,
PM-11, RA-3, RA-8, RA-9, SA-5, SA-17, SA-22, SI-12, SR-2, SR-4.
Control Enhancements:
(1) SYSTEM SECURITY AND PRIVACY PLANS | CONCEPT OF OPERATIONS
[Withdrawn: Incorporated into PL-7.]
(2) SYSTEM SECURITY AND PRIVACY PLANS | FUNCTIONAL ARCHITECTURE
[Withdrawn: Incorporated into PL-8.]
(3) SYSTEM SECURITY AND PRIVACY PLANS | PLAN AND COORDINATE WITH OTHER ORGANIZATIONAL
ENTITIES
[Withdrawn: Incorporated into PL-2.]
References:  [OMB A-130], [SP 800-18], [SP 800-37], [SP 800-160-1], [SP 800-160-2].
