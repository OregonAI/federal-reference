---
schema_version: 1
corpus: federal-reference
jurisdiction: us
id: nist-sp-800-53-r5.mp-6
title: NIST SP 800-53 Rev. 5 MP-6 — MEDIA SANITIZATION
doc_type: federal_instrument
citation: NIST SP 800-53 Rev. 5 MP-6
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

**NIST SP 800-53 Rev. 5 MP-6** — MEDIA SANITIZATION

- Issued by: National Institute of Standards and Technology
- Publication: NIST SP 800-53 Rev. 5 — Security and Privacy Controls for Information Systems and Organizations ([nist-sp-800-53-r5](./nist-sp-800-53-r5.md))
- Version: Rev. 5 (September 2020, includes updates as of 2020-12-10)
- Text as of: 2026-11-12
- Cited by held documents: 28 times (cjis-sp-6-1 ×12, irs-pub-1075-11-2021 ×9, arc-ampe ×6, 6-cfr-37 ×1)
- Reproduction basis: 17 U.S.C. § 105 — work of the U.S. government (NIST). Determined per document on 2026-11-12 against the publication itself, not assumed from its issuer: its Authority statement (PDF page 3) reads "This publication may be used by nongovernmental organizations on a voluntary basis and is not subject to copyright in the United States. Attribution would, however, be appreciated by NIST." Held here: the front matter and Chapter Three (the control catalog) only. Chapter Three names ISO/IEC standards solely as bibliographic references and reproduces none of their text. NOT mirrored: the References bibliography and Appendices A-C; Appendix A (glossary) adapts third-party definitions (ISO/IEC 15026, ISO 25237, ISO/IEC 29100, ISO 15288, IETF RFC 4949), which ADR-0002 treats as not reproducible by being incorporated, and whose reproducibility has not been determined.


_NON-AUTHORITATIVE copy of one control, cut from the SP 800-53 Rev. 5 snapshot this corpus holds. Whether and how this binds a given agency depends on the instrument that incorporates it — read it at the source URL before relying on it. This copy is the Rev. 5 text of record, which is not necessarily the text a citing document meant (a document citing Rev. 4 is not answered by it)._


## Full text

