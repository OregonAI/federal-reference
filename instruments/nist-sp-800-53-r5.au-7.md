---
schema_version: 1
corpus: federal-reference
jurisdiction: us
id: nist-sp-800-53-r5.au-7
title: NIST SP 800-53 Rev. 5 AU-7 — AUDIT RECORD REDUCTION AND REPORT GENERATION
doc_type: federal_instrument
citation: NIST SP 800-53 Rev. 5 AU-7
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

**NIST SP 800-53 Rev. 5 AU-7** — AUDIT RECORD REDUCTION AND REPORT GENERATION

- Issued by: National Institute of Standards and Technology
- Publication: NIST SP 800-53 Rev. 5 — Security and Privacy Controls for Information Systems and Organizations ([nist-sp-800-53-r5](./nist-sp-800-53-r5.md))
- Version: Rev. 5 (September 2020, includes updates as of 2020-12-10)
- Text as of: 2026-11-12
- Cited by held documents: 20 times (cjis-sp-6-1 ×14, irs-pub-1075-11-2021 ×4, 6-cfr-37 ×2), 1 of them naming an enhancement of this control
- Reproduction basis: 17 U.S.C. § 105 — work of the U.S. government (NIST). Determined per document on 2026-11-12 against the publication itself, not assumed from its issuer: its Authority statement (PDF page 3) reads "This publication may be used by nongovernmental organizations on a voluntary basis and is not subject to copyright in the United States. Attribution would, however, be appreciated by NIST." Held here: the front matter and Chapter Three (the control catalog) only. Chapter Three names ISO/IEC standards solely as bibliographic references and reproduces none of their text. NOT mirrored: the References bibliography and Appendices A-C; Appendix A (glossary) adapts third-party definitions (ISO/IEC 15026, ISO 25237, ISO/IEC 29100, ISO 15288, IETF RFC 4949), which ADR-0002 treats as not reproducible by being incorporated, and whose reproducibility has not been determined.


_NON-AUTHORITATIVE copy of one control, cut from the SP 800-53 Rev. 5 snapshot this corpus holds. Whether and how this binds a given agency depends on the instrument that incorporates it — read it at the source URL before relying on it. This copy is the Rev. 5 text of record, which is not necessarily the text a citing document meant (a document citing Rev. 4 is not answered by it)._


## Full text

### AU-7 AUDIT RECORD REDUCTION AND REPORT GENERATION
Control:  Provide and implement an audit record reduction and report generation capability that:
a. Supports on-demand audit record review, analysis, and reporting requirements and after-
the-fact investigations of incidents; and
b. Does not alter the original content or time ordering of audit records.
Discussion:  Audit record reduction is a process that manipulates collected audit log information
and organizes it into a summary format that is more meaningful to analysts. Audit record
CHAPTER THREE   PAGE 73
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
reduction and report generation capabilities do not always emanate from the same system or
from the same organizational entities that conduct audit logging activities. The audit record
reduction capability includes modern data mining techniques with advanced data filters to
identify anomalous behavior in audit records. The report generation capability provided by the
system can generate customizable reports. Time ordering of audit records can be an issue if the
granularity of the timestamp in the record is insufficient.
Related Controls:  AC-2, AU-2, AU-3, AU-4, AU-5, AU-6, AU-12, AU-16, CM-5, IA-5, IR-4, PM-12, SI-
4.
Control Enhancements:
(1) AUDIT RECORD REDUCTION AND REPORT GENERATION | AUTOMATIC PROCESSING
Provide and implement the capability to process, sort, and search audit records for events
of interest based on the following content: [Assignment: organization-defined fields within
audit records].
Discussion:  Events of interest can be identified by the content of audit records, including
system resources involved, information objects accessed, identities of individuals, event
types, event locations, event dates and times, Internet Protocol addresses involved, or event
success or failure. Organizations may define event criteria to any degree of granularity
required, such as locations selectable by a general networking location or by specific system
component.
Related Controls:  None.
(2) AUDIT RECORD REDUCTION AND REPORT GENERATION | AUTOMATIC SORT AND SEARCH
[Withdrawn: Incorporated into AU-7(1).]
References:  None.
