---
schema_version: 1
corpus: federal-reference
jurisdiction: us
id: nist-sp-800-53-r5.sc-20
title: NIST SP 800-53 Rev. 5 SC-20 — SECURE NAME/ADDRESS RESOLUTION SERVICE (AUTHORITATIVE SOURCE)
doc_type: federal_instrument
citation: NIST SP 800-53 Rev. 5 SC-20
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

**NIST SP 800-53 Rev. 5 SC-20** — SECURE NAME/ADDRESS RESOLUTION SERVICE (AUTHORITATIVE SOURCE)

- Issued by: National Institute of Standards and Technology
- Publication: NIST SP 800-53 Rev. 5 — Security and Privacy Controls for Information Systems and Organizations ([nist-sp-800-53-r5](./nist-sp-800-53-r5.md))
- Version: Rev. 5 (September 2020, includes updates as of 2020-12-10)
- Text as of: 2026-11-12
- Cited by held documents: 18 times (cjis-sp-6-1 ×10, arc-ampe ×3, irs-pub-1075-11-2021 ×3, 6-cfr-37 ×2)
- Reproduction basis: 17 U.S.C. § 105 — work of the U.S. government (NIST). Determined per document on 2026-11-12 against the publication itself, not assumed from its issuer: its Authority statement (PDF page 3) reads "This publication may be used by nongovernmental organizations on a voluntary basis and is not subject to copyright in the United States. Attribution would, however, be appreciated by NIST." Held here: the front matter and Chapter Three (the control catalog) only. Chapter Three names ISO/IEC standards solely as bibliographic references and reproduces none of their text. NOT mirrored: the References bibliography and Appendices A-C; Appendix A (glossary) adapts third-party definitions (ISO/IEC 15026, ISO 25237, ISO/IEC 29100, ISO 15288, IETF RFC 4949), which ADR-0002 treats as not reproducible by being incorporated, and whose reproducibility has not been determined.


_NON-AUTHORITATIVE copy of one control, cut from the SP 800-53 Rev. 5 snapshot this corpus holds. Whether and how this binds a given agency depends on the instrument that incorporates it — read it at the source URL before relying on it. This copy is the Rev. 5 text of record, which is not necessarily the text a citing document meant (a document citing Rev. 4 is not answered by it)._


## Full text

### SC-20 SECURE NAME/ADDRESS RESOLUTION SERVICE (AUTHORITATIVE SOURCE)
Control:
a. Provide additional data origin authentication and integrity verification artifacts along with
the authoritative name resolution data the system returns in response to external
name/address resolution queries; and
b. Provide the means to indicate the security status of child zones and (if the child supports
secure resolution services) to enable verification of a chain of trust among parent and child
domains, when operating as part of a distributed, hierarchical namespace.
Discussion:  Providing authoritative source information enables external clients, including remote
Internet clients, to obtain origin authentication and integrity verification assurances for the
host/service name to network address resolution information obtained through the service.
Systems that provide name and address resolution services include domain name system (DNS)
servers. Additional artifacts include DNS Security Extensions (DNSSEC) digital signatures and
cryptographic keys. Authoritative data includes DNS resource records. The means for indicating
the security status of child zones include the use of delegation signer resource records in the
DNS. Systems that use technologies other than the DNS to map between host and service names
and network addresses provide other means to assure the authenticity and integrity of response
data.
Related Controls:  AU-10, SC-8, SC-12, SC-13, SC-21, SC-22.
Control Enhancements:
(1) SECURE NAME/ADDRESS RESOLUTION SERVICE (AUTHORITATIVE SOURCE) | CHILD SUBSPACES
[Withdrawn: Incorporated into SC-20.]
(2) SECURE NAME/ADDRESS RESOLUTION SERVICE (AUTHORITATIVE SOURCE) | DATA ORIGIN AND
INTEGRITY
Provide data origin and integrity protection artifacts for internal name/address resolution
queries.
Discussion:  None.
Related Controls:  None.
References:  [FIPS 140-3], [FIPS 186-4], [SP 800-81-2].
