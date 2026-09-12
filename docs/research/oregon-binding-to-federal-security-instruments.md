# Is a named Oregon agency bound to these eight federal security instruments?

**Research note.** Written 2026-09-11 to unpark issues #22, #23, #24 and #25, which all ask
the same question of eight instruments and were all blocked on the same evidentiary
problem.

> **This directory is new.** `docs/research/` did not exist before this file. The
> convention it establishes: a research note is a *dated finding about the world*, not a
> corpus document and not a decision. It carries no `schema_version` front matter, is not
> served over MCP, and is not indexed in `llms.txt`. ADRs in `docs/adr/` record what this
> corpus decided; notes here record what was checked, by whom, on what date, and what was
> **not** settled. A note goes stale; an ADR does not. Date every claim here accordingly.

## The bar this note holds

Issue #22 states it and this note does not relax it:

> **"Mandatory in practice" is an assertion, not evidence.**

Evidence is ranked, strongest first, and every finding below is labelled with the tier it
actually reached:

| Tier | What it is |
|---|---|
| **T1** | An Oregon statute (ORS) or administrative rule (OAR) naming the instrument |
| **T2** | An Oregon agency contract, IGA, or data-exchange agreement incorporating it |
| **T3** | An Oregon agency policy or published security plan citing it as binding |
| **T4** | A federal grant condition Oregon demonstrably accepted (grant named, acceptance named) |
| **T5** | A federal program document asserting applicability to states generally — **weakest, not sufficient alone** |

`COULD NOT DETERMINE` is a result, not a failure. Where it appears, the places searched are
named. Nothing here is padded to avoid saying it.

## Summary

| Instrument | Verdict | Strongest evidence | Tier | Issue |
|---|---|---|---|---|
| **MARS-E** (now **ARC-AMPE**) | **BOUND** | ODHS\|OHA ISPO policies 090-004/-006/-009/-016 name ARC-AMPE, 090-013 names MARS-E v2.2, as governing references; CMS makes it mandatory for the State Medicaid Agency, State CHIP Agency, State BHP and SBE | T3 + T5 | #22 |
| **USDA FNS Handbook 901** | **COULD NOT DETERMINE** — *and the premise needs correcting* | Handbook 901 is the **Advance Planning Document** handbook, not a security standard. The SNAP security obligation lives in **7 CFR 277.18(m)**, a regulation. No Oregon document found naming either. | — | #22 |
| **SSA TSSR** | **BOUND** | Seven ODHS\|OHA ISPO policies cite "Social Security Administration Information Exchange Security Requirements and Procedures" as a governing reference; 090-003 ¶17 states the obligation | T3 | #24 |
| **PCI-DSS** | **BOUND** | DOC Policy 30.1.5 §III.A.1–2 requires DOC payment-card systems to conform to current PCI DSS; OAM 10.35.00.PR ¶.137 states agencies "must also comply" | T3 | #23 |
| **NIMS** | **BOUND** | OAR 104-010-0005(3)(b) makes NIMS compliance an EMPG eligibility condition; ORS 401.038(1) requires NIMS training of state agency heads; ORS 404.110/404.120 require NIMS ICS for search and rescue | T1 | #25 |
| **CISA CPGs** | **NOT BOUND** (as a compliance obligation) | The 2023 Oregon Cybersecurity Plan commits to "support, promote, and utilize" CPGs — aspirational language, not a control requirement; CPGs are **not** among SLCGP's seven mandatory best practices | — | #25 |
| **FedRAMP** | **BOUND, conditionally** — not statewide | IRS Pub 1075 §3.3.1(a) makes FedRAMP authorization mandatory for any cloud holding FTI, and ten ODHS\|OHA policies name Pub 1075 as governing. Statewide cloud policy DAS 107-004-150 says FedRAMP "may also be acceptable" — i.e. optional | T3 → T5 chain | #23 |
| **StateRAMP / GovRAMP** | **NOT BOUND** | Statewide standards were "developed using" and "informed by" StateRAMP baselines — influence, not obligation; DAS's own 2024 briefing says Oregon "is in the process of adopting"; the 2025 draft cloud policy makes GovRAMP an *exemption route*, not a requirement | — | #23 |

**Copyright:** PCI-DSS — **summary plus official link only**. StateRAMP/GovRAMP — **summary
plus official link only**; the "not a U.S. government work" flag in issue #23 is
**confirmed**.

---

## 1. MARS-E — **BOUND** (as superseded by ARC-AMPE)

**Named Oregon agencies:** Oregon Health Authority and Oregon Department of Human Services,
through the shared ODHS|OHA Information Security and Privacy Office (ISPO).

### The instrument moved, and that matters before anything else

CMS retired MARS-E during the period these issues sat parked. ARC-AMPE Volume I,
Version 1.01 (March 10, 2025), footnote 6:

> "ARC-AMPE supersedes and replaces MARS-E and the NEE GRC Framework effective upon
> publication."

— <https://www.cms.gov/files/document/arc-ampe-vol-1-v102-508-5cr-04112025.pdf> (retrieved
2026-09-11; the cover sheet reads Version 1.02, the running footer Version 1.01 — a
discrepancy in CMS's own document, recorded rather than resolved).

**Anything ingested under the name "MARS-E" would be ingesting a superseded instrument.**
AGENTS.md rule 3 — "Never present a superseded version as current" — applies directly.

### Oregon-side evidence (T3)

Four ODHS|OHA ISPO policies name ARC-AMPE by its full current title in their governing
`References` block:

