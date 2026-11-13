---
schema_version: 1
corpus: federal-reference
jurisdiction: us
id: nist-sp-800-53-r5.si-10
title: NIST SP 800-53 Rev. 5 SI-10 — INFORMATION INPUT VALIDATION
doc_type: federal_instrument
citation: NIST SP 800-53 Rev. 5 SI-10
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

**NIST SP 800-53 Rev. 5 SI-10** — INFORMATION INPUT VALIDATION

- Issued by: National Institute of Standards and Technology
- Publication: NIST SP 800-53 Rev. 5 — Security and Privacy Controls for Information Systems and Organizations ([nist-sp-800-53-r5](./nist-sp-800-53-r5.md))
- Version: Rev. 5 (September 2020, includes updates as of 2020-12-10)
- Text as of: 2026-11-12
- Cited by held documents: 14 times (cjis-sp-6-1 ×9, irs-pub-1075-11-2021 ×3, 6-cfr-37 ×1, arc-ampe ×1), 1 of them naming an enhancement of this control
- Reproduction basis: 17 U.S.C. § 105 — work of the U.S. government (NIST). Determined per document on 2026-11-12 against the publication itself, not assumed from its issuer: its Authority statement (PDF page 3) reads "This publication may be used by nongovernmental organizations on a voluntary basis and is not subject to copyright in the United States. Attribution would, however, be appreciated by NIST." Held here: the front matter and Chapter Three (the control catalog) only. Chapter Three names ISO/IEC standards solely as bibliographic references and reproduces none of their text. NOT mirrored: the References bibliography and Appendices A-C; Appendix A (glossary) adapts third-party definitions (ISO/IEC 15026, ISO 25237, ISO/IEC 29100, ISO 15288, IETF RFC 4949), which ADR-0002 treats as not reproducible by being incorporated, and whose reproducibility has not been determined.


_NON-AUTHORITATIVE copy of one control, cut from the SP 800-53 Rev. 5 snapshot this corpus holds. Whether and how this binds a given agency depends on the instrument that incorporates it — read it at the source URL before relying on it. This copy is the Rev. 5 text of record, which is not necessarily the text a citing document meant (a document citing Rev. 4 is not answered by it)._


## Full text

### SI-10  INFORMATION INPUT VALIDATION
Control:  Check the validity of the following information inputs: [Assignment: organization-
defined information inputs to the system].
Discussion:  Checking the valid syntax and semantics of system inputs—including character set,
length, numerical range, and acceptable values—verifies that inputs match specified definitions
for format and content. For example, if the organization specifies that numerical values between
1-100 are the only acceptable inputs for a field in a given application, inputs of “387,” “abc,” or
“%K%” are invalid inputs and are not accepted as input to the system. Valid inputs are likely to
vary from field to field within a software application. Applications typically follow well-defined
protocols that use structured messages (i.e., commands or queries) to communicate between
software modules or system components. Structured messages can contain raw or unstructured
data interspersed with metadata or control information. If software applications use attacker-
supplied inputs to construct structured messages without properly encoding such messages,
then the attacker could insert malicious commands or special characters that can cause the data
CHAPTER THREE   PAGE 350
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
to be interpreted as control information or metadata. Consequently, the module or component
that receives the corrupted output will perform the wrong operations or otherwise interpret the
data incorrectly. Prescreening inputs prior to passing them to interpreters prevents the content
from being unintentionally interpreted as commands. Input validation ensures accurate and
correct inputs and prevents attacks such as cross-site scripting and a variety of injection attacks.
Related Controls:  None.
Control Enhancements:
(1) INFORMATION INPUT VALIDATION | MANUAL OVERRIDE CAPABILITY
(a) Provide a manual override capability for input validation of the following information
inputs: [Assignment: organization-defined inputs defined in the base control (SI-10)];
(b) Restrict the use of the manual override capability to only [Assignment: organization-
defined authorized individuals]; and
(c) Audit the use of the manual override capability.
Discussion:  In certain situations, such as during events that are defined in contingency plans,
a manual override capability for input validation may be needed. Manual overrides are used
only in limited circumstances and with the inputs defined by the organization.
Related Controls:  AC-3, AU-2, AU-12.
(2) INFORMATION INPUT VALIDATION | REVIEW AND RESOLVE ERRORS
Review and resolve input validation errors within [Assignment: organization-defined time
period].
Discussion:  Resolution of input validation errors includes correcting systemic causes of
errors and resubmitting transactions with corrected input. Input validation errors are those
related to the information inputs defined by the organization in the base control (SI-10).
Related Controls:  None.
(3) INFORMATION INPUT VALIDATION | PREDICTABLE BEHAVIOR
Verify that the system behaves in a predictable and documented manner when invalid
inputs are received.
Discussion:  A common vulnerability in organizational systems is unpredictable behavior
when invalid inputs are received. Verification of system predictability helps ensure that the
system behaves as expected when invalid inputs are received. This occurs by specifying
system responses that allow the system to transition to known states without adverse,
unintended side effects. The invalid inputs are those related to the information inputs
defined by the organization in the base control (SI-10).
Related Controls:  None.
(4) INFORMATION INPUT VALIDATION | TIMING INTERACTIONS
Account for timing interactions among system components in determining appropriate
responses for invalid inputs.
Discussion:  In addressing invalid system inputs received across protocol interfaces, timing
interactions become relevant, where one protocol needs to consider the impact of the error
response on other protocols in the protocol stack. For example, 802.11 standard wireless
network protocols do not interact well with Transmission Control Protocols (TCP) when
packets are dropped (which could be due to invalid packet input). TCP assumes packet losses
are due to congestion, while packets lost over 802.11 links are typically dropped due to noise
or collisions on the link. If TCP makes a congestion response, it takes the wrong action in
response to a collision event. Adversaries may be able to use what appear to be acceptable
individual behaviors of the protocols in concert to achieve adverse effects through suitable
CHAPTER THREE   PAGE 351
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
construction of invalid input. The invalid inputs are those related to the information inputs
defined by the organization in the base control (SI-10).
Related Controls:  None.
(5) INFORMATION INPUT VALIDATION | RESTRICT INPUTS TO TRUSTED SOURCES AND APPROVED
FORMATS
Restrict the use of information inputs to [Assignment: organization-defined trusted
sources] and/or [Assignment: organization-defined formats].
Discussion:  Restricting the use of inputs to trusted sources and in trusted formats applies
the concept of authorized or permitted software to information inputs. Specifying known
trusted sources for information inputs and acceptable formats for such inputs can reduce
the probability of malicious activity. The information inputs are those defined by the
organization in the base control (SI-10).
Related Controls:  AC-3, AC-6.
(6) INFORMATION INPUT VALIDATION | INJECTION PREVENTION
Prevent untrusted data injections.
Discussion: Untrusted data injections may be prevented using a parameterized interface or
output escaping (output encoding). Parameterized interfaces separate data from code so
that injections of malicious or unintended data cannot change the semantics of commands
being sent. Output escaping uses specified characters to inform the interpreter’s parser
whether data is trusted. Prevention of untrusted data injections are with respect to the
information inputs defined by the organization in the base control (SI-10).
Related Controls:  AC-3, AC-6.
References:  [OMB A-130].
