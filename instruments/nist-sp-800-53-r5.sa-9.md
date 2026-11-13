---
schema_version: 1
corpus: federal-reference
jurisdiction: us
id: nist-sp-800-53-r5.sa-9
title: NIST SP 800-53 Rev. 5 SA-9 — EXTERNAL SYSTEM SERVICES
doc_type: federal_instrument
citation: NIST SP 800-53 Rev. 5 SA-9
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

**NIST SP 800-53 Rev. 5 SA-9** — EXTERNAL SYSTEM SERVICES

- Issued by: National Institute of Standards and Technology
- Publication: NIST SP 800-53 Rev. 5 — Security and Privacy Controls for Information Systems and Organizations ([nist-sp-800-53-r5](./nist-sp-800-53-r5.md))
- Version: Rev. 5 (September 2020, includes updates as of 2020-12-10)
- Text as of: 2026-11-12
- Cited by held documents: 31 times (cjis-sp-6-1 ×20, arc-ampe ×5, irs-pub-1075-11-2021 ×5, 6-cfr-37 ×1)
- Reproduction basis: 17 U.S.C. § 105 — work of the U.S. government (NIST). Determined per document on 2026-11-12 against the publication itself, not assumed from its issuer: its Authority statement (PDF page 3) reads "This publication may be used by nongovernmental organizations on a voluntary basis and is not subject to copyright in the United States. Attribution would, however, be appreciated by NIST." Held here: the front matter and Chapter Three (the control catalog) only. Chapter Three names ISO/IEC standards solely as bibliographic references and reproduces none of their text. NOT mirrored: the References bibliography and Appendices A-C; Appendix A (glossary) adapts third-party definitions (ISO/IEC 15026, ISO 25237, ISO/IEC 29100, ISO 15288, IETF RFC 4949), which ADR-0002 treats as not reproducible by being incorporated, and whose reproducibility has not been determined.


_NON-AUTHORITATIVE copy of one control, cut from the SP 800-53 Rev. 5 snapshot this corpus holds. Whether and how this binds a given agency depends on the instrument that incorporates it — read it at the source URL before relying on it. This copy is the Rev. 5 text of record, which is not necessarily the text a citing document meant (a document citing Rev. 4 is not answered by it)._


## Full text

