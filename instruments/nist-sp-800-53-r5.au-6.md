---
schema_version: 1
corpus: federal-reference
jurisdiction: us
id: nist-sp-800-53-r5.au-6
title: NIST SP 800-53 Rev. 5 AU-6 — AUDIT RECORD REVIEW, ANALYSIS, AND REPORTING
doc_type: federal_instrument
citation: NIST SP 800-53 Rev. 5 AU-6
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

**NIST SP 800-53 Rev. 5 AU-6** — AUDIT RECORD REVIEW, ANALYSIS, AND REPORTING

- Issued by: National Institute of Standards and Technology
- Publication: NIST SP 800-53 Rev. 5 — Security and Privacy Controls for Information Systems and Organizations ([nist-sp-800-53-r5](./nist-sp-800-53-r5.md))
- Version: Rev. 5 (September 2020, includes updates as of 2020-12-10)
- Text as of: 2026-11-12
- Cited by held documents: 41 times (cjis-sp-6-1 ×33, irs-pub-1075-11-2021 ×4, 6-cfr-37 ×2, arc-ampe ×2), 1 of them naming an enhancement of this control
- Reproduction basis: 17 U.S.C. § 105 — work of the U.S. government (NIST). Determined per document on 2026-11-12 against the publication itself, not assumed from its issuer: its Authority statement (PDF page 3) reads "This publication may be used by nongovernmental organizations on a voluntary basis and is not subject to copyright in the United States. Attribution would, however, be appreciated by NIST." Held here: the front matter and Chapter Three (the control catalog) only. Chapter Three names ISO/IEC standards solely as bibliographic references and reproduces none of their text. NOT mirrored: the References bibliography and Appendices A-C; Appendix A (glossary) adapts third-party definitions (ISO/IEC 15026, ISO 25237, ISO/IEC 29100, ISO 15288, IETF RFC 4949), which ADR-0002 treats as not reproducible by being incorporated, and whose reproducibility has not been determined.


_NON-AUTHORITATIVE copy of one control, cut from the SP 800-53 Rev. 5 snapshot this corpus holds. Whether and how this binds a given agency depends on the instrument that incorporates it — read it at the source URL before relying on it. This copy is the Rev. 5 text of record, which is not necessarily the text a citing document meant (a document citing Rev. 4 is not answered by it)._


## Full text

