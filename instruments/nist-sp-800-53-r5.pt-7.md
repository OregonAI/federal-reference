---
schema_version: 1
corpus: federal-reference
jurisdiction: us
id: nist-sp-800-53-r5.pt-7
title: NIST SP 800-53 Rev. 5 PT-7 — SPECIFIC CATEGORIES OF PERSONALLY IDENTIFIABLE INFORMATION
doc_type: federal_instrument
citation: NIST SP 800-53 Rev. 5 PT-7
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

**NIST SP 800-53 Rev. 5 PT-7** — SPECIFIC CATEGORIES OF PERSONALLY IDENTIFIABLE INFORMATION

- Issued by: National Institute of Standards and Technology
- Publication: NIST SP 800-53 Rev. 5 — Security and Privacy Controls for Information Systems and Organizations ([nist-sp-800-53-r5](./nist-sp-800-53-r5.md))
- Version: Rev. 5 (September 2020, includes updates as of 2020-12-10)
- Text as of: 2026-11-12
- Cited by held documents: 3 times (arc-ampe ×2, cjis-sp-6-1 ×1)
- Reproduction basis: 17 U.S.C. § 105 — work of the U.S. government (NIST). Determined per document on 2026-11-12 against the publication itself, not assumed from its issuer: its Authority statement (PDF page 3) reads "This publication may be used by nongovernmental organizations on a voluntary basis and is not subject to copyright in the United States. Attribution would, however, be appreciated by NIST." Held here: the front matter and Chapter Three (the control catalog) only. Chapter Three names ISO/IEC standards solely as bibliographic references and reproduces none of their text. NOT mirrored: the References bibliography and Appendices A-C; Appendix A (glossary) adapts third-party definitions (ISO/IEC 15026, ISO 25237, ISO/IEC 29100, ISO 15288, IETF RFC 4949), which ADR-0002 treats as not reproducible by being incorporated, and whose reproducibility has not been determined.


_NON-AUTHORITATIVE copy of one control, cut from the SP 800-53 Rev. 5 snapshot this corpus holds. Whether and how this binds a given agency depends on the instrument that incorporates it — read it at the source URL before relying on it. This copy is the Rev. 5 text of record, which is not necessarily the text a citing document meant (a document citing Rev. 4 is not answered by it)._


## Full text

### PT-7 SPECIFIC CATEGORIES OF PERSONALLY IDENTIFIABLE INFORMATION
Control: Apply [Assignment: organization-defined processing conditions] for specific categories of
personally identifiable information.
Discussion:  Organizations apply any conditions or protections that may be necessary for specific
categories of personally identifiable information. These conditions may be required by laws,
executive orders, directives, regulations, policies, standards, or guidelines. The requirements may
also come from the results of privacy risk assessments that factor in contextual changes that may
result in an organizational determination that a particular category of personally identifiable
information is particularly sensitive or raises particular privacy risks. Organizations consult with
the senior agency official for privacy and legal counsel regarding any protections that may be
necessary.
Related Controls:  IR-9, PT-2, PT-3, RA-3.
Control Enhancements:
(1) SPECIFIC CATEGORIES OF PERSONALLY IDENTIFIABLE INFORMATION | SOCIAL SECURITY NUMBERS
When a system processes Social Security numbers:
(a) Eliminate unnecessary collection, maintenance, and use of Social Security numbers,
and explore alternatives to their use as a personal identifier;
(b) Do not deny any individual any right, benefit, or privilege provided by law because of
such individual’s refusal to disclose his or her Social Security number; and
(c) Inform any individual who is asked to disclose his or her Social Security number
whether that disclosure is mandatory or voluntary, by what statutory or other
authority such number is solicited, and what uses will be made of it.
Discussion:  Federal law and policy establish specific requirements for organizations’
processing of Social Security numbers. Organizations take steps to eliminate unnecessary
uses of Social Security numbers and other sensitive information and observe any particular
requirements that apply.
Related Controls:  IA-4.
(2) SPECIFIC CATEGORIES OF PERSONALLY IDENTIFIABLE INFORMATION | FIRST AMENDMENT
INFORMATION
Prohibit the processing of information describing how any individual exercises rights
guaranteed by the First Amendment unless expressly authorized by statute or by the
individual or unless pertinent to and within the scope of an authorized law enforcement
activity.
Discussion:  The [PRIVACT] limits agencies’ ability to process information that describes how
individuals exercise rights guaranteed by the First Amendment. Organizations consult with
the senior agency official for privacy and legal counsel regarding these requirements.
Related Controls:  None.
References:  [PRIVACT], [OMB A-130], [OMB A-108], [NARA CUI].
CHAPTER THREE   PAGE 237
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
