---
schema_version: 1
corpus: federal-reference
jurisdiction: us
id: nist-sp-800-53-r5.mp-7
title: NIST SP 800-53 Rev. 5 MP-7 — MEDIA USE
doc_type: federal_instrument
citation: NIST SP 800-53 Rev. 5 MP-7
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

**NIST SP 800-53 Rev. 5 MP-7** — MEDIA USE

- Issued by: National Institute of Standards and Technology
- Publication: NIST SP 800-53 Rev. 5 — Security and Privacy Controls for Information Systems and Organizations ([nist-sp-800-53-r5](./nist-sp-800-53-r5.md))
- Version: Rev. 5 (September 2020, includes updates as of 2020-12-10)
- Text as of: 2026-11-12
- Cited by held documents: 16 times (cjis-sp-6-1 ×9, arc-ampe ×3, irs-pub-1075-11-2021 ×3, 6-cfr-37 ×1)
- Reproduction basis: 17 U.S.C. § 105 — work of the U.S. government (NIST). Determined per document on 2026-11-12 against the publication itself, not assumed from its issuer: its Authority statement (PDF page 3) reads "This publication may be used by nongovernmental organizations on a voluntary basis and is not subject to copyright in the United States. Attribution would, however, be appreciated by NIST." Held here: the front matter and Chapter Three (the control catalog) only. Chapter Three names ISO/IEC standards solely as bibliographic references and reproduces none of their text. NOT mirrored: the References bibliography and Appendices A-C; Appendix A (glossary) adapts third-party definitions (ISO/IEC 15026, ISO 25237, ISO/IEC 29100, ISO 15288, IETF RFC 4949), which ADR-0002 treats as not reproducible by being incorporated, and whose reproducibility has not been determined.


_NON-AUTHORITATIVE copy of one control, cut from the SP 800-53 Rev. 5 snapshot this corpus holds. Whether and how this binds a given agency depends on the instrument that incorporates it — read it at the source URL before relying on it. This copy is the Rev. 5 text of record, which is not necessarily the text a citing document meant (a document citing Rev. 4 is not answered by it)._


## Full text

### MP-7 MEDIA USE
Control:
a. [Selection: Restrict; Prohibit] the use of [Assignment: organization-defined types of system
media] on [Assignment: organization-defined systems or system components] using
[Assignment: organization-defined controls]; and
b. Prohibit the use of portable storage devices in organizational systems when such devices
have no identifiable owner.
Discussion:  System media includes both digital and non-digital media. Digital media includes
diskettes, magnetic tapes, flash drives, compact discs, digital versatile discs, and removable hard
disk drives. Non-digital media includes paper and microfilm. Media use protections also apply to
mobile devices with information storage capabilities. In contrast to MP-2, which restricts user
access to media, MP-7 restricts the use of certain types of media on systems, for example,
restricting or prohibiting the use of flash drives or external hard disk drives. Organizations use
technical and nontechnical controls to restrict the use of system media. Organizations may
restrict the use of portable storage devices, for example, by using physical cages on workstations
to prohibit access to certain external ports or disabling or removing the ability to insert, read, or
CHAPTER THREE   PAGE 177
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
write to such devices. Organizations may also limit the use of portable storage devices to only
approved devices, including devices provided by the organization, devices provided by other
approved organizations, and devices that are not personally owned. Finally, organizations may
restrict the use of portable storage devices based on the type of device, such as by prohibiting
the use of writeable, portable storage devices and implementing this restriction by disabling or
removing the capability to write to such devices. Requiring identifiable owners for storage
devices reduces the risk of using such devices by allowing organizations to assign responsibility
for addressing known vulnerabilities in the devices.
Related Controls:  AC-19, AC-20, PL-4, PM-12, SC-34, SC-41
.
Control Enhancements:
(1) MEDIA USE | PROHIBIT USE WITHOUT OWNER
[Withdrawn: Incorporated into MP-7.]
(2) MEDIA USE | PROHIBIT USE OF SANITIZATION-RESISTANT MEDIA
Prohibit the use of sanitization-resistant media in organizational systems.
Discussion:  Sanitization resistance refers to how resistant media are to non-destructive
sanitization techniques with respect to the capability to purge information from media.
Certain types of media do not support sanitization commands, or if supported, the interfaces
are not supported in a standardized way across these devices. Sanitization-resistant media
includes compact flash, embedded flash on boards and devices, solid state drives, and USB
removable media.
Related Controls:  MP-6.
References:  [FIPS 199], [SP 800-111].
