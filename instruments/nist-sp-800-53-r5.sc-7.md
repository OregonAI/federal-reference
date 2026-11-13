---
schema_version: 1
corpus: federal-reference
jurisdiction: us
id: nist-sp-800-53-r5.sc-7
title: NIST SP 800-53 Rev. 5 SC-7 — BOUNDARY PROTECTION
doc_type: federal_instrument
citation: NIST SP 800-53 Rev. 5 SC-7
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

**NIST SP 800-53 Rev. 5 SC-7** — BOUNDARY PROTECTION

- Issued by: National Institute of Standards and Technology
- Publication: NIST SP 800-53 Rev. 5 — Security and Privacy Controls for Information Systems and Organizations ([nist-sp-800-53-r5](./nist-sp-800-53-r5.md))
- Version: Rev. 5 (September 2020, includes updates as of 2020-12-10)
- Text as of: 2026-11-12
- Cited by held documents: 49 times (cjis-sp-6-1 ×36, arc-ampe ×6, irs-pub-1075-11-2021 ×5, 6-cfr-37 ×2), 1 of them naming an enhancement of this control
- Reproduction basis: 17 U.S.C. § 105 — work of the U.S. government (NIST). Determined per document on 2026-11-12 against the publication itself, not assumed from its issuer: its Authority statement (PDF page 3) reads "This publication may be used by nongovernmental organizations on a voluntary basis and is not subject to copyright in the United States. Attribution would, however, be appreciated by NIST." Held here: the front matter and Chapter Three (the control catalog) only. Chapter Three names ISO/IEC standards solely as bibliographic references and reproduces none of their text. NOT mirrored: the References bibliography and Appendices A-C; Appendix A (glossary) adapts third-party definitions (ISO/IEC 15026, ISO 25237, ISO/IEC 29100, ISO 15288, IETF RFC 4949), which ADR-0002 treats as not reproducible by being incorporated, and whose reproducibility has not been determined.


_NON-AUTHORITATIVE copy of one control, cut from the SP 800-53 Rev. 5 snapshot this corpus holds. Whether and how this binds a given agency depends on the instrument that incorporates it — read it at the source URL before relying on it. This copy is the Rev. 5 text of record, which is not necessarily the text a citing document meant (a document citing Rev. 4 is not answered by it)._


## Full text

