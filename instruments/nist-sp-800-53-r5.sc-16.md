---
schema_version: 1
corpus: federal-reference
jurisdiction: us
id: nist-sp-800-53-r5.sc-16
title: NIST SP 800-53 Rev. 5 SC-16 — TRANSMISSION OF SECURITY AND PRIVACY ATTRIBUTES
doc_type: federal_instrument
citation: NIST SP 800-53 Rev. 5 SC-16
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

**NIST SP 800-53 Rev. 5 SC-16** — TRANSMISSION OF SECURITY AND PRIVACY ATTRIBUTES

- Issued by: National Institute of Standards and Technology
- Publication: NIST SP 800-53 Rev. 5 — Security and Privacy Controls for Information Systems and Organizations ([nist-sp-800-53-r5](./nist-sp-800-53-r5.md))
- Version: Rev. 5 (September 2020, includes updates as of 2020-12-10)
- Text as of: 2026-11-12
- Cited by held documents: 1 time (arc-ampe ×1)
- Reproduction basis: 17 U.S.C. § 105 — work of the U.S. government (NIST). Determined per document on 2026-11-12 against the publication itself, not assumed from its issuer: its Authority statement (PDF page 3) reads "This publication may be used by nongovernmental organizations on a voluntary basis and is not subject to copyright in the United States. Attribution would, however, be appreciated by NIST." Held here: the front matter and Chapter Three (the control catalog) only. Chapter Three names ISO/IEC standards solely as bibliographic references and reproduces none of their text. NOT mirrored: the References bibliography and Appendices A-C; Appendix A (glossary) adapts third-party definitions (ISO/IEC 15026, ISO 25237, ISO/IEC 29100, ISO 15288, IETF RFC 4949), which ADR-0002 treats as not reproducible by being incorporated, and whose reproducibility has not been determined.


_NON-AUTHORITATIVE copy of one control, cut from the SP 800-53 Rev. 5 snapshot this corpus holds. Whether and how this binds a given agency depends on the instrument that incorporates it — read it at the source URL before relying on it. This copy is the Rev. 5 text of record, which is not necessarily the text a citing document meant (a document citing Rev. 4 is not answered by it)._


## Full text

### SC-16 TRANSMISSION OF SECURITY AND PRIVACY ATTRIBUTES
Control:  Associate [Assignment: organization-defined security and privacy attributes] with
information exchanged between systems and between system components.
Discussion:  Security and privacy attributes can be explicitly or implicitly associated with the
information contained in organizational systems or system components. Attributes are
abstractions that represent the basic properties or characteristics of an entity with respect to
protecting information or the management of personally identifiable information. Attributes are
typically associated with internal data structures, including records, buffers, and files within the
system. Security and privacy attributes are used to implement access control and information
flow control policies; reflect special dissemination, management, or distribution instructions,
including permitted uses of personally identifiable information; or support other aspects of the
information security and privacy policies. Privacy attributes may be used independently or in
conjunction with security attributes.
Related Controls:  AC-3, AC-4, AC-16.
Control Enhancements:
CHAPTER THREE   PAGE 311
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
(1) TRANSMISSION OF SECURITY AND PRIVACY ATTRIBUTES | INTEGRITY VERIFICATION
Verify the integrity of transmitted security and privacy attributes.
Discussion:  Part of verifying the integrity of transmitted information is ensuring that security
and privacy attributes that are associated with such information have not been modified in
an unauthorized manner. Unauthorized modification of security or privacy attributes can
result in a loss of integrity for transmitted information.
Related Controls:  AU-10, SC-8.
(2) TRANSMISSION OF SECURITY AND PRIVACY ATTRIBUTES | ANTI-SPOOFING MECHANISMS
Implement anti-spoofing mechanisms to prevent adversaries from falsifying the security
attributes indicating the successful application of the security process.
Discussion:  Some attack vectors operate by altering the security attributes of an information
system to intentionally and maliciously implement an insufficient level of security within the
system. The alteration of attributes leads organizations to believe that a greater number of
security functions are in place and operational than have actually been implemented.
Related Controls:  SI-3, SI-4, SI-7.
(3) TRANSMISSION OF SECURITY AND PRIVACY ATTRIBUTES | CRYPTOGRAPHIC BINDING
Implement [Assignment: organization-defined mechanisms or techniques] to bind security
and privacy attributes to transmitted information.
Discussion:  Cryptographic mechanisms and techniques can provide strong security and
privacy attribute binding to transmitted information to help ensure the integrity of such
information.
Related Controls:  AC-16, SC-12, SC-13.
References:  [OMB A-130].
