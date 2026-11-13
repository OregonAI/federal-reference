---
schema_version: 1
corpus: federal-reference
jurisdiction: us
id: nist-sp-800-53-r5.sa-15
title: NIST SP 800-53 Rev. 5 SA-15 — DEVELOPMENT PROCESS, STANDARDS, AND TOOLS
doc_type: federal_instrument
citation: NIST SP 800-53 Rev. 5 SA-15
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

**NIST SP 800-53 Rev. 5 SA-15** — DEVELOPMENT PROCESS, STANDARDS, AND TOOLS

- Issued by: National Institute of Standards and Technology
- Publication: NIST SP 800-53 Rev. 5 — Security and Privacy Controls for Information Systems and Organizations ([nist-sp-800-53-r5](./nist-sp-800-53-r5.md))
- Version: Rev. 5 (September 2020, includes updates as of 2020-12-10)
- Text as of: 2026-11-12
- Cited by held documents: 24 times (cjis-sp-6-1 ×19, irs-pub-1075-11-2021 ×3, 6-cfr-37 ×1, arc-ampe ×1)
- Reproduction basis: 17 U.S.C. § 105 — work of the U.S. government (NIST). Determined per document on 2026-11-12 against the publication itself, not assumed from its issuer: its Authority statement (PDF page 3) reads "This publication may be used by nongovernmental organizations on a voluntary basis and is not subject to copyright in the United States. Attribution would, however, be appreciated by NIST." Held here: the front matter and Chapter Three (the control catalog) only. Chapter Three names ISO/IEC standards solely as bibliographic references and reproduces none of their text. NOT mirrored: the References bibliography and Appendices A-C; Appendix A (glossary) adapts third-party definitions (ISO/IEC 15026, ISO 25237, ISO/IEC 29100, ISO 15288, IETF RFC 4949), which ADR-0002 treats as not reproducible by being incorporated, and whose reproducibility has not been determined.


_NON-AUTHORITATIVE copy of one control, cut from the SP 800-53 Rev. 5 snapshot this corpus holds. Whether and how this binds a given agency depends on the instrument that incorporates it — read it at the source URL before relying on it. This copy is the Rev. 5 text of record, which is not necessarily the text a citing document meant (a document citing Rev. 4 is not answered by it)._


