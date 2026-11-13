---
schema_version: 1
corpus: federal-reference
jurisdiction: us
id: nist-sp-800-53-r5.ac-19
title: NIST SP 800-53 Rev. 5 AC-19 — ACCESS CONTROL FOR MOBILE DEVICES
doc_type: federal_instrument
citation: NIST SP 800-53 Rev. 5 AC-19
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

**NIST SP 800-53 Rev. 5 AC-19** — ACCESS CONTROL FOR MOBILE DEVICES

- Issued by: National Institute of Standards and Technology
- Publication: NIST SP 800-53 Rev. 5 — Security and Privacy Controls for Information Systems and Organizations ([nist-sp-800-53-r5](./nist-sp-800-53-r5.md))
- Version: Rev. 5 (September 2020, includes updates as of 2020-12-10)
- Text as of: 2026-11-12
- Cited by held documents: 39 times (cjis-sp-6-1 ×31, irs-pub-1075-11-2021 ×4, 6-cfr-37 ×2, arc-ampe ×2), 1 of them naming an enhancement of this control
- Reproduction basis: 17 U.S.C. § 105 — work of the U.S. government (NIST). Determined per document on 2026-11-12 against the publication itself, not assumed from its issuer: its Authority statement (PDF page 3) reads "This publication may be used by nongovernmental organizations on a voluntary basis and is not subject to copyright in the United States. Attribution would, however, be appreciated by NIST." Held here: the front matter and Chapter Three (the control catalog) only. Chapter Three names ISO/IEC standards solely as bibliographic references and reproduces none of their text. NOT mirrored: the References bibliography and Appendices A-C; Appendix A (glossary) adapts third-party definitions (ISO/IEC 15026, ISO 25237, ISO/IEC 29100, ISO 15288, IETF RFC 4949), which ADR-0002 treats as not reproducible by being incorporated, and whose reproducibility has not been determined.


_NON-AUTHORITATIVE copy of one control, cut from the SP 800-53 Rev. 5 snapshot this corpus holds. Whether and how this binds a given agency depends on the instrument that incorporates it — read it at the source URL before relying on it. This copy is the Rev. 5 text of record, which is not necessarily the text a citing document meant (a document citing Rev. 4 is not answered by it)._


## Full text

### AC-19 ACCESS CONTROL FOR MOBILE DEVICES
Control:
a. Establish configuration requirements, connection requirements, and implementation
guidance for organization-controlled mobile devices, to include when such devices are
outside of controlled areas; and
b. Authorize the connection of mobile devices to organizational systems.
Discussion:  A mobile device is a computing device that has a small form factor such that it can
easily be carried by a single individual; is designed to operate without a physical connection;
possesses local, non-removable or removable data storage; and includes a self-contained power
source. Mobile device functionality may also include voice communication capabilities, on-board
sensors that allow the device to capture information, and/or built-in features for synchronizing
local data with remote locations. Examples include smart phones and tablets. Mobile devices are
typically associated with a single individual. The processing, storage, and transmission capability
of the mobile device may be comparable to or merely a subset of notebook/desktop systems,
depending on the nature and intended purpose of the device. Protection and control of mobile
devices is behavior or policy-based and requires users to take physical action to protect and
control such devices when outside of controlled areas. Controlled areas are spaces for which
organizations provide physical or procedural controls to meet the requirements established for
protecting information and systems.
CHAPTER THREE   PAGE 52
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
Due to the large variety of mobile devices with different characteristics and capabilities,
organizational restrictions may vary for the different classes or types of such devices. Usage
restrictions and specific implementation guidance for mobile devices include configuration
management, device identification and authentication, implementation of mandatory protective
software, scanning devices for malicious code, updating virus protection software, scanning for
critical software updates and patches, conducting primary operating system (and possibly other
resident software) integrity checks, and disabling unnecessary hardware.
Usage restrictions and authorization to connect may vary among organizational systems. For
example, the organization may authorize the connection of mobile devices to its network and
impose a set of usage restrictions, while a system owner may withhold authorization for mobile
device connection to specific applications or impose additional usage restrictions before allowing
mobile device connections to a system. Adequate security for mobile devices goes beyond the
requirements specified in AC-19. Many safeguards for mobile devices are reflected in other
controls. AC-20 addresses mobile devices that are not organization-controlled.
Related Controls:  AC-3, AC-4, AC-7, AC-11, AC-17, AC-18, AC-20, CA-9, CM-2, CM-6, IA-2, IA-3,
MP-2, MP-4, MP-5, MP-7, PL-4, SC-7, SC-34, SC-43, SI-3, SI-4.
Control Enhancements:
(1) ACCESS CONTROL FOR MOBILE DEVICES | USE OF WRITABLE AND PORTABLE STORAGE DEVICES
[Withdrawn: Incorporated into MP-7.]
(2) ACCESS CONTROL FOR MOBILE DEVICES | USE OF PERSONALLY OWNED PORTABLE STORAGE DEVICES
[Withdrawn: Incorporated into MP-7.]
(3) ACCESS CONTROL FOR MOBILE DEVICES | USE OF PORTABLE STORAGE DEVICES WITH NO
IDENTIFIABLE OWNER
[Withdrawn: Incorporated into MP-7.]
(4) ACCESS CONTROL FOR MOBILE DEVICES | RESTRICTIONS FOR CLASSIFIED INFORMATION
(a) Prohibit the use of unclassified mobile devices in facilities containing systems
processing, storing, or transmitting classified information unless specifically permitted
by the authorizing official; and
(b) Enforce the following restrictions on individuals permitted by the authorizing official
to use unclassified mobile devices in facilities containing systems processing, storing,
or transmitting classified information:
(1) Connection of unclassified mobile devices to classified systems is prohibited;
(2) Connection of unclassified mobile devices to unclassified systems requires
approval from the authorizing official;
(3) Use of internal or external modems or wireless interfaces within the unclassified
mobile devices is prohibited; and
(4) Unclassified mobile devices and the information stored on those devices are
subject to random reviews and inspections by [Assignment: organization-defined
security officials], and if classified information is found, the incident handling
policy is followed.
(c) Restrict the connection of classified mobile devices to classified systems in accordance
with [Assignment: organization-defined security policies].
Discussion:  None.
Related Controls:  CM-8, IR-4.
(5) ACCESS CONTROL FOR MOBILE DEVICES | FULL DEVICE OR CONTAINER-BASED ENCRYPTION
CHAPTER THREE   PAGE 53
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
Employ [Selection: full-device encryption; container-based encryption] to protect the
confidentiality and integrity of information on [Assignment: organization-defined mobile
devices].
Discussion:  Container-based encryption provides a more fine-grained approach to data and
information encryption on mobile devices, including encrypting selected data structures
such as files, records, or fields.
Related Controls:  SC-12,  SC-13, SC-28.
References:  [SP 800-114], [SP 800-124].
