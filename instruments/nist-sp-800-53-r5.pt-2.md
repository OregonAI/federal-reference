---
schema_version: 1
corpus: federal-reference
jurisdiction: us
id: nist-sp-800-53-r5.pt-2
title: NIST SP 800-53 Rev. 5 PT-2 — AUTHORITY TO PROCESS PERSONALLY IDENTIFIABLE INFORMATION
doc_type: federal_instrument
citation: NIST SP 800-53 Rev. 5 PT-2
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

**NIST SP 800-53 Rev. 5 PT-2** — AUTHORITY TO PROCESS PERSONALLY IDENTIFIABLE INFORMATION

- Issued by: National Institute of Standards and Technology
- Publication: NIST SP 800-53 Rev. 5 — Security and Privacy Controls for Information Systems and Organizations ([nist-sp-800-53-r5](./nist-sp-800-53-r5.md))
- Version: Rev. 5 (September 2020, includes updates as of 2020-12-10)
- Text as of: 2026-11-12
- Cited by held documents: 6 times (arc-ampe ×3, irs-pub-1075-11-2021 ×3)
- Reproduction basis: 17 U.S.C. § 105 — work of the U.S. government (NIST). Determined per document on 2026-11-12 against the publication itself, not assumed from its issuer: its Authority statement (PDF page 3) reads "This publication may be used by nongovernmental organizations on a voluntary basis and is not subject to copyright in the United States. Attribution would, however, be appreciated by NIST." Held here: the front matter and Chapter Three (the control catalog) only. Chapter Three names ISO/IEC standards solely as bibliographic references and reproduces none of their text. NOT mirrored: the References bibliography and Appendices A-C; Appendix A (glossary) adapts third-party definitions (ISO/IEC 15026, ISO 25237, ISO/IEC 29100, ISO 15288, IETF RFC 4949), which ADR-0002 treats as not reproducible by being incorporated, and whose reproducibility has not been determined.


_NON-AUTHORITATIVE copy of one control, cut from the SP 800-53 Rev. 5 snapshot this corpus holds. Whether and how this binds a given agency depends on the instrument that incorporates it — read it at the source URL before relying on it. This copy is the Rev. 5 text of record, which is not necessarily the text a citing document meant (a document citing Rev. 4 is not answered by it)._


## Full text

### PT-2 AUTHORITY TO PROCESS PERSONALLY IDENTIFIABLE INFORMATION
Control:
a. Determine and document the [Assignment: organization-defined authority] that permits the
[Assignment: organization-defined processing] of personally identifiable information; and
b. Restrict the [Assignment: organization-defined processing] of personally identifiable
information to only that which is authorized.
Discussion:  The processing of personally identifiable information is an operation or set of
operations that the information system or organization performs with respect to personally
identifiable information across the information life cycle. Processing includes but is not limited to
creation, collection, use, processing, storage, maintenance, dissemination, disclosure, and
disposal. Processing operations also include logging, generation, and transformation, as well as
analysis techniques, such as data mining.
Organizations may be subject to laws, executive orders, directives, regulations, or policies that
establish the organization’s authority and thereby limit certain types of processing of personally
identifiable information or establish other requirements related to the processing. Organizational
personnel consult with the senior agency official for privacy and legal counsel regarding such
authority, particularly if the organization is subject to multiple jurisdictions or sources of
authority. For organizations whose processing is not determined according to legal authorities,
the organization’s policies and determinations govern how they process personally identifiable
information. While processing of personally identifiable information may be legally permissible,
privacy risks may still arise. Privacy risk assessments can identify the privacy risks associated with
the authorized processing of personally identifiable information and support solutions to manage
such risks.
Organizations consider applicable requirements and organizational policies to determine how to
document this authority. For federal agencies, the authority to process personally identifiable
information is documented in privacy policies and notices, system of records notices, privacy
impact assessments, [PRIVACT] statements, computer matching agreements and notices,
contracts, information sharing agreements, memoranda of understanding, and other
documentation.
Organizations take steps to ensure that personally identifiable information is only processed for
authorized purposes, including training organizational personnel on the authorized processing of
personally identifiable information and monitoring and auditing organizational use of personally
identifiable information.
Related Controls:  AC-2, AC-3, CM-13, IR-9, PM-9, PM-24, PT-1, PT-3, PT-5, PT-6, RA-3, RA-8,
SI-
12, SI-18.
Control Enhancements:
(1) AUTHORITY TO PROCESS PERSONALLY IDENTIFIABLE INFORMATION | DATA TAGGING
Attach data tags containing [Assignment: organization-defined authorized processing] to
[Assignment: organization-defined elements of personally identifiable information].
Discussion:  Data tags support the tracking and enforcement of authorized processing by
conveying the types of processing that are authorized along with the relevant elements of
CHAPTER THREE   PAGE 231
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
personally identifiable information throughout the system. Data tags may also support the
use of automated tools.
Related Controls:  AC-16, CA-6, CM-12, PM-5, PM-22, PT-4, SC-16, SC-43, SI-10, SI-15, SI-19.
(2) AUTHORITY TO PROCESS PERSONALLY IDENTIFIABLE INFORMATION | AUTOMATION
Manage enforcement of the authorized processing of personally identifiable information
using [Assignment: organization-defined automated mechanisms].
Discussion:  Automated mechanisms augment verification that only authorized processing is
occurring.
Related Controls:  CA-6, CM-12, PM-5, PM-22, PT-4, SC-16, SC-43, SI-10, SI-15, SI-19.
References:  [PRIVACT], [OMB A-130], [IR 8112].
