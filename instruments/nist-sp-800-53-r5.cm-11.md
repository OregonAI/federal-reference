---
schema_version: 1
corpus: federal-reference
jurisdiction: us
id: nist-sp-800-53-r5.cm-11
title: NIST SP 800-53 Rev. 5 CM-11 — USER-INSTALLED SOFTWARE
doc_type: federal_instrument
citation: NIST SP 800-53 Rev. 5 CM-11
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

**NIST SP 800-53 Rev. 5 CM-11** — USER-INSTALLED SOFTWARE

- Issued by: National Institute of Standards and Technology
- Publication: NIST SP 800-53 Rev. 5 — Security and Privacy Controls for Information Systems and Organizations ([nist-sp-800-53-r5](./nist-sp-800-53-r5.md))
- Version: Rev. 5 (September 2020, includes updates as of 2020-12-10)
- Text as of: 2026-11-12
- Cited by held documents: 23 times (cjis-sp-6-1 ×18, irs-pub-1075-11-2021 ×3, 6-cfr-37 ×1, arc-ampe ×1)
- Reproduction basis: 17 U.S.C. § 105 — work of the U.S. government (NIST). Determined per document on 2026-11-12 against the publication itself, not assumed from its issuer: its Authority statement (PDF page 3) reads "This publication may be used by nongovernmental organizations on a voluntary basis and is not subject to copyright in the United States. Attribution would, however, be appreciated by NIST." Held here: the front matter and Chapter Three (the control catalog) only. Chapter Three names ISO/IEC standards solely as bibliographic references and reproduces none of their text. NOT mirrored: the References bibliography and Appendices A-C; Appendix A (glossary) adapts third-party definitions (ISO/IEC 15026, ISO 25237, ISO/IEC 29100, ISO 15288, IETF RFC 4949), which ADR-0002 treats as not reproducible by being incorporated, and whose reproducibility has not been determined.


_NON-AUTHORITATIVE copy of one control, cut from the SP 800-53 Rev. 5 snapshot this corpus holds. Whether and how this binds a given agency depends on the instrument that incorporates it — read it at the source URL before relying on it. This copy is the Rev. 5 text of record, which is not necessarily the text a citing document meant (a document citing Rev. 4 is not answered by it)._


## Full text

### CM-11 USER-INSTALLED SOFTWARE
Control:
a. Establish [Assignment: organization-defined policies] governing the installation of software
by users;
b. Enforce software installation policies through the following methods: [Assignment:
organization-defined methods]; and
c. Monitor policy compliance [Assignment: organization-defined frequency].
Discussion:  If provided the necessary privileges, users can install software in organizational
systems. To maintain control over the software installed, organizations identify permitted and
prohibited actions regarding software installation. Permitted software installations include
updates and security patches to existing software and downloading new applications from
organization-approved “app stores.” Prohibited software installations include software with
unknown or suspect pedigrees or software that organizations consider potentially malicious.
Policies selected for governing user-installed software are organization-developed or provided by
some external entity. Policy enforcement methods can include procedural methods and
automated methods.
Related Controls:  AC-3, AU-6, CM-2, CM-3, CM-5, CM-6, CM-7, CM-8, PL-4, SI-4, SI-7.
Control Enhancements:
(1) USER-INSTALLED SOFTWARE | ALERTS FOR UNAUTHORIZED INSTALLATIONS
[Withdrawn: Incorporated into CM-8(3).]
(2) USER-INSTALLED SOFTWARE | SOFTWARE INSTALLATION WITH PRIVILEGED STATUS
Allow user installation of software only with explicit privileged status.
Discussion:  Privileged status can be obtained, for example, by serving in the role of system
administrator.
Related Controls:  AC-5, AC-6.
(3) USER-INSTALLED SOFTWARE | AUTOMATED ENFORCEMENT AND MONITORING
CHAPTER THREE   PAGE 113
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
Enforce and monitor compliance with software installation policies using [Assignment:
organization-defined automated mechanisms].
Discussion:  Organizations enforce and monitor compliance with software installation
policies using automated mechanisms to more quickly detect and respond to unauthorized
software installation which can be an indicator of an internal or external hostile attack.
Related Controls:  None.
References:  None.
