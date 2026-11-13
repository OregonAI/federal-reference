---
schema_version: 1
corpus: federal-reference
jurisdiction: us
id: nist-sp-800-53-r5.ac-20
title: NIST SP 800-53 Rev. 5 AC-20 — USE OF EXTERNAL SYSTEMS
doc_type: federal_instrument
citation: NIST SP 800-53 Rev. 5 AC-20
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

**NIST SP 800-53 Rev. 5 AC-20** — USE OF EXTERNAL SYSTEMS

- Issued by: National Institute of Standards and Technology
- Publication: NIST SP 800-53 Rev. 5 — Security and Privacy Controls for Information Systems and Organizations ([nist-sp-800-53-r5](./nist-sp-800-53-r5.md))
- Version: Rev. 5 (September 2020, includes updates as of 2020-12-10)
- Text as of: 2026-11-12
- Cited by held documents: 27 times (cjis-sp-6-1 ×18, irs-pub-1075-11-2021 ×5, 6-cfr-37 ×2, arc-ampe ×2)
- Reproduction basis: 17 U.S.C. § 105 — work of the U.S. government (NIST). Determined per document on 2026-11-12 against the publication itself, not assumed from its issuer: its Authority statement (PDF page 3) reads "This publication may be used by nongovernmental organizations on a voluntary basis and is not subject to copyright in the United States. Attribution would, however, be appreciated by NIST." Held here: the front matter and Chapter Three (the control catalog) only. Chapter Three names ISO/IEC standards solely as bibliographic references and reproduces none of their text. NOT mirrored: the References bibliography and Appendices A-C; Appendix A (glossary) adapts third-party definitions (ISO/IEC 15026, ISO 25237, ISO/IEC 29100, ISO 15288, IETF RFC 4949), which ADR-0002 treats as not reproducible by being incorporated, and whose reproducibility has not been determined.


_NON-AUTHORITATIVE copy of one control, cut from the SP 800-53 Rev. 5 snapshot this corpus holds. Whether and how this binds a given agency depends on the instrument that incorporates it — read it at the source URL before relying on it. This copy is the Rev. 5 text of record, which is not necessarily the text a citing document meant (a document citing Rev. 4 is not answered by it)._


## Full text

