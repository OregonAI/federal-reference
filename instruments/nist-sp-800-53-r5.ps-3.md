---
schema_version: 1
corpus: federal-reference
jurisdiction: us
id: nist-sp-800-53-r5.ps-3
title: NIST SP 800-53 Rev. 5 PS-3 — PERSONNEL SCREENING
doc_type: federal_instrument
citation: NIST SP 800-53 Rev. 5 PS-3
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

**NIST SP 800-53 Rev. 5 PS-3** — PERSONNEL SCREENING

- Issued by: National Institute of Standards and Technology
- Publication: NIST SP 800-53 Rev. 5 — Security and Privacy Controls for Information Systems and Organizations ([nist-sp-800-53-r5](./nist-sp-800-53-r5.md))
- Version: Rev. 5 (September 2020, includes updates as of 2020-12-10)
- Text as of: 2026-11-12
- Cited by held documents: 19 times (cjis-sp-6-1 ×12, irs-pub-1075-11-2021 ×3, 6-cfr-37 ×2, arc-ampe ×2)
- Reproduction basis: 17 U.S.C. § 105 — work of the U.S. government (NIST). Determined per document on 2026-11-12 against the publication itself, not assumed from its issuer: its Authority statement (PDF page 3) reads "This publication may be used by nongovernmental organizations on a voluntary basis and is not subject to copyright in the United States. Attribution would, however, be appreciated by NIST." Held here: the front matter and Chapter Three (the control catalog) only. Chapter Three names ISO/IEC standards solely as bibliographic references and reproduces none of their text. NOT mirrored: the References bibliography and Appendices A-C; Appendix A (glossary) adapts third-party definitions (ISO/IEC 15026, ISO 25237, ISO/IEC 29100, ISO 15288, IETF RFC 4949), which ADR-0002 treats as not reproducible by being incorporated, and whose reproducibility has not been determined.


_NON-AUTHORITATIVE copy of one control, cut from the SP 800-53 Rev. 5 snapshot this corpus holds. Whether and how this binds a given agency depends on the instrument that incorporates it — read it at the source URL before relying on it. This copy is the Rev. 5 text of record, which is not necessarily the text a citing document meant (a document citing Rev. 4 is not answered by it)._


## Full text

### PS-3 PERSONNEL SCREENING
Control:
a. Screen individuals prior to authorizing access to the system; and
b. Rescreen individuals in accordance with [Assignment: organization-defined conditions
requiring rescreening and, where rescreening is so indicated, the frequency of rescreening].
Discussion:  Personnel screening and rescreening activities reflect applicable laws, executive
orders, directives, regulations, policies, standards, guidelines, and specific criteria established for
the risk designations of assigned positions. Examples of personnel screening include background
investigations and agency checks. Organizations may define different rescreening conditions and
frequencies for personnel accessing systems based on types of information processed, stored, or
transmitted by the systems.
Related Controls:  AC-2, IA-4, MA-5, PE-2, PM-12, PS-2, PS-6, PS-7, SA-21.
Control Enhancements:
(1) PERSONNEL SCREENING | CLASSIFIED INFORMATION
Verify that individuals accessing a system processing, storing, or transmitting classified
information are cleared and indoctrinated to the highest classification level of the
information to which they have access on the system.
Discussion:  Classified information is the most sensitive information that the Federal
Government processes, stores, or transmits. It is imperative that individuals have the
requisite security clearances and system access authorizations prior to gaining access to such
CHAPTER THREE    PAGE 224
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
information. Access authorizations are enforced by system access controls (see AC-3) and
flow controls (see AC-4).
Related Controls:  AC-3, AC-4.
(2) PERSONNEL SCREENING | FORMAL INDOCTRINATION
Verify that individuals accessing a system processing, storing, or transmitting types of
classified information that require formal indoctrination, are formally indoctrinated for all
the relevant types of information to which they have access on the system.
Discussion:  Types of classified information that require formal indoctrination include Special
Access Program (SAP), Restricted Data (RD), and Sensitive Compartmented Information (SCI).
Related Controls:  AC-3, AC-4.
(3) PERSONNEL SCREENING | INFORMATION REQUIRING SPECIAL PROTECTIVE MEASURES
Verify that individuals accessing a system processing, storing, or transmitting information
requiring special protection:
(a) Have valid access authorizations that are demonstrated by assigned official
government duties; and
(b) Satisfy [Assignment: organization-defined additional personnel screening criteria].
Discussion:  Organizational information that requires special protection includes controlled
unclassified information. Personnel security criteria include position sensitivity background
screening requirements.
Related Controls:  None.
(4) PERSONNEL SCREENING | CITIZENSHIP REQUIREMENTS
Verify that individuals accessing a system processing, storing, or transmitting [Assignment:
organization-defined information types] meet [Assignment: organization-defined
citizenship requirements].
Discussion:  None.
Related Controls:  None.
References:  [EO 13526], [EO 13587], [FIPS 199], [FIPS 201-2], [SP 800-60-1], [SP 800-60-2], [SP
800-73-4], [SP 800-76-2], [SP 800-78-4].
