---
schema_version: 1
corpus: federal-reference
jurisdiction: us
id: nist-sp-800-53-r5.sc-5
title: NIST SP 800-53 Rev. 5 SC-5 — DENIAL-OF-SERVICE PROTECTION
doc_type: federal_instrument
citation: NIST SP 800-53 Rev. 5 SC-5
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

**NIST SP 800-53 Rev. 5 SC-5** — DENIAL-OF-SERVICE PROTECTION

- Issued by: National Institute of Standards and Technology
- Publication: NIST SP 800-53 Rev. 5 — Security and Privacy Controls for Information Systems and Organizations ([nist-sp-800-53-r5](./nist-sp-800-53-r5.md))
- Version: Rev. 5 (September 2020, includes updates as of 2020-12-10)
- Text as of: 2026-11-12
- Cited by held documents: 16 times (cjis-sp-6-1 ×11, arc-ampe ×4, 6-cfr-37 ×1), 1 of them naming an enhancement of this control
- Reproduction basis: 17 U.S.C. § 105 — work of the U.S. government (NIST). Determined per document on 2026-11-12 against the publication itself, not assumed from its issuer: its Authority statement (PDF page 3) reads "This publication may be used by nongovernmental organizations on a voluntary basis and is not subject to copyright in the United States. Attribution would, however, be appreciated by NIST." Held here: the front matter and Chapter Three (the control catalog) only. Chapter Three names ISO/IEC standards solely as bibliographic references and reproduces none of their text. NOT mirrored: the References bibliography and Appendices A-C; Appendix A (glossary) adapts third-party definitions (ISO/IEC 15026, ISO 25237, ISO/IEC 29100, ISO 15288, IETF RFC 4949), which ADR-0002 treats as not reproducible by being incorporated, and whose reproducibility has not been determined.


_NON-AUTHORITATIVE copy of one control, cut from the SP 800-53 Rev. 5 snapshot this corpus holds. Whether and how this binds a given agency depends on the instrument that incorporates it — read it at the source URL before relying on it. This copy is the Rev. 5 text of record, which is not necessarily the text a citing document meant (a document citing Rev. 4 is not answered by it)._


## Full text

### SC-5 DENIAL-OF-SERVICE PROTECTION
Control:
a. [Selection: Protect against; Limit] the effects of the following types of denial-of-service
events: [Assignment: organization-defined types of denial-of-service events]; and
b. Employ the following controls to achieve the denial-of-service objective: [Assignment:
organization-defined controls by type of denial-of-service event].
Discussion:  Denial-of-service events may occur due to a variety of internal and external causes,
such as an attack by an adversary or a lack of planning to support organizational needs with
respect to capacity and bandwidth. Such attacks can occur across a wide range of network
protocols (e.g., IPv4, IPv6). A variety of technologies are available to limit or eliminate the
origination and effects of denial-of-service events. For example, boundary protection devices can
filter certain types of packets to protect system components on internal networks from being
directly affected by or the source of denial-of-service attacks. Employing increased network
capacity and bandwidth combined with service redundancy also reduces the susceptibility to
denial-of-service events.
Related Controls:  CP-2, IR-4, SC-6, SC-7, SC-40.
Control Enhancements:
(1) DENIAL-OF-SERVICE PROTECTION | RESTRICT ABILITY TO ATTACK OTHER SYSTEMS
Restrict the ability of individuals to launch the following denial-of-service attacks against
other systems: [Assignment: organization-defined denial-of-service attacks].
Discussion:  Restricting the ability of individuals to launch denial-of-service attacks requires
the mechanisms commonly used for such attacks to be unavailable. Individuals of concern
include hostile insiders or external adversaries who have breached or compromised the
system and are using it to launch a denial-of-service attack. Organizations can restrict the
ability of individuals to connect and transmit arbitrary information on the transport medium
(i.e., wired networks, wireless networks, spoofed Internet protocol packets). Organizations
can also limit the ability of individuals to use excessive system resources. Protection against
individuals having the ability to launch denial-of-service attacks may be implemented on
specific systems or boundary devices that prohibit egress to potential target systems.
Related Controls:  None.
(2) DENIAL-OF-SERVICE PROTECTION | CAPACITY, BANDWIDTH, AND REDUNDANCY
Manage capacity, bandwidth, or other redundancy to limit the effects of information
flooding denial-of-service attacks.
Discussion:  Managing capacity ensures that sufficient capacity is available to counter
flooding attacks. Managing capacity includes establishing selected usage priorities, quotas,
partitioning, or load balancing.
Related Controls:  None.
(3) DENIAL-OF-SERVICE PROTECTION | DETECTION AND MONITORING
(a) Employ the following monitoring tools to detect indicators of denial-of-service attacks
against, or launched from, the system: [Assignment: organization-defined monitoring
tools]; and
(b) Monitor the following system resources to determine if sufficient resources exist to
prevent effective denial-of-service attacks: [Assignment: organization-defined system
resources].
CHAPTER THREE   PAGE 297
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
Discussion:  Organizations consider the utilization and capacity of system resources when
managing risk associated with a denial of service due to malicious attacks. Denial-of-service
attacks can originate from external or internal sources. System resources that are sensitive
to denial of service include physical disk storage, memory, and CPU cycles. Techniques used
to prevent denial-of-service attacks related to storage utilization and capacity include
instituting disk quotas, configuring systems to automatically alert administrators when
specific storage capacity thresholds are reached, using file compression technologies to
maximize available storage space, and imposing separate partitions for system and user
data.
Related Controls:  CA-7, SI-4.
References:  [SP 800-189].
