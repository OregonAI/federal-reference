---
schema_version: 1
corpus: federal-reference
jurisdiction: us
id: nist-sp-800-53-r5.sr-9
title: NIST SP 800-53 Rev. 5 SR-9 — TAMPER RESISTANCE AND DETECTION
doc_type: federal_instrument
citation: NIST SP 800-53 Rev. 5 SR-9
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

**NIST SP 800-53 Rev. 5 SR-9** — TAMPER RESISTANCE AND DETECTION

- Issued by: National Institute of Standards and Technology
- Publication: NIST SP 800-53 Rev. 5 — Security and Privacy Controls for Information Systems and Organizations ([nist-sp-800-53-r5](./nist-sp-800-53-r5.md))
- Version: Rev. 5 (September 2020, includes updates as of 2020-12-10)
- Text as of: 2026-11-12
- Cited by held documents: 1 time (6-cfr-37 ×1)
- Reproduction basis: 17 U.S.C. § 105 — work of the U.S. government (NIST). Determined per document on 2026-11-12 against the publication itself, not assumed from its issuer: its Authority statement (PDF page 3) reads "This publication may be used by nongovernmental organizations on a voluntary basis and is not subject to copyright in the United States. Attribution would, however, be appreciated by NIST." Held here: the front matter and Chapter Three (the control catalog) only. Chapter Three names ISO/IEC standards solely as bibliographic references and reproduces none of their text. NOT mirrored: the References bibliography and Appendices A-C; Appendix A (glossary) adapts third-party definitions (ISO/IEC 15026, ISO 25237, ISO/IEC 29100, ISO 15288, IETF RFC 4949), which ADR-0002 treats as not reproducible by being incorporated, and whose reproducibility has not been determined.


_NON-AUTHORITATIVE copy of one control, cut from the SP 800-53 Rev. 5 snapshot this corpus holds. Whether and how this binds a given agency depends on the instrument that incorporates it — read it at the source URL before relying on it. This copy is the Rev. 5 text of record, which is not necessarily the text a citing document meant (a document citing Rev. 4 is not answered by it)._


## Full text

### SR-9 TAMPER RESISTANCE AND DETECTION
Control:  Implement a tamper protection program for the system, system component, or system
service.
Discussion:  Anti-tamper technologies, tools, and techniques provide a level of protection for
systems, system components, and services against many threats, including reverse engineering,
modification, and substitution. Strong identification combined with tamper resistance and/or
tamper detection is essential to protecting systems and components during distribution and
when in use.
Related Controls:  PE-3, PM-30, SA-15, SI-4, SI-7, SR-3, SR-4, SR-5, SR-10, SR-11.
Control Enhancements:
(1) TAMPER RESISTANCE AND DETECTION | MULTIPLE STAGES OF SYSTEM DEVELOPMENT LIFE CYCLE
Employ anti-tamper technologies, tools, and techniques throughout the system
development life cycle.
Discussion:  The system development life cycle includes research and development, design,
manufacturing, acquisition, delivery, integration, operations and maintenance, and disposal.
Organizations use a combination of hardware and software techniques for tamper resistance
and detection. Organizations use obfuscation and self-checking to make reverse engineering
and modifications more difficult, time-consuming, and expensive for adversaries. The
customization of systems and system components can make substitutions easier to detect
and therefore limit damage.
Related Controls:  SA-3.
CHAPTER THREE   PAGE 372
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
References:  [ISO 20243].
