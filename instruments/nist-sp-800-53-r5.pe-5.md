---
schema_version: 1
corpus: federal-reference
jurisdiction: us
id: nist-sp-800-53-r5.pe-5
title: NIST SP 800-53 Rev. 5 PE-5 — ACCESS CONTROL FOR OUTPUT DEVICES
doc_type: federal_instrument
citation: NIST SP 800-53 Rev. 5 PE-5
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

**NIST SP 800-53 Rev. 5 PE-5** — ACCESS CONTROL FOR OUTPUT DEVICES

- Issued by: National Institute of Standards and Technology
- Publication: NIST SP 800-53 Rev. 5 — Security and Privacy Controls for Information Systems and Organizations ([nist-sp-800-53-r5](./nist-sp-800-53-r5.md))
- Version: Rev. 5 (September 2020, includes updates as of 2020-12-10)
- Text as of: 2026-11-12
- Cited by held documents: 14 times (cjis-sp-6-1 ×8, irs-pub-1075-11-2021 ×4, 6-cfr-37 ×1, arc-ampe ×1)
- Reproduction basis: 17 U.S.C. § 105 — work of the U.S. government (NIST). Determined per document on 2026-11-12 against the publication itself, not assumed from its issuer: its Authority statement (PDF page 3) reads "This publication may be used by nongovernmental organizations on a voluntary basis and is not subject to copyright in the United States. Attribution would, however, be appreciated by NIST." Held here: the front matter and Chapter Three (the control catalog) only. Chapter Three names ISO/IEC standards solely as bibliographic references and reproduces none of their text. NOT mirrored: the References bibliography and Appendices A-C; Appendix A (glossary) adapts third-party definitions (ISO/IEC 15026, ISO 25237, ISO/IEC 29100, ISO 15288, IETF RFC 4949), which ADR-0002 treats as not reproducible by being incorporated, and whose reproducibility has not been determined.


_NON-AUTHORITATIVE copy of one control, cut from the SP 800-53 Rev. 5 snapshot this corpus holds. Whether and how this binds a given agency depends on the instrument that incorporates it — read it at the source URL before relying on it. This copy is the Rev. 5 text of record, which is not necessarily the text a citing document meant (a document citing Rev. 4 is not answered by it)._


## Full text

### PE-5 ACCESS CONTROL FOR OUTPUT DEVICES
Control:  Control physical access to output from [Assignment: organization-defined output
devices] to prevent unauthorized individuals from obtaining the output.
Discussion:  Controlling physical access to output devices includes placing output devices in
locked rooms or other secured areas with keypad or card reader access controls and allowing
access to authorized individuals only, placing output devices in locations that can be monitored
by personnel, installing monitor or screen filters, and using headphones. Examples of output
devices include monitors, printers, scanners, audio devices, facsimile machines, and copiers.
Related Controls:  PE-2, PE-3, PE-4, PE-18.
Control Enhancements:
(1) ACCESS CONTROL FOR OUTPUT DEVICES | ACCESS TO OUTPUT BY AUTHORIZED INDIVIDUALS
[Withdrawn: Incorporated into PE-5.]
(2) ACCESS CONTROL FOR OUTPUT DEVICES | LINK TO INDIVIDUAL IDENTITY
Link individual identity to receipt of output from output devices.
Discussion:  Methods for linking individual identity to the receipt of output from output
devices include installing security functionality on facsimile machines, copiers, and printers.
Such functionality allows organizations to implement authentication on output devices prior
to the release of output to individuals.
CHAPTER THREE   PAGE 184
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
Related Controls:  None.
(3) ACCESS CONTROL FOR OUTPUT DEVICES | MARKING OUTPUT DEVICES
[Withdrawn: Incorporated into PE-22.]
References:  [IR 8023].
