---
schema_version: 1
corpus: federal-reference
jurisdiction: us
id: nist-sp-800-53-r5.sa-22
title: NIST SP 800-53 Rev. 5 SA-22 — UNSUPPORTED SYSTEM COMPONENTS
doc_type: federal_instrument
citation: NIST SP 800-53 Rev. 5 SA-22
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

**NIST SP 800-53 Rev. 5 SA-22** — UNSUPPORTED SYSTEM COMPONENTS

- Issued by: National Institute of Standards and Technology
- Publication: NIST SP 800-53 Rev. 5 — Security and Privacy Controls for Information Systems and Organizations ([nist-sp-800-53-r5](./nist-sp-800-53-r5.md))
- Version: Rev. 5 (September 2020, includes updates as of 2020-12-10)
- Text as of: 2026-11-12
- Cited by held documents: 10 times (cjis-sp-6-1 ×6, irs-pub-1075-11-2021 ×3, 6-cfr-37 ×1)
- Reproduction basis: 17 U.S.C. § 105 — work of the U.S. government (NIST). Determined per document on 2026-11-12 against the publication itself, not assumed from its issuer: its Authority statement (PDF page 3) reads "This publication may be used by nongovernmental organizations on a voluntary basis and is not subject to copyright in the United States. Attribution would, however, be appreciated by NIST." Held here: the front matter and Chapter Three (the control catalog) only. Chapter Three names ISO/IEC standards solely as bibliographic references and reproduces none of their text. NOT mirrored: the References bibliography and Appendices A-C; Appendix A (glossary) adapts third-party definitions (ISO/IEC 15026, ISO 25237, ISO/IEC 29100, ISO 15288, IETF RFC 4949), which ADR-0002 treats as not reproducible by being incorporated, and whose reproducibility has not been determined.


_NON-AUTHORITATIVE copy of one control, cut from the SP 800-53 Rev. 5 snapshot this corpus holds. Whether and how this binds a given agency depends on the instrument that incorporates it — read it at the source URL before relying on it. This copy is the Rev. 5 text of record, which is not necessarily the text a citing document meant (a document citing Rev. 4 is not answered by it)._


## Full text

### SA-22 UNSUPPORTED SYSTEM COMPONENTS
Control:
a. Replace system components when support for the components is no longer available from
the developer, vendor, or manufacturer; or
b. Provide the following options for alternative sources for continued support for unsupported
components [Selection (one or more): in-house support; [Assignment: organization-defined
support from external providers]].
Discussion:  Support for system components includes software patches, firmware updates,
replacement parts, and maintenance contracts. An example of unsupported components
includes when vendors no longer provide critical software patches or product updates, which can
result in an opportunity for adversaries to exploit weaknesses in the installed components.
Exceptions to replacing unsupported system components include systems that provide critical
mission or business capabilities where newer technologies are not available or where the
systems are so isolated that installing replacement components is not an option.
Alternative sources for support address the need to provide continued support for system
components that are no longer supported by the original manufacturers, developers, or vendors
when such components remain essential to organizational mission and business functions. If
necessary, organizations can establish in-house support by developing customized patches for
critical software components or, alternatively, obtain the services of external providers who
provide ongoing support for the designated unsupported components through contractual
relationships. Such contractual relationships can include open-source software value-added
vendors. The increased risk of using unsupported system components can be mitigated, for
example, by prohibiting the connection of such components to public or uncontrolled networks,
or implementing other forms of isolation.
Related Controls:  PL-2, SA-3.
Control Enhancements:
(1) UNSUPPORTED SYSTEM COMPONENTS | ALTERNATIVE SOURCES FOR CONTINUED SUPPORT
[Withdrawn: Incorporated into SA-22.]
References:  None.
CHAPTER THREE   PAGE 291
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
