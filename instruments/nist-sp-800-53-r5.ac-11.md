---
schema_version: 1
corpus: federal-reference
jurisdiction: us
id: nist-sp-800-53-r5.ac-11
title: NIST SP 800-53 Rev. 5 AC-11 — DEVICE LOCK
doc_type: federal_instrument
citation: NIST SP 800-53 Rev. 5 AC-11
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

**NIST SP 800-53 Rev. 5 AC-11** — DEVICE LOCK

- Issued by: National Institute of Standards and Technology
- Publication: NIST SP 800-53 Rev. 5 — Security and Privacy Controls for Information Systems and Organizations ([nist-sp-800-53-r5](./nist-sp-800-53-r5.md))
- Version: Rev. 5 (September 2020, includes updates as of 2020-12-10)
- Text as of: 2026-11-12
- Cited by held documents: 15 times (cjis-sp-6-1 ×10, irs-pub-1075-11-2021 ×3, 6-cfr-37 ×2)
- Reproduction basis: 17 U.S.C. § 105 — work of the U.S. government (NIST). Determined per document on 2026-11-12 against the publication itself, not assumed from its issuer: its Authority statement (PDF page 3) reads "This publication may be used by nongovernmental organizations on a voluntary basis and is not subject to copyright in the United States. Attribution would, however, be appreciated by NIST." Held here: the front matter and Chapter Three (the control catalog) only. Chapter Three names ISO/IEC standards solely as bibliographic references and reproduces none of their text. NOT mirrored: the References bibliography and Appendices A-C; Appendix A (glossary) adapts third-party definitions (ISO/IEC 15026, ISO 25237, ISO/IEC 29100, ISO 15288, IETF RFC 4949), which ADR-0002 treats as not reproducible by being incorporated, and whose reproducibility has not been determined.


_NON-AUTHORITATIVE copy of one control, cut from the SP 800-53 Rev. 5 snapshot this corpus holds. Whether and how this binds a given agency depends on the instrument that incorporates it — read it at the source URL before relying on it. This copy is the Rev. 5 text of record, which is not necessarily the text a citing document meant (a document citing Rev. 4 is not answered by it)._


## Full text

### AC-11 DEVICE LOCK
Control:
a. Prevent further access to the system by [Selection (one or more): initiating a device lock after
[Assignment: organization-defined time period] of inactivity; requiring the user to initiate a
device lock before leaving the system unattended]; and
b. Retain the device lock until the user reestablishes access using established identification and
authentication procedures.
Discussion:  Device locks are temporary actions taken to prevent logical access to organizational
systems when users stop work and move away from the immediate vicinity of those systems but
do not want to log out because of the temporary nature of their absences. Device locks can be
implemented at the operating system level or at the application level. A proximity lock may be
used to initiate the device lock (e.g., via a Bluetooth-enabled device or dongle). User-initiated
device locking is behavior or policy-based and, as such, requires users to take physical action to
initiate the device lock. Device locks are not an acceptable substitute for logging out of systems,
such as when organizations require users to log out at the end of workdays.
Related Controls:  AC-2, AC-7, IA-11, PL-4.
Control Enhancements:
(1) DEVICE LOCK | PATTERN-HIDING DISPLAYS
Conceal, via the device lock, information previously visible on the display with a publicly
viewable image.
CHAPTER THREE   PAGE 43
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
Discussion:  The pattern-hiding display can include static or dynamic images, such as
patterns used with screen savers, photographic images, solid colors, clock, battery life
indicator, or a blank screen with the caveat that controlled unclassified information is not
displayed.
Related Controls:  None.
References:  None.
