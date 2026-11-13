---
schema_version: 1
corpus: federal-reference
jurisdiction: us
id: nist-sp-800-53-r5.si-19
title: NIST SP 800-53 Rev. 5 SI-19 — DE-IDENTIFICATION
doc_type: federal_instrument
citation: NIST SP 800-53 Rev. 5 SI-19
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

**NIST SP 800-53 Rev. 5 SI-19** — DE-IDENTIFICATION

- Issued by: National Institute of Standards and Technology
- Publication: NIST SP 800-53 Rev. 5 — Security and Privacy Controls for Information Systems and Organizations ([nist-sp-800-53-r5](./nist-sp-800-53-r5.md))
- Version: Rev. 5 (September 2020, includes updates as of 2020-12-10)
- Text as of: 2026-11-12
- Cited by held documents: 1 time (arc-ampe ×1), 1 of them naming an enhancement of this control
- Reproduction basis: 17 U.S.C. § 105 — work of the U.S. government (NIST). Determined per document on 2026-11-12 against the publication itself, not assumed from its issuer: its Authority statement (PDF page 3) reads "This publication may be used by nongovernmental organizations on a voluntary basis and is not subject to copyright in the United States. Attribution would, however, be appreciated by NIST." Held here: the front matter and Chapter Three (the control catalog) only. Chapter Three names ISO/IEC standards solely as bibliographic references and reproduces none of their text. NOT mirrored: the References bibliography and Appendices A-C; Appendix A (glossary) adapts third-party definitions (ISO/IEC 15026, ISO 25237, ISO/IEC 29100, ISO 15288, IETF RFC 4949), which ADR-0002 treats as not reproducible by being incorporated, and whose reproducibility has not been determined.


_NON-AUTHORITATIVE copy of one control, cut from the SP 800-53 Rev. 5 snapshot this corpus holds. Whether and how this binds a given agency depends on the instrument that incorporates it — read it at the source URL before relying on it. This copy is the Rev. 5 text of record, which is not necessarily the text a citing document meant (a document citing Rev. 4 is not answered by it)._


## Full text

