---
schema_version: 1
corpus: federal-reference
jurisdiction: us
id: nist-sp-800-53-r5.ca-2
title: NIST SP 800-53 Rev. 5 CA-2 — CONTROL ASSESSMENTS
doc_type: federal_instrument
citation: NIST SP 800-53 Rev. 5 CA-2
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

**NIST SP 800-53 Rev. 5 CA-2** — CONTROL ASSESSMENTS

- Issued by: National Institute of Standards and Technology
- Publication: NIST SP 800-53 Rev. 5 — Security and Privacy Controls for Information Systems and Organizations ([nist-sp-800-53-r5](./nist-sp-800-53-r5.md))
- Version: Rev. 5 (September 2020, includes updates as of 2020-12-10)
- Text as of: 2026-11-12
- Cited by held documents: 26 times (cjis-sp-6-1 ×19, irs-pub-1075-11-2021 ×4, arc-ampe ×2, 6-cfr-37 ×1), 1 of them naming an enhancement of this control
- Reproduction basis: 17 U.S.C. § 105 — work of the U.S. government (NIST). Determined per document on 2026-11-12 against the publication itself, not assumed from its issuer: its Authority statement (PDF page 3) reads "This publication may be used by nongovernmental organizations on a voluntary basis and is not subject to copyright in the United States. Attribution would, however, be appreciated by NIST." Held here: the front matter and Chapter Three (the control catalog) only. Chapter Three names ISO/IEC standards solely as bibliographic references and reproduces none of their text. NOT mirrored: the References bibliography and Appendices A-C; Appendix A (glossary) adapts third-party definitions (ISO/IEC 15026, ISO 25237, ISO/IEC 29100, ISO 15288, IETF RFC 4949), which ADR-0002 treats as not reproducible by being incorporated, and whose reproducibility has not been determined.


_NON-AUTHORITATIVE copy of one control, cut from the SP 800-53 Rev. 5 snapshot this corpus holds. Whether and how this binds a given agency depends on the instrument that incorporates it — read it at the source URL before relying on it. This copy is the Rev. 5 text of record, which is not necessarily the text a citing document meant (a document citing Rev. 4 is not answered by it)._


## Full text

