---
schema_version: 1
corpus: federal-reference
jurisdiction: us
id: nist-sp-800-53-r5.pe-8
title: NIST SP 800-53 Rev. 5 PE-8 — VISITOR ACCESS RECORDS
doc_type: federal_instrument
citation: NIST SP 800-53 Rev. 5 PE-8
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

**NIST SP 800-53 Rev. 5 PE-8** — VISITOR ACCESS RECORDS

- Issued by: National Institute of Standards and Technology
- Publication: NIST SP 800-53 Rev. 5 — Security and Privacy Controls for Information Systems and Organizations ([nist-sp-800-53-r5](./nist-sp-800-53-r5.md))
- Version: Rev. 5 (September 2020, includes updates as of 2020-12-10)
- Text as of: 2026-11-12
- Cited by held documents: 16 times (cjis-sp-6-1 ×10, irs-pub-1075-11-2021 ×4, 6-cfr-37 ×1, arc-ampe ×1)
- Reproduction basis: 17 U.S.C. § 105 — work of the U.S. government (NIST). Determined per document on 2026-11-12 against the publication itself, not assumed from its issuer: its Authority statement (PDF page 3) reads "This publication may be used by nongovernmental organizations on a voluntary basis and is not subject to copyright in the United States. Attribution would, however, be appreciated by NIST." Held here: the front matter and Chapter Three (the control catalog) only. Chapter Three names ISO/IEC standards solely as bibliographic references and reproduces none of their text. NOT mirrored: the References bibliography and Appendices A-C; Appendix A (glossary) adapts third-party definitions (ISO/IEC 15026, ISO 25237, ISO/IEC 29100, ISO 15288, IETF RFC 4949), which ADR-0002 treats as not reproducible by being incorporated, and whose reproducibility has not been determined.


_NON-AUTHORITATIVE copy of one control, cut from the SP 800-53 Rev. 5 snapshot this corpus holds. Whether and how this binds a given agency depends on the instrument that incorporates it — read it at the source URL before relying on it. This copy is the Rev. 5 text of record, which is not necessarily the text a citing document meant (a document citing Rev. 4 is not answered by it)._


## Full text

### PE-8 VISITOR ACCESS RECORDS
Control:
a. Maintain visitor access records to the facility where the system resides for [Assignment:
organization-defined time period];
b. Review visitor access records [Assignment: organization-defined frequency]; and
c. Report anomalies in visitor access records to [Assignment: organization-defined personnel].
Discussion:  Visitor access records include the names and organizations of individuals visiting,
visitor signatures, forms of identification, dates of access, entry and departure times, purpose of
visits, and the names and organizations of individuals visited. Access record reviews determine if
access authorizations are current and are still required to support organizational mission and
business functions. Access records are not required for publicly accessible areas.
Related Controls:  PE-2, PE-3, PE-6.
Control Enhancements:
(1) VISITOR ACCESS RECORDS | AUTOMATED RECORDS MAINTENANCE AND REVIEW
CHAPTER THREE   PAGE 186
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
Maintain and review visitor access records using [Assignment: organization-defined
automated mechanisms].
Discussion:  Visitor access records may be stored and maintained in a database management
system that is accessible by organizational personnel. Automated access to such records
facilitates record reviews on a regular basis to determine if access authorizations are current
and still required to support organizational mission and business functions.
Related Controls:  None.
(2) VISITOR ACCESS RECORDS | PHYSICAL ACCESS RECORDS
[Withdrawn: Incorporated into PE-2.]
(3) VISITOR ACCESS RECORDS | LIMIT PERSONALLY IDENTIFIABLE INFORMATION ELEMENTS
Limit personally identifiable information contained in visitor access records to the
following elements identified in the privacy risk assessment: [Assignment: organization-
defined elements].
Discussion:  Organizations may have requirements that specify the contents of visitor access
records. Limiting personally identifiable information in visitor access records when such
information is not needed for operational purposes helps reduce the level of privacy risk
created by a system.
Related Controls:  RA-3, SA-8.
References:  None.
