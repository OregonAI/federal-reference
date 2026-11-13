---
schema_version: 1
corpus: federal-reference
jurisdiction: us
id: nist-sp-800-53-r5.ir-7
title: NIST SP 800-53 Rev. 5 IR-7 — INCIDENT RESPONSE ASSISTANCE
doc_type: federal_instrument
citation: NIST SP 800-53 Rev. 5 IR-7
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

**NIST SP 800-53 Rev. 5 IR-7** — INCIDENT RESPONSE ASSISTANCE

- Issued by: National Institute of Standards and Technology
- Publication: NIST SP 800-53 Rev. 5 — Security and Privacy Controls for Information Systems and Organizations ([nist-sp-800-53-r5](./nist-sp-800-53-r5.md))
- Version: Rev. 5 (September 2020, includes updates as of 2020-12-10)
- Text as of: 2026-11-12
- Cited by held documents: 15 times (cjis-sp-6-1 ×9, irs-pub-1075-11-2021 ×3, 6-cfr-37 ×2, arc-ampe ×1)
- Reproduction basis: 17 U.S.C. § 105 — work of the U.S. government (NIST). Determined per document on 2026-11-12 against the publication itself, not assumed from its issuer: its Authority statement (PDF page 3) reads "This publication may be used by nongovernmental organizations on a voluntary basis and is not subject to copyright in the United States. Attribution would, however, be appreciated by NIST." Held here: the front matter and Chapter Three (the control catalog) only. Chapter Three names ISO/IEC standards solely as bibliographic references and reproduces none of their text. NOT mirrored: the References bibliography and Appendices A-C; Appendix A (glossary) adapts third-party definitions (ISO/IEC 15026, ISO 25237, ISO/IEC 29100, ISO 15288, IETF RFC 4949), which ADR-0002 treats as not reproducible by being incorporated, and whose reproducibility has not been determined.


_NON-AUTHORITATIVE copy of one control, cut from the SP 800-53 Rev. 5 snapshot this corpus holds. Whether and how this binds a given agency depends on the instrument that incorporates it — read it at the source URL before relying on it. This copy is the Rev. 5 text of record, which is not necessarily the text a citing document meant (a document citing Rev. 4 is not answered by it)._


## Full text

### IR-7 INCIDENT RESPONSE ASSISTANCE
Control:  Provide an incident response support resource, integral to the organizational incident
response capability, that offers advice and assistance to users of the system for the handling and
reporting of incidents.
Discussion:  Incident response support resources provided by organizations include help desks,
assistance groups, automated ticketing systems to open and track incident response tickets, and
access to forensics services or consumer redress services, when required.
Related Controls:  AT-2, AT-3, IR-4, IR-6, IR-8, PM-22, PM-26, SA-9, SI-18.
Control Enhancements:
(1) INCIDENT RESPONSE ASSISTANCE | AUTOMATION SUPPORT FOR AVAILABILITY OF INFORMATION AND
SUPPORT
Increase the availability of incident response information and support using [Assignment:
organization-defined automated mechanisms].
Discussion:  Automated mechanisms can provide a push or pull capability for users to obtain
incident response assistance. For example, individuals may have access to a website to query
the assistance capability, or the assistance capability can proactively send incident response
information to users (general distribution or targeted) as part of increasing understanding of
current response capabilities and support.
Related Controls:  None.
(2) INCIDENT RESPONSE ASSISTANCE | COORDINATION WITH EXTERNAL PROVIDERS
(a) Establish a direct, cooperative relationship between its incident response capability
and external providers of system protection capability; and
(b) Identify organizational incident response team members to the external providers.
Discussion:  External providers of a system protection capability include the Computer
Network Defense program within the U.S. Department of Defense. External providers help to
protect, monitor, analyze, detect, and respond to unauthorized activity within organizational
information systems and networks. It may be beneficial to have agreements in place with
external providers to clarify the roles and responsibilities of each party before an incident
occurs.
Related Controls:  None.
References:  [OMB A-130], [IR 7559].
