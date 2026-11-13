---
schema_version: 1
corpus: federal-reference
jurisdiction: us
id: nist-sp-800-53-r5.si-4
title: NIST SP 800-53 Rev. 5 SI-4 — SYSTEM MONITORING
doc_type: federal_instrument
citation: NIST SP 800-53 Rev. 5 SI-4
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

**NIST SP 800-53 Rev. 5 SI-4** — SYSTEM MONITORING

- Issued by: National Institute of Standards and Technology
- Publication: NIST SP 800-53 Rev. 5 — Security and Privacy Controls for Information Systems and Organizations ([nist-sp-800-53-r5](./nist-sp-800-53-r5.md))
- Version: Rev. 5 (September 2020, includes updates as of 2020-12-10)
- Text as of: 2026-11-12
- Cited by held documents: 59 times (cjis-sp-6-1 ×40, arc-ampe ×10, irs-pub-1075-11-2021 ×5, 6-cfr-37 ×4), 2 of them naming an enhancement of this control
- Reproduction basis: 17 U.S.C. § 105 — work of the U.S. government (NIST). Determined per document on 2026-11-12 against the publication itself, not assumed from its issuer: its Authority statement (PDF page 3) reads "This publication may be used by nongovernmental organizations on a voluntary basis and is not subject to copyright in the United States. Attribution would, however, be appreciated by NIST." Held here: the front matter and Chapter Three (the control catalog) only. Chapter Three names ISO/IEC standards solely as bibliographic references and reproduces none of their text. NOT mirrored: the References bibliography and Appendices A-C; Appendix A (glossary) adapts third-party definitions (ISO/IEC 15026, ISO 25237, ISO/IEC 29100, ISO 15288, IETF RFC 4949), which ADR-0002 treats as not reproducible by being incorporated, and whose reproducibility has not been determined.


_NON-AUTHORITATIVE copy of one control, cut from the SP 800-53 Rev. 5 snapshot this corpus holds. Whether and how this binds a given agency depends on the instrument that incorporates it — read it at the source URL before relying on it. This copy is the Rev. 5 text of record, which is not necessarily the text a citing document meant (a document citing Rev. 4 is not answered by it)._


## Full text

