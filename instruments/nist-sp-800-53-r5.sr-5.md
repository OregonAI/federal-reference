---
schema_version: 1
corpus: federal-reference
jurisdiction: us
id: nist-sp-800-53-r5.sr-5
title: NIST SP 800-53 Rev. 5 SR-5 — ACQUISITION STRATEGIES, TOOLS, AND METHODS
doc_type: federal_instrument
citation: NIST SP 800-53 Rev. 5 SR-5
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

**NIST SP 800-53 Rev. 5 SR-5** — ACQUISITION STRATEGIES, TOOLS, AND METHODS

- Issued by: National Institute of Standards and Technology
- Publication: NIST SP 800-53 Rev. 5 — Security and Privacy Controls for Information Systems and Organizations ([nist-sp-800-53-r5](./nist-sp-800-53-r5.md))
- Version: Rev. 5 (September 2020, includes updates as of 2020-12-10)
- Text as of: 2026-11-12
- Cited by held documents: 19 times (cjis-sp-6-1 ×14, arc-ampe ×3, 6-cfr-37 ×2)
- Reproduction basis: 17 U.S.C. § 105 — work of the U.S. government (NIST). Determined per document on 2026-11-12 against the publication itself, not assumed from its issuer: its Authority statement (PDF page 3) reads "This publication may be used by nongovernmental organizations on a voluntary basis and is not subject to copyright in the United States. Attribution would, however, be appreciated by NIST." Held here: the front matter and Chapter Three (the control catalog) only. Chapter Three names ISO/IEC standards solely as bibliographic references and reproduces none of their text. NOT mirrored: the References bibliography and Appendices A-C; Appendix A (glossary) adapts third-party definitions (ISO/IEC 15026, ISO 25237, ISO/IEC 29100, ISO 15288, IETF RFC 4949), which ADR-0002 treats as not reproducible by being incorporated, and whose reproducibility has not been determined.


_NON-AUTHORITATIVE copy of one control, cut from the SP 800-53 Rev. 5 snapshot this corpus holds. Whether and how this binds a given agency depends on the instrument that incorporates it — read it at the source URL before relying on it. This copy is the Rev. 5 text of record, which is not necessarily the text a citing document meant (a document citing Rev. 4 is not answered by it)._


## Full text

### SR-5 ACQUISITION STRATEGIES, TOOLS, AND METHODS
Control:  Employ the following acquisition strategies, contract tools, and procurement methods
to protect against, identify, and mitigate supply chain risks: [Assignment: organization-defined
acquisition strategies, contract tools, and procurement methods].
Discussion:  The use of the acquisition process provides an important vehicle to protect the
supply chain. There are many useful tools and techniques available, including obscuring the end
use of a system or system component, using blind or filtered buys, requiring tamper-evident
packaging, or using trusted or controlled distribution. The results from a supply chain risk
assessment can guide and inform the strategies, tools, and methods that are most applicable to
the situation. Tools and techniques may provide protections against unauthorized production,
theft, tampering, insertion of counterfeits, insertion of malicious software or backdoors, and
poor development practices throughout the system development life cycle. Organizations also
CHAPTER THREE   PAGE 369
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
consider providing incentives for suppliers who implement controls, promote transparency into
their processes and security and privacy practices, provide contract language that addresses the
prohibition of tainted or counterfeit components, and restrict purchases from untrustworthy
suppliers. Organizations consider providing training, education, and awareness programs for
personnel regarding supply chain risk, available mitigation strategies, and when the programs
should be employed. Methods for reviewing and protecting development plans, documentation,
and evidence are commensurate with the security and privacy requirements of the organization.
Contracts may specify documentation protection requirements.
Related Controls:  AT-3, SA-2, SA-3, SA-4, SA-5, SA-8, SA-9, SA-10, SA-15, SR-6, SR-9, SR-10, SR-11.
Control Enhancements:
(1) ACQUISITION STRATEGIES, TOOLS, AND METHODS | ADEQUATE SUPPLY
Employ the following controls to ensure an adequate supply of [Assignment: organization-
defined critical system components]: [Assignment: organization-defined controls].
Discussion:  Adversaries can attempt to impede organizational operations by disrupting the
supply of critical system components or corrupting supplier operations. Organizations may
track systems and component mean time to failure to mitigate the loss of temporary or
permanent system function. Controls to ensure that adequate supplies of critical system
components include the use of multiple suppliers throughout the supply chain for the
identified critical components, stockpiling spare components to ensure operation during
mission-critical times, and the identification of functionally identical or similar components
that may be used, if necessary.
Related Controls:  RA-9.
(2) ACQUISITION STRATEGIES, TOOLS, AND METHODS | ASSESSMENTS PRIOR TO SELECTION,
ACCEPTANCE, MODIFICATION, OR UPDATE
Assess the system, system component, or system service prior to selection, acceptance,
modification, or update.
Discussion:  Organizational personnel or independent, external entities conduct assessments
of systems, components, products, tools, and services to uncover evidence of tampering,
unintentional and intentional vulnerabilities, or evidence of non-compliance with supply
chain controls. These include malicious code, malicious processes, defective software,
backdoors, and counterfeits. Assessments can include evaluations; design proposal reviews;
visual or physical inspection; static and dynamic analyses; visual, x-ray, or magnetic particle
inspections; simulations; white, gray, or black box testing; fuzz testing; stress testing; and
penetration testing (see
SR-6(1)). Evidence generated during assessments is documented for
follow-on actions by organizations. The evidence generated during the organizational or
independent assessments of supply chain elements may be used to improve supply chain
processes and inform the supply chain risk management process. The evidence can be
leveraged in follow-on assessments. Evidence and other documentation may be shared in
accordance with organizational agreements.
Related Controls:  CA-8, RA-5, SA-11, SI-7.
References:  [FASC18], [41 CFR 201], [EO 13873], [ISO 27036], [ISO 20243], [SP 800-30], [SP 800-
161], [IR 7622], [IR 8272].
