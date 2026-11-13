---
schema_version: 1
corpus: federal-reference
jurisdiction: us
id: nist-sp-800-53-r5.ra-5
title: NIST SP 800-53 Rev. 5 RA-5 — VULNERABILITY MONITORING AND SCANNING
doc_type: federal_instrument
citation: NIST SP 800-53 Rev. 5 RA-5
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

**NIST SP 800-53 Rev. 5 RA-5** — VULNERABILITY MONITORING AND SCANNING

- Issued by: National Institute of Standards and Technology
- Publication: NIST SP 800-53 Rev. 5 — Security and Privacy Controls for Information Systems and Organizations ([nist-sp-800-53-r5](./nist-sp-800-53-r5.md))
- Version: Rev. 5 (September 2020, includes updates as of 2020-12-10)
- Text as of: 2026-11-12
- Cited by held documents: 28 times (cjis-sp-6-1 ×21, irs-pub-1075-11-2021 ×4, arc-ampe ×2, 6-cfr-37 ×1)
- Reproduction basis: 17 U.S.C. § 105 — work of the U.S. government (NIST). Determined per document on 2026-11-12 against the publication itself, not assumed from its issuer: its Authority statement (PDF page 3) reads "This publication may be used by nongovernmental organizations on a voluntary basis and is not subject to copyright in the United States. Attribution would, however, be appreciated by NIST." Held here: the front matter and Chapter Three (the control catalog) only. Chapter Three names ISO/IEC standards solely as bibliographic references and reproduces none of their text. NOT mirrored: the References bibliography and Appendices A-C; Appendix A (glossary) adapts third-party definitions (ISO/IEC 15026, ISO 25237, ISO/IEC 29100, ISO 15288, IETF RFC 4949), which ADR-0002 treats as not reproducible by being incorporated, and whose reproducibility has not been determined.


_NON-AUTHORITATIVE copy of one control, cut from the SP 800-53 Rev. 5 snapshot this corpus holds. Whether and how this binds a given agency depends on the instrument that incorporates it — read it at the source URL before relying on it. This copy is the Rev. 5 text of record, which is not necessarily the text a citing document meant (a document citing Rev. 4 is not answered by it)._


## Full text

