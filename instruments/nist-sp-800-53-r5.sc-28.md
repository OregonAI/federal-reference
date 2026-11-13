---
schema_version: 1
corpus: federal-reference
jurisdiction: us
id: nist-sp-800-53-r5.sc-28
title: NIST SP 800-53 Rev. 5 SC-28 — PROTECTION OF INFORMATION AT REST
doc_type: federal_instrument
citation: NIST SP 800-53 Rev. 5 SC-28
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

**NIST SP 800-53 Rev. 5 SC-28** — PROTECTION OF INFORMATION AT REST

- Issued by: National Institute of Standards and Technology
- Publication: NIST SP 800-53 Rev. 5 — Security and Privacy Controls for Information Systems and Organizations ([nist-sp-800-53-r5](./nist-sp-800-53-r5.md))
- Version: Rev. 5 (September 2020, includes updates as of 2020-12-10)
- Text as of: 2026-11-12
- Cited by held documents: 30 times (cjis-sp-6-1 ×22, irs-pub-1075-11-2021 ×4, 6-cfr-37 ×2, arc-ampe ×2)
- Reproduction basis: 17 U.S.C. § 105 — work of the U.S. government (NIST). Determined per document on 2026-11-12 against the publication itself, not assumed from its issuer: its Authority statement (PDF page 3) reads "This publication may be used by nongovernmental organizations on a voluntary basis and is not subject to copyright in the United States. Attribution would, however, be appreciated by NIST." Held here: the front matter and Chapter Three (the control catalog) only. Chapter Three names ISO/IEC standards solely as bibliographic references and reproduces none of their text. NOT mirrored: the References bibliography and Appendices A-C; Appendix A (glossary) adapts third-party definitions (ISO/IEC 15026, ISO 25237, ISO/IEC 29100, ISO 15288, IETF RFC 4949), which ADR-0002 treats as not reproducible by being incorporated, and whose reproducibility has not been determined.


_NON-AUTHORITATIVE copy of one control, cut from the SP 800-53 Rev. 5 snapshot this corpus holds. Whether and how this binds a given agency depends on the instrument that incorporates it — read it at the source URL before relying on it. This copy is the Rev. 5 text of record, which is not necessarily the text a citing document meant (a document citing Rev. 4 is not answered by it)._


## Full text

### SC-28 PROTECTION OF INFORMATION AT REST
Control:  Protect the [Selection (one or more): confidentiality; integrity] of the following
information at rest: [Assignment: organization-defined information at rest].
Discussion:  Information at rest refers to the state of information when it is not in process or in
transit and is located on system components. Such components include internal or external hard
disk drives, storage area network devices, or databases. However, the focus of protecting
information at rest is not on the type of storage device or frequency of access but rather on the
state of the information. Information at rest addresses the confidentiality and integrity of
CHAPTER THREE   PAGE 317
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
information and covers user information and system information. System-related information
that requires protection includes configurations or rule sets for firewalls, intrusion detection and
prevention systems, filtering routers, and authentication information. Organizations may employ
different mechanisms to achieve confidentiality and integrity protections, including the use of
cryptographic mechanisms and file share scanning. Integrity protection can be achieved, for
example, by implementing write-once-read-many (WORM) technologies. When adequate
protection of information at rest cannot otherwise be achieved, organizations may employ other
controls, including frequent scanning to identify malicious code at rest and secure offline storage
in lieu of online storage.
Related Controls:  AC-3, AC-4, AC-6, AC-19, CA-7, CM-3, CM-5, CM-6, CP-9, MP-4, MP-5, PE-3, SC-
8, SC-12, SC-13, SC-34, SI-3, SI-7, SI-16.
Control Enhancements:
(1) PROTECTION OF INFORMATION AT REST | CRYPTOGRAPHIC PROTECTION
Implement cryptographic mechanisms to prevent unauthorized disclosure and
modification of the following information at rest on [Assignment: organization-defined
system components or media]: [Assignment: organization-defined information].
Discussion:  The selection of cryptographic mechanisms is based on the need to protect the
confidentiality and integrity of organizational information. The strength of mechanism is
commensurate with the security category or classification of the information. Organizations
have the flexibility to encrypt information on system components or media or encrypt data
structures, including files, records, or fields.
Related Controls:  AC-19, SC-12, SC-13.
(2) PROTECTION OF INFORMATION AT REST | OFFLINE STORAGE
Remove the following information from online storage and store offline in a secure
location: [Assignment: organization-defined information].
Discussion:  Removing organizational information from online storage to offline storage
eliminates the possibility of individuals gaining unauthorized access to the information
through a network. Therefore, organizations may choose to move information to offline
storage in lieu of protecting such information in online storage.
Related Controls:  None.
(3) PROTECTION OF INFORMATION AT REST | CRYPTOGRAPHIC KEYS
Provide protected storage for cryptographic keys [Selection: [Assignment: organization-
defined safeguards]; hardware-protected key store].
Discussion:  A Trusted Platform Module (TPM) is an example of a hardware-protected data
store that can be used to protect cryptographic keys.
Related Controls:  SC-12, SC-13.
References:  [OMB A-130], [SP 800-56A], [SP 800-56B], [SP 800-56C], [SP 800-57-1], [SP 800-57-
2], [SP 800-57-3], [SP 800-111], [SP 800-124].
