---
schema_version: 1
corpus: federal-reference
jurisdiction: us
id: nist-sp-800-53-r5.ir-6
title: NIST SP 800-53 Rev. 5 IR-6 — INCIDENT REPORTING
doc_type: federal_instrument
citation: NIST SP 800-53 Rev. 5 IR-6
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

**NIST SP 800-53 Rev. 5 IR-6** — INCIDENT REPORTING

- Issued by: National Institute of Standards and Technology
- Publication: NIST SP 800-53 Rev. 5 — Security and Privacy Controls for Information Systems and Organizations ([nist-sp-800-53-r5](./nist-sp-800-53-r5.md))
- Version: Rev. 5 (September 2020, includes updates as of 2020-12-10)
- Text as of: 2026-11-12
- Cited by held documents: 18 times (cjis-sp-6-1 ×11, irs-pub-1075-11-2021 ×5, 6-cfr-37 ×1, arc-ampe ×1)
- Reproduction basis: 17 U.S.C. § 105 — work of the U.S. government (NIST). Determined per document on 2026-11-12 against the publication itself, not assumed from its issuer: its Authority statement (PDF page 3) reads "This publication may be used by nongovernmental organizations on a voluntary basis and is not subject to copyright in the United States. Attribution would, however, be appreciated by NIST." Held here: the front matter and Chapter Three (the control catalog) only. Chapter Three names ISO/IEC standards solely as bibliographic references and reproduces none of their text. NOT mirrored: the References bibliography and Appendices A-C; Appendix A (glossary) adapts third-party definitions (ISO/IEC 15026, ISO 25237, ISO/IEC 29100, ISO 15288, IETF RFC 4949), which ADR-0002 treats as not reproducible by being incorporated, and whose reproducibility has not been determined.


_NON-AUTHORITATIVE copy of one control, cut from the SP 800-53 Rev. 5 snapshot this corpus holds. Whether and how this binds a given agency depends on the instrument that incorporates it — read it at the source URL before relying on it. This copy is the Rev. 5 text of record, which is not necessarily the text a citing document meant (a document citing Rev. 4 is not answered by it)._


> **Release 5.2.0 postdates this text.** NIST's listing of record ([https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final)) says that on 2025-08-27 it issued release 5.2.0 of SP 800-53, which updates the related controls for this control. The text below is the Rev. 5 PDF of record and does NOT include that change; read NIST's own list of the changes ([summary](https://csrc.nist.gov/files/projects/Risk-Management/800-53%20Comment%20Site/SP800-53-r5.2.0-changes.pdf)) before relying on this control's text.


## Full text

### IR-6 INCIDENT REPORTING
Control:
a. Require personnel to report suspected incidents to the organizational incident response
capability within [Assignment: organization-defined time period]; and
b. Report incident information to [Assignment: organization-defined authorities].
Discussion:  The types of incidents reported, the content and timeliness of the reports, and the
designated reporting authorities reflect applicable laws, executive orders, directives, regulations,
policies, standards, and guidelines. Incident information can inform risk assessments, control
effectiveness assessments, security requirements for acquisitions, and selection criteria for
technology products.
Related Controls:  CM-6, CP-2, IR-4, IR-5, IR-8, IR-9.
Control Enhancements:
(1) INCIDENT REPORTING | AUTOMATED REPORTING
Report incidents using [Assignment: organization-defined automated mechanisms].
Discussion:  The recipients of incident reports are specified in IR-6b. Automated reporting
mechanisms include email, posting on websites (with automatic updates), and automated
incident response tools and programs.
Related Controls:  IR-7.
(2) INCIDENT REPORTING | VULNERABILITIES RELATED TO INCIDENTS
Report system vulnerabilities associated with reported incidents to [Assignment:
organization-defined personnel or roles].
Discussion:  Reported incidents that uncover system vulnerabilities are analyzed by
organizational personnel including system owners, mission and business owners, senior
agency information security officers, senior agency officials for privacy, authorizing officials,
and the risk executive (function). The analysis can serve to prioritize and initiate mitigation
actions to address the discovered system vulnerability.
Related Controls:  None.
(3) INCIDENT REPORTING | SUPPLY CHAIN COORDINATION
Provide incident information to the provider of the product or service and other
organizations involved in the supply chain or supply chain governance for systems or
system components related to the incident.
Discussion:  Organizations involved in supply chain activities include product developers,
system integrators, manufacturers, packagers, assemblers, distributors, vendors, and
resellers. Entities that provide supply chain governance include the Federal Acquisition
Security Council (FASC). Supply chain incidents include compromises or breaches that involve
information technology products, system components, development processes or personnel,
distribution processes, or warehousing facilities. Organizations determine the appropriate
information to share and consider the value gained from informing external organizations
about supply chain incidents, including the ability to improve processes or to identify the
root cause of an incident.
Related Controls:  SR-8.
References:  [FASC18], [41 CFR 201], [USCERT IR], [SP 800-61].
CHAPTER THREE   PAGE 158
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
