---
schema_version: 1
corpus: federal-reference
jurisdiction: us
id: nist-sp-800-53-r5.cm-4
title: NIST SP 800-53 Rev. 5 CM-4 — IMPACT ANALYSES
doc_type: federal_instrument
citation: NIST SP 800-53 Rev. 5 CM-4
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

**NIST SP 800-53 Rev. 5 CM-4** — IMPACT ANALYSES

- Issued by: National Institute of Standards and Technology
- Publication: NIST SP 800-53 Rev. 5 — Security and Privacy Controls for Information Systems and Organizations ([nist-sp-800-53-r5](./nist-sp-800-53-r5.md))
- Version: Rev. 5 (September 2020, includes updates as of 2020-12-10)
- Text as of: 2026-11-12
- Cited by held documents: 27 times (cjis-sp-6-1 ×17, arc-ampe ×4, 6-cfr-37 ×3, irs-pub-1075-11-2021 ×3)
- Reproduction basis: 17 U.S.C. § 105 — work of the U.S. government (NIST). Determined per document on 2026-11-12 against the publication itself, not assumed from its issuer: its Authority statement (PDF page 3) reads "This publication may be used by nongovernmental organizations on a voluntary basis and is not subject to copyright in the United States. Attribution would, however, be appreciated by NIST." Held here: the front matter and Chapter Three (the control catalog) only. Chapter Three names ISO/IEC standards solely as bibliographic references and reproduces none of their text. NOT mirrored: the References bibliography and Appendices A-C; Appendix A (glossary) adapts third-party definitions (ISO/IEC 15026, ISO 25237, ISO/IEC 29100, ISO 15288, IETF RFC 4949), which ADR-0002 treats as not reproducible by being incorporated, and whose reproducibility has not been determined.


_NON-AUTHORITATIVE copy of one control, cut from the SP 800-53 Rev. 5 snapshot this corpus holds. Whether and how this binds a given agency depends on the instrument that incorporates it — read it at the source URL before relying on it. This copy is the Rev. 5 text of record, which is not necessarily the text a citing document meant (a document citing Rev. 4 is not answered by it)._


## Full text

### CM-4 IMPACT ANALYSES
Control:  Analyze changes to the system to determine potential security and privacy impacts
prior to change implementation.
Discussion:  Organizational personnel with security or privacy responsibilities conduct impact
analyses. Individuals conducting impact analyses possess the necessary skills and technical
expertise to analyze the changes to systems as well as the security or privacy ramifications.
Impact analyses include reviewing security and privacy plans, policies, and procedures to
understand control requirements; reviewing system design documentation and operational
procedures to understand control implementation and how specific system changes might affect
the controls; reviewing the impact of changes on organizational supply chain partners with
stakeholders; and determining how potential changes to a system create new risks to the privacy
of individuals and the ability of implemented controls to mitigate those risks. Impact analyses
also include risk assessments to understand the impact of the changes and determine if
additional controls are required.
Related Controls:  CA-7, CM-3, CM-8, CM-9, MA-2, RA-3, RA-5, RA-8, SA-5, SA-8, SA-10, SI-2.
Control Enhancements:
(1) IMPACT ANALYSES | SEPARATE TEST ENVIRONMENTS
Analyze changes to the system in a separate test environment before implementation in
an operational environment, looking for security and privacy impacts due to flaws,
weaknesses, incompatibility, or intentional malice.
Discussion:  A separate test environment requires an environment that is physically or
logically separate and distinct from the operational environment. The separation is sufficient
to ensure that activities in the test environment do not impact activities in the operational
environment and that information in the operational environment is not inadvertently
transmitted to the test environment. Separate environments can be achieved by physical or
logical means. If physically separate test environments are not implemented, organizations
determine the strength of mechanism required when implementing logical separation.
Related Controls:  SA-11, SC-7.
(2) IMPACT ANALYSES | VERIFICATION OF CONTROLS
CHAPTER THREE   PAGE 102
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
After system changes, verify that the impacted controls are implemented correctly,
operating as intended, and producing the desired outcome with regard to meeting the
security and privacy requirements for the system.
Discussion:  Implementation in this context refers to installing changed code in the
operational system that may have an impact on security or privacy controls.
Related Controls:  SA-11, SC-3, SI-6.
References:  [SP 800-128].
