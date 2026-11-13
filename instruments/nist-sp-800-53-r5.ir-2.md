---
schema_version: 1
corpus: federal-reference
jurisdiction: us
id: nist-sp-800-53-r5.ir-2
title: NIST SP 800-53 Rev. 5 IR-2 — INCIDENT RESPONSE TRAINING
doc_type: federal_instrument
citation: NIST SP 800-53 Rev. 5 IR-2
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

**NIST SP 800-53 Rev. 5 IR-2** — INCIDENT RESPONSE TRAINING

- Issued by: National Institute of Standards and Technology
- Publication: NIST SP 800-53 Rev. 5 — Security and Privacy Controls for Information Systems and Organizations ([nist-sp-800-53-r5](./nist-sp-800-53-r5.md))
- Version: Rev. 5 (September 2020, includes updates as of 2020-12-10)
- Text as of: 2026-11-12
- Cited by held documents: 23 times (cjis-sp-6-1 ×13, irs-pub-1075-11-2021 ×5, arc-ampe ×3, 6-cfr-37 ×2), 2 of them naming an enhancement of this control
- Reproduction basis: 17 U.S.C. § 105 — work of the U.S. government (NIST). Determined per document on 2026-11-12 against the publication itself, not assumed from its issuer: its Authority statement (PDF page 3) reads "This publication may be used by nongovernmental organizations on a voluntary basis and is not subject to copyright in the United States. Attribution would, however, be appreciated by NIST." Held here: the front matter and Chapter Three (the control catalog) only. Chapter Three names ISO/IEC standards solely as bibliographic references and reproduces none of their text. NOT mirrored: the References bibliography and Appendices A-C; Appendix A (glossary) adapts third-party definitions (ISO/IEC 15026, ISO 25237, ISO/IEC 29100, ISO 15288, IETF RFC 4949), which ADR-0002 treats as not reproducible by being incorporated, and whose reproducibility has not been determined.


_NON-AUTHORITATIVE copy of one control, cut from the SP 800-53 Rev. 5 snapshot this corpus holds. Whether and how this binds a given agency depends on the instrument that incorporates it — read it at the source URL before relying on it. This copy is the Rev. 5 text of record, which is not necessarily the text a citing document meant (a document citing Rev. 4 is not answered by it)._


## Full text

### IR-2 INCIDENT RESPONSE TRAINING
Control:
a. Provide incident response training to system users consistent with assigned roles and
responsibilities:
1. Within [Assignment: organization-defined time period] of assuming an incident response
role or responsibility or acquiring system access;
2. When required by system changes; and
3. [Assignment: organization-defined frequency] thereafter; and
b. Review and update incident response training content [Assignment: organization-defined
frequency] and following [Assignment: organization-defined events].
Discussion:  Incident response training is associated with the assigned roles and responsibilities
of organizational personnel to ensure that the appropriate content and level of detail are
included in such training. For example, users may only need to know who to call or how to
recognize an incident; system administrators may require additional training on how to handle
incidents; and incident responders may receive more specific training on forensics, data
collection techniques, reporting, system recovery, and system restoration. Incident response
training includes user training in identifying and reporting suspicious activities from external and
internal sources. Incident response training for users may be provided as part of AT-2 or AT-3.
Events that may precipitate an update to incident response training content include, but are not
limited to, incident response plan testing or response to an actual incident (lessons learned),
assessment or audit findings, or changes in applicable laws, executive orders, directives,
regulations, policies, standards, and guidelines.
Related Controls:  AT-2, AT-3, AT-4, CP-3, IR-3, IR-4, IR-8, IR-9.
Control Enhancements:
(1) INCIDENT RESPONSE TRAINING | SIMULATED EVENTS
Incorporate simulated events into incident response training to facilitate the required
response by personnel in crisis situations.
Discussion:  Organizations establish requirements for responding to incidents in incident
response plans. Incorporating simulated events into incident response training helps to
ensure that personnel understand their individual responsibilities and what specific actions
to take in crisis situations.
Related Controls:  None.
(2) INCIDENT RESPONSE TRAINING | AUTOMATED TRAINING ENVIRONMENTS
Provide an incident response training environment using [Assignment: organization-
defined automated mechanisms].
Discussion:  Automated mechanisms can provide a more thorough and realistic incident
response training environment. This can be accomplished, for example, by providing more
complete coverage of incident response issues, selecting more realistic training scenarios
and environments, and stressing the response capability.
Related Controls:  None.
(3) INCIDENT RESPONSE TRAINING | BREACH
Provide incident response training on how to identify and respond to a breach, including
the organization’s process for reporting a breach.
CHAPTER THREE   PAGE 151
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
Discussion:  For federal agencies, an incident that involves personally identifiable
information is considered a breach. A breach results in the loss of control, compromise,
unauthorized disclosure, unauthorized acquisition, or a similar occurrence where a person
other than an authorized user accesses or potentially accesses personally identifiable
information or an authorized user accesses or potentially accesses such information for
other than authorized purposes. The incident response training emphasizes the obligation of
individuals to report both confirmed and suspected breaches involving information in any
medium or form, including paper, oral, and electronic. Incident response training includes
tabletop exercises that simulate a breach. See IR-2(1).
Related Controls:  None.
References:  [OMB M-17-12], [SP 800-50].