- `oha-ispo-090-004` — Information Security and Privacy Awareness and Training Policy, line 159–160
- `oha-ispo-090-006` — line 183
- `oha-ispo-090-009` — Administrative, Technical and Physical Safeguards of Information Policy, line 220
- `oha-ispo-090-016` — line 126

Reading as: "Acceptable Risk Controls for Affordable Care Act (ACA), Medicaid, and Partner
Entities (ARC-AMPE)". Two more (`oha-ispo-090-005`, `oha-ispo-090-011`) carry the older
shorthand "ARCAMP". Corpus documents in `executive-regulatory-frameworks`; source URLs of
the form `https://sharedsystems.dhsoha.state.or.us/DHSForms/Served/me090-0NN.pdf`.

The predecessor is named too. `oha-ispo-090-013` (Administrative Privileges Policy, ODHS|OHA
090-013, effective 2022-03-07, last update 2025-08-01, source
<https://sharedsystems.dhsoha.state.or.us/DHSForms/Served//me090-013.pdf>) lists under
`References`:

> "Minimum Acceptable Risk Safeguards for Exchanges (MARS-E) Document Suite, Volume 1:
> Harmonized Security and Privacy Framework, Version 2.2"

Note that ODHS|OHA writes "Safeguards" where CMS writes "Standards" — the agency's own
citation is slightly off, which is itself a reason for this corpus to hold a canonical
entry.

**How binding, precisely.** These are `References` blocks, not operative clauses, so the
tier is T3 and not higher. The operative hook is `oha-ispo-090-013` ¶8, which requires third
parties to comply "with any applicable federal requirements," and the References block is
the agency's own statement of which federal requirements those are. This is an agency policy
citing the instrument as governing — not a rule, and not a contract.

### Federal-side evidence (T5)

ARC-AMPE Volume I §1.3.2 defines the mandatory population:

> "ACA Administering Entity (ACA AE) – Exchanges, whether federal or state, state Medicaid
> agencies, state CHIP agencies, or state agencies administering a BHP."

§3.1, Table 2 (Mandatory ARC-AMPE Implementation) lists as mandatory: State Medicaid Agency
("State Integrated Eligibility & Enrollment System (IES) connected to FFE through the Hub"),
State CHIP Agency, State Basic Health Program (BHP), and State-based Exchange (SBE).
§4.1 supplies the enforcement mechanism:

> "Authorization of the entity's connection to the Hub is documented in the Interconnection
> Security Agreement (ISA). The ISA establishes the Authority to Connect (ATC) for AEs."

Oregon lands in that table more than once:

- **State Medicaid / CHIP agency:** OHA administers the Oregon Health Plan through the ONE
  eligibility system (<https://www.oregon.gov/oha/ohp/pages/one.aspx>).
- **State BHP:** OHA administers OHP Bridge, Oregon's § 1331 Basic Health Program. CMS
  blueprint: <https://www.medicaid.gov/basic-health-program/downloads/or-basic-hlth-prgm-blprnt.pdf>;
  Oregon's contract: <https://www.oregon.gov/oha/HSD/OHP/Documents/2025-BHP-Contract.pdf>.
- **Exchange:** CMS lists Oregon under "State-based Exchanges on the Federal Platform for
  Plan Year 2026" and under "States seeking to transition to a State-based Exchange for Plan
  Year 2027" — <https://www.cms.gov/cciio/resources/fact-sheets-and-faqs/state-marketplaces>
  (page last modified 08/14/2026, retrieved 2026-09-11). The Oregon Health Insurance
  Marketplace is a division of the **Department of Consumer and Business Services**, per the
  issuing body of OAR chapter 945 (e.g. OAR 945-001-0002, legal authority ORS 741.002 —
  <https://secure.sos.state.or.us/oard/view.action?ruleNumber=945-001-0002>).

**inference:** the ISA/ATC that binds OHA is a non-public agreement between OHA and CMS. The
existence of a signed ISA for Oregon was not verified — only that CMS's published framework
requires one for entities in Oregon's categories. A T2 citation almost certainly exists and
is not public.

### What is missing

- No OAR or ORS names MARS-E or ARC-AMPE (0 hits across `rules/`, `statutes/` in
  `executive-regulatory-frameworks`).
- No Secretary of State audit measures any Oregon agency against MARS-E or ARC-AMPE: 0 hits
  for "MARS-E", "ARC-AMPE", "ARCAMP" and "Minimum Acceptable Risk" across all 242 reports in
  `oregon-audits/reports/` (report dates 2020-02-01 through 2026-07-01).

### Verdict

**BOUND** — T3 (Oregon agency policy) reinforced by T5 (CMS mandatory-implementation table).
If this corpus ingests the instrument, it ingests **ARC-AMPE v1.01/1.02 (2025)**, not
MARS-E 2.2, and records MARS-E as superseded.

---

## 2. USDA FNS Handbook 901 — **COULD NOT DETERMINE** (and the question is mis-framed)

**The premise needs correcting before the verdict means anything.** Issue #22 lists FNS
Handbook 901 as a security instrument. It is not one. FNS's own page describes it as the
Advance Planning Document handbook:

> "The primary objective of this Handbook is to help state agencies navigate FNS
> requirements to secure approval, and get the requested funding, for modern eligibility
> systems and electronic benefit transfer (EBT) benefit delivery services."

— <https://www.fns.usda.gov/sso/apd/handbook-901> and
<https://www.fns.usda.gov/sso/fns-handbook-901-v2-advance-planning-documents> (both
retrieved 2026-09-11; the first timed out on direct fetch and is cited from the FNS-hosted
search result — **flagged as not directly retrieved**).

The actual SNAP information-system security obligation is a **regulation**, not a handbook.
7 CFR 277.18(m)(2):

> "State agencies shall implement and maintain a comprehensive Security Program for IS and
> installations involved in the administration of the SNAP."

and (m)(3):

> "State agencies shall review the security of IS involved in the administration of SNAP on
> a biennial basis."

— retrieved 2026-09-11 from
<https://www.govinfo.gov/content/pkg/CFR-2024-title7-vol4/xml/CFR-2024-title7-vol4-sec277-18.xml>.
Handbook 901 is referenced in that same section at paragraph (d), for APD *content*
requirements — funding approval, not security controls. (eCFR was not usable:
`www.ecfr.gov` redirected every request to `https://unblock.federalregister.gov/` on
2026-09-11.)

### Where I looked for Oregon-side evidence, and found none

- `executive-regulatory-frameworks`, across `agencies/`, `rules/`, `statutes/`,
  `executive-orders/`, `external-references/`: **0** documents contain "Handbook 901" or
  "FNS Handbook".
- `oregon-audits/reports/`, all 242 reports: **0** contain "Handbook 901". The five reports
  that mention Food and Nutrition Service at all (2020-14, 2021-09, 2021-13, 2022-18,
  2023-21) mention it for waivers and program approvals, not security — e.g. 2022-18 line
  469, "Department of Agriculture Food and Nutrition Services provided a waiver allowing
  states to…".
- Web search restricted to `oregon.gov` for "Handbook 901": no Oregon page returned.

### Verdict

**COULD NOT DETERMINE.** No Oregon agency document naming FNS Handbook 901 was found, and
the handbook is in any case the wrong instrument for a security corpus. **Next step is to
ask, not to read more** — see the closing section.

---

## 3. SSA TSSR — **BOUND**

**Named Oregon agencies:** OHA and ODHS (ISPO). The Department of Corrections and Oregon
Youth Authority also hold SSA data per their own policies, but their SSA references were not
run down.

### Oregon-side evidence (T3)

Seven ODHS|OHA ISPO policies cite the SSA requirements document by name in their governing
`References` block: `oha-ispo-090-003`, `-004`, `-005`, `-006`, `-007`, `-009`, `-011` — all
in `executive-regulatory-frameworks/agencies/oregon-health-authority/policies/`. The cited
title is:

> "Social Security Administration Information Exchange Security Requirements and Procedures"

The operative clause is `oha-ispo-090-003` (Access Control Policy, ODHS|OHA 090-003, source
<https://sharedsystems.dhsoha.state.or.us/DHSForms/Served/ME090-003.pdf>) ¶17:

> "Social Security Administration (SSA) data shall only be accessed or used by ODHS and OHA
> staff in accordance with the SSA's information security safeguard requirements. For
> additional information related to SSA safeguard requirements, staff shall contact the
> Information Security and Privacy Office (ISPO)."

`oha-ispo-090-011` (Media Protection and Disposal Policy, effective 2021-07-12) ¶3 lists
"Social Security Administration (SSA) information" as a protected information class subject
to the policy's storage and transport controls.

The statewide security plan corroborates that SSA audits Oregon against these requirements.
`eis-css-secplan` (DAS Enterprise Information Services / Cyber Security Services), line 1634:

> "Security assessments may also include CJIS audits, Social Security Administration (SSA)
> audits,"

### On the name "TSSR"

The instrument Oregon cites and the instrument issue #24 calls "TSSR" appear to be the same
document under two names — SSA's "Electronic Information Exchange Security Requirements and
Procedures For State and Local Agencies Exchanging Electronic Information With The Social
Security Administration," historically abbreviated TSSR (Technical System Security
Requirements). **This equivalence is not confirmed from ssa.gov.**

**Access failure, recorded:** `www.ssa.gov` returned **HTTP 403** to every automated request
on 2026-09-11 — both `WebFetch` and `curl` with a browser user agent, against
<https://www.ssa.gov/dataexchange/security.html> and
<https://www.ssa.gov/dataexchange/documents/IEA(S)%20State%20Agency%20Level.pdf>
(Akamai edge denial, reference `18.ccd50b17.1789193731.24172e01`). The document is also
distributed by SSA to exchange partners rather than posted openly. Copies exist on other
states' sites (Minnesota Commerce, Illinois HFS) — **those are primary as to Minnesota and
Illinois, not as to Oregon, and not as to SSA's current version**, so they are not cited
here as authority.

### Verdict

**BOUND** — T3, on Oregon's own policies, which is the tier that matters. The federal text
is a separate problem: it is not reliably public, and this corpus should not claim to hold
it without a retrievable, versioned copy from ssa.gov.

**inference:** a T2 citation exists — the Information Exchange Agreement between SSA and the
Oregon agency — and it is not public.

---

## 4. PCI-DSS — **BOUND**

**Named Oregon agencies:** Department of Corrections (operative policy); all state agencies
accepting cards, via the DAS Oregon Accounting Manual.

### Oregon-side evidence (T3)

**DOC Policy 30.1.5, "Customer Credit Card Payment," effective 2025-01-30**
(<https://www.oregon.gov/doc/rules-and-policies/Documents/30-1-5-readoption.pdf>;
corpus id `doc-30-1-5`). §III.A:

> "1. All DOC systems associated with payment cards will be developed and maintained in
> accordance with, but not limited to current PCI DSS standards.
> 2. All transactions associated with payment cards will be conducted in accordance with,
> but not limited to current PCI DSS standards."

and §I:

> "This policy provides direction and support for information security in accordance with
> business requirements and relevant laws and regulations including but not limited to the
> Department of Corrections (DOC) Information Security Plan and the Payment Card Industry
> Data Security Standards (PCI DSS)."

This is an operative requirement in the policy body, not a reference-list entry — the
strongest T3 finding in this note.

**OAM 10.35.00.PR, "Credit card acceptance for payment — procedure"** (DAS Chief Financial
Office / Office of the State Controller;
<https://www.oregon.gov/das/Financial/Acctng/Documents/10.35.00.pr.pdf>; corpus id
`oam-10-35-00-pr`), ¶.137:

> "Agencies that store, process or transmit cardholder information associated with credit
> card transactions must also comply with applicable industry data security standards. Visa,
> MasterCard, American Express, and Discover card brands require compliance with the Payment
> Card Industry Data Security Standard (PCI-DSS)."

¶.138 imposes specific PCI-derived storage prohibitions ("State agencies are required to
implement a credit card processing system that does not store…"). ¶.140 is weaker — agencies
"should work with OST to ensure they are PCI-DSS compliant."

Two further ODHS|OHA policies treat PCI data as a protected class with mandatory handling
and breach-reporting rules: `oha-ispo-090-011` ¶3(f) and `oha-ispo-090-015` ¶9.

**Not chased:** OAM ¶.141 points to **Oregon State Treasury Policy 02 18 14.PO** for third-
party card processor prequalification. That policy is not held in
`executive-regulatory-frameworks` and was not retrieved. It is the most likely home of a
harder, contractual PCI obligation.

### Verdict

**BOUND** — T3, on an operative clause in DOC 30.1.5 and a "must comply" statement in the
statewide accounting manual. Note the obligation's true origin is **card-brand contract**,
not federal law: OAM ¶.137 says the *card brands* require it. PCI-DSS is in this corpus's
scope only because Oregon agencies are contractually bound, not because a federal program
imposes it.

---

## 5. NIMS — **BOUND** (the only T1 finding in this note)

**Named Oregon agencies:** Oregon Department of Emergency Management (ODEM); every state
agency head; county sheriffs.

### Oregon-side evidence (T1 — administrative rule)

**OAR 104-010-0005**, "Participation of Local and Tribal Governments in the Emergency
Management Performance Grant (EMPG) Program of the Federal Emergency Management Agency
(FEMA)" — issuing body Oregon Military Department / Office of Emergency Management, statutory
authority ORS 401.092, implementing ORS 401.096, OEM 33-2023 effective 2023-10-11
(<https://secure.sos.state.or.us/oard/view.action?ruleNumber=104-010-0005>). Section (3):

> "Each county, tribal government and city must meet the following requirements to be
> eligible to participate in the program: (a) Have an assigned emergency manager. **(b) Be
> National Incident Management System (NIMS) compliant.** …"

Section (8) attaches consequences: failure may result in "no funding for the next fiscal
year, forfeiture of grants funds already received…, non-reimbursement of outstanding
requested expenditures."

### Oregon-side evidence (T1 — statute)

**ORS 401.038(1)** (2025 Edition):

> "All elected officials in this state, all administrative heads of state agencies and all
> persons in the state government management service as defined in ORS 240.212 shall
> complete introductory courses offered or approved by the Federal Emergency Management
> Agency on incident command and the National Incident Management System."

**ORS 404.110** requires unified command "as outlined in the National Incident Management
System Incident Command System established by Homeland Security Presidential Directive 5 of
February 28, 2003"; **ORS 404.120** requires county search and rescue plans to "comply with
the relevant provisions of" the same. **OAR 259-009-0062** (DPSST) recognises NWCG's
"National Incident Management System: Wildland Qualification System Guide (PMS 310-1)" for
wildland fire certifications.

### Federal-side evidence (T4/T5)

FEMA, <https://www.fema.gov/emergency-managers/nims/implementation-training> (retrieved
2026-09-11):

> "Local, state, tribal and territorial jurisdictions are required to adopt NIMS in order to
> receive federal Preparedness Grants."

### Verdict

**BOUND** — T1. An Oregon administrative rule names the instrument and conditions grant
eligibility on compliance with it; an Oregon statute mandates training in it. This is the
cleanest binding of the eight and the only one that does not depend on an agency policy.

**Scope caveat:** OAR 104-010-0005(3)(b) binds *local and tribal* EMPG participants. ODEM's
own NIMS compliance is a condition of FEMA's award to ODEM as State Administrative Agency,
not of this rule. The audits corpus contains no finding measuring an Oregon agency against
NIMS: 2 of 242 reports mention "National Incident Management" at all.

---

## 6. CISA Cross-Sector Cybersecurity Performance Goals — **NOT BOUND**

**Named Oregon agencies:** ODEM (State Administrative Agency for SLCGP); DAS Enterprise
Information Services / Cyber Security Services (program administrator); the State CISO
(Planning Committee chair).

### What Oregon actually committed to

The **2023 Oregon Cybersecurity Plan**, "Approved by State of Oregon Planning Committee on
7/31/23" (<https://www.oregon.gov/oem/Documents/Oregon-Cybersecurity-Plan.pdf>), lists under
Objective 2.3 "Drive improvements to Oregon's cybersecurity posture" the action item:

> "Support, promote, and utilize CISA's Cross Sector Cybersecurity Performance Goals to
> evaluate and establish baseline configurations for IT and OT systems."

That is the **only** mention of CPGs in the entire plan. "Support, promote, and utilize" is
not "comply with," and no control, deadline, assessment or consequence attaches to it. The
plan names the responsible parties:

> "The Oregon Department of Emergency Management (ODEM) is the State Administrative Agency
> (SAA) for Oregon. ODEM is the SLCGP grant administrator… Enterprise Information Services
> through Cyber Security Service (CSS) is the SLCGP program administrator for Oregon."

### Oregon demonstrably accepted the grant (T4 — but for a different obligation)

ODEM's January 2025 legislative report on the SLCGP, responding to Budget Note 7 of Oregon
Laws 2024 ch. 114 (SB 5701)
(<https://www.oregon.gov/oem/Documents/2025-A258-CyberSecurity-Report.pdf>):

> "Under the Homeland Security Act of 2002, as amended by the Bipartisan Infrastructure Law
> (BIL), SLCGP grant recipients must develop a Cybersecurity Plan, establish a Cybersecurity
> Planning Committee to support plan development and identify projects for implementation
> using SLCGP funding… Through a partnership between OEM and the Oregon Department of
> Administrative Services, Office of Enterprise Information Services/Cyber Security Services
> (DAS-EIS/CSS), Oregon completed the required Cybersecurity Plan and established a
> pass-through grant program"

So Oregon accepted the grant and met its conditions. **The conditions do not include the
CPGs.** CISA's SLCGP FAQ
(<https://www.cisa.gov/state-and-local-cybersecurity-grant-program-frequently-asked-questions>,
retrieved 2026-09-11) enumerates what the plan must contain:

> "the Cybersecurity Plan must discuss the below seven best practices: Multi-factor
> authentication; Enhanced logging; Data encryption for data at rest and in transit; End use
> of unsupported/end of life software and hardware that are accessible from the Internet;
> Prohibit use of known/fixed/default passwords and credentials; The ability to reconstitute
> systems (backups); and Migration to the .gov internet domain."

CPGs are not in that list, and the FAQ does not mention them at all.

### Corroborating absences

- `executive-regulatory-frameworks`: **0** documents across `agencies/`, `rules/`,
  `statutes/`, `executive-orders/`, `external-references/` contain "CISA",
  "Cross-Sector", "Cross Sector" or "Cybersecurity Performance Goals".
- `oregon-audits/reports/`: **0** of 242 reports contain "Cybersecurity Performance Goals".

### Verdict

**NOT BOUND.** Positive evidence: the federal grant's own required-elements list excludes
CPGs; Oregon's own plan frames CPGs as something to "support, promote, and utilize"; no
Oregon rule, statute, policy or audit names them anywhere. Oregon **uses** the CPGs. Nothing
found **requires** it to.

---

## 7. FedRAMP — **BOUND for FTI in the cloud; NOT a statewide requirement**

### The statewide cloud policy makes FedRAMP optional

**DAS Statewide Policy 107-004-150, "Cloud and Hosted Systems"** (Office of the State CIO,
legal authority ORS 276A.206, effective 2019-05-01, last reviewed 2019-05-25;
<https://www.oregon.gov/das/Policies/107-004-150.pdf>; corpus id `das-107-004-150`):

> "While there is no single audit standard that is uniformly required, the state frequently
> accepts a SOC2 Type 2 audit covering all five Trust Services Criteria. **Other types of
> audits or certifications, such as FedRAMP, may also be acceptable.** Agencies should work
> with OSCIO throughout the process to ensure that audit standards are acceptable."

"May also be acceptable" is positive evidence of **no** statewide obligation. This is the
only mention of FedRAMP in the whole of `executive-regulatory-frameworks`.

### FedRAMP's own statute does not reach Oregon

The FedRAMP Authorization Act (Pub. L. 117-263) sits in 44 U.S.C. ch. 36. 44 U.S.C.
§ 3607(a) provides that "the definitions under sections 3502 and 3552 apply to this section
through section 3616," and 44 U.S.C. § 3502(1) defines "agency" as:

> "any executive department, military department, Government corporation, Government
> controlled corporation, or other establishment in the executive branch of the Government
> (including the Executive Office of the President), or any independent regulatory agency…"

— <https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title44-section3502&num=0&edition=prelim>
(retrieved 2026-09-11). State governments are not within that definition. FedRAMP binds
federal agencies; it does not, of its own force, bind Oregon.

### But a federal instrument Oregon *is* bound to makes it mandatory

**IRS Publication 1075 (Rev. 11-2021) § 3.3.1, "Cloud Computing"** — held in this corpus as
`instruments/irs-pub-1075-11-2021.md`:

> "To use a cloud computing model to receive, process, store, access, protect and/or
> transmit FTI, the agency must comply with all requirements in this publication. The
> following mandatory requirements are in effect for using cloud services to receive,
> process, store, access, protect and/or transmit FTI:
> **a. FedRAMP Authorization: FTI may only be introduced to cloud environments that have
> been provided an authorization by the Joint Advisory Board (JAB) or a Federal Agency.**"

Pub 1075 § 2.E.6.1 additionally requires agencies to "Document the cloud service provider's
FedRAMP authorization" in the 45-day notification, and AC-3(CE-9) makes "FedRAMP ATO" one of
the controls validating release of FTI.

Ten ODHS|OHA ISPO policies name IRS Publication 1075 as a governing reference
(`oha-ispo-090-003` through `-016`), and OAR 407-007-0020(1)(e) requires a five-yearly
criminal records check where a position "requires use or access to FTI"
(<https://secure.sos.state.or.us/oard/view.action?ruleNumber=407-007-0020>) — an Oregon rule
that presupposes the FTI safeguarding regime without naming Pub 1075.

**inference:** an Oregon agency placing FTI in a cloud environment is therefore bound to use
a FedRAMP-authorized provider, via Pub 1075 rather than via FedRAMP directly. This is a
two-step chain — Oregon policy → Pub 1075 → FedRAMP — and no Oregon document found states
the FedRAMP requirement in its own words. The conclusion is inferred from the chain, not
cited from a single Oregon source.

Separately, **CJIS Security Policy 6.1** (held as `instruments/cjis-sp-6-1.md`) declines to
make FedRAMP sufficient:

> "When selecting a cloud service provider, the CJIS ISO Program reminds agencies the CJIS
> Security Policy sets the minimum requirements for the protection of CJI. Additional
> security assurances from other authorizations such as FedRAMP, StateRAMP, SOC Type 2,
> etc., may be leveraged, however, they do not guarantee compliance with the CJIS Security
> Policy."

### Verdict

**BOUND, conditionally.** Not statewide; not by FedRAMP's own statute; mandatory for any
Oregon agency putting federal tax information in a cloud, through IRS Pub 1075 § 3.3.1(a).
The right framing for the corpus is not "Oregon is bound to FedRAMP" but "Pub 1075 § 3.3.1
incorporates FedRAMP, and Pub 1075 is already held here."

---

## 8. StateRAMP / GovRAMP — **NOT BOUND**

**First, the name changed.** StateRAMP rebranded to GovRAMP. Its own Security Assessment
Framework v4.2 (April 2026) reads: "a steering committee of government and industry leaders
chartered StateRAMP dba GovRAMP ('GovRAMP')"
(<https://govramp.org/hubfs/GovRAMP%20Security%20Assessment%20Framework%20(July%202026).pdf>).
Searching Oregon sources for "StateRAMP" alone will increasingly miss things.

### Oregon names it as a design input, never as a requirement

**Statewide Information Technology (IT) Control Standards (January 2024)**, DAS Enterprise
Information Services / Cyber Security Services, legal authority ORS 276A.300
(<https://www.oregon.gov/eis/cyber-security-services/Documents/eis-css-statewide-information-technology(IT)-control-standards.pdf>;
corpus id `eis-css-itcs`):

> "These Standards have been developed using reference documents from the following
> resources: National Institute of Standards and Technology (NIST); **State Risk and
> Authorization Management Program (StateRAMP) Baselines**; Federal, State, and Local
> Statues and Rules"

**2023 Statewide Information Security Program Plan** (same issuing body, v1.2 final review
2023-12-08;
<https://www.oregon.gov/eis/cyber-security-services/Documents/eis-css-statewide-information-security-program-plan.pdf>;
corpus id `eis-css-program-plan-2023`), §2 and §3.2:

> "The requirements documented herein are based on the Statewide Standards, which were
> developed to align with NIST SP800-53 and **informed by** the State Risk and Authorization
> Management Program (StateRAMP)."

> "The State of Oregon has adopted the NIST family of cybersecurity controls, as well as the
> programmatic activities outlined in NIST SP800-53, **in conjunction with StateRAMP**."

Oregon adopted **NIST**. StateRAMP "informed" the standards. No control in either document
requires a StateRAMP authorization of anyone.

### DAS's own briefing says adoption was still prospective in 2024

**"State of Oregon StateRAMP Adoption — Designated Procurement Officer (DPO)," June 26,
2024, Sherri Yoakum, CSS Business Security Advisor Manager**
(<https://www.oregon.gov/das/Procurement/Documents/DPO-StateRAMP.pdf>):

> "Oregon is in the process of adopting the StateRAMP vendor authorization process."

and, in the conditional:

> "Oregon follows NIST 800-53 standards for cybersecurity but lacks pre-procurement audits.
> **StateRAMP would fill this gap** with upfront and continuous security checks."

### The 2025 draft cloud policy makes GovRAMP an exemption, not a mandate

Draft replacement for statewide policy 107-004-150, posted for comment 2025-07-18, approved
signature block Terrence Woods, State CIO, superseding the 2019 version
(<https://www.oregon.gov/eis/Documents/107-004-150%2020250718%20For%20Comment.pdf>):

> "Note: Cloud services providers with current GovRAMP moderate or higher authorization and
> with CSS having visibility to the GovRAMP artifacts **will not be required to complete the
> Cloud Checklist**"

That is a route *out of* a state requirement, not into one. **This draft has a blank
effective date and is a comment draft;** the 2019 policy is what
`executive-regulatory-frameworks` carries as current (retrieved 2026-07-17). Whether the
draft has since been adopted was not checked.

### Corroborating absences

- No OAR or ORS names StateRAMP or GovRAMP (0 hits in `rules/`, `statutes/`).
- No DAS procurement rule in OAR chapter 125 mentions StateRAMP, FedRAMP, "Payment Card" or
  NIST (0 hits in `rules/125/`).
- `oregon-audits/reports/`: **0** of 242 reports mention StateRAMP or GovRAMP.
- CJIS SP 6.1 (quoted in §7 above) expressly says StateRAMP authorization "do[es] not
  guarantee compliance."

### Verdict

**NOT BOUND.** Oregon uses StateRAMP/GovRAMP baselines as a reference and offers GovRAMP
authorization as a procurement shortcut. Every Oregon document found describes it as an
input, an option, or a work in progress — none as an obligation.

---

## Copyright and reproducibility

Both determinations below are per-document determinations under
[ADR-0002](../adr/0002-copyright-decided-per-document.md), made 2026-09-11 from the terms as
published on that date. Neither rests on "federal, therefore publishable" — neither is
federal.

### PCI-DSS — **summary plus official link only**

Issue #23 asked for this first because it sizes the work. It sizes it **down**.

PCI Security Standards Council Terms and Conditions,
<https://www.pcisecuritystandards.org/terms_and_conditions/> (retrieved 2026-09-11). The
limited grant permits only that a user may:

> "view, download and print any materials and information owned and made available by the
> Council on or through the Services…solely for your own personal, non-commercial, review,
> study and informational purposes."

And the prohibition:

> "Except for the limited rights expressly granted herein, or as otherwise required by law
> or granted pursuant to a separate written agreement between you and the Council, you may
> not publish, distribute, copy, assign, license, sublicense, transfer, sell, prepare of
> derivative works of, or use for any non-personal purpose, any Content; and all right,
> title and interest in and to the Services and all Content is hereby reserved."

*(“prepare of derivative works” is PCI SSC's own typo, quoted as printed.)* Site footer:

> "Copyright © 2006 – 2026 PCI Security Standards Council, LLC. All rights reserved."

**Determination.** PCI DSS is the copyrighted work of a private LLC. The only granted use is
personal, non-commercial review. Publishing a mirror in this corpus — even excerpts —
exceeds the grant. **`reproduction: summary`**, `doc_type: external_reference`, which the
schema already forces to `content_mode: summary`.

`reproduction_basis` for the manifest entry, as determined:

> "PCI SSC Terms and Conditions reviewed 2026-09-11: grant is limited to personal,
> non-commercial review; publishing, distributing, copying and derivative works are
> expressly prohibited. Summary and official link only; no excerpting."

**Note for OAM 10.35.00.PR and DOC 30.1.5:** ADR-0002's incorporation-by-reference warning
applies exactly here. Those Oregon policies are freely reproducible; the PCI DSS text they
point at is not.

### StateRAMP / GovRAMP — flag **CONFIRMED**; summary plus official link only

GovRAMP is a private nonprofit, not a U.S. government body. Its Security Assessment
Framework v4.2 (April 2026) states:

> "GovRAMP operates as a 501(c)6 nonprofit."

17 U.S.C. § 105 does not apply. GovRAMP Terms & Conditions,
<https://govramp.org/terms-conditions> (retrieved 2026-09-11):

> "All content published and made available on our Site is the property of GovRAMP and the
> Site's creators. This includes, but is not limited to images, text, logos, documents,
> downloadable files and anything that contributes to the composition of our Site."

Site footer: "© 2026 GovRAMP".

**What the terms do *not* say, stated plainly:** they contain no express prohibition on
reproduction and no express license permitting it. There is an ownership assertion and no
grant. Absent a grant, the default under copyright is that reproduction is not permitted —
so the determination is the same as if a prohibition had been printed, but the *basis* is
different and the manifest entry must say which it is.

**Determination.** **`reproduction: summary`**, `doc_type: external_reference`.

`reproduction_basis` as determined:

> "GovRAMP (StateRAMP dba GovRAMP) is a 501(c)(6) nonprofit, not a U.S. government body;
> 17 U.S.C. § 105 does not apply. Terms & Conditions reviewed 2026-09-11 assert GovRAMP
> ownership of all site content including downloadable documents and grant no reproduction
> license. Summary and official link only, on absence of a grant rather than on an express
> prohibition."

**Recorded for whoever ingests this:** the baselines themselves are derived from NIST SP
800-53, which *is* freely reproducible. The NIST control text is not made un-free by
GovRAMP's packaging of it — but GovRAMP's selection, tailoring and accompanying prose are
its own. Mirroring "the StateRAMP baseline" would mirror both. Don't.

---

## What this resolves, and what it does not

### Issue #22 — MARS-E and USDA FNS

- **MARS-E: resolved.** BOUND, T3+T5. The ingest target is **ARC-AMPE v1.01/1.02 (2025)**,
  not MARS-E 2.2 — reopen the issue's scope before ingesting. ARC-AMPE Volume I is a CMS
  work; reproducibility appears straightforward but is **a separate per-document
  determination that this note did not make**.
- **FNS Handbook 901: not resolved, and mis-scoped.** The security obligation is
  7 CFR 277.18(m), which this corpus does not hold (it holds 7 CFR 273, not 277).
  **Recommendation: close the FNS half of #22 and open a new issue for 7 CFR 277.18.**
  Handbook 901 is an APD funding handbook and does not belong in a security corpus.

### Issue #23 — PCI-DSS, FedRAMP, StateRAMP

- **PCI-DSS: resolved on both questions.** BOUND (T3, DOC 30.1.5 §III.A and OAM
  10.35.00.PR ¶.137). Copyright: summary-plus-link. The ingest is small, as #23 hoped.
- **FedRAMP: resolved, with a corrected framing.** Not a statewide binding; mandatory for
  FTI in cloud via IRS Pub 1075 § 3.3.1(a), which this corpus **already holds**. The
  cheapest correct action is a `graph` relationship from `irs-pub-1075-11-2021` to a
  FedRAMP `external_reference` stub — not a new full instrument.
- **StateRAMP: resolved.** NOT BOUND. Copyright flag confirmed; summary-plus-link.
  A `summary`-only stub is still worth holding so that "StateRAMP" and "GovRAMP" resolve to
  something, per ADR-0002's closing paragraph.

### Issue #24 — SSA TSSR

- **Resolved as to the binding:** BOUND, T3, on seven ODHS|OHA ISPO policies and
  ODHS|OHA 090-003 ¶17.
- **Not resolved as to the text.** ssa.gov returned HTTP 403 to all automated access on
  2026-09-11, and the document is distributed to exchange partners rather than published.
  This corpus cannot hold a versioned copy it cannot retrieve. **Recommendation: hold a
  `summary` stub citing <https://www.ssa.gov/dataexchange/security.html>, and record the
  access failure in `access-failures.json` alongside the existing entries.**

### Issue #25 — NIMS and CISA CPGs

- **NIMS: resolved.** BOUND, T1 — OAR 104-010-0005(3)(b) and ORS 401.038(1). This is the
  strongest finding in the note and the clearest ingest case of the eight.
- **CPGs: resolved as NOT BOUND.** Oregon uses them voluntarily. A corpus entry would assert
  an obligation the record does not support. **Recommendation: do not ingest; record the
  determination.**

### Still unresolved — and for each, whether to read more or to ask

| Open question | Next step | Who to ask, and what |
|---|---|---|
| Does ODHS have an FNS-imposed security obligation beyond 7 CFR 277.18? | **Ask.** No public document was found in three named places. | **ODHS**, Office of Information Services / ISPO: "Which FNS information-security document, if any, is named in Oregon's SNAP or WIC APD approvals or system agreements — and does FNS conduct the biennial 7 CFR 277.18(m)(3) security review of ODHS?" |
| Is there a signed ISA/ATC between OHA and CMS incorporating ARC-AMPE? | **Ask.** CMS's framework requires one; the instrument is non-public. | **OHA**, Information Security and Privacy Office: "Does OHA hold a current Interconnection Security Agreement / Authority to Connect with CMS, and does it incorporate ARC-AMPE Volume II?" |
| Which Oregon agencies hold SSA Information Exchange Agreements, and does the IEA name the TSSR by that name? | **Ask.** ssa.gov is closed to automated retrieval; the agreements are not published. | **ODHS/OHA ISPO** (and separately **DOC** and **OYA**, both of which reference SSA data): "Please identify the SSA agreement and the exact title and version of the SSA security requirements document it incorporates." |
| Does Oregon State Treasury Policy 02 18 14.PO impose PCI obligations by contract on agencies or processors? | **Read**, then ask if not public. Not held in `executive-regulatory-frameworks`; not retrieved. | **Oregon State Treasury**, if the policy is not published. |
| Has the 2025 draft of statewide policy 107-004-150 been adopted, and does the adopted version change the GovRAMP position? | **Read.** Check <https://www.oregon.gov/das/Policies/107-004-150.pdf> for a post-2019 effective date. | — |
| Has Oregon completed its SBE transition for PY2027, changing its ARC-AMPE category from SBE-FP to SBE? | **Read.** CMS updates <https://www.cms.gov/cciio/resources/fact-sheets-and-faqs/state-marketplaces>; Oregon was listed in both columns as of 2026-08-14. | — |

---

## Sources consulted, in full

**Local corpora** (checked out; primary as to what Oregon cites):

- `/home/dzinck/executive-regulatory-frameworks` — searched `agencies/`, `rules/`,
  `statutes/`, `executive-orders/`, `constitution/`, `external-references/` for all
  fourteen instrument names and their variants. Hit counts recorded in each section.
- `/home/dzinck/oregon-audits` — all 242 reports in `reports/`, report dates 2020-02-01
  through 2026-07-01. **Zero hits** for MARS-E, ARC-AMPE, TSSR, PCI, Payment Card, FedRAMP,
  StateRAMP, GovRAMP, Handbook 901, Cybersecurity Performance Goals, or IRS Publication
  1075. Two reports mention NIMS. *No Oregon agency has been audited against any of these
  eight instruments in the period this corpus covers* — which is a real finding about audit
  coverage, not evidence of compliance or of absence of obligation.

**This corpus:** `instruments/irs-pub-1075-11-2021.md`, `instruments/cjis-sp-6-1.md`,
`_meta/source-manifest.yml`, `_meta/ingest-queue.yml` (the queue is CFR-part-shaped and
contains none of these eight).

**Federal:** cms.gov, medicaid.gov, fns.usda.gov, govinfo.gov, uscode.house.gov, fema.gov,
cisa.gov, fedramp.gov, ssa.gov (403), ecfr.gov (redirect loop).

**Oregon:** secure.sos.state.or.us (OARD), oregon.gov/das, oregon.gov/eis, oregon.gov/oem,
oregon.gov/oha, oregon.gov/odhs, oregon.gov/doc, healthcare.oregon.gov.

**Standards bodies:** pcisecuritystandards.org, govramp.org.

**Not cited as evidence anywhere in this note:** any blog, vendor page, compliance-consultancy
article, or summary site. Where a search engine's summary of a primary page was the only
retrieval that succeeded, that is flagged in place (see §2, FNS).
