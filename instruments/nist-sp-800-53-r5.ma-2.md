---
schema_version: 1
corpus: federal-reference
jurisdiction: us
id: nist-sp-800-53-r5.ma-2
title: NIST SP 800-53 Rev. 5 MA-2 — CONTROLLED MAINTENANCE
doc_type: federal_instrument
citation: NIST SP 800-53 Rev. 5 MA-2
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

**NIST SP 800-53 Rev. 5 MA-2** — CONTROLLED MAINTENANCE

- Issued by: National Institute of Standards and Technology
- Publication: NIST SP 800-53 Rev. 5 — Security and Privacy Controls for Information Systems and Organizations ([nist-sp-800-53-r5](./nist-sp-800-53-r5.md))
- Version: Rev. 5 (September 2020, includes updates as of 2020-12-10)
- Text as of: 2026-11-12
- Cited by held documents: 22 times (cjis-sp-6-1 ×17, irs-pub-1075-11-2021 ×3, 6-cfr-37 ×1, arc-ampe ×1)
- Reproduction basis: 17 U.S.C. § 105 — work of the U.S. government (NIST). Determined per document on 2026-11-12 against the publication itself, not assumed from its issuer: its Authority statement (PDF page 3) reads "This publication may be used by nongovernmental organizations on a voluntary basis and is not subject to copyright in the United States. Attribution would, however, be appreciated by NIST." Held here: the front matter and Chapter Three (the control catalog) only. Chapter Three names ISO/IEC standards solely as bibliographic references and reproduces none of their text. NOT mirrored: the References bibliography and Appendices A-C; Appendix A (glossary) adapts third-party definitions (ISO/IEC 15026, ISO 25237, ISO/IEC 29100, ISO 15288, IETF RFC 4949), which ADR-0002 treats as not reproducible by being incorporated, and whose reproducibility has not been determined.


_NON-AUTHORITATIVE copy of one control, cut from the SP 800-53 Rev. 5 snapshot this corpus holds. Whether and how this binds a given agency depends on the instrument that incorporates it — read it at the source URL before relying on it. This copy is the Rev. 5 text of record, which is not necessarily the text a citing document meant (a document citing Rev. 4 is not answered by it)._


## Full text

### MA-2 CONTROLLED MAINTENANCE
Control:
a. Schedule, document, and review records of maintenance, repair, and replacement on
system components in accordance with manufacturer or vendor specifications and/or
organizational requirements;
b. Approve and monitor all maintenance activities, whether performed on site or remotely and
whether the system or system components are serviced on site or removed to another
location;
c. Require that [Assignment: organization-defined personnel or roles] explicitly approve the
removal of the system or system components from organizational facilities for off-site
maintenance, repair, or replacement;
d. Sanitize equipment to remove the following information from associated media prior to
removal from organizational facilities for off-site maintenance, repair, or replacement:
[Assignment: organization-defined information];
e. Check all potentially impacted controls to verify that the controls are still functioning
properly following maintenance, repair, or replacement actions; and
f. Include the following information in organizational maintenance records: [Assignment:
organization-defined information].
Discussion:  Controlling system maintenance addresses the information security aspects of the
system maintenance program and applies to all types of maintenance to system components
conducted by local or nonlocal entities. Maintenance includes peripherals such as scanners,
copiers, and printers. Information necessary for creating effective maintenance records includes
the date and time of maintenance, a description of the maintenance performed, names of the
individuals or group performing the maintenance, name of the escort, and system components
or equipment that are removed or replaced. Organizations consider supply chain-related risks
associated with replacement components for systems.
Related Controls:  CM-2,  CM-3, CM-4, CM-5, CM-8, MA-4, MP-6, PE-16, SI-2, SR-3, SR-4, SR-11.
Control Enhancements:
(1) CONTROLLED MAINTENANCE | RECORD CONTENT
[Withdrawn: Incorporated into MA-2.]
(2) CONTROLLED MAINTENANCE | AUTOMATED MAINTENANCE ACTIVITIES
(a) Schedule, conduct, and document maintenance, repair, and replacement actions for
the system using [Assignment: organization-defined automated mechanisms]; and
(b) Produce up-to date, accurate, and complete records of all maintenance, repair, and
replacement actions requested, scheduled, in process, and completed.
Discussion:  The use of automated mechanisms to manage and control system maintenance
programs and activities helps to ensure the generation of timely, accurate, complete, and
consistent maintenance records.
Related Controls:  MA-3.
References:  [OMB A-130], [IR 8023].
