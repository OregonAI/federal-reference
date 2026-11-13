---
schema_version: 1
corpus: federal-reference
jurisdiction: us
id: nist-sp-800-53-r5.pl-8
title: NIST SP 800-53 Rev. 5 PL-8 — SECURITY AND PRIVACY ARCHITECTURES
doc_type: federal_instrument
citation: NIST SP 800-53 Rev. 5 PL-8
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

**NIST SP 800-53 Rev. 5 PL-8** — SECURITY AND PRIVACY ARCHITECTURES

- Issued by: National Institute of Standards and Technology
- Publication: NIST SP 800-53 Rev. 5 — Security and Privacy Controls for Information Systems and Organizations ([nist-sp-800-53-r5](./nist-sp-800-53-r5.md))
- Version: Rev. 5 (September 2020, includes updates as of 2020-12-10)
- Text as of: 2026-11-12
- Cited by held documents: 22 times (cjis-sp-6-1 ×14, irs-pub-1075-11-2021 ×5, arc-ampe ×2, 6-cfr-37 ×1)
- Reproduction basis: 17 U.S.C. § 105 — work of the U.S. government (NIST). Determined per document on 2026-11-12 against the publication itself, not assumed from its issuer: its Authority statement (PDF page 3) reads "This publication may be used by nongovernmental organizations on a voluntary basis and is not subject to copyright in the United States. Attribution would, however, be appreciated by NIST." Held here: the front matter and Chapter Three (the control catalog) only. Chapter Three names ISO/IEC standards solely as bibliographic references and reproduces none of their text. NOT mirrored: the References bibliography and Appendices A-C; Appendix A (glossary) adapts third-party definitions (ISO/IEC 15026, ISO 25237, ISO/IEC 29100, ISO 15288, IETF RFC 4949), which ADR-0002 treats as not reproducible by being incorporated, and whose reproducibility has not been determined.


_NON-AUTHORITATIVE copy of one control, cut from the SP 800-53 Rev. 5 snapshot this corpus holds. Whether and how this binds a given agency depends on the instrument that incorporates it — read it at the source URL before relying on it. This copy is the Rev. 5 text of record, which is not necessarily the text a citing document meant (a document citing Rev. 4 is not answered by it)._


## Full text