### AU-6 AUDIT RECORD REVIEW, ANALYSIS, AND REPORTING
Control:
a. Review and analyze system audit records [Assignment: organization-defined frequency] for
indications of [Assignment: organization-defined inappropriate or unusual activity] and the
potential impact of the inappropriate or unusual activity;
b. Report findings to [Assignment: organization-defined personnel or roles]; and
c. Adjust the level of audit record review, analysis, and reporting within the system when there
is a change in risk based on law enforcement information, intelligence information, or other
credible sources of information.
Discussion:  Audit record review, analysis, and reporting covers information security- and privacy-
related logging performed by organizations, including logging that results from the monitoring of
account usage, remote access, wireless connectivity, mobile device connection, configuration
settings, system component inventory, use of maintenance tools and non-local maintenance,
physical access, temperature and humidity, equipment delivery and removal, communications at
system interfaces, and use of mobile code or Voice over Internet Protocol (VoIP). Findings can be
reported to organizational entities that include the incident response team, help desk, and
security or privacy offices. If organizations are prohibited from reviewing and analyzing audit
records or unable to conduct such activities, the review or analysis may be carried out by other
organizations granted such authority. The frequency, scope, and/or depth of the audit record
review, analysis, and reporting may be adjusted to meet organizational needs based on new
information received.
Related Controls:  AC-2, AC-3, AC-5, AC-6, AC-7, AC-17, AU-7, AU-16, CA-2, CA-7, CM-2, CM-5,
CM-6, CM-10, CM-11, IA-2, IA-3, IA-5, IA-8, IR-5, MA-4, MP-4, PE-3, PE-6, RA-5, SA-8, SC-7, SI-3,
SI-4, SI-7.
Control Enhancements:
(1) AUDIT RECORD REVIEW, ANALYSIS, AND REPORTING | AUTOMATED PROCESS INTEGRATION
Integrate audit record review, analysis, and reporting processes using [Assignment:
organization-defined automated mechanisms].
Discussion:  Organizational processes that benefit from integrated audit record review,
analysis, and reporting include incident response, continuous monitoring, contingency
planning, investigation and response to suspicious activities, and Inspector General audits.
CHAPTER THREE   PAGE 71
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
Related Controls:  PM-7.
(2) AUDIT RECORD REVIEW, ANALYSIS, AND REPORTING | AUTOMATED SECURITY ALERTS
[Withdrawn: Incorporated into SI-4.]
(3) AUDIT RECORD REVIEW, ANALYSIS, AND REPORTING | CORRELATE AUDIT RECORD REPOSITORIES
Analyze and correlate audit records across different repositories to gain organization-wide
situational awareness.
Discussion:  Organization-wide situational awareness includes awareness across all three
levels of risk management (i.e., organizational level, mission/business process level, and
information system level) and supports cross-organization awareness.
Related Controls:  AU-12, IR-4.
(4) AUDIT RECORD REVIEW, ANALYSIS, AND REPORTING | CENTRAL REVIEW AND ANALYSIS
Provide and implement the capability to centrally review and analyze audit records from
multiple components within the system.
Discussion:  Automated mechanisms for centralized reviews and analyses include Security
Information and Event Management products.
Related Controls:  AU-2, AU-12.
(5) AUDIT RECORD REVIEW, ANALYSIS, AND REPORTING | INTEGRATED ANALYSIS OF AUDIT RECORDS
Integrate analysis of audit records with analysis of [Selection (one or more): vulnerability
scanning information; performance data; system monitoring information; [Assignment:
organization-defined data/information collected from other sources]] to further enhance
the ability to identify inappropriate or unusual activity.
Discussion:  Integrated analysis of audit records does not require vulnerability scanning, the
generation of performance data, or system monitoring. Rather, integrated analysis requires
that the analysis of information generated by scanning, monitoring, or other data collection
activities is integrated with the analysis of audit record information. Security Information
and Event Management tools can facilitate audit record aggregation or consolidation from
multiple system components as well as audit record correlation and analysis. The use of
standardized audit record analysis scripts developed by organizations (with localized script
adjustments, as necessary) provides more cost-effective approaches for analyzing audit
record information collected. The correlation of audit record information with vulnerability
scanning information is important in determining the veracity of vulnerability scans of the
system and in correlating attack detection events with scanning results. Correlation with
performance data can uncover denial-of-service attacks or other types of attacks that result
in the unauthorized use of resources. Correlation with system monitoring information can
assist in uncovering attacks and in better relating audit information to operational situations.
Related Controls:  AU-12, IR-4.
(6) AUDIT RECORD REVIEW, ANALYSIS, AND REPORTING | CORRELATION WITH PHYSICAL MONITORING
Correlate information from audit records with information obtained from monitoring
physical access to further enhance the ability to identify suspicious, inappropriate,
unusual, or malevolent activity.
Discussion:  The correlation of physical audit record information and the audit records from
systems may assist organizations in identifying suspicious behavior or supporting evidence of
such behavior. For example, the correlation of an individual’s identity for logical access to
certain systems with the additional physical security information that the individual was
present at the facility when the logical access occurred may be useful in investigations.
Related Controls:  None.
CHAPTER THREE   PAGE 72
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
(7) AUDIT RECORD REVIEW, ANALYSIS, AND REPORTING | PERMITTED ACTIONS
Specify the permitted actions for each [Selection (one or more): system process; role; user]
associated with the review, analysis, and reporting of audit record information.
Discussion:  Organizations specify permitted actions for system processes, roles, and users
associated with the review, analysis, and reporting of audit records through system account
management activities. Specifying permitted actions on audit record information is a way to
enforce the principle of least privilege. Permitted actions are enforced by the system and
include read, write, execute, append, and delete.
Related Controls:  None.
(8) AUDIT RECORD REVIEW, ANALYSIS, AND REPORTING | FULL TEXT ANALYSIS OF PRIVILEGED
COMMANDS
Perform a full text analysis of logged privileged commands in a physically distinct
component or subsystem of the system, or other system that is dedicated to that analysis.
Discussion:  Full text analysis of privileged commands requires a distinct environment for the
analysis of audit record information related to privileged users without compromising such
information on the system where the users have elevated privileges, including the capability
to execute privileged commands. Full text analysis refers to analysis that considers the full
text of privileged commands (i.e., commands and parameters) as opposed to analysis that
considers only the name of the command. Full text analysis includes the use of pattern
matching and heuristics.
Related Controls:  AU-3, AU-9, AU-11, AU-12.
(9) AUDIT RECORD REVIEW, ANALYSIS, AND REPORTING | CORRELATION WITH INFORMATION FROM
NONTECHNICAL SOURCES
Correlate information from nontechnical sources with audit record information to enhance
organization-wide situational awareness.
Discussion:  Nontechnical sources include records that document organizational policy
violations related to harassment incidents and the improper use of information assets. Such
information can lead to a directed analytical effort to detect potential malicious insider
activity. Organizations limit access to information that is available from nontechnical sources
due to its sensitive nature. Limited access minimizes the potential for inadvertent release of
privacy-related information to individuals who do not have a need to know. The correlation
of information from nontechnical sources with audit record information generally occurs
only when individuals are suspected of being involved in an incident. Organizations obtain
legal advice prior to initiating such actions.
Related Controls:  PM-12.
(10) AUDIT RECORD REVIEW, ANALYSIS, AND REPORTING | AUDIT LEVEL ADJUSTMENT
[Withdrawn: Incorporated into AU-6.]
References:  [SP 800-86], [SP 800-101].
