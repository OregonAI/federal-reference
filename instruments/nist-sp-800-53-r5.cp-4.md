---
schema_version: 1
corpus: federal-reference
jurisdiction: us
id: nist-sp-800-53-r5.cp-4
title: NIST SP 800-53 Rev. 5 CP-4 — CONTINGENCY PLAN TESTING
doc_type: federal_instrument
citation: NIST SP 800-53 Rev. 5 CP-4
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

**NIST SP 800-53 Rev. 5 CP-4** — CONTINGENCY PLAN TESTING

- Issued by: National Institute of Standards and Technology
- Publication: NIST SP 800-53 Rev. 5 — Security and Privacy Controls for Information Systems and Organizations ([nist-sp-800-53-r5](./nist-sp-800-53-r5.md))
- Version: Rev. 5 (September 2020, includes updates as of 2020-12-10)
- Text as of: 2026-11-12
- Cited by held documents: 19 times (cjis-sp-6-1 ×13, irs-pub-1075-11-2021 ×3, 6-cfr-37 ×2, arc-ampe ×1)
- Reproduction basis: 17 U.S.C. § 105 — work of the U.S. government (NIST). Determined per document on 2026-11-12 against the publication itself, not assumed from its issuer: its Authority statement (PDF page 3) reads "This publication may be used by nongovernmental organizations on a voluntary basis and is not subject to copyright in the United States. Attribution would, however, be appreciated by NIST." Held here: the front matter and Chapter Three (the control catalog) only. Chapter Three names ISO/IEC standards solely as bibliographic references and reproduces none of their text. NOT mirrored: the References bibliography and Appendices A-C; Appendix A (glossary) adapts third-party definitions (ISO/IEC 15026, ISO 25237, ISO/IEC 29100, ISO 15288, IETF RFC 4949), which ADR-0002 treats as not reproducible by being incorporated, and whose reproducibility has not been determined.


_NON-AUTHORITATIVE copy of one control, cut from the SP 800-53 Rev. 5 snapshot this corpus holds. Whether and how this binds a given agency depends on the instrument that incorporates it — read it at the source URL before relying on it. This copy is the Rev. 5 text of record, which is not necessarily the text a citing document meant (a document citing Rev. 4 is not answered by it)._


## Full text

### CP-4 CONTINGENCY PLAN TESTING
Control:
a. Test the contingency plan for the system [Assignment: organization-defined frequency] using
the following tests to determine the effectiveness of the plan and the readiness to execute
the plan: [Assignment: organization-defined tests].
b. Review the contingency plan test results; and
CHAPTER THREE   PAGE 120
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
c. Initiate corrective actions, if needed.
Discussion:  Methods for testing contingency plans to determine the effectiveness of the plans
and identify potential weaknesses include checklists, walk-through and tabletop exercises,
simulations (parallel or full interrupt), and comprehensive exercises. Organizations conduct
testing based on the requirements in contingency plans and include a determination of the
effects on organizational operations, assets, and individuals due to contingency operations.
Organizations have flexibility and discretion in the breadth, depth, and timelines of corrective
actions.
Related Controls:  AT-3, CP-2, CP-3, CP-8, CP-9, IR-3, IR-4, PL-2, PM-14, SR-2.
Control Enhancements:
(1) CONTINGENCY PLAN TESTING | COORDINATE WITH RELATED PLANS
Coordinate contingency plan testing with organizational elements responsible for related
plans.
Discussion:  Plans related to contingency planning for organizational systems include
Business Continuity Plans, Disaster Recovery Plans, Continuity of Operations Plans, Crisis
Communications Plans, Critical Infrastructure Plans, Cyber Incident Response Plans, and
Occupant Emergency Plans. Coordination of contingency plan testing does not require
organizations to create organizational elements to handle related plans or to align such
elements with specific plans. However, it does require that if such organizational elements
are responsible for related plans, organizations coordinate with those elements.
Related Controls:  IR-8, PM-8.
(2) CONTINGENCY PLAN TESTING | ALTERNATE PROCESSING SITE
Test the contingency plan at the alternate processing site:
(a) To familiarize contingency personnel with the facility and available resources; and
(b) To evaluate the capabilities of the alternate processing site to support contingency
operations.
Discussion:  Conditions at the alternate processing site may be significantly different than
the conditions at the primary site. Having the opportunity to visit the alternate site and
experience the actual capabilities available at the site can provide valuable information on
potential vulnerabilities that could affect essential organizational mission and business
functions. The on-site visit can also provide an opportunity to refine the contingency plan to
address the vulnerabilities discovered during testing.
Related Controls:  CP-7.
(3) CONTINGENCY PLAN TESTING | AUTOMATED TESTING
Test the contingency plan using [Assignment: organization-defined automated
mechanisms].
Discussion:  Automated mechanisms facilitate thorough and effective testing of contingency
plans by providing more complete coverage of contingency issues, selecting more realistic
test scenarios and environments, and effectively stressing the system and supported mission
and business functions.
Related Controls:  None.
(4) CONTINGENCY PLAN TESTING | FULL RECOVERY AND RECONSTITUTION
Include a full recovery and reconstitution of the system to a known state as part of
contingency plan testing.
Discussion:  Recovery is executing contingency plan activities to restore organizational
mission and business functions. Reconstitution takes place following recovery and includes
CHAPTER THREE   PAGE 121
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
activities for returning systems to fully operational states. Organizations establish a known
state for systems that includes system state information for hardware, software programs,
and data. Preserving system state information facilitates system restart and return to the
operational mode of organizations with less disruption of mission and business processes.
Related Controls:  CP-10, SC-24.
(5) CONTINGENCY PLAN TESTING | SELF-CHALLENGE
Employ [Assignment: organization-defined mechanisms] to [Assignment: organization-
defined system or system component] to disrupt and adversely affect the system or system
component.
Discussion:  Often, the best method of assessing system resilience is to disrupt the system in
some manner. The mechanisms used by the organization could disrupt system functions or
system services in many ways, including terminating or disabling critical system components,
changing the configuration of system components, degrading critical functionality (e.g.,
restricting network bandwidth), or altering privileges. Automated, on-going, and simulated
cyber-attacks and service disruptions can reveal unexpected functional dependencies and
help the organization determine its ability to ensure resilience in the face of an actual cyber-
attack.
Related Controls:  None.
References:  [FIPS 199], [SP 800-34], [SP 800-84], [SP 800-160-2].
