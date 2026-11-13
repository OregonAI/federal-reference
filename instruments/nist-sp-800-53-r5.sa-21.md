---
schema_version: 1
corpus: federal-reference
jurisdiction: us
id: nist-sp-800-53-r5.sa-21
title: NIST SP 800-53 Rev. 5 SA-21 — DEVELOPER SCREENING
doc_type: federal_instrument
citation: NIST SP 800-53 Rev. 5 SA-21
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

**NIST SP 800-53 Rev. 5 SA-21** — DEVELOPER SCREENING

- Issued by: National Institute of Standards and Technology
- Publication: NIST SP 800-53 Rev. 5 — Security and Privacy Controls for Information Systems and Organizations ([nist-sp-800-53-r5](./nist-sp-800-53-r5.md))
- Version: Rev. 5 (September 2020, includes updates as of 2020-12-10)
- Text as of: 2026-11-12
- Cited by held documents: 1 time (6-cfr-37 ×1)
- Reproduction basis: 17 U.S.C. § 105 — work of the U.S. government (NIST). Determined per document on 2026-11-12 against the publication itself, not assumed from its issuer: its Authority statement (PDF page 3) reads "This publication may be used by nongovernmental organizations on a voluntary basis and is not subject to copyright in the United States. Attribution would, however, be appreciated by NIST." Held here: the front matter and Chapter Three (the control catalog) only. Chapter Three names ISO/IEC standards solely as bibliographic references and reproduces none of their text. NOT mirrored: the References bibliography and Appendices A-C; Appendix A (glossary) adapts third-party definitions (ISO/IEC 15026, ISO 25237, ISO/IEC 29100, ISO 15288, IETF RFC 4949), which ADR-0002 treats as not reproducible by being incorporated, and whose reproducibility has not been determined.


_NON-AUTHORITATIVE copy of one control, cut from the SP 800-53 Rev. 5 snapshot this corpus holds. Whether and how this binds a given agency depends on the instrument that incorporates it — read it at the source URL before relying on it. This copy is the Rev. 5 text of record, which is not necessarily the text a citing document meant (a document citing Rev. 4 is not answered by it)._


## Full text

### SA-21 DEVELOPER SCREENING
Control:  Require that the developer of [Assignment: organization-defined system, system
component, or system service]:
a. Has appropriate access authorizations as determined by assigned [Assignment: organization-
defined official government duties]; and
b. Satisfies the following additional personnel screening criteria: [Assignment: organization-
defined additional personnel screening criteria].
Discussion:  Developer screening is directed at external developers. Internal developer screening
is addressed by PS-3. Because the system, system component, or system service may be used in
critical activities essential to the national or economic security interests of the United States,
organizations have a strong interest in ensuring that developers are trustworthy. The degree of
CHAPTER THREE   PAGE 290
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
trust required of developers may need to be consistent with that of the individuals who access
the systems, system components, or system services once deployed. Authorization and
personnel screening criteria include clearances, background checks, citizenship, and nationality.
Developer trustworthiness may also include a review and analysis of company ownership and
relationships that the company has with entities that may potentially affect the quality and
reliability of the systems, components, or services being developed. Satisfying the required
access authorizations and personnel screening criteria includes providing a list of all individuals
who are authorized to perform development activities on the selected system, system
component, or system service so that organizations can validate that the developer has satisfied
the authorization and screening requirements.
Related Controls:  PS-2, PS-3, PS-6, PS-7, SA-4, SR-6.
Control Enhancements:
(1) DEVELOPER SCREENING | VALIDATION OF SCREENING
[Withdrawn: Incorporated into SA-21.]
References:  None.
