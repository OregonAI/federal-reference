---
schema_version: 1
corpus: federal-reference
jurisdiction: us
id: nist-sp-800-53-r5.ia-12
title: NIST SP 800-53 Rev. 5 IA-12 — IDENTITY PROOFING
doc_type: federal_instrument
citation: NIST SP 800-53 Rev. 5 IA-12
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

**NIST SP 800-53 Rev. 5 IA-12** — IDENTITY PROOFING

- Issued by: National Institute of Standards and Technology
- Publication: NIST SP 800-53 Rev. 5 — Security and Privacy Controls for Information Systems and Organizations ([nist-sp-800-53-r5](./nist-sp-800-53-r5.md))
- Version: Rev. 5 (September 2020, includes updates as of 2020-12-10)
- Text as of: 2026-11-12
- Cited by held documents: 30 times (cjis-sp-6-1 ×21, arc-ampe ×4, irs-pub-1075-11-2021 ×4, 6-cfr-37 ×1), 1 of them naming an enhancement of this control
- Reproduction basis: 17 U.S.C. § 105 — work of the U.S. government (NIST). Determined per document on 2026-11-12 against the publication itself, not assumed from its issuer: its Authority statement (PDF page 3) reads "This publication may be used by nongovernmental organizations on a voluntary basis and is not subject to copyright in the United States. Attribution would, however, be appreciated by NIST." Held here: the front matter and Chapter Three (the control catalog) only. Chapter Three names ISO/IEC standards solely as bibliographic references and reproduces none of their text. NOT mirrored: the References bibliography and Appendices A-C; Appendix A (glossary) adapts third-party definitions (ISO/IEC 15026, ISO 25237, ISO/IEC 29100, ISO 15288, IETF RFC 4949), which ADR-0002 treats as not reproducible by being incorporated, and whose reproducibility has not been determined.


_NON-AUTHORITATIVE copy of one control, cut from the SP 800-53 Rev. 5 snapshot this corpus holds. Whether and how this binds a given agency depends on the instrument that incorporates it — read it at the source URL before relying on it. This copy is the Rev. 5 text of record, which is not necessarily the text a citing document meant (a document citing Rev. 4 is not answered by it)._


## Full text

### IA-12 IDENTITY PROOFING
Control:
a. Identity proof users that require accounts for logical access to systems based on appropriate
identity assurance level requirements as specified in applicable standards and guidelines;
b. Resolve user identities to a unique individual; and
c. Collect, validate, and verify identity evidence.
Discussion:  Identity proofing is the process of collecting, validating, and verifying a user’s
identity information for the purposes of establishing credentials for accessing a system. Identity
proofing is intended to mitigate threats to the registration of users and the establishment of
CHAPTER THREE   PAGE 147
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
their accounts. Standards and guidelines specifying identity assurance levels for identity proofing
include [SP 800-63-3] and [SP 800-63A]. Organizations may be subject to laws, executive orders,
directives, regulations, or policies that address the collection of identity evidence. Organizational
personnel consult with the senior agency official for privacy and legal counsel regarding such
requirements.
Related Controls:  AC-5, IA-1, IA-2, IA-3, IA-4, IA-5,  IA-6, IA-8.
Control Enhancements:
(1) IDENTITY PROOFING | SUPERVISOR AUTHORIZATION
Require that the registration process to receive an account for logical access includes
supervisor or sponsor authorization.
Discussion:  Including supervisor or sponsor authorization as part of the registration process
provides an additional level of scrutiny to ensure that the user’s management chain is aware
of the account, the account is essential to carry out organizational missions and functions,
and the user’s privileges are appropriate for the anticipated responsibilities and authorities
within the organization.
Related Controls:  None.
(2) IDENTITY PROOFING | IDENTITY EVIDENCE
Require evidence of individual identification be presented to the registration authority.
Discussion:  Identity evidence, such as documentary evidence or a combination of
documents and biometrics, reduces the likelihood of individuals using fraudulent
identification to establish an identity or at least increases the work factor of potential
adversaries. The forms of acceptable evidence are consistent with the risks to the systems,
roles, and privileges associated with the user’s account.
Related Controls:  None.
(3) IDENTITY PROOFING | IDENTITY EVIDENCE VALIDATION AND VERIFICATION
Require that the presented identity evidence be validated and verified through
[Assignment: organizational defined methods of validation and verification].
Discussion:  Validation and verification of identity evidence increases the assurance that
accounts and identifiers are being established for the correct user and authenticators are
being bound to that user. Validation refers to the process of confirming that the evidence is
genuine and authentic, and the data contained in the evidence is correct, current, and
related to an individual. Verification confirms and establishes a linkage between the claimed
identity and the actual existence of the user presenting the evidence. Acceptable methods
for validating and verifying identity evidence are consistent with the risks to the systems,
roles, and privileges associated with the users account.
Related Controls:  None.
(4) IDENTITY PROOFING | IN-PERSON VALIDATION AND VERIFICATION
Require that the validation and verification of identity evidence be conducted in person
before a designated registration authority.
Discussion:  In-person proofing reduces the likelihood of fraudulent credentials being issued
because it requires the physical presence of individuals, the presentation of physical identity
documents, and actual face-to-face interactions with designated registration authorities.
Related Controls:  None.
(5) IDENTITY PROOFING | ADDRESS CONFIRMATION
CHAPTER THREE   PAGE 148
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
Require that a [Selection: registration code; notice of proofing] be delivered through an
out-of-band channel to verify the users address (physical or digital) of record.
Discussion:  To make it more difficult for adversaries to pose as legitimate users during the
identity proofing process, organizations can use out-of-band methods to ensure that the
individual associated with an address of record is the same individual that participated in the
registration. Confirmation can take the form of a temporary enrollment code or a notice of
proofing. The delivery address for these artifacts is obtained from records and not self-
asserted by the user. The address can include a physical or digital address. A home address is
an example of a physical address. Email addresses and telephone numbers are examples of
digital addresses.
Related Controls:  IA-12.
(6) IDENTITY PROOFING | ACCEPT EXTERNALLY-PROOFED IDENTITIES
Accept externally-proofed identities at [Assignment: organization-defined identity
assurance level].
Discussion:  To limit unnecessary re-proofing of identities, particularly of non-PIV users,
organizations accept proofing conducted at a commensurate level of assurance by other
agencies or organizations. Proofing is consistent with organizational security policy and the
identity assurance level appropriate for the system, application, or information accessed.
Accepting externally-proofed identities is a fundamental component of managing federated
identities across agencies and organizations.
Related Controls:  IA-3, IA-4, IA-5, IA-8.
References:  [FIPS 201-2], [SP 800-63-3], [SP 800-63A], [SP 800-79-2].
CHAPTER THREE   PAGE 149
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
3.8   INCIDENT RESPONSE
Quick link to Incident Response Summary Table
