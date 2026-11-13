---
schema_version: 1
corpus: federal-reference
jurisdiction: us
id: nist-sp-800-53-r5.ra-2
title: NIST SP 800-53 Rev. 5 RA-2 — SECURITY CATEGORIZATION
doc_type: federal_instrument
citation: NIST SP 800-53 Rev. 5 RA-2
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

**NIST SP 800-53 Rev. 5 RA-2** — SECURITY CATEGORIZATION

- Issued by: National Institute of Standards and Technology
- Publication: NIST SP 800-53 Rev. 5 — Security and Privacy Controls for Information Systems and Organizations ([nist-sp-800-53-r5](./nist-sp-800-53-r5.md))
- Version: Rev. 5 (September 2020, includes updates as of 2020-12-10)
- Text as of: 2026-11-12
- Cited by held documents: 21 times (cjis-sp-6-1 ×16, arc-ampe ×3, 6-cfr-37 ×2)
- Reproduction basis: 17 U.S.C. § 105 — work of the U.S. government (NIST). Determined per document on 2026-11-12 against the publication itself, not assumed from its issuer: its Authority statement (PDF page 3) reads "This publication may be used by nongovernmental organizations on a voluntary basis and is not subject to copyright in the United States. Attribution would, however, be appreciated by NIST." Held here: the front matter and Chapter Three (the control catalog) only. Chapter Three names ISO/IEC standards solely as bibliographic references and reproduces none of their text. NOT mirrored: the References bibliography and Appendices A-C; Appendix A (glossary) adapts third-party definitions (ISO/IEC 15026, ISO 25237, ISO/IEC 29100, ISO 15288, IETF RFC 4949), which ADR-0002 treats as not reproducible by being incorporated, and whose reproducibility has not been determined.


_NON-AUTHORITATIVE copy of one control, cut from the SP 800-53 Rev. 5 snapshot this corpus holds. Whether and how this binds a given agency depends on the instrument that incorporates it — read it at the source URL before relying on it. This copy is the Rev. 5 text of record, which is not necessarily the text a citing document meant (a document citing Rev. 4 is not answered by it)._


## Full text

### RA-2 SECURITY CATEGORIZATION
Control:
a. Categorize the system and information it processes, stores, and transmits;
b. Document the security categorization results, including supporting rationale, in the security
plan for the system; and
c. Verify that the authorizing official or authorizing official designated representative reviews
and approves the security categorization decision.
Discussion:  Security categories describe the potential adverse impacts or negative consequences
to organizational operations, organizational assets, and individuals if organizational information
and systems are compromised through a loss of confidentiality, integrity, or availability. Security
categorization is also a type of asset loss characterization in systems security engineering
processes that is carried out throughout the system development life cycle. Organizations can
use privacy risk assessments or privacy impact assessments to better understand the potential
adverse effects on individuals. [
CNSSI 1253] provides additional guidance on categorization for
national security systems.
Organizations conduct the security categorization process as an organization-wide activity with
the direct involvement of chief information officers, senior agency information security officers,
senior agency officials for privacy, system owners, mission and business owners, and information
owners or stewards. Organizations consider the potential adverse impacts to other organizations
and, in accordance with [USA PATRIOT] and Homeland Security Presidential Directives, potential
national-level adverse impacts.
Security categorization processes facilitate the development of inventories of information assets
and, along with CM-8, mappings to specific system components where information is processed,
stored, or transmitted. The security categorization process is revisited throughout the system
development life cycle to ensure that the security categories remain accurate and relevant.
Related Controls:  CM-8, MP-4, PL-2, PL-10, PL-11, PM-7, RA-3, RA-5, RA-7, RA-8, SA-8, SC-7, SC-
38, SI-12.
Control Enhancements:
(1) SECURITY CATEGORIZATION | IMPACT-LEVEL PRIORITIZATION
Conduct an impact-level prioritization of organizational systems to obtain additional
granularity on system impact levels.
Discussion:  Organizations apply the “high-water mark” concept to each system categorized
in accordance with [FIPS 199], resulting in systems designated as low impact, moderate
impact, or high impact. Organizations that desire additional granularity in the system impact
designations for risk-based decision-making, can further partition the systems into sub-
categories of the initial system categorization. For example, an impact-level prioritization on
a moderate-impact system can produce three new sub-categories: low-moderate systems,
moderate-moderate systems, and high-moderate systems. Impact-level prioritization and
the resulting sub-categories of the system give organizations an opportunity to focus their
investments related to security control selection and the tailoring of control baselines in
responding to identified risks. Impact-level prioritization can also be used to determine
those systems that may be of heightened interest or value to adversaries or represent a
critical loss to the federal enterprise, sometimes described as high value assets. For such
high value assets, organizations may be more focused on complexity, aggregation, and
information exchanges. Systems with high value assets can be prioritized by partitioning
high-impact systems into low-high systems, moderate-high systems, and high-high systems.
CHAPTER THREE   PAGE 240
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
Alternatively, organizations can apply the guidance in [CNSSI 1253] for security objective-
related categorization.
Related Controls:  None.
References:  [FIPS 199], [FIPS 200], [SP 800-30], [SP 800-37], [SP 800-39], [SP 800-60-1], [SP 800-
60-2], [SP 800-160-1], [CNSSI 1253], [NARA CUI].
