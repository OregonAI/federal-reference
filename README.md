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

## Status: bootstrapped, **no documents yet**

The repository exists and CI is wired. The corpus is **empty**, and one toolkit release is
still required before it can hold anything — the `federal_instrument` doc_type does not
exist yet.

## What this is

Federal instruments Oregon agencies must comply with and cite as legal authority. Every
other corpus on this platform stops at the Oregon border; an OAR citing a federal
requirement resolved to nothing, so the authority chain ran statute → rule → policy and
then hit a wall exactly where the binding constraint lives.

**It is not primarily here to retire dead citations.** Measured before building anything:
Oregon rules make 916 federal authority claims, and the instruments most people would name
first account for 2 of them. The corpus is here so an agency can find the requirement it
must *comply with* — and obligations do not depend on a rule happening to cite them.

The clearest case, and the first document planned:

> **2 CFR 200**, the Uniform Guidance, governs every federal grant Oregon receives.
> **Zero** Oregon rules declare it as authority. It is cited **180 times** in Oregon's
> single audits — the reports that audit the state against federal requirements.

### Before you quote anything from here

This corpus is the one most likely to be mistaken for legal advice. Federal requirements
carry penalties Oregon policy does not.

It holds **current text**, with an `as_of` date and the upstream `amended_on`. An Oregon
rule written in 2019 implements the text that existed in 2019 — resolving its citation to
today's text is a wrong answer that looks like a right one. Both dates are served on every
document so that comparison can be made. See [AGENTS.md](AGENTS.md).

## License
Content (curated government material): CC0-1.0. Tooling, structure,
metadata: MIT. See [LICENSE](LICENSE).
