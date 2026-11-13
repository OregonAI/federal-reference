---
schema_version: 1
corpus: federal-reference
jurisdiction: us
id: nist-sp-800-53-r5.sa-3
title: NIST SP 800-53 Rev. 5 SA-3 — SYSTEM DEVELOPMENT LIFE CYCLE
doc_type: federal_instrument
citation: NIST SP 800-53 Rev. 5 SA-3
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

**NIST SP 800-53 Rev. 5 SA-3** — SYSTEM DEVELOPMENT LIFE CYCLE

- Issued by: National Institute of Standards and Technology
- Publication: NIST SP 800-53 Rev. 5 — Security and Privacy Controls for Information Systems and Organizations ([nist-sp-800-53-r5](./nist-sp-800-53-r5.md))
- Version: Rev. 5 (September 2020, includes updates as of 2020-12-10)
- Text as of: 2026-11-12
- Cited by held documents: 19 times (cjis-sp-6-1 ×14, irs-pub-1075-11-2021 ×3, 6-cfr-37 ×1, arc-ampe ×1)
- Reproduction basis: 17 U.S.C. § 105 — work of the U.S. government (NIST). Determined per document on 2026-11-12 against the publication itself, not assumed from its issuer: its Authority statement (PDF page 3) reads "This publication may be used by nongovernmental organizations on a voluntary basis and is not subject to copyright in the United States. Attribution would, however, be appreciated by NIST." Held here: the front matter and Chapter Three (the control catalog) only. Chapter Three names ISO/IEC standards solely as bibliographic references and reproduces none of their text. NOT mirrored: the References bibliography and Appendices A-C; Appendix A (glossary) adapts third-party definitions (ISO/IEC 15026, ISO 25237, ISO/IEC 29100, ISO 15288, IETF RFC 4949), which ADR-0002 treats as not reproducible by being incorporated, and whose reproducibility has not been determined.


_NON-AUTHORITATIVE copy of one control, cut from the SP 800-53 Rev. 5 snapshot this corpus holds. Whether and how this binds a given agency depends on the instrument that incorporates it — read it at the source URL before relying on it. This copy is the Rev. 5 text of record, which is not necessarily the text a citing document meant (a document citing Rev. 4 is not answered by it)._


## Full text

### SA-3 SYSTEM DEVELOPMENT LIFE CYCLE
Control:
a. Acquire, develop, and manage the system using [Assignment: organization-defined system
development life cycle] that incorporates information security and privacy considerations;
b. Define and document information security and privacy roles and responsibilities throughout
the system development life cycle;
c. Identify individuals having information security and privacy roles and responsibilities; and
d. Integrate the organizational information security and privacy risk management process into
system development life cycle activities.
Discussion:  A system development life cycle process provides the foundation for the successful
development, implementation, and operation of organizational systems. The integration of
security and privacy considerations early in the system development life cycle is a foundational
principle of systems security engineering and privacy engineering. To apply the required controls
within the system development life cycle requires a basic understanding of information security
and privacy, threats, vulnerabilities, adverse impacts, and risk to critical mission and business
functions. The security engineering principles in SA-8 help individuals properly design, code, and
test systems and system components. Organizations include qualified personnel (e.g., senior
agency information security officers, senior agency officials for privacy, security and privacy
architects, and security and privacy engineers) in system development life cycle processes to
ensure that established security and privacy requirements are incorporated into organizational
systems. Role-based security and privacy training programs can ensure that individuals with key
security and privacy roles and responsibilities have the experience, skills, and expertise to
conduct assigned system development life cycle activities.
The effective integration of security and privacy requirements into enterprise architecture also
helps to ensure that important security and privacy considerations are addressed throughout the
system life cycle and that those considerations are directly related to organizational mission and
business processes. This process also facilitates the integration of the information security and
privacy architectures into the enterprise architecture, consistent with the risk management
strategy of the organization. Because the system development life cycle involves multiple
organizations, (e.g., external suppliers, developers, integrators, service providers), acquisition
CHAPTER THREE   PAGE 251
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
and supply chain risk management functions and controls play significant roles in the effective
management of the system during the life cycle.
Related Controls:  AT-3, PL-8, PM-7, SA-4, SA-5, SA-8, SA-11, SA-15, SA-17, SA-22, SR-3, SR-4, SR-
5, SR-9.
Control Enhancements:
(1) SYSTEM DEVELOPMENT LIFE CYCLE | MANAGE PREPRODUCTION ENVIRONMENT
Protect system preproduction environments commensurate with risk throughout the
system development life cycle for the system, system component, or system service.
Discussion:  The preproduction environment includes development, test, and integration
environments. The program protection planning processes established by the Department of
Defense are examples of managing the preproduction environment for defense contractors.
Criticality analysis and the application of controls on developers also contribute to a more
secure system development environment.
Related Controls:  CM-2, CM-4, RA-3, RA-9, SA-4.
(2) SYSTEM DEVELOPMENT LIFE CYCLE | USE OF LIVE OR OPERATIONAL DATA
(a) Approve, document, and control the use of live data in preproduction environments
for the system, system component, or system service; and
(b) Protect preproduction environments for the system, system component, or system
service at the same impact or classification level as any live data in use within the
preproduction environments.
Discussion:  Live data is also referred to as operational data. The use of live or operational
data in preproduction (i.e., development, test, and integration) environments can result in
significant risks to organizations. In addition, the use of personally identifiable information in
testing, research, and training increases the risk of unauthorized disclosure or misuse of such
information. Therefore, it is important for the organization to manage any additional risks
that may result from the use of live or operational data. Organizations can minimize such
risks by using test or dummy data during the design, development, and testing of systems,
system components, and system services. Risk assessment techniques may be used to
determine if the risk of using live or operational data is acceptable.
Related Controls:  PM-25, RA-3.
(3) SYSTEM DEVELOPMENT LIFE CYCLE | TECHNOLOGY REFRESH
Plan for and implement a technology refresh schedule for the system throughout the
system development life cycle.
Discussion:  Technology refresh planning may encompass hardware, software, firmware,
processes, personnel skill sets, suppliers, service providers, and facilities. The use of obsolete
or nearing obsolete technology may increase the security and privacy risks associated with
unsupported components, counterfeit or repurposed components, components unable to
implement security or privacy requirements, slow or inoperable components, components
from untrusted sources, inadvertent personnel error, or increased complexity. Technology
refreshes typically occur during the operations and maintenance stage of the system
development life cycle.
Related Controls:  MA-6.
References:  [OMB A-130], [SP 800-30], [SP 800-37], [SP 800-160-1], [SP 800-171], [SP 800-172].
CHAPTER THREE   PAGE 252
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