### AC-20 USE OF EXTERNAL SYSTEMS
Control:
a. [Selection (one or more): Establish [Assignment: organization-defined terms and conditions];
Identify [Assignment: organization-defined controls asserted to be implemented on external
systems]], consistent with the trust relationships established with other organizations
owning, operating, and/or maintaining external systems, allowing authorized individuals to:
1. Access the system from external systems; and
2. Process, store, or transmit organization-controlled information using external systems;
or
b. Prohibit the use of [Assignment: organizationally-defined types of external systems].
Discussion:  External systems are systems that are used by but not part of organizational systems,
and for which the organization has no direct control over the implementation of required
controls or the assessment of control effectiveness. External systems include personally owned
systems, components, or devices; privately owned computing and communications devices in
commercial or public facilities; systems owned or controlled by nonfederal organizations;
systems managed by contractors; and federal information systems that are not owned by,
operated by, or under the direct supervision or authority of the organization. External systems
also include systems owned or operated by other components within the same organization and
systems within the organization with different authorization boundaries. Organizations have the
option to prohibit the use of any type of external system or prohibit the use of specified types of
external systems, (e.g., prohibit the use of any external system that is not organizationally owned
or prohibit the use of personally-owned systems).
For some external systems (i.e., systems operated by other organizations), the trust relationships
that have been established between those organizations and the originating organization may be
such that no explicit terms and conditions are required. Systems within these organizations may
not be considered external. These situations occur when, for example, there are pre-existing
information exchange agreements (either implicit or explicit) established between organizations
or components or when such agreements are specified by applicable laws, executive orders,
directives, regulations, policies, or standards. Authorized individuals include organizational
personnel, contractors, or other individuals with authorized access to organizational systems and
over which organizations have the authority to impose specific rules of behavior regarding
system access. Restrictions that organizations impose on authorized individuals need not be
uniform, as the restrictions may vary depending on trust relationships between organizations.
Therefore, organizations may choose to impose different security restrictions on contractors
than on state, local, or tribal governments.
External systems used to access public interfaces to organizational systems are outside the scope
of AC-20
. Organizations establish specific terms and conditions for the use of external systems in
accordance with organizational security policies and procedures. At a minimum, terms and
conditions address the specific types of applications that can be accessed on organizational
CHAPTER THREE   PAGE 54
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
systems from external systems and the highest security category of information that can be
processed, stored, or transmitted on external systems. If the terms and conditions with the
owners of the external systems cannot be established, organizations may impose restrictions on
organizational personnel using those external systems.
Related Controls:  AC-2, AC-3, AC-17, AC-19, CA-3, PL-2, PL-4, SA-9, SC-7.
Control Enhancements:
(1) USE OF EXTERNAL SYSTEMS | LIMITS ON AUTHORIZED USE
Permit authorized individuals to use an external system to access the system or to process,
store, or transmit organization-controlled information only after:
(a) Verification of the implementation of controls on the external system as specified in
the organization’s security and privacy policies and security and privacy plans; or
(b) Retention of approved system connection or processing agreements with the
organizational entity hosting the external system.
Discussion:  Limiting authorized use recognizes circumstances where individuals using
external systems may need to access organizational systems. Organizations need assurance
that the external systems contain the necessary controls so as not to compromise, damage,
or otherwise harm organizational systems. Verification that the required controls have been
implemented can be achieved by external, independent assessments, attestations, or other
means, depending on the confidence level required by organizations.
Related Controls:  CA-2.
(2) USE OF EXTERNAL SYSTEMS | PORTABLE STORAGE DEVICES — RESTRICTED USE
Restrict the use of organization-controlled portable storage devices by authorized
individuals on external systems using [Assignment: organization-defined restrictions].
Discussion:  Limits on the use of organization-controlled portable storage devices in external
systems include restrictions on how the devices may be used and under what conditions the
devices may be used.
Related Controls:  MP-7, SC-41.
(3) USE OF EXTERNAL SYSTEMS | NON-ORGANIZATIONALLY OWNED SYSTEMS  — RESTRICTED USE
Restrict the use of non-organizationally owned systems or system components to process,
store, or transmit organizational information using [Assignment: organization-defined
restrictions].
Discussion:  Non-organizationally owned systems or system components include systems or
system components owned by other organizations as well as personally owned devices.
There are potential risks to using non-organizationally owned systems or components. In
some cases, the risk is sufficiently high as to prohibit such use (see AC-20 b.). In other cases,
the use of such systems or system components may be allowed but restricted in some way.
Restrictions include requiring the implementation of approved controls prior to authorizing
the connection of non-organizationally owned systems and components; limiting access to
types of information, services, or applications; using virtualization techniques to limit
processing and storage activities to servers or system components provisioned by the
organization; and agreeing to the terms and conditions for usage. Organizations consult with
the Office of the General Counsel regarding legal issues associated with using personally
owned devices, including requirements for conducting forensic analyses during
investigations after an incident.
Related Controls:  None.
(4) USE OF EXTERNAL SYSTEMS | NETWORK ACCESSIBLE STORAGE DEVICES — PROHIBITED USE
CHAPTER THREE   PAGE 55
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
Prohibit the use of [Assignment: organization-defined network accessible storage devices]
in external systems.
Discussion:  Network-accessible storage devices in external systems include online storage
devices in public, hybrid, or community cloud-based systems.
Related Controls:  None.
(5) USE OF EXTERNAL SYSTEMS | PORTABLE STORAGE DEVICES — PROHIBITED USE
Prohibit the use of organization-controlled portable storage devices by authorized
individuals on external systems.
Discussion:  Limits on the use of organization-controlled portable storage devices in external
systems include a complete prohibition of the use of such devices. Prohibiting such use is
enforced using technical methods and/or nontechnical (i.e., process-based) methods.
Related Controls:  MP-7, PL-4, PS-6, SC-41.
References:  [FIPS 199], [SP 800-171], [SP 800-172].
