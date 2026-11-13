---
schema_version: 1
corpus: federal-reference
jurisdiction: us
id: nist-sp-800-53-r5.cp-6
title: NIST SP 800-53 Rev. 5 CP-6 — ALTERNATE STORAGE SITE
doc_type: federal_instrument
citation: NIST SP 800-53 Rev. 5 CP-6
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

**NIST SP 800-53 Rev. 5 CP-6** — ALTERNATE STORAGE SITE

- Issued by: National Institute of Standards and Technology
- Publication: NIST SP 800-53 Rev. 5 — Security and Privacy Controls for Information Systems and Organizations ([nist-sp-800-53-r5](./nist-sp-800-53-r5.md))
- Version: Rev. 5 (September 2020, includes updates as of 2020-12-10)
- Text as of: 2026-11-12
- Cited by held documents: 15 times (cjis-sp-6-1 ×12, 6-cfr-37 ×2, arc-ampe ×1)
- Reproduction basis: 17 U.S.C. § 105 — work of the U.S. government (NIST). Determined per document on 2026-11-12 against the publication itself, not assumed from its issuer: its Authority statement (PDF page 3) reads "This publication may be used by nongovernmental organizations on a voluntary basis and is not subject to copyright in the United States. Attribution would, however, be appreciated by NIST." Held here: the front matter and Chapter Three (the control catalog) only. Chapter Three names ISO/IEC standards solely as bibliographic references and reproduces none of their text. NOT mirrored: the References bibliography and Appendices A-C; Appendix A (glossary) adapts third-party definitions (ISO/IEC 15026, ISO 25237, ISO/IEC 29100, ISO 15288, IETF RFC 4949), which ADR-0002 treats as not reproducible by being incorporated, and whose reproducibility has not been determined.


_NON-AUTHORITATIVE copy of one control, cut from the SP 800-53 Rev. 5 snapshot this corpus holds. Whether and how this binds a given agency depends on the instrument that incorporates it — read it at the source URL before relying on it. This copy is the Rev. 5 text of record, which is not necessarily the text a citing document meant (a document citing Rev. 4 is not answered by it)._


## Full text

### CP-6 ALTERNATE STORAGE SITE
Control:
a. Establish an alternate storage site, including necessary agreements to permit the storage
and retrieval of system backup information; and
b. Ensure that the alternate storage site provides controls equivalent to that of the primary
site.
Discussion:  Alternate storage sites are geographically distinct from primary storage sites and
maintain duplicate copies of information and data if the primary storage site is not available.
Similarly, alternate processing sites provide processing capability if the primary processing site is
not available. Geographically distributed architectures that support contingency requirements
may be considered alternate storage sites. Items covered by alternate storage site agreements
include environmental conditions at the alternate sites, access rules for systems and facilities,
physical and environmental protection requirements, and coordination of delivery and retrieval
of backup media. Alternate storage sites reflect the requirements in contingency plans so that
organizations can maintain essential mission and business functions despite compromise, failure,
or disruption in organizational systems.
Related Controls:  CP-2, CP-7, CP-8, CP-9, CP-10, MP-4, MP-5, PE-3, SC-36, SI-13.
Control Enhancements:
(1) ALTERNATE STORAGE SITE | SEPARATION FROM PRIMARY SITE
Identify an alternate storage site that is sufficiently separated from the primary storage
site to reduce susceptibility to the same threats.
Discussion:  Threats that affect alternate storage sites are defined in organizational risk
assessments and include natural disasters, structural failures, hostile attacks, and errors of
CHAPTER THREE   PAGE 122
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
omission or commission. Organizations determine what is considered a sufficient degree of
separation between primary and alternate storage sites based on the types of threats that
are of concern. For threats such as hostile attacks, the degree of separation between sites is
less relevant.
Related Controls:  RA-3.
(2) ALTERNATE STORAGE SITE | RECOVERY TIME AND RECOVERY POINT OBJECTIVES
Configure the alternate storage site to facilitate recovery operations in accordance with
recovery time and recovery point objectives.
Discussion:  Organizations establish recovery time and recovery point objectives as part of
contingency planning. Configuration of the alternate storage site includes physical facilities
and the systems supporting recovery operations that ensure accessibility and correct
execution.
Related Controls:  None.
(3) ALTERNATE STORAGE SITE | ACCESSIBILITY
Identify potential accessibility problems to the alternate storage site in the event of an
area-wide disruption or disaster and outline explicit mitigation actions.
Discussion:  Area-wide disruptions refer to those types of disruptions that are broad in
geographic scope with such determinations made by organizations based on organizational
assessments of risk. Explicit mitigation actions include duplicating backup information at
other alternate storage sites if access problems occur at originally designated alternate sites
or planning for physical access to retrieve backup information if electronic accessibility to
the alternate site is disrupted.
Related Controls:  RA-3.
References:  [SP 800-34].
