---
schema_version: 1
corpus: federal-reference
jurisdiction: us
id: nist-sp-800-53-r5.ac-21
title: NIST SP 800-53 Rev. 5 AC-21 — INFORMATION SHARING
doc_type: federal_instrument
citation: NIST SP 800-53 Rev. 5 AC-21
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

**NIST SP 800-53 Rev. 5 AC-21** — INFORMATION SHARING

- Issued by: National Institute of Standards and Technology
- Publication: NIST SP 800-53 Rev. 5 — Security and Privacy Controls for Information Systems and Organizations ([nist-sp-800-53-r5](./nist-sp-800-53-r5.md))
- Version: Rev. 5 (September 2020, includes updates as of 2020-12-10)
- Text as of: 2026-11-12
- Cited by held documents: 13 times (cjis-sp-6-1 ×7, irs-pub-1075-11-2021 ×4, 6-cfr-37 ×1, arc-ampe ×1)
- Reproduction basis: 17 U.S.C. § 105 — work of the U.S. government (NIST). Determined per document on 2026-11-12 against the publication itself, not assumed from its issuer: its Authority statement (PDF page 3) reads "This publication may be used by nongovernmental organizations on a voluntary basis and is not subject to copyright in the United States. Attribution would, however, be appreciated by NIST." Held here: the front matter and Chapter Three (the control catalog) only. Chapter Three names ISO/IEC standards solely as bibliographic references and reproduces none of their text. NOT mirrored: the References bibliography and Appendices A-C; Appendix A (glossary) adapts third-party definitions (ISO/IEC 15026, ISO 25237, ISO/IEC 29100, ISO 15288, IETF RFC 4949), which ADR-0002 treats as not reproducible by being incorporated, and whose reproducibility has not been determined.


_NON-AUTHORITATIVE copy of one control, cut from the SP 800-53 Rev. 5 snapshot this corpus holds. Whether and how this binds a given agency depends on the instrument that incorporates it — read it at the source URL before relying on it. This copy is the Rev. 5 text of record, which is not necessarily the text a citing document meant (a document citing Rev. 4 is not answered by it)._


## Full text

### AC-21 INFORMATION SHARING
Control:
a. Enable authorized users to determine whether access authorizations assigned to a sharing
partner match the information’s access and use restrictions for [Assignment: organization-
defined information sharing circumstances where user discretion is required]; and
b. Employ [Assignment: organization-defined automated mechanisms or manual processes] to
assist users in making information sharing and collaboration decisions.
Discussion:  Information sharing applies to information that may be restricted in some manner
based on some formal or administrative determination. Examples of such information include,
contract-sensitive information, classified information related to special access programs or
compartments, privileged information, proprietary information, and personally identifiable
information. Security and privacy risk assessments as well as applicable laws, regulations, and
policies can provide useful inputs to these determinations. Depending on the circumstances,
sharing partners may be defined at the individual, group, or organizational level. Information
may be defined by content, type, security category, or special access program or compartment.
Access restrictions may include non-disclosure agreements (NDA). Information flow techniques
and security attributes may be used to provide automated assistance to users making sharing
and collaboration decisions.
Related Controls:  AC-3, AC-4, AC-16, PT-2, PT-7, RA-3, SC-15.
Control Enhancements:
(1) INFORMATION SHARING | AUTOMATED DECISION SUPPORT
Employ [Assignment: organization-defined automated mechanisms] to enforce
information-sharing decisions by authorized users based on access authorizations of
sharing partners and access restrictions on information to be shared.
Discussion:  Automated mechanisms are used to enforce information sharing decisions.
Related Controls:  None.
(2) INFORMATION SHARING | INFORMATION SEARCH AND RETRIEVAL
Implement information search and retrieval services that enforce [Assignment:
organization-defined information sharing restrictions].
Discussion:  Information search and retrieval services identify information system resources
relevant to an information need.
CHAPTER THREE   PAGE 56
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
Related Controls:  None.
References:  [OMB A-130], [SP 800-150], [IR 8062].
