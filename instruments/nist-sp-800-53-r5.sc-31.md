---
schema_version: 1
corpus: federal-reference
jurisdiction: us
id: nist-sp-800-53-r5.sc-31
title: NIST SP 800-53 Rev. 5 SC-31 — COVERT CHANNEL ANALYSIS
doc_type: federal_instrument
citation: NIST SP 800-53 Rev. 5 SC-31
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

**NIST SP 800-53 Rev. 5 SC-31** — COVERT CHANNEL ANALYSIS

- Issued by: National Institute of Standards and Technology
- Publication: NIST SP 800-53 Rev. 5 — Security and Privacy Controls for Information Systems and Organizations ([nist-sp-800-53-r5](./nist-sp-800-53-r5.md))
- Version: Rev. 5 (September 2020, includes updates as of 2020-12-10)
- Text as of: 2026-11-12
- Cited by held documents: 1 time (arc-ampe ×1)
- Reproduction basis: 17 U.S.C. § 105 — work of the U.S. government (NIST). Determined per document on 2026-11-12 against the publication itself, not assumed from its issuer: its Authority statement (PDF page 3) reads "This publication may be used by nongovernmental organizations on a voluntary basis and is not subject to copyright in the United States. Attribution would, however, be appreciated by NIST." Held here: the front matter and Chapter Three (the control catalog) only. Chapter Three names ISO/IEC standards solely as bibliographic references and reproduces none of their text. NOT mirrored: the References bibliography and Appendices A-C; Appendix A (glossary) adapts third-party definitions (ISO/IEC 15026, ISO 25237, ISO/IEC 29100, ISO 15288, IETF RFC 4949), which ADR-0002 treats as not reproducible by being incorporated, and whose reproducibility has not been determined.


_NON-AUTHORITATIVE copy of one control, cut from the SP 800-53 Rev. 5 snapshot this corpus holds. Whether and how this binds a given agency depends on the instrument that incorporates it — read it at the source URL before relying on it. This copy is the Rev. 5 text of record, which is not necessarily the text a citing document meant (a document citing Rev. 4 is not answered by it)._


## Full text

### SC-31 COVERT CHANNEL ANALYSIS
Control:
CHAPTER THREE   PAGE 320
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
a. Perform a covert channel analysis to identify those aspects of communications within the
system that are potential avenues for covert [Selection (one or more): storage; timing]
channels; and
b. Estimate the maximum bandwidth of those channels.
Discussion:  Developers are in the best position to identify potential areas within systems that
might lead to covert channels. Covert channel analysis is a meaningful activity when there is the
potential for unauthorized information flows across security domains, such as in the case of
systems that contain export-controlled information and have connections to external networks
(i.e., networks that are not controlled by organizations). Covert channel analysis is also useful for
multilevel secure systems, multiple security level systems, and cross-domain systems.
Related Controls:  AC-3, AC-4, SA-8, SI-11.
Control Enhancements:
(1) COVERT CHANNEL ANALYSIS | TEST COVERT CHANNELS FOR EXPLOITABILITY
Test a subset of the identified covert channels to determine the channels that are
exploitable.
Discussion:  None.
Related Controls:  None.
(2) COVERT CHANNEL ANALYSIS | MAXIMUM BANDWIDTH
Reduce the maximum bandwidth for identified covert [Selection (one or more): storage;
timing] channels to [Assignment: organization-defined values].
Discussion:  The complete elimination of covert channels, especially covert timing channels,
is usually not possible without significant performance impacts.
Related Controls:  None.
(3) COVERT CHANNEL ANALYSIS | MEASURE BANDWIDTH IN OPERATIONAL ENVIRONMENTS
Measure the bandwidth of [Assignment: organization-defined subset of identified covert
channels] in the operational environment of the system.
Discussion:  Measuring covert channel bandwidth in specified operational environments
helps organizations determine how much information can be covertly leaked before such
leakage adversely affects mission or business functions. Covert channel bandwidth may be
significantly different when measured in settings that are independent of the specific
environments of operation, including laboratories or system development environments.
Related Controls:  None.
References:  None.
