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
