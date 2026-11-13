---
schema_version: 1
corpus: federal-reference
jurisdiction: us
id: nist-sp-800-53-r5.cm-2
title: NIST SP 800-53 Rev. 5 CM-2 — BASELINE CONFIGURATION
doc_type: federal_instrument
citation: NIST SP 800-53 Rev. 5 CM-2
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

**NIST SP 800-53 Rev. 5 CM-2** — BASELINE CONFIGURATION

- Issued by: National Institute of Standards and Technology
- Publication: NIST SP 800-53 Rev. 5 — Security and Privacy Controls for Information Systems and Organizations ([nist-sp-800-53-r5](./nist-sp-800-53-r5.md))
- Version: Rev. 5 (September 2020, includes updates as of 2020-12-10)
- Text as of: 2026-11-12
- Cited by held documents: 36 times (cjis-sp-6-1 ×24, arc-ampe ×8, irs-pub-1075-11-2021 ×3, 6-cfr-37 ×1), 2 of them naming an enhancement of this control
- Reproduction basis: 17 U.S.C. § 105 — work of the U.S. government (NIST). Determined per document on 2026-11-12 against the publication itself, not assumed from its issuer: its Authority statement (PDF page 3) reads "This publication may be used by nongovernmental organizations on a voluntary basis and is not subject to copyright in the United States. Attribution would, however, be appreciated by NIST." Held here: the front matter and Chapter Three (the control catalog) only. Chapter Three names ISO/IEC standards solely as bibliographic references and reproduces none of their text. NOT mirrored: the References bibliography and Appendices A-C; Appendix A (glossary) adapts third-party definitions (ISO/IEC 15026, ISO 25237, ISO/IEC 29100, ISO 15288, IETF RFC 4949), which ADR-0002 treats as not reproducible by being incorporated, and whose reproducibility has not been determined.


_NON-AUTHORITATIVE copy of one control, cut from the SP 800-53 Rev. 5 snapshot this corpus holds. Whether and how this binds a given agency depends on the instrument that incorporates it — read it at the source URL before relying on it. This copy is the Rev. 5 text of record, which is not necessarily the text a citing document meant (a document citing Rev. 4 is not answered by it)._


## Full text

### CM-2 BASELINE CONFIGURATION
Control:
a. Develop, document, and maintain under configuration control, a current baseline
configuration of the system; and
b. Review and update the baseline configuration of the system:
1. [Assignment: organization-defined frequency];
2. When required due to [Assignment: organization-defined circumstances]; and
3. When system components are installed or upgraded.
Discussion:  Baseline configurations for systems and system components include connectivity,
operational, and communications aspects of systems. Baseline configurations are documented,
formally reviewed, and agreed-upon specifications for systems or configuration items within
those systems. Baseline configurations serve as a basis for future builds, releases, or changes to
systems and include security and privacy control implementations, operational procedures,
information about system components, network topology, and logical placement of components
in the system architecture. Maintaining baseline configurations requires creating new baselines
as organizational systems change over time. Baseline configurations of systems reflect the
current enterprise architecture.
Related Controls:  AC-19, AU-6, CA-9, CM-1, CM-3, CM-5, CM-6, CM-8, CM-9, CP-9, CP-10, CP-12,
MA-2, PL-8, PM-5, SA-8, SA-10, SA-15, SC-18.
Control Enhancements:
(1) BASELINE CONFIGURATION | REVIEWS AND UPDATES
[Withdrawn: Incorporated into CM-2.]
(2) BASELINE CONFIGURATION | AUTOMATION SUPPORT FOR ACCURACY AND CURRENCY
Maintain the currency, completeness, accuracy, and availability of the baseline
configuration of the system using [Assignment: organization-defined automated
mechanisms].
Discussion:  Automated mechanisms that help organizations maintain consistent baseline
configurations for systems include configuration management tools, hardware, software,
firmware inventory tools, and network management tools. Automated tools can be used at
the organization level, mission and business process level, or system level on workstations,
servers, notebook computers, network components, or mobile devices. Tools can be used to
track version numbers on operating systems, applications, types of software installed, and
current patch levels. Automation support for accuracy and currency can be satisfied by the
implementation of
CM-8(2) for organizations that combine system component inventory and
baseline configuration activities.
Related Controls:  CM-7, IA-3, RA-5.
(3) BASELINE CONFIGURATION | RETENTION OF PREVIOUS CONFIGURATIONS
Retain [Assignment: organization-defined number] of previous versions of baseline
configurations of the system to support rollback.
Discussion:  Retaining previous versions of baseline configurations to support rollback
include hardware, software, firmware, configuration files, configuration records, and
associated documentation.
Related Controls:  None.
(4) BASELINE CONFIGURATION | UNAUTHORIZED SOFTWARE
CHAPTER THREE   PAGE 98
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
[Withdrawn: Incorporated into CM-7(4).]
(5) BASELINE CONFIGURATION | AUTHORIZED SOFTWARE
[Withdrawn: Incorporated into CM-7(5).]
(6) BASELINE CONFIGURATION | DEVELOPMENT AND TEST ENVIRONMENTS
Maintain a baseline configuration for system development and test environments that is
managed separately from the operational baseline configuration.
Discussion:  Establishing separate baseline configurations for development, testing, and
operational environments protects systems from unplanned or unexpected events related to
development and testing activities. Separate baseline configurations allow organizations to
apply the configuration management that is most appropriate for each type of configuration.
For example, the management of operational configurations typically emphasizes the need
for stability, while the management of development or test configurations requires greater
flexibility. Configurations in the test environment mirror configurations in the operational
environment to the extent practicable so that the results of the testing are representative of
the proposed changes to the operational systems. Separate baseline configurations do not
necessarily require separate physical environments.
Related Controls:  CM-4, SC-3, SC-7.
(7) BASELINE CONFIGURATION | CONFIGURE SYSTEMS AND COMPONENTS FOR HIGH-RISK AREAS
(a) Issue [Assignment: organization-defined systems or system components] with
[Assignment: organization-defined configurations] to individuals traveling to locations
that the organization deems to be of significant risk; and
(b) Apply the following controls to the systems or components when the individuals
return from travel: [Assignment: organization-defined controls].
Discussion:  When it is known that systems or system components will be in high-risk areas
external to the organization, additional controls may be implemented to counter the
increased threat in such areas. For example, organizations can take actions for notebook
computers used by individuals departing on and returning from travel. Actions include
determining the locations that are of concern, defining the required configurations for the
components, ensuring that components are configured as intended before travel is initiated,
and applying controls to the components after travel is completed. Specially configured
notebook computers include computers with sanitized hard drives, limited applications, and
more stringent configuration settings. Controls applied to mobile devices upon return from
travel include examining the mobile device for signs of physical tampering and purging and
reimaging disk drives. Protecting information that resides on mobile devices is addressed in
the MP (Media Protection) family.
Related Controls:  MP-4, MP-5.
References:  [SP 800-124], [SP 800-128].
