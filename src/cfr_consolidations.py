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
