---
schema_version: 1
corpus: federal-reference
jurisdiction: us
id: nist-sp-800-53-r5.ca-9
title: NIST SP 800-53 Rev. 5 CA-9 — INTERNAL SYSTEM CONNECTIONS
doc_type: federal_instrument
citation: NIST SP 800-53 Rev. 5 CA-9
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

**NIST SP 800-53 Rev. 5 CA-9** — INTERNAL SYSTEM CONNECTIONS

- Issued by: National Institute of Standards and Technology
- Publication: NIST SP 800-53 Rev. 5 — Security and Privacy Controls for Information Systems and Organizations ([nist-sp-800-53-r5](./nist-sp-800-53-r5.md))
- Version: Rev. 5 (September 2020, includes updates as of 2020-12-10)
- Text as of: 2026-11-12
- Cited by held documents: 19 times (cjis-sp-6-1 ×14, irs-pub-1075-11-2021 ×3, 6-cfr-37 ×1, arc-ampe ×1)
- Reproduction basis: 17 U.S.C. § 105 — work of the U.S. government (NIST). Determined per document on 2026-11-12 against the publication itself, not assumed from its issuer: its Authority statement (PDF page 3) reads "This publication may be used by nongovernmental organizations on a voluntary basis and is not subject to copyright in the United States. Attribution would, however, be appreciated by NIST." Held here: the front matter and Chapter Three (the control catalog) only. Chapter Three names ISO/IEC standards solely as bibliographic references and reproduces none of their text. NOT mirrored: the References bibliography and Appendices A-C; Appendix A (glossary) adapts third-party definitions (ISO/IEC 15026, ISO 25237, ISO/IEC 29100, ISO 15288, IETF RFC 4949), which ADR-0002 treats as not reproducible by being incorporated, and whose reproducibility has not been determined.


_NON-AUTHORITATIVE copy of one control, cut from the SP 800-53 Rev. 5 snapshot this corpus holds. Whether and how this binds a given agency depends on the instrument that incorporates it — read it at the source URL before relying on it. This copy is the Rev. 5 text of record, which is not necessarily the text a citing document meant (a document citing Rev. 4 is not answered by it)._


## Full text

### CA-9 INTERNAL SYSTEM CONNECTIONS
Control:
a. Authorize internal connections of [Assignment: organization-defined system components or
classes of components] to the system;
b. Document, for each internal connection, the interface characteristics, security and privacy
requirements, and the nature of the information communicated;
c. Terminate internal system connections after [Assignment: organization-defined conditions];
and
d. Review [Assignment: organization-defined frequency] the continued need for each internal
connection.
Discussion:  Internal system connections are connections between organizational systems and
separate constituent system components (i.e., connections between components that are part of
the same system) including components used for system development. Intra-system connections
include connections with mobile devices, notebook and desktop computers, tablets, printers,
copiers, facsimile machines, scanners, sensors, and servers. Instead of authorizing each internal
system connection individually, organizations can authorize internal connections for a class of
system components with common characteristics and/or configurations, including printers,
scanners, and copiers with a specified processing, transmission, and storage capability or smart
phones and tablets with a specific baseline configuration. The continued need for an internal
system connection is reviewed from the perspective of whether it provides support for
organizational missions or business functions.
Related Controls:  AC-3, AC-4, AC-18, AC-19, CM-2, IA-3, SC-7, SI-12.
Control Enhancements:
CHAPTER THREE   PAGE 95
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
(1) INTERNAL SYSTEM CONNECTIONS | COMPLIANCE CHECKS
Perform security and privacy compliance checks on constituent system components prior
to the establishment of the internal connection.
Discussion:  Compliance checks include verification of the relevant baseline configuration.
Related Controls:  CM-6.
References:  [SP 800-124], [IR 8023].
CHAPTER THREE   PAGE 96
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
3.5   CONFIGURATION MANAGEMENT
Quick link to Configuration Management Summary Table
