---
schema_version: 1
corpus: federal-reference
jurisdiction: us
id: nist-sp-800-53-r5.sa-5
title: NIST SP 800-53 Rev. 5 SA-5 — SYSTEM DOCUMENTATION
doc_type: federal_instrument
citation: NIST SP 800-53 Rev. 5 SA-5
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

**NIST SP 800-53 Rev. 5 SA-5** — SYSTEM DOCUMENTATION

- Issued by: National Institute of Standards and Technology
- Publication: NIST SP 800-53 Rev. 5 — Security and Privacy Controls for Information Systems and Organizations ([nist-sp-800-53-r5](./nist-sp-800-53-r5.md))
- Version: Rev. 5 (September 2020, includes updates as of 2020-12-10)
- Text as of: 2026-11-12
- Cited by held documents: 24 times (cjis-sp-6-1 ×20, irs-pub-1075-11-2021 ×3, 6-cfr-37 ×1)
- Reproduction basis: 17 U.S.C. § 105 — work of the U.S. government (NIST). Determined per document on 2026-11-12 against the publication itself, not assumed from its issuer: its Authority statement (PDF page 3) reads "This publication may be used by nongovernmental organizations on a voluntary basis and is not subject to copyright in the United States. Attribution would, however, be appreciated by NIST." Held here: the front matter and Chapter Three (the control catalog) only. Chapter Three names ISO/IEC standards solely as bibliographic references and reproduces none of their text. NOT mirrored: the References bibliography and Appendices A-C; Appendix A (glossary) adapts third-party definitions (ISO/IEC 15026, ISO 25237, ISO/IEC 29100, ISO 15288, IETF RFC 4949), which ADR-0002 treats as not reproducible by being incorporated, and whose reproducibility has not been determined.


_NON-AUTHORITATIVE copy of one control, cut from the SP 800-53 Rev. 5 snapshot this corpus holds. Whether and how this binds a given agency depends on the instrument that incorporates it — read it at the source URL before relying on it. This copy is the Rev. 5 text of record, which is not necessarily the text a citing document meant (a document citing Rev. 4 is not answered by it)._


> **Release 5.2.0 postdates this text.** NIST's listing of record ([https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final)) says that on 2025-08-27 it issued release 5.2.0 of SP 800-53, which updates the control discussion for this control. The text below is the Rev. 5 PDF of record and does NOT include that change; read NIST's own list of the changes ([summary](https://csrc.nist.gov/files/projects/Risk-Management/800-53%20Comment%20Site/SP800-53-r5.2.0-changes.pdf)) before relying on this control's text.


## Full text

### SA-5 SYSTEM DOCUMENTATION
Control:
a. Obtain or develop administrator documentation for the system, system component, or
system service that describes:
1. Secure configuration, installation, and operation of the system, component, or service;
2. Effective use and maintenance of security and privacy functions and mechanisms; and
3. Known vulnerabilities regarding configuration and use of administrative or privileged
functions;
b. Obtain or develop user documentation for the system, system component, or system service
that describes:
1. User-accessible security and privacy functions and mechanisms and how to effectively
use those functions and mechanisms;
2. Methods for user interaction, which enables individuals to use the system, component,
or service in a more secure manner and protect individual privacy; and
3. User responsibilities in maintaining the security of the system, component, or service
and privacy of individuals;
c. Document attempts to obtain system, system component, or system service documentation
when such documentation is either unavailable or nonexistent and take [Assignment:
organization-defined actions] in response; and
d. Distribute documentation to [Assignment: organization-defined personnel or roles].
Discussion:  System documentation helps personnel understand the implementation and
operation of controls. Organizations consider establishing specific measures to determine the
quality and completeness of the content provided. System documentation may be used to
support the management of supply chain risk, incident response, and other functions. Personnel
or roles that require documentation include system owners, system security officers, and system
administrators. Attempts to obtain documentation include contacting manufacturers or suppliers
and conducting web-based searches. The inability to obtain documentation may occur due to the
age of the system or component or the lack of support from developers and contractors. When
documentation cannot be obtained, organizations may need to recreate the documentation if it
is essential to the implementation or operation of the controls. The protection provided for the
documentation is commensurate with the security category or classification of the system.
Documentation that addresses system vulnerabilities may require an increased level of
protection. Secure operation of the system includes initially starting the system and resuming
secure system operation after a lapse in system operation.
Related Controls:  CM-4, CM-6, CM-7, CM-8, PL-2, PL-4, PL-8, PS-2, SA-3, SA-4, SA-8, SA-9, SA-10,
SA-11, SA-15, SA-16, SA-17, SI-12, SR-3.
Control Enhancements:
(1) SYSTEM DOCUMENTATION | FUNCTIONAL PROPERTIES OF SECURITY CONTROLS
[Withdrawn: Incorporated into SA-4(1).]
(2) SYSTEM DOCUMENTATION | SECURITY-RELEVANT EXTERNAL SYSTEM INTERFACES
[Withdrawn: Incorporated into SA-4(2).]
(3) SYSTEM DOCUMENTATION | HIGH-LEVEL DESIGN
[Withdrawn: Incorporated into SA-4(2).]
CHAPTER THREE   PAGE 257
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
(4) SYSTEM DOCUMENTATION | LOW-LEVEL DESIGN
[Withdrawn: Incorporated into SA-4(2).]
(5) SYSTEM DOCUMENTATION | SOURCE CODE
[Withdrawn: Incorporated into SA-4(2).]
References:  [SP 800-160-1].
