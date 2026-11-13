---
schema_version: 1
corpus: federal-reference
jurisdiction: us
id: nist-sp-800-53-r5.cm-10
title: NIST SP 800-53 Rev. 5 CM-10 — SOFTWARE USAGE RESTRICTIONS
doc_type: federal_instrument
citation: NIST SP 800-53 Rev. 5 CM-10
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

**NIST SP 800-53 Rev. 5 CM-10** — SOFTWARE USAGE RESTRICTIONS

- Issued by: National Institute of Standards and Technology
- Publication: NIST SP 800-53 Rev. 5 — Security and Privacy Controls for Information Systems and Organizations ([nist-sp-800-53-r5](./nist-sp-800-53-r5.md))
- Version: Rev. 5 (September 2020, includes updates as of 2020-12-10)
- Text as of: 2026-11-12
- Cited by held documents: 15 times (cjis-sp-6-1 ×10, irs-pub-1075-11-2021 ×3, 6-cfr-37 ×1, arc-ampe ×1)
- Reproduction basis: 17 U.S.C. § 105 — work of the U.S. government (NIST). Determined per document on 2026-11-12 against the publication itself, not assumed from its issuer: its Authority statement (PDF page 3) reads "This publication may be used by nongovernmental organizations on a voluntary basis and is not subject to copyright in the United States. Attribution would, however, be appreciated by NIST." Held here: the front matter and Chapter Three (the control catalog) only. Chapter Three names ISO/IEC standards solely as bibliographic references and reproduces none of their text. NOT mirrored: the References bibliography and Appendices A-C; Appendix A (glossary) adapts third-party definitions (ISO/IEC 15026, ISO 25237, ISO/IEC 29100, ISO 15288, IETF RFC 4949), which ADR-0002 treats as not reproducible by being incorporated, and whose reproducibility has not been determined.


_NON-AUTHORITATIVE copy of one control, cut from the SP 800-53 Rev. 5 snapshot this corpus holds. Whether and how this binds a given agency depends on the instrument that incorporates it — read it at the source URL before relying on it. This copy is the Rev. 5 text of record, which is not necessarily the text a citing document meant (a document citing Rev. 4 is not answered by it)._


## Full text

### CM-10 SOFTWARE USAGE RESTRICTIONS
Control:
a. Use software and associated documentation in accordance with contract agreements and
copyright laws;
b. Track the use of software and associated documentation protected by quantity licenses to
control copying and distribution; and
c. Control and document the use of peer-to-peer file sharing technology to ensure that this
capability is not used for the unauthorized distribution, display, performance, or
reproduction of copyrighted work.
Discussion:  Software license tracking can be accomplished by manual or automated methods,
depending on organizational needs. Examples of contract agreements include software license
agreements and non-disclosure agreements.
Related Controls:  AC-17, AU-6, CM-7, CM-8, PM-30, SC-7.
CHAPTER THREE   PAGE 112
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
Control Enhancements:
(1) SOFTWARE USAGE RESTRICTIONS | OPEN-SOURCE SOFTWARE
Establish the following restrictions on the use of open-source software: [Assignment:
organization-defined restrictions].
Discussion:  Open-source software refers to software that is available in source code form.
Certain software rights normally reserved for copyright holders are routinely provided under
software license agreements that permit individuals to study, change, and improve the
software. From a security perspective, the major advantage of open-source software is that
it provides organizations with the ability to examine the source code. In some cases, there is
an online community associated with the software that inspects, tests,  updates, and reports
on issues found in software on an ongoing basis. However, remediating vulnerabilities in
open-source software may be problematic. There may also be licensing issues associated
with open-source software, including the constraints on derivative use of such software.
Open-source software that is available only in binary form may increase the level of risk in
using such software.
Related Controls:  SI-7.
References:  None.
