---
schema_version: 1
corpus: federal-reference
jurisdiction: us
id: nist-sp-800-53-r5.ia-5
title: NIST SP 800-53 Rev. 5 IA-5 — AUTHENTICATOR MANAGEMENT
doc_type: federal_instrument
citation: NIST SP 800-53 Rev. 5 IA-5
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

**NIST SP 800-53 Rev. 5 IA-5** — AUTHENTICATOR MANAGEMENT

- Issued by: National Institute of Standards and Technology
- Publication: NIST SP 800-53 Rev. 5 — Security and Privacy Controls for Information Systems and Organizations ([nist-sp-800-53-r5](./nist-sp-800-53-r5.md))
- Version: Rev. 5 (September 2020, includes updates as of 2020-12-10)
- Text as of: 2026-11-12
- Cited by held documents: 74 times (cjis-sp-6-1 ×59, irs-pub-1075-11-2021 ×6, arc-ampe ×5, 6-cfr-37 ×4), 9 of them naming an enhancement of this control
- Reproduction basis: 17 U.S.C. § 105 — work of the U.S. government (NIST). Determined per document on 2026-11-12 against the publication itself, not assumed from its issuer: its Authority statement (PDF page 3) reads "This publication may be used by nongovernmental organizations on a voluntary basis and is not subject to copyright in the United States. Attribution would, however, be appreciated by NIST." Held here: the front matter and Chapter Three (the control catalog) only. Chapter Three names ISO/IEC standards solely as bibliographic references and reproduces none of their text. NOT mirrored: the References bibliography and Appendices A-C; Appendix A (glossary) adapts third-party definitions (ISO/IEC 15026, ISO 25237, ISO/IEC 29100, ISO 15288, IETF RFC 4949), which ADR-0002 treats as not reproducible by being incorporated, and whose reproducibility has not been determined.


_NON-AUTHORITATIVE copy of one control, cut from the SP 800-53 Rev. 5 snapshot this corpus holds. Whether and how this binds a given agency depends on the instrument that incorporates it — read it at the source URL before relying on it. This copy is the Rev. 5 text of record, which is not necessarily the text a citing document meant (a document citing Rev. 4 is not answered by it)._


## Full text

