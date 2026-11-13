---
schema_version: 1
corpus: federal-reference
jurisdiction: us
id: nist-sp-800-53-r5.ca-3
title: NIST SP 800-53 Rev. 5 CA-3 — INFORMATION EXCHANGE
doc_type: federal_instrument
citation: NIST SP 800-53 Rev. 5 CA-3
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

**NIST SP 800-53 Rev. 5 CA-3** — INFORMATION EXCHANGE

- Issued by: National Institute of Standards and Technology
- Publication: NIST SP 800-53 Rev. 5 — Security and Privacy Controls for Information Systems and Organizations ([nist-sp-800-53-r5](./nist-sp-800-53-r5.md))
- Version: Rev. 5 (September 2020, includes updates as of 2020-12-10)
- Text as of: 2026-11-12
- Cited by held documents: 27 times (cjis-sp-6-1 ×21, irs-pub-1075-11-2021 ×3, arc-ampe ×2, 6-cfr-37 ×1), 1 of them naming an enhancement of this control
- Reproduction basis: 17 U.S.C. § 105 — work of the U.S. government (NIST). Determined per document on 2026-11-12 against the publication itself, not assumed from its issuer: its Authority statement (PDF page 3) reads "This publication may be used by nongovernmental organizations on a voluntary basis and is not subject to copyright in the United States. Attribution would, however, be appreciated by NIST." Held here: the front matter and Chapter Three (the control catalog) only. Chapter Three names ISO/IEC standards solely as bibliographic references and reproduces none of their text. NOT mirrored: the References bibliography and Appendices A-C; Appendix A (glossary) adapts third-party definitions (ISO/IEC 15026, ISO 25237, ISO/IEC 29100, ISO 15288, IETF RFC 4949), which ADR-0002 treats as not reproducible by being incorporated, and whose reproducibility has not been determined.


_NON-AUTHORITATIVE copy of one control, cut from the SP 800-53 Rev. 5 snapshot this corpus holds. Whether and how this binds a given agency depends on the instrument that incorporates it — read it at the source URL before relying on it. This copy is the Rev. 5 text of record, which is not necessarily the text a citing document meant (a document citing Rev. 4 is not answered by it)._


## Full text

### CA-3 INFORMATION EXCHANGE
Control:
a. Approve and manage the exchange of information between the system and other systems
using [Selection (one or more): interconnection security agreements; information exchange
security agreements; memoranda of understanding or agreement; service level agreements;
CHAPTER THREE   PAGE 87
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
user agreements; nondisclosure agreements; [Assignment: organization-defined type of
agreement]];
b. Document, as part of each exchange agreement, the interface characteristics, security and
privacy requirements, controls, and responsibilities for each system, and the impact level of
the information communicated; and
c. Review and update the agreements [Assignment: organization-defined frequency].
Discussion:  System information exchange requirements apply to information exchanges
between two or more systems. System information exchanges include connections via leased
lines or virtual private networks, connections to internet service providers, database sharing or
exchanges of database transaction information, connections and exchanges with cloud services,
exchanges via web-based services, or exchanges of files via file transfer protocols, network
protocols (e.g., IPv4, IPv6), email, or other organization-to-organization communications.
Organizations consider the risk related to new or increased threats that may be introduced when
systems exchange information with other systems that may have different security and privacy
requirements and controls. This includes systems within the same organization and systems that
are external to the organization. A joint authorization of the systems exchanging information, as
described in CA-6(1) or CA-6(2), may help to communicate and reduce risk.
Authorizing officials determine the risk associated with system information exchange and the
controls needed for appropriate risk mitigation. The types of agreements selected are based on
factors such as the impact level of the information being exchanged, the relationship between
the organizations exchanging information (e.g., government to government, government to
business, business to business, government or business to service provider, government or
business to individual), or the level of access to the organizational system by users of the other
system. If systems that exchange information have the same authorizing official, organizations
need not develop agreements. Instead, the interface characteristics between the systems (e.g.,
how the information is being exchanged. how the information is protected) are described in the
respective security and privacy plans. If the systems that exchange information have different
authorizing officials within the same organization, the organizations can develop agreements or
provide the same information that would be provided in the appropriate agreement type from
CA-3a
in the respective security and privacy plans for the systems. Organizations may incorporate
agreement information into formal contracts, especially for information exchanges established
between federal agencies and nonfederal organizations (including service providers, contractors,
system developers, and system integrators). Risk considerations include systems that share the
same networks.
Related Controls:  AC-4,  AC-20, AU-16, CA-6, IA-3, IR-4, PL-2, PT-7, RA-3, SA-9, SC-7, SI-12.
Control Enhancements:
(1) SYSTEM CONNECTIONS | UNCLASSIFIED NATIONAL SECURITY SYSTEM CONNECTIONS
[Withdrawn: Moved to SC-7(25).]
(2) SYSTEM CONNECTIONS | CLASSIFIED NATIONAL SECURITY SYSTEM CONNECTIONS
[Withdrawn: Moved to SC-7(26).]
(3) SYSTEM CONNECTIONS | UNCLASSIFIED NON-NATIONAL SECURITY SYSTEM CONNECTIONS
[Withdrawn: Moved to SC-7(27).]
(4) SYSTEM CONNECTIONS | CONNECTIONS TO PUBLIC NETWORKS
[Withdrawn: Moved to SC-7(28).]
(5) SYSTEM CONNECTIONS | RESTRICTIONS ON EXTERNAL SYSTEM CONNECTIONS
CHAPTER THREE   PAGE 88
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
[Withdrawn: Moved to SC-7(5).]
(6) INFORMATION EXCHANGE | TRANSFER AUTHORIZATIONS
Verify that individuals or systems transferring data between interconnecting systems have
the requisite authorizations (i.e., write permissions or privileges) prior to accepting such
data.
Discussion:  To prevent unauthorized individuals and systems from making information
transfers to protected systems, the protected system verifies—via independent means—
whether the individual or system attempting to transfer information is authorized to do so.
Verification of the authorization to transfer information also applies to control plane traffic
(e.g., routing and DNS) and services (e.g., authenticated SMTP relays).
Related Controls:  AC-2, AC-3, AC-4.
(7) INFORMATION EXCHANGE |TRANSITIVE INFORMATION EXCHANGES
(a) Identify transitive (downstream) information exchanges with other systems through
the systems identified in CA-3a; and
(b) Take measures to ensure that transitive (downstream) information exchanges cease
when the controls on identified transitive (downstream) systems cannot be verified or
validated.
Discussion:  Transitive or “downstream” information exchanges are information exchanges
between the system or systems with which the organizational system exchanges information
and other systems. For mission-essential systems, services, and applications, including high
value assets, it is necessary to identify such information exchanges. The transparency of the
controls or protection measures in place in such downstream systems connected directly or
indirectly to organizational systems is essential to understanding the security and privacy
risks resulting from those information exchanges. Organizational systems can inherit risk
from downstream systems through transitive connections and information exchanges, which
can make the organizational systems more susceptible to threats, hazards, and adverse
impacts.
Related Controls:  SC-7.
References:  [OMB A-130], [FIPS 199], [SP 800-47].
