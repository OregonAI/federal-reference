---
schema_version: 1
corpus: federal-reference
jurisdiction: us
id: nist-sp-800-53-r5.cm-12
title: NIST SP 800-53 Rev. 5 CM-12 — INFORMATION LOCATION
doc_type: federal_instrument
citation: NIST SP 800-53 Rev. 5 CM-12
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

**NIST SP 800-53 Rev. 5 CM-12** — INFORMATION LOCATION

- Issued by: National Institute of Standards and Technology
- Publication: NIST SP 800-53 Rev. 5 — Security and Privacy Controls for Information Systems and Organizations ([nist-sp-800-53-r5](./nist-sp-800-53-r5.md))
- Version: Rev. 5 (September 2020, includes updates as of 2020-12-10)
- Text as of: 2026-11-12
- Cited by held documents: 10 times (cjis-sp-6-1 ×4, irs-pub-1075-11-2021 ×3, arc-ampe ×2, 6-cfr-37 ×1)
- Reproduction basis: 17 U.S.C. § 105 — work of the U.S. government (NIST). Determined per document on 2026-11-12 against the publication itself, not assumed from its issuer: its Authority statement (PDF page 3) reads "This publication may be used by nongovernmental organizations on a voluntary basis and is not subject to copyright in the United States. Attribution would, however, be appreciated by NIST." Held here: the front matter and Chapter Three (the control catalog) only. Chapter Three names ISO/IEC standards solely as bibliographic references and reproduces none of their text. NOT mirrored: the References bibliography and Appendices A-C; Appendix A (glossary) adapts third-party definitions (ISO/IEC 15026, ISO 25237, ISO/IEC 29100, ISO 15288, IETF RFC 4949), which ADR-0002 treats as not reproducible by being incorporated, and whose reproducibility has not been determined.


_NON-AUTHORITATIVE copy of one control, cut from the SP 800-53 Rev. 5 snapshot this corpus holds. Whether and how this binds a given agency depends on the instrument that incorporates it — read it at the source URL before relying on it. This copy is the Rev. 5 text of record, which is not necessarily the text a citing document meant (a document citing Rev. 4 is not answered by it)._


## Full text

### CM-12 INFORMATION LOCATION
Control:
a. Identify and document the location of [Assignment: organization-defined information] and
the specific system components on which the information is processed and stored;
b. Identify and document the users who have access to the system and system components
where the information is processed and stored; and
c. Document changes to the location (i.e., system or system components) where the
information is processed and stored.
Discussion:  Information location addresses the need to understand where information is being
processed and stored. Information location includes identifying where specific information types
and information reside in system components and how information is being processed so that
information flow can be understood and adequate protection and policy management provided
for such information and system components. The security category of the information is also a
factor in determining the controls necessary to protect the information and the system
component where the information resides (see FIPS 199). The location of the information and
system components is also a factor in the architecture and design of the system (see SA-4, SA-8,
SA-17).
Related Controls:  AC-2, AC-3, AC-4, AC-6, AC-23, CM-8, PM-5, RA-2, SA-4, SA-8, SA-17, SC-4, SC-
16, SC-28, SI-4, SI-7.
Control Enhancements:
(1) INFORMATION LOCATION | AUTOMATED TOOLS TO SUPPORT INFORMATION LOCATION
Use automated tools to identify [Assignment: organization-defined information by
information type] on [Assignment: organization-defined system components] to ensure
controls are in place to protect organizational information and individual privacy.
Discussion:  The use of automated tools helps to increase the effectiveness and efficiency of
the information location capability implemented within the system. Automation also helps
organizations manage the data produced during information location activities and share
such information across the organization. The output of automated information location
tools can be used to guide and inform system architecture and design decisions.
Related Controls:  None.
References:  [FIPS 199], [SP 800-60-1], [SP 800-60-2].