### RA-5 VULNERABILITY MONITORING AND SCANNING
Control:
a. Monitor and scan for vulnerabilities in the system and hosted applications [Assignment:
organization-defined frequency and/or randomly in accordance with organization-defined
process] and when new vulnerabilities potentially affecting the system are identified and
reported;
b. Employ vulnerability monitoring tools and techniques that facilitate interoperability among
tools and automate parts of the vulnerability management process by using standards for:
1. Enumerating platforms, software flaws, and improper configurations;
2. Formatting checklists and test procedures; and
3. Measuring vulnerability impact;
c. Analyze vulnerability scan reports and results from vulnerability monitoring;
d. Remediate legitimate vulnerabilities [Assignment: organization-defined response times] in
accordance with an organizational assessment of risk;
e. Share information obtained from the vulnerability monitoring process and control
assessments with [Assignment: organization-defined personnel or roles] to help eliminate
similar vulnerabilities in other systems; and
f. Employ vulnerability monitoring tools that include the capability to readily update the
vulnerabilities to be scanned.
Discussion:  Security categorization of information and systems guides the frequency and
comprehensiveness of vulnerability monitoring (including scans). Organizations determine the
required vulnerability monitoring for system components, ensuring that the potential sources of
vulnerabilities—such as infrastructure components (e.g., switches, routers, guards, sensors),
networked printers, scanners, and copiers—are not overlooked. The capability to readily update
vulnerability monitoring tools as new vulnerabilities are discovered and announced and as new
scanning methods are developed helps to ensure that new vulnerabilities are not missed by
employed vulnerability monitoring tools. The vulnerability monitoring tool update process helps
to ensure that potential vulnerabilities in the system are identified and addressed as quickly as
possible. Vulnerability monitoring and analyses for custom software may require additional
approaches, such as static analysis, dynamic analysis, binary analysis, or a hybrid of the three
approaches. Organizations can use these analysis approaches in source code reviews and in a
variety of tools, including web-based application scanners, static analysis tools, and binary
analyzers.
Vulnerability monitoring includes scanning for patch levels; scanning for functions, ports,
protocols, and services that should not be accessible to users or devices; and scanning for flow
control mechanisms that are improperly configured or operating incorrectly. Vulnerability
CHAPTER THREE   PAGE 243
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
monitoring may also include continuous vulnerability monitoring tools that use instrumentation
to continuously analyze components. Instrumentation-based tools may improve accuracy and
may be run throughout an organization without scanning. Vulnerability monitoring tools that
facilitate interoperability include tools that are Security Content Automated Protocol (SCAP)-
validated. Thus, organizations consider using scanning tools that express vulnerabilities in the
Common Vulnerabilities and Exposures (CVE) naming convention and that employ the Open
Vulnerability Assessment Language (OVAL) to determine the presence of vulnerabilities. Sources
for vulnerability information include the Common Weakness Enumeration (CWE) listing and the
National Vulnerability Database (NVD). Control assessments, such as red team exercises, provide
additional sources of potential vulnerabilities for which to scan. Organizations also consider using
scanning tools that express vulnerability impact by the Common Vulnerability Scoring System
(CVSS).
Vulnerability monitoring includes a channel and process for receiving reports of security
vulnerabilities from the public at-large. Vulnerability disclosure programs can be as simple as
publishing a monitored email address or web form that can receive reports, including notification
authorizing good-faith research and disclosure of security vulnerabilities. Organizations generally
expect that such research is happening with or without their authorization and can use public
vulnerability disclosure channels to increase the likelihood that discovered vulnerabilities are
reported directly to the organization for remediation.
Organizations may also employ the use of financial incentives (also known as “bug bounties”) to
further encourage external security researchers to report discovered vulnerabilities. Bug bounty
programs can be tailored to the organization’s needs. Bounties can be operated indefinitely or
over a defined period of time and can be offered to the general public or to a curated group.
Organizations may run public and private bounties simultaneously and could choose to offer
partially credentialed access to certain participants in order to evaluate security vulnerabilities
from privileged vantage points.
Related Controls:  CA-2, CA-7, CA-8, CM-2, CM-4, CM-6, CM-8, RA-2, RA-3, SA-11, SA-15, SC-38
,
SI-2, SI-3, SI-4, SI-7, SR-11.
Control Enhancements:
(1) VULNERABILITY MONITORING AND SCANNING | UPDATE TOOL CAPABILITY
[Withdrawn: Incorporated into RA-5.]
(2) VULNERABILITY MONITORING AND SCANNING | UPDATE VULNERABILITIES TO BE SCANNED
Update the system vulnerabilities to be scanned [Selection (one or more): [Assignment:
organization-defined frequency]; prior to a new scan; when new vulnerabilities are
identified and reported].
Discussion:  Due to the complexity of modern software, systems, and other factors, new
vulnerabilities are discovered on a regular basis. It is important that newly discovered
vulnerabilities are added to the list of vulnerabilities to be scanned to ensure that the
organization can take steps to mitigate those vulnerabilities in a timely manner.
Related Controls:  SI-5.
(3) VULNERABILITY MONITORING AND SCANNING | BREADTH AND DEPTH OF COVERAGE
Define the breadth and depth of vulnerability scanning coverage.
Discussion:  The breadth of vulnerability scanning coverage can be expressed as a
percentage of components within the system, by the particular types of systems, by the
criticality of systems, or by the number of vulnerabilities to be checked. Conversely, the
depth of vulnerability scanning coverage can be expressed as the level of the system design
that the organization intends to monitor (e.g., component, module, subsystem, element).
CHAPTER THREE   PAGE 244
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
Organizations can determine the sufficiency of vulnerability scanning coverage with regard
to its risk tolerance and other factors. Scanning tools and how the tools are configured may
affect the depth and coverage. Multiple scanning tools may be needed to achieve the
desired depth and coverage. [SP 800-53A] provides additional information on the breadth
and depth of coverage.
Related Controls:  None.
(4) VULNERABILITY MONITORING AND SCANNING | DISCOVERABLE INFORMATION
Determine information about the system that is discoverable and take [Assignment:
organization-defined corrective actions].
Discussion:  Discoverable information includes information that adversaries could obtain
without compromising or breaching the system, such as by collecting information that the
system is exposing or by conducting extensive web searches. Corrective actions include
notifying appropriate organizational personnel, removing designated information, or
changing the system to make the designated information less relevant or attractive to
adversaries. This enhancement excludes intentionally discoverable information that may be
part of a decoy capability (e.g., honeypots, honeynets, or deception nets) deployed by the
organization.
Related Controls:  AU-13, SC-26.
(5) VULNERABILITY MONITORING AND SCANNING | PRIVILEGED ACCESS
Implement privileged access authorization to [Assignment: organization-defined system
components] for [Assignment: organization-defined vulnerability scanning activities].
Discussion:  In certain situations, the nature of the vulnerability scanning may be more
intrusive, or the system component that is the subject of the scanning may contain classified
or controlled unclassified information, such as personally identifiable information. Privileged
access authorization to selected system components facilitates more thorough vulnerability
scanning and protects the sensitive nature of such scanning.
Related Controls:  None.
(6) VULNERABILITY MONITORING AND SCANNING | AUTOMATED TREND ANALYSES
Compare the results of multiple vulnerability scans using [Assignment: organization-
defined automated mechanisms].
Discussion:  Using automated mechanisms to analyze multiple vulnerability scans over time
can help determine trends in system vulnerabilities and identify patterns of attack.
Related Controls:  None.
(7) VULNERABILITY MONITORING AND SCANNING | AUTOMATED DETECTION AND NOTIFICATION OF
UNAUTHORIZED COMPONENTS
[Withdrawn: Incorporated into CM-8.]
(8) VULNERABILITY MONITORING AND SCANNING | REVIEW HISTORIC AUDIT LOGS
Review historic audit logs to determine if a vulnerability identified in a [Assignment:
organization-defined system] has been previously exploited within an [Assignment:
organization-defined time period].
Discussion:  Reviewing historic audit logs to determine if a recently detected vulnerability in
a system has been previously exploited by an adversary can provide important information
for forensic analyses. Such analyses can help identify, for example, the extent of a previous
intrusion, the trade craft employed during the attack, organizational information exfiltrated
or modified, mission or business capabilities affected, and the duration of the attack.
Related Controls:  AU-6, AU-11.
CHAPTER THREE   PAGE 245
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
(9) VULNERABILITY MONITORING AND SCANNING | PENETRATION TESTING AND ANALYSES
[Withdrawn: Incorporated into CA-8.]
(10) VULNERABILITY MONITORING AND SCANNING | CORRELATE SCANNING INFORMATION
Correlate the output from vulnerability scanning tools to determine the presence of multi-
vulnerability and multi-hop attack vectors.
Discussion:  An attack vector is a path or means by which an adversary can gain access to a
system in order to deliver malicious code or exfiltrate information. Organizations can use
attack trees to show how hostile activities by adversaries interact and combine to produce
adverse impacts or negative consequences to systems and organizations. Such information,
together with correlated data from vulnerability scanning tools, can provide greater clarity
regarding multi-vulnerability and multi-hop attack vectors. The correlation of vulnerability
scanning information is especially important when organizations are transitioning from older
technologies to newer technologies (e.g., transitioning from IPv4 to IPv6 network protocols).
During such transitions, some system components may inadvertently be unmanaged and
create opportunities for adversary exploitation.
Related Controls:  None.
(11) VULNERABILITY MONITORING AND SCANNING | PUBLIC DISCLOSURE PROGRAM
Establish a public reporting channel for receiving reports of vulnerabilities in
organizational systems and system components.
Discussion:  The reporting channel is publicly discoverable and contains clear language
authorizing good-faith research and the disclosure of vulnerabilities to the organization. The
organization does not condition its authorization on an expectation of indefinite non-
disclosure to the public by the reporting entity but may request a specific time period to
properly remediate the vulnerability.
Related Controls:  None.
References:  [ISO 29147], [SP 800-40], [SP 800-53A], [SP 800-70], [SP 800-115], [SP 800-126], [IR
7788], [IR 8011-4], [IR 8023].