### SA-9 EXTERNAL SYSTEM SERVICES
Control:
a. Require that providers of external system services comply with organizational security and
privacy requirements and employ the following controls: [Assignment: organization-defined
controls];
b. Define and document organizational oversight and user roles and responsibilities with regard
to external system services; and
c. Employ the following processes, methods, and techniques to monitor control compliance by
external service providers on an ongoing basis: [Assignment: organization-defined processes,
methods, and techniques].
Discussion:  External system services are provided by an external provider, and the organization
has no direct control over the implementation of the required controls or the assessment of
control effectiveness. Organizations establish relationships with external service providers in a
variety of ways, including through business partnerships, contracts, interagency agreements,
lines of business arrangements, licensing agreements, joint ventures, and supply chain
exchanges. The responsibility for managing risks from the use of external system services
remains with authorizing officials. For services external to organizations, a chain of trust requires
that organizations establish and retain a certain level of confidence that each provider in the
consumer-provider relationship provides adequate protection for the services rendered. The
extent and nature of this chain of trust vary based on relationships between organizations and
the external providers. Organizations document the basis for the trust relationships so that the
relationships can be monitored. External system services documentation includes government,
service providers, end user security roles and responsibilities, and service-level agreements.
Service-level agreements define the expectations of performance for implemented controls,
describe measurable outcomes, and identify remedies and response requirements for identified
instances of noncompliance.
Related Controls:  AC-20, CA-3, CP-2, IR-4, IR-7, PL-10, PL-11, PS-7, SA-2, SA-4, SR-3, SR-5.
Control Enhancements:
(1) EXTERNAL SYSTEM SERVICES | RISK ASSESSMENTS AND ORGANIZATIONAL APPROVALS
(a) Conduct an organizational assessment of risk prior to the acquisition or outsourcing of
information security services; and
(b) Verify that the acquisition or outsourcing of dedicated information security services is
approved by [Assignment: organization-defined personnel or roles].
Discussion:  Information security services include the operation of security devices, such as
firewalls or key management services as well as incident monitoring, analysis, and response.
Risks assessed can include system, mission or business, security, privacy, or supply chain
risks.
Related Controls:  CA-6, RA-3, RA-8.
(2) EXTERNAL SYSTEM SERVICES | IDENTIFICATION OF FUNCTIONS, PORTS, PROTOCOLS, AND SERVICES
Require providers of the following external system services to identify the functions, ports,
protocols, and other services required for the use of such services: [Assignment:
organization-defined external system services].
CHAPTER THREE   PAGE 272
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
Discussion:  Information from external service providers regarding the specific functions,
ports, protocols, and services used in the provision of such services can be useful when the
need arises to understand the trade-offs involved in restricting certain functions and services
or blocking certain ports and protocols.
Related Controls:  CM-6, CM-7.
(3) EXTERNAL SYSTEM SERVICES | ESTABLISH AND MAINTAIN TRUST RELATIONSHIP WITH PROVIDERS
Establish, document, and maintain trust relationships with external service providers
based on the following requirements, properties, factors, or conditions: [Assignment:
organization-defined security and privacy requirements, properties, factors, or conditions
defining acceptable trust relationships].
Discussion:  Trust relationships between organizations and external service providers reflect
the degree of confidence that the risk from using external services is at an acceptable level.
Trust relationships can help organizations gain increased levels of confidence that service
providers are providing adequate protection for the services rendered and can also be useful
when conducting incident response or when planning for upgrades or obsolescence. Trust
relationships can be complicated due to the potentially large number of entities participating
in the consumer-provider interactions, subordinate relationships and levels of trust, and
types of interactions between the parties. In some cases, the degree of trust is based on the
level of control that organizations can exert on external service providers regarding the
controls necessary for the protection of the service, information, or individual privacy and
the evidence brought forth as to the effectiveness of the implemented controls. The level of
control is established by the terms and conditions of the contracts or service-level
agreements.
Related Controls:  SR-2.
(4) EXTERNAL SYSTEM SERVICES |CONSISTENT INTERESTS OF CONSUMERS AND PROVIDERS
Take the following actions to verify that the interests of [Assignment: organization-
defined external service providers] are consistent with and reflect organizational interests:
[Assignment: organization-defined actions].
Discussion:  As organizations increasingly use external service providers, it is possible that
the interests of the service providers may diverge from organizational interests. In such
situations, simply having the required technical, management, or operational controls in
place may not be sufficient if the providers that implement and manage those controls are
not operating in a manner consistent with the interests of the consuming organizations.
Actions that organizations take to address such concerns include requiring background
checks for selected service provider personnel; examining ownership records; employing
only trustworthy service providers, such as providers with which organizations have had
successful trust relationships; and conducting routine, periodic, unscheduled visits to service
provider facilities.
Related Controls:  None.
(5) EXTERNAL SYSTEM SERVICES | PROCESSING, STORAGE, AND SERVICE LOCATION
Restrict the location of [Selection (one or more): information processing; information or
data; system services] to [Assignment: organization-defined locations] based on
[Assignment: organization-defined requirements or conditions].
Discussion:  The location of information processing, information and data storage, or system
services can have a direct impact on the ability of organizations to successfully execute their
mission and business functions. The impact occurs when external providers control the
location of processing, storage, or services. The criteria that external providers use for the
selection of processing, storage, or service locations may be different from the criteria that
organizations use. For example, organizations may desire that data or information storage
CHAPTER THREE   PAGE 273
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
locations be restricted to certain locations to help facilitate incident response activities in
case of information security incidents or breaches. Incident response activities, including
forensic analyses and after-the-fact investigations, may be adversely affected by the
governing laws, policies, or protocols in the locations where processing and storage occur
and/or the locations from which system services emanate.
Related Controls:  SA-5, SR-4.
(6) EXTERNAL SYSTEM SERVICES | ORGANIZATION-CONTROLLED CRYPTOGRAPHIC KEYS
Maintain exclusive control of cryptographic keys for encrypted material stored or
transmitted through an external system.
Discussion:  Maintaining exclusive control of cryptographic keys in an external system
prevents decryption of organizational data by external system staff. Organizational control
of cryptographic keys can be implemented by encrypting and decrypting data inside the
organization as data is sent to and received from the external system or by employing a
component that permits encryption and decryption functions to be local to the external
system but allows exclusive organizational access to the encryption keys.
Related Controls:  SC-12, SC-13, SI-4.
(7) EXTERNAL SYSTEM SERVICES | ORGANIZATION-CONTROLLED INTEGRITY CHECKING
Provide the capability to check the integrity of information while it resides in the external
system.
Discussion:  Storage of organizational information in an external system could limit visibility
into the security status of its data. The ability of the organization to verify and validate the
integrity of its stored data without transferring it out of the external system provides such
visibility.
Related Controls:  SI-7.
(8) EXTERNAL SYSTEM SERVICES | PROCESSING AND STORAGE LOCATION — U.S. JURISDICTION
Restrict the geographic location of information processing and data storage to facilities
located within in the legal jurisdictional boundary of the United States.
Discussion:  The geographic location of information processing and data storage can have a
direct impact on the ability of organizations to successfully execute their mission and
business functions. A compromise or breach of high impact information and systems can
have severe or catastrophic adverse impacts on organizational assets and operations,
individuals, other organizations, and the Nation. Restricting the processing and storage of
high-impact information to facilities within the legal jurisdictional boundary of the United
States provides greater control over such processing and storage.
Related Controls:  SA-5, SR-4.
References:  [OMB A-130], [SP 800-35], [SP 800-160-1], [SP 800-161], [SP 800-171].
