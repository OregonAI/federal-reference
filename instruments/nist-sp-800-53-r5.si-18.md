---
schema_version: 1
corpus: federal-reference
jurisdiction: us
id: nist-sp-800-53-r5.si-18
title: NIST SP 800-53 Rev. 5 SI-18 — PERSONALLY IDENTIFIABLE INFORMATION QUALITY OPERATIONS
doc_type: federal_instrument
citation: NIST SP 800-53 Rev. 5 SI-18
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

**NIST SP 800-53 Rev. 5 SI-18** — PERSONALLY IDENTIFIABLE INFORMATION QUALITY OPERATIONS

- Issued by: National Institute of Standards and Technology
- Publication: NIST SP 800-53 Rev. 5 — Security and Privacy Controls for Information Systems and Organizations ([nist-sp-800-53-r5](./nist-sp-800-53-r5.md))
- Version: Rev. 5 (September 2020, includes updates as of 2020-12-10)
- Text as of: 2026-11-12
- Cited by held documents: 8 times (arc-ampe ×8), 1 of them naming an enhancement of this control
- Reproduction basis: 17 U.S.C. § 105 — work of the U.S. government (NIST). Determined per document on 2026-11-12 against the publication itself, not assumed from its issuer: its Authority statement (PDF page 3) reads "This publication may be used by nongovernmental organizations on a voluntary basis and is not subject to copyright in the United States. Attribution would, however, be appreciated by NIST." Held here: the front matter and Chapter Three (the control catalog) only. Chapter Three names ISO/IEC standards solely as bibliographic references and reproduces none of their text. NOT mirrored: the References bibliography and Appendices A-C; Appendix A (glossary) adapts third-party definitions (ISO/IEC 15026, ISO 25237, ISO/IEC 29100, ISO 15288, IETF RFC 4949), which ADR-0002 treats as not reproducible by being incorporated, and whose reproducibility has not been determined.


_NON-AUTHORITATIVE copy of one control, cut from the SP 800-53 Rev. 5 snapshot this corpus holds. Whether and how this binds a given agency depends on the instrument that incorporates it — read it at the source URL before relying on it. This copy is the Rev. 5 text of record, which is not necessarily the text a citing document meant (a document citing Rev. 4 is not answered by it)._


## Full text

### SI-18 PERSONALLY IDENTIFIABLE INFORMATION QUALITY OPERATIONS
Control:
a. Check the accuracy, relevance, timeliness, and completeness of personally identifiable
information across the information life cycle [Assignment: organization-defined frequency];
and
b. Correct or delete inaccurate or outdated personally identifiable information.
Discussion:  Personally identifiable information quality operations include the steps that
organizations take to confirm the accuracy and relevance of personally identifiable information
throughout the information life cycle. The information life cycle includes the creation, collection,
use, processing, storage, maintenance, dissemination, disclosure, and disposal of personally
identifiable information. Personally identifiable information quality operations include editing
and validating addresses as they are collected or entered into systems using automated address
verification look-up application programming interfaces. Checking personally identifiable
information quality includes the tracking of updates or changes to data over time, which enables
organizations to know how and what personally identifiable information was changed should
erroneous information be identified. The measures taken to protect personally identifiable
information quality are based on the nature and context of the personally identifiable
information, how it is to be used, how it was obtained, and the potential de-identification
methods employed. The measures taken to validate the accuracy of personally identifiable
information used to make determinations about the rights, benefits, or privileges of individuals
covered under federal programs may be more comprehensive than the measures used to
validate personally identifiable information used for less sensitive purposes.
Related Controls:  PM-22, PM-24, PT-2, SI-4.
Control Enhancements:
(1) PERSONALLY IDENTIFIABLE INFORMATION QUALITY OPERATIONS | AUTOMATION SUPPORT
CHAPTER THREE   PAGE 357
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
Correct or delete personally identifiable information that is inaccurate or outdated,
incorrectly determined regarding impact, or incorrectly de-identified using [Assignment:
organization-defined automated mechanisms].
Discussion:  The use of automated mechanisms to improve data quality may inadvertently
create privacy risks. Automated tools may connect to external or otherwise unrelated
systems, and the matching of records between these systems may create linkages with
unintended consequences. Organizations assess and document these risks in their privacy
impact assessments and make determinations that are in alignment with their privacy
program plans.
As data is obtained and used across the information life cycle, it is important to confirm the
accuracy and relevance of personally identifiable information. Automated mechanisms can
augment existing data quality processes and procedures and enable an organization to
better identify and manage personally identifiable information in large-scale systems. For
example, automated tools can greatly improve efforts to consistently normalize data or
identify malformed data. Automated tools can also be used to improve the auditing of data
and detect errors that may incorrectly alter personally identifiable information or incorrectly
associate such information with the wrong individual. Automated capabilities backstop
processes and procedures at-scale and enable more fine-grained detection and correction of
data quality errors.
Related Controls:  PM-18, RA-8.
(2) PERSONALLY IDENTIFIABLE INFORMATION QUALITY OPERATIONS | DATA TAGS
Employ data tags to automate the correction or deletion of personally identifiable
information across the information life cycle within organizational systems.
Discussion:  Data tagging personally identifiable information includes tags that note
processing permissions, authority to process, de-identification, impact level, information life
cycle stage, and retention or last updated dates. Employing data tags for personally
identifiable information can support the use of automation tools to correct or delete
relevant personally identifiable information.
Related Controls:  AC-3, AC-16,  SC-16.
(3) PERSONALLY IDENTIFIABLE INFORMATION QUALITY OPERATIONS | COLLECTION
Collect personally identifiable information directly from the individual.
Discussion:  Individuals or their designated representatives can be sources of correct
personally identifiable information. Organizations consider contextual factors that may
incentivize individuals to provide correct data versus false data. Additional steps may be
necessary to validate collected information based on the nature and context of the
personally identifiable information, how it is to be used, and how it was obtained. The
measures taken to validate the accuracy of personally identifiable information used to make
determinations about the rights, benefits, or privileges of individuals under federal programs
may be more comprehensive than the measures taken to validate less sensitive personally
identifiable information.
Related Controls:  None.
(4) PERSONALLY IDENTIFIABLE INFORMATION QUALITY OPERATIONS | INDIVIDUAL REQUESTS
Correct or delete personally identifiable information upon request by individuals or their
designated representatives.
Discussion:  Inaccurate personally identifiable information maintained by organizations may
cause problems for individuals, especially in those business functions where inaccurate
information may result in inappropriate decisions or the denial of benefits and services to
individuals. Even correct information, in certain circumstances, can cause problems for
CHAPTER THREE   PAGE 358
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
individuals that outweigh the benefits of an organization maintaining the information.
Organizations use discretion when determining if personally identifiable information is to be
corrected or deleted based on the scope of requests, the changes sought, the impact of the
changes, and laws, regulations, and policies. Organizational personnel consult with the
senior agency official for privacy and legal counsel regarding appropriate instances of
correction or deletion.
Related Controls:  None.
(5) PERSONALLY IDENTIFIABLE INFORMATION QUALITY OPERATIONS | NOTICE OF CORRECTION OR
DELETION
Notify [Assignment: organization-defined recipients of personally identifiable information]
and individuals that the personally identifiable information has been corrected or deleted.
Discussion:  When personally identifiable information is corrected or deleted, organizations
take steps to ensure that all authorized recipients of such information, and the individual
with whom the information is associated or their designated representatives, are informed
of the corrected or deleted information.
Related Controls:  None.
References:  [OMB M-19-15], [SP 800-188], [IR 8112].
