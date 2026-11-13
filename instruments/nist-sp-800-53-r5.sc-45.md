---
schema_version: 1
corpus: federal-reference
jurisdiction: us
id: nist-sp-800-53-r5.sc-45
title: NIST SP 800-53 Rev. 5 SC-45 — SYSTEM TIME SYNCHRONIZATION
doc_type: federal_instrument
citation: NIST SP 800-53 Rev. 5 SC-45
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

**NIST SP 800-53 Rev. 5 SC-45** — SYSTEM TIME SYNCHRONIZATION

- Issued by: National Institute of Standards and Technology
- Publication: NIST SP 800-53 Rev. 5 — Security and Privacy Controls for Information Systems and Organizations ([nist-sp-800-53-r5](./nist-sp-800-53-r5.md))
- Version: Rev. 5 (September 2020, includes updates as of 2020-12-10)
- Text as of: 2026-11-12
- Cited by held documents: 3 times (irs-pub-1075-11-2021 ×3)
- Reproduction basis: 17 U.S.C. § 105 — work of the U.S. government (NIST). Determined per document on 2026-11-12 against the publication itself, not assumed from its issuer: its Authority statement (PDF page 3) reads "This publication may be used by nongovernmental organizations on a voluntary basis and is not subject to copyright in the United States. Attribution would, however, be appreciated by NIST." Held here: the front matter and Chapter Three (the control catalog) only. Chapter Three names ISO/IEC standards solely as bibliographic references and reproduces none of their text. NOT mirrored: the References bibliography and Appendices A-C; Appendix A (glossary) adapts third-party definitions (ISO/IEC 15026, ISO 25237, ISO/IEC 29100, ISO 15288, IETF RFC 4949), which ADR-0002 treats as not reproducible by being incorporated, and whose reproducibility has not been determined.


_NON-AUTHORITATIVE copy of one control, cut from the SP 800-53 Rev. 5 snapshot this corpus holds. Whether and how this binds a given agency depends on the instrument that incorporates it — read it at the source URL before relying on it. This copy is the Rev. 5 text of record, which is not necessarily the text a citing document meant (a document citing Rev. 4 is not answered by it)._


## Full text

### SC-45  SYSTEM TIME SYNCHRONIZATION
Control:  Synchronize system clocks within and between systems and system components.
Discussion:  Time synchronization of system clocks is essential for the correct execution of many
system services, including identification and authentication processes that involve certificates
and time-of-day restrictions as part of access control. Denial of service or failure to deny expired
credentials may result without properly synchronized clocks within and between systems and
system components. Time is commonly expressed in Coordinated Universal Time (UTC), a
modern continuation of Greenwich Mean Time (GMT), or local time with an offset from UTC. The
granularity of time measurements refers to the degree of synchronization between system clocks
and reference clocks, such as clocks synchronizing within hundreds of milliseconds or tens of
milliseconds. Organizations may define different time granularities for system components. Time
service can be critical to other security capabilities—such as access control and identification and
authentication—depending on the nature of the mechanisms used to support the capabilities.
Related Controls:  AC-3, AU-8, IA-2, IA-8.
Control Enhancements:
(1) SYSTEM TIME SYNCHRONIZATION | SYNCHRONIZATION WITH AUTHORITATIVE TIME SOURCE
(a) Compare the internal system clocks [Assignment: organization-defined frequency]
with [Assignment: organization-defined authoritative time source]; and
CHAPTER THREE   PAGE 329
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
(b) Synchronize the internal system clocks to the authoritative time source when the time
difference is greater than [Assignment: organization-defined time period].
Discussion:  Synchronization of internal system clocks with an authoritative source provides
uniformity of time stamps for systems with multiple system clocks and systems connected
over a network.
Related Controls:  None.
(2) SYSTEM TIME SYNCHRONIZATION | SECONDARY AUTHORITATIVE TIME SOURCE
(a) Identify a secondary authoritative time source that is in a different geographic region
than the primary authoritative time source; and
(b) Synchronize the internal system clocks to the secondary authoritative time source if
the primary authoritative time source is unavailable.
Discussion:  It may be necessary to employ geolocation information to determine that the
secondary authoritative time source is in a different geographic region.
Related Controls:  None.
References:  [IETF 5905].
