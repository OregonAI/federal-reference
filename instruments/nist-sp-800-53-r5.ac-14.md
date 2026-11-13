---
schema_version: 1
corpus: federal-reference
jurisdiction: us
id: nist-sp-800-53-r5.ac-14
title: NIST SP 800-53 Rev. 5 AC-14 — PERMITTED ACTIONS WITHOUT IDENTIFICATION OR AUTHENTICATION
doc_type: federal_instrument
citation: NIST SP 800-53 Rev. 5 AC-14
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

**NIST SP 800-53 Rev. 5 AC-14** — PERMITTED ACTIONS WITHOUT IDENTIFICATION OR AUTHENTICATION

- Issued by: National Institute of Standards and Technology
- Publication: NIST SP 800-53 Rev. 5 — Security and Privacy Controls for Information Systems and Organizations ([nist-sp-800-53-r5](./nist-sp-800-53-r5.md))
- Version: Rev. 5 (September 2020, includes updates as of 2020-12-10)
- Text as of: 2026-11-12
- Cited by held documents: 16 times (cjis-sp-6-1 ×8, arc-ampe ×4, irs-pub-1075-11-2021 ×3, 6-cfr-37 ×1)
- Reproduction basis: 17 U.S.C. § 105 — work of the U.S. government (NIST). Determined per document on 2026-11-12 against the publication itself, not assumed from its issuer: its Authority statement (PDF page 3) reads "This publication may be used by nongovernmental organizations on a voluntary basis and is not subject to copyright in the United States. Attribution would, however, be appreciated by NIST." Held here: the front matter and Chapter Three (the control catalog) only. Chapter Three names ISO/IEC standards solely as bibliographic references and reproduces none of their text. NOT mirrored: the References bibliography and Appendices A-C; Appendix A (glossary) adapts third-party definitions (ISO/IEC 15026, ISO 25237, ISO/IEC 29100, ISO 15288, IETF RFC 4949), which ADR-0002 treats as not reproducible by being incorporated, and whose reproducibility has not been determined.


_NON-AUTHORITATIVE copy of one control, cut from the SP 800-53 Rev. 5 snapshot this corpus holds. Whether and how this binds a given agency depends on the instrument that incorporates it — read it at the source URL before relying on it. This copy is the Rev. 5 text of record, which is not necessarily the text a citing document meant (a document citing Rev. 4 is not answered by it)._


## Full text

### AC-14 PERMITTED ACTIONS WITHOUT IDENTIFICATION OR AUTHENTICATION
Control:
a. Identify [Assignment: organization-defined user actions] that can be performed on the
system without identification or authentication consistent with organizational mission and
business functions; and
b. Document and provide supporting rationale in the security plan for the system, user actions
not requiring identification or authentication.
Discussion:  Specific user actions may be permitted without identification or authentication if
organizations determine that identification and authentication are not required for the specified
user actions. Organizations may allow a limited number of user actions without identification or
authentication, including when individuals access public websites or other publicly accessible
federal systems, when individuals use mobile phones to receive calls, or when facsimiles are
received. Organizations identify actions that normally require identification or authentication but
may, under certain circumstances, allow identification or authentication mechanisms to be
bypassed. Such bypasses may occur, for example, via a software-readable physical switch that
commands bypass of the logon functionality and is protected from accidental or unmonitored
use. Permitting actions without identification or authentication does not apply to situations
where identification and authentication have already occurred and are not repeated but rather
to situations where identification and authentication have not yet occurred. Organizations may
decide that there are no user actions that can be performed on organizational systems without
identification and authentication, and therefore, the value for the assignment operation can be
“none.”
Related Controls:  AC-8, IA-2, PL-2.
Control Enhancements:  None.
(1) PERMITTED ACTIONS WITHOUT IDENTIFICATION OR AUTHENTICATION | NECESSARY USES
[Withdrawn: Incorporated into AC-14.]
References:  None.
