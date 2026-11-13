---
schema_version: 1
corpus: federal-reference
jurisdiction: us
id: nist-sp-800-53-r5.si-2
title: NIST SP 800-53 Rev. 5 SI-2 — FLAW REMEDIATION
doc_type: federal_instrument
citation: NIST SP 800-53 Rev. 5 SI-2
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

**NIST SP 800-53 Rev. 5 SI-2** — FLAW REMEDIATION

- Issued by: National Institute of Standards and Technology
- Publication: NIST SP 800-53 Rev. 5 — Security and Privacy Controls for Information Systems and Organizations ([nist-sp-800-53-r5](./nist-sp-800-53-r5.md))
- Version: Rev. 5 (September 2020, includes updates as of 2020-12-10)
- Text as of: 2026-11-12
- Cited by held documents: 26 times (cjis-sp-6-1 ×20, irs-pub-1075-11-2021 ×4, 6-cfr-37 ×2)
- Reproduction basis: 17 U.S.C. § 105 — work of the U.S. government (NIST). Determined per document on 2026-11-12 against the publication itself, not assumed from its issuer: its Authority statement (PDF page 3) reads "This publication may be used by nongovernmental organizations on a voluntary basis and is not subject to copyright in the United States. Attribution would, however, be appreciated by NIST." Held here: the front matter and Chapter Three (the control catalog) only. Chapter Three names ISO/IEC standards solely as bibliographic references and reproduces none of their text. NOT mirrored: the References bibliography and Appendices A-C; Appendix A (glossary) adapts third-party definitions (ISO/IEC 15026, ISO 25237, ISO/IEC 29100, ISO 15288, IETF RFC 4949), which ADR-0002 treats as not reproducible by being incorporated, and whose reproducibility has not been determined.


_NON-AUTHORITATIVE copy of one control, cut from the SP 800-53 Rev. 5 snapshot this corpus holds. Whether and how this binds a given agency depends on the instrument that incorporates it — read it at the source URL before relying on it. This copy is the Rev. 5 text of record, which is not necessarily the text a citing document meant (a document citing Rev. 4 is not answered by it)._


> **Release 5.2.0 postdates this text.** NIST's listing of record ([https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final)) says that on 2025-08-27 it issued release 5.2.0 of SP 800-53, which adds a control or enhancement and updates the control discussion and updates the related controls for this control. The text below is the Rev. 5 PDF of record and does NOT include that change; read NIST's own list of the changes ([summary](https://csrc.nist.gov/files/projects/Risk-Management/800-53%20Comment%20Site/SP800-53-r5.2.0-changes.pdf)) before relying on this control's text.


## Full text

### SI-2 FLAW REMEDIATION
Control:
a. Identify, report, and correct system flaws;
b. Test software and firmware updates related to flaw remediation for effectiveness and
potential side effects before installation;
c. Install security-relevant software and firmware updates within [Assignment: organization-
defined time period] of the release of the updates; and
d. Incorporate flaw remediation into the organizational configuration management process.
Discussion:  The need to remediate system flaws applies to all types of software and firmware.
Organizations identify systems affected by software flaws, including potential vulnerabilities
resulting from those flaws, and report this information to designated organizational personnel
with information security and privacy responsibilities. Security-relevant updates include patches,
service packs, and malicious code signatures. Organizations also address flaws discovered during
assessments, continuous monitoring, incident response activities, and system error handling. By
incorporating flaw remediation into configuration management processes, required remediation
actions can be tracked and verified.
Organization-defined time periods for updating security-relevant software and firmware may
vary based on a variety of risk factors, including the security category of the system, the criticality
of the update (i.e., severity of the vulnerability related to the discovered flaw), the organizational
risk tolerance, the mission supported by the system, or the threat environment. Some types of
flaw remediation may require more testing than other types. Organizations determine the type
of testing needed for the specific type of flaw remediation activity under consideration and the
types of changes that are to be configuration-managed. In some situations, organizations may
determine that the testing of software or firmware updates is not necessary or practical, such as
when implementing simple malicious code signature updates. In testing decisions, organizations
consider whether security-relevant software or firmware updates are obtained from authorized
sources with appropriate digital signatures.
Related Controls:  CA-5, CM-3, CM-4, CM-5, CM-6, CM-8, MA-2, RA-5, SA-8, SA-10, SA-11, SI-3,
SI-
5, SI-7, SI-11.
Control Enhancements:
(1) FLAW REMEDIATION | CENTRAL MANAGEMENT
[Withdrawn: Incorporated into PL-9.]
(2) FLAW REMEDIATION | AUTOMATED FLAW REMEDIATION STATUS
Determine if system components have applicable security-relevant software and firmware
updates installed using [Assignment: organization-defined automated mechanisms]
[Assignment: organization-defined frequency].
Discussion:  Automated mechanisms can track and determine the status of known flaws for
system components.
Related Controls:  CA-7, SI-4.
(3) FLAW REMEDIATION | TIME TO REMEDIATE FLAWS AND BENCHMARKS FOR CORRECTIVE ACTIONS
(a) Measure the time between flaw identification and flaw remediation; and
(b) Establish the following benchmarks for taking corrective actions: [Assignment:
organization-defined benchmarks].
Discussion:  Organizations determine the time it takes on average to correct system flaws
after such flaws have been identified and subsequently establish organizational benchmarks
CHAPTER THREE   PAGE 334
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
(i.e., time frames) for taking corrective actions. Benchmarks can be established by the type
of flaw or the severity of the potential vulnerability if the flaw can be exploited.
Related Controls:  None.
(4) FLAW REMEDIATION | AUTOMATED PATCH MANAGEMENT TOOLS
Employ automated patch management tools to facilitate flaw remediation to the following
system components: [Assignment: organization-defined system components].
Discussion:  Using automated tools to support patch management helps to ensure the
timeliness and completeness of system patching operations.
Related Controls:  None.
(5) FLAW REMEDIATION | AUTOMATIC SOFTWARE AND FIRMWARE UPDATES
Install [Assignment: organization-defined security-relevant software and firmware
updates] automatically to [Assignment: organization-defined system components].
Discussion:  Due to system integrity and availability concerns, organizations consider the
methodology used to carry out automatic updates. Organizations balance the need to
ensure that the updates are installed as soon as possible with the need to maintain
configuration management and control with any mission or operational impacts that
automatic updates might impose.
Related Controls:  None.
(6) FLAW REMEDIATION | REMOVAL OF PREVIOUS VERSIONS OF SOFTWARE AND FIRMWARE
Remove previous versions of [Assignment: organization-defined software and firmware
components] after updated versions have been installed.
Discussion:  Previous versions of software or firmware components that are not removed
from the system after updates have been installed may be exploited by adversaries. Some
products may automatically remove previous versions of software and firmware from the
system.
Related Controls:  None.
References:  [OMB A-130], [FIPS 140-3], [FIPS 186-4], [SP 800-39], [SP 800-40], [SP 800-128], [IR
7788].
