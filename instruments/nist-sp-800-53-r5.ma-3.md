---
schema_version: 1
corpus: federal-reference
jurisdiction: us
id: nist-sp-800-53-r5.ma-3
title: NIST SP 800-53 Rev. 5 MA-3 — MAINTENANCE TOOLS
doc_type: federal_instrument
citation: NIST SP 800-53 Rev. 5 MA-3
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

**NIST SP 800-53 Rev. 5 MA-3** — MAINTENANCE TOOLS

- Issued by: National Institute of Standards and Technology
- Publication: NIST SP 800-53 Rev. 5 — Security and Privacy Controls for Information Systems and Organizations ([nist-sp-800-53-r5](./nist-sp-800-53-r5.md))
- Version: Rev. 5 (September 2020, includes updates as of 2020-12-10)
- Text as of: 2026-11-12
- Cited by held documents: 19 times (cjis-sp-6-1 ×14, irs-pub-1075-11-2021 ×3, 6-cfr-37 ×1, arc-ampe ×1)
- Reproduction basis: 17 U.S.C. § 105 — work of the U.S. government (NIST). Determined per document on 2026-11-12 against the publication itself, not assumed from its issuer: its Authority statement (PDF page 3) reads "This publication may be used by nongovernmental organizations on a voluntary basis and is not subject to copyright in the United States. Attribution would, however, be appreciated by NIST." Held here: the front matter and Chapter Three (the control catalog) only. Chapter Three names ISO/IEC standards solely as bibliographic references and reproduces none of their text. NOT mirrored: the References bibliography and Appendices A-C; Appendix A (glossary) adapts third-party definitions (ISO/IEC 15026, ISO 25237, ISO/IEC 29100, ISO 15288, IETF RFC 4949), which ADR-0002 treats as not reproducible by being incorporated, and whose reproducibility has not been determined.


_NON-AUTHORITATIVE copy of one control, cut from the SP 800-53 Rev. 5 snapshot this corpus holds. Whether and how this binds a given agency depends on the instrument that incorporates it — read it at the source URL before relying on it. This copy is the Rev. 5 text of record, which is not necessarily the text a citing document meant (a document citing Rev. 4 is not answered by it)._


## Full text

### MA-3 MAINTENANCE TOOLS
Control:
a. Approve, control, and monitor the use of system maintenance tools; and
CHAPTER THREE   PAGE 164
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
b. Review previously approved system maintenance tools [Assignment: organization-defined
frequency].
Discussion:  Approving, controlling, monitoring, and reviewing maintenance tools address
security-related issues associated with maintenance tools that are not within system
authorization boundaries and are used specifically for diagnostic and repair actions on
organizational systems. Organizations have flexibility in determining roles for the approval of
maintenance tools and how that approval is documented. A periodic review of maintenance
tools facilitates the withdrawal of approval for outdated, unsupported, irrelevant, or no-longer-
used tools. Maintenance tools can include hardware, software, and firmware items and may be
pre-installed, brought in with maintenance personnel on media, cloud-based, or downloaded
from a website. Such tools can be vehicles for transporting malicious code, either intentionally or
unintentionally, into a facility and subsequently into systems. Maintenance tools can include
hardware and software diagnostic test equipment and packet sniffers. The hardware and
software components that support maintenance and are a part of the system (including the
software implementing utilities such as “ping,” “ls,” “ipconfig,” or the hardware and software
implementing the monitoring port of an Ethernet switch) are not addressed by maintenance
tools.
Related Controls:  MA-2, PE-16.
Control Enhancements:
(1) MAINTENANCE TOOLS | INSPECT TOOLS
Inspect the maintenance tools used by maintenance personnel for improper or
unauthorized modifications.
Discussion:  Maintenance tools can be directly brought into a facility by maintenance
personnel or downloaded from a vendor’s website. If, upon inspection of the maintenance
tools, organizations determine that the tools have been modified in an improper manner or
the tools contain malicious code, the incident is handled consistent with organizational
policies and procedures for incident handling.
Related Controls:  SI-7.
(2) MAINTENANCE TOOLS | INSPECT MEDIA
Check media containing diagnostic and test programs for malicious code before the media
are used in the system.
Discussion:  If, upon inspection of media containing maintenance, diagnostic, and test
programs, organizations determine that the media contains malicious code, the incident is
handled consistent with organizational incident handling policies and procedures.
Related Controls:  SI-3.
(3) MAINTENANCE TOOLS | PREVENT UNAUTHORIZED REMOVAL
Prevent the removal of maintenance equipment containing organizational information by:
(a) Verifying that there is no organizational information contained on the equipment;
(b) Sanitizing or destroying the equipment;
(c) Retaining the equipment within the facility; or
(d) Obtaining an exemption from [Assignment: organization-defined personnel or roles]
explicitly authorizing removal of the equipment from the facility.
Discussion:  Organizational information includes all information owned by organizations and
any information provided to organizations for which the organizations serve as information
stewards.
Related Controls:  MP-6.
CHAPTER THREE   PAGE 165
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
(4) MAINTENANCE TOOLS | RESTRICTED TOOL USE
Restrict the use of maintenance tools to authorized personnel only.
Discussion:  Restricting the use of maintenance tools to only authorized personnel applies to
systems that are used to carry out maintenance functions.
Related Controls:  AC-3, AC-5, AC-6.
(5) MAINTENANCE TOOLS | EXECUTION WITH PRIVILEGE
Monitor the use of maintenance tools that execute with increased privilege.
Discussion:  Maintenance tools that execute with increased system privilege can result in
unauthorized access to organizational information and assets that would otherwise be
inaccessible.
Related Controls:  AC-3, AC-6.
(6) MAINTENANCE TOOLS | SOFTWARE UPDATES AND PATCHES
Inspect maintenance tools to ensure the latest software updates and patches are installed.
Discussion:  Maintenance tools using outdated and/or unpatched software can provide a
threat vector for adversaries and result in a significant vulnerability for organizations.
Related Controls:  AC-3, AC-6.
References:  [SP 800-88].
