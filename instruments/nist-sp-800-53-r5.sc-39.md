---
schema_version: 1
corpus: federal-reference
jurisdiction: us
id: nist-sp-800-53-r5.sc-39
title: NIST SP 800-53 Rev. 5 SC-39 — PROCESS ISOLATION
doc_type: federal_instrument
citation: NIST SP 800-53 Rev. 5 SC-39
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

**NIST SP 800-53 Rev. 5 SC-39** — PROCESS ISOLATION

- Issued by: National Institute of Standards and Technology
- Publication: NIST SP 800-53 Rev. 5 — Security and Privacy Controls for Information Systems and Organizations ([nist-sp-800-53-r5](./nist-sp-800-53-r5.md))
- Version: Rev. 5 (September 2020, includes updates as of 2020-12-10)
- Text as of: 2026-11-12
- Cited by held documents: 11 times (cjis-sp-6-1 ×7, irs-pub-1075-11-2021 ×3, 6-cfr-37 ×1)
- Reproduction basis: 17 U.S.C. § 105 — work of the U.S. government (NIST). Determined per document on 2026-11-12 against the publication itself, not assumed from its issuer: its Authority statement (PDF page 3) reads "This publication may be used by nongovernmental organizations on a voluntary basis and is not subject to copyright in the United States. Attribution would, however, be appreciated by NIST." Held here: the front matter and Chapter Three (the control catalog) only. Chapter Three names ISO/IEC standards solely as bibliographic references and reproduces none of their text. NOT mirrored: the References bibliography and Appendices A-C; Appendix A (glossary) adapts third-party definitions (ISO/IEC 15026, ISO 25237, ISO/IEC 29100, ISO 15288, IETF RFC 4949), which ADR-0002 treats as not reproducible by being incorporated, and whose reproducibility has not been determined.


_NON-AUTHORITATIVE copy of one control, cut from the SP 800-53 Rev. 5 snapshot this corpus holds. Whether and how this binds a given agency depends on the instrument that incorporates it — read it at the source URL before relying on it. This copy is the Rev. 5 text of record, which is not necessarily the text a citing document meant (a document citing Rev. 4 is not answered by it)._


## Full text

### SC-39 PROCESS ISOLATION
Control:  Maintain a separate execution domain for each executing system process.
Discussion:  Systems can maintain separate execution domains for each executing process by
assigning each process a separate address space. Each system process has a distinct address
space so that communication between processes is performed in a manner controlled through
the security functions, and one process cannot modify the executing code of another process.
Maintaining separate execution domains for executing processes can be achieved, for example,
by implementing separate address spaces. Process isolation technologies, including sandboxing
or virtualization, logically separate software and firmware from other software, firmware, and
data. Process isolation helps limit the access of potentially untrusted software to other system
resources. The capability to maintain separate execution domains is available in commercial
operating systems that employ multi-state processor technologies.
Related Controls:  AC-3, AC-4, AC-6, AC-25, SA-8, SC-2, SC-3, SI-16.
Control Enhancements:
(1) PROCESS ISOLATION | HARDWARE SEPARATION
Implement hardware separation mechanisms to facilitate process isolation.
Discussion:  Hardware-based separation of system processes is generally less susceptible to
compromise than software-based separation, thus providing greater assurance that the
separation will be enforced. Hardware separation mechanisms include hardware memory
management.
Related Controls:  None.
(2) PROCESS ISOLATION | SEPARATE EXECUTION DOMAIN PER THREAD
Maintain a separate execution domain for each thread in [Assignment: organization-
defined multi-threaded processing].
Discussion:  None.
Related Controls:  None.
References:  [SP 800-160-1].
