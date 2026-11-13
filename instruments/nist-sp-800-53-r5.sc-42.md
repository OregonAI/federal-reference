---
schema_version: 1
corpus: federal-reference
jurisdiction: us
id: nist-sp-800-53-r5.sc-42
title: NIST SP 800-53 Rev. 5 SC-42 — SENSOR CAPABILITY AND DATA
doc_type: federal_instrument
citation: NIST SP 800-53 Rev. 5 SC-42
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

**NIST SP 800-53 Rev. 5 SC-42** — SENSOR CAPABILITY AND DATA

- Issued by: National Institute of Standards and Technology
- Publication: NIST SP 800-53 Rev. 5 — Security and Privacy Controls for Information Systems and Organizations ([nist-sp-800-53-r5](./nist-sp-800-53-r5.md))
- Version: Rev. 5 (September 2020, includes updates as of 2020-12-10)
- Text as of: 2026-11-12
- Cited by held documents: 1 time (arc-ampe ×1), 1 of them naming an enhancement of this control
- Reproduction basis: 17 U.S.C. § 105 — work of the U.S. government (NIST). Determined per document on 2026-11-12 against the publication itself, not assumed from its issuer: its Authority statement (PDF page 3) reads "This publication may be used by nongovernmental organizations on a voluntary basis and is not subject to copyright in the United States. Attribution would, however, be appreciated by NIST." Held here: the front matter and Chapter Three (the control catalog) only. Chapter Three names ISO/IEC standards solely as bibliographic references and reproduces none of their text. NOT mirrored: the References bibliography and Appendices A-C; Appendix A (glossary) adapts third-party definitions (ISO/IEC 15026, ISO 25237, ISO/IEC 29100, ISO 15288, IETF RFC 4949), which ADR-0002 treats as not reproducible by being incorporated, and whose reproducibility has not been determined.


_NON-AUTHORITATIVE copy of one control, cut from the SP 800-53 Rev. 5 snapshot this corpus holds. Whether and how this binds a given agency depends on the instrument that incorporates it — read it at the source URL before relying on it. This copy is the Rev. 5 text of record, which is not necessarily the text a citing document meant (a document citing Rev. 4 is not answered by it)._


## Full text

### SC-42 SENSOR CAPABILITY AND DATA
Control:
a. Prohibit [Selection (one or more): the use of devices possessing [Assignment: organization-
defined environmental sensing capabilities] in [Assignment: organization-defined facilities,
areas, or systems]; the remote activation of environmental sensing capabilities on
organizational systems or system components with the following exceptions: [Assignment:
organization-defined exceptions where remote activation of sensors is allowed]]; and
b. Provide an explicit indication of sensor use to [Assignment: organization-defined group of
users].
Discussion:  Sensor capability and data applies to types of systems or system components
characterized as mobile devices, such as cellular telephones, smart phones, and tablets. Mobile
devices often include sensors that can collect and record data regarding the environment where
the system is in use. Sensors that are embedded within mobile devices include microphones,
cameras, Global Positioning System (GPS) mechanisms, and accelerometers. While the sensors
on mobiles devices provide an important function, if activated covertly, such devices can
potentially provide a means for adversaries to learn valuable information about individuals and
organizations. For example, remotely activating the GPS function on a mobile device could
provide an adversary with the ability to track the movements of an individual. Organizations may
prohibit individuals from bringing cellular telephones or digital cameras into certain designated
facilities or controlled areas within facilities where classified information is stored or sensitive
conversations are taking place.
Related Controls:  SC-15.
Control Enhancements:
(1) SENSOR CAPABILITY AND DATA | REPORTING TO AUTHORIZED INDIVIDUALS OR ROLES
CHAPTER THREE   PAGE 327
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
Verify that the system is configured so that data or information collected by the
[Assignment: organization-defined sensors] is only reported to authorized individuals or
roles.
Discussion:  In situations where sensors are activated by authorized individuals, it is still
possible that the data or information collected by the sensors will be sent to unauthorized
entities.
Related Controls:  None.
(2) SENSOR CAPABILITY AND DATA | AUTHORIZED USE
Employ the following measures so that data or information collected by [Assignment:
organization-defined sensors] is only used for authorized purposes: [Assignment:
organization-defined measures].
Discussion:  Information collected by sensors for a specific authorized purpose could be
misused for some unauthorized purpose. For example, GPS sensors that are used to support
traffic navigation could be misused to track the movements of individuals. Measures to
mitigate such activities include additional training to help ensure that authorized individuals
do not abuse their authority and, in the case where sensor data is maintained by external
parties, contractual restrictions on the use of such data.
Related Controls:  PT-2.
(3) SENSOR CAPABILITY AND DATA | PROHIBIT USE OF DEVICES
[Withdrawn: Incorporated into SC-42.]
(4) SENSOR CAPABILITY AND DATA | NOTICE OF COLLECTION
Employ the following measures to facilitate an individual’s awareness that personally
identifiable information is being collected by [Assignment: organization-defined sensors]:
[Assignment: organization-defined measures].
Discussion:  Awareness that organizational sensors are collecting data enables individuals to
more effectively engage in managing their privacy. Measures can include conventional
written notices and sensor configurations that make individuals directly or indirectly aware
through other devices that the sensor is collecting information. The usability and efficacy of
the notice are important considerations.
Related Controls:  PT-1, PT-4, PT-5.
(5) SENSOR CAPABILITY AND DATA | COLLECTION MINIMIZATION
Employ [Assignment: organization-defined sensors] that are configured to minimize the
collection of information about individuals that is not needed.
Discussion:  Although policies to control for authorized use can be applied to information
once it is collected, minimizing the collection of information that is not needed mitigates
privacy risk at the system entry point and mitigates the risk of policy control failures. Sensor
configurations include the obscuring of human features, such as blurring or pixelating flesh
tones.
Related Controls:  SA-8, SI-12.
References:  [OMB A-130], [SP 800-124].
