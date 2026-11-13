---
schema_version: 1
corpus: federal-reference
jurisdiction: us
id: nist-sp-800-53-r5.ir-9
title: NIST SP 800-53 Rev. 5 IR-9 — INFORMATION SPILLAGE RESPONSE
doc_type: federal_instrument
citation: NIST SP 800-53 Rev. 5 IR-9
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

**NIST SP 800-53 Rev. 5 IR-9** — INFORMATION SPILLAGE RESPONSE

- Issued by: National Institute of Standards and Technology
- Publication: NIST SP 800-53 Rev. 5 — Security and Privacy Controls for Information Systems and Organizations ([nist-sp-800-53-r5](./nist-sp-800-53-r5.md))
- Version: Rev. 5 (September 2020, includes updates as of 2020-12-10)
- Text as of: 2026-11-12
- Cited by held documents: 4 times (irs-pub-1075-11-2021 ×3, arc-ampe ×1)
- Reproduction basis: 17 U.S.C. § 105 — work of the U.S. government (NIST). Determined per document on 2026-11-12 against the publication itself, not assumed from its issuer: its Authority statement (PDF page 3) reads "This publication may be used by nongovernmental organizations on a voluntary basis and is not subject to copyright in the United States. Attribution would, however, be appreciated by NIST." Held here: the front matter and Chapter Three (the control catalog) only. Chapter Three names ISO/IEC standards solely as bibliographic references and reproduces none of their text. NOT mirrored: the References bibliography and Appendices A-C; Appendix A (glossary) adapts third-party definitions (ISO/IEC 15026, ISO 25237, ISO/IEC 29100, ISO 15288, IETF RFC 4949), which ADR-0002 treats as not reproducible by being incorporated, and whose reproducibility has not been determined.


_NON-AUTHORITATIVE copy of one control, cut from the SP 800-53 Rev. 5 snapshot this corpus holds. Whether and how this binds a given agency depends on the instrument that incorporates it — read it at the source URL before relying on it. This copy is the Rev. 5 text of record, which is not necessarily the text a citing document meant (a document citing Rev. 4 is not answered by it)._


## Full text

### IR-9 INFORMATION SPILLAGE RESPONSE
Control:  Respond to information spills by:
a. Assigning [Assignment: organization-defined personnel or roles] with responsibility for
responding to information spills;
CHAPTER THREE   PAGE 160
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
b. Identifying the specific information involved in the system contamination;
c. Alerting [Assignment: organization-defined personnel or roles] of the information spill using
a method of communication not associated with the spill;
d. Isolating the contaminated system or system component;
e. Eradicating the information from the contaminated system or component;
f. Identifying other systems or system components that may have been subsequently
contaminated; and
g. Performing the following additional actions: [Assignment: organization-defined actions].
Discussion:  Information spillage refers to instances where information is placed on systems that
are not authorized to process such information. Information spills occur when information that is
thought to be a certain classification or impact level is transmitted to a system and subsequently
is determined to be of a higher classification or impact level. At that point, corrective action is
required. The nature of the response is based on the classification or impact level of the spilled
information, the security capabilities of the system, the specific nature of the contaminated
storage media, and the access authorizations of individuals with authorized access to the
contaminated system. The methods used to communicate information about the spill after the
fact do not involve methods directly associated with the actual spill to minimize the risk of
further spreading the contamination before such contamination is isolated and eradicated.
Related Controls:  CP-2, IR-6, PM-26, PM-27, PT-2, PT-3, PT-7, RA-7.
Control Enhancements:
(1) INFORMATION SPILLAGE RESPONSE | RESPONSIBLE PERSONNEL
[Withdrawn: Incorporated into IR-9.]
(2) INFORMATION SPILLAGE RESPONSE | TRAINING
Provide information spillage response training [Assignment: organization-defined
frequency].
Discussion:  Organizations establish requirements for responding to information spillage
incidents in incident response plans. Incident response training on a regular basis helps to
ensure that organizational personnel understand their individual responsibilities and what
specific actions to take when spillage incidents occur.
Related Controls:  AT-2, AT-3, CP-3, IR-2.
(3) INFORMATION SPILLAGE RESPONSE | POST-SPILL OPERATIONS
Implement the following procedures to ensure that organizational personnel impacted by
information spills can continue to carry out assigned tasks while contaminated systems are
undergoing corrective actions: [Assignment: organization-defined procedures].
Discussion:  Corrective actions for systems contaminated due to information spillages may
be time-consuming. Personnel may not have access to the contaminated systems while
corrective actions are being taken, which may potentially affect their ability to conduct
organizational business.
Related Controls:  None.
(4) INFORMATION SPILLAGE RESPONSE | EXPOSURE TO UNAUTHORIZED PERSONNEL
Employ the following controls for personnel exposed to information not within assigned
access authorizations: [Assignment: organization-defined controls].
Discussion:  Controls include ensuring that personnel who are exposed to spilled information
are made aware of the laws, executive orders, directives, regulations, policies, standards,
CHAPTER THREE   PAGE 161
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
and guidelines regarding the information and the restrictions imposed based on exposure to
such information.
Related Controls:  None.
References:  None.