### MP-6 MEDIA SANITIZATION
Control:
a. Sanitize [Assignment: organization-defined system media] prior to disposal, release out of
organizational control, or release for reuse using [Assignment: organization-defined
sanitization techniques and procedures]; and
b. Employ sanitization mechanisms with the strength and integrity commensurate with the
security category or classification of the information.
Discussion:   Media sanitization applies to all digital and non-digital system media subject to
disposal or reuse, whether or not the media is considered removable. Examples include digital
media in scanners, copiers, printers, notebook computers, workstations, network components,
mobile devices, and non-digital media (e.g., paper and microfilm). The sanitization process
removes information from system media such that the information cannot be retrieved or
reconstructed. Sanitization techniques—including clearing, purging, cryptographic erase, de-
identification of personally identifiable information, and destruction—prevent the disclosure of
information to unauthorized individuals when such media is reused or released for disposal.
Organizations determine the appropriate sanitization methods, recognizing that destruction is
sometimes necessary when other methods cannot be applied to media requiring sanitization.
CHAPTER THREE   PAGE 175
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
Organizations use discretion on the employment of approved sanitization techniques and
procedures for media that contains information deemed to be in the public domain or publicly
releasable or information deemed to have no adverse impact on organizations or individuals if
released for reuse or disposal. Sanitization of non-digital media includes destruction, removing a
classified appendix from an otherwise unclassified document, or redacting selected sections or
words from a document by obscuring the redacted sections or words in a manner equivalent in
effectiveness to removing them from the document. NSA standards and policies control the
sanitization process for media that contains classified information. NARA policies control the
sanitization process for controlled unclassified information.
Related Controls:  AC-3, AC-7, AU-11, MA-2, MA-3, MA-4, MA-5, PM-22, SI-12, SI-18, SI-19, SR-11.
Control Enhancements:
(1) MEDIA SANITIZATION | REVIEW, APPROVE, TRACK, DOCUMENT, AND VERIFY
Review, approve, track, document, and verify media sanitization and disposal actions.
Discussion:  Organizations review and approve media to be sanitized to ensure compliance
with records retention policies. Tracking and documenting actions include listing personnel
who reviewed and approved sanitization and disposal actions, types of media sanitized, files
stored on the media, sanitization methods used, date and time of the sanitization actions,
personnel who performed the sanitization, verification actions taken and personnel who
performed the verification, and the disposal actions taken. Organizations verify that the
sanitization of the media was effective prior to disposal.
Related Controls:  None.
(2) MEDIA SANITIZATION | EQUIPMENT TESTING
Test sanitization equipment and procedures [Assignment: organization-defined frequency]
to ensure that the intended sanitization is being achieved.
Discussion:  Testing of sanitization equipment and procedures may be conducted by
qualified and authorized external entities, including federal agencies or external service
providers.
Related Controls:  None.
(3) MEDIA SANITIZATION | NONDESTRUCTIVE TECHNIQUES
Apply nondestructive sanitization techniques to portable storage devices prior to
connecting such devices to the system under the following circumstances: [Assignment:
organization-defined circumstances requiring sanitization of portable storage devices].
Discussion:  Portable storage devices include external or removable hard disk drives (e.g.,
solid state, magnetic), optical discs, magnetic or optical tapes, flash memory devices, flash
memory cards, and other external or removable disks. Portable storage devices can be
obtained from untrustworthy sources and contain malicious code that can be inserted into
or transferred to organizational systems through USB ports or other entry portals. While
scanning storage devices is recommended, sanitization provides additional assurance that
such devices are free of malicious code. Organizations consider nondestructive sanitization
of portable storage devices when the devices are purchased from manufacturers or vendors
prior to initial use or when organizations cannot maintain a positive chain of custody for the
devices.
Related Controls:  None.
(4) MEDIA SANITIZATION | CONTROLLED UNCLASSIFIED INFORMATION
[Withdrawn: Incorporated into MP-6.]
(5) MEDIA SANITIZATION | CLASSIFIED INFORMATION
CHAPTER THREE   PAGE 176
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
[Withdrawn: Incorporated into MP-6.]
(6) MEDIA SANITIZATION | MEDIA DESTRUCTION
[Withdrawn: Incorporated into MP-6.]
(7) MEDIA SANITIZATION | DUAL AUTHORIZATION
Enforce dual authorization for the sanitization of [Assignment: organization-defined
system media].
Discussion:  Organizations employ dual authorization to help ensure that system media
sanitization cannot occur unless two technically qualified individuals conduct the designated
task. Individuals who sanitize system media possess sufficient skills and expertise to
determine if the proposed sanitization reflects applicable federal and organizational
standards, policies, and procedures. Dual authorization also helps to ensure that sanitization
occurs as intended, protecting against errors and false claims of having performed the
sanitization actions. Dual authorization may also be known as two-person control. To reduce
the risk of collusion, organizations consider rotating dual authorization duties to other
individuals.
Related Controls:  AC-3, MP-2.
(8) MEDIA SANITIZATION | REMOTE PURGING OR WIPING OF INFORMATION
Provide the capability to purge or wipe information from [Assignment: organization-
defined systems or system components] [Selection: remotely; under the following
conditions: [Assignment: organization-defined conditions]].
Discussion:  Remote purging or wiping of information protects information on organizational
systems and system components if systems or components are obtained by unauthorized
individuals. Remote purge or wipe commands require strong authentication to help mitigate
the risk of unauthorized individuals purging or wiping the system, component, or device. The
purge or wipe function can be implemented in a variety of ways, including by overwriting
data or information multiple times or by destroying the key necessary to decrypt encrypted
data.
Related Controls:  None.
References:  [32 CFR 2002], [OMB A-130], [NARA CUI], [FIPS 199], [SP 800-60-1], [SP 800-60-2],
[SP 800-88], [SP 800-124], [IR 8023], [NSA MEDIA].
