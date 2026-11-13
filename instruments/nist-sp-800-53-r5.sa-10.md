---
schema_version: 1
corpus: federal-reference
jurisdiction: us
id: nist-sp-800-53-r5.sa-10
title: NIST SP 800-53 Rev. 5 SA-10 — DEVELOPER CONFIGURATION MANAGEMENT
doc_type: federal_instrument
citation: NIST SP 800-53 Rev. 5 SA-10
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

**NIST SP 800-53 Rev. 5 SA-10** — DEVELOPER CONFIGURATION MANAGEMENT

- Issued by: National Institute of Standards and Technology
- Publication: NIST SP 800-53 Rev. 5 — Security and Privacy Controls for Information Systems and Organizations ([nist-sp-800-53-r5](./nist-sp-800-53-r5.md))
- Version: Rev. 5 (September 2020, includes updates as of 2020-12-10)
- Text as of: 2026-11-12
- Cited by held documents: 23 times (cjis-sp-6-1 ×17, irs-pub-1075-11-2021 ×3, arc-ampe ×2, 6-cfr-37 ×1)
- Reproduction basis: 17 U.S.C. § 105 — work of the U.S. government (NIST). Determined per document on 2026-11-12 against the publication itself, not assumed from its issuer: its Authority statement (PDF page 3) reads "This publication may be used by nongovernmental organizations on a voluntary basis and is not subject to copyright in the United States. Attribution would, however, be appreciated by NIST." Held here: the front matter and Chapter Three (the control catalog) only. Chapter Three names ISO/IEC standards solely as bibliographic references and reproduces none of their text. NOT mirrored: the References bibliography and Appendices A-C; Appendix A (glossary) adapts third-party definitions (ISO/IEC 15026, ISO 25237, ISO/IEC 29100, ISO 15288, IETF RFC 4949), which ADR-0002 treats as not reproducible by being incorporated, and whose reproducibility has not been determined.


_NON-AUTHORITATIVE copy of one control, cut from the SP 800-53 Rev. 5 snapshot this corpus holds. Whether and how this binds a given agency depends on the instrument that incorporates it — read it at the source URL before relying on it. This copy is the Rev. 5 text of record, which is not necessarily the text a citing document meant (a document citing Rev. 4 is not answered by it)._


## Full text

