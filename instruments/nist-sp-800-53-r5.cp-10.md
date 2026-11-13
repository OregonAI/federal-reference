---
schema_version: 1
corpus: federal-reference
jurisdiction: us
id: nist-sp-800-53-r5.cp-10
title: NIST SP 800-53 Rev. 5 CP-10 — SYSTEM RECOVERY AND RECONSTITUTION
doc_type: federal_instrument
citation: NIST SP 800-53 Rev. 5 CP-10
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

**NIST SP 800-53 Rev. 5 CP-10** — SYSTEM RECOVERY AND RECONSTITUTION

- Issued by: National Institute of Standards and Technology
- Publication: NIST SP 800-53 Rev. 5 — Security and Privacy Controls for Information Systems and Organizations ([nist-sp-800-53-r5](./nist-sp-800-53-r5.md))
- Version: Rev. 5 (September 2020, includes updates as of 2020-12-10)
- Text as of: 2026-11-12
- Cited by held documents: 22 times (cjis-sp-6-1 ×15, irs-pub-1075-11-2021 ×3, 6-cfr-37 ×2, arc-ampe ×2)
- Reproduction basis: 17 U.S.C. § 105 — work of the U.S. government (NIST). Determined per document on 2026-11-12 against the publication itself, not assumed from its issuer: its Authority statement (PDF page 3) reads "This publication may be used by nongovernmental organizations on a voluntary basis and is not subject to copyright in the United States. Attribution would, however, be appreciated by NIST." Held here: the front matter and Chapter Three (the control catalog) only. Chapter Three names ISO/IEC standards solely as bibliographic references and reproduces none of their text. NOT mirrored: the References bibliography and Appendices A-C; Appendix A (glossary) adapts third-party definitions (ISO/IEC 15026, ISO 25237, ISO/IEC 29100, ISO 15288, IETF RFC 4949), which ADR-0002 treats as not reproducible by being incorporated, and whose reproducibility has not been determined.


_NON-AUTHORITATIVE copy of one control, cut from the SP 800-53 Rev. 5 snapshot this corpus holds. Whether and how this binds a given agency depends on the instrument that incorporates it — read it at the source URL before relying on it. This copy is the Rev. 5 text of record, which is not necessarily the text a citing document meant (a document citing Rev. 4 is not answered by it)._


## Full text

### CP-10 SYSTEM RECOVERY AND RECONSTITUTION
Control:  Provide for the recovery and reconstitution of the system to a known state within
[Assignment: organization-defined time period consistent with recovery time and recovery point
objectives] after a disruption, compromise, or failure.
Discussion:  Recovery is executing contingency plan activities to restore organizational mission
and business functions. Reconstitution takes place following recovery and includes activities for
returning systems to fully operational states. Recovery and reconstitution operations reflect
mission and business priorities; recovery point, recovery time, and reconstitution objectives; and
organizational metrics consistent with contingency plan requirements. Reconstitution includes
the deactivation of interim system capabilities that may have been needed during recovery
operations. Reconstitution also includes assessments of fully restored system capabilities,
reestablishment of continuous monitoring activities, system reauthorization (if required), and
activities to prepare the system and organization for future disruptions, breaches, compromises,
or failures. Recovery and reconstitution capabilities can include automated mechanisms and
manual procedures.
Organizations establish recovery time and recovery point objectives as part
of contingency planning.
Related Controls:  CP-2, CP-4, CP-6, CP-7, CP-9, IR-4, SA-8, SC-24, SI-13.
Control Enhancements:
(1) SYSTEM RECOVERY AND RECONSTITUTION | CONTINGENCY PLAN TESTING
[Withdrawn: Incorporated into CP-4.]
(2) SYSTEM RECOVERY AND RECONSTITUTION | TRANSACTION RECOVERY
Implement transaction recovery for systems that are transaction-based.
Discussion:  Transaction-based systems include database management systems and
transaction processing systems. Mechanisms supporting transaction recovery include
transaction rollback and transaction journaling.
Related Controls:  None.
(3) SYSTEM RECOVERY AND RECONSTITUTION | COMPENSATING SECURITY CONTROLS
[Withdrawn: Addressed through tailoring.]
(4) SYSTEM RECOVERY AND RECONSTITUTION | RESTORE WITHIN TIME PERIOD
Provide the capability to restore system components within [Assignment: organization-
defined restoration time periods] from configuration-controlled and integrity-protected
information representing a known, operational state for the components.
Discussion:  Restoration of system components includes reimaging, which restores the
components to known, operational states.
Related Controls:  CM-2, CM-6.
(5) SYSTEM RECOVERY AND RECONSTITUTION | FAILOVER CAPABILITY
[Withdrawn: Incorporated into SI-13.]
(6) SYSTEM RECOVERY AND RECONSTITUTION | COMPONENT PROTECTION
Protect system components used for recovery and reconstitution.
Discussion:  Protection of system recovery and reconstitution components (i.e., hardware,
firmware, and software) includes physical and technical controls. Backup and restoration
components used for recovery and reconstitution include router tables, compilers, and other
system software.
Related Controls:  AC-3, AC-6, MP-2, MP-4, PE-3, PE-6.
CHAPTER THREE   PAGE 129
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
References:  [SP 800-34].
