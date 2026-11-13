---
schema_version: 1
corpus: federal-reference
jurisdiction: us
id: nist-sp-800-53-r5.sr-11
title: NIST SP 800-53 Rev. 5 SR-11 — COMPONENT AUTHENTICITY
doc_type: federal_instrument
citation: NIST SP 800-53 Rev. 5 SR-11
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

**NIST SP 800-53 Rev. 5 SR-11** — COMPONENT AUTHENTICITY

- Issued by: National Institute of Standards and Technology
- Publication: NIST SP 800-53 Rev. 5 — Security and Privacy Controls for Information Systems and Organizations ([nist-sp-800-53-r5](./nist-sp-800-53-r5.md))
- Version: Rev. 5 (September 2020, includes updates as of 2020-12-10)
- Text as of: 2026-11-12
- Cited by held documents: 14 times (cjis-sp-6-1 ×10, irs-pub-1075-11-2021 ×3, 6-cfr-37 ×1)
- Reproduction basis: 17 U.S.C. § 105 — work of the U.S. government (NIST). Determined per document on 2026-11-12 against the publication itself, not assumed from its issuer: its Authority statement (PDF page 3) reads "This publication may be used by nongovernmental organizations on a voluntary basis and is not subject to copyright in the United States. Attribution would, however, be appreciated by NIST." Held here: the front matter and Chapter Three (the control catalog) only. Chapter Three names ISO/IEC standards solely as bibliographic references and reproduces none of their text. NOT mirrored: the References bibliography and Appendices A-C; Appendix A (glossary) adapts third-party definitions (ISO/IEC 15026, ISO 25237, ISO/IEC 29100, ISO 15288, IETF RFC 4949), which ADR-0002 treats as not reproducible by being incorporated, and whose reproducibility has not been determined.


_NON-AUTHORITATIVE copy of one control, cut from the SP 800-53 Rev. 5 snapshot this corpus holds. Whether and how this binds a given agency depends on the instrument that incorporates it — read it at the source URL before relying on it. This copy is the Rev. 5 text of record, which is not necessarily the text a citing document meant (a document citing Rev. 4 is not answered by it)._


## Full text

### SR-11 COMPONENT AUTHENTICITY
Control:
a. Develop and implement anti-counterfeit policy and procedures that include the means to
detect and prevent counterfeit components from entering the system; and
b. Report counterfeit system components to [Selection (one or more): source of counterfeit
component; [Assignment: organization-defined external reporting organizations];
[Assignment: organization-defined personnel or roles]].
Discussion:  Sources of counterfeit components include manufacturers, developers, vendors, and
contractors. Anti-counterfeiting policies and procedures support tamper resistance and provide a
level of protection against the introduction of malicious code. External reporting organizations
include CISA.
Related Controls:  PE-3, SA-4, SI-7, SR-9, SR-10.
Control Enhancements:
(1) COMPONENT AUTHENTICITY | ANTI-COUNTERFEIT TRAINING
Train [Assignment: organization-defined personnel or roles] to detect counterfeit system
components (including hardware, software, and firmware).
Discussion:  None.
Related Controls:  AT-3.
(2) COMPONENT AUTHENTICITY | CONFIGURATION CONTROL FOR COMPONENT SERVICE AND REPAIR
Maintain configuration control over the following system components awaiting service or
repair and serviced or repaired components awaiting return to service: [Assignment:
organization-defined system components].
Discussion:  None.
Related Controls:  CM-3, MA-2, MA-4, SA-10.
(3) COMPONENT AUTHENTICITY | ANTI-COUNTERFEIT SCANNING
Scan for counterfeit system components [Assignment: organization-defined frequency].
Discussion:  The type of component determines the type of scanning to be conducted (e.g.,
web application scanning if the component is a web application).
Related Controls:  RA-5.
CHAPTER THREE   PAGE 373
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
References:  [ISO 20243].
