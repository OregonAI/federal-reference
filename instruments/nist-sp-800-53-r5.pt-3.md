---
schema_version: 1
corpus: federal-reference
jurisdiction: us
id: nist-sp-800-53-r5.pt-3
title: NIST SP 800-53 Rev. 5 PT-3 — PERSONALLY IDENTIFIABLE INFORMATION PROCESSING PURPOSES
doc_type: federal_instrument
citation: NIST SP 800-53 Rev. 5 PT-3
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

**NIST SP 800-53 Rev. 5 PT-3** — PERSONALLY IDENTIFIABLE INFORMATION PROCESSING PURPOSES

- Issued by: National Institute of Standards and Technology
- Publication: NIST SP 800-53 Rev. 5 — Security and Privacy Controls for Information Systems and Organizations ([nist-sp-800-53-r5](./nist-sp-800-53-r5.md))
- Version: Rev. 5 (September 2020, includes updates as of 2020-12-10)
- Text as of: 2026-11-12
- Cited by held documents: 3 times (arc-ampe ×3)
- Reproduction basis: 17 U.S.C. § 105 — work of the U.S. government (NIST). Determined per document on 2026-11-12 against the publication itself, not assumed from its issuer: its Authority statement (PDF page 3) reads "This publication may be used by nongovernmental organizations on a voluntary basis and is not subject to copyright in the United States. Attribution would, however, be appreciated by NIST." Held here: the front matter and Chapter Three (the control catalog) only. Chapter Three names ISO/IEC standards solely as bibliographic references and reproduces none of their text. NOT mirrored: the References bibliography and Appendices A-C; Appendix A (glossary) adapts third-party definitions (ISO/IEC 15026, ISO 25237, ISO/IEC 29100, ISO 15288, IETF RFC 4949), which ADR-0002 treats as not reproducible by being incorporated, and whose reproducibility has not been determined.


_NON-AUTHORITATIVE copy of one control, cut from the SP 800-53 Rev. 5 snapshot this corpus holds. Whether and how this binds a given agency depends on the instrument that incorporates it — read it at the source URL before relying on it. This copy is the Rev. 5 text of record, which is not necessarily the text a citing document meant (a document citing Rev. 4 is not answered by it)._


## Full text

### PT-3 PERSONALLY IDENTIFIABLE INFORMATION PROCESSING PURPOSES
Control:
a. Identify and document the [Assignment: organization-defined purpose(s)] for processing
personally identifiable information;
b. Describe the purpose(s) in the public privacy notices and policies of the organization;
c. Restrict the [Assignment: organization-defined processing] of personally identifiable
information to only that which is compatible with the identified purpose(s); and
d. Monitor changes in processing personally identifiable information and implement
[Assignment: organization-defined mechanisms] to ensure that any changes are made in
accordance with [Assignment: organization-defined requirements].
Discussion:  Identifying and documenting the purpose for processing provides organizations with
a basis for understanding why personally identifiable information may be processed. The term
“process” includes every step of the information life cycle, including creation, collection, use,
processing, storage, maintenance, dissemination, disclosure, and disposal. Identifying and
documenting the purpose of processing is a prerequisite to enabling owners and operators of the
system and individuals whose information is processed by the system to understand how the
information will be processed. This enables individuals to make informed decisions about their
engagement with information systems and organizations and to manage their privacy interests.
Once the specific processing purpose has been identified, the purpose is described in the
organization’s privacy notices, policies, and any related privacy compliance documentation,
including privacy impact assessments, system of records notices, [
PRIVACT] statements,
computer matching notices, and other applicable Federal Register notices.
Organizations take steps to help ensure that personally identifiable information is processed only
for identified purposes, including training organizational personnel and monitoring and auditing
organizational processing of personally identifiable information.
Organizations monitor for changes in personally identifiable information processing.
Organizational personnel consult with the senior agency official for privacy and legal counsel to
ensure that any new purposes that arise from changes in processing are compatible with the
purpose for which the information was collected, or if the new purpose is not compatible,
implement mechanisms in accordance with defined requirements to allow for the new
processing, if appropriate. Mechanisms may include obtaining consent from individuals, revising
privacy policies, or other measures to manage privacy risks that arise from changes in personally
identifiable information processing purposes.
Related Controls:  AC-2, AC-3, AT-3, CM-13, IR-9, PM-9, PM-25, PT-2, PT-5, PT-6, PT-7, RA-8,
SC-
43, SI-12, SI-18.
CHAPTER THREE   PAGE 232
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
Control Enhancements:
(1) PERSONALLY IDENTIFIABLE INFORMATION PROCESSING PURPOSES | DATA TAGGING
Attach data tags containing the following purposes to [Assignment: organization-defined
elements of personally identifiable information]: [Assignment: organization-defined
processing purposes].
Discussion:  Data tags support the tracking of processing purposes by conveying the
purposes along with the relevant elements of personally identifiable information throughout
the system. By conveying the processing purposes in a data tag along with the personally
identifiable information as the information transits a system, a system owner or operator
can identify whether a change in processing would be compatible with the identified and
documented purposes. Data tags may also support the use of automated tools.
Related Controls:  CA-6, CM-12, PM-5, PM-22, SC-16, SC-43, SI-10, SI-15, SI-19.
(2) PERSONALLY IDENTIFIABLE INFORMATION PROCESSING PURPOSES | AUTOMATION
Track processing purposes of personally identifiable information using [Assignment:
organization-defined automated mechanisms].
Discussion:  Automated mechanisms augment tracking of the processing purposes.
Related Controls:  CA-6, CM-12, PM-5, PM-22, SC-16, SC-43, SI-10, SI-15, SI-19.
References:  [PRIVACT], [OMB A-130], [IR 8112].