### SI-19 DE-IDENTIFICATION
Control:
a. Remove the following elements of personally identifiable information from datasets:
[Assignment: organization-defined elements of personally identifiable information]; and
b. Evaluate [Assignment: organization-defined frequency] for effectiveness of de-identification.
Discussion:  De-identification is the general term for the process of removing the association
between a set of identifying data and the data subject. Many datasets contain information about
individuals that can be used to distinguish or trace an individual’s identity, such as name, social
security number, date and place of birth, mother’s maiden name, or biometric records. Datasets
may also contain other information that is linked or linkable to an individual, such as medical,
educational, financial, and employment information. Personally identifiable information is
removed from datasets by trained individuals when such information is not (or no longer)
necessary to satisfy the requirements envisioned for the data. For example, if the dataset is only
used to produce aggregate statistics, the identifiers that are not needed for producing those
statistics are removed. Removing identifiers improves privacy protection since information that is
removed cannot be inadvertently disclosed or improperly used.
Organizations may be subject to
specific de-identification definitions or methods under applicable laws, regulations, or policies.
Re-identification is a residual risk with de-identified data. Re-identification attacks can vary,
including combining new datasets or other improvements in data analytics. Maintaining
awareness of potential attacks and evaluating for the effectiveness of the de-identification over
time support the management of this residual risk.
Related Controls:  MP-6, PM-22, PM-23, PM-24, RA-2, SI-12.
Control Enhancements:
(1) DE-IDENTIFICATION | COLLECTION
De-identify the dataset upon collection by not collecting personally identifiable
information.
Discussion:  If a data source contains personally identifiable information but the information
will not be used, the dataset can be de-identified when it is created by not collecting the
CHAPTER THREE   PAGE 359
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
data elements that contain the personally identifiable information. For example, if an
organization does not intend to use the social security number of an applicant, then
application forms do not ask for a social security number.
Related Controls:  None.
(2) DE-IDENTIFICATION | ARCHIVING
Prohibit archiving of personally identifiable information elements if those elements in a
dataset will not be needed after the dataset is archived.
Discussion:  Datasets can be archived for many reasons. The envisioned purposes for the
archived dataset are specified, and if personally identifiable information elements are not
required, the elements are not archived. For example, social security numbers may have
been collected for record linkage, but the archived dataset may include the required
elements from the linked records. In this case, it is not necessary to archive the social
security numbers.
Related Controls:  None.
(3) DE-IDENTIFICATION | RELEASE
Remove personally identifiable information elements from a dataset prior to its release if
those elements in the dataset do not need to be part of the data release.
Discussion:  Prior to releasing a dataset, a data custodian considers the intended uses of the
dataset and determines if it is necessary to release personally identifiable information. If the
personally identifiable information is not necessary, the information can be removed using
de-identification techniques.
Related Controls:  None.
(4) DE-IDENTIFICATION | REMOVAL, MASKING, ENCRYPTION, HASHING, OR REPLACEMENT OF DIRECT
IDENTIFIERS
Remove, mask, encrypt, hash, or replace direct identifiers in a dataset.
Discussion:  There are many possible processes for removing direct identifiers from a
dataset. Columns in a dataset that contain a direct identifier can be removed. In masking,
the direct identifier is transformed into a repeating character, such as XXXXXX or 999999.
Identifiers can be encrypted or hashed so that the linked records remain linked. In the case
of encryption or hashing, algorithms are employed that require the use of a key, including
the Advanced Encryption Standard or a Hash-based Message Authentication Code.
Implementations may use the same key for all identifiers or use a different key for each
identifier. Using a different key for each identifier provides a higher degree of security and
privacy. Identifiers can alternatively be replaced with a keyword, including transforming
“George Washington” to “PATIENT” or replacing it with a surrogate value, such as
transforming “George Washington” to “Abraham Polk.”
Related Controls:  SC-12, SC-13.
(5) DE-IDENTIFICATION | STATISTICAL DISCLOSURE CONTROL
Manipulate numerical data, contingency tables, and statistical findings so that no
individual or organization is identifiable in the results of the analysis.
Discussion:  Many types of statistical analyses can result in the disclosure of information
about individuals even if only summary information is provided. For example, if a school that
publishes a monthly table with the number of minority students enrolled, reports that it has
10-19 such students in January, and subsequently reports that it has 20-29 such students in
March, then it can be inferred that the student who enrolled in February was a minority.
Related Controls:  None.
CHAPTER THREE   PAGE 360
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
(6) DE-IDENTIFICATION | DIFFERENTIAL PRIVACY
Prevent disclosure of personally identifiable information by adding non-deterministic
noise to the results of mathematical operations before the results are reported.
Discussion:  The mathematical definition for differential privacy holds that the result of a
dataset analysis should be approximately the same before and after the addition or removal
of a single data record (which is assumed to be the data from a single individual). In its most
basic form, differential privacy applies only to online query systems. However, it can also be
used to produce machine-learning statistical classifiers and synthetic data. Differential
privacy comes at the cost of decreased accuracy of results, forcing organizations to quantify
the trade-off between privacy protection and the overall accuracy, usefulness, and utility of
the de-identified dataset. Non-deterministic noise can include adding small, random values
to the results of mathematical operations in dataset analysis.
Related Controls:  SC-12, SC-13.
(7) DE-IDENTIFICATION | VALIDATED ALGORITHMS AND SOFTWARE
Perform de-identification using validated algorithms and software that is validated to
implement the algorithms.
Discussion:  Algorithms that appear to remove personally identifiable information from a
dataset may in fact leave information that is personally identifiable or data that is re-
identifiable. Software that is claimed to implement a validated algorithm may contain bugs
or implement a different algorithm. Software may de-identify one type of data, such as
integers, but not de-identify another type of data, such as floating point numbers. For these
reasons, de-identification is performed using algorithms and software that are validated.
Related Controls:  None.
(8) DE-IDENTIFICATION | MOTIVATED INTRUDER
Perform a motivated intruder test on the de-identified dataset to determine if the
identified data remains or if the de-identified data can be re-identified.
Discussion:  A motivated intruder test is a test in which an individual or group takes a data
release and specified resources and attempts to re-identify one or more individuals in the
de-identified dataset. Such tests specify the amount of inside knowledge, computational
resources, financial resources, data, and skills that intruders possess to conduct the tests. A
motivated intruder test can determine if the de-identification is insufficient. It can also be a
useful diagnostic tool to assess if de-identification is likely to be sufficient. However, the test
alone cannot prove that de-identification is sufficient.
Related Controls:  None.
References:  [OMB A-130], [SP 800-188].
