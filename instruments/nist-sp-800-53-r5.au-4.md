---
schema_version: 1
corpus: federal-reference
jurisdiction: us
id: nist-sp-800-53-r5.au-4
title: NIST SP 800-53 Rev. 5 AU-4 — AUDIT LOG STORAGE CAPACITY
doc_type: federal_instrument
citation: NIST SP 800-53 Rev. 5 AU-4
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

**NIST SP 800-53 Rev. 5 AU-4** — AUDIT LOG STORAGE CAPACITY

- Issued by: National Institute of Standards and Technology
- Publication: NIST SP 800-53 Rev. 5 — Security and Privacy Controls for Information Systems and Organizations ([nist-sp-800-53-r5](./nist-sp-800-53-r5.md))
- Version: Rev. 5 (September 2020, includes updates as of 2020-12-10)
- Text as of: 2026-11-12
- Cited by held documents: 19 times (cjis-sp-6-1 ×10, 6-cfr-37 ×4, irs-pub-1075-11-2021 ×3, arc-ampe ×2)
- Reproduction basis: 17 U.S.C. § 105 — work of the U.S. government (NIST). Determined per document on 2026-11-12 against the publication itself, not assumed from its issuer: its Authority statement (PDF page 3) reads "This publication may be used by nongovernmental organizations on a voluntary basis and is not subject to copyright in the United States. Attribution would, however, be appreciated by NIST." Held here: the front matter and Chapter Three (the control catalog) only. Chapter Three names ISO/IEC standards solely as bibliographic references and reproduces none of their text. NOT mirrored: the References bibliography and Appendices A-C; Appendix A (glossary) adapts third-party definitions (ISO/IEC 15026, ISO 25237, ISO/IEC 29100, ISO 15288, IETF RFC 4949), which ADR-0002 treats as not reproducible by being incorporated, and whose reproducibility has not been determined.


_NON-AUTHORITATIVE copy of one control, cut from the SP 800-53 Rev. 5 snapshot this corpus holds. Whether and how this binds a given agency depends on the instrument that incorporates it — read it at the source URL before relying on it. This copy is the Rev. 5 text of record, which is not necessarily the text a citing document meant (a document citing Rev. 4 is not answered by it)._


## Full text

### AU-4 AUDIT LOG STORAGE CAPACITY
Control:  Allocate audit log storage capacity to accommodate [Assignment: organization-defined
audit log retention requirements].
Discussion:  Organizations consider the types of audit logging to be performed and the audit log
processing requirements when allocating audit log storage capacity. Allocating sufficient audit
log storage capacity reduces the likelihood of such capacity being exceeded and resulting in the
potential loss or reduction of audit logging capability.
Related Controls:  AU-2, AU-5, AU-6, AU-7, AU-9, AU-11, AU-12, AU-14, SI-4.
Control Enhancements:
(1) AUDIT LOG STORAGE CAPACITY | TRANSFER TO ALTERNATE STORAGE
Transfer audit logs [Assignment: organization-defined frequency] to a different system,
system component, or media other than the system or system component conducting the
logging.
Discussion:  Audit log transfer, also known as off-loading, is a common process in systems
with limited audit log storage capacity and thus supports availability of the audit logs. The
initial audit log storage is only used in a transitory fashion until the system can communicate
with the secondary or alternate system allocated to audit log storage, at which point the
audit logs are transferred. Transferring audit logs to alternate storage is similar to AU-9(2) in
that audit logs are transferred to a different entity. However, the purpose of selecting AU-
9(2) is to protect the confidentiality and integrity of audit records. Organizations can select
either control enhancement to obtain the benefit of increased audit log storage capacity and
preserving the confidentiality, integrity, and availability of audit records and logs.
Related Controls:  None.
References:  None.
