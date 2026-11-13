---
schema_version: 1
corpus: federal-reference
jurisdiction: us
id: nist-sp-800-53-r5.cp-3
title: NIST SP 800-53 Rev. 5 CP-3 — CONTINGENCY TRAINING
doc_type: federal_instrument
citation: NIST SP 800-53 Rev. 5 CP-3
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

**NIST SP 800-53 Rev. 5 CP-3** — CONTINGENCY TRAINING

- Issued by: National Institute of Standards and Technology
- Publication: NIST SP 800-53 Rev. 5 — Security and Privacy Controls for Information Systems and Organizations ([nist-sp-800-53-r5](./nist-sp-800-53-r5.md))
- Version: Rev. 5 (September 2020, includes updates as of 2020-12-10)
- Text as of: 2026-11-12
- Cited by held documents: 19 times (cjis-sp-6-1 ×12, irs-pub-1075-11-2021 ×5, 6-cfr-37 ×1, arc-ampe ×1)
- Reproduction basis: 17 U.S.C. § 105 — work of the U.S. government (NIST). Determined per document on 2026-11-12 against the publication itself, not assumed from its issuer: its Authority statement (PDF page 3) reads "This publication may be used by nongovernmental organizations on a voluntary basis and is not subject to copyright in the United States. Attribution would, however, be appreciated by NIST." Held here: the front matter and Chapter Three (the control catalog) only. Chapter Three names ISO/IEC standards solely as bibliographic references and reproduces none of their text. NOT mirrored: the References bibliography and Appendices A-C; Appendix A (glossary) adapts third-party definitions (ISO/IEC 15026, ISO 25237, ISO/IEC 29100, ISO 15288, IETF RFC 4949), which ADR-0002 treats as not reproducible by being incorporated, and whose reproducibility has not been determined.


_NON-AUTHORITATIVE copy of one control, cut from the SP 800-53 Rev. 5 snapshot this corpus holds. Whether and how this binds a given agency depends on the instrument that incorporates it — read it at the source URL before relying on it. This copy is the Rev. 5 text of record, which is not necessarily the text a citing document meant (a document citing Rev. 4 is not answered by it)._


## Full text

### CP-3 CONTINGENCY TRAINING
Control:
a. Provide contingency training to system users consistent with assigned roles and
responsibilities:
1. Within [Assignment: organization-defined time period] of assuming a contingency role
or responsibility;
2. When required by system changes; and
CHAPTER THREE   PAGE 119
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
3. [Assignment: organization-defined frequency] thereafter; and
b. Review and update contingency training content [Assignment: organization-defined
frequency] and following [Assignment: organization-defined events].
Discussion:  Contingency training provided by organizations is linked to the assigned roles and
responsibilities of organizational personnel to ensure that the appropriate content and level of
detail is included in such training. For example, some individuals may only need to know when
and where to report for duty during contingency operations and if normal duties are affected;
system administrators may require additional training on how to establish systems at alternate
processing and storage sites; and organizational officials may receive more specific training on
how to conduct mission-essential functions in designated off-site locations and how to establish
communications with other governmental entities for purposes of coordination on contingency-
related activities. Training for contingency roles or responsibilities reflects the specific continuity
requirements in the contingency plan. Events that may precipitate an update to contingency
training content include, but are not limited to, contingency plan testing or an actual contingency
(lessons learned), assessment or audit findings, security incidents or breaches, or changes in
laws, executive orders, directives, regulations, policies, standards, and guidelines. At the
discretion of the organization, participation in a contingency plan test or exercise, including
lessons learned sessions subsequent to the test or exercise, may satisfy contingency plan training
requirements.
Related Controls:  AT-2, AT-3, AT-4, CP-2, CP-4, CP-8, IR-2, IR-4, IR-9.
Control Enhancements:
(1) CONTINGENCY TRAINING | SIMULATED EVENTS
Incorporate simulated events into contingency training to facilitate effective response by
personnel in crisis situations.
Discussion:  The use of simulated events creates an environment for personnel to experience
actual threat events, including cyber-attacks that disable websites, ransomware attacks that
encrypt organizational data on servers, hurricanes that damage or destroy organizational
facilities, or hardware or software failures.
Related Controls:  None.
(2) CONTINGENCY TRAINING | MECHANISMS USED IN TRAINING ENVIRONMENTS
Employ mechanisms used in operations to provide a more thorough and realistic
contingency training environment.
Discussion:  Operational mechanisms refer to processes that have been established to
accomplish an organizational goal or a system that supports a particular organizational
mission or business objective. Actual mission and business processes, systems, and/or
facilities may be used to generate simulated events and enhance the realism of simulated
events during contingency training.
Related Controls:  None.
References:  [SP 800-50].
