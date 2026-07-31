#!/usr/bin/env python3
"""Citation schemes this corpus resolves, registered with the MCP framework.

Loaded via `plugins.citation_module` in _meta/corpus.yml. Importing this module IS the
contract — `register_scheme` calls happen at import time.

THIS FILE EXISTS AT STAGE 0 DELIBERATELY, EVEN THOUGH IT REGISTERS NOTHING.

`citation_module` is declared in corpus.yml, and a declared-but-missing module fails in a
way that validation cannot see: `corpus-validate-frontmatter` passes, and then
`CorpusFramework(...)` raises ModuleNotFoundError. The corpus looks healthy in CI and the
server will not start. Measured, not guessed — that is exactly what happened before this
file was added.

NOTHING IS REGISTERED YET, AND THAT IS ALSO DELIBERATE. A scheme that matches a citation
and then resolves nothing is worse than no scheme at all: the response reads as a genuine
"there is no such document" rather than as configuration that has not been finished. With
no scheme registered, an unresolvable citation is honestly unmatched.

The schemes below land with the documents they resolve, in Stage 3. Sketched here so the
shape is on the record, not because the sketch is authoritative:

    cfr-part     `2 CFR 200`, `29 CFR 1910.147`
                 Section-level resolution matters more here than in any other corpus: an
                 OAR cites a CONTROL, not a publication. Whether a section is its own
                 document or an anchor inside a part is decided per instrument, by whether
                 anything actually cites it that precisely.

    usc-section  `42 U.S.C. 1396`, `42 USC 1396`
                 Spacing and punctuation vary constantly in the wild.

    public-law   `Pub. L. 113-128`, with the U.S.C. sections it created as aliases —
                 agencies cite both forms interchangeably for the same instrument.

    irs-pub      `IRS Pub 1075 (Rev. 11-2021)`. THE REVISION IS PART OF THE IDENTITY, not
                 metadata: requirements change between revisions, so resolving a 2019
                 citation to the 2021 text is a wrong answer that looks right.

    cjis-policy  `CJIS SP 5.9 §5.6` — version plus section, same reasoning.

None of these carries `corpus=`: this corpus is the CEILING of the authority chain. The
resolution that matters runs INTO it, from executive-regulatory-frameworks and
oregon-audits declaring it as their sibling. It does not resolve back down.
"""
from corpus_toolkit.mcp.framework import register_scheme  # noqa: F401  (Stage 3 uses it)
