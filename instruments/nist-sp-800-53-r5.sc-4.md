---
schema_version: 1
corpus: federal-reference
jurisdiction: us
id: nist-sp-800-53-r5.sc-4
title: NIST SP 800-53 Rev. 5 SC-4 — INFORMATION IN SHARED SYSTEM RESOURCES
doc_type: federal_instrument
citation: NIST SP 800-53 Rev. 5 SC-4
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

**NIST SP 800-53 Rev. 5 SC-4** — INFORMATION IN SHARED SYSTEM RESOURCES

- Issued by: National Institute of Standards and Technology
- Publication: NIST SP 800-53 Rev. 5 — Security and Privacy Controls for Information Systems and Organizations ([nist-sp-800-53-r5](./nist-sp-800-53-r5.md))
- Version: Rev. 5 (September 2020, includes updates as of 2020-12-10)
- Text as of: 2026-11-12
- Cited by held documents: 12 times (cjis-sp-6-1 ×7, irs-pub-1075-11-2021 ×4, 6-cfr-37 ×1)
- Reproduction basis: 17 U.S.C. § 105 — work of the U.S. government (NIST). Determined per document on 2026-11-12 against the publication itself, not assumed from its issuer: its Authority statement (PDF page 3) reads "This publication may be used by nongovernmental organizations on a voluntary basis and is not subject to copyright in the United States. Attribution would, however, be appreciated by NIST." Held here: the front matter and Chapter Three (the control catalog) only. Chapter Three names ISO/IEC standards solely as bibliographic references and reproduces none of their text. NOT mirrored: the References bibliography and Appendices A-C; Appendix A (glossary) adapts third-party definitions (ISO/IEC 15026, ISO 25237, ISO/IEC 29100, ISO 15288, IETF RFC 4949), which ADR-0002 treats as not reproducible by being incorporated, and whose reproducibility has not been determined.


_NON-AUTHORITATIVE copy of one control, cut from the SP 800-53 Rev. 5 snapshot this corpus holds. Whether and how this binds a given agency depends on the instrument that incorporates it — read it at the source URL before relying on it. This copy is the Rev. 5 text of record, which is not necessarily the text a citing document meant (a document citing Rev. 4 is not answered by it)._


## Full text

### SC-4 INFORMATION IN SHARED SYSTEM RESOURCES
Control:  Prevent unauthorized and unintended information transfer via shared system
resources.
Discussion:  Preventing unauthorized and unintended information transfer via shared system
resources stops information produced by the actions of prior users or roles (or the actions of
processes acting on behalf of prior users or roles) from being available to current users or roles
(or current processes acting on behalf of current users or roles) that obtain access to shared
system resources after those resources have been released back to the system. Information in
shared system resources also applies to encrypted representations of information. In other
contexts, control of information in shared system resources is referred to as object reuse and
residual information protection. Information in shared system resources does not address
information remanence, which refers to the residual representation of data that has been
nominally deleted; covert channels (including storage and timing channels), where shared system
resources are manipulated to violate information flow restrictions; or components within
systems for which there are only single users or roles.
Related Controls:  AC-3, AC-4, SA-8.
Control Enhancements:
(1) INFORMATION IN SHARED SYSTEM RESOURCES | SECURITY LEVELS
[Withdrawn: Incorporated into SC-4.]
(2) INFORMATION IN SHARED SYSTEM RESOURCES | MULTILEVEL OR PERIODS PROCESSING
Prevent unauthorized information transfer via shared resources in accordance with
[Assignment: organization-defined procedures] when system processing explicitly switches
between different information classification levels or security categories.
Discussion:  Changes in processing levels can occur during multilevel or periods processing
with information at different classification levels or security categories. It can also occur
during serial reuse of hardware components at different classification levels. Organization-
defined procedures can include approved sanitization processes for electronically stored
information.
Related Controls:  None.
References:  None.
CHAPTER THREE   PAGE 296
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
