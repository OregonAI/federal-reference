---
schema_version: 1
corpus: federal-reference
jurisdiction: us
id: nist-sp-800-53-r5.cp-8
title: NIST SP 800-53 Rev. 5 CP-8 — TELECOMMUNICATIONS SERVICES
doc_type: federal_instrument
citation: NIST SP 800-53 Rev. 5 CP-8
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

**NIST SP 800-53 Rev. 5 CP-8** — TELECOMMUNICATIONS SERVICES

- Issued by: National Institute of Standards and Technology
- Publication: NIST SP 800-53 Rev. 5 — Security and Privacy Controls for Information Systems and Organizations ([nist-sp-800-53-r5](./nist-sp-800-53-r5.md))
- Version: Rev. 5 (September 2020, includes updates as of 2020-12-10)
- Text as of: 2026-11-12
- Cited by held documents: 16 times (cjis-sp-6-1 ×11, arc-ampe ×3, 6-cfr-37 ×2)
- Reproduction basis: 17 U.S.C. § 105 — work of the U.S. government (NIST). Determined per document on 2026-11-12 against the publication itself, not assumed from its issuer: its Authority statement (PDF page 3) reads "This publication may be used by nongovernmental organizations on a voluntary basis and is not subject to copyright in the United States. Attribution would, however, be appreciated by NIST." Held here: the front matter and Chapter Three (the control catalog) only. Chapter Three names ISO/IEC standards solely as bibliographic references and reproduces none of their text. NOT mirrored: the References bibliography and Appendices A-C; Appendix A (glossary) adapts third-party definitions (ISO/IEC 15026, ISO 25237, ISO/IEC 29100, ISO 15288, IETF RFC 4949), which ADR-0002 treats as not reproducible by being incorporated, and whose reproducibility has not been determined.


_NON-AUTHORITATIVE copy of one control, cut from the SP 800-53 Rev. 5 snapshot this corpus holds. Whether and how this binds a given agency depends on the instrument that incorporates it — read it at the source URL before relying on it. This copy is the Rev. 5 text of record, which is not necessarily the text a citing document meant (a document citing Rev. 4 is not answered by it)._


## Full text

### CP-8 TELECOMMUNICATIONS SERVICES
Control:  Establish alternate telecommunications services, including necessary agreements to
permit the resumption of [Assignment: organization-defined system operations] for essential
mission and business functions within [Assignment: organization-defined time period] when the
primary telecommunications capabilities are unavailable at either the primary or alternate
processing or storage sites.
Discussion:  Telecommunications services (for data and voice) for primary and alternate
processing and storage sites are in scope for CP-8. Alternate telecommunications services reflect
the continuity requirements in contingency plans to maintain essential mission and business
functions despite the loss of primary telecommunications services. Organizations may specify
different time periods for primary or alternate sites. Alternate telecommunications services
include additional organizational or commercial ground-based circuits or lines, network-based
approaches to telecommunications, or the use of satellites. Organizations consider factors such
as availability, quality of service, and access when entering into alternate telecommunications
agreements.
Related Controls:  CP-2, CP-6, CP-7, CP-11, SC-7.
Control Enhancements:
(1) TELECOMMUNICATIONS SERVICES | PRIORITY OF SERVICE PROVISIONS
(a) Develop primary and alternate telecommunications service agreements that contain
priority-of-service provisions in accordance with availability requirements (including
recovery time objectives); and
(b) Request Telecommunications Service Priority for all telecommunications services used
for national security emergency preparedness if the primary and/or alternate
telecommunications services are provided by a common carrier.
Discussion:  Organizations consider the potential mission or business impact in situations
where telecommunications service providers are servicing other organizations with similar
priority of service provisions. Telecommunications Service Priority (TSP) is a Federal
Communications Commission (FCC) program that directs telecommunications service
providers (e.g., wireline and wireless phone companies) to give preferential treatment to
users enrolled in the program when they need to add new lines or have their lines restored
following a disruption of service, regardless of the cause. The FCC sets the rules and policies
for the TSP program, and the Department of Homeland Security manages the TSP program.
The TSP program is always in effect and not contingent on a major disaster or attack taking
place. Federal sponsorship is required to enroll in the TSP program.
Related Controls:  None.
(2) TELECOMMUNICATIONS SERVICES | SINGLE POINTS OF FAILURE
Obtain alternate telecommunications services to reduce the likelihood of sharing a single
point of failure with primary telecommunications services.
Discussion:  In certain circumstances, telecommunications service providers or services may
share the same physical lines, which increases the vulnerability of a single failure point. It is
important to have provider transparency for the actual physical transmission capability for
telecommunication services.
CHAPTER THREE   PAGE 125
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
Related Controls:  None.
(3) TELECOMMUNICATIONS SERVICES | SEPARATION OF PRIMARY AND ALTERNATE PROVIDERS
Obtain alternate telecommunications services from providers that are separated from
primary service providers to reduce susceptibility to the same threats.
Discussion:  Threats that affect telecommunications services are defined in organizational
assessments of risk and include natural disasters, structural failures, cyber or physical
attacks, and errors of omission or commission. Organizations can reduce common
susceptibilities by minimizing shared infrastructure among telecommunications service
providers and achieving sufficient geographic separation between services. Organizations
may consider using a single service provider in situations where the service provider can
provide alternate telecommunications services that meet the separation needs addressed in
the risk assessment.
Related Controls:  None.
(4) TELECOMMUNICATIONS SERVICES | PROVIDER CONTINGENCY PLAN
(a) Require primary and alternate telecommunications service providers to have
contingency plans;
(b) Review provider contingency plans to ensure that the plans meet organizational
contingency requirements; and
(c) Obtain evidence of contingency testing and training by providers [Assignment:
organization-defined frequency].
Discussion:  Reviews of provider contingency plans consider the proprietary nature of such
plans. In some situations, a summary of provider contingency plans may be sufficient
evidence for organizations to satisfy the review requirement. Telecommunications service
providers may also participate in ongoing disaster recovery exercises in coordination with
the Department of Homeland Security and state and local governments. Organizations may
use these types of activities to satisfy evidentiary requirements related to service provider
contingency plan reviews, testing, and training.
Related Controls:  CP-3, CP-4.
(5) TELECOMMUNICATIONS SERVICES | ALTERNATE TELECOMMUNICATION SERVICE TESTING
Test alternate telecommunication services [Assignment: organization-defined frequency].
Discussion:  Alternate telecommunications services testing is arranged through contractual
agreements with service providers. The testing may occur in parallel with normal operations
to ensure that there is no degradation in organizational missions or functions.
Related Controls:  CP-3.
References:  [SP 800-34].
