"""Which part of a shared snapshot a document is responsible for reproducing.

Registered as `plugins.snapshot_slice_module` in _meta/corpus.yml. The toolkit calls
`slice(doc_id, snapshot_id, raw_text) -> str` and measures full-text coverage against what
comes back; the default implementation is the identity function.

WHY THIS CORPUS NEEDS IT. Sections cited out of a CFR part are cut from the part's one
snapshot and share it via `snapshot_id`, rather than each re-fetching and storing its own
copy — one source of truth on disk, so a section cannot drift from the part it came from.
But coverage is `len(document full text) / len(slice)`, so with the default identity slice
every section is measured against the WHOLE part and scores near 0%. All 29 of 2 CFR 200's
failed exactly that way before this existed.

#34: `SECTION_ID` used to be a literal pattern matching only `2-cfr-200.NNN`, true only of the
one part this corpus held when this file was written. That is not a dormant hardcode — it is
a live bug for every part ingested since: a second part's section document (`6-cfr-37.72`,
say) fails to match, falls through to `return raw_text` (the identity default), and coverage
is measured against the whole part again — the exact ~1% failure this file's own docstring
says it exists to prevent, silently reintroduced one id format over. Generalized to any
`{title}-cfr-{part}.{section}`.

The failure to notice is the inverse one: a slicer that returns something too SMALL makes
coverage look complete no matter what the document contains. So `_section` returns the span
between one `### ` heading and the next — the same boundary the splitter cut on — and raises
rather than falling back to the whole text when it cannot find the heading. A slice that
silently widens to the full part would turn this check back into the near-0% it was, and a
slice that silently narrows would turn it into a rubber stamp.
"""
from __future__ import annotations

import re

# `2-cfr-200.303` -> part `200`, section `303`; `6-cfr-37.72` -> part `37`, section `72`.
# The bare part id (no trailing `.NNN`) must NOT match -- it owns its whole snapshot.
DOC_ID = re.compile(r"^\d{1,2}-cfr-(\d{1,4})\.(\d+)$")


def _section(raw_text: str, sec: str) -> str:
    """The span of the part text belonging to § `sec`, heading included.

    `(?!\\d)` is load-bearing: without it `200.1` also matches the heading for `200.10`
    and `200.100`, and the slice would start at the wrong section while still looking
    like a plausible chunk of CFR text.
    """
    start = re.search(rf"^### §*\s*{re.escape(sec)}(?!\d)", raw_text, re.M)
    if start is None:
        raise LookupError(f"no `### ` heading for § {sec} in the snapshot")
    nxt = re.search(r"^### ", raw_text[start.end():], re.M)
    end = start.end() + nxt.start() if nxt else len(raw_text)
    return raw_text[start.start():end]


def slice(doc_id: str, snapshot_id: str, raw_text: str) -> str:  # noqa: A001
    m = DOC_ID.match(doc_id or "")
    if not m:
        # The part itself, and every non-CFR instrument, owns its whole snapshot.
        return raw_text
    part, sec = m.group(1), m.group(2)
    return _section(raw_text, f"{part}.{sec}")
