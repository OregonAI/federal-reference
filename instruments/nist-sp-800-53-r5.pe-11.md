---
schema_version: 1
corpus: federal-reference
jurisdiction: us
id: nist-sp-800-53-r5.pe-11
title: NIST SP 800-53 Rev. 5 PE-11 — EMERGENCY POWER
doc_type: federal_instrument
citation: NIST SP 800-53 Rev. 5 PE-11
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

**NIST SP 800-53 Rev. 5 PE-11** — EMERGENCY POWER

- Issued by: National Institute of Standards and Technology
- Publication: NIST SP 800-53 Rev. 5 — Security and Privacy Controls for Information Systems and Organizations ([nist-sp-800-53-r5](./nist-sp-800-53-r5.md))
- Version: Rev. 5 (September 2020, includes updates as of 2020-12-10)
- Text as of: 2026-11-12
- Cited by held documents: 10 times (cjis-sp-6-1 ×5, arc-ampe ×4, 6-cfr-37 ×1)
- Reproduction basis: 17 U.S.C. § 105 — work of the U.S. government (NIST). Determined per document on 2026-11-12 against the publication itself, not assumed from its issuer: its Authority statement (PDF page 3) reads "This publication may be used by nongovernmental organizations on a voluntary basis and is not subject to copyright in the United States. Attribution would, however, be appreciated by NIST." Held here: the front matter and Chapter Three (the control catalog) only. Chapter Three names ISO/IEC standards solely as bibliographic references and reproduces none of their text. NOT mirrored: the References bibliography and Appendices A-C; Appendix A (glossary) adapts third-party definitions (ISO/IEC 15026, ISO 25237, ISO/IEC 29100, ISO 15288, IETF RFC 4949), which ADR-0002 treats as not reproducible by being incorporated, and whose reproducibility has not been determined.


_NON-AUTHORITATIVE copy of one control, cut from the SP 800-53 Rev. 5 snapshot this corpus holds. Whether and how this binds a given agency depends on the instrument that incorporates it — read it at the source URL before relying on it. This copy is the Rev. 5 text of record, which is not necessarily the text a citing document meant (a document citing Rev. 4 is not answered by it)._


## Full text

### PE-11 EMERGENCY POWER
Control:  Provide an uninterruptible power supply to facilitate [Selection (one or more): an
orderly shutdown of the system; transition of the system to long-term alternate power] in the
event of a primary power source loss.
Discussion:  An uninterruptible power supply (UPS) is an electrical system or mechanism that
provides emergency power when there is a failure of the main power source. A UPS is typically
used to protect computers, data centers, telecommunication equipment, or other electrical
equipment where an unexpected power disruption could cause injuries, fatalities, serious
mission or business disruption, or loss of data or information. A UPS differs from an emergency
power system or backup generator in that the UPS provides near-instantaneous protection from
unanticipated power interruptions from the main power source by providing energy stored in
batteries, supercapacitors, or flywheels. The battery duration of a UPS is relatively short but
provides sufficient time to start a standby power source, such as a backup generator, or properly
shut down the system.
Related Controls:  AT-3, CP-2, CP-7.
Control Enhancements:
(1) EMERGENCY POWER | ALTERNATE POWER SUPPLY — MINIMAL OPERATIONAL CAPABILITY
Provide an alternate power supply for the system that is activated [Selection: manually;
automatically] and that can maintain minimally required operational capability in the
event of an extended loss of the primary power source.
Discussion:  Provision of an alternate power supply with minimal operating capability can be
satisfied by accessing a secondary commercial power supply or other external power supply.
Related Controls:  None.
(2) EMERGENCY POWER | ALTERNATE POWER SUPPLY — SELF-CONTAINED
Provide an alternate power supply for the system that is activated [Selection: manually;
automatically] and that is:
(a) Self-contained;
CHAPTER THREE   PAGE 188
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
(b) Not reliant on external power generation; and
(c) Capable of maintaining [Selection: minimally required operational capability; full
operational capability] in the event of an extended loss of the primary power source.
Discussion:  The provision of a long-term, self-contained power supply can be satisfied by
using one or more generators with sufficient capacity to meet the needs of the organization.
Related Controls:  None.
References:  None.