> **Release 5.2.0 postdates this text.** NIST's listing of record ([https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final)) says that on 2025-08-27 it issued release 5.2.0 of SP 800-53, which adds a control or enhancement and updates the related controls for this control. The text below is the Rev. 5 PDF of record and does NOT include that change; read NIST's own list of the changes ([summary](https://csrc.nist.gov/files/projects/Risk-Management/800-53%20Comment%20Site/SP800-53-r5.2.0-changes.pdf)) before relying on this control's text.


## Full text

### SA-15 DEVELOPMENT PROCESS, STANDARDS, AND TOOLS
Control:
a. Require the developer of the system, system component, or system service to follow a
documented development process that:
1. Explicitly addresses security and privacy requirements;
2. Identifies the standards and tools used in the development process;
3. Documents the specific tool options and tool configurations used in the development
process; and
4. Documents, manages, and ensures the integrity of changes to the process and/or tools
used in development; and
b. Review the development process, standards, tools, tool options, and tool configurations
[Assignment: organization-defined frequency] to determine if the process, standards, tools,
tool options and tool configurations selected and employed can satisfy the following security
and privacy requirements: [Assignment: organization-defined security and privacy
requirements].
Discussion:  Development tools include programming languages and computer-aided design
systems. Reviews of development processes include the use of maturity models to determine the
potential effectiveness of such processes. Maintaining the integrity of changes to tools and
processes facilitates effective supply chain risk assessment and mitigation. Such integrity requires
configuration control throughout the system development life cycle to track authorized changes
and prevent unauthorized changes.
Related Controls:  MA-6, SA-3, SA-4, SA-8, SA-10, SA-11, SR-3, SR-4, SR-5, SR-6, SR-9.
Control Enhancements:
(1) DEVELOPMENT PROCESS, STANDARDS, AND TOOLS | QUALITY METRICS
Require the developer of the system, system component, or system service to:
(a) Define quality metrics at the beginning of the development process; and
(b) Provide evidence of meeting the quality metrics [Selection (one or more):
[Assignment: organization-defined frequency]; [Assignment: organization-defined
program review milestones]; upon delivery].
Discussion:  Organizations use quality metrics to establish acceptable levels of system
quality. Metrics can include quality gates, which are collections of completion criteria or
sufficiency standards that represent the satisfactory execution of specific phases of the
system development project. For example, a quality gate may require the elimination of all
compiler warnings or a determination that such warnings have no impact on the
effectiveness of required security or privacy capabilities. During the execution phases of
development projects, quality gates provide clear, unambiguous indications of progress.
Other metrics apply to the entire development project. Metrics can include defining the
severity thresholds of vulnerabilities in accordance with organizational risk tolerance, such
CHAPTER THREE   PAGE 282
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
as requiring no known vulnerabilities in the delivered system with a Common Vulnerability
Scoring System (CVSS) severity of medium or high.
Related Controls:  None.
(2) DEVELOPMENT PROCESS, STANDARDS, AND TOOLS | SECURITY AND PRIVACY TRACKING TOOLS
Require the developer of the system, system component, or system service to select and
employ security and privacy tracking tools for use during the development process.
Discussion:  System development teams select and deploy security and privacy tracking
tools, including vulnerability or work item tracking systems that facilitate assignment,
sorting, filtering, and tracking of completed work items or tasks associated with
development processes.
Related Controls:  SA-11.
(3) DEVELOPMENT PROCESS, STANDARDS, AND TOOLS | CRITICALITY ANALYSIS
Require the developer of the system, system component, or system service to perform a
criticality analysis:
(a) At the following decision points in the system development life cycle: [Assignment:
organization-defined decision points in the system development life cycle]; and
(b) At the following level of rigor: [Assignment: organization-defined breadth and depth
of criticality analysis].
Discussion:  Criticality analysis performed by the developer provides input to the criticality
analysis performed by organizations. Developer input is essential to organizational criticality
analysis because organizations may not have access to detailed design documentation for
system components that are developed as commercial off-the-shelf products. Such design
documentation includes functional specifications, high-level designs, low-level designs,
source code, and hardware schematics. Criticality analysis is important for organizational
systems that are designated as high value assets. High value assets can be moderate- or
high-impact systems due to heightened adversarial interest or potential adverse effects on
the federal enterprise. Developer input is especially important when organizations conduct
supply chain criticality analyses.
Related Controls:  RA-9.
(4) DEVELOPMENT PROCESS, STANDARDS, AND TOOLS | THREAT MODELING AND VULNERABILITY
ANALYSIS
[Withdrawn: Incorporated into SA-11(2).]
(5) DEVELOPMENT PROCESS, STANDARDS, AND TOOLS | ATTACK SURFACE REDUCTION
Require the developer of the system, system component, or system service to reduce
attack surfaces to [Assignment: organization-defined thresholds].
Discussion:  Attack surface reduction is closely aligned with threat and vulnerability analyses
and system architecture and design. Attack surface reduction is a means of reducing risk to
organizations by giving attackers less opportunity to exploit weaknesses or deficiencies (i.e.,
potential vulnerabilities) within systems, system components, and system services. Attack
surface reduction includes implementing the concept of layered defenses, applying the
principles of least privilege and least functionality, applying secure software development
practices, deprecating unsafe functions, reducing entry points available to unauthorized
users, reducing the amount of code that executes, and eliminating application programming
interfaces (APIs) that are vulnerable to attacks.
Related Controls:  AC-6, CM-7, RA-3, SA-11.
(6) DEVELOPMENT PROCESS, STANDARDS, AND TOOLS | CONTINUOUS IMPROVEMENT
CHAPTER THREE   PAGE 283
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
Require the developer of the system, system component, or system service to implement
an explicit process to continuously improve the development process.
Discussion:  Developers of systems, system components, and system services consider the
effectiveness and efficiency of their development processes for meeting quality objectives
and addressing the security and privacy capabilities in current threat environments.
Related Controls:  None.
(7) DEVELOPMENT PROCESS, STANDARDS, AND TOOLS | AUTOMATED VULNERABILITY ANALYSIS
Require the developer of the system, system component, or system service [Assignment:
organization-defined frequency] to:
(a) Perform an automated vulnerability analysis using [Assignment: organization-defined
tools];
(b) Determine the exploitation potential for discovered vulnerabilities;
(c) Determine potential risk mitigations for delivered vulnerabilities; and
(d) Deliver the outputs of the tools and results of the analysis to [Assignment:
organization-defined personnel or roles].
Discussion:  Automated tools can be more effective at analyzing exploitable weaknesses or
deficiencies in large and complex systems, prioritizing vulnerabilities by severity, and
providing recommendations for risk mitigations.
Related Controls:  RA-5, SA-11.
(8) DEVELOPMENT PROCESS, STANDARDS, AND TOOLS | REUSE OF THREAT AND VULNERABILITY
INFORMATION
Require the developer of the system, system component, or system service to use threat
modeling and vulnerability analyses from similar systems, components, or services to
inform the current development process.
Discussion:  Analysis of vulnerabilities found in similar software applications can inform
potential design and implementation issues for systems under development. Similar systems
or system components may exist within developer organizations. Vulnerability information is
available from a variety of public and private sector sources, including the NIST National
Vulnerability Database.
Related Controls:  None.
(9) DEVELOPMENT PROCESS, STANDARDS, AND TOOLS | USE OF LIVE DATA
[Withdrawn: Incorporated into SA-3(2).]
(10) DEVELOPMENT PROCESS, STANDARDS, AND TOOLS | INCIDENT RESPONSE PLAN
Require the developer of the system, system component, or system service to provide,
implement, and test an incident response plan.
Discussion:  The incident response plan provided by developers may provide information not
readily available to organizations and be incorporated into organizational incident response
plans. Developer information may also be extremely helpful, such as when organizations
respond to vulnerabilities in commercial off-the-shelf products.
Related Controls:  IR-8.
(11) DEVELOPMENT PROCESS, STANDARDS, AND TOOLS | ARCHIVE SYSTEM OR COMPONENT
Require the developer of the system or system component to archive the system or
component to be released or delivered together with the corresponding evidence
supporting the final security and privacy review.
CHAPTER THREE   PAGE 284
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
Discussion:  Archiving system or system components requires the developer to retain key
development artifacts, including hardware specifications, source code, object code, and
relevant documentation from the development process that can provide a readily available
configuration baseline for system and component upgrades or modifications.
Related Controls:  CM-2.
(12) DEVELOPMENT PROCESS, STANDARDS, AND TOOLS | MINIMIZE PERSONALLY IDENTIFIABLE
INFORMATION
Require the developer of the system or system component to minimize the use of
personally identifiable information in development and test environments.
Discussion:  Organizations can minimize the risk to an individual’s privacy by using
techniques such as de-identification or synthetic data. Limiting the use of personally
identifiable information in development and test environments helps reduce the level of
privacy risk created by a system.
Related Controls:  PM-25, SA-3, SA-8.
References:  [SP 800-160-1], [IR 8179].
