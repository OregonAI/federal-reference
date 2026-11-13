---
schema_version: 1
corpus: federal-reference
jurisdiction: us
id: nist-sp-800-53-r5.sc-13
title: NIST SP 800-53 Rev. 5 SC-13 — CRYPTOGRAPHIC PROTECTION
doc_type: federal_instrument
citation: NIST SP 800-53 Rev. 5 SC-13
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

**NIST SP 800-53 Rev. 5 SC-13** — CRYPTOGRAPHIC PROTECTION

- Issued by: National Institute of Standards and Technology
- Publication: NIST SP 800-53 Rev. 5 — Security and Privacy Controls for Information Systems and Organizations ([nist-sp-800-53-r5](./nist-sp-800-53-r5.md))
- Version: Rev. 5 (September 2020, includes updates as of 2020-12-10)
- Text as of: 2026-11-12
- Cited by held documents: 38 times (cjis-sp-6-1 ×30, 6-cfr-37 ×4, irs-pub-1075-11-2021 ×4)
- Reproduction basis: 17 U.S.C. § 105 — work of the U.S. government (NIST). Determined per document on 2026-11-12 against the publication itself, not assumed from its issuer: its Authority statement (PDF page 3) reads "This publication may be used by nongovernmental organizations on a voluntary basis and is not subject to copyright in the United States. Attribution would, however, be appreciated by NIST." Held here: the front matter and Chapter Three (the control catalog) only. Chapter Three names ISO/IEC standards solely as bibliographic references and reproduces none of their text. NOT mirrored: the References bibliography and Appendices A-C; Appendix A (glossary) adapts third-party definitions (ISO/IEC 15026, ISO 25237, ISO/IEC 29100, ISO 15288, IETF RFC 4949), which ADR-0002 treats as not reproducible by being incorporated, and whose reproducibility has not been determined.


_NON-AUTHORITATIVE copy of one control, cut from the SP 800-53 Rev. 5 snapshot this corpus holds. Whether and how this binds a given agency depends on the instrument that incorporates it — read it at the source URL before relying on it. This copy is the Rev. 5 text of record, which is not necessarily the text a citing document meant (a document citing Rev. 4 is not answered by it)._


## Full text

### SC-13  CRYPTOGRAPHIC PROTECTION
Control:
a. Determine the [Assignment: organization-defined cryptographic uses]; and
CHAPTER THREE   PAGE 309
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
b. Implement the following types of cryptography required for each specified cryptographic
use: [Assignment: organization-defined types of cryptography for each specified
cryptographic use].
Discussion:  Cryptography can be employed to support a variety of security solutions, including
the protection of classified information and controlled unclassified information, the provision
and implementation of digital signatures, and the enforcement of information separation when
authorized individuals have the necessary clearances but lack the necessary formal access
approvals. Cryptography can also be used to support random number and hash generation.
Generally applicable cryptographic standards include FIPS-validated cryptography and NSA-
approved cryptography. For example, organizations that need to protect classified information
may specify the use of NSA-approved cryptography. Organizations that need to provision and
implement digital signatures may specify the use of FIPS-validated cryptography. Cryptography is
implemented in accordance with applicable laws, executive orders, directives, regulations,
policies, standards, and guidelines.
Related Controls:  AC-2, AC-3, AC-7, AC-17, AC-18, AC-19, AU-9, AU-10, CM-11, CP-9, IA-3, IA-5,
IA-7, MA-4, MP-2, MP-4, MP-5, SA-4, SA-8, SA-9, SC-8, SC-12, SC-20, SC-23, SC-28, SC-40, SI-3, SI-
7.
Control Enhancements:  None.
(1) CRYPTOGRAPHIC PROTECTION | FIPS-VALIDATED CRYPTOGRAPHY
[Withdrawn: Incorporated into SC-13.]
(2) CRYPTOGRAPHIC PROTECTION | NSA-APPROVED CRYPTOGRAPHY
[Withdrawn: Incorporated into SC-13.]
(3) CRYPTOGRAPHIC PROTECTION | INDIVIDUALS WITHOUT FORMAL ACCESS APPROVALS
[Withdrawn: Incorporated into SC-13.]
(4) CRYPTOGRAPHIC PROTECTION | DIGITAL SIGNATURES
[Withdrawn: Incorporated into SC-13.]
References:  [FIPS 140-3].
