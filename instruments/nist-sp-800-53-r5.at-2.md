---
schema_version: 1
corpus: federal-reference
jurisdiction: us
id: nist-sp-800-53-r5.at-2
title: NIST SP 800-53 Rev. 5 AT-2 — LITERACY TRAINING AND AWARENESS
doc_type: federal_instrument
citation: NIST SP 800-53 Rev. 5 AT-2
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

**NIST SP 800-53 Rev. 5 AT-2** — LITERACY TRAINING AND AWARENESS

- Issued by: National Institute of Standards and Technology
- Publication: NIST SP 800-53 Rev. 5 — Security and Privacy Controls for Information Systems and Organizations ([nist-sp-800-53-r5](./nist-sp-800-53-r5.md))
- Version: Rev. 5 (September 2020, includes updates as of 2020-12-10)
- Text as of: 2026-11-12
- Cited by held documents: 23 times (cjis-sp-6-1 ×16, irs-pub-1075-11-2021 ×5, 6-cfr-37 ×1, arc-ampe ×1), 1 of them naming an enhancement of this control
- Reproduction basis: 17 U.S.C. § 105 — work of the U.S. government (NIST). Determined per document on 2026-11-12 against the publication itself, not assumed from its issuer: its Authority statement (PDF page 3) reads "This publication may be used by nongovernmental organizations on a voluntary basis and is not subject to copyright in the United States. Attribution would, however, be appreciated by NIST." Held here: the front matter and Chapter Three (the control catalog) only. Chapter Three names ISO/IEC standards solely as bibliographic references and reproduces none of their text. NOT mirrored: the References bibliography and Appendices A-C; Appendix A (glossary) adapts third-party definitions (ISO/IEC 15026, ISO 25237, ISO/IEC 29100, ISO 15288, IETF RFC 4949), which ADR-0002 treats as not reproducible by being incorporated, and whose reproducibility has not been determined.


_NON-AUTHORITATIVE copy of one control, cut from the SP 800-53 Rev. 5 snapshot this corpus holds. Whether and how this binds a given agency depends on the instrument that incorporates it — read it at the source URL before relying on it. This copy is the Rev. 5 text of record, which is not necessarily the text a citing document meant (a document citing Rev. 4 is not answered by it)._


## Full text

