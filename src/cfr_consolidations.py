#!/usr/bin/env python3
"""Shared record of CFR section consolidations -- one dict, not two.

src/citation_schemes.py (the citation resolver's refusal notes) and src/split_cfr_sections.py
(the removed-section document's own body text) both need the same fact about a removed
section: WHERE its content went, if anywhere. A snapshot diff cannot supply that -- it is
knowledge about the amendment itself, not something present in either snapshot's text -- so
it is hand-recorded per part, here, ONCE.

#33 is the reason this is one file rather than two literals: the OMB issuing_body hardcode
lived separately in ingest_instruments.py AND split_cfr_sections.py, fixed in one and left to
reproduce the same bug one layer down in the other. Two places asserting the same fact about
a specific part drift the moment only one of them is edited. Importing this module from both
callers makes that drift structurally impossible instead of trusting two edits to stay in
sync.

Keyed by `{title}-cfr-{part}`. `scope` is REQUIRED for either caller's message to name WHAT
was consolidated ("...which consolidated {scope} into...") -- see #35's fix in
citation_schemes.py, which fabricated "Subpart A's definitions" for a synthetic second part
that had an `into` but no `scope`. A part with no entry here, or an entry with no `scope`,
gets a true, less specific statement from each caller instead of a guessed one.
"""
from __future__ import annotations

CONSOLIDATIONS: dict[str, dict] = {
    "2-cfr-200": {"date": "2021-02-22", "into": "200.1", "scope": "Subpart A's definitions"},
}

# A WHOLE PART removed from the CFR, which is not a section consolidation and cannot be
# recorded as one: there is no `into` SECTION, because there is no surviving part to hold it.
# 45 CFR 75 was removed in its entirety on 2025-10-01; eCFR 404s for it, so this corpus pins
# the part at its last-in-force date and holds the cited sections as superseded documents.
#
# WHAT IS AND IS NOT RECORDED HERE. The date, the fact of the removal, and the successor part
# are NOT here -- they are `amended_on`, `status: superseded` and `superseded_by` in the part
# document's own frontmatter, which src/split_cfr_sections.py reads (part_facts()). Recording
# them a second time is the drift this module's own docstring argues against. What is here is
# the one thing no snapshot and no frontmatter field states: WHY the agency did it. `why` is a
# clause, spliced after "...removed from the CFR in its entirety that same date". A part with
# no entry here still gets a true, less specific sentence -- the same fallback ladder
# `scope` has above.
PART_REMOVALS: dict[str, dict] = {
    "45-cfr-75": {
        "why": "when HHS retired its own Uniform Guidance for [2 CFR 200](./2-cfr-200.md) "
               "government-wide (HHS-specific modifications relocated to 2 CFR 300, not yet "
               "held here)",
    },
}
