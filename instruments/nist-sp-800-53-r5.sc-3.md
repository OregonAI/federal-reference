---
schema_version: 1
corpus: federal-reference
jurisdiction: us
id: nist-sp-800-53-r5.sc-3
title: NIST SP 800-53 Rev. 5 SC-3 — SECURITY FUNCTION ISOLATION
doc_type: federal_instrument
citation: NIST SP 800-53 Rev. 5 SC-3
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

**NIST SP 800-53 Rev. 5 SC-3** — SECURITY FUNCTION ISOLATION

- Issued by: National Institute of Standards and Technology
- Publication: NIST SP 800-53 Rev. 5 — Security and Privacy Controls for Information Systems and Organizations ([nist-sp-800-53-r5](./nist-sp-800-53-r5.md))
- Version: Rev. 5 (September 2020, includes updates as of 2020-12-10)
- Text as of: 2026-11-12
- Cited by held documents: 3 times (cjis-sp-6-1 ×2, 6-cfr-37 ×1)
- Reproduction basis: 17 U.S.C. § 105 — work of the U.S. government (NIST). Determined per document on 2026-11-12 against the publication itself, not assumed from its issuer: its Authority statement (PDF page 3) reads "This publication may be used by nongovernmental organizations on a voluntary basis and is not subject to copyright in the United States. Attribution would, however, be appreciated by NIST." Held here: the front matter and Chapter Three (the control catalog) only. Chapter Three names ISO/IEC standards solely as bibliographic references and reproduces none of their text. NOT mirrored: the References bibliography and Appendices A-C; Appendix A (glossary) adapts third-party definitions (ISO/IEC 15026, ISO 25237, ISO/IEC 29100, ISO 15288, IETF RFC 4949), which ADR-0002 treats as not reproducible by being incorporated, and whose reproducibility has not been determined.


_NON-AUTHORITATIVE copy of one control, cut from the SP 800-53 Rev. 5 snapshot this corpus holds. Whether and how this binds a given agency depends on the instrument that incorporates it — read it at the source URL before relying on it. This copy is the Rev. 5 text of record, which is not necessarily the text a citing document meant (a document citing Rev. 4 is not answered by it)._


## Full text

### SC-3 SECURITY FUNCTION ISOLATION
Control:  Isolate security functions from nonsecurity functions.
Discussion:  Security functions are isolated from nonsecurity functions by means of an isolation
boundary implemented within a system via partitions and domains. The isolation boundary
controls access to and protects the integrity of the hardware, software, and firmware that
perform system security functions. Systems implement code separation in many ways, such as
through the provision of security kernels via processor rings or processor modes. For non-kernel
code, security function isolation is often achieved through file system protections that protect
the code on disk and address space protections that protect executing code. Systems can restrict
access to security functions using access control mechanisms and by implementing least privilege
CHAPTER THREE   PAGE 294
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
capabilities. While the ideal is for all code within the defined security function isolation boundary
to only contain security-relevant code, it is sometimes necessary to include nonsecurity functions
as an exception. The isolation of security functions from nonsecurity functions can be achieved
by applying the systems security engineering design principles in SA-8, including SA-8(1), SA-8(3),
SA-8(4), SA-8(10), SA-8(12), SA-8(13), SA-8(14), and SA-8(18).
Related Controls:  AC-3, AC-6, AC-25, CM-2, CM-4, SA-4, SA-5, SA-8, SA-15, SA-17, SC-2, SC-7, SC-
32, SC-39, SI-16.
Control Enhancements:
(1) SECURITY FUNCTION ISOLATION | HARDWARE SEPARATION
Employ hardware separation mechanisms to implement security function isolation.
Discussion:  Hardware separation mechanisms include hardware ring architectures that are
implemented within microprocessors and hardware-enforced address segmentation used to
support logically distinct storage objects with separate attributes (i.e., readable, writeable).
Related Controls:  None.
(2) SECURITY FUNCTION ISOLATION | ACCESS AND FLOW CONTROL FUNCTIONS
Isolate security functions enforcing access and information flow control from nonsecurity
functions and from other security functions.
Discussion:  Security function isolation occurs because of implementation. The functions can
still be scanned and monitored. Security functions that are potentially isolated from access
and flow control enforcement functions include auditing, intrusion detection, and malicious
code protection functions.
Related Controls:  None.
(3) SECURITY FUNCTION ISOLATION | MINIMIZE NONSECURITY FUNCTIONALITY
Minimize the number of nonsecurity functions included within the isolation boundary
containing security functions.
Discussion:  Where it is not feasible to achieve strict isolation of nonsecurity functions from
security functions, it is necessary to take actions to minimize nonsecurity-relevant functions
within the security function boundary. Nonsecurity functions contained within the isolation
boundary are considered security-relevant because errors or malicious code in the software
can directly impact the security functions of systems. The fundamental design objective is
that the specific portions of systems that provide information security are of minimal size
and complexity. Minimizing the number of nonsecurity functions in the security-relevant
system components allows designers and implementers to focus only on those functions
which are necessary to provide the desired security capability (typically access enforcement).
By minimizing the nonsecurity functions within the isolation boundaries, the amount of code
that is trusted to enforce security policies is significantly reduced, thus contributing to
understandability.
Related Controls:  None.
(4) SECURITY FUNCTION ISOLATION | MODULE COUPLING AND COHESIVENESS
Implement security functions as largely independent modules that maximize internal
cohesiveness within modules and minimize coupling between modules.
Discussion:  The reduction of inter-module interactions helps to constrain security functions
and manage complexity. The concepts of coupling and cohesion are important with respect
to modularity in software design. Coupling refers to the dependencies that one module has
on other modules. Cohesion refers to the relationship between functions within a module.
Best practices in software engineering and systems security engineering rely on layering,
CHAPTER THREE   PAGE 295
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
minimization, and modular decomposition to reduce and manage complexity. This produces
software modules that are highly cohesive and loosely coupled.
Related Controls:  None.
(5) SECURITY FUNCTION ISOLATION | LAYERED STRUCTURES
Implement security functions as a layered structure minimizing interactions between
layers of the design and avoiding any dependence by lower layers on the functionality or
correctness of higher layers.
Discussion:  The implementation of layered structures with minimized interactions among
security functions and non-looping layers (i.e., lower-layer functions do not depend on
higher-layer functions) enables the isolation of security functions and the management of
complexity.
Related Controls:  None.
References:  None.