### AT-2 LITERACY TRAINING AND AWARENESS
Control:
a. Provide security and privacy literacy training to system users (including managers, senior
executives, and contractors):
1. As part of initial training for new users and [Assignment: organization-defined
frequency] thereafter; and
2. When required by system changes or following [Assignment: organization-defined
events];
b. Employ the following techniques to increase the security and privacy awareness of system
users [Assignment: organization-defined awareness techniques];
c. Update literacy training and awareness content [Assignment: organization-defined
frequency] and following [Assignment: organization-defined events]; and
d. Incorporate lessons learned from internal or external security incidents or breaches into
literacy training and awareness techniques.
Discussion:  Organizations provide basic and advanced levels of literacy training to system users,
including measures to test the knowledge level of users. Organizations determine the content of
literacy training and awareness based on specific organizational requirements, the systems to
which personnel have authorized access, and work environments (e.g., telework). The content
includes an understanding of the need for security and privacy as well as actions by users to
maintain security and personal privacy and to respond to suspected incidents. The content
addresses the need for operations security and the handling of personally identifiable
information.
Awareness techniques include displaying posters, offering supplies inscribed with security and
privacy reminders, displaying logon screen messages, generating email advisories or notices from
organizational officials, and conducting awareness events. Literacy training after the initial
training described in AT-2a.1 is conducted at a minimum frequency consistent with applicable
laws, directives, regulations, and policies. Subsequent literacy training may be satisfied by one or
more short ad hoc sessions and include topical information on recent attack schemes, changes to
organizational security and privacy policies, revised security and privacy expectations, or a subset
of topics from the initial training. Updating literacy training and awareness content on a regular
basis helps to ensure that the content remains relevant. Events that may precipitate an update to
literacy training and awareness content include, but are not limited to, assessment or audit
findings, security incidents or breaches, or changes in applicable laws, executive orders,
directives, regulations, policies, standards, and guidelines.
Related Controls:  AC-3, AC-17, AC-22, AT-3, AT-4, CP-3, IA-4, IR-2, IR-7, IR-9, PL-4, PM-13, PM-21,
PS-7, PT-2, SA-8, SA-16.
Control Enhancements:
(1) LITERACY TRAINING AND AWARENESS | PRACTICAL EXERCISES
Provide practical exercises in literacy training that simulate events and incidents.
Discussion:  Practical exercises include no-notice social engineering attempts to collect
information, gain unauthorized access, or simulate the adverse impact of opening malicious
email attachments or invoking, via spear phishing attacks, malicious web links.
Related Controls:  CA-2, CA-7, CP-4, IR-3.
(2) LITERACY TRAINING AND AWARENESS | INSIDER THREAT
Provide literacy training on recognizing and reporting potential indicators of insider threat.
CHAPTER THREE   PAGE 61
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
Discussion:  Potential indicators and possible precursors of insider threat can include
behaviors such as inordinate, long-term job dissatisfaction; attempts to gain access to
information not required for job performance; unexplained access to financial resources;
bullying or harassment of fellow employees; workplace violence; and other serious violations
of policies, procedures, directives, regulations, rules, or practices. Literacy training includes
how to communicate the concerns of employees and management regarding potential
indicators of insider threat through channels established by the organization and in
accordance with established policies and procedures. Organizations may consider tailoring
insider threat awareness topics to the role. For example, training for managers may be
focused on changes in the behavior of team members, while training for employees may be
focused on more general observations.
Related Controls:  PM-12.
(3) LITERACY TRAINING AND AWARENESS | SOCIAL ENGINEERING AND MINING
Provide literacy training on recognizing and reporting potential and actual instances of
social engineering and social mining.
Discussion:  Social engineering is an attempt to trick an individual into revealing information
or taking an action that can be used to breach, compromise, or otherwise adversely impact a
system. Social engineering includes phishing, pretexting, impersonation, baiting, quid pro
quo, thread-jacking, social media exploitation, and tailgating. Social mining is an attempt to
gather information about the organization that may be used to support future attacks.
Literacy training includes information on how to communicate the concerns of employees
and management regarding potential and actual instances of social engineering and data
mining through organizational channels based on established policies and procedures.
Related Controls:  None.
(4) LITERACY TRAINING AND AWARENESS | SUSPICIOUS COMMUNICATIONS AND ANOMALOUS SYSTEM
BEHAVIOR
Provide literacy training on recognizing suspicious communications and anomalous
behavior in organizational systems using [Assignment: organization-defined indicators of
malicious code].
Discussion:  A well-trained workforce provides another organizational control that can be
employed as part of a defense-in-depth strategy to protect against malicious code coming
into organizations via email or the web applications. Personnel are trained to look for
indications of potentially suspicious email (e.g., receiving an unexpected email, receiving an
email containing strange or poor grammar, or receiving an email from an unfamiliar sender
that appears to be from a known sponsor or contractor). Personnel are also trained on how
to respond to suspicious email or web communications. For this process to work effectively,
personnel are trained and made aware of what constitutes suspicious communications.
Training personnel on how to recognize anomalous behaviors in systems can provide
organizations with early warning for the presence of malicious code. Recognition of
anomalous behavior by organizational personnel can supplement malicious code detection
and protection tools and systems employed by organizations.
Related Controls:  None.
(5) LITERACY TRAINING AND AWARENESS | ADVANCED PERSISTENT THREAT
Provide literacy training on the advanced persistent threat.
Discussion:  An effective way to detect advanced persistent threats (APT) and to preclude
successful attacks is to provide specific literacy training for individuals. Threat literacy
training includes educating individuals on the various ways that APTs can infiltrate the
organization (e.g., through websites, emails, advertisement pop-ups, articles, and social
CHAPTER THREE   PAGE 62
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
engineering). Effective training includes techniques for recognizing suspicious emails, use of
removable systems in non-secure settings, and the potential targeting of individuals at
home.
Related Controls:  None.
(6) LITERACY TRAINING AND AWARENESS | CYBER THREAT ENVIRONMENT
(a) Provide literacy training on the cyber threat environment; and
(b) Reflect current cyber threat information in system operations.
Discussion:  Since threats continue to change over time, threat literacy training by the
organization is dynamic. Moreover, threat literacy training is not performed in isolation from
the system operations that support organizational mission and business functions.
Related Controls:  RA-3.
References:  [OMB A-130], [SP 800-50], [SP 800-160-2], [SP 800-181], [ODNI CTF].
