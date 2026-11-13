---
schema_version: 1
corpus: federal-reference
jurisdiction: us
id: nist-sp-800-53-r5.sc-23
title: NIST SP 800-53 Rev. 5 SC-23 — SESSION AUTHENTICITY
doc_type: federal_instrument
citation: NIST SP 800-53 Rev. 5 SC-23
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

**NIST SP 800-53 Rev. 5 SC-23** — SESSION AUTHENTICITY

- Issued by: National Institute of Standards and Technology
- Publication: NIST SP 800-53 Rev. 5 — Security and Privacy Controls for Information Systems and Organizations ([nist-sp-800-53-r5](./nist-sp-800-53-r5.md))
- Version: Rev. 5 (September 2020, includes updates as of 2020-12-10)
- Text as of: 2026-11-12
- Cited by held documents: 15 times (cjis-sp-6-1 ×10, irs-pub-1075-11-2021 ×3, 6-cfr-37 ×1, arc-ampe ×1)
- Reproduction basis: 17 U.S.C. § 105 — work of the U.S. government (NIST). Determined per document on 2026-11-12 against the publication itself, not assumed from its issuer: its Authority statement (PDF page 3) reads "This publication may be used by nongovernmental organizations on a voluntary basis and is not subject to copyright in the United States. Attribution would, however, be appreciated by NIST." Held here: the front matter and Chapter Three (the control catalog) only. Chapter Three names ISO/IEC standards solely as bibliographic references and reproduces none of their text. NOT mirrored: the References bibliography and Appendices A-C; Appendix A (glossary) adapts third-party definitions (ISO/IEC 15026, ISO 25237, ISO/IEC 29100, ISO 15288, IETF RFC 4949), which ADR-0002 treats as not reproducible by being incorporated, and whose reproducibility has not been determined.


_NON-AUTHORITATIVE copy of one control, cut from the SP 800-53 Rev. 5 snapshot this corpus holds. Whether and how this binds a given agency depends on the instrument that incorporates it — read it at the source URL before relying on it. This copy is the Rev. 5 text of record, which is not necessarily the text a citing document meant (a document citing Rev. 4 is not answered by it)._


## Full text

### SC-23 SESSION AUTHENTICITY
Control:  Protect the authenticity of communications sessions.
Discussion:  Protecting session authenticity addresses communications protection at the session
level, not at the packet level. Such protection establishes grounds for confidence at both ends of
communications sessions in the ongoing identities of other parties and the validity of transmitted
information. Authenticity protection includes protecting against “man-in-the-middle” attacks,
session hijacking, and the insertion of false information into sessions.
Related Controls:  AU-10, SC-8, SC-10, SC-11.
Control Enhancements:
(1) SESSION AUTHENTICITY | INVALIDATE SESSION IDENTIFIERS AT LOGOUT
Invalidate session identifiers upon user logout or other session termination.
Discussion:  Invalidating session identifiers at logout curtails the ability of adversaries to
capture and continue to employ previously valid session IDs.
CHAPTER THREE   PAGE 315
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
Related Controls:  None.
(2) SESSION AUTHENTICITY | USER-INITIATED LOGOUTS AND MESSAGE DISPLAYS
[Withdrawn: Incorporated into AC-12(1).]
(3) SESSION AUTHENTICITY | UNIQUE SYSTEM-GENERATED SESSION IDENTIFIERS
Generate a unique session identifier for each session with [Assignment: organization-
defined randomness requirements] and recognize only session identifiers that are system-
generated.
Discussion:  Generating unique session identifiers curtails the ability of adversaries to reuse
previously valid session IDs. Employing the concept of randomness in the generation of
unique session identifiers protects against brute-force attacks to determine future session
identifiers.
Related Controls:  AC-10, SC-12, SC-13.
(4) SESSION AUTHENTICITY | UNIQUE SESSION IDENTIFIERS WITH RANDOMIZATION
[Withdrawn: Incorporated into SC-23(3).]
(5) SESSION AUTHENTICITY | ALLOWED CERTIFICATE AUTHORITIES
Only allow the use of [Assignment: organization-defined certificate authorities] for
verification of the establishment of protected sessions.
Discussion:  Reliance on certificate authorities for the establishment of secure sessions
includes the use of Transport Layer Security (TLS) certificates. These certificates, after
verification by their respective certificate authorities, facilitate the establishment of
protected sessions between web clients and web servers.
Related Controls:  SC-12, SC-13.
References:  [SP 800-52], [SP 800-77], [SP 800-95], [SP 800-113].
