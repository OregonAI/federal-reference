---
schema_version: 1
corpus: federal-reference
jurisdiction: us
id: nist-sp-800-53-r5.ac-4
title: NIST SP 800-53 Rev. 5 AC-4 — INFORMATION FLOW ENFORCEMENT
doc_type: federal_instrument
citation: NIST SP 800-53 Rev. 5 AC-4
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

**NIST SP 800-53 Rev. 5 AC-4** — INFORMATION FLOW ENFORCEMENT

- Issued by: National Institute of Standards and Technology
- Publication: NIST SP 800-53 Rev. 5 — Security and Privacy Controls for Information Systems and Organizations ([nist-sp-800-53-r5](./nist-sp-800-53-r5.md))
- Version: Rev. 5 (September 2020, includes updates as of 2020-12-10)
- Text as of: 2026-11-12
- Cited by held documents: 34 times (cjis-sp-6-1 ×22, arc-ampe ×7, irs-pub-1075-11-2021 ×3, 6-cfr-37 ×2)
- Reproduction basis: 17 U.S.C. § 105 — work of the U.S. government (NIST). Determined per document on 2026-11-12 against the publication itself, not assumed from its issuer: its Authority statement (PDF page 3) reads "This publication may be used by nongovernmental organizations on a voluntary basis and is not subject to copyright in the United States. Attribution would, however, be appreciated by NIST." Held here: the front matter and Chapter Three (the control catalog) only. Chapter Three names ISO/IEC standards solely as bibliographic references and reproduces none of their text. NOT mirrored: the References bibliography and Appendices A-C; Appendix A (glossary) adapts third-party definitions (ISO/IEC 15026, ISO 25237, ISO/IEC 29100, ISO 15288, IETF RFC 4949), which ADR-0002 treats as not reproducible by being incorporated, and whose reproducibility has not been determined.


_NON-AUTHORITATIVE copy of one control, cut from the SP 800-53 Rev. 5 snapshot this corpus holds. Whether and how this binds a given agency depends on the instrument that incorporates it — read it at the source URL before relying on it. This copy is the Rev. 5 text of record, which is not necessarily the text a citing document meant (a document citing Rev. 4 is not answered by it)._


## Full text