### SC-7  BOUNDARY PROTECTION
Control:
a. Monitor and control communications at the external managed interfaces to the system and
at key internal managed interfaces within the system;
b. Implement subnetworks for publicly accessible system components that are [Selection:
physically; logically] separated from internal organizational networks; and
c. Connect to external networks or systems only through managed interfaces consisting of
boundary protection devices arranged in accordance with an organizational security and
privacy architecture.
Discussion:  Managed interfaces include gateways, routers, firewalls, guards, network-based
malicious code analysis, virtualization systems, or encrypted tunnels implemented within a
security architecture. Subnetworks that are physically or logically separated from internal
networks are referred to as demilitarized zones or DMZs. Restricting or prohibiting interfaces
within organizational systems includes restricting external web traffic to designated web servers
within managed interfaces, prohibiting external traffic that appears to be spoofing internal
addresses, and prohibiting internal traffic that appears to be spoofing external addresses. [SP
800-189] provides additional information on source address validation techniques to prevent
ingress and egress of traffic with spoofed addresses. Commercial telecommunications services
are provided by network components and consolidated management systems shared by
customers. These services may also include third party-provided access lines and other service
elements. Such services may represent sources of increased risk despite contract security
provisions. Boundary protection may be implemented as a common control for all or part of an
organizational network such that the boundary to be protected is greater than a system-specific
boundary (i.e., an authorization boundary).
CHAPTER THREE   PAGE 298
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
Related Controls:  AC-4, AC-17, AC-18, AC-19, AC-20, AU-13, CA-3, CM-2, CM-4, CM-7, CM-10, CP-
8, CP-10, IR-4, MA-4, PE-3, PL-8, PM-12, SA-8, SA-17, SC-5, SC-26, SC-32, SC-35, SC-43.
Control Enhancements:
(1) BOUNDARY PROTECTION | PHYSICALLY SEPARATED SUBNETWORKS
[Withdrawn: Incorporated into SC-7.]
(2) BOUNDARY PROTECTION | PUBLIC ACCESS
[Withdrawn: Incorporated into SC-7.]
(3) BOUNDARY PROTECTION | ACCESS POINTS
Limit the number of external network connections to the system.
Discussion:  Limiting the number of external network connections facilitates monitoring of
inbound and outbound communications traffic. The Trusted Internet Connection [DHS TIC]
initiative is an example of a federal guideline that requires limits on the number of external
network connections. Limiting the number of external network connections to the system is
important during transition periods from older to newer technologies (e.g., transitioning
from IPv4 to IPv6 network protocols). Such transitions may require implementing the older
and newer technologies simultaneously during the transition period and thus increase the
number of access points to the system.
Related Controls:  None.
(4) BOUNDARY PROTECTION | EXTERNAL TELECOMMUNICATIONS SERVICES
(a) Implement a managed interface for each external telecommunication service;
(b) Establish a traffic flow policy for each managed interface;
(c) Protect the confidentiality and integrity of the information being transmitted across
each interface;
(d) Document each exception to the traffic flow policy with a supporting mission or
business need and duration of that need;
(e) Review exceptions to the traffic flow policy [Assignment: organization-defined
frequency] and remove exceptions that are no longer supported by an explicit mission
or business need;
(f) Prevent unauthorized exchange of control plane traffic with external networks;
(g) Publish information to enable remote networks to detect unauthorized control plane
traffic from internal networks; and
(h) Filter unauthorized control plane traffic from external networks.
Discussion:  External telecommunications services can provide data and/or voice
communications services. Examples of control plane traffic include Border Gateway Protocol
(BGP) routing, Domain Name System (DNS), and management protocols. See [SP 800-189]
for additional information on the use of the resource public key infrastructure (RPKI) to
protect BGP routes and detect unauthorized BGP announcements.
Related Controls:  AC-3, SC-8, SC-20, SC-21, SC-22.
(5) BOUNDARY PROTECTION | DENY BY DEFAULT — ALLOW BY EXCEPTION
Deny network communications traffic by default and allow network communications
traffic by exception [Selection (one or more): at managed interfaces; for [Assignment:
organization-defined systems]].
Discussion:  Denying by default and allowing by exception applies to inbound and outbound
network communications traffic. A deny-all, permit-by-exception network communications
traffic policy ensures that only those system connections that are essential and approved are
CHAPTER THREE   PAGE 299
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
allowed. Deny by default, allow by exception also applies to a system that is connected to an
external system.
Related Controls:  None.
(6) BOUNDARY PROTECTION | RESPONSE TO RECOGNIZED FAILURES
[Withdrawn: Incorporated into SC-7(18).]
(7) BOUNDARY PROTECTION | SPLIT TUNNELING FOR REMOTE DEVICES
Prevent split tunneling for remote devices connecting to organizational systems unless the
split tunnel is securely provisioned using [Assignment: organization-defined safeguards].
Discussion:  Split tunneling is the process of allowing a remote user or device to establish a
non-remote connection with a system and simultaneously communicate via some other
connection to a resource in an external network. This method of network access enables a
user to access remote devices and simultaneously, access uncontrolled networks. Split
tunneling might be desirable by remote users to communicate with local system resources,
such as printers or file servers. However, split tunneling can facilitate unauthorized external
connections, making the system vulnerable to attack and to exfiltration of organizational
information. Split tunneling can be prevented by disabling configuration settings that allow
such capability in remote devices and by preventing those configuration settings from being
configurable by users. Prevention can also be achieved by the detection of split tunneling (or
of configuration settings that allow split tunneling) in the remote device, and by prohibiting
the connection if the remote device is using split tunneling. A virtual private network (VPN)
can be used to securely provision a split tunnel. A securely provisioned VPN includes locking
connectivity to exclusive, managed, and named environments, or to a specific set of pre-
approved addresses, without user control.
Related Controls:  None.
(8) BOUNDARY PROTECTION | ROUTE TRAFFIC TO AUTHENTICATED PROXY SERVERS
Route [Assignment: organization-defined internal communications traffic] to [Assignment:
organization-defined external networks] through authenticated proxy servers at managed
interfaces.
Discussion:  External networks are networks outside of organizational control. A proxy server
is a server (i.e., system or application) that acts as an intermediary for clients requesting
system resources from non-organizational or other organizational servers. System resources
that may be requested include files, connections, web pages, or services. Client requests
established through a connection to a proxy server are assessed to manage complexity and
provide additional protection by limiting direct connectivity. Web content filtering devices
are one of the most common proxy servers that provide access to the Internet. Proxy servers
can support the logging of Transmission Control Protocol sessions and the blocking of
specific Uniform Resource Locators, Internet Protocol addresses, and domain names. Web
proxies can be configured with organization-defined lists of authorized and unauthorized
websites. Note that proxy servers may inhibit the use of virtual private networks (VPNs) and
create the potential for “man-in-the-middle” attacks (depending on the implementation).
Related Controls:  AC-3.
(9) BOUNDARY PROTECTION | RESTRICT THREATENING OUTGOING COMMUNICATIONS TRAFFIC
(a) Detect and deny outgoing communications traffic posing a threat to external systems;
and
(b) Audit the identity of internal users associated with denied communications.
Discussion:  Detecting outgoing communications traffic from internal actions that may pose
threats to external systems is known as extrusion detection. Extrusion detection is carried
out within the system at managed interfaces. Extrusion detection includes the analysis of
CHAPTER THREE   PAGE 300
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
incoming and outgoing communications traffic while searching for indications of internal
threats to the security of external systems. Internal threats to external systems include
traffic indicative of denial-of-service attacks, traffic with spoofed source addresses, and
traffic that contains malicious code. Organizations have criteria to determine, update, and
manage identified threats related to extrusion detection.
Related Controls:  AU-2, AU-6, SC-5, SC-38, SC-44, SI-3, SI-4.
(10) BOUNDARY PROTECTION | PREVENT EXFILTRATION
(a) Prevent the exfiltration of information; and
(b) Conduct exfiltration tests [Assignment: organization-defined frequency].
Discussion:  Prevention of exfiltration applies to both the intentional and unintentional
exfiltration of information. Techniques used to prevent the exfiltration of information from
systems may be implemented at internal endpoints, external boundaries, and across
managed interfaces and include adherence to protocol formats, monitoring for beaconing
activity from systems, disconnecting external network interfaces except when explicitly
needed, employing traffic profile analysis to detect deviations from the volume and types of
traffic expected, call backs to command and control centers, conducting penetration testing,
monitoring for steganography, disassembling and reassembling packet headers, and using
data loss and data leakage prevention tools. Devices that enforce strict adherence to
protocol formats include deep packet inspection firewalls and Extensible Markup Language
(XML) gateways. The devices verify adherence to protocol formats and specifications at the
application layer and identify vulnerabilities that cannot be detected by devices that operate
at the network or transport layers. The prevention of exfiltration is similar to data loss
prevention or data leakage prevention and is closely associated with cross-domain solutions
and system guards that enforce information flow requirements.
Related Controls:  AC-2, CA-8, SI-3.
(11) BOUNDARY PROTECTION | RESTRICT INCOMING COMMUNICATIONS TRAFFIC
Only allow incoming communications from [Assignment: organization-defined authorized
sources] to be routed to [Assignment: organization-defined authorized destinations].
Discussion:  General source address validation techniques are applied to restrict the use of
illegal and unallocated source addresses as well as source addresses that should only be
used within the system. The restriction of incoming communications traffic provides
determinations that source and destination address pairs represent authorized or allowed
communications. Determinations can be based on several factors, including the presence of
such address pairs in the lists of authorized or allowed communications, the absence of such
address pairs in lists of unauthorized or disallowed pairs, or meeting more general rules for
authorized or allowed source and destination pairs. Strong authentication of network
addresses is not possible without the use of explicit security protocols, and thus, addresses
can often be spoofed. Further, identity-based incoming traffic restriction methods can be
employed, including router access control lists and firewall rules.
Related Controls:  AC-3.
(12) BOUNDARY PROTECTION | HOST-BASED PROTECTION
Implement [Assignment: organization-defined host-based boundary protection
mechanisms] at [Assignment: organization-defined system components].
Discussion:  Host-based boundary protection mechanisms include host-based firewalls.
System components that employ host-based boundary protection mechanisms include
servers, workstations, notebook computers, and mobile devices.
Related Controls:  None.
CHAPTER THREE   PAGE 301
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
(13) BOUNDARY PROTECTION | ISOLATION OF SECURITY TOOLS, MECHANISMS, AND SUPPORT
COMPONENTS
Isolate [Assignment: organization-defined information security tools, mechanisms, and
support components] from other internal system components by implementing physically
separate subnetworks with managed interfaces to other components of the system.
Discussion:  Physically separate subnetworks with managed interfaces are useful in isolating
computer network defenses from critical operational processing networks to prevent
adversaries from discovering the analysis and forensics techniques employed by
organizations.
Related Controls:  SC-2, SC-3.
(14) BOUNDARY PROTECTION | PROTECT AGAINST UNAUTHORIZED PHYSICAL CONNECTIONS
Protect against unauthorized physical connections at [Assignment: organization-defined
managed interfaces].
Discussion:  Systems that operate at different security categories or classification levels may
share common physical and environmental controls, since the systems may share space
within the same facilities. In practice, it is possible that these separate systems may share
common equipment rooms, wiring closets, and cable distribution paths. Protection against
unauthorized physical connections can be achieved by using clearly identified and physically
separated cable trays, connection frames, and patch panels for each side of managed
interfaces with physical access controls that enforce limited authorized access to these
items.
Related Controls:  PE-4, PE-19.
(15) BOUNDARY PROTECTION | NETWORKED PRIVILEGED ACCESSES
Route networked, privileged accesses through a dedicated, managed interface for
purposes of access control and auditing.
Discussion:  Privileged access provides greater accessibility to system functions, including
security functions. Adversaries attempt to gain privileged access to systems through remote
access to cause adverse mission or business impacts, such as by exfiltrating information or
bringing down a critical system capability. Routing networked, privileged access requests
through a dedicated, managed interface further restricts privileged access for increased
access control and auditing.
Related Controls:  AC-2, AC-3, AU-2, SI-4.
(16) BOUNDARY PROTECTION | PREVENT DISCOVERY OF SYSTEM COMPONENTS
Prevent the discovery of specific system components that represent a managed interface.
Discussion:  Preventing the discovery of system components representing a managed
interface helps protect network addresses of those components from discovery through
common tools and techniques used to identify devices on networks. Network addresses are
not available for discovery and require prior knowledge for access. Preventing the discovery
of components and devices can be accomplished by not publishing network addresses, using
network address translation, or not entering the addresses in domain name systems.
Another prevention technique is to periodically change network addresses.
Related Controls:  None.
(17) BOUNDARY PROTECTION | AUTOMATED ENFORCEMENT OF PROTOCOL FORMATS
Enforce adherence to protocol formats.
Discussion:  System components that enforce protocol formats include deep packet
inspection firewalls and XML gateways. The components verify adherence to protocol
CHAPTER THREE   PAGE 302
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
formats and specifications at the application layer and identify vulnerabilities that cannot be
detected by devices operating at the network or transport layers.
Related Controls:  SC-4.
(18) BOUNDARY PROTECTION | FAIL SECURE
Prevent systems from entering unsecure states in the event of an operational failure of a
boundary protection device.
Discussion:  Fail secure is a condition achieved by employing mechanisms to ensure that in
the event of operational failures of boundary protection devices at managed interfaces,
systems do not enter into unsecure states where intended security properties no longer
hold. Managed interfaces include routers, firewalls, and application gateways that reside on
protected subnetworks (commonly referred to as demilitarized zones). Failures of boundary
protection devices cannot lead to or cause information external to the devices to enter the
devices nor can failures permit unauthorized information releases.
Related Controls:  CP-2, CP-12, SC-24.
(19) BOUNDARY PROTECTION | BLOCK COMMUNICATION FROM NON-ORGANIZATIONALLY CONFIGURED
HOSTS
Block inbound and outbound communications traffic between [Assignment: organization-
defined communication clients] that are independently configured by end users and
external service providers.
Discussion:  Communication clients independently configured by end users and external
service providers include instant messaging clients and video conferencing software and
applications. Traffic blocking does not apply to communication clients that are configured by
organizations to perform authorized functions.
Related Controls:  None.
(20) BOUNDARY PROTECTION | DYNAMIC ISOLATION AND SEGREGATION
Provide the capability to dynamically isolate [Assignment: organization-defined system
components] from other system components.
Discussion:  The capability to dynamically isolate certain internal system components is
useful when it is necessary to partition or separate system components of questionable
origin from components that possess greater trustworthiness. Component isolation reduces
the attack surface of organizational systems. Isolating selected system components can also
limit the damage from successful attacks when such attacks occur.
Related Controls:  None.
(21) BOUNDARY PROTECTION | ISOLATION OF SYSTEM COMPONENTS
Employ boundary protection mechanisms to isolate [Assignment: organization-defined
system components] supporting [Assignment: organization-defined missions and/or
business functions].
Discussion:  Organizations can isolate system components that perform different mission or
business functions. Such isolation limits unauthorized information flows among system
components and provides the opportunity to deploy greater levels of protection for selected
system components. Isolating system components with boundary protection mechanisms
provides the capability for increased protection of individual system components and to
more effectively control information flows between those components. Isolating system
components provides enhanced protection that limits the potential harm from hostile cyber-
attacks and errors. The degree of isolation varies depending upon the mechanisms chosen.
Boundary protection mechanisms include routers, gateways, and firewalls that separate
system components into physically separate networks or subnetworks; cross-domain devices
CHAPTER THREE   PAGE 303
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
that separate subnetworks; virtualization techniques; and the encryption of information
flows among system components using distinct encryption keys.
Related Controls:  CA-9.
(22) BOUNDARY PROTECTION | SEPARATE SUBNETS FOR CONNECTING TO DIFFERENT SECURITY DOMAINS
Implement separate network addresses to connect to systems in different security
domains.
Discussion:  The decomposition of systems into subnetworks (i.e., subnets) helps to provide
the appropriate level of protection for network connections to different security domains
that contain information with different security categories or classification levels.
Related Controls:  None.
(23) BOUNDARY PROTECTION | DISABLE SENDER FEEDBACK ON PROTOCOL VALIDATION FAILURE
Disable feedback to senders on protocol format validation failure.
Discussion:  Disabling feedback to senders when there is a failure in protocol validation
format prevents adversaries from obtaining information that would otherwise be
unavailable.
Related Controls:  None.
(24) BOUNDARY PROTECTION | PERSONALLY IDENTIFIABLE INFORMATION
For systems that process personally identifiable information:
(a) Apply the following processing rules to data elements of personally identifiable
information: [Assignment: organization-defined processing rules];
(b) Monitor for permitted processing at the external interfaces to the system and at key
internal boundaries within the system;
(c) Document each processing exception; and
(d) Review and remove exceptions that are no longer supported.
Discussion:  Managing the processing of personally identifiable information is an important
aspect of protecting an individual’s privacy. Applying, monitoring for, and documenting
exceptions to processing rules ensure that personally identifiable information is processed
only in accordance with established privacy requirements.
Related Controls:  PT-2, SI-15.
(25) BOUNDARY PROTECTION | UNCLASSIFIED NATIONAL SECURITY SYSTEM CONNECTIONS
Prohibit the direct connection of [Assignment: organization-defined unclassified national
security system] to an external network without the use of [Assignment: organization-
defined boundary protection device].
Discussion:  A direct connection is a dedicated physical or virtual connection between two or
more systems. Organizations typically do not have complete control over external networks,
including the Internet. Boundary protection devices (e.g., firewalls, gateways, and routers)
mediate communications and information flows between unclassified national security
systems and external networks.
Related Controls:  None.
(26) BOUNDARY PROTECTION | CLASSIFIED NATIONAL SECURITY SYSTEM CONNECTIONS
Prohibit the direct connection of a classified national security system to an external
network without the use of [Assignment: organization-defined boundary protection
device].
Discussion:  A direct connection is a dedicated physical or virtual connection between two or
more systems. Organizations typically do not have complete control over external networks,
CHAPTER THREE   PAGE 304
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
including the Internet. Boundary protection devices (e.g., firewalls, gateways, and routers)
mediate communications and information flows between classified national security systems
and external networks. In addition, approved boundary protection devices (typically
managed interface or cross-domain systems) provide information flow enforcement from
systems to external networks.
Related Controls:  None.
(27) BOUNDARY PROTECTION | UNCLASSIFIED NON-NATIONAL SECURITY SYSTEM CONNECTIONS
Prohibit the direct connection of [Assignment: organization-defined unclassified non-
national security system] to an external network without the use of [Assignment:
organization-defined boundary protection device].
Discussion:  A direct connection is a dedicated physical or virtual connection between two or
more systems. Organizations typically do not have complete control over external networks,
including the Internet. Boundary protection devices (e.g., firewalls, gateways, and routers)
mediate communications and information flows between unclassified non-national security
systems and external networks.
Related Controls:  None.
(28) BOUNDARY PROTECTION | CONNECTIONS TO PUBLIC NETWORKS
Prohibit the direct connection of [Assignment: organization-defined system] to a public
network.
Discussion:  A direct connection is a dedicated physical or virtual connection between two or
more systems. A public network is a network accessible to the public, including the Internet
and organizational extranets with public access.
Related Controls:  None.
(29) BOUNDARY PROTECTION | SEPARATE SUBNETS TO ISOLATE FUNCTIONS
Implement [Selection: physically; logically] separate subnetworks to isolate the following
critical system components and functions: [Assignment: organization-defined critical
system components and functions].
Discussion:  Separating critical system components and functions from other noncritical
system components and functions through separate subnetworks may be necessary to
reduce susceptibility to a catastrophic or debilitating breach or compromise that results in
system failure. For example, physically separating the command and control function from
the in-flight entertainment function through separate subnetworks in a commercial aircraft
provides an increased level of assurance in the trustworthiness of critical system functions.
Related Controls:  None.
References:  [OMB A-130], [FIPS 199], [SP 800-37], [SP 800-41], [SP 800-77], [SP 800-189].
