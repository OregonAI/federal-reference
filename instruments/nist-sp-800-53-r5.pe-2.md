---
schema_version: 1
corpus: federal-reference
jurisdiction: us
id: nist-sp-800-53-r5.pe-2
title: NIST SP 800-53 Rev. 5 PE-2 — PHYSICAL ACCESS AUTHORIZATIONS
doc_type: federal_instrument
citation: NIST SP 800-53 Rev. 5 PE-2
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

**NIST SP 800-53 Rev. 5 PE-2** — PHYSICAL ACCESS AUTHORIZATIONS

- Issued by: National Institute of Standards and Technology
- Publication: NIST SP 800-53 Rev. 5 — Security and Privacy Controls for Information Systems and Organizations ([nist-sp-800-53-r5](./nist-sp-800-53-r5.md))
- Version: Rev. 5 (September 2020, includes updates as of 2020-12-10)
- Text as of: 2026-11-12
- Cited by held documents: 32 times (cjis-sp-6-1 ×23, irs-pub-1075-11-2021 ×4, arc-ampe ×3, 6-cfr-37 ×2)
- Reproduction basis: 17 U.S.C. § 105 — work of the U.S. government (NIST). Determined per document on 2026-11-12 against the publication itself, not assumed from its issuer: its Authority statement (PDF page 3) reads "This publication may be used by nongovernmental organizations on a voluntary basis and is not subject to copyright in the United States. Attribution would, however, be appreciated by NIST." Held here: the front matter and Chapter Three (the control catalog) only. Chapter Three names ISO/IEC standards solely as bibliographic references and reproduces none of their text. NOT mirrored: the References bibliography and Appendices A-C; Appendix A (glossary) adapts third-party definitions (ISO/IEC 15026, ISO 25237, ISO/IEC 29100, ISO 15288, IETF RFC 4949), which ADR-0002 treats as not reproducible by being incorporated, and whose reproducibility has not been determined.


_NON-AUTHORITATIVE copy of one control, cut from the SP 800-53 Rev. 5 snapshot this corpus holds. Whether and how this binds a given agency depends on the instrument that incorporates it — read it at the source URL before relying on it. This copy is the Rev. 5 text of record, which is not necessarily the text a citing document meant (a document citing Rev. 4 is not answered by it)._


## Full text

### PE-2 PHYSICAL ACCESS AUTHORIZATIONS
Control:
a. Develop, approve, and maintain a list of individuals with authorized access to the facility
where the system resides;
b. Issue authorization credentials for facility access;
c. Review the access list detailing authorized facility access by individuals [Assignment:
organization-defined frequency]; and
d. Remove individuals from the facility access list when access is no longer required.
Discussion:  Physical access authorizations apply to employees and visitors. Individuals with
permanent physical access authorization credentials are not considered visitors. Authorization
credentials include ID badges, identification cards, and smart cards. Organizations determine the
strength of authorization credentials needed consistent with applicable laws, executive orders,
directives, regulations, policies, standards, and guidelines. Physical access authorizations may not
be necessary to access certain areas within facilities that are designated as publicly accessible.
Related Controls:  AT-3, AU-9, IA-4, MA-5, MP-2, PE-3, PE-4, PE-5, PE-8, PM-12, PS-3, PS-4, PS-5,
PS-6.
Control Enhancements:
(1) PHYSICAL ACCESS AUTHORIZATIONS | ACCESS BY POSITION OR ROLE
Authorize physical access to the facility where the system resides based on position or
role.
Discussion:  Role-based facility access includes access by authorized permanent and
regular/routine maintenance personnel, duty officers, and emergency medical staff.
Related Controls:  AC-2, AC-3, AC-6.
(2) PHYSICAL ACCESS AUTHORIZATIONS | TWO FORMS OF IDENTIFICATION
Require two forms of identification from the following forms of identification for visitor
access to the facility where the system resides: [Assignment: organization-defined list of
acceptable forms of identification].
Discussion:  Acceptable forms of identification include passports, REAL ID-compliant drivers’
licenses, and Personal Identity Verification (PIV) cards. For gaining access to facilities using
automated mechanisms, organizations may use PIV cards, key cards, PINs, and biometrics.
Related Controls:  IA-2, IA-4, IA-5.
(3) PHYSICAL ACCESS AUTHORIZATIONS | RESTRICT UNESCORTED ACCESS
Restrict unescorted access to the facility where the system resides to personnel with
[Selection (one or more): security clearances for all information contained within the
system; formal access authorizations for all information contained within the system; need
for access to all information contained within the system; [Assignment: organization-
defined physical access authorizations]].
Discussion:  Individuals without required security clearances, access approvals, or need to
know are escorted by individuals with appropriate physical access authorizations to ensure
that information is not exposed or otherwise compromised.
Related Controls:  PS-2, PS-6.
References:  [FIPS 201-2], [SP 800-73-4], [SP 800-76-2], [SP 800-78-4].
CHAPTER THREE   PAGE 181
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
