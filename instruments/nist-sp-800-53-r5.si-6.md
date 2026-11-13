---
schema_version: 1
corpus: federal-reference
jurisdiction: us
id: nist-sp-800-53-r5.si-6
title: NIST SP 800-53 Rev. 5 SI-6 — SECURITY AND PRIVACY FUNCTION VERIFICATION
doc_type: federal_instrument
citation: NIST SP 800-53 Rev. 5 SI-6
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

**NIST SP 800-53 Rev. 5 SI-6** — SECURITY AND PRIVACY FUNCTION VERIFICATION

- Issued by: National Institute of Standards and Technology
- Publication: NIST SP 800-53 Rev. 5 — Security and Privacy Controls for Information Systems and Organizations ([nist-sp-800-53-r5](./nist-sp-800-53-r5.md))
- Version: Rev. 5 (September 2020, includes updates as of 2020-12-10)
- Text as of: 2026-11-12
- Cited by held documents: 1 time (6-cfr-37 ×1)
- Reproduction basis: 17 U.S.C. § 105 — work of the U.S. government (NIST). Determined per document on 2026-11-12 against the publication itself, not assumed from its issuer: its Authority statement (PDF page 3) reads "This publication may be used by nongovernmental organizations on a voluntary basis and is not subject to copyright in the United States. Attribution would, however, be appreciated by NIST." Held here: the front matter and Chapter Three (the control catalog) only. Chapter Three names ISO/IEC standards solely as bibliographic references and reproduces none of their text. NOT mirrored: the References bibliography and Appendices A-C; Appendix A (glossary) adapts third-party definitions (ISO/IEC 15026, ISO 25237, ISO/IEC 29100, ISO 15288, IETF RFC 4949), which ADR-0002 treats as not reproducible by being incorporated, and whose reproducibility has not been determined.


_NON-AUTHORITATIVE copy of one control, cut from the SP 800-53 Rev. 5 snapshot this corpus holds. Whether and how this binds a given agency depends on the instrument that incorporates it — read it at the source URL before relying on it. This copy is the Rev. 5 text of record, which is not necessarily the text a citing document meant (a document citing Rev. 4 is not answered by it)._


## Full text

### SI-6 SECURITY AND PRIVACY FUNCTION VERIFICATION
Control:
a. Verify the correct operation of [Assignment: organization-defined security and privacy
functions];
b. Perform the verification of the functions specified in SI-6a [Selection (one or more):
[Assignment: organization-defined system transitional states]; upon command by user with
appropriate privilege; [Assignment: organization-defined frequency]];
c. Alert [Assignment: organization-defined personnel or roles] to failed security and privacy
verification tests; and
d. [Selection (one or more): Shut the system down; Restart the system; [Assignment:
organization-defined alternative action(s)]] when anomalies are discovered.
Discussion:  Transitional states for systems include system startup, restart, shutdown, and abort.
System notifications include hardware indicator lights, electronic alerts to system administrators,
and messages to local computer consoles. In contrast to security function verification, privacy
function verification ensures that privacy functions operate as expected and are approved by the
senior agency official for privacy or that privacy attributes are applied or used as expected.
Related Controls:  CA-7, CM-4, CM-6, SI-7.
Control Enhancements:
(1) SECURITY AND PRIVACY FUNCTION VERIFICATION | NOTIFICATION OF FAILED SECURITY TESTS
[Withdrawn: Incorporated into SI-6.]
(2) SECURITY AND PRIVACY FUNCTION VERIFICATION | AUTOMATION SUPPORT FOR DISTRIBUTED
TESTING
Implement automated mechanisms to support the management of distributed security
and privacy function testing.
CHAPTER THREE   PAGE 345
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
Discussion:  The use of automated mechanisms to support the management of distributed
function testing helps to ensure the integrity, timeliness, completeness, and efficacy of such
testing.
Related Controls:  SI-2.
(3) SECURITY AND PRIVACY FUNCTION VERIFICATION | REPORT VERIFICATION RESULTS
Report the results of security and privacy function verification to [Assignment:
organization-defined personnel or roles].
Discussion:  Organizational personnel with potential interest in the results of the verification
of security and privacy functions include systems security officers, senior agency information
security officers, and senior agency officials for privacy.
Related Controls:  SI-4, SR-4, SR-5.
References:  [OMB A-130].
