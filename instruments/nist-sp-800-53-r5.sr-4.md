---
schema_version: 1
corpus: federal-reference
jurisdiction: us
id: nist-sp-800-53-r5.sr-4
title: NIST SP 800-53 Rev. 5 SR-4 — PROVENANCE
doc_type: federal_instrument
citation: NIST SP 800-53 Rev. 5 SR-4
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

**NIST SP 800-53 Rev. 5 SR-4** — PROVENANCE

- Issued by: National Institute of Standards and Technology
- Publication: NIST SP 800-53 Rev. 5 — Security and Privacy Controls for Information Systems and Organizations ([nist-sp-800-53-r5](./nist-sp-800-53-r5.md))
- Version: Rev. 5 (September 2020, includes updates as of 2020-12-10)
- Text as of: 2026-11-12
- Cited by held documents: 3 times (6-cfr-37 ×2, arc-ampe ×1)
- Reproduction basis: 17 U.S.C. § 105 — work of the U.S. government (NIST). Determined per document on 2026-11-12 against the publication itself, not assumed from its issuer: its Authority statement (PDF page 3) reads "This publication may be used by nongovernmental organizations on a voluntary basis and is not subject to copyright in the United States. Attribution would, however, be appreciated by NIST." Held here: the front matter and Chapter Three (the control catalog) only. Chapter Three names ISO/IEC standards solely as bibliographic references and reproduces none of their text. NOT mirrored: the References bibliography and Appendices A-C; Appendix A (glossary) adapts third-party definitions (ISO/IEC 15026, ISO 25237, ISO/IEC 29100, ISO 15288, IETF RFC 4949), which ADR-0002 treats as not reproducible by being incorporated, and whose reproducibility has not been determined.


_NON-AUTHORITATIVE copy of one control, cut from the SP 800-53 Rev. 5 snapshot this corpus holds. Whether and how this binds a given agency depends on the instrument that incorporates it — read it at the source URL before relying on it. This copy is the Rev. 5 text of record, which is not necessarily the text a citing document meant (a document citing Rev. 4 is not answered by it)._


## Full text

