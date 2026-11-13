---
schema_version: 1
corpus: federal-reference
jurisdiction: us
id: nist-sp-800-53-r5.mp-8
title: NIST SP 800-53 Rev. 5 MP-8 — MEDIA DOWNGRADING
doc_type: federal_instrument
citation: NIST SP 800-53 Rev. 5 MP-8
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

**NIST SP 800-53 Rev. 5 MP-8** — MEDIA DOWNGRADING

- Issued by: National Institute of Standards and Technology
- Publication: NIST SP 800-53 Rev. 5 — Security and Privacy Controls for Information Systems and Organizations ([nist-sp-800-53-r5](./nist-sp-800-53-r5.md))
- Version: Rev. 5 (September 2020, includes updates as of 2020-12-10)
- Text as of: 2026-11-12
- Cited by held documents: 3 times (arc-ampe ×3)
- Reproduction basis: 17 U.S.C. § 105 — work of the U.S. government (NIST). Determined per document on 2026-11-12 against the publication itself, not assumed from its issuer: its Authority statement (PDF page 3) reads "This publication may be used by nongovernmental organizations on a voluntary basis and is not subject to copyright in the United States. Attribution would, however, be appreciated by NIST." Held here: the front matter and Chapter Three (the control catalog) only. Chapter Three names ISO/IEC standards solely as bibliographic references and reproduces none of their text. NOT mirrored: the References bibliography and Appendices A-C; Appendix A (glossary) adapts third-party definitions (ISO/IEC 15026, ISO 25237, ISO/IEC 29100, ISO 15288, IETF RFC 4949), which ADR-0002 treats as not reproducible by being incorporated, and whose reproducibility has not been determined.


_NON-AUTHORITATIVE copy of one control, cut from the SP 800-53 Rev. 5 snapshot this corpus holds. Whether and how this binds a given agency depends on the instrument that incorporates it — read it at the source URL before relying on it. This copy is the Rev. 5 text of record, which is not necessarily the text a citing document meant (a document citing Rev. 4 is not answered by it)._


## Full text

### MP-8 MEDIA DOWNGRADING
Control:
a. Establish [Assignment: organization-defined system media downgrading process] that
includes employing downgrading mechanisms with strength and integrity commensurate
with the security category or classification of the information;
b. Verify that the system media downgrading process is commensurate with the security
category and/or classification level of the information to be removed and the access
authorizations of the potential recipients of the downgraded information;
c. Identify [Assignment: organization-defined system media requiring downgrading]; and
d. Downgrade the identified system media using the established process.
Discussion:  Media downgrading applies to digital and non-digital media subject to release
outside of the organization, whether the media is considered removable or not. When applied to
system media, the downgrading process removes information from the media, typically by
security category or classification level, such that the information cannot be retrieved or
reconstructed. Downgrading of media includes redacting information to enable wider release
and distribution. Downgrading ensures that empty space on the media is devoid of information.
Related Controls:  None.
Control Enhancements:
(1) MEDIA DOWNGRADING | DOCUMENTATION OF PROCESS
Document system media downgrading actions.
CHAPTER THREE   PAGE 178
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
Discussion:  Organizations can document the media downgrading process by providing
information, such as the downgrading technique employed, the identification number of the
downgraded media, and the identity of the individual that authorized and/or performed the
downgrading action.
Related Controls:  None.
(2) MEDIA DOWNGRADING | EQUIPMENT TESTING
Test downgrading equipment and procedures [Assignment: organization-defined
frequency] to ensure that downgrading actions are being achieved.
Discussion:  None.
Related Controls:  None.
(3) MEDIA DOWNGRADING | CONTROLLED UNCLASSIFIED INFORMATION
Downgrade system media containing controlled unclassified information prior to public
release.
Discussion:  The downgrading of controlled unclassified information uses approved
sanitization tools, techniques, and procedures.
Related Controls:  None.
(4) MEDIA DOWNGRADING | CLASSIFIED INFORMATION
Downgrade system media containing classified information prior to release to individuals
without required access authorizations.
Discussion:  Downgrading of classified information uses approved sanitization tools,
techniques, and procedures to transfer information confirmed to be unclassified from
classified systems to unclassified media.
Related Controls:  None.
References:  [32 CFR 2002], [NSA MEDIA].
CHAPTER THREE   PAGE 179
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
3.11   PHYSICAL AND ENVIRONMENTAL PROTECTION
Quick link to Physical and Environmental Protection Summary Table
