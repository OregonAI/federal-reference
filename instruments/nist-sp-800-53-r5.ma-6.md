---
schema_version: 1
corpus: federal-reference
jurisdiction: us
id: nist-sp-800-53-r5.ma-6
title: NIST SP 800-53 Rev. 5 MA-6 — TIMELY MAINTENANCE
doc_type: federal_instrument
citation: NIST SP 800-53 Rev. 5 MA-6
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

**NIST SP 800-53 Rev. 5 MA-6** — TIMELY MAINTENANCE

- Issued by: National Institute of Standards and Technology
- Publication: NIST SP 800-53 Rev. 5 — Security and Privacy Controls for Information Systems and Organizations ([nist-sp-800-53-r5](./nist-sp-800-53-r5.md))
- Version: Rev. 5 (September 2020, includes updates as of 2020-12-10)
- Text as of: 2026-11-12
- Cited by held documents: 14 times (cjis-sp-6-1 ×9, irs-pub-1075-11-2021 ×3, 6-cfr-37 ×1, arc-ampe ×1)
- Reproduction basis: 17 U.S.C. § 105 — work of the U.S. government (NIST). Determined per document on 2026-11-12 against the publication itself, not assumed from its issuer: its Authority statement (PDF page 3) reads "This publication may be used by nongovernmental organizations on a voluntary basis and is not subject to copyright in the United States. Attribution would, however, be appreciated by NIST." Held here: the front matter and Chapter Three (the control catalog) only. Chapter Three names ISO/IEC standards solely as bibliographic references and reproduces none of their text. NOT mirrored: the References bibliography and Appendices A-C; Appendix A (glossary) adapts third-party definitions (ISO/IEC 15026, ISO 25237, ISO/IEC 29100, ISO 15288, IETF RFC 4949), which ADR-0002 treats as not reproducible by being incorporated, and whose reproducibility has not been determined.


_NON-AUTHORITATIVE copy of one control, cut from the SP 800-53 Rev. 5 snapshot this corpus holds. Whether and how this binds a given agency depends on the instrument that incorporates it — read it at the source URL before relying on it. This copy is the Rev. 5 text of record, which is not necessarily the text a citing document meant (a document citing Rev. 4 is not answered by it)._


## Full text

### MA-6 TIMELY MAINTENANCE
Control:  Obtain maintenance support and/or spare parts for [Assignment: organization-defined
system components] within [Assignment: organization-defined time period] of failure.
Discussion:  Organizations specify the system components that result in increased risk to
organizational operations and assets, individuals, other organizations, or the Nation when the
functionality provided by those components is not operational. Organizational actions to obtain
maintenance support include having appropriate contracts in place.
Related Controls:  CM-8, CP-2, CP-7, RA-7, SA-15, SI-13, SR-2, SR-3, SR-4.
Control Enhancements:
(1) TIMELY MAINTENANCE | PREVENTIVE MAINTENANCE
Perform preventive maintenance on [Assignment: organization-defined system
components] at [Assignment: organization-defined time intervals].
Discussion:  Preventive maintenance includes proactive care and the servicing of system
components to maintain organizational equipment and facilities in satisfactory operating
condition. Such maintenance provides for the systematic inspection, tests, measurements,
adjustments, parts replacement, detection, and correction of incipient failures either before
they occur or before they develop into major defects. The primary goal of preventive
maintenance is to avoid or mitigate the consequences of equipment failures. Preventive
maintenance is designed to preserve and restore equipment reliability by replacing worn
components before they fail. Methods of determining what preventive (or other) failure
management policies to apply include original equipment manufacturer recommendations;
statistical failure records; expert opinion; maintenance that has already been conducted on
similar equipment; requirements of codes, laws, or regulations within a jurisdiction; or
measured values and performance indications.
Related Controls:  None.
(2) TIMELY MAINTENANCE | PREDICTIVE MAINTENANCE
Perform predictive maintenance on [Assignment: organization-defined system
components] at [Assignment: organization-defined time intervals].
Discussion:  Predictive maintenance evaluates the condition of equipment by performing
periodic or continuous (online) equipment condition monitoring. The goal of predictive
maintenance is to perform maintenance at a scheduled time when the maintenance activity
is most cost-effective and before the equipment loses performance within a threshold. The
predictive component of predictive maintenance stems from the objective of predicting the
future trend of the equipment's condition. The predictive maintenance approach employs
principles of statistical process control to determine at what point in the future maintenance
activities will be appropriate. Most predictive maintenance inspections are performed while
equipment is in service, thus minimizing disruption of normal system operations. Predictive
maintenance can result in substantial cost savings and higher system reliability.
Related Controls:  None.
CHAPTER THREE   PAGE 170
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
(3) TIMELY MAINTENANCE | AUTOMATED SUPPORT FOR PREDICTIVE MAINTENANCE
Transfer predictive maintenance data to a maintenance management system using
[Assignment: organization-defined automated mechanisms].
Discussion:  A computerized maintenance management system maintains a database of
information about the maintenance operations of organizations and automates the
processing of equipment condition data to trigger maintenance planning, execution, and
reporting.
Related Controls:  None.
References:  None.
