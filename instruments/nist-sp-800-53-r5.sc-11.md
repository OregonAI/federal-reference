---
schema_version: 1
corpus: federal-reference
jurisdiction: us
id: nist-sp-800-53-r5.sc-11
title: NIST SP 800-53 Rev. 5 SC-11 — TRUSTED PATH
doc_type: federal_instrument
citation: NIST SP 800-53 Rev. 5 SC-11
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

**NIST SP 800-53 Rev. 5 SC-11** — TRUSTED PATH

- Issued by: National Institute of Standards and Technology
- Publication: NIST SP 800-53 Rev. 5 — Security and Privacy Controls for Information Systems and Organizations ([nist-sp-800-53-r5](./nist-sp-800-53-r5.md))
- Version: Rev. 5 (September 2020, includes updates as of 2020-12-10)
- Text as of: 2026-11-12
- Cited by held documents: 3 times (arc-ampe ×3)
- Reproduction basis: 17 U.S.C. § 105 — work of the U.S. government (NIST). Determined per document on 2026-11-12 against the publication itself, not assumed from its issuer: its Authority statement (PDF page 3) reads "This publication may be used by nongovernmental organizations on a voluntary basis and is not subject to copyright in the United States. Attribution would, however, be appreciated by NIST." Held here: the front matter and Chapter Three (the control catalog) only. Chapter Three names ISO/IEC standards solely as bibliographic references and reproduces none of their text. NOT mirrored: the References bibliography and Appendices A-C; Appendix A (glossary) adapts third-party definitions (ISO/IEC 15026, ISO 25237, ISO/IEC 29100, ISO 15288, IETF RFC 4949), which ADR-0002 treats as not reproducible by being incorporated, and whose reproducibility has not been determined.


_NON-AUTHORITATIVE copy of one control, cut from the SP 800-53 Rev. 5 snapshot this corpus holds. Whether and how this binds a given agency depends on the instrument that incorporates it — read it at the source URL before relying on it. This copy is the Rev. 5 text of record, which is not necessarily the text a citing document meant (a document citing Rev. 4 is not answered by it)._


## Full text

### SC-11 TRUSTED PATH
Control:
a. Provide a [Selection: physically; logically] isolated trusted communications path for
communications between the user and the trusted components of the system; and
CHAPTER THREE   PAGE 307
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
b. Permit users to invoke the trusted communications path for communications between the
user and the following security functions of the system, including at a minimum,
authentication and re-authentication: [Assignment: organization-defined security functions].
Discussion:  Trusted paths are mechanisms by which users can communicate (using input devices
such as keyboards) directly with the security functions of systems with the requisite assurance to
support security policies. Trusted path mechanisms can only be activated by users or the security
functions of organizational systems. User responses that occur via trusted paths are protected
from modification by and disclosure to untrusted applications. Organizations employ trusted
paths for trustworthy, high-assurance connections between security functions of systems and
users, including during system logons. The original implementations of trusted paths employed
an out-of-band signal to initiate the path, such as using the <BREAK> key, which does not
transmit characters that can be spoofed. In later implementations, a key combination that could
not be hijacked was used (e.g., the <CTRL> + <ALT> + <DEL> keys). Such key combinations,
however, are platform-specific and may not provide a trusted path implementation in every case.
The enforcement of trusted communications paths is provided by a specific implementation that
meets the reference monitor concept.
Related Controls:  AC-16, AC-25, SC-12, SC-23.
Control Enhancements:
(1) TRUSTED PATH | IRREFUTABLE COMMUNICATIONS PATH
(a) Provide a trusted communications path that is irrefutably distinguishable from other
communications paths; and
(b) Initiate the trusted communications path for communications between the
[Assignment: organization-defined security functions] of the system and the user.
Discussion:  An irrefutable communications path permits the system to initiate a trusted path,
which necessitates that the user can unmistakably recognize the source of the communication as
a trusted system component. For example, the trusted path may appear in an area of the display
that other applications cannot access or be based on the presence of an identifier that cannot be
spoofed.
Related Controls:  None.
References:  [OMB A-130].
