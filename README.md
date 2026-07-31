# Federal Reference — instruments Oregon must comply with

> ## ⚠️ NON-AUTHORITATIVE — AI-friendly reference only
> Curated copies/summaries, not official text. Always verify at the
> authoritative source linked in each document. See [DISCLAIMER.md](DISCLAIMER.md).

Part of the OregonAI civic corpus platform
([reference architecture](https://github.com/OregonAI/corpus-toolkit)).
Archetype: **document**. MCP interface: contract v1.

| Entry point | For |
|---|---|
| [llms.txt](llms.txt) | Machine-readable index — AI agents start here |
| [AGENTS.md](AGENTS.md) | Agent rules and anti-fabrication requirements |
| [STATUS.md](STATUS.md) | Generated health: freshness, coverage, drift |
| `_meta/corpus.yml` | Corpus configuration |

## Status: **43 documents** — 5 instruments and 38 CFR sections

| | |
|---|---|
| `2-cfr-200` | Uniform Guidance — 180 sections, 12 appendices |
| `2-cfr-200.NNN` | the **38 sections Oregon actually cites**, individually addressable |
| `cjis-sp-6-1` | CJIS Security Policy 6.1 — 473 pages |
| `pl-113-128` | Workforce Innovation and Opportunity Act — 298 pages |
| `irs-pub-1075-11-2021` | Tax Information Security Guidelines — 216 pages |
| `pl-115-224` | Perkins V — 61 pages |

**Both siblings now point here.** `executive-regulatory-frameworks` and `oregon-audits`
declare this corpus and resolve federal citations into it. Of the audits' 393 federal
citation occurrences, 181 (46%) land here; of ERF's 916 federal authority claims, 15 do —
small, and the 15 are rules whose stated legal basis previously resolved to nothing.

### Why the sections are split out

**85% of the Uniform Guidance citations Oregon makes are section-level** — 256 of 300, with
§ 200.303 alone accounting for 58. A corpus holding only the part would answer `2 CFR 200`
and miss every one of those. The split list is derived, not chosen:

```
python3 src/scan_cited_sections.py --erf ../oregon-policy-repo --audits ../oregon-audits
python3 src/split_cfr_sections.py
```

The result is committed to `_meta/cited-sections.yml` because CI cannot reach the sibling
repositories — a build-time scan would find nothing there and split nothing, silently.
`--check` on the splitter keeps that file and the 38 documents from drifting apart.

The scan counts the **short form** (`§200.414`) as well as the full one, but only in files
that also carry a full `2 CFR 200` citation to establish which part is meant. Requiring the
literal `2 CFR` on every hit hid 42 citations across 18 sections, nine of which had no
document — including § 200.414 at 10 citations.

Sections share the part's snapshot via `snapshot_id` rather than storing their own copies,
so a section cannot drift from the part it was cut from. `src/slicing.py` tells the
provenance checker which span of that snapshot each section is answerable for.

### Two sections in here no longer exist

§ 200.53 and § 200.62 were **removed on 2021-02-22**, when Subpart A's definitions were
consolidated into § 200.1. Oregon audits still cite them, because they were in force for
the fiscal years under audit. They are held at their **last-in-force text** (2021-02-21),
marked `status: superseded` with `superseded_by: 2-cfr-200.1`.

Resolving them to current text would answer with law that was not in force when it was
cited; dropping them would leave four real citations pointing at nothing.

### What a citation this corpus cannot answer gets back

An **explanation**, never a plausible substitute. `resolve_citation` refuses rather than
guessing, and `src/check_citations.py` enforces it in CI:

| Citation | Answer |
|---|---|
| `CJIS Security Policy 5.9.4` | **refused** — 6.1 is held; Oregon cites 5.6, 5.9.4, 6.0, none held |
| `IRS Pub 1075 (Rev. 09-2016)` | **refused** — revision 11-2021 is held; requirements differ |
| `CJIS Security Policy, Version 6.0` | **refused** — the refusal holds across spellings, not one canonical form |
| `2 CFR 200.53` | returned, labelled **not current law**, removed 2021-02-22 |
| `2 CFR 200.200` | returns the **part**, and says it did so instead of the section |
| `42 U.S.C. 1396` | **refused** — enacted public laws are held, not the codified Code |

The dangerous failure is not "did not resolve", which is visible. It is "resolved to
something plausible that is not what was cited" — an answer an agent would act on.

## What this is

Federal instruments Oregon agencies must comply with and cite as legal authority. Every
other corpus on this platform stops at the Oregon border; an OAR citing a federal
requirement resolved to nothing, so the authority chain ran statute → rule → policy and
then hit a wall exactly where the binding constraint lives.

**It is not primarily here to retire dead citations.** Measured before building anything:
Oregon rules make 916 federal authority claims, and the four instruments the seed named by
title account for **none** of them — the 2 belong to HIPAA, which this corpus does not hold. The corpus is here so an agency can find the requirement it
must *comply with* — and obligations do not depend on a rule happening to cite them.

The clearest case, and the flagship document:

> **2 CFR 200**, the Uniform Guidance, governs every federal grant Oregon receives.
> It is cited **180 times** in Oregon's single audits — the reports that audit the state
> against federal requirements — and declared as legal authority by **15** Oregon documents,
> 1.6% of the 916 federal authority claims Oregon rules make.

### Before you quote anything from here

This corpus is the one most likely to be mistaken for legal advice. Federal requirements
carry penalties Oregon policy does not.

It holds **current text**, with an `as_of` date and the upstream `amended_on`. An Oregon
rule written in 2019 implements the text that existed in 2019 — resolving its citation to
today's text is a wrong answer that looks like a right one. Both dates are served on every
document so that comparison can be made. See [AGENTS.md](AGENTS.md).

The two exceptions are deliberate and labelled: § 200.53 and § 200.62 are held at their
**last-in-force** text with `status: superseded`, because Oregon material cites them and
they no longer exist. Check `status` before treating anything here as current law.

## License
Content (curated government material): CC0-1.0. Tooling, structure,
metadata: MIT. See [LICENSE](LICENSE).