### CA-2 CONTROL ASSESSMENTS
Control:
a. Select the appropriate assessor or assessment team for the type of assessment to be
conducted;
b. Develop a control assessment plan that describes the scope of the assessment including:
1. Controls and control enhancements under assessment;
2. Assessment procedures to be used to determine control effectiveness; and
3. Assessment environment, assessment team, and assessment roles and responsibilities;
c. Ensure the control assessment plan is reviewed and approved by the authorizing official or
designated representative prior to conducting the assessment;
d. Assess the controls in the system and its environment of operation [Assignment:
organization-defined frequency] to determine the extent to which the controls are
implemented correctly, operating as intended, and producing the desired outcome with
respect to meeting established security and privacy requirements;
e. Produce a control assessment report that document the results of the assessment; and
f. Provide the results of the control assessment to [Assignment: organization-defined
individuals or roles].
Discussion:  Organizations ensure that control assessors possess the required skills and technical
expertise to develop effective assessment plans and to conduct assessments of system-specific,
hybrid, common, and program management controls, as appropriate. The required skills include
general knowledge of risk management concepts and approaches as well as comprehensive
knowledge of and experience with the hardware, software, and firmware system components
implemented.
Organizations assess controls in systems and the environments in which those systems operate
as part of initial and ongoing authorizations, continuous monitoring, FISMA annual assessments,
system design and development, systems security engineering, privacy engineering, and the
system development life cycle. Assessments help to ensure that organizations meet information
security and privacy requirements, identify weaknesses and deficiencies in the system design and
development process, provide essential information needed to make risk-based decisions as part
of authorization processes, and comply with vulnerability mitigation procedures. Organizations
conduct assessments on the implemented controls as documented in security and privacy plans.
Assessments can also be conducted throughout the system development life cycle as part of
systems engineering and systems security engineering processes. The design for controls can be
assessed as RFPs are developed, responses assessed, and design reviews conducted. If a design
to implement controls and subsequent implementation in accordance with the design are
assessed during development, the final control testing can be a simple confirmation utilizing
previously completed control assessment and aggregating the outcomes.
Organizations may develop a single, consolidated security and privacy assessment plan for the
system or maintain separate plans. A consolidated assessment plan clearly delineates the roles
and responsibilities for control assessment. If multiple organizations participate in assessing a
system, a coordinated approach can reduce redundancies and associated costs.
Organizations can use other types of assessment activities, such as vulnerability scanning and
system monitoring, to maintain the security and privacy posture of systems during the system
CHAPTER THREE   PAGE 85
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
life cycle. Assessment reports document assessment results in sufficient detail, as deemed
necessary by organizations, to determine the accuracy and completeness of the reports and
whether the controls are implemented correctly, operating as intended, and producing the
desired outcome with respect to meeting requirements. Assessment results are provided to the
individuals or roles appropriate for the types of assessments being conducted. For example,
assessments conducted in support of authorization decisions are provided to authorizing
officials, senior agency officials for privacy, senior agency information security officers, and
authorizing official designated representatives.
To satisfy annual assessment requirements, organizations can use assessment results from the
following sources: initial or ongoing system authorizations, continuous monitoring, systems
engineering processes, or system development life cycle activities. Organizations ensure that
assessment results are current, relevant to the determination of control effectiveness, and
obtained with the appropriate level of assessor independence. Existing control assessment
results can be reused to the extent that the results are still valid and can also be supplemented
with additional assessments as needed. After the initial authorizations, organizations assess
controls during continuous monitoring. Organizations also establish the frequency for ongoing
assessments in accordance with organizational continuous monitoring strategies. External audits,
including audits by external entities such as regulatory agencies, are outside of the scope of CA-2
.
Related Controls:  AC-20, CA-5, CA-6, CA-7, PM-9, RA-5, RA-10, SA-11, SC-38, SI-3, SI-12, SR-2, SR-
3.
Control Enhancements:
(1) CONTROL ASSESSMENTS | INDEPENDENT ASSESSORS
Employ independent assessors or assessment teams to conduct control assessments.
Discussion:  Independent assessors or assessment teams are individuals or groups who
conduct impartial assessments of systems. Impartiality means that assessors are free from
any perceived or actual conflicts of interest regarding the development, operation,
sustainment, or management of the systems under assessment or the determination of
control effectiveness. To achieve impartiality, assessors do not create a mutual or conflicting
interest with the organizations where the assessments are being conducted, assess their
own work, act as management or employees of the organizations they are serving, or place
themselves in positions of advocacy for the organizations acquiring their services.
Independent assessments can be obtained from elements within organizations or be
contracted to public or private sector entities outside of organizations. Authorizing officials
determine the required level of independence based on the security categories of systems
and/or the risk to organizational operations, organizational assets, or individuals. Authorizing
officials also determine if the level of assessor independence provides sufficient assurance
that the results are sound and can be used to make credible, risk-based decisions. Assessor
independence determination includes whether contracted assessment services have
sufficient independence, such as when system owners are not directly involved in
contracting processes or cannot influence the impartiality of the assessors conducting the
assessments. During the system design and development phase, having independent
assessors is analogous to having independent SMEs involved in design reviews.
When organizations that own the systems are small or the structures of the organizations
require that assessments be conducted by individuals that are in the developmental,
operational, or management chain of the system owners, independence in assessment
processes can be achieved by ensuring that assessment results are carefully reviewed and
analyzed by independent teams of experts to validate the completeness, accuracy, integrity,
and reliability of the results. Assessments performed for purposes other than to support
CHAPTER THREE   PAGE 86
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
authorization decisions are more likely to be useable for such decisions when performed by
assessors with sufficient independence, thereby reducing the need to repeat assessments.
Related Controls:  None.
(2) CONTROL ASSESSMENTS | SPECIALIZED ASSESSMENTS
Include as part of control assessments, [Assignment: organization-defined frequency],
[Selection: announced; unannounced], [Selection (one or more): in-depth monitoring;
security instrumentation; automated security test cases; vulnerability scanning; malicious
user testing; insider threat assessment; performance and load testing; data leakage or
data loss assessment; [Assignment: organization-defined other forms of assessment]].
Discussion:  Organizations can conduct specialized assessments, including verification and
validation, system monitoring, insider threat assessments, malicious user testing, and other
forms of testing. These assessments can improve readiness by exercising organizational
capabilities and indicating current levels of performance as a means of focusing actions to
improve security and privacy. Organizations conduct specialized assessments in accordance
with applicable laws, executive orders, directives, regulations, policies, standards, and
guidelines. Authorizing officials approve the assessment methods in coordination with the
organizational risk executive function. Organizations can include vulnerabilities uncovered
during assessments into vulnerability remediation processes. Specialized assessments can
also be conducted early in the system development life cycle (e.g., during initial design,
development, and unit testing).
Related Controls:  PE-3, SI-2.
(3) CONTROL ASSESSMENTS | LEVERAGING RESULTS FROM EXTERNAL ORGANIZATIONS
Leverage the results of control assessments performed by [Assignment: organization-
defined external organization] on [Assignment: organization-defined system] when the
assessment meets [Assignment: organization-defined requirements].
Discussion:  Organizations may rely on control assessments of organizational systems by
other (external) organizations. Using such assessments and reusing existing assessment
evidence can decrease the time and resources required for assessments by limiting the
independent assessment activities that organizations need to perform. The factors that
organizations consider in determining whether to accept assessment results from external
organizations can vary. Such factors include the organization’s past experience with the
organization that conducted the assessment, the reputation of the assessment organization,
the level of detail of supporting assessment evidence provided, and mandates imposed by
applicable laws, executive orders, directives, regulations, policies, standards, and guidelines.
Accredited testing laboratories that support the Common Criteria Program [
ISO 15408-1],
the NIST Cryptographic Module Validation Program (CMVP), or the NIST Cryptographic
Algorithm Validation Program (CAVP) can provide independent assessment results that
organizations can leverage.
Related Controls:  SA-4.
References:  [OMB A-130], [FIPS 199], [SP 800-18], [SP 800-37], [SP 800-39], [SP 800-53A], [SP
800-115], [SP 800-137], [IR 8011-1], [IR 8062].
