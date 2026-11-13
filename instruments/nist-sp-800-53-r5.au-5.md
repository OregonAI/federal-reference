---
schema_version: 1
corpus: federal-reference
jurisdiction: us
id: nist-sp-800-53-r5.au-5
title: NIST SP 800-53 Rev. 5 AU-5 — RESPONSE TO AUDIT LOGGING PROCESS FAILURES
doc_type: federal_instrument
citation: NIST SP 800-53 Rev. 5 AU-5
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

**NIST SP 800-53 Rev. 5 AU-5** — RESPONSE TO AUDIT LOGGING PROCESS FAILURES

- Issued by: National Institute of Standards and Technology
- Publication: NIST SP 800-53 Rev. 5 — Security and Privacy Controls for Information Systems and Organizations ([nist-sp-800-53-r5](./nist-sp-800-53-r5.md))
- Version: Rev. 5 (September 2020, includes updates as of 2020-12-10)
- Text as of: 2026-11-12
- Cited by held documents: 15 times (cjis-sp-6-1 ×11, irs-pub-1075-11-2021 ×3, 6-cfr-37 ×1)
- Reproduction basis: 17 U.S.C. § 105 — work of the U.S. government (NIST). Determined per document on 2026-11-12 against the publication itself, not assumed from its issuer: its Authority statement (PDF page 3) reads "This publication may be used by nongovernmental organizations on a voluntary basis and is not subject to copyright in the United States. Attribution would, however, be appreciated by NIST." Held here: the front matter and Chapter Three (the control catalog) only. Chapter Three names ISO/IEC standards solely as bibliographic references and reproduces none of their text. NOT mirrored: the References bibliography and Appendices A-C; Appendix A (glossary) adapts third-party definitions (ISO/IEC 15026, ISO 25237, ISO/IEC 29100, ISO 15288, IETF RFC 4949), which ADR-0002 treats as not reproducible by being incorporated, and whose reproducibility has not been determined.


_NON-AUTHORITATIVE copy of one control, cut from the SP 800-53 Rev. 5 snapshot this corpus holds. Whether and how this binds a given agency depends on the instrument that incorporates it — read it at the source URL before relying on it. This copy is the Rev. 5 text of record, which is not necessarily the text a citing document meant (a document citing Rev. 4 is not answered by it)._


## Full text

### AU-5 RESPONSE TO AUDIT LOGGING PROCESS FAILURES
Control:
a. Alert [Assignment: organization-defined personnel or roles] within [Assignment:
organization-defined time period] in the event of an audit logging process failure; and
b. Take the following additional actions: [Assignment: organization-defined additional actions].
Discussion:  Audit logging process failures include software and hardware errors, failures in audit
log capturing mechanisms, and reaching or exceeding audit log storage capacity. Organization-
defined actions include overwriting oldest audit records, shutting down the system, and stopping
CHAPTER THREE   PAGE 69
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
the generation of audit records. Organizations may choose to define additional actions for audit
logging process failures based on the type of failure, the location of the failure, the severity of
the failure, or a combination of such factors. When the audit logging process failure is related to
storage, the response is carried out for the audit log storage repository (i.e., the distinct system
component where the audit logs are stored), the system on which the audit logs reside, the total
audit log storage capacity of the organization (i.e., all audit log storage repositories combined), or
all three. Organizations may decide to take no additional actions after alerting designated roles
or personnel.
Related Controls:  AU-2, AU-4, AU-7, AU-9, AU-11, AU-12, AU-14, SI-4, SI-12.
Control Enhancements:
(1) RESPONSE TO AUDIT LOGGING PROCESS FAILURES | STORAGE CAPACITY WARNING
Provide a warning to [Assignment: organization-defined personnel, roles, and/or locations]
within [Assignment: organization-defined time period] when allocated audit log storage
volume reaches [Assignment: organization-defined percentage] of repository maximum
audit log storage capacity.
Discussion:  Organizations may have multiple audit log storage repositories distributed
across multiple system components with each repository having different storage volume
capacities.
Related Controls:  None.
(2) RESPONSE TO AUDIT LOGGING PROCESS FAILURES | REAL-TIME ALERTS
Provide an alert within [Assignment: organization-defined real-time period] to
[Assignment: organization-defined personnel, roles, and/or locations] when the following
audit failure events occur: [Assignment: organization-defined audit logging failure events
requiring real-time alerts].
Discussion:  Alerts provide organizations with urgent messages. Real-time alerts provide
these messages at information technology speed (i.e., the time from event detection to alert
occurs in seconds or less).
Related Controls:  None.
(3) RESPONSE TO AUDIT LOGGING PROCESS FAILURES | CONFIGURABLE TRAFFIC VOLUME THRESHOLDS
Enforce configurable network communications traffic volume thresholds reflecting limits
on audit log storage capacity and [Selection: reject; delay] network traffic above those
thresholds.
Discussion:  Organizations have the capability to reject or delay the processing of network
communications traffic if audit logging information about such traffic is determined to
exceed the storage capacity of the system audit logging function. The rejection or delay
response is triggered by the established organizational traffic volume thresholds that can be
adjusted based on changes to audit log storage capacity.
Related Controls:  None.
(4) RESPONSE TO AUDIT LOGGING PROCESS FAILURES | SHUTDOWN ON FAILURE
Invoke a [Selection: full system shutdown; partial system shutdown; degraded operational
mode with limited mission or business functionality available] in the event of [Assignment:
organization-defined audit logging failures], unless an alternate audit logging capability
exists.
Discussion:  Organizations determine the types of audit logging failures that can trigger
automatic system shutdowns or degraded operations. Because of the importance of
ensuring mission and business continuity, organizations may determine that the nature of
the audit logging failure is not so severe that it warrants a complete shutdown of the system
CHAPTER THREE   PAGE 70
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
supporting the core organizational mission and business functions. In those instances, partial
system shutdowns or operating in a degraded mode with reduced capability may be viable
alternatives.
Related Controls:  AU-15.
(5) RESPONSE TO AUDIT LOGGING PROCESS FAILURES | ALTERNATE AUDIT LOGGING CAPABILITY
Provide an alternate audit logging capability in the event of a failure in primary audit
logging capability that implements [Assignment: organization-defined alternate audit
logging functionality].
Discussion:  Since an alternate audit logging capability may be a short-term protection
solution employed until the failure in the primary audit logging capability is corrected,
organizations may determine that the alternate audit logging capability need only provide a
subset of the primary audit logging functionality that is impacted by the failure.
Related Controls:  AU-9.
References:  None.
