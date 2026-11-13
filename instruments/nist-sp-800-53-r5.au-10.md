---
schema_version: 1
corpus: federal-reference
jurisdiction: us
id: nist-sp-800-53-r5.au-10
title: NIST SP 800-53 Rev. 5 AU-10 — NON-REPUDIATION
doc_type: federal_instrument
citation: NIST SP 800-53 Rev. 5 AU-10
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

**NIST SP 800-53 Rev. 5 AU-10** — NON-REPUDIATION

- Issued by: National Institute of Standards and Technology
- Publication: NIST SP 800-53 Rev. 5 — Security and Privacy Controls for Information Systems and Organizations ([nist-sp-800-53-r5](./nist-sp-800-53-r5.md))
- Version: Rev. 5 (September 2020, includes updates as of 2020-12-10)
- Text as of: 2026-11-12
- Cited by held documents: 4 times (6-cfr-37 ×4)
- Reproduction basis: 17 U.S.C. § 105 — work of the U.S. government (NIST). Determined per document on 2026-11-12 against the publication itself, not assumed from its issuer: its Authority statement (PDF page 3) reads "This publication may be used by nongovernmental organizations on a voluntary basis and is not subject to copyright in the United States. Attribution would, however, be appreciated by NIST." Held here: the front matter and Chapter Three (the control catalog) only. Chapter Three names ISO/IEC standards solely as bibliographic references and reproduces none of their text. NOT mirrored: the References bibliography and Appendices A-C; Appendix A (glossary) adapts third-party definitions (ISO/IEC 15026, ISO 25237, ISO/IEC 29100, ISO 15288, IETF RFC 4949), which ADR-0002 treats as not reproducible by being incorporated, and whose reproducibility has not been determined.


_NON-AUTHORITATIVE copy of one control, cut from the SP 800-53 Rev. 5 snapshot this corpus holds. Whether and how this binds a given agency depends on the instrument that incorporates it — read it at the source URL before relying on it. This copy is the Rev. 5 text of record, which is not necessarily the text a citing document meant (a document citing Rev. 4 is not answered by it)._


## Full text

### AU-10 NON-REPUDIATION
Control:  Provide irrefutable evidence that an individual (or process acting on behalf of an
individual) has performed [Assignment: organization-defined actions to be covered by non-
repudiation].
Discussion:  Types of individual actions covered by non-repudiation include creating information,
sending and receiving messages, and approving information. Non-repudiation protects against
claims by authors of not having authored certain documents, senders of not having transmitted
messages, receivers of not having received messages, and signatories of not having signed
documents. Non-repudiation services can be used to determine if information originated from an
individual or if an individual took specific actions (e.g., sending an email, signing a contract,
approving a procurement request, or receiving specific information). Organizations obtain non-
repudiation services by employing various techniques or mechanisms, including digital signatures
and digital message receipts.
Related Controls:  AU-9, PM-12, SA-8, SC-8, SC-12, SC-13, SC-16, SC-17, SC-23.
Control Enhancements:
(1) NON-REPUDIATION | ASSOCIATION OF IDENTITIES
(a) Bind the identity of the information producer with the information to [Assignment:
organization-defined strength of binding]; and
(b) Provide the means for authorized individuals to determine the identity of the
producer of the information.
Discussion:  Binding identities to the information supports audit requirements that provide
organizational personnel with the means to identify who produced specific information in
the event of an information transfer. Organizations determine and approve the strength of
attribute binding between the information producer and the information based on the
security category of the information and other relevant risk factors.
Related Controls:  AC-4, AC-16.
(2) NON-REPUDIATION | VALIDATE BINDING OF INFORMATION PRODUCER IDENTITY
(a) Validate the binding of the information producer identity to the information at
[Assignment: organization-defined frequency]; and
(b) Perform [Assignment: organization-defined actions] in the event of a validation error.
Discussion:  Validating the binding of the information producer identity to the information
prevents the modification of information between production and review. The validation of
bindings can be achieved by, for example, using cryptographic checksums. Organizations
determine if validations are in response to user requests or generated automatically.
Related Controls:  AC-3, AC-4, AC-16.
(3) NON-REPUDIATION | CHAIN OF CUSTODY
Maintain reviewer or releaser credentials within the established chain of custody for
information reviewed or released.
Discussion:  Chain of custody is a process that tracks the movement of evidence through its
collection, safeguarding, and analysis life cycle by documenting each individual who handled
the evidence, the date and time the evidence was collected or transferred, and the purpose
for the transfer. If the reviewer is a human or if the review function is automated but
separate from the release or transfer function, the system associates the identity of the
reviewer of the information to be released with the information and the information label.
In the case of human reviews, maintaining the credentials of reviewers or releasers provides
CHAPTER THREE   PAGE 77
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
the organization with the means to identify who reviewed and released the information. In
the case of automated reviews, it ensures that only approved review functions are used.
Related Controls:  AC-4, AC-16.
(4) NON-REPUDIATION | VALIDATE BINDING OF INFORMATION REVIEWER IDENTITY
(a) Validate the binding of the information reviewer identity to the information at the
transfer or release points prior to release or transfer between [Assignment:
organization-defined security domains]; and
(b) Perform [Assignment: organization-defined actions] in the event of a validation error.
Discussion:  Validating the binding of the information reviewer identity to the information at
transfer or release points prevents the unauthorized modification of information between
review and the transfer or release. The validation of bindings can be achieved by using
cryptographic checksums. Organizations determine if validations are in response to user
requests or generated automatically.
Related Controls:  AC-4, AC-16.
(5) NON-REPUDIATION | DIGITAL SIGNATURES
[Withdrawn: Incorporated into SI-7.]
References:  [FIPS 140-3], [FIPS 180-4], [FIPS 186-4], [FIPS 202], [SP 800-177].
