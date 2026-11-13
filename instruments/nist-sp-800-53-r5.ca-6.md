---
schema_version: 1
corpus: federal-reference
jurisdiction: us
id: nist-sp-800-53-r5.ca-6
title: NIST SP 800-53 Rev. 5 CA-6 — AUTHORIZATION
doc_type: federal_instrument
citation: NIST SP 800-53 Rev. 5 CA-6
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

**NIST SP 800-53 Rev. 5 CA-6** — AUTHORIZATION

- Issued by: National Institute of Standards and Technology
- Publication: NIST SP 800-53 Rev. 5 — Security and Privacy Controls for Information Systems and Organizations ([nist-sp-800-53-r5](./nist-sp-800-53-r5.md))
- Version: Rev. 5 (September 2020, includes updates as of 2020-12-10)
- Text as of: 2026-11-12
- Cited by held documents: 15 times (cjis-sp-6-1 ×10, irs-pub-1075-11-2021 ×4, 6-cfr-37 ×1)
- Reproduction basis: 17 U.S.C. § 105 — work of the U.S. government (NIST). Determined per document on 2026-11-12 against the publication itself, not assumed from its issuer: its Authority statement (PDF page 3) reads "This publication may be used by nongovernmental organizations on a voluntary basis and is not subject to copyright in the United States. Attribution would, however, be appreciated by NIST." Held here: the front matter and Chapter Three (the control catalog) only. Chapter Three names ISO/IEC standards solely as bibliographic references and reproduces none of their text. NOT mirrored: the References bibliography and Appendices A-C; Appendix A (glossary) adapts third-party definitions (ISO/IEC 15026, ISO 25237, ISO/IEC 29100, ISO 15288, IETF RFC 4949), which ADR-0002 treats as not reproducible by being incorporated, and whose reproducibility has not been determined.


_NON-AUTHORITATIVE copy of one control, cut from the SP 800-53 Rev. 5 snapshot this corpus holds. Whether and how this binds a given agency depends on the instrument that incorporates it — read it at the source URL before relying on it. This copy is the Rev. 5 text of record, which is not necessarily the text a citing document meant (a document citing Rev. 4 is not answered by it)._


## Full text

### CA-6 AUTHORIZATION
Control:
a. Assign a senior official as the authorizing official for the system;
b. Assign a senior official as the authorizing official for common controls available for
inheritance by organizational systems;
c. Ensure that the authorizing official for the system, before commencing operations:
1. Accepts the use of common controls inherited by the system; and
2. Authorizes the system to operate;
d. Ensure that the authorizing official for common controls authorizes the use of those controls
for inheritance by organizational systems;
e. Update the authorizations [Assignment: organization-defined frequency].
Discussion:  Authorizations are official management decisions by senior officials to authorize
operation of systems, authorize the use of common controls for inheritance by organizational
systems, and explicitly accept the risk to organizational operations and assets, individuals, other
organizations, and the Nation based on the implementation of agreed-upon controls. Authorizing
officials provide budgetary oversight for organizational systems and common controls or assume
responsibility for the mission and business functions supported by those systems or common
controls. The authorization process is a federal responsibility, and therefore, authorizing officials
must be federal employees. Authorizing officials are both responsible and accountable for
security and privacy risks associated with the operation and use of organizational systems.
Nonfederal organizations may have similar processes to authorize systems and senior officials
that assume the authorization role and associated responsibilities.
Authorizing officials issue ongoing authorizations of systems based on evidence produced from
implemented continuous monitoring programs. Robust continuous monitoring programs reduce
the need for separate reauthorization processes. Through the employment of comprehensive
continuous monitoring processes, the information contained in authorization packages (i.e.,
security and privacy plans, assessment reports, and plans of action and milestones) is updated on
an ongoing basis. This provides authorizing officials, common control providers, and system
owners with an up-to-date status of the security and privacy posture of their systems, controls,
and operating environments. To reduce the cost of reauthorization, authorizing officials can
leverage the results of continuous monitoring processes to the maximum extent possible as the
basis for rendering reauthorization decisions.
CHAPTER THREE   PAGE 90
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
Related Controls:  CA-2, CA-3, CA-7, PM-9, PM-10, RA-3, SA-10, SI-12.
Control Enhancements:
(1) AUTHORIZATION | JOINT AUTHORIZATION — INTRA-ORGANIZATION
Employ a joint authorization process for the system that includes multiple authorizing
officials from the same organization conducting the authorization.
Discussion:  Assigning multiple authorizing officials from the same organization to serve as
co-authorizing officials for the system increases the level of independence in the risk-based
decision-making process. It also implements the concepts of separation of duties and dual
authorization as applied to the system authorization process. The intra-organization joint
authorization process is most relevant for connected systems, shared systems, and systems
with multiple information owners.
Related Controls:  AC-6.
(2) AUTHORIZATION | JOINT AUTHORIZATION — INTER-ORGANIZATION
Employ a joint authorization process for the system that includes multiple authorizing
officials with at least one authorizing official from an organization external to the
organization conducting the authorization.
Discussion:  Assigning multiple authorizing officials, at least one of whom comes from an
external organization, to serve as co-authorizing officials for the system increases the level of
independence in the risk-based decision-making process. It implements the concepts of
separation of duties and dual authorization as applied to the system authorization process.
Employing authorizing officials from external organizations to supplement the authorizing
official from the organization that owns or hosts the system may be necessary when the
external organizations have a vested interest or equities in the outcome of the authorization
decision. The inter-organization joint authorization process is relevant and appropriate for
connected systems, shared systems or services, and systems with multiple information
owners. The authorizing officials from the external organizations are key stakeholders of the
system undergoing authorization.
Related Controls:  AC-6.
References:  [OMB A-130], [SP 800-37], [SP 800-137].
