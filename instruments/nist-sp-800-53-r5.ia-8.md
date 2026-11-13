---
schema_version: 1
corpus: federal-reference
jurisdiction: us
id: nist-sp-800-53-r5.ia-8
title: NIST SP 800-53 Rev. 5 IA-8 — IDENTIFICATION AND AUTHENTICATION (NON-ORGANIZATIONAL USERS)
doc_type: federal_instrument
citation: NIST SP 800-53 Rev. 5 IA-8
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

**NIST SP 800-53 Rev. 5 IA-8** — IDENTIFICATION AND AUTHENTICATION (NON-ORGANIZATIONAL USERS)

- Issued by: National Institute of Standards and Technology
- Publication: NIST SP 800-53 Rev. 5 — Security and Privacy Controls for Information Systems and Organizations ([nist-sp-800-53-r5](./nist-sp-800-53-r5.md))
- Version: Rev. 5 (September 2020, includes updates as of 2020-12-10)
- Text as of: 2026-11-12
- Cited by held documents: 33 times (cjis-sp-6-1 ×22, arc-ampe ×5, 6-cfr-37 ×3, irs-pub-1075-11-2021 ×3)
- Reproduction basis: 17 U.S.C. § 105 — work of the U.S. government (NIST). Determined per document on 2026-11-12 against the publication itself, not assumed from its issuer: its Authority statement (PDF page 3) reads "This publication may be used by nongovernmental organizations on a voluntary basis and is not subject to copyright in the United States. Attribution would, however, be appreciated by NIST." Held here: the front matter and Chapter Three (the control catalog) only. Chapter Three names ISO/IEC standards solely as bibliographic references and reproduces none of their text. NOT mirrored: the References bibliography and Appendices A-C; Appendix A (glossary) adapts third-party definitions (ISO/IEC 15026, ISO 25237, ISO/IEC 29100, ISO 15288, IETF RFC 4949), which ADR-0002 treats as not reproducible by being incorporated, and whose reproducibility has not been determined.


_NON-AUTHORITATIVE copy of one control, cut from the SP 800-53 Rev. 5 snapshot this corpus holds. Whether and how this binds a given agency depends on the instrument that incorporates it — read it at the source URL before relying on it. This copy is the Rev. 5 text of record, which is not necessarily the text a citing document meant (a document citing Rev. 4 is not answered by it)._


## Full text

### IA-8 IDENTIFICATION AND AUTHENTICATION (NON-ORGANIZATIONAL USERS)
Control:  Uniquely identify and authenticate non-organizational users or processes acting on
behalf of non-organizational users.
CHAPTER THREE   PAGE 144
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
Discussion:  Non-organizational users include system users other than organizational users
explicitly covered by IA-2. Non-organizational users are uniquely identified and authenticated for
accesses other than those explicitly identified and documented in AC-14. Identification and
authentication of non-organizational users accessing federal systems may be required to protect
federal, proprietary, or privacy-related information (with exceptions noted for national security
systems). Organizations consider many factors—including security, privacy, scalability, and
practicality—when balancing the need to ensure ease of use for access to federal information
and systems with the need to protect and adequately mitigate risk.
Related Controls:  AC-2, AC-6, AC-14, AC-17, AC-18, AU-6, IA-2, IA-4, IA-5, IA-10, IA-11, MA-4, RA-
3, SA-4, SC-8.
Control Enhancements:
(1) IDENTIFICATION AND AUTHENTICATION (NON-ORGANIZATIONAL USERS) | ACCEPTANCE OF PIV
CREDENTIALS FROM OTHER AGENCIES
Accept and electronically verify Personal Identity Verification-compliant credentials from
other federal agencies.
Discussion:  Acceptance of Personal Identity Verification (PIV) credentials from other federal
agencies applies to both logical and physical access control systems. PIV credentials are
those credentials issued by federal agencies that conform to FIPS Publication 201 and
supporting guidelines. The adequacy and reliability of PIV card issuers are addressed and
authorized using [SP 800-79-2].
Related Controls:  PE-3.
(2) IDENTIFICATION AND AUTHENTICATION (NON-ORGANIZATIONAL USERS) | ACCEPTANCE OF EXTERNAL
AUTHENTICATORS
(a) Accept only external authenticators that are NIST-compliant; and
(b) Document and maintain a list of accepted external authenticators.
Discussion:  Acceptance of only NIST-compliant external authenticators applies to
organizational systems that are accessible to the public (e.g., public-facing websites).
External authenticators are issued by nonfederal government entities and are compliant
with [SP 800-63B]. Approved external authenticators meet or exceed the minimum Federal
Government-wide technical, security, privacy, and organizational maturity requirements.
Meeting or exceeding Federal requirements allows Federal Government relying parties to
trust external authenticators in connection with an authentication transaction at a specified
authenticator assurance level.
Related Controls:  None.
(3) IDENTIFICATION AND AUTHENTICATION (NON-ORGANIZATIONAL USERS) | USE OF FICAM-APPROVED
PRODUCTS
[Withdrawn: Incorporated into IA-8(2).]
(4) IDENTIFICATION AND AUTHENTICATION (NON-ORGANIZATIONAL USERS) | USE OF DEFINED PROFILES
Conform to the following profiles for identity management [Assignment: organization-
defined identity management profiles].
Discussion:  Organizations define profiles for identity management based on open identity
management standards. To ensure that open identity management standards are viable,
robust, reliable, sustainable, and interoperable as documented, the Federal Government
assesses and scopes the standards and technology implementations against applicable laws,
executive orders, directives, policies, regulations, standards, and guidelines.
Related Controls:  None.
CHAPTER THREE   PAGE 145
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
(5) IDENTIFICATION AND AUTHENTICATION (NON-ORGANIZATIONAL USERS) | ACCEPTANCE OF PIV-I
CREDENTIALS
Accept and verify federated or PKI credentials that meet [Assignment: organization-
defined policy].
Discussion:  Acceptance of PIV-I credentials can be implemented by PIV, PIV-I, and other
commercial or external identity providers. The acceptance and verification of PIV-I-compliant
credentials apply to both logical and physical access control systems. The acceptance and
verification of PIV-I credentials address nonfederal issuers of identity cards that desire to
interoperate with United States Government PIV systems and that can be trusted by Federal
Government-relying parties. The X.509 certificate policy for the Federal Bridge Certification
Authority (FBCA) addresses PIV-I requirements. The PIV-I card is commensurate with the PIV
credentials as defined in cited references. PIV-I credentials are the credentials issued by a
PIV-I provider whose PIV-I certificate policy maps to the Federal Bridge PIV-I Certificate
Policy. A PIV-I provider is cross-certified with the FBCA (directly or through another PKI
bridge) with policies that have been mapped and approved as meeting the requirements of
the PIV-I policies defined in the FBCA certificate policy.
Related Controls:  None.
(6) IDENTIFICATION AND AUTHENTICATION (NON-ORGANIZATIONAL USERS) | DISASSOCIABILITY
Implement the following measures to disassociate user attributes or identifier assertion
relationships among individuals, credential service providers, and relying parties:
[Assignment: organization-defined measures].
Discussion:  Federated identity solutions can create increased privacy risks due to the
tracking and profiling of individuals. Using identifier mapping tables or cryptographic
techniques to blind credential service providers and relying parties from each other or to
make identity attributes less visible to transmitting parties can reduce these privacy risks.
Related Controls:  None.
References:  [OMB A-130], [FED PKI], [FIPS 201-2], [SP 800-63-3], [SP 800-79-2], [SP 800-116], [IR
8062].
