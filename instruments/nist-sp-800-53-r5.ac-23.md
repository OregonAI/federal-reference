---
schema_version: 1
corpus: federal-reference
jurisdiction: us
id: nist-sp-800-53-r5.ac-23
title: NIST SP 800-53 Rev. 5 AC-23 — DATA MINING PROTECTION
doc_type: federal_instrument
citation: NIST SP 800-53 Rev. 5 AC-23
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

**NIST SP 800-53 Rev. 5 AC-23** — DATA MINING PROTECTION

- Issued by: National Institute of Standards and Technology
- Publication: NIST SP 800-53 Rev. 5 — Security and Privacy Controls for Information Systems and Organizations ([nist-sp-800-53-r5](./nist-sp-800-53-r5.md))
- Version: Rev. 5 (September 2020, includes updates as of 2020-12-10)
- Text as of: 2026-11-12
- Cited by held documents: 5 times (irs-pub-1075-11-2021 ×4, cjis-sp-6-1 ×1)
- Reproduction basis: 17 U.S.C. § 105 — work of the U.S. government (NIST). Determined per document on 2026-11-12 against the publication itself, not assumed from its issuer: its Authority statement (PDF page 3) reads "This publication may be used by nongovernmental organizations on a voluntary basis and is not subject to copyright in the United States. Attribution would, however, be appreciated by NIST." Held here: the front matter and Chapter Three (the control catalog) only. Chapter Three names ISO/IEC standards solely as bibliographic references and reproduces none of their text. NOT mirrored: the References bibliography and Appendices A-C; Appendix A (glossary) adapts third-party definitions (ISO/IEC 15026, ISO 25237, ISO/IEC 29100, ISO 15288, IETF RFC 4949), which ADR-0002 treats as not reproducible by being incorporated, and whose reproducibility has not been determined.


_NON-AUTHORITATIVE copy of one control, cut from the SP 800-53 Rev. 5 snapshot this corpus holds. Whether and how this binds a given agency depends on the instrument that incorporates it — read it at the source URL before relying on it. This copy is the Rev. 5 text of record, which is not necessarily the text a citing document meant (a document citing Rev. 4 is not answered by it)._


## Full text

### AC-23 DATA MINING PROTECTION
Control:  Employ [Assignment: organization-defined data mining prevention and detection
techniques] for [Assignment: organization-defined data storage objects] to detect and protect
against unauthorized data mining.
Discussion:  Data mining is an analytical process that attempts to find correlations or patterns in
large data sets for the purpose of data or knowledge discovery. Data storage objects include
database records and database fields. Sensitive information can be extracted from data mining
operations. When information is personally identifiable information, it may lead to unanticipated
revelations about individuals and give rise to privacy risks. Prior to performing data mining
activities, organizations determine whether such activities are authorized. Organizations may be
subject to applicable laws, executive orders, directives, regulations, or policies that address data
mining requirements. Organizational personnel consult with the senior agency official for privacy
and legal counsel regarding such requirements.
Data mining prevention and detection techniques include limiting the number and frequency of
database queries to increase the work factor needed to determine the contents of databases,
limiting types of responses provided to database queries, applying differential privacy techniques
or homomorphic encryption, and notifying personnel when atypical database queries or accesses
occur. Data mining protection focuses on protecting information from data mining while such
information resides in organizational data stores. In contrast, AU-13 focuses on monitoring for
organizational information that may have been mined or otherwise obtained from data stores
CHAPTER THREE   PAGE 57
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
and is available as open-source information residing on external sites, such as social networking
or social media websites.
[EO 13587] requires the establishment of an insider threat program for deterring, detecting, and
mitigating insider threats, including the safeguarding of sensitive information from exploitation,
compromise, or other unauthorized disclosure. Data mining protection requires organizations to
identify appropriate techniques to prevent and detect unnecessary or unauthorized data mining.
Data mining can be used by an insider to collect organizational information for the purpose of
exfiltration.
Related Controls:  PM-12, PT-2.
Control Enhancements:  None.
References:  [EO 13587].
