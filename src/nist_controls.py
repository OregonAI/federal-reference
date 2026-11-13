"""Shared definitions for the NIST SP 800-53 control intake (#42).

One module so the scanner (what is cited), the anchorer (where controls start), the slicer
(what a control document reproduces), the splitter (what is written) and the resolver (what
a citation means) all use the SAME grammar for a control id. Pure: no network, and nothing
is read from disk except by the functions that say so.
"""
from __future__ import annotations

import re
from collections import Counter

from federal_ids import NIST_FAMILIES

PUBLICATION_ID = "nist-sp-800-53-r5"

# `AC-2`, `AC-2(1)`. The lookbehind is the CSF guard: NIST CSF 1.1 subcategories are
# `PR.AC-3`, `PR.IP-3`, and a bare `\bAC-3` matches inside them. Measured on 2026-11-12: the
# issue's own scan counted them as 800-53 controls (6 CFR 37 and the CISA CPGs both carry CSF
# subcategories), which is one reason this scan's list is not the issue's 228.
CONTROL_TOKEN = re.compile(
    r"(?<![A-Za-z0-9.])(?P<fam>[A-Z]{2})-(?P<num>\d{1,2})(?P<enh>(?:\(\d{1,2}\))*)(?![0-9A-Za-z])")


def control_id(fam: str, num: str | int) -> str:
    return f"{fam.lower()}-{int(num)}"


def scan_text(text: str) -> tuple[Counter, Counter]:
    """(base-control counts, enhancement counts) for every control token in `text`.

    `ac-2` counts `AC-2` and also each `AC-2(n)` (an enhancement is cited inside its base
    control's document); `ac-2(1)` counts only the enhancement form. The caller decides WHICH
    documents to scan -- this does not know about 800-53 context.
    """
    base: Counter = Counter()
    enh: Counter = Counter()
    for m in CONTROL_TOKEN.finditer(text):
        if m.group("fam") not in NIST_FAMILIES or int(m.group("num")) == 0:
            continue
        cid = control_id(m.group("fam"), m.group("num"))
        base[cid] += 1
        if m.group("enh"):
            enh[f"{cid}{m.group('enh')}"] += 1
    return base, enh


_CATALOG_HEADING = re.compile(r"^### (?P<fam>[A-Z]{2})-(?P<num>\d{1,2})\s", re.M)


def catalog_ids(anchored_text: str) -> set[str]:
    """The control ids the publication's catalog contains: every anchored control heading.

    Read from the ANCHORED snapshot (src/anchor_sections.py), so "what the catalog has" and
    "where a control document is cut from" are the same list and cannot disagree.
    """
    return {control_id(m.group("fam"), m.group("num"))
            for m in _CATALOG_HEADING.finditer(anchored_text)
            if m.group("fam") in NIST_FAMILIES}


# The brief's own test for "this document is citing 800-53": it names the publication at all.
MENTIONS_800_53 = re.compile(r"800[-‑ ]?53", re.I)


def natural_key(cid: str):
    fam, num = cid.split("-", 1)
    return fam, int(num)


# The catalog is Chapter Three. It opens at the first control and closes at the standalone line
# `REFERENCES` (the table of contents' own `REFERENCES ........ 374` carries dot-leaders and is
# not that line). Shared by the anchorer, the extractor and the extraction check so all three
# draw the same boundary.
CATALOG_START = re.compile(r"^AC-1\s+POLICY AND PROCEDURES$")


_BANNER = re.compile(r"^This publication is available free of charge from:")
_REFERENCES_PAGE_HEADER = re.compile(r"^REFERENCES\s+PAGE \d+$")


def is_catalog_end(line: str) -> bool:
    return line.strip() == "REFERENCES"


def held_scope(text: str) -> str:
    """The part of the extracted publication this corpus reproduces: everything from the cover
    through the last control of the catalog, and nothing after it.

    WHY NOT THE WHOLE PUBLICATION (ADR-0002, AGENTS.md hard rule 3). Everything after the
    catalog -- the bibliography, Appendix A (glossary), B (acronyms) and C (control summaries)
    -- is not cited by any held document, and Appendix A adapts third-party definitions
    (`[ISO/IEC 15026, Adapted]`, `[ISO 25237]`, `[ISO/IEC 29100, Adapted]`, `[ISO 15288]`,
    `[IETF 4949]`), whose reproducibility nobody has determined. The determination is a human
    step; until it is made the text is left out, not guessed at. The raw PDF snapshot still
    holds all of it (it is the source of record), and check_extraction.py proves the committed
    text is exactly the raw PDF's token stream up to this boundary.

    RAISES rather than falling back to the whole text: a missing boundary means the PDF is not
    the publication this was written for, and widening silently would publish the glossary.
    """
    lines = text.split("\n")
    start = next((i for i, l in enumerate(lines) if CATALOG_START.match(l.strip())), None)
    if start is None:
        raise ValueError("no catalog opening (`AC-1 POLICY AND PROCEDURES`) in the extracted "
                         "text -- not SP 800-53 Rev. 5, or the extraction is broken")
    end = next((i for i in range(start + 1, len(lines)) if is_catalog_end(lines[i])), None)
    if end is None:
        raise ValueError("the catalog never closes (no standalone `REFERENCES` line after "
                         "`AC-1`) -- refusing to hold the whole publication")
    # The page that opens the bibliography prints its running header and the document banner
    # ABOVE the `REFERENCES` heading (`REFERENCES   PAGE 374` / `This publication is available
    # free of charge ...`); they belong to the page that is not held, so they go with it.
    while end - 1 > start and (_BANNER.match(lines[end - 1].strip())
                               or _REFERENCES_PAGE_HEADER.match(lines[end - 1].strip())):
        end -= 1
    return "\n".join(lines[:end]).rstrip("\n")