### IA-5 AUTHENTICATOR MANAGEMENT
Control:  Manage system authenticators by:
a. Verifying, as part of the initial authenticator distribution, the identity of the individual,
group, role, service, or device receiving the authenticator;
b. Establishing initial authenticator content for any authenticators issued by the organization;
c. Ensuring that authenticators have sufficient strength of mechanism for their intended use;
d. Establishing and implementing administrative procedures for initial authenticator
distribution, for lost or compromised or damaged authenticators, and for revoking
authenticators;
e. Changing default authenticators prior to first use;
f. Changing or refreshing authenticators [Assignment: organization-defined time period by
authenticator type] or when [Assignment: organization-defined events] occur;
g. Protecting authenticator content from unauthorized disclosure and modification;
h. Requiring individuals to take, and having devices implement, specific controls to protect
authenticators; and
i. Changing authenticators for group or role accounts when membership to those accounts
changes.
Discussion:  Authenticators include passwords, cryptographic devices, biometrics, certificates,
one-time password devices, and ID badges. Device authenticators include certificates and
passwords. Initial authenticator content is the actual content of the authenticator (e.g., the initial
password). In contrast, the requirements for authenticator content contain specific criteria or
characteristics (e.g., minimum password length). Developers may deliver system components
with factory default authentication credentials (i.e., passwords) to allow for initial installation
and configuration. Default authentication credentials are often well known, easily discoverable,
and present a significant risk. The requirement to protect individual authenticators may be
implemented via control PL-4 or PS-6 for authenticators in the possession of individuals and by
controls AC-3, AC-6, and SC-28 for authenticators stored in organizational systems, including
passwords stored in hashed or encrypted formats or files containing encrypted or hashed
passwords accessible with administrator privileges.
Systems support authenticator management by organization-defined settings and restrictions for
various authenticator characteristics (e.g., minimum password length, validation time window for
CHAPTER THREE   PAGE 139
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
time synchronous one-time tokens, and number of allowed rejections during the verification
stage of biometric authentication). Actions can be taken to safeguard individual authenticators,
including maintaining possession of authenticators, not sharing authenticators with others, and
immediately reporting lost, stolen, or compromised authenticators. Authenticator management
includes issuing and revoking authenticators for temporary access when no longer needed.
Related Controls:  AC-3, AC-6, CM-6, IA-2, IA-4, IA-7, IA-8, IA-9, MA-4, PE-2, PL-4, SC-12, SC-13.
Control Enhancements:
(1) AUTHENTICATOR MANAGEMENT | PASSWORD-BASED AUTHENTICATION
For password-based authentication:
(a) Maintain a list of commonly-used, expected, or compromised passwords and update
the list [Assignment: organization-defined frequency] and when organizational
passwords are suspected to have been compromised directly or indirectly;
(b) Verify, when users create or update passwords, that the passwords are not found on
the list of commonly-used, expected, or compromised passwords in IA-5(1)(a);
(c) Transmit passwords only over cryptographically-protected channels;
(d) Store passwords using an approved salted key derivation function, preferably using a
keyed hash;
(e) Require immediate selection of a new password upon account recovery;
(f) Allow user selection of long passwords and passphrases, including spaces and all
printable characters;
(g) Employ automated tools to assist the user in selecting strong password
authenticators; and
(h) Enforce the following composition and complexity rules: [Assignment: organization-
defined composition and complexity rules].
Discussion:  Password-based authentication applies to passwords regardless of whether they
are used in single-factor or multi-factor authentication. Long passwords or passphrases are
preferable over shorter passwords. Enforced composition rules provide marginal security
benefits while decreasing usability. However, organizations may choose to establish certain
rules for password generation (e.g., minimum character length for long passwords) under
certain circumstances and can enforce this requirement in IA-5(1)(h). Account recovery can
occur, for example, in situations when a password is forgotten. Cryptographically protected
passwords include salted one-way cryptographic hashes of passwords. The list of commonly
used, compromised, or expected passwords includes passwords obtained from previous
breach corpuses, dictionary words, and repetitive or sequential characters. The list includes
context-specific words, such as the name of the service, username, and derivatives thereof.
Related Controls:  IA-6.
(2) AUTHENTICATOR MANAGEMENT | PUBLIC KEY-BASED AUTHENTICATION
(a) For public key-based authentication:
(1) Enforce authorized access to the corresponding private key; and
(2) Map the authenticated identity to the account of the individual or group; and
(b) When public key infrastructure (PKI) is used:
(1) Validate certificates by constructing and verifying a certification path to an
accepted trust anchor, including checking certificate status information; and
(2) Implement a local cache of revocation data to support path discovery and
validation.
CHAPTER THREE   PAGE 140
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
Discussion:  Public key cryptography is a valid authentication mechanism for individuals,
machines, and devices. For PKI solutions, status information for certification paths includes
certificate revocation lists or certificate status protocol responses. For PIV cards, certificate
validation involves the construction and verification of a certification path to the Common
Policy Root trust anchor, which includes certificate policy processing. Implementing a local
cache of revocation data to support path discovery and validation also supports system
availability in situations where organizations are unable to access revocation information via
the network.
Related Controls:  IA-3, SC-17.
(3) AUTHENTICATOR MANAGEMENT | IN-PERSON OR TRUSTED EXTERNAL PARTY REGISTRATION
[Withdrawn: Incorporated into IA-12(4).]
(4) AUTHENTICATOR MANAGEMENT | AUTOMATED SUPPORT FOR PASSWORD STRENGTH
DETERMINATION
[Withdrawn: Incorporated into IA-5(1).]
(5) AUTHENTICATOR MANAGEMENT | CHANGE AUTHENTICATORS PRIOR TO DELIVERY
Require developers and installers of system components to provide unique authenticators
or change default authenticators prior to delivery and installation.
Discussion:  Changing authenticators prior to the delivery and installation of system
components extends the requirement for organizations to change default authenticators
upon system installation by requiring developers and/or installers to provide unique
authenticators or change default authenticators for system components prior to delivery
and/or installation. However, it typically does not apply to developers of commercial off-the-
shelf information technology products. Requirements for unique authenticators can be
included in acquisition documents prepared by organizations when procuring systems or
system components.
Related Controls:  None.
(6) AUTHENTICATOR MANAGEMENT | PROTECTION OF AUTHENTICATORS
Protect authenticators commensurate with the security category of the information to
which use of the authenticator permits access.
Discussion:  For systems that contain multiple security categories of information without
reliable physical or logical separation between categories, authenticators used to grant
access to the systems are protected commensurate with the highest security category of
information on the systems. Security categories of information are determined as part of the
security categorization process.
Related Controls:  RA-2.
(7) AUTHENTICATOR MANAGEMENT | NO EMBEDDED UNENCRYPTED STATIC AUTHENTICATORS
Ensure that unencrypted static authenticators are not embedded in applications or other
forms of static storage.
Discussion:  In addition to applications, other forms of static storage include access scripts
and function keys. Organizations exercise caution when determining whether embedded or
stored authenticators are in encrypted or unencrypted form. If authenticators are used in
the manner stored, then those representations are considered unencrypted authenticators.
Related Controls:  None.
(8) AUTHENTICATOR MANAGEMENT | MULTIPLE SYSTEM ACCOUNTS
Implement [Assignment: organization-defined security controls] to manage the risk of
compromise due to individuals having accounts on multiple systems.
CHAPTER THREE   PAGE 141
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
Discussion:  When individuals have accounts on multiple systems and use the same
authenticators such as passwords, there is the risk that a compromise of one account may
lead to the compromise of other accounts. Alternative approaches include having different
authenticators (passwords) on all systems, employing a single sign-on or federation
mechanism, or using some form of one-time passwords on all systems. Organizations can
also use rules of behavior (see PL-4) and access agreements (see PS-6) to mitigate the risk of
multiple system accounts.
Related Controls:  PS-6.
(9) AUTHENTICATOR MANAGEMENT | FEDERATED CREDENTIAL MANAGEMENT
Use the following external organizations to federate credentials: [Assignment:
organization-defined external organizations].
Discussion:  Federation provides organizations with the capability to authenticate individuals
and devices when conducting cross-organization activities involving the processing, storage,
or transmission of information. Using a specific list of approved external organizations for
authentication helps to ensure that those organizations are vetted and trusted.
Related Controls:  AU-7, AU-16.
(10) AUTHENTICATOR MANAGEMENT | DYNAMIC CREDENTIAL BINDING
Bind identities and authenticators dynamically using the following rules: [Assignment:
organization-defined binding rules].
Discussion:  Authentication requires some form of binding between an identity and the
authenticator that is used to confirm the identity. In conventional approaches, binding is
established by pre-provisioning both the identity and the authenticator to the system. For
example, the binding between a username (i.e., identity) and a password (i.e., authenticator)
is accomplished by provisioning the identity and authenticator as a pair in the system. New
authentication techniques allow the binding between the identity and the authenticator to
be implemented external to a system. For example, with smartcard credentials, the identity
and authenticator are bound together on the smartcard. Using these credentials, systems
can authenticate identities that have not been pre-provisioned, dynamically provisioning the
identity after authentication. In these situations, organizations can anticipate the dynamic
provisioning of identities. Pre-established trust relationships and mechanisms with
appropriate authorities to validate identities and related credentials are essential.
Related Controls:  AU-16, IA-5.
(11) AUTHENTICATOR MANAGEMENT | HARDWARE TOKEN-BASED AUTHENTICATION
[Withdrawn: Incorporated into IA-2(1) and IA-2(2).]
(12) AUTHENTICATOR MANAGEMENT | BIOMETRIC AUTHENTICATION PERFORMANCE
For biometric-based authentication, employ mechanisms that satisfy the following
biometric quality requirements [Assignment: organization-defined biometric quality
requirements].
Discussion:  Unlike password-based authentication, which provides exact matches of user-
input passwords to stored passwords, biometric authentication does not provide exact
matches. Depending on the type of biometric and the type of collection mechanism, there is
likely to be some divergence from the presented biometric and the stored biometric that
serves as the basis for comparison. Matching performance is the rate at which a biometric
algorithm correctly results in a match for a genuine user and rejects other users. Biometric
performance requirements include the match rate, which reflects the accuracy of the
biometric matching algorithm used by a system.
Related Controls:  AC-7.
CHAPTER THREE   PAGE 142
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
(13) AUTHENTICATOR MANAGEMENT | EXPIRATION OF CACHED AUTHENTICATORS
Prohibit the use of cached authenticators after [Assignment: organization-defined time
period].
Discussion:  Cached authenticators are used to authenticate to the local machine when the
network is not available. If cached authentication information is out of date, the validity of
the authentication information may be questionable.
Related Controls:  None.
(14) AUTHENTICATOR MANAGEMENT | MANAGING CONTENT OF PKI TRUST STORES
For PKI-based authentication, employ an organization-wide methodology for managing the
content of PKI trust stores installed across all platforms, including networks, operating
systems, browsers, and applications.
Discussion:  An organization-wide methodology for managing the content of PKI trust stores
helps improve the accuracy and currency of PKI-based authentication credentials across the
organization.
Related Controls:  None.
(15) AUTHENTICATOR MANAGEMENT | GSA-APPROVED PRODUCTS AND SERVICES
Use only General Services Administration-approved products and services for identity,
credential, and access management.
Discussion:  General Services Administration (GSA)-approved products and services are
products and services that have been approved through the GSA conformance program,
where applicable, and posted to the GSA Approved Products List. GSA provides guidance for
teams to design and build functional and secure systems that comply with Federal Identity,
Credential, and Access Management (FICAM) policies, technologies, and implementation
patterns.
Related Controls:  None.
(16) AUTHENTICATOR MANAGEMENT | IN-PERSON OR TRUSTED EXTERNAL PARTY AUTHENTICATOR
ISSUANCE
Require that the issuance of [Assignment: organization-defined types of and/or specific
authenticators] be conducted [Selection: in person; by a trusted external party] before
[Assignment: organization-defined registration authority] with authorization by
[Assignment: organization-defined personnel or roles].
Discussion:  Issuing authenticators in person or by a trusted external party enhances and
reinforces the trustworthiness of the identity proofing process.
Related Controls:  IA-12.
(17) AUTHENTICATOR MANAGEMENT | PRESENTATION ATTACK DETECTION FOR BIOMETRIC
AUTHENTICATORS
Employ presentation attack detection mechanisms for biometric-based authentication.
Discussion:  Biometric characteristics do not constitute secrets. Such characteristics can be
obtained by online web accesses, taking a picture of someone with a camera phone to
obtain facial images with or without their knowledge, lifting from objects that someone has
touched (e.g., a latent fingerprint), or capturing a high-resolution image (e.g., an iris
pattern). Presentation attack detection technologies including liveness detection, can
mitigate the risk of these types of attacks by making it difficult to produce artifacts intended
to defeat the biometric sensor.
Related Controls:  AC-7.
(18) AUTHENTICATOR MANAGEMENT | PASSWORD MANAGERS
CHAPTER THREE   PAGE 143
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-53r5
(a) Employ [Assignment: organization-defined password managers] to generate and
manage passwords; and
(b) Protect the passwords using [Assignment: organization-defined controls].
Discussion:  For systems where static passwords are employed, it is often a challenge to
ensure that the passwords are suitably complex and that the same passwords are not
employed on multiple systems. A password manager is a solution to this problem as it
automatically generates and stores strong and different passwords for various accounts. A
potential risk of using password managers is that adversaries can target the collection of
passwords generated by the password manager. Therefore, the collection of passwords
requires protection including encrypting the passwords (see IA-5(1)(d)) and storing the
collection offline in a token.
Related Controls:  None.
References:  [FIPS 140-3], [FIPS 180-4], [FIPS 201-2], [FIPS 202], [SP 800-63-3], [SP 800-73-4], [SP
800-76-2], [SP 800-78-4], [IR 7539], [IR 7817], [IR 7849], [IR 7870], [IR 8040].
