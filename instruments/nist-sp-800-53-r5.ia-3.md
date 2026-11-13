---
schema_version: 1
corpus: federal-reference
jurisdiction: us
id: nist-sp-800-53-r5.ia-3
title: NIST SP 800-53 Rev. 5 IA-3 — DEVICE IDENTIFICATION AND AUTHENTICATION
doc_type: federal_instrument
citation: NIST SP 800-53 Rev. 5 IA-3
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

**NIST SP 800-53 Rev. 5 IA-3** — DEVICE IDENTIFICATION AND AUTHENTICATION

- Issued by: National Institute of Standards and Technology
- Publication: NIST SP 800-53 Rev. 5 — Security and Privacy Controls for Information Systems and Organizations ([nist-sp-800-53-r5](./nist-sp-800-53-r5.md))
- Version: Rev. 5 (September 2020, includes updates as of 2020-12-10)
- Text as of: 2026-11-12
- Cited by held documents: 34 times (cjis-sp-6-1 ×23, 6-cfr-37 ×4, arc-ampe ×4, irs-pub-1075-11-2021 ×3)
- Reproduction basis: 17 U.S.C. § 105 — work of the U.S. government (NIST). Determined per document on 2026-11-12 against the publication itself, not assumed from its issuer: its Authority statement (PDF page 3) reads "This publication may be used by nongovernmental organizations on a voluntary basis and is not subject to copyright in the United States. Attribution would, however, be appreciated by NIST." Held here: the front matter and Chapter Three (the control catalog) only. Chapter Three names ISO/IEC standards solely as bibliographic references and reproduces none of their text. NOT mirrored: the References bibliography and Appendices A-C; Appendix A (glossary) adapts third-party definitions (ISO/IEC 15026, ISO 25237, ISO/IEC 29100, ISO 15288, IETF RFC 4949), which ADR-0002 treats as not reproducible by being incorporated, and whose reproducibility has not been determined.


_NON-AUTHORITATIVE copy of one control, cut from the SP 800-53 Rev. 5 snapshot this corpus holds. Whether and how this binds a given agency depends on the instrument that incorporates it — read it at the source URL before relying on it. This copy is the Rev. 5 text of record, which is not necessarily the text a citing document meant (a document citing Rev. 4 is not answered by it)._


## Full text

### IA-3 DEVICE IDENTIFICATION AND AUTHENTICATION
Control:  Uniquely identify and authenticate [Assignment: organization-defined devices and/or
types of devices] before establishing a [Selection (one or more): local; remote; network]
connection.
Discussion:  Devices that require unique device-to-device identification and authentication are
defined by type, device, or a combination of type and device. Organization-defined device types
include devices that are not owned by the organization. Systems use shared known information
(e.g., Media Access Control [MAC], Transmission Control Protocol/Internet Protocol [TCP/IP]
addresses) for device identification or organizational authentication solutions (e.g., Institute of
Electrical and Electronics Engineers (IEEE) 802.1x and Extensible Authentication Protocol [EAP],
RADIUS server with EAP-Transport Layer Security [TLS] authentication, Kerberos) to identify and
authenticate devices on local and wide area networks. Organizations determine the required
strength of authentication mechanisms based on the security categories of systems and mission
or business requirements. Because of the challenges of implementing device authentication on a
large scale, organizations can restrict the application of the control to a limited number/type of
devices based on mission or business needs.
Related Controls:  AC-17, AC-18, AC-19, AU-6, CA-3, CA-9, IA-4, IA-5, IA-9, IA-11, SI-4.
Control Enhancements:
(1) DEVICE IDENTIFICATION AND AUTHENTICATION | CRYPTOGRAPHIC BIDIRECTIONAL AUTHENTICATION
Authenticate [Assignment: organization-defined devices and/or types of devices] before
establishing [Selection (one or more): local; remote; network] connection using
bidirectional authentication that is cryptographically based.
Discussion:  A local connection is a connection with a device that communicates without the
use of a network. A network connection is a connection with a device that communicates
through a network. A remote connection is a connection with a device that communicates
through an external network. Bidirectional authentication provides stronger protection to
validate the identity of other devices for connections that are of greater risk.
Related Controls:  SC-8, SC-12, SC-13.
(2) DEVICE IDENTIFICATION AND AUTHENTICATION | CRYPTOGRAPHIC BIDIRECTIONAL NETWORK
AUTHENTICATION
CHAPTER THREE   PAGE 136
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
[Withdrawn: Incorporated into IA-3(1).]
(3) DEVICE IDENTIFICATION AND AUTHENTICATION | DYNAMIC ADDRESS ALLOCATION
(a) Where addresses are allocated dynamically, standardize dynamic address allocation
lease information and the lease duration assigned to devices in accordance with
[Assignment: organization-defined lease information and lease duration]; and
(b) Audit lease information when assigned to a device.
Discussion:  The Dynamic Host Configuration Protocol (DHCP) is an example of a means by
which clients can dynamically receive network address assignments.
Related Controls:  AU-2.
(4) DEVICE IDENTIFICATION AND AUTHENTICATION | DEVICE ATTESTATION
Handle device identification and authentication based on attestation by [Assignment:
organization-defined configuration management process].
Discussion:  Device attestation refers to the identification and authentication of a device
based on its configuration and known operating state. Device attestation can be determined
via a cryptographic hash of the device. If device attestation is the means of identification and
authentication, then it is important that patches and updates to the device are handled via a
configuration management process such that the patches and updates are done securely
and do not disrupt identification and authentication to other devices.
Related Controls:  CM-2, CM-3, CM-6.
References:  None.
