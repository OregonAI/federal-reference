---
schema_version: 1
corpus: federal-reference
jurisdiction: us
id: nist-sp-800-53-r5.cm-6
title: NIST SP 800-53 Rev. 5 CM-6 — CONFIGURATION SETTINGS
doc_type: federal_instrument
citation: NIST SP 800-53 Rev. 5 CM-6
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

**NIST SP 800-53 Rev. 5 CM-6** — CONFIGURATION SETTINGS

- Issued by: National Institute of Standards and Technology
- Publication: NIST SP 800-53 Rev. 5 — Security and Privacy Controls for Information Systems and Organizations ([nist-sp-800-53-r5](./nist-sp-800-53-r5.md))
- Version: Rev. 5 (September 2020, includes updates as of 2020-12-10)
- Text as of: 2026-11-12
- Cited by held documents: 42 times (cjis-sp-6-1 ×33, arc-ampe ×5, irs-pub-1075-11-2021 ×3, 6-cfr-37 ×1), 1 of them naming an enhancement of this control
- Reproduction basis: 17 U.S.C. § 105 — work of the U.S. government (NIST). Determined per document on 2026-11-12 against the publication itself, not assumed from its issuer: its Authority statement (PDF page 3) reads "This publication may be used by nongovernmental organizations on a voluntary basis and is not subject to copyright in the United States. Attribution would, however, be appreciated by NIST." Held here: the front matter and Chapter Three (the control catalog) only. Chapter Three names ISO/IEC standards solely as bibliographic references and reproduces none of their text. NOT mirrored: the References bibliography and Appendices A-C; Appendix A (glossary) adapts third-party definitions (ISO/IEC 15026, ISO 25237, ISO/IEC 29100, ISO 15288, IETF RFC 4949), which ADR-0002 treats as not reproducible by being incorporated, and whose reproducibility has not been determined.


_NON-AUTHORITATIVE copy of one control, cut from the SP 800-53 Rev. 5 snapshot this corpus holds. Whether and how this binds a given agency depends on the instrument that incorporates it — read it at the source URL before relying on it. This copy is the Rev. 5 text of record, which is not necessarily the text a citing document meant (a document citing Rev. 4 is not answered by it)._


## Full text

### CM-6 CONFIGURATION SETTINGS
Control:
a. Establish and document configuration settings for components employed within the system
that reflect the most restrictive mode consistent with operational requirements using
[Assignment: organization-defined common secure configurations];
b. Implement the configuration settings;
c. Identify, document, and approve any deviations from established configuration settings for
[Assignment: organization-defined system components] based on [Assignment: organization-
defined operational requirements]; and
d. Monitor and control changes to the configuration settings in accordance with organizational
policies and procedures.
Discussion:  Configuration settings are the parameters that can be changed in the hardware,
software, or firmware components of the system that affect the security and privacy posture or
functionality of the system. Information technology products for which configuration settings can
be defined include mainframe computers, servers, workstations, operating systems, mobile
devices, input/output devices, protocols, and applications. Parameters that impact the security
posture of systems include registry settings; account, file, or directory permission settings; and
settings for functions, protocols, ports, services, and remote connections. Privacy parameters are
parameters impacting the privacy posture of systems, including the parameters required to
satisfy other privacy controls. Privacy parameters include settings for access controls, data
processing preferences, and processing and retention permissions. Organizations establish
organization-wide configuration settings and subsequently derive specific configuration settings
for systems. The established settings become part of the configuration baseline for the system.
Common secure configurations (also known as security configuration checklists, lockdown and
hardening guides, and security reference guides) provide recognized, standardized, and
established benchmarks that stipulate secure configuration settings for information technology
CHAPTER THREE   PAGE 104
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
products and platforms as well as instructions for configuring those products or platforms to
meet operational requirements. Common secure configurations can be developed by a variety of
organizations, including information technology product developers, manufacturers, vendors,
federal agencies, consortia, academia, industry, and other organizations in the public and private
sectors.
Implementation of a common secure configuration may be mandated at the organization level,
mission and business process level, system level, or at a higher level, including by a regulatory
agency. Common secure configurations include the United States Government Configuration
Baseline [USGCB] and security technical implementation guides (STIGs), which affect the
implementation of CM-6 and other controls such as AC-19 and CM-7. The Security Content
Automation Protocol (SCAP) and the defined standards within the protocol provide an effective
method to uniquely identify, track, and control configuration settings.
Related Controls:  AC-3, AC-19, AU-2, AU-6, CA-9, CM-2, CM-3, CM-5, CM-7, CM-11, CP-7, CP-9,
CP-10, IA-3, IA-5, PL-8, PL-9, RA-5, SA-4, SA-5, SA-8, SA-9, SC-18, SC-28, SC-43, SI-2, SI-4, SI-6.
Control Enhancements:
(1) CONFIGURATION SETTINGS | AUTOMATED MANAGEMENT, APPLICATION, AND VERIFICATION
Manage, apply, and verify configuration settings for [Assignment: organization-defined
system components] using [Assignment: organization-defined automated mechanisms].
Discussion:  Automated tools (e.g., hardening tools, baseline configuration tools) can
improve the accuracy, consistency, and availability of configuration settings information.
Automation can also provide data aggregation and data correlation capabilities, alerting
mechanisms, and dashboards to support risk-based decision-making within the organization.
Related Controls:  CA-7.
(2) CONFIGURATION SETTINGS | RESPOND TO UNAUTHORIZED CHANGES
Take the following actions in response to unauthorized changes to [Assignment:
organization-defined configuration settings]: [Assignment: organization-defined actions].
Discussion:  Responses to unauthorized changes to configuration settings include alerting
designated organizational personnel, restoring established configuration settings, or—in
extreme cases—halting affected system processing.
Related Controls:  IR-4, IR-6, SI-7.
(3) CONFIGURATION SETTINGS | UNAUTHORIZED CHANGE DETECTION
[Withdrawn: Incorporated into SI-7.]
(4) CONFIGURATION SETTINGS | CONFORMANCE DEMONSTRATION
[Withdrawn: Incorporated into CM-4.]
References:  [SP 800-70], [SP 800-126], [SP 800-128], [USGCB], [NCPR], [DOD STIG].