### AC-4 INFORMATION FLOW ENFORCEMENT
Control:  Enforce approved authorizations for controlling the flow of information within the
system and between connected systems based on [Assignment: organization-defined
information flow control policies].
Discussion:  Information flow control regulates where information can travel within a system and
between systems (in contrast to who is allowed to access the information) and without regard to
subsequent accesses to that information. Flow control restrictions include blocking external
traffic that claims to be from within the organization, keeping export-controlled information
from being transmitted in the clear to the Internet, restricting web requests that are not from
the internal web proxy server, and limiting information transfers between organizations based
on data structures and content. Transferring information between organizations may require an
agreement specifying how the information flow is enforced (see CA-3). Transferring information
between systems in different security or privacy domains with different security or privacy
policies introduces the risk that such transfers violate one or more domain security or privacy
policies. In such situations, information owners/stewards provide guidance at designated policy
enforcement points between connected systems. Organizations consider mandating specific
architectural solutions to enforce specific security and privacy policies. Enforcement includes
prohibiting information transfers between connected systems (i.e., allowing access only),
verifying write permissions before accepting information from another security or privacy
domain or connected system, employing hardware mechanisms to enforce one-way information
CHAPTER THREE   PAGE 29
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
flows, and implementing trustworthy regrading mechanisms to reassign security or privacy
attributes and labels.
Organizations commonly employ information flow control policies and enforcement mechanisms
to control the flow of information between designated sources and destinations within systems
and between connected systems. Flow control is based on the characteristics of the information
and/or the information path. Enforcement occurs, for example, in boundary protection devices
that employ rule sets or establish configuration settings that restrict system services, provide a
packet-filtering capability based on header information, or provide a message-filtering capability
based on message content. Organizations also consider the trustworthiness of filtering and/or
inspection mechanisms (i.e., hardware, firmware, and software components) that are critical to
information flow enforcement. Control enhancements 3 through 32 primarily address cross-
domain solution needs that focus on more advanced filtering techniques, in-depth analysis, and
stronger flow enforcement mechanisms implemented in cross-domain products, such as high-
assurance guards. Such capabilities are generally not available in commercial off-the-shelf
products. Information flow enforcement also applies to control plane traffic (e.g., routing and
DNS).
Related Controls:  AC-3, AC-6, AC-16, AC-17, AC-19, AC-21, AU-10, CA-3, CA-9, CM-7, PL-9, PM-24,
SA-17, SC-4, SC-7, SC-16, SC-31.
Control Enhancements:
(1) INFORMATION FLOW ENFORCEMENT | OBJECT SECURITY AND PRIVACY ATTRIBUTES
Use [Assignment: organization-defined security and privacy attributes] associated with
[Assignment: organization-defined information, source, and destination objects] to enforce
[Assignment: organization-defined information flow control policies] as a basis for flow
control decisions.
Discussion:  Information flow enforcement mechanisms compare security and privacy
attributes associated with information (i.e., data content and structure) and source and
destination objects and respond appropriately when the enforcement mechanisms
encounter information flows not explicitly allowed by information flow policies. For
example, an information object labeled Secret would be allowed to flow to a destination
object labeled Secret, but an information object labeled Top Secret would not be allowed to
flow to a destination object labeled Secret. A dataset of personally identifiable information
may be tagged with restrictions against combining with other types of datasets and, thus,
would not be allowed to flow to the restricted dataset. Security and privacy attributes can
also include source and destination addresses employed in traffic filter firewalls. Flow
enforcement using explicit security or privacy attributes can be used, for example, to control
the release of certain types of information.
Related Controls:  None.
(2) INFORMATION FLOW ENFORCEMENT | PROCESSING DOMAINS
Use protected processing domains to enforce [Assignment: organization-defined
information flow control policies] as a basis for flow control decisions.
Discussion:  Protected processing domains within systems are processing spaces that have
controlled interactions with other processing spaces, enabling control of information flows
between these spaces and to/from information objects. A protected processing domain can
be provided, for example, by implementing domain and type enforcement. In domain and
type enforcement, system processes are assigned to domains, information is identified by
types, and information flows are controlled based on allowed information accesses (i.e.,
determined by domain and type), allowed signaling among domains, and allowed process
transitions to other domains.
CHAPTER THREE   PAGE 30
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
Related Controls:  SC-39.
(3) INFORMATION FLOW ENFORCEMENT | DYNAMIC INFORMATION FLOW CONTROL
Enforce [Assignment: organization-defined information flow control policies].
Discussion:  Organizational policies regarding dynamic information flow control include
allowing or disallowing information flows based on changing conditions or mission or
operational considerations. Changing conditions include changes in risk tolerance due to
changes in the immediacy of mission or business needs, changes in the threat environment,
and detection of potentially harmful or adverse events.
Related Controls:  SI-4.
(4) INFORMATION FLOW ENFORCEMENT | FLOW CONTROL OF ENCRYPTED INFORMATION
Prevent encrypted information from bypassing [Assignment: organization-defined
information flow control mechanisms] by [Selection (one or more): decrypting the
information; blocking the flow of the encrypted information; terminating communications
sessions attempting to pass encrypted information; [Assignment: organization-defined
procedure or method]].
Discussion:  Flow control mechanisms include content checking, security policy filters, and
data type identifiers. The term encryption is extended to cover encoded data not recognized
by filtering mechanisms.
Related Controls:  SI-4.
(5) INFORMATION FLOW ENFORCEMENT | EMBEDDED DATA TYPES
Enforce [Assignment: organization-defined limitations] on embedding data types within
other data types.
Discussion:  Embedding data types within other data types may result in reduced flow
control effectiveness. Data type embedding includes inserting files as objects within other
files and using compressed or archived data types that may include multiple embedded data
types. Limitations on data type embedding consider the levels of embedding and prohibit
levels of data type embedding that are beyond the capability of the inspection tools.
Related Controls:  None.
(6) INFORMATION FLOW ENFORCEMENT | METADATA
Enforce information flow control based on [Assignment: organization-defined metadata].
Discussion:  Metadata is information that describes the characteristics of data. Metadata can
include structural metadata describing data structures or descriptive metadata describing
data content. Enforcement of allowed information flows based on metadata enables simpler
and more effective flow control. Organizations consider the trustworthiness of metadata
regarding data accuracy (i.e., knowledge that the metadata values are correct with respect
to the data), data integrity (i.e., protecting against unauthorized changes to metadata tags),
and the binding of metadata to the data payload (i.e., employing sufficiently strong binding
techniques with appropriate assurance).
Related Controls:  AC-16, SI-7.
(7) INFORMATION FLOW ENFORCEMENT | ONE-WAY FLOW MECHANISMS
Enforce one-way information flows through hardware-based flow control mechanisms.
Discussion:  One-way flow mechanisms may also be referred to as a unidirectional network,
unidirectional security gateway, or data diode. One-way flow mechanisms can be used to
prevent data from being exported from a higher impact or classified domain or system while
permitting data from a lower impact or unclassified domain or system to be imported.
Related Controls:  None.
CHAPTER THREE   PAGE 31
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
(8) INFORMATION FLOW ENFORCEMENT | SECURITY AND PRIVACY POLICY FILTERS
(a) Enforce information flow control using [Assignment: organization-defined security or
privacy policy filters] as a basis for flow control decisions for [Assignment:
organization-defined information flows]; and
(b) [Selection (one or more): Block; Strip; Modify; Quarantine] data after a filter
processing failure in accordance with [Assignment: organization-defined security or
privacy policy].
Discussion:  Organization-defined security or privacy policy filters can address data
structures and content. For example, security or privacy policy filters for data structures can
check for maximum file lengths, maximum field sizes, and data/file types (for structured and
unstructured data). Security or privacy policy filters for data content can check for specific
words, enumerated values or data value ranges, and hidden content. Structured data
permits the interpretation of data content by applications. Unstructured data refers to
digital information without a data structure or with a data structure that does not facilitate
the development of rule sets to address the impact or classification level of the information
conveyed by the data or the flow enforcement decisions. Unstructured data consists of
bitmap objects that are inherently non-language-based (i.e., image, video, or audio files) and
textual objects that are based on written or printed languages. Organizations can implement
more than one security or privacy policy filter to meet information flow control objectives.
Related Controls:  None.
(9) INFORMATION FLOW ENFORCEMENT | HUMAN REVIEWS
Enforce the use of human reviews for [Assignment: organization-defined information
flows] under the following conditions: [Assignment: organization-defined conditions].
Discussion:  Organizations define security or privacy policy filters for all situations where
automated flow control decisions are possible. When a fully automated flow control decision
is not possible, then a human review may be employed in lieu of or as a complement to
automated security or privacy policy filtering. Human reviews may also be employed as
deemed necessary by organizations.
Related Controls:  None.
(10) INFORMATION FLOW ENFORCEMENT | ENABLE AND DISABLE SECURITY OR PRIVACY POLICY FILTERS
Provide the capability for privileged administrators to enable and disable [Assignment:
organization-defined security or privacy policy filters] under the following conditions:
[Assignment: organization-defined conditions].
Discussion:  For example, as allowed by the system authorization, administrators can enable
security or privacy policy filters to accommodate approved data types. Administrators also
have the capability to select the filters that are executed on a specific data flow based on the
type of data that is being transferred, the source and destination security domains, and
other security or privacy relevant features, as needed.
Related Controls:  None.
(11) INFORMATION FLOW ENFORCEMENT | CONFIGURATION OF SECURITY OR PRIVACY POLICY FILTERS
Provide the capability for privileged administrators to configure [Assignment:
organization-defined security or privacy policy filters] to support different security or
privacy policies.
Discussion:  Documentation contains detailed information for configuring security or privacy
policy filters. For example, administrators can configure security or privacy policy filters to
include the list of inappropriate words that security or privacy policy mechanisms check in
accordance with the definitions provided by organizations.
Related Controls:  None.
CHAPTER THREE   PAGE 32
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
(12) INFORMATION FLOW ENFORCEMENT | DATA TYPE IDENTIFIERS
When transferring information between different security domains, use [Assignment:
organization-defined data type identifiers] to validate data essential for information flow
decisions.
Discussion:  Data type identifiers include filenames, file types, file signatures or tokens, and
multiple internal file signatures or tokens. Systems only allow transfer of data that is
compliant with data type format specifications. Identification and validation of data types is
based on defined specifications associated with each allowed data format. The filename and
number alone are not used for data type identification. Content is validated syntactically and
semantically against its specification to ensure that it is the proper data type.
Related Controls:  None.
(13) INFORMATION FLOW ENFORCEMENT | DECOMPOSITION INTO POLICY-RELEVANT SUBCOMPONENTS
When transferring information between different security domains, decompose
information into [Assignment: organization-defined policy-relevant subcomponents] for
submission to policy enforcement mechanisms.
Discussion:  Decomposing information into policy-relevant subcomponents prior to
information transfer facilitates policy decisions on source, destination, certificates,
classification, attachments, and other security- or privacy-related component differentiators.
Policy enforcement mechanisms apply filtering, inspection, and/or sanitization rules to the
policy-relevant subcomponents of information to facilitate flow enforcement prior to
transferring such information to different security domains.
Related Controls:  None.
(14) INFORMATION FLOW ENFORCEMENT | SECURITY OR PRIVACY POLICY FILTER CONSTRAINTS
When transferring information between different security domains, implement
[Assignment: organization-defined security or privacy policy filters] requiring fully
enumerated formats that restrict data structure and content.
Discussion:  Data structure and content restrictions reduce the range of potential malicious
or unsanctioned content in cross-domain transactions. Security or privacy policy filters that
restrict data structures include restricting file sizes and field lengths. Data content policy
filters include encoding formats for character sets, restricting character data fields to only
contain alpha-numeric characters, prohibiting special characters, and validating schema
structures.
Related Controls:  None.
(15) INFORMATION FLOW ENFORCEMENT | DETECTION OF UNSANCTIONED INFORMATION
When transferring information between different security domains, examine the
information for the presence of [Assignment: organization-defined unsanctioned
information] and prohibit the transfer of such information in accordance with the
[Assignment: organization-defined security or privacy policy].
Discussion:  Unsanctioned information includes malicious code, information that is
inappropriate for release from the source network, or executable code that could disrupt or
harm the services or systems on the destination network.
Related Controls:  SI-3.
(16) INFORMATION FLOW ENFORCEMENT | INFORMATION TRANSFERS ON INTERCONNECTED SYSTEMS
[Withdrawn: Incorporated into AC-4.]
(17) INFORMATION FLOW ENFORCEMENT | DOMAIN AUTHENTICATION
CHAPTER THREE   PAGE 33
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
Uniquely identify and authenticate source and destination points by [Selection (one or
more): organization; system; application; service; individual] for information transfer.
Discussion:  Attribution is a critical component of a security and privacy concept of
operations. The ability to identify source and destination points for information flowing
within systems allows the forensic reconstruction of events and encourages policy
compliance by attributing policy violations to specific organizations or individuals. Successful
domain authentication requires that system labels distinguish among systems, organizations,
and individuals involved in preparing, sending, receiving, or disseminating information.
Attribution also allows organizations to better maintain the lineage of personally identifiable
information processing as it flows through systems and can facilitate consent tracking, as
well as correction, deletion, or access requests from individuals.
Related Controls:  IA-2, IA-3, IA-9.
(18) INFORMATION FLOW ENFORCEMENT | SECURITY ATTRIBUTE BINDING
[Withdrawn: Incorporated into AC-16.]
(19) INFORMATION FLOW ENFORCEMENT | VALIDATION OF METADATA
When transferring information between different security domains, implement
[Assignment: organization-defined security or privacy policy filters] on metadata.
Discussion:  All information (including metadata and the data to which the metadata applies)
is subject to filtering and inspection. Some organizations distinguish between metadata and
data payloads (i.e., only the data to which the metadata is bound). Other organizations do
not make such distinctions and consider metadata and the data to which the metadata
applies to be part of the payload.
Related Controls:  None.
(20) INFORMATION FLOW ENFORCEMENT | APPROVED SOLUTIONS
Employ [Assignment: organization-defined solutions in approved configurations] to control
the flow of [Assignment: organization-defined information] across security domains.
Discussion:  Organizations define approved solutions and configurations in cross-domain
policies and guidance in accordance with the types of information flows across classification
boundaries. The National Security Agency (NSA) National Cross Domain Strategy and
Management Office provides a listing of approved cross-domain solutions. Contact
ncdsmo@nsa.gov for more information.
Related Controls:  None.
(21) INFORMATION FLOW ENFORCEMENT | PHYSICAL OR LOGICAL SEPARATION OF INFORMATION FLOWS
Separate information flows logically or physically using [Assignment: organization-defined
mechanisms and/or techniques] to accomplish [Assignment: organization-defined required
separations by types of information].
Discussion:  Enforcing the separation of information flows associated with defined types of
data can enhance protection by ensuring that information is not commingled while in transit
and by enabling flow control by transmission paths that are not otherwise achievable. Types
of separable information include inbound and outbound communications traffic, service
requests and responses, and information of differing security impact or classification levels.
Related Controls:  SC-32.
(22) INFORMATION FLOW ENFORCEMENT | ACCESS ONLY
Provide access from a single device to computing platforms, applications, or data residing
in multiple different security domains, while preventing information flow between the
different security domains.
CHAPTER THREE   PAGE 34
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
Discussion:  The system provides a capability for users to access each connected security
domain without providing any mechanisms to allow users to transfer data or information
between the different security domains. An example of an access-only solution is a terminal
that provides a user access to information with different security classifications while
assuredly keeping the information separate.
Related Controls:  None.
(23) INFORMATION FLOW ENFORCEMENT | MODIFY NON-RELEASABLE INFORMATION
When transferring information between different security domains, modify non-releasable
information by implementing [Assignment: organization-defined modification action].
Discussion:  Modifying non-releasable information can help prevent a data spill or attack
when information is transferred across security domains. Modification actions include
masking, permutation, alteration, removal, or redaction.
Related Controls:  None.
(24) INFORMATION FLOW ENFORCEMENT | INTERNAL NORMALIZED FORMAT
When transferring information between different security domains, parse incoming data
into an internal normalized format and regenerate the data to be consistent with its
intended specification.
Discussion:  Converting data into normalized forms is one of most of effective mechanisms
to stop malicious attacks and large classes of data exfiltration.
Related Controls:  None.
(25) INFORMATION FLOW ENFORCEMENT | DATA SANITIZATION
When transferring information between different security domains, sanitize data to
minimize [Selection (one or more): delivery of malicious content, command and control of
malicious code, malicious code augmentation, and steganography encoded data; spillage
of sensitive information] in accordance with [Assignment: organization-defined policy]].
Discussion:  Data sanitization is the process of irreversibly removing or destroying data
stored on a memory device (e.g., hard drives, flash memory/solid state drives, mobile
devices, CDs, and DVDs) or in hard copy form.
Related Controls:  MP-6.
(26) INFORMATION FLOW ENFORCEMENT | AUDIT FILTERING ACTIONS
When transferring information between different security domains, record and audit
content filtering actions and results for the information being filtered.
Discussion:  Content filtering is the process of inspecting information as it traverses a cross-
domain solution and determines if the information meets a predefined policy. Content
filtering actions and the results of filtering actions are recorded for individual messages to
ensure that the correct filter actions were applied. Content filter reports are used to assist in
troubleshooting actions by, for example, determining why message content was modified
and/or why it failed the filtering process. Audit events are defined in AU-2. Audit records are
generated in AU-12.
Related Controls:  AU-2, AU-3, AU-12.
(27) INFORMATION FLOW ENFORCEMENT | REDUNDANT/INDEPENDENT FILTERING MECHANISMS
When transferring information between different security domains, implement content
filtering solutions that provide redundant and independent filtering mechanisms for each
data type.
Discussion:  Content filtering is the process of inspecting information as it traverses a cross-
domain solution and determines if the information meets a predefined policy. Redundant
CHAPTER THREE   PAGE 35
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
and independent content filtering eliminates a single point of failure filtering system.
Independence is defined as the implementation of a content filter that uses a different code
base and supporting libraries (e.g., two JPEG filters using different vendors’ JPEG libraries)
and multiple, independent system processes.
Related Controls:  None.
(28) INFORMATION FLOW ENFORCEMENT | LINEAR FILTER PIPELINES
When transferring information between different security domains, implement a linear
content filter pipeline that is enforced with discretionary and mandatory access controls.
Discussion:  Content filtering is the process of inspecting information as it traverses a cross-
domain solution and determines if the information meets a predefined policy. The use of
linear content filter pipelines ensures that filter processes are non-bypassable and always
invoked. In general, the use of parallel filtering architectures for content filtering of a single
data type introduces bypass and non-invocation issues.
Related Controls:  None.
(29) INFORMATION FLOW ENFORCEMENT | FILTER ORCHESTRATION ENGINES
When transferring information between different security domains, employ content filter
orchestration engines to ensure that:
(a) Content filtering mechanisms successfully complete execution without errors; and
(b) Content filtering actions occur in the correct order and comply with [Assignment:
organization-defined policy].
Discussion:  Content filtering is the process of inspecting information as it traverses a cross-
domain solution and determines if the information meets a predefined security policy. An
orchestration engine coordinates the sequencing of activities (manual and automated) in a
content filtering process. Errors are defined as either anomalous actions or unexpected
termination of the content filter process. This is not the same as a filter failing content due
to non-compliance with policy. Content filter reports are a commonly used mechanism to
ensure that expected filtering actions are completed successfully.
Related Controls:  None.
(30) INFORMATION FLOW ENFORCEMENT | FILTER MECHANISMS USING MULTIPLE PROCESSES
When transferring information between different security domains, implement content
filtering mechanisms using multiple processes.
Discussion:  The use of multiple processes to implement content filtering mechanisms
reduces the likelihood of a single point of failure.
Related Controls:  None.
(31) INFORMATION FLOW ENFORCEMENT | FAILED CONTENT TRANSFER PREVENTION
When transferring information between different security domains, prevent the transfer
of failed content to the receiving domain.
Discussion:  Content that failed filtering checks can corrupt the system if transferred to the
receiving domain.
Related Controls:  None.
(32) INFORMATION FLOW ENFORCEMENT | PROCESS REQUIREMENTS FOR INFORMATION TRANSFER
When transferring information between different security domains, the process that
transfers information between filter pipelines:
(a) Does not filter message content;
(b) Validates filtering metadata;
CHAPTER THREE   PAGE 36
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
(c) Ensures the content associated with the filtering metadata has successfully completed
filtering; and
(d) Transfers the content to the destination filter pipeline.
Discussion:  The processes transferring information between filter pipelines have minimum
complexity and functionality to provide assurance that the processes operate correctly.
Related Controls:  None.
References:  [SP-800-160-1], [SP 800-162], [SP 800-178], [IR 8112].