### SR-4 PROVENANCE
Control:  Document, monitor, and maintain valid provenance of the following systems, system
components, and associated data: [Assignment: organization-defined systems, system
components, and associated data].
Discussion:  Every system and system component has a point of origin and may be changed
throughout its existence. Provenance is the chronology of the origin, development, ownership,
location, and changes to a system or system component and associated data. It may also include
personnel and processes used to interact with or make modifications to the system, component,
or associated data. Organizations consider developing procedures (see SR-1) for allocating
responsibilities for the creation, maintenance, and monitoring of provenance for systems and
system components; transferring provenance documentation and responsibility between
organizations; and preventing and monitoring for unauthorized changes to the provenance
records. Organizations have methods to document, monitor, and maintain valid provenance
baselines for systems, system components, and related data. These actions help track, assess,
CHAPTER THREE   PAGE 367
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
and document any changes to the provenance, including changes in supply chain elements or
configuration, and help ensure non-repudiation of provenance information and the provenance
change records. Provenance considerations are addressed throughout the system development
life cycle and incorporated into contracts and other arrangements, as appropriate.
Related Controls:  CM-8, MA-2, MA-6, RA-9, SA-3, SA-8, SI-4.
Control Enhancements:
(1) PROVENANCE | IDENTITY
Establish and maintain unique identification of the following supply chain elements,
processes, and personnel associated with the identified system and critical system
components: [Assignment: organization-defined supply chain elements, processes, and
personnel associated with organization-defined systems and critical system components].
Discussion:  Knowing who and what is in the supply chains of organizations is critical to
gaining visibility into supply chain activities. Visibility into supply chain activities is also
important for monitoring and identifying high-risk events and activities. Without reasonable
visibility into supply chains elements, processes, and personnel, it is very difficult for
organizations to understand and manage risk and reduce their susceptibility to adverse
events. Supply chain elements include organizations, entities, or tools used for the research
and development, design, manufacturing, acquisition, delivery, integration, operations,
maintenance, and disposal of systems and system components. Supply chain processes
include development processes for hardware, software, and firmware; shipping and handling
procedures; configuration management tools, techniques, and measures to maintain
provenance; personnel and physical security programs; or other programs, processes, or
procedures associated with the production and distribution of supply chain elements. Supply
chain personnel are individuals with specific roles and responsibilities related to the secure
the research and development, design, manufacturing, acquisition, delivery, integration,
operations and maintenance, and disposal of a system or system component. Identification
methods are sufficient to support an investigation in case of a supply chain change (e.g. if a
supply company is purchased), compromise, or event.
Related Controls:  IA-2, IA-8, PE-16.
(2) PROVENANCE | TRACK AND TRACE
Establish and maintain unique identification of the following systems and critical system
components for tracking through the supply chain: [Assignment: organization-defined
systems and critical system components].
Discussion:  Tracking the unique identification of systems and system components during
development and transport activities provides a foundational identity structure for the
establishment and maintenance of provenance. For example, system components may be
labeled using serial numbers or tagged using radio-frequency identification tags. Labels and
tags can help provide better visibility into the provenance of a system or system component.
A system or system component may have more than one unique identifier. Identification
methods are sufficient to support a forensic investigation after a supply chain compromise
or event.
Related Controls:  IA-2, IA-8, PE-16, PL-2.
(3) PROVENANCE | VALIDATE AS GENUINE AND NOT ALTERED
Employ the following controls to validate that the system or system component received is
genuine and has not been altered: [Assignment: organization-defined controls].
Discussion:  For many systems and system components, especially hardware, there are
technical means to determine if the items are genuine or have been altered, including
optical and nanotechnology tagging, physically unclonable functions, side-channel analysis,
CHAPTER THREE   PAGE 368
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
cryptographic hash verifications or digital signatures, and visible anti-tamper labels or
stickers. Controls can also include monitoring for out of specification performance, which
can be an indicator of tampering or counterfeits. Organizations may leverage supplier and
contractor processes for validating that a system or component is genuine and has not been
altered and for replacing a suspect system or component. Some indications of tampering
may be visible and addressable before accepting delivery, such as inconsistent packaging,
broken seals, and incorrect labels. When a system or system component is suspected of
being altered or counterfeit, the supplier, contractor, or original equipment manufacturer
may be able to replace the item or provide a forensic capability to determine the origin of
the counterfeit or altered item. Organizations can provide training to personnel on how to
identify suspicious system or component deliveries.
Related Controls:  AT-3, SR-9, SR-10, SR-11
.
(4) PROVENANCE | SUPPLY CHAIN INTEGRITY — PEDIGREE
Employ [Assignment: organization-defined controls] and conduct [Assignment:
organization-defined analysis] to ensure the integrity of the system and system
components by validating the internal composition and provenance of critical or mission-
essential technologies, products, and services.
Discussion:  Authoritative information regarding the internal composition of system
components and the provenance of technology, products, and services provides a strong
basis for trust. The validation of the internal composition and provenance of technologies,
products, and services is referred to as the pedigree. For microelectronics, this includes
material composition of components. For software this includes the composition of open-
source and proprietary code, including the version of the component at a given point in
time. Pedigrees increase the assurance that the claims suppliers assert about the internal
composition and provenance of the products, services, and technologies they provide are
valid. The validation of the internal composition and provenance can be achieved by various
evidentiary artifacts or records that manufacturers and suppliers produce during the
research and development, design, manufacturing, acquisition, delivery, integration,
operations and maintenance, and disposal of technology, products, and services. Evidentiary
artifacts include, but are not limited to, software identification (SWID) tags, software
component inventory, the manufacturers’ declarations of platform attributes (e.g., serial
numbers, hardware component inventory), and measurements (e.g., firmware hashes) that
are tightly bound to the hardware itself.
Related Controls:  RA-3.
References:  [FASC18], [41 CFR 201], [EO 13873], [ISO 27036], [ISO 20243], [SP 800-160-1], [SP
800-161], [IR 7622], [IR 8112], [IR 8272].
