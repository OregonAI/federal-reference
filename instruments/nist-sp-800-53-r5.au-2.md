---
schema_version: 1
corpus: federal-reference
jurisdiction: us
id: nist-sp-800-53-r5.au-2
title: NIST SP 800-53 Rev. 5 AU-2 — EVENT LOGGING
doc_type: federal_instrument
citation: NIST SP 800-53 Rev. 5 AU-2
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

**NIST SP 800-53 Rev. 5 AU-2** — EVENT LOGGING

- Issued by: National Institute of Standards and Technology
- Publication: NIST SP 800-53 Rev. 5 — Security and Privacy Controls for Information Systems and Organizations ([nist-sp-800-53-r5](./nist-sp-800-53-r5.md))
- Version: Rev. 5 (September 2020, includes updates as of 2020-12-10)
- Text as of: 2026-11-12
- Cited by held documents: 39 times (cjis-sp-6-1 ×29, 6-cfr-37 ×5, irs-pub-1075-11-2021 ×5)
- Reproduction basis: 17 U.S.C. § 105 — work of the U.S. government (NIST). Determined per document on 2026-11-12 against the publication itself, not assumed from its issuer: its Authority statement (PDF page 3) reads "This publication may be used by nongovernmental organizations on a voluntary basis and is not subject to copyright in the United States. Attribution would, however, be appreciated by NIST." Held here: the front matter and Chapter Three (the control catalog) only. Chapter Three names ISO/IEC standards solely as bibliographic references and reproduces none of their text. NOT mirrored: the References bibliography and Appendices A-C; Appendix A (glossary) adapts third-party definitions (ISO/IEC 15026, ISO 25237, ISO/IEC 29100, ISO 15288, IETF RFC 4949), which ADR-0002 treats as not reproducible by being incorporated, and whose reproducibility has not been determined.


_NON-AUTHORITATIVE copy of one control, cut from the SP 800-53 Rev. 5 snapshot this corpus holds. Whether and how this binds a given agency depends on the instrument that incorporates it — read it at the source URL before relying on it. This copy is the Rev. 5 text of record, which is not necessarily the text a citing document meant (a document citing Rev. 4 is not answered by it)._


> **Release 5.2.0 postdates this text.** NIST's listing of record ([https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final)) says that on 2025-08-27 it issued release 5.2.0 of SP 800-53, which updates the related controls for this control. The text below is the Rev. 5 PDF of record and does NOT include that change; read NIST's own list of the changes ([summary](https://csrc.nist.gov/files/projects/Risk-Management/800-53%20Comment%20Site/SP800-53-r5.2.0-changes.pdf)) before relying on this control's text.


## Full text

### AU-2 EVENT LOGGING
Control:
a. Identify the types of events that the system is capable of logging in support of the audit
function: [Assignment: organization-defined event types that the system is capable of
logging];
b. Coordinate the event logging function with other organizational entities requiring audit-
related information to guide and inform the selection criteria for events to be logged;
c. Specify the following event types for logging within the system: [Assignment: organization-
defined event types (subset of the event types defined in AU-2a.) along with the frequency of
(or situation requiring) logging for each identified event type];
d. Provide a rationale for why the event types selected for logging are deemed to be adequate
to support after-the-fact investigations of incidents; and
e. Review and update the event types selected for logging [Assignment: organization-defined
frequency].
Discussion:  An event is an observable occurrence in a system. The types of events that require
logging are those events that are significant and relevant to the security of systems and the
privacy of individuals. Event logging also supports specific monitoring and auditing needs. Event
types include password changes, failed logons or failed accesses related to systems, security or
privacy attribute changes, administrative privilege usage, PIV credential usage, data action
changes, query parameters, or external credential usage. In determining the set of event types
that require logging, organizations consider the monitoring and auditing appropriate for each of
the controls to be implemented. For completeness, event logging includes all protocols that are
operational and supported by the system.
To balance monitoring and auditing requirements with other system needs, event logging
requires identifying the subset of event types that are logged at a given point in time. For
example, organizations may determine that systems need the capability to log every file access
successful and unsuccessful, but not activate that capability except for specific circumstances due
to the potential burden on system performance. The types of events that organizations desire to
be logged may change. Reviewing and updating the set of logged events is necessary to help
ensure that the events remain relevant and continue to support the needs of the organization.
Organizations consider how the types of logging events can reveal information about individuals
that may give rise to privacy risk and how best to mitigate such risks. For example, there is the
potential to reveal personally identifiable information in the audit trail, especially if the logging
event is based on patterns or time of usage.
Event logging requirements, including the need to log specific event types, may be referenced in
other controls and control enhancements. These include AC-2(4), AC-3(10), AC-6(9), AC-17(1),
CM-3f, CM-5(1), IA-3(3.b), MA-4(1), MP-4(2), PE-3, PM-21, PT-7, RA-8, SC-7(9), SC-7(15), SI-3(8),
SI-4(22), SI-7(8), and SI-10(1). Organizations include event types that are required by applicable
laws, executive orders, directives, policies, regulations, standards, and guidelines. Audit records
can be generated at various levels, including at the packet level as information traverses the
network. Selecting the appropriate level of event logging is an important part of a monitoring
and auditing capability and can identify the root causes of problems. When defining event types,
organizations consider the logging necessary to cover related event types, such as the steps in
distributed, transaction-based processes and the actions that occur in service-oriented
architectures.
Related Controls:  AC-2, AC-3, AC-6, AC-7, AC-8, AC-16, AC-17, AU-3, AU-4, AU-5, AU-6, AU-7, AU-
11, AU-12, CM-3, CM-5, CM-6, CM-13, IA-3, MA-4, MP-4, PE-3, PM-21, PT-2, PT-7, RA-8, SA-8, SC-
7, SC-18, SI-3, SI-4, SI-7, SI-10, SI-11.
CHAPTER THREE   PAGE 67
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
Control Enhancements:
(1) EVENT LOGGING | COMPILATION OF AUDIT RECORDS FROM MULTIPLE SOURCES
[Withdrawn: Incorporated into AU-12.]
(2) EVENT LOGGING | SELECTION OF AUDIT EVENTS BY COMPONENT
[Withdrawn: Incorporated into AU-12.]
(3) EVENT LOGGING | REVIEWS AND UPDATES
[Withdrawn: Incorporated into AU-2.]
(4) EVENT LOGGING | PRIVILEGED FUNCTIONS
[Withdrawn: Incorporated into AC-6(9).]
References:  [OMB A-130], [SP 800-92].
