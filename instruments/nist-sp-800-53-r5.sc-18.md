---
schema_version: 1
corpus: federal-reference
jurisdiction: us
id: nist-sp-800-53-r5.sc-18
title: NIST SP 800-53 Rev. 5 SC-18 — MOBILE CODE
doc_type: federal_instrument
citation: NIST SP 800-53 Rev. 5 SC-18
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

**NIST SP 800-53 Rev. 5 SC-18** — MOBILE CODE

- Issued by: National Institute of Standards and Technology
- Publication: NIST SP 800-53 Rev. 5 — Security and Privacy Controls for Information Systems and Organizations ([nist-sp-800-53-r5](./nist-sp-800-53-r5.md))
- Version: Rev. 5 (September 2020, includes updates as of 2020-12-10)
- Text as of: 2026-11-12
- Cited by held documents: 16 times (cjis-sp-6-1 ×11, irs-pub-1075-11-2021 ×3, 6-cfr-37 ×1, arc-ampe ×1)
- Reproduction basis: 17 U.S.C. § 105 — work of the U.S. government (NIST). Determined per document on 2026-11-12 against the publication itself, not assumed from its issuer: its Authority statement (PDF page 3) reads "This publication may be used by nongovernmental organizations on a voluntary basis and is not subject to copyright in the United States. Attribution would, however, be appreciated by NIST." Held here: the front matter and Chapter Three (the control catalog) only. Chapter Three names ISO/IEC standards solely as bibliographic references and reproduces none of their text. NOT mirrored: the References bibliography and Appendices A-C; Appendix A (glossary) adapts third-party definitions (ISO/IEC 15026, ISO 25237, ISO/IEC 29100, ISO 15288, IETF RFC 4949), which ADR-0002 treats as not reproducible by being incorporated, and whose reproducibility has not been determined.


_NON-AUTHORITATIVE copy of one control, cut from the SP 800-53 Rev. 5 snapshot this corpus holds. Whether and how this binds a given agency depends on the instrument that incorporates it — read it at the source URL before relying on it. This copy is the Rev. 5 text of record, which is not necessarily the text a citing document meant (a document citing Rev. 4 is not answered by it)._


## Full text

### SC-18 MOBILE CODE
Control:
a. Define acceptable and unacceptable mobile code and mobile code technologies; and
b. Authorize, monitor, and control the use of mobile code within the system.
CHAPTER THREE   PAGE 312
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
Discussion:  Mobile code includes any program, application, or content that can be transmitted
across a network (e.g., embedded in an email, document, or website) and executed on a remote
system. Decisions regarding the use of mobile code within organizational systems are based on
the potential for the code to cause damage to the systems if used maliciously. Mobile code
technologies include Java applets, JavaScript, HTML5, WebGL, and VBScript. Usage restrictions
and implementation guidelines apply to both the selection and use of mobile code installed on
servers and mobile code downloaded and executed on individual workstations and devices,
including notebook computers and smart phones. Mobile code policy and procedures address
specific actions taken to prevent the development, acquisition, and introduction of unacceptable
mobile code within organizational systems, including requiring mobile code to be digitally signed
by a trusted source.
Related Controls:  AU-2, AU-12, CM-2, CM-6, SI-3.
Control Enhancements:
(1) MOBILE CODE | IDENTIFY UNACCEPTABLE CODE AND TAKE CORRECTIVE ACTIONS
Identify [Assignment: organization-defined unacceptable mobile code] and take
[Assignment: organization-defined corrective actions].
Discussion:  Corrective actions when unacceptable mobile code is detected include blocking,
quarantine, or alerting administrators. Blocking includes preventing the transmission of
word processing files with embedded macros when such macros have been determined to
be unacceptable mobile code.
Related Controls:  None.
(2) MOBILE CODE | ACQUISITION, DEVELOPMENT, AND USE
Verify that the acquisition, development, and use of mobile code to be deployed in the
system meets [Assignment: organization-defined mobile code requirements].
Discussion:  None.
Related Controls:  None.
(3) MOBILE CODE | PREVENT DOWNLOADING AND EXECUTION
Prevent the download and execution of [Assignment: organization-defined unacceptable
mobile code].
Discussion:  None.
Related Controls:  None.
(4) MOBILE CODE | PREVENT AUTOMATIC EXECUTION
Prevent the automatic execution of mobile code in [Assignment: organization-defined
software applications] and enforce [Assignment: organization-defined actions] prior to
executing the code.
Discussion:  Actions enforced before executing mobile code include prompting users prior to
opening email attachments or clicking on web links. Preventing the automatic execution of
mobile code includes disabling auto-execute features on system components that employ
portable storage devices, such as compact discs, digital versatile discs, and universal serial
bus devices.
Related Controls:  None.
(5) MOBILE CODE | ALLOW EXECUTION ONLY IN CONFINED ENVIRONMENTS
Allow execution of permitted mobile code only in confined virtual machine environments.
CHAPTER THREE   PAGE 313
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
Discussion:  Permitting the execution of mobile code only in confined virtual machine
environments helps prevent the introduction of malicious code into other systems and
system components.
Related Controls:  SC-44, SI-7.
References:  [SP 800-28].
