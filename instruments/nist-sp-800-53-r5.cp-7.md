---
schema_version: 1
corpus: federal-reference
jurisdiction: us
id: nist-sp-800-53-r5.cp-7
title: NIST SP 800-53 Rev. 5 CP-7 — ALTERNATE PROCESSING SITE
doc_type: federal_instrument
citation: NIST SP 800-53 Rev. 5 CP-7
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

**NIST SP 800-53 Rev. 5 CP-7** — ALTERNATE PROCESSING SITE

- Issued by: National Institute of Standards and Technology
- Publication: NIST SP 800-53 Rev. 5 — Security and Privacy Controls for Information Systems and Organizations ([nist-sp-800-53-r5](./nist-sp-800-53-r5.md))
- Version: Rev. 5 (September 2020, includes updates as of 2020-12-10)
- Text as of: 2026-11-12
- Cited by held documents: 19 times (cjis-sp-6-1 ×15, 6-cfr-37 ×2, arc-ampe ×2)
- Reproduction basis: 17 U.S.C. § 105 — work of the U.S. government (NIST). Determined per document on 2026-11-12 against the publication itself, not assumed from its issuer: its Authority statement (PDF page 3) reads "This publication may be used by nongovernmental organizations on a voluntary basis and is not subject to copyright in the United States. Attribution would, however, be appreciated by NIST." Held here: the front matter and Chapter Three (the control catalog) only. Chapter Three names ISO/IEC standards solely as bibliographic references and reproduces none of their text. NOT mirrored: the References bibliography and Appendices A-C; Appendix A (glossary) adapts third-party definitions (ISO/IEC 15026, ISO 25237, ISO/IEC 29100, ISO 15288, IETF RFC 4949), which ADR-0002 treats as not reproducible by being incorporated, and whose reproducibility has not been determined.


_NON-AUTHORITATIVE copy of one control, cut from the SP 800-53 Rev. 5 snapshot this corpus holds. Whether and how this binds a given agency depends on the instrument that incorporates it — read it at the source URL before relying on it. This copy is the Rev. 5 text of record, which is not necessarily the text a citing document meant (a document citing Rev. 4 is not answered by it)._


## Full text

### CP-7 ALTERNATE PROCESSING SITE
Control:
a. Establish an alternate processing site, including necessary agreements to permit the transfer
and resumption of [Assignment: organization-defined system operations] for essential
mission and business functions within [Assignment: organization-defined time period
consistent with recovery time and recovery point objectives] when the primary processing
capabilities are unavailable;
b. Make available at the alternate processing site, the equipment and supplies required to
transfer and resume operations or put contracts in place to support delivery to the site
within the organization-defined time period for transfer and resumption; and
c. Provide controls at the alternate processing site that are equivalent to those at the primary
site.
Discussion:  Alternate processing sites are geographically distinct from primary processing sites
and provide processing capability if the primary processing site is not available. The alternate
processing capability may be addressed using a physical processing site or other alternatives,
such as failover to a cloud-based service provider or other internally or externally provided
processing service. Geographically distributed architectures that support contingency
requirements may also be considered alternate processing sites. Controls that are covered by
alternate processing site agreements include the environmental conditions at alternate sites,
access rules, physical and environmental protection requirements, and the coordination for the
transfer and assignment of personnel. Requirements are allocated to alternate processing sites
CHAPTER THREE   PAGE 123
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
that reflect the requirements in contingency plans to maintain essential mission and business
functions despite disruption, compromise, or failure in organizational systems.
Related Controls:  CP-2, CP-6, CP-8, CP-9, CP-10, MA-6, PE-3, PE-11, PE-12, PE-17, SC-36, SI-13.
Control Enhancements:
(1) ALTERNATE PROCESSING SITE | SEPARATION FROM PRIMARY SITE
Identify an alternate processing site that is sufficiently separated from the primary
processing site to reduce susceptibility to the same threats.
Discussion:  Threats that affect alternate processing sites are defined in organizational
assessments of risk and include natural disasters, structural failures, hostile attacks, and
errors of omission or commission. Organizations determine what is considered a sufficient
degree of separation between primary and alternate processing sites based on the types of
threats that are of concern. For threats such as hostile attacks, the degree of separation
between sites is less relevant.
Related Controls:  RA-3.
(2) ALTERNATE PROCESSING SITE | ACCESSIBILITY
Identify potential accessibility problems to alternate processing sites in the event of an
area-wide disruption or disaster and outlines explicit mitigation actions.
Discussion:  Area-wide disruptions refer to those types of disruptions that are broad in
geographic scope with such determinations made by organizations based on organizational
assessments of risk.
Related Controls:  RA-3.
(3) ALTERNATE PROCESSING SITE | PRIORITY OF SERVICE
Develop alternate processing site agreements that contain priority-of-service provisions in
accordance with availability requirements (including recovery time objectives).
Discussion:  Priority of service agreements refer to negotiated agreements with service
providers that ensure that organizations receive priority treatment consistent with their
availability requirements and the availability of information resources for logical alternate
processing and/or at the physical alternate processing site. Organizations establish recovery
time objectives as part of contingency planning.
Related Controls:  None.
(4) ALTERNATE PROCESSING SITE | PREPARATION FOR USE
Prepare the alternate processing site so that the site can serve as the operational site
supporting essential mission and business functions.
Discussion:  Site preparation includes establishing configuration settings for systems at the
alternate processing site consistent with the requirements for such settings at the primary
site and ensuring that essential supplies and logistical considerations are in place.
Related Controls:  CM-2, CM-6, CP-4.
(5) ALTERNATE PROCESSING SITE | EQUIVALENT INFORMATION SECURITY SAFEGUARDS
[Withdrawn: Incorporated into CP-7.]
(6) ALTERNATE PROCESSING SITE | INABILITY TO RETURN TO PRIMARY SITE
Plan and prepare for circumstances that preclude returning to the primary processing site.
Discussion:  There may be situations that preclude an organization from returning to the
primary processing site such as if a natural disaster (e.g., flood or a hurricane) damaged or
CHAPTER THREE   PAGE 124
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
destroyed a facility and it was determined that rebuilding in the same location was not
prudent.
Related Controls:  None.
References:  [SP 800-34].
