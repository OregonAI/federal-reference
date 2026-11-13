---
schema_version: 1
corpus: federal-reference
jurisdiction: us
id: nist-sp-800-53-r5.pt-4
title: NIST SP 800-53 Rev. 5 PT-4 — CONSENT
doc_type: federal_instrument
citation: NIST SP 800-53 Rev. 5 PT-4
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

**NIST SP 800-53 Rev. 5 PT-4** — CONSENT

- Issued by: National Institute of Standards and Technology
- Publication: NIST SP 800-53 Rev. 5 — Security and Privacy Controls for Information Systems and Organizations ([nist-sp-800-53-r5](./nist-sp-800-53-r5.md))
- Version: Rev. 5 (September 2020, includes updates as of 2020-12-10)
- Text as of: 2026-11-12
- Cited by held documents: 2 times (arc-ampe ×2)
- Reproduction basis: 17 U.S.C. § 105 — work of the U.S. government (NIST). Determined per document on 2026-11-12 against the publication itself, not assumed from its issuer: its Authority statement (PDF page 3) reads "This publication may be used by nongovernmental organizations on a voluntary basis and is not subject to copyright in the United States. Attribution would, however, be appreciated by NIST." Held here: the front matter and Chapter Three (the control catalog) only. Chapter Three names ISO/IEC standards solely as bibliographic references and reproduces none of their text. NOT mirrored: the References bibliography and Appendices A-C; Appendix A (glossary) adapts third-party definitions (ISO/IEC 15026, ISO 25237, ISO/IEC 29100, ISO 15288, IETF RFC 4949), which ADR-0002 treats as not reproducible by being incorporated, and whose reproducibility has not been determined.


_NON-AUTHORITATIVE copy of one control, cut from the SP 800-53 Rev. 5 snapshot this corpus holds. Whether and how this binds a given agency depends on the instrument that incorporates it — read it at the source URL before relying on it. This copy is the Rev. 5 text of record, which is not necessarily the text a citing document meant (a document citing Rev. 4 is not answered by it)._


## Full text

### PT-4 CONSENT
Control:  Implement [Assignment: organization-defined tools or mechanisms] for individuals to
consent to the processing of their personally identifiable information prior to its collection that
facilitate individuals’ informed decision-making.
Discussion:  Consent allows individuals to participate in making decisions about the processing of
their information and transfers some of the risk that arises from the processing of personally
identifiable information from the organization to an individual. Consent may be required by
applicable laws, executive orders, directives, regulations, policies, standards, or guidelines.
Otherwise, when selecting consent as a control, organizations consider whether individuals can
be reasonably expected to understand and accept the privacy risks that arise from their
authorization. Organizations consider whether other controls may more effectively mitigate
privacy risk either alone or in conjunction with consent. Organizations also consider any
demographic or contextual factors that may influence the understanding or behavior of
individuals with respect to the processing carried out by the system or organization. When
soliciting consent from individuals, organizations consider the appropriate mechanism for
obtaining consent, including the type of consent (e.g., opt-in, opt-out), how to properly
authenticate and identity proof individuals and how to obtain consent through electronic means.
In addition, organizations consider providing a mechanism for individuals to revoke consent once
it has been provided, as appropriate. Finally, organizations consider usability factors to help
individuals understand the risks being accepted when providing consent, including the use of
plain language and avoiding technical jargon.
Related Controls:  AC-16, PT-2, PT-5.
Control Enhancements:
(1) CONSENT | TAILORED CONSENT
Provide [Assignment: organization-defined mechanisms] to allow individuals to tailor
processing permissions to selected elements of personally identifiable information.
CHAPTER THREE   PAGE 233
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
Discussion: While some processing may be necessary for the basic functionality of the
product or service, other processing may not. In these circumstances, organizations allow
individuals to select how specific personally identifiable information elements may be
processed. More tailored consent may help reduce privacy risk, increase individual
satisfaction, and avoid adverse behaviors, such as abandonment of the product or service.
Related Controls:  PT-2.
(2) CONSENT | JUST-IN-TIME CONSENT
Present [Assignment: organization-defined consent mechanisms] to individuals at
[Assignment: organization-defined frequency] and in conjunction with [Assignment:
organization-defined personally identifiable information processing].
Discussion:  Just-in-time consent enables individuals to participate in how their personally
identifiable information is being processed at the time or in conjunction with specific types
of data processing when such participation may be most useful to the individual. Individual
assumptions about how personally identifiable information is being processed might not be
accurate or reliable if time has passed since the individual last gave consent or the type of
processing creates significant privacy risk. Organizations use discretion to determine when
to use just-in-time consent and may use supporting information on demographics, focus
groups, or surveys to learn more about individuals’ privacy interests and concerns.
Related Controls:  PT-2.
(3) CONSENT | REVOCATION
Implement [Assignment: organization-defined tools or mechanisms] for individuals to
revoke consent to the processing of their personally identifiable information.
Discussion: Revocation of consent enables individuals to exercise control over their initial
consent decision when circumstances change. Organizations consider usability factors in
enabling easy-to-use revocation capabilities.
Related Controls:  PT-2.
References:  [PRIVACT], [OMB A-130], [SP 800-63-3].