### SI-4 SYSTEM MONITORING
Control:
CHAPTER THREE   PAGE 337
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
a. Monitor the system to detect:
1. Attacks and indicators of potential attacks in accordance with the following monitoring
objectives: [Assignment: organization-defined monitoring objectives]; and
2. Unauthorized local, network, and remote connections;
b. Identify unauthorized use of the system through the following techniques and methods:
[Assignment: organization-defined techniques and methods];
c. Invoke internal monitoring capabilities or deploy monitoring devices:
1. Strategically within the system to collect organization-determined essential information;
and
2. At ad hoc locations within the system to track specific types of transactions of interest
to the organization;
d. Analyze detected events and anomalies;
e. Adjust the level of system monitoring activity when there is a change in risk to organizational
operations and assets, individuals, other organizations, or the Nation;
f. Obtain legal opinion regarding system monitoring activities; and
g. Provide [Assignment: organization-defined system monitoring information] to [Assignment:
organization-defined personnel or roles] [Selection (one or more): as needed; [Assignment:
organization-defined frequency]].
Discussion:  System monitoring includes external and internal monitoring. External monitoring
includes the observation of events occurring at external interfaces to the system. Internal
monitoring includes the observation of events occurring within the system. Organizations
monitor systems by observing audit activities in real time or by observing other system aspects
such as access patterns, characteristics of access, and other actions. The monitoring objectives
guide and inform the determination of the events. System monitoring capabilities are achieved
through a variety of tools and techniques, including intrusion detection and prevention systems,
malicious code protection software, scanning tools, audit record monitoring software, and
network monitoring software.
Depending on the security architecture, the distribution and configuration of monitoring devices
may impact throughput at key internal and external boundaries as well as at other locations
across a network due to the introduction of network throughput latency. If throughput
management is needed, such devices are strategically located and deployed as part of an
established organization-wide security architecture. Strategic locations for monitoring devices
include selected perimeter locations and near key servers and server farms that support critical
applications. Monitoring devices are typically employed at the managed interfaces associated
with controls SC-7 and AC-17. The information collected is a function of the organizational
monitoring objectives and the capability of systems to support such objectives. Specific types of
transactions of interest include Hypertext Transfer Protocol (HTTP) traffic that bypasses HTTP
proxies. System monitoring is an integral part of organizational continuous monitoring and
incident response programs, and output from system monitoring serves as input to those
programs. System monitoring requirements, including the need for specific types of system
monitoring, may be referenced in other controls (e.g., AC-2g, AC-2(7), AC-2(12)(a), AC-17(1), AU-
13, AU-13(1), AU-13(2), CM-3f, CM-6d, MA-3a, MA-4a, SC-5(3)(b), SC-7a, SC-7(24)(b), SC-18b, SC-
43b). Adjustments to levels of system monitoring are based on law enforcement information,
intelligence information, or other sources of information. The legality of system monitoring
activities is based on applicable laws, executive orders, directives, regulations, policies,
standards, and guidelines.
CHAPTER THREE   PAGE 338
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
Related Controls:  AC-2, AC-3, AC-4, AC-8, AC-17, AU-2, AU-6, AU-7, AU-9, AU-12, AU-13, AU-14,
CA-7, CM-3, CM-6, CM-8, CM-11, IA-10, IR-4, MA-3, MA-4, PL-9, PM-12, RA-5, RA-10, SC-5, SC-7,
SC-18, SC-26, SC-31, SC-35, SC-36, SC-37, SC-43, SI-3, SI-6, SI-7, SR-9, SR-10.
Control Enhancements:
(1) SYSTEM MONITORING | SYSTEM-WIDE INTRUSION DETECTION SYSTEM
Connect and configure individual intrusion detection tools into a system-wide intrusion
detection system.
Discussion:  Linking individual intrusion detection tools into a system-wide intrusion
detection system provides additional coverage and effective detection capabilities. The
information contained in one intrusion detection tool can be shared widely across the
organization, making the system-wide detection capability more robust and powerful.
Related Controls:  None.
(2) SYSTEM MONITORING | AUTOMATED TOOLS AND MECHANISMS FOR REAL-TIME ANALYSIS
Employ automated tools and mechanisms to support near real-time analysis of events.
Discussion:  Automated tools and mechanisms include host-based, network-based,
transport-based, or storage-based event monitoring tools and mechanisms or security
information and event management (SIEM) technologies that provide real-time analysis of
alerts and notifications generated by organizational systems. Automated monitoring
techniques can create unintended privacy risks because automated controls may connect to
external or otherwise unrelated systems. The matching of records between these systems
may create linkages with unintended consequences. Organizations assess and document
these risks in their privacy impact assessment and make determinations that are in
alignment with their privacy program plan.
Related Controls:  PM-23, PM-25.
(3) SYSTEM MONITORING | AUTOMATED TOOL AND MECHANISM INTEGRATION
Employ automated tools and mechanisms to integrate intrusion detection tools and
mechanisms into access control and flow control mechanisms.
Discussion:  Using automated tools and mechanisms to integrate intrusion detection tools
and mechanisms into access and flow control mechanisms facilitates a rapid response to
attacks by enabling the reconfiguration of mechanisms in support of attack isolation and
elimination.
Related Controls:  PM-23, PM-25.
(4) SYSTEM MONITORING | INBOUND AND OUTBOUND COMMUNICATIONS TRAFFIC
(a) Determine criteria for unusual or unauthorized activities or conditions for inbound
and outbound communications traffic;
(b) Monitor inbound and outbound communications traffic [Assignment: organization-
defined frequency] for [Assignment: organization-defined unusual or unauthorized
activities or conditions].
Discussion:  Unusual or unauthorized activities or conditions related to system inbound and
outbound communications traffic includes internal traffic that indicates the presence of
malicious code or unauthorized use of legitimate code or credentials within organizational
systems or propagating among system components, signaling to external systems, and the
unauthorized exporting of information. Evidence of malicious code or unauthorized use of
legitimate code or credentials is used to identify potentially compromised systems or system
components.
Related Controls:  None.
CHAPTER THREE   PAGE 339
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
(5) SYSTEM MONITORING | SYSTEM-GENERATED ALERTS
Alert [Assignment: organization-defined personnel or roles] when the following system-
generated indications of compromise or potential compromise occur: [Assignment:
organization-defined compromise indicators].
Discussion:  Alerts may be generated from a variety of sources, including audit records or
inputs from malicious code protection mechanisms, intrusion detection or prevention
mechanisms, or boundary protection devices such as firewalls, gateways, and routers. Alerts
can be automated and may be transmitted telephonically, by electronic mail messages, or by
text messaging. Organizational personnel on the alert notification list can include system
administrators, mission or business owners, system owners, information owners/stewards,
senior agency information security officers, senior agency officials for privacy, system
security officers, or privacy officers. In contrast to alerts generated by the system, alerts
generated by organizations in SI-4(12) focus on information sources external to the system,
such as suspicious activity reports and reports on potential insider threats.
Related Controls:  AU-4, AU-5, PE-6.
(6) SYSTEM MONITORING | RESTRICT NON-PRIVILEGED USERS
[Withdrawn: Incorporated into AC-6(10).]
(7) SYSTEM MONITORING | AUTOMATED RESPONSE TO SUSPICIOUS EVENTS
(a) Notify [Assignment: organization-defined incident response personnel (identified by
name and/or by role)] of detected suspicious events; and
(b) Take the following actions upon detection: [Assignment: organization-defined least-
disruptive actions to terminate suspicious events].
Discussion:  Least-disruptive actions include initiating requests for human responses.
Related Controls:  None.
(8) SYSTEM MONITORING | PROTECTION OF MONITORING INFORMATION
[Withdrawn: Incorporated into SI-4.]
(9) SYSTEM MONITORING | TESTING OF MONITORING TOOLS AND MECHANISMS
Test intrusion-monitoring tools and mechanisms [Assignment: organization-defined
frequency].
Discussion:  Testing intrusion-monitoring tools and mechanisms is necessary to ensure that
the tools and mechanisms are operating correctly and continue to satisfy the monitoring
objectives of organizations. The frequency and depth of testing depends on the types of
tools and mechanisms used by organizations and the methods of deployment.
Related Controls:  None.
(10) SYSTEM MONITORING | VISIBILITY OF ENCRYPTED COMMUNICATIONS
Make provisions so that [Assignment: organization-defined encrypted communications
traffic] is visible to [Assignment: organization-defined system monitoring tools and
mechanisms].
Discussion:  Organizations balance the need to encrypt communications traffic to protect
data confidentiality with the need to maintain visibility into such traffic from a monitoring
perspective. Organizations determine whether the visibility requirement applies to internal
encrypted traffic, encrypted traffic intended for external destinations, or a subset of the
traffic types.
Related Controls:  None.
(11) SYSTEM MONITORING | ANALYZE COMMUNICATIONS TRAFFIC ANOMALIES
CHAPTER THREE   PAGE 340
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
Analyze outbound communications traffic at the external interfaces to the system and
selected [Assignment: organization-defined interior points within the system] to discover
anomalies.
Discussion:  Organization-defined interior points include subnetworks and subsystems.
Anomalies within organizational systems include large file transfers, long-time persistent
connections, attempts to access information from unexpected locations, the use of unusual
protocols and ports, the use of unmonitored network protocols (e.g., IPv6 usage during IPv4
transition), and attempted communications with suspected malicious external addresses.
Related Controls:  None.
(12) SYSTEM MONITORING | AUTOMATED ORGANIZATION-GENERATED ALERTS
Alert [Assignment: organization-defined personnel or roles] using [Assignment:
organization-defined automated mechanisms] when the following indications of
inappropriate or unusual activities with security or privacy implications occur:
[Assignment: organization-defined activities that trigger alerts].
Discussion:  Organizational personnel on the system alert notification list include system
administrators, mission or business owners, system owners, senior agency information
security officer, senior agency official for privacy, system security officers, or privacy officers.
Automated organization-generated alerts are the security alerts generated by organizations
and transmitted using automated means. The sources for organization-generated alerts are
focused on other entities such as suspicious activity reports and reports on potential insider
threats. In contrast to alerts generated by the organization, alerts generated by the system
in SI-4(5) focus on information sources that are internal to the systems, such as audit
records.
Related Controls:  None.
(13) SYSTEM MONITORING | ANALYZE TRAFFIC AND EVENT PATTERNS
(a) Analyze communications traffic and event patterns for the system;
(b) Develop profiles representing common traffic and event patterns; and
(c) Use the traffic and event profiles in tuning system-monitoring devices.
Discussion:  Identifying and understanding common communications traffic and event
patterns help organizations provide useful information to system monitoring devices to
more effectively identify suspicious or anomalous traffic and events when they occur. Such
information can help reduce the number of false positives and false negatives during system
monitoring.
Related Controls:  None.
(14) SYSTEM MONITORING | WIRELESS INTRUSION DETECTION
Employ a wireless intrusion detection system to identify rogue wireless devices and to
detect attack attempts and potential compromises or breaches to the system.
Discussion:  Wireless signals may radiate beyond organizational facilities. Organizations
proactively search for unauthorized wireless connections, including the conduct of thorough
scans for unauthorized wireless access points. Wireless scans are not limited to those areas
within facilities containing systems but also include areas outside of facilities to verify that
unauthorized wireless access points are not connected to organizational systems.
Related Controls:  AC-18, IA-3.
(15) SYSTEM MONITORING | WIRELESS TO WIRELINE COMMUNICATIONS
Employ an intrusion detection system to monitor wireless communications traffic as the
traffic passes from wireless to wireline networks.
CHAPTER THREE   PAGE 341
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
Discussion:  Wireless networks are inherently less secure than wired networks. For example,
wireless networks are more susceptible to eavesdroppers or traffic analysis than wireline
networks. When wireless to wireline communications exist, the wireless network could
become a port of entry into the wired network. Given the greater facility of unauthorized
network access via wireless access points compared to unauthorized wired network access
from within the physical boundaries of the system, additional monitoring of transitioning
traffic between wireless and wired networks may be necessary to detect malicious activities.
Employing intrusion detection systems to monitor wireless communications traffic helps to
ensure that the traffic does not contain malicious code prior to transitioning to the wireline
network.
Related Controls:  AC-18.
(16) SYSTEM MONITORING | CORRELATE MONITORING INFORMATION
Correlate information from monitoring tools and mechanisms employed throughout the
system.
Discussion:  Correlating information from different system monitoring tools and mechanisms
can provide a more comprehensive view of system activity. Correlating system monitoring
tools and mechanisms that typically work in isolation—including malicious code protection
software, host monitoring, and network monitoring—can provide an organization-wide
monitoring view and may reveal otherwise unseen attack patterns. Understanding the
capabilities and limitations of diverse monitoring tools and mechanisms and how to
maximize the use of information generated by those tools and mechanisms can help
organizations develop, operate, and maintain effective monitoring programs. The correlation
of monitoring information is especially important during the transition from older to newer
technologies (e.g., transitioning from IPv4 to IPv6 network protocols).
Related Controls:  AU-6.
(17) SYSTEM MONITORING | INTEGRATED SITUATIONAL AWARENESS
Correlate information from monitoring physical, cyber, and supply chain activities to
achieve integrated, organization-wide situational awareness.
Discussion:  Correlating monitoring information from a more diverse set of information
sources helps to achieve integrated situational awareness. Integrated situational awareness
from a combination of physical, cyber, and supply chain monitoring activities enhances the
capability of organizations to more quickly detect sophisticated attacks and investigate the
methods and techniques employed to carry out such attacks. In contrast to SI-4(16), which
correlates the various cyber monitoring information, integrated situational awareness is
intended to correlate monitoring beyond the cyber domain. Correlation of monitoring
information from multiple activities may help reveal attacks on organizations that are
operating across multiple attack vectors.
Related Controls:  AU-16, PE-6, SR-2, SR-4, SR-6.
(18) SYSTEM MONITORING | ANALYZE TRAFFIC AND COVERT EXFILTRATION
Analyze outbound communications traffic at external interfaces to the system and at the
following interior points to detect covert exfiltration of information: [Assignment:
organization-defined interior points within the system].
Discussion:  Organization-defined interior points include subnetworks and subsystems.
Covert means that can be used to exfiltrate information include steganography.
Related Controls:  None.
(19) SYSTEM MONITORING | RISK FOR INDIVIDUALS
CHAPTER THREE   PAGE 342
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
Implement [Assignment: organization-defined additional monitoring] of individuals who
have been identified by [Assignment: organization-defined sources] as posing an increased
level of risk.
Discussion:  Indications of increased risk from individuals can be obtained from different
sources, including personnel records, intelligence agencies, law enforcement organizations,
and other sources. The monitoring of individuals is coordinated with the management, legal,
security, privacy, and human resource officials who conduct such monitoring. Monitoring is
conducted in accordance with applicable laws, executive orders, directives, regulations,
policies, standards, and guidelines.
Related Controls:  None.
(20) SYSTEM MONITORING | PRIVILEGED USERS
Implement the following additional monitoring of privileged users: [Assignment:
organization-defined additional monitoring].
Discussion:  Privileged users have access to more sensitive information, including security-
related information, than the general user population. Access to such information means
that privileged users can potentially do greater damage to systems and organizations than
non-privileged users. Therefore, implementing additional monitoring on privileged users
helps to ensure that organizations can identify malicious activity at the earliest possible time
and take appropriate actions.
Related Controls:  AC-18.
(21) SYSTEM MONITORING | PROBATIONARY PERIODS
Implement the following additional monitoring of individuals during [Assignment:
organization-defined probationary period]: [Assignment: organization-defined additional
monitoring].
Discussion:  During probationary periods, employees do not have permanent employment
status within organizations. Without such status or access to information that is resident on
the system, additional monitoring can help identify any potentially malicious activity or
inappropriate behavior.
Related Controls:  AC-18.
(22) SYSTEM MONITORING | UNAUTHORIZED NETWORK SERVICES
(a) Detect network services that have not been authorized or approved by [Assignment:
organization-defined authorization or approval processes]; and
(b) [Selection (one or more): Audit; Alert [Assignment: organization-defined personnel or
roles]] when detected.
Discussion:  Unauthorized or unapproved network services include services in service-
oriented architectures that lack organizational verification or validation and may therefore
be unreliable or serve as malicious rogues for valid services.
Related Controls:  CM-7.
(23) SYSTEM MONITORING | HOST-BASED DEVICES
Implement the following host-based monitoring mechanisms at [Assignment:
organization-defined system components]: [Assignment: organization-defined host-based
monitoring mechanisms].
Discussion:  Host-based monitoring collects information about the host (or system in which it
resides). System components in which host-based monitoring can be implemented include
servers, notebook computers, and mobile devices. Organizations may consider employing
host-based monitoring mechanisms from multiple product developers or vendors.
Related Controls:  AC-18, AC-19.
CHAPTER THREE   PAGE 343
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
(24) SYSTEM MONITORING | INDICATORS OF COMPROMISE
Discover, collect, and distribute to [Assignment: organization-defined personnel or roles],
indicators of compromise provided by [Assignment: organization-defined sources].
Discussion:  Indicators of compromise (IOC) are forensic artifacts from intrusions that are
identified on organizational systems at the host or network level. IOCs provide valuable
information on systems that have been compromised. IOCs can include the creation of
registry key values. IOCs for network traffic include Universal Resource Locator or protocol
elements that indicate malicious code command and control servers. The rapid distribution
and adoption of IOCs can improve information security by reducing the time that systems
and organizations are vulnerable to the same exploit or attack. Threat indicators, signatures,
tactics, techniques, procedures, and other indicators of compromise may be available via
government and non-government cooperatives, including the Forum of Incident Response
and Security Teams, the United States Computer Emergency Readiness Team, the Defense
Industrial Base Cybersecurity Information Sharing Program, and the CERT Coordination
Center.
Related Controls:  AC-18.
(25) SYSTEM MONITORING | OPTIMIZE NETWORK TRAFFIC ANALYSIS
Provide visibility into network traffic at external and key internal system interfaces to
optimize the effectiveness of monitoring devices.
Discussion:  Encrypted traffic, asymmetric routing architectures, capacity and latency
limitations, and transitioning from older to newer technologies (e.g., IPv4 to IPv6 network
protocol transition) may result in blind spots for organizations when analyzing network
traffic. Collecting, decrypting, pre-processing, and distributing only relevant traffic to
monitoring devices can streamline the efficiency and use of devices and optimize traffic
analysis.
Related Controls:  None.
References:  [OMB A-130], [FIPS 140-3], [SP 800-61], [SP 800-83], [SP 800-92], [SP 800-94], [SP
800-137].
