---
schema_version: 1
corpus: federal-reference
jurisdiction: us
id: nist-sp-800-53-r5.au-12
title: NIST SP 800-53 Rev. 5 AU-12 — AUDIT RECORD GENERATION
doc_type: federal_instrument
citation: NIST SP 800-53 Rev. 5 AU-12
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

**NIST SP 800-53 Rev. 5 AU-12** — AUDIT RECORD GENERATION

- Issued by: National Institute of Standards and Technology
- Publication: NIST SP 800-53 Rev. 5 — Security and Privacy Controls for Information Systems and Organizations ([nist-sp-800-53-r5](./nist-sp-800-53-r5.md))
- Version: Rev. 5 (September 2020, includes updates as of 2020-12-10)
- Text as of: 2026-11-12
- Cited by held documents: 27 times (cjis-sp-6-1 ×18, irs-pub-1075-11-2021 ×4, arc-ampe ×3, 6-cfr-37 ×2)
- Reproduction basis: 17 U.S.C. § 105 — work of the U.S. government (NIST). Determined per document on 2026-11-12 against the publication itself, not assumed from its issuer: its Authority statement (PDF page 3) reads "This publication may be used by nongovernmental organizations on a voluntary basis and is not subject to copyright in the United States. Attribution would, however, be appreciated by NIST." Held here: the front matter and Chapter Three (the control catalog) only. Chapter Three names ISO/IEC standards solely as bibliographic references and reproduces none of their text. NOT mirrored: the References bibliography and Appendices A-C; Appendix A (glossary) adapts third-party definitions (ISO/IEC 15026, ISO 25237, ISO/IEC 29100, ISO 15288, IETF RFC 4949), which ADR-0002 treats as not reproducible by being incorporated, and whose reproducibility has not been determined.


_NON-AUTHORITATIVE copy of one control, cut from the SP 800-53 Rev. 5 snapshot this corpus holds. Whether and how this binds a given agency depends on the instrument that incorporates it — read it at the source URL before relying on it. This copy is the Rev. 5 text of record, which is not necessarily the text a citing document meant (a document citing Rev. 4 is not answered by it)._


## Full text

### AU-12 AUDIT RECORD GENERATION
Control:
CHAPTER THREE   PAGE 78
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
a. Provide audit record generation capability for the event types the system is capable of
auditing as defined in AU-2a on [Assignment: organization-defined system components];
b. Allow [Assignment: organization-defined personnel or roles] to select the event types that
are to be logged by specific components of the system; and
c. Generate audit records for the event types defined in AU-2c that include the audit record
content defined in AU-3.
Discussion:  Audit records can be generated from many different system components. The event
types specified in AU-2d are the event types for which audit logs are to be generated and are a
subset of all event types for which the system can generate audit records.
Related Controls:  AC-6, AC-17, AU-2, AU-3, AU-4, AU-5, AU-6, AU-7, AU-14, CM-5, MA-4, MP-4,
PM-12, SA-8, SC-18, SI-3, SI-4, SI-7, SI-10.
Control Enhancements:
(1) AUDIT RECORD GENERATION | SYSTEM-WIDE AND TIME-CORRELATED AUDIT TRAIL
Compile audit records from [Assignment: organization-defined system components] into a
system-wide (logical or physical) audit trail that is time-correlated to within [Assignment:
organization-defined level of tolerance for the relationship between time stamps of
individual records in the audit trail].
Discussion:  Audit trails are time-correlated if the time stamps in the individual audit records
can be reliably related to the time stamps in other audit records to achieve a time ordering
of the records within organizational tolerances.
Related Controls:  AU-8, SC-45.
(2) AUDIT RECORD GENERATION | STANDARDIZED FORMATS
Produce a system-wide (logical or physical) audit trail composed of audit records in a
standardized format.
Discussion:  Audit records that follow common standards promote interoperability and
information exchange between devices and systems. Promoting interoperability and
information exchange facilitates the production of event information that can be readily
analyzed and correlated. If logging mechanisms do not conform to standardized formats,
systems may convert individual audit records into standardized formats when compiling
system-wide audit trails.
Related Controls:  None.
(3) AUDIT RECORD GENERATION | CHANGES BY AUTHORIZED INDIVIDUALS
Provide and implement the capability for [Assignment: organization-defined individuals or
roles] to change the logging to be performed on [Assignment: organization-defined system
components] based on [Assignment: organization-defined selectable event criteria] within
[Assignment: organization-defined time thresholds].
Discussion:  Permitting authorized individuals to make changes to system logging enables
organizations to extend or limit logging as necessary to meet organizational requirements.
Logging that is limited to conserve system resources may be extended (either temporarily or
permanently) to address certain threat situations. In addition, logging may be limited to a
specific set of event types to facilitate audit reduction, analysis, and reporting. Organizations
can establish time thresholds in which logging actions are changed (e.g., near real-time,
within minutes, or within hours).
Related Controls:  AC-3.
CHAPTER THREE   PAGE 79
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
(4) AUDIT RECORD GENERATION | QUERY PARAMETER AUDITS OF PERSONALLY IDENTIFIABLE
INFORMATION
Provide and implement the capability for auditing the parameters of user query events for
data sets containing personally identifiable information.
Discussion:  Query parameters are explicit criteria that an individual or automated system
submits to a system to retrieve data. Auditing of query parameters for datasets that contain
personally identifiable information augments the capability of an organization to track and
understand the access, usage, or sharing of personally identifiable information by authorized
personnel.
Related Controls:  None.
References:  None.