### PL-8 SECURITY AND PRIVACY ARCHITECTURES
Control:
a. Develop security and privacy architectures for the system that:
1. Describe the requirements and approach to be taken for protecting the confidentiality,
integrity, and availability of organizational information;
2. Describe the requirements and approach to be taken for processing personally
identifiable information to minimize privacy risk to individuals;
3. Describe how the architectures are integrated into and support the enterprise
architecture; and
4. Describe any assumptions about, and dependencies on, external systems and services;
b. Review and update the architectures [Assignment: organization-defined frequency] to reflect
changes in the enterprise architecture; and
c. Reflect planned architecture changes in security and privacy plans, Concept of Operations
(CONOPS), criticality analysis, organizational procedures, and procurements and acquisitions.
Discussion:  The security and privacy architectures at the system level are consistent with the
organization-wide security and privacy architectures described in PM-7, which are integral to and
developed as part of the enterprise architecture. The architectures include an architectural
description, the allocation of security and privacy functionality (including controls), security- and
privacy-related information for external interfaces, information being exchanged across the
interfaces, and the protection mechanisms associated with each interface. The architectures can
CHAPTER THREE   PAGE 199
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
also include other information, such as user roles and the access privileges assigned to each role;
security and privacy requirements; types of information processed, stored, and transmitted by
the system; supply chain risk management requirements; restoration priorities of information
and system services; and other protection needs.
[SP 800-160-1] provides guidance on the use of security architectures as part of the system
development life cycle process. [OMB M-19-03] requires the use of the systems security
engineering concepts described in [SP 800-160-1] for high value assets. Security and privacy
architectures are reviewed and updated throughout the system development life cycle, from
analysis of alternatives through review of the proposed architecture in the RFP responses to the
design reviews before and during implementation (e.g., during preliminary design reviews and
critical design reviews).
In today’s modern computing architectures, it is becoming less common for organizations to
control all information resources. There may be key dependencies on external information
services and service providers. Describing such dependencies in the security and privacy
architectures is necessary for developing a comprehensive mission and business protection
strategy. Establishing, developing, documenting, and maintaining under configuration control a
baseline configuration for organizational systems is critical to implementing and maintaining
effective architectures. The development of the architectures is coordinated with the senior
agency information security officer and the senior agency official for privacy to ensure that the
controls needed to support security and privacy requirements are identified and effectively
implemented. In many circumstances, there may be no distinction between the security and
privacy architecture for a system. In other circumstances, security objectives may be adequately
satisfied, but privacy objectives may only be partially satisfied by the security requirements. In
these cases, consideration of the privacy requirements needed to achieve satisfaction will result
in a distinct privacy architecture. The documentation, however, may simply reflect the combined
architectures.
PL-8
is primarily directed at organizations to ensure that architectures are developed for the
system and, moreover, that the architectures are integrated with or tightly coupled to the
enterprise architecture. In contrast, SA-17 is primarily directed at the external information
technology product and system developers and integrators. SA-17, which is complementary to
PL-8, is selected when organizations outsource the development of systems or components to
external entities and when there is a need to demonstrate consistency with the organization’s
enterprise architecture and security and privacy architectures.
Related Controls:  CM-2, CM-6, PL-2, PL-7, PL-9, PM-5, PM-7, RA-9, SA-3, SA-5, SA-8, SA-17, SC-7.
Control Enhancements:
(1) SECURITY AND PRIVACY ARCHITECTURES | DEFENSE IN DEPTH
Design the security and privacy architectures for the system using a defense-in-depth
approach that:
(a) Allocates [Assignment: organization-defined controls] to [Assignment: organization-
defined locations and architectural layers]; and
(b) Ensures that the allocated controls operate in a coordinated and mutually reinforcing
manner.
Discussion:  Organizations strategically allocate security and privacy controls in the security
and privacy architectures so that adversaries must overcome multiple controls to achieve
their objective. Requiring adversaries to defeat multiple controls makes it more difficult to
attack information resources by increasing the work factor of the adversary; it also increases
the likelihood of detection. The coordination of allocated controls is essential to ensure that
an attack that involves one control does not create adverse, unintended consequences by
interfering with other controls. Unintended consequences can include system lockout and
CHAPTER THREE   PAGE 200
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
cascading alarms. The placement of controls in systems and organizations is an important
activity that requires thoughtful analysis. The value of organizational assets is an important
consideration in providing additional layering. Defense-in-depth architectural approaches
include modularity and layering (see SA-8(3)), separation of system and user functionality
(see SC-2), and security function isolation (see SC-3).
Related Controls:  SC-2, SC-3, SC-29, SC-36.
(2) SECURITY AND PRIVACY ARCHITECTURES | SUPPLIER DIVERSITY
Require that [Assignment: organization-defined controls] allocated to [Assignment:
organization-defined locations and architectural layers] are obtained from different
suppliers.
Discussion:  Information technology products have different strengths and weaknesses.
Providing a broad spectrum of products complements the individual offerings. For example,
vendors offering malicious code protection typically update their products at different times,
often developing solutions for known viruses, Trojans, or worms based on their priorities
and development schedules. By deploying different products at different locations, there is
an increased likelihood that at least one of the products will detect the malicious code. With
respect to privacy, vendors may offer products that track personally identifiable information
in systems. Products may use different tracking methods. Using multiple products may result
in more assurance that personally identifiable information is inventoried.
Related Controls:  SC-29, SR-3.
References:  [OMB A-130], [SP 800-160-1], [SP 800-160-2].