### SA-10 DEVELOPER CONFIGURATION MANAGEMENT
Control:  Require the developer of the system, system component, or system service to:
a. Perform configuration management during system, component, or service [Selection (one or
more): design; development; implementation; operation; disposal];
b. Document, manage, and control the integrity of changes to [Assignment: organization-
defined configuration items under configuration management];
c. Implement only organization-approved changes to the system, component, or service;
CHAPTER THREE   PAGE 274
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
d. Document approved changes to the system, component, or service and the potential
security and privacy impacts of such changes; and
e. Track security flaws and flaw resolution within the system, component, or service and report
findings to [Assignment: organization-defined personnel].
Discussion:  Organizations consider the quality and completeness of configuration management
activities conducted by developers as direct evidence of applying effective security controls.
Controls include protecting the master copies of material used to generate security-relevant
portions of the system hardware, software, and firmware from unauthorized modification or
destruction. Maintaining the integrity of changes to the system, system component, or system
service requires strict configuration control throughout the system development life cycle to
track authorized changes and prevent unauthorized changes.
The configuration items that are placed under configuration management include the formal
model; the functional, high-level, and low-level design specifications; other design data;
implementation documentation; source code and hardware schematics; the current running
version of the object code; tools for comparing new versions of security-relevant hardware
descriptions and source code with previous versions; and test fixtures and documentation.
Depending on the mission and business needs of organizations and the nature of the contractual
relationships in place, developers may provide configuration management support during the
operations and maintenance stage of the system development life cycle.
Related Controls:  CM-2, CM-3, CM-4, CM-7, CM-9, SA-4, SA-5, SA-8, SA-15, SI-2, SR-3, SR-4, SR-5,
SR-6.
Control Enhancements:
(1) DEVELOPER CONFIGURATION MANAGEMENT | SOFTWARE AND FIRMWARE INTEGRITY VERIFICATION
Require the developer of the system, system component, or system service to enable
integrity verification of software and firmware components.
Discussion:  Software and firmware integrity verification allows organizations to detect
unauthorized changes to software and firmware components using developer-provided
tools, techniques, and mechanisms. The integrity checking mechanisms can also address
counterfeiting of software and firmware components. Organizations verify the integrity of
software and firmware components, for example, through secure one-way hashes provided
by developers. Delivered software and firmware components also include any updates to
such components.
Related Controls:  SI-7, SR-11.
(2) DEVELOPER CONFIGURATION MANAGEMENT | ALTERNATIVE CONFIGURATION MANAGEMENT
PROCESSES
Provide an alternate configuration management process using organizational personnel in
the absence of a dedicated developer configuration management team.
Discussion:  Alternate configuration management processes may be required when
organizations use commercial off-the-shelf information technology products. Alternate
configuration management processes include organizational personnel who review and
approve proposed changes to systems, system components, and system services and
conduct security and privacy impact analyses prior to the implementation of changes to
systems, components, or services.
Related Controls:  None.
(3) DEVELOPER CONFIGURATION MANAGEMENT | HARDWARE INTEGRITY VERIFICATION
Require the developer of the system, system component, or system service to enable
integrity verification of hardware components.
CHAPTER THREE   PAGE 275
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
Discussion:  Hardware integrity verification allows organizations to detect unauthorized
changes to hardware components using developer-provided tools, techniques, methods, and
mechanisms. Organizations may verify the integrity of hardware components with hard-to-
copy labels, verifiable serial numbers provided by developers, and by requiring the use of
anti-tamper technologies. Delivered hardware components also include hardware and
firmware updates to such components.
Related Controls:  SI-7.
(4) DEVELOPER CONFIGURATION MANAGEMENT | TRUSTED GENERATION
Require the developer of the system, system component, or system service to employ
tools for comparing newly generated versions of security-relevant hardware descriptions,
source code, and object code with previous versions.
Discussion:  The trusted generation of descriptions, source code, and object code addresses
authorized changes to hardware, software, and firmware components between versions
during development. The focus is on the efficacy of the configuration management process
by the developer to ensure that newly generated versions of security-relevant hardware
descriptions, source code, and object code continue to enforce the security policy for the
system, system component, or system service. In contrast,
SA-10(1) and SA-10(3) allow
organizations to detect unauthorized changes to hardware, software, and firmware
components using tools, techniques, or mechanisms provided by developers.
Related Controls:  None.
(5) DEVELOPER CONFIGURATION MANAGEMENT | MAPPING INTEGRITY FOR VERSION CONTROL
Require the developer of the system, system component, or system service to maintain
the integrity of the mapping between the master build data describing the current version
of security-relevant hardware, software, and firmware and the on-site master copy of the
data for the current version.
Discussion:  Mapping integrity for version control addresses changes to hardware, software,
and firmware components during both initial development and system development life
cycle updates. Maintaining the integrity between the master copies of security-relevant
hardware, software, and firmware (including designs, hardware drawings, source code) and
the equivalent data in master copies in operational environments is essential to ensuring the
availability of organizational systems that support critical mission and business functions.
Related Controls:  None.
(6) DEVELOPER CONFIGURATION MANAGEMENT | TRUSTED DISTRIBUTION
Require the developer of the system, system component, or system service to execute
procedures for ensuring that security-relevant hardware, software, and firmware updates
distributed to the organization are exactly as specified by the master copies.
Discussion:  The trusted distribution of security-relevant hardware, software, and firmware
updates help to ensure that the updates are correct representations of the master copies
maintained by the developer and have not been tampered with during distribution.
Related Controls:  None.
(7) DEVELOPER CONFIGURATION MANAGEMENT | SECURITY AND PRIVACY REPRESENTATIVES
Require [Assignment: organization-defined security and privacy representatives] to be
included in the [Assignment: organization-defined configuration change management and
control process].
Discussion: Information security and privacy representatives can include system security
officers, senior agency information security officers, senior agency officials for privacy, and
system privacy officers. Representation by personnel with information security and privacy
CHAPTER THREE   PAGE 276
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
expertise is important because changes to system configurations can have unintended side
effects, some of which may be security- or privacy-relevant. Detecting such changes early in
the process can help avoid unintended, negative consequences that could ultimately affect
the security and privacy posture of systems. The configuration change management and
control process in this control enhancement refers to the change management and control
process defined by organizations in SA-10b.
Related Controls:  None.
References:  [FIPS 140-3], [FIPS 180-4], [FIPS 202], [SP 800-128], [SP 800-160-1].
