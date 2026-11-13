---
schema_version: 1
corpus: federal-reference
jurisdiction: us
id: nist-sp-800-53-r5.ra-9
title: NIST SP 800-53 Rev. 5 RA-9 — CRITICALITY ANALYSIS
doc_type: federal_instrument
citation: NIST SP 800-53 Rev. 5 RA-9
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

**NIST SP 800-53 Rev. 5 RA-9** — CRITICALITY ANALYSIS

- Issued by: National Institute of Standards and Technology
- Publication: NIST SP 800-53 Rev. 5 — Security and Privacy Controls for Information Systems and Organizations ([nist-sp-800-53-r5](./nist-sp-800-53-r5.md))
- Version: Rev. 5 (September 2020, includes updates as of 2020-12-10)
- Text as of: 2026-11-12
- Cited by held documents: 15 times (cjis-sp-6-1 ×10, arc-ampe ×4, 6-cfr-37 ×1)
- Reproduction basis: 17 U.S.C. § 105 — work of the U.S. government (NIST). Determined per document on 2026-11-12 against the publication itself, not assumed from its issuer: its Authority statement (PDF page 3) reads "This publication may be used by nongovernmental organizations on a voluntary basis and is not subject to copyright in the United States. Attribution would, however, be appreciated by NIST." Held here: the front matter and Chapter Three (the control catalog) only. Chapter Three names ISO/IEC standards solely as bibliographic references and reproduces none of their text. NOT mirrored: the References bibliography and Appendices A-C; Appendix A (glossary) adapts third-party definitions (ISO/IEC 15026, ISO 25237, ISO/IEC 29100, ISO 15288, IETF RFC 4949), which ADR-0002 treats as not reproducible by being incorporated, and whose reproducibility has not been determined.


_NON-AUTHORITATIVE copy of one control, cut from the SP 800-53 Rev. 5 snapshot this corpus holds. Whether and how this binds a given agency depends on the instrument that incorporates it — read it at the source URL before relying on it. This copy is the Rev. 5 text of record, which is not necessarily the text a citing document meant (a document citing Rev. 4 is not answered by it)._


## Full text

### RA-9 CRITICALITY ANALYSIS
Control:  Identify critical system components and functions by performing a criticality analysis for
[Assignment: organization-defined systems, system components, or system services] at
[Assignment: organization-defined decision points in the system development life cycle].
Discussion:  Not all system components, functions, or services necessarily require significant
protections. For example, criticality analysis is a key tenet of supply chain risk management and
informs the prioritization of protection activities. The identification of critical system components
and functions considers applicable laws, executive orders, regulations, directives, policies,
standards, system functionality requirements, system and component interfaces, and system and
component dependencies. Systems engineers conduct a functional decomposition of a system to
identify mission-critical functions and components. The functional decomposition includes the
identification of organizational missions supported by the system, decomposition into the
specific functions to perform those missions, and traceability to the hardware, software, and
firmware components that implement those functions, including when the functions are shared
by many components within and  external to the system.
The operational environment of a system or a system component may impact the criticality,
including the connections to and dependencies on cyber-physical systems, devices, system-of-
systems, and outsourced IT services. System components that allow unmediated access to critical
system components or functions are considered critical due to the inherent vulnerabilities that
such components create. Component and function criticality are assessed in terms of the impact
of a component or function failure on the organizational missions that are supported by the
system that contains the components and functions.
Criticality analysis is performed when an architecture or design is being developed, modified, or
upgraded. If such analysis is performed early in the system development life cycle, organizations
may be able to modify the system design to reduce the critical nature of these components and
functions, such as by adding redundancy or alternate paths into the system design. Criticality
analysis can also influence the protection measures required by development contractors. In
addition to criticality analysis for systems, system components, and system services, criticality
analysis of information is an important consideration. Such analysis is conducted as part of
security categorization in RA-2.
Related Controls:  CP-2, PL-2, PL-8, PL-11, PM-1, PM-11, RA-2, SA-8, SA-15, SA-20, SR-5.
Control Enhancements:  None.
References:  [IR 8179].
