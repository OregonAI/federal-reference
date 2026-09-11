#!/usr/bin/env python3
"""Citation schemes this corpus resolves, registered with the MCP framework.

Loaded via `plugins.citation_module` in _meta/corpus.yml. Importing this module IS the
contract — `register_scheme` calls happen at import time.

THE RULE THIS FILE IS BUILT AROUND: a citation this corpus cannot answer must come back as
an EXPLANATION, never as a plausible-looking substitute. Every resolver below can return
`(candidates, note)`, and the framework surfaces `note` whether or not anything resolved.
That is what makes "we hold 6.1, you asked for 5.9.4" expressible at all — the alternative
is handing back 6.1, which is a wrong answer wearing a right answer's clothes.

WHAT IS HELD IS READ FROM THE DOCUMENTS, NOT HARD-CODED. Versions especially: a literal
"6.1" in this file keeps claiming 6.1 after CJIS 6.2 is ingested, and the version gap is the
single thing these schemes exist to police. Held ids and versions come from the frontmatter
at import, so the schemes cannot disagree with the corpus.

NO SCHEME CARRIES `corpus=`. This corpus is the CEILING of the authority chain. The
resolution that matters runs INTO it — executive-regulatory-frameworks and oregon-audits
declaring it as their sibling (Stage 4). It does not resolve back down.
"""
from __future__ import annotations

import functools
import pathlib
import re

import yaml

from corpus_toolkit.mcp.framework import register_scheme

import sys as _sys
_sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
# MAX_RANGE (the "too wide to be a real range" cutoff) lives in federal_ids.py — the
# parity-locked cross-corpus contract file — and is IMPORTED, not copied, so both sides
# apply the same cutoff. RANGE and LIST_SEC are NOT imported from there, and NOT because
# federal_ids.py "only ever needs to expand 2 CFR 200 today" -- that claim is false, and
# measurably so: `candidates("17 CFR 230.504, 230.506")` drops the held 17-cfr-230.506
# right now, in this corpus, same for "2 CFR 180.300 and 180.305" and "7 CFR 273.7 through
# 273.9". Purity is not the obstacle either -- `candidates()` already parses the part it
# needs from the citation string (`hits[0].group('part')`), and returning an id from a pure
# function is explicitly not a claim the document exists (see federal_ids.py's own
# docstring).
#
# The real reason: federal_ids.py is copied BYTE-IDENTICAL into every sibling corpus (see
# its docstring), so generalizing RANGE/LIST_SEC there has to land the same way in every
# copy at once -- a coordinated cross-repo change, not a one-file fix, and out of scope for
# #55 (see that issue's own "What would fix it"). This resolver knows exactly which parts
# THIS corpus holds, so for its own in-corpus resolution it builds the equivalent patterns
# per PART below instead of waiting on that coordination (federal-reference#55).
#
# THE GAP THIS LEAVES: federal_ids.candidates() -- the path every SIBLING corpus walks for
# exact-id lookup -- still only expands 2 CFR 200's multi-section citations. A sibling
# resolving "17 CFR 230.504, 230.506" against this corpus's published index still gets only
# the first id, silently dropping a document this corpus holds, for every held part except
# 200. That is #35's failure mode (federal-reference#12) recurring cross-corpus, and it is
# what check_citations.py's "known gap (#55, cross-corpus)" check below pins down so it
# cannot slide from filed to silent. #55 stays open for the coordinated federal_ids.py fix.
# USC joins the import for ADR-0006: the suffix-aware section regex (`1320d-2`, never
# truncated to `1320d`) is a CONTRACT the sibling side already relies on via
# federal_ids.candidates(), and this corpus's own resolver must parse the identical thing
# or the two can disagree about which section a citation names -- the exact substitution
# ADR-0004/-0006 exist to refuse. RANGE and LIST_SEC are still NOT imported, for the
# reason above: this resolver builds them per PART.
from federal_ids import MAX_RANGE, USC  # noqa: E402

INSTRUMENTS = pathlib.Path(__file__).resolve().parent.parent / "instruments"


def _held() -> dict[str, dict]:
    """{document id: frontmatter} for everything this corpus holds.

    Read once at import. If it comes back empty every scheme would match and then resolve
    nothing, which reads to a caller as a genuine "there is no such document" — so an empty
    result is treated as a failure rather than as an empty corpus.
    """
    out: dict[str, dict] = {}
    for path in sorted(INSTRUMENTS.glob("*.md")):
        head = path.read_text(encoding="utf-8").split("---", 2)
        if len(head) < 3:
            continue
        fm = yaml.safe_load(head[1]) or {}
        if fm.get("id"):
            out[str(fm["id"])] = fm
    if not out:
        raise RuntimeError(
            f"citation schemes: no documents found under {INSTRUMENTS} — every scheme would "
            f"match and then resolve nothing, which reads as 'no such document'")
    return out


HELD = _held()


def _section_numbers(text: str, part: str) -> frozenset[str]:
    """Section numbers appearing as `### § {part}.NNN` headings in an extracted part text."""
    return frozenset(re.findall(rf"^### §*\s*{re.escape(part)}\.(\d+)\b", text, re.M))


# Which sections a part ACTUALLY contains, current and as of its last snapshot before a known
# amendment. Without these, a citation to a section that does not exist gets told to go find a
# heading that is not there — a confidently false instruction, and the kind of plausible-
# sounding wrong answer this corpus is built to refuse.
#
# COMPUTED PER PART, ON DEMAND, FROM WHAT IS HELD — not a module-level pair of constants for
# "the" part. #35: the whole file used to assume there was only ever one part; these two used
# to be computed once at import for the single hard-coded 2-cfr-200 literal, so a second
# ingested part had no section data at all and fell through to "not held" before it even
# reached this logic. Cached because
# each is a disk read and a citation to the same part is resolved many times in one run.
_SNAPSHOTS = INSTRUMENTS.parent / "_meta" / "snapshots"


_SNAPSHOT_DATE_RE = re.compile(r"-(\d{4}-\d{2}-\d{2})\.txt$")


@functools.lru_cache(maxsize=None)
def _current_section_numbers(base: str) -> frozenset[str]:
    """`base` is `{title}-cfr-{part}`; `part` is derived from it rather than taken as a
    second parameter, so a mismatched pair (`_current_section_numbers("2-cfr-200")` called
    with a `part` that disagrees with `base`) cannot exist as a class of bug.

    A missing document here is NOT an empty part — every `base` this is called with came
    from `_held_cfr_parts()`, i.e. HELD already says this id IS a held cfr_part, loaded by
    globbing `instruments/*.md` and keying on each document's own frontmatter `id` (see
    `_held()`). If `instruments/{base}.md` does not exist, the index and the instruments
    directory disagree — an id whose document was named differently on disk, say — and
    that is exactly the confident-false-refusal class #35 exists to close, one field over:
    swallowing it here would make `_cfr_one` tell a caller "there is no § X.Y" about a part
    it is simultaneously serving. Raise loudly instead; `_held()` already treats an empty
    HELD the same way, for the same reason (see its docstring)."""
    path = INSTRUMENTS / f"{base}.md"
    if not path.is_file():
        raise RuntimeError(
            f"citation schemes: {base!r} is held as a cfr_part in HELD but {path} does not "
            f"exist. The index and the instruments directory disagree about this part's "
            f"document — resolving section citations against it would silently produce "
            f"'there is no such section', a confident answer with nothing behind it.")
    part = base.split("-cfr-", 1)[1]
    return _section_numbers(path.read_text(encoding="utf-8"), part)


@functools.lru_cache(maxsize=None)
def _former_section_numbers(base: str) -> frozenset[str]:
    """Section numbers seen in any DATED snapshot of this part (e.g. `2-cfr-200-2021-02-21.txt`)
    that are not in the current text. Most parts have no such snapshot and correctly come back
    empty — that is an absence of history, not a gap in this function.

    The glob is `{base}-*.txt`, which would also match a same-prefix file that is not a
    dated snapshot at all (`2-cfr-200-draft.txt`); filtered through `_SNAPSHOT_DATE_RE` so
    the code actually enforces the "DATED" this docstring promises, rather than relying on
    nothing else ever being dropped in `_meta/snapshots/` with a matching prefix."""
    part = base.split("-cfr-", 1)[1]
    out: set[str] = set()
    for snap in sorted(_SNAPSHOTS.glob(f"{base}-*.txt")):
        if not _SNAPSHOT_DATE_RE.search(snap.name):
            continue
        out |= _section_numbers(snap.read_text(encoding="utf-8"), part)
    return frozenset(out) - _current_section_numbers(base)


def _snapshot_dates(base: str) -> list[str]:
    """Dates of every snapshot actually consulted for `base` by `_former_section_numbers`,
    for a refusal message to name — so "there is no such section" can say WHICH texts were
    checked instead of just asserting it."""
    dates = []
    for snap in sorted(_SNAPSHOTS.glob(f"{base}-*.txt")):
        m = _SNAPSHOT_DATE_RE.search(snap.name)
        if m:
            dates.append(m.group(1))
    return dates


# The facts about a removed-and-consolidated section that a snapshot diff cannot supply:
# WHERE its content went, and WHAT moved there. Both are knowledge about the amendment
# itself, not something present in the text, so both are hand-recorded per held part rather
# than derived. #34: this used to be a dict literal defined here alone; src/split_cfr_sections.py
# needs the identical fact (its removed-section document says the same thing in prose) and
# had its OWN separate hardcode of it, which is exactly the shape of bug #33 was -- one place
# fixed, an identical literal one file over left to reproduce it. Now imported from
# src/cfr_consolidations.py, the one place either caller can drift from is itself.
from cfr_consolidations import CONSOLIDATIONS as _CONSOLIDATIONS  # noqa: E402


def _version_of(doc_id: str) -> str | None:
    v = (HELD.get(doc_id) or {}).get("version")
    return str(v) if v else None


def _norm_rev(s: str) -> str:
    return "".join((s or "").split()).replace("/", "-")


# A version-ish token ANYWHERE in the citation string. Deliberately generous, and used only
# to decide whether the caller NAMED a version -- never to pick a document.
#
# The bug this exists to kill: the version group inside CJIS_RE/IRSPUB_RE was optional and
# the patterns were case-sensitive, so `CJIS Security Policy, Version 6.0` captured nothing,
# fell through to the "no version named" branch, and returned 6.1 -- while asserting "the
# citation named no version" about a string that named 6.0, a version listed in that very
# document's `known_cited_versions_not_held`. An uncaptured version must REFUSE, never
# default to "unversioned".
CJIS_VER_TOKEN = re.compile(r"\b\d+\.\d+(?:\.\d+)?\b")
IRS_REV_TOKEN = re.compile(r"\b(\d{1,2})\s*[-/]\s*(\d{4})\b")


def _declared(pattern, text: str):
    """The first version-ish token in `text`, or None."""
    m = pattern.search(text or "")
    return m.group(0) if m else None


# --------------------------------------------------------------------------- CFR
# `2 CFR 200`, `2 C.F.R. § 200.303`, `2 CFR Part 200.303`, `2 CFR §§ 200.303`.
#
# ONE scheme covers part and section. Splitting them makes resolution depend on registration
# order, and the section form is the common one -- 188 of the 232 citations Oregon makes.
CFR_RE = (r"(?i)(?P<title>\d{1,2})\s*C\.?\s?F\.?\s?R\.?\s*(?:Part\s+)?§{0,2}\s*"
          r"(?P<part>\d{1,4})(?:\.(?P<sec>\d{1,4}))?\b")


def _range_re(part: str) -> re.Pattern:
    """`{part}.331-{part}.333`, `{part}.510 through {part}.512`, en/em dashes included.

    Built PER PART rather than reused from federal_ids.RANGE, which matches only a literal
    `200.` — this corpus knows which part it is resolving, so it is not limited to the one
    part federal_ids.py can hard-code (federal-reference#55).

    `(?<![\\d.])` guards BOTH occurrences of `{p}\\.`. Without it, "45 CFR 98.1, see also 12
    CFR 398.20-25" resolves part 98's pattern against the "98.20-25" tail of "3**98**.20-25"
    -- a different title's section handed back as if this corpus's 45 CFR 98 held it. Anchoring
    on a digit/dot immediately before the part number closes that; it does NOT need to also
    restrict the search window to text after the anchor match, because the range's OWN low
    bound is the anchor's own `{part}.{sec}` text and must still be found there."""
    p = re.escape(part)
    return re.compile(
        rf"(?<![\d.]){p}\.(\d{{1,4}})\s*(?:-|–|—|to|through|thru)\s*"
        rf"(?:(?<![\d.]){p}\.)?(\d{{1,4}})\b", re.I)


def _list_sec_re(part: str) -> re.Pattern:
    """A section continuing a list: the `, {part}.303` in "2 CFR 200.302, 200.303". Requires
    a list separator immediately before it, exactly like federal_ids.LIST_SEC, but keyed off
    the actual part being resolved rather than a literal `200.` (federal-reference#55).

    Same `(?<![\\d.])` guard as `_range_re`, and for the same reason: without it a list
    continuation for part 98 can match inside another title's "398.20", not just the range
    form."""
    p = re.escape(part)
    return re.compile(rf"(?:,|;|\band\b|&)\s*§{{0,2}}\s*(?<![\d.]){p}\.(\d{{1,4}})\b", re.I)


def _cfr(m, nodes=None):
    """Resolve the anchor section, then every list/range continuation in the SAME
    citation — "2 CFR 200.302, 200.303" and "200.331 through 200.333" are one citation
    naming several sections, and answering only the first silently dropped documents
    this corpus holds (federal-reference#12; the sibling-side federal_ids.candidates()
    fixed this long ago, so the two sides disagreed about the same string).

    Works for ANY held CFR part, not just 2 CFR 200 (federal-reference#55) — the range/list
    patterns are built per-part above rather than reused from federal_ids.py's 200-only
    ones. Gated on `_held_cfr_parts()` rather than run unconditionally: an unheld part
    already gets one true refusal from `_cfr_one` below, and expanding further would only
    re-derive the same "not held" note once per extra section named, never a section this
    corpus does not have — `_cfr_one` still owns that check per section either way."""
    title, part, sec = m.group("title"), m.group("part"), m.group("sec")
    cands, note = _cfr_one(title, part, sec)
    if sec is None or f"{title}-cfr-{part}" not in _held_cfr_parts():
        return cands, note
    secs, notes = [sec], ([note] if note else [])
    text = m.string
    rm = _range_re(part).search(text)
    if rm:
        lo, hi = int(rm.group(1)), int(rm.group(2))
        if lo < hi and hi - lo <= MAX_RANGE:
            secs.extend(str(n) for n in range(lo, hi + 1) if str(n) not in secs)
    for extra in _list_sec_re(part).findall(text):
        if extra not in secs:
            secs.append(extra)
    for s in secs[1:]:
        c2, n2 = _cfr_one(title, part, s)
        cands.extend(i for i in c2 if i not in cands)
        if n2:
            # `s` is always drawn from secs[1:], so len(secs) > 1 holds for every iteration
            # here by construction — the "just n2, no prefix" arm was dead code chasing a
            # condition this loop can never make false.
            notes.append(f"§ {part}.{s}: {n2}")
    return cands, ("; ".join(notes) or None)


def _held_of_kind(kind: str) -> dict[str, dict]:
    """{doc_id: frontmatter} for every held document of one `instrument_kind`.

    Filtered straight out of HELD — itself read from the documents at import, not a literal
    (see `_held()`) — so a newly ingested document of that kind becomes resolvable, and an
    unheld one is correctly refused BY NAME, without editing this file. #35: `_held_cfr_parts`
    used to compare against a literal ("2", "200"), so a part sitting right there in HELD,
    loaded from its own document's frontmatter, was reported "not held" anyway. Shared by
    every kind-scoped refusal below rather than one dict comprehension per kind, so the next
    kind to need a real filter (excluding a superseded document, say) changes this once.
    """
    return {doc_id: fm for doc_id, fm in HELD.items() if fm.get("instrument_kind") == kind}


def _held_cfr_parts() -> dict[str, dict]:
    """{'title-cfr-part': frontmatter} for every cfr_part document actually held.

    See `_held_of_kind()` — this is that filter, scoped to `cfr_part`.
    """
    return _held_of_kind("cfr_part")


def _cfr_one(title, part, sec):
    base = f"{title}-cfr-{part}"
    part_fm = HELD.get(base)

    if part_fm is None or part_fm.get("instrument_kind") != "cfr_part":
        held = _held_cfr_parts()
        listing = ", ".join(sorted(fm.get("citation", k) for k, fm in held.items()))
        return [], (
            f"this corpus does not hold {title} CFR {part}. It holds "
            f"{listing or 'no CFR parts'}. The citation is well-formed — it is simply "
            f"outside what has been ingested.")

    if sec is None:
        return [base], None

    doc = f"{base}.{sec}"
    fm = HELD.get(doc)

    if fm is None:
        if sec in _current_section_numbers(base):
            # The section IS inside the part we hold; it just was not split out, because only
            # the sections Oregon cites are. Returning the part is a TRUE answer, but it is a
            # different document from the one asked for, so it is labelled rather than
            # silently substituted.
            return [base], (
                f"§ {part}.{sec} is not held as its own document — only the sections Oregon "
                f"cites are split out. Returning {title} CFR {part}, the part that contains "
                f"it; look for the `### § {part}.{sec}` heading in its full text.")

        # Not in the current part at all. Telling the caller to go find a heading that is not
        # there would be a confidently false instruction, so say what is actually true — and
        # if a dated snapshot shows it existed before a known amendment, say what that
        # amendment did, because for this corpus's audit citations that is usually the real
        # explanation.
        if sec in _former_section_numbers(base):
            consolidation = _CONSOLIDATIONS.get(base)
            if consolidation and consolidation.get("scope"):
                target = consolidation["into"]
                return [], (
                    f"§ {part}.{sec} is NOT in the current {title} CFR {part}. It existed "
                    f"until the {consolidation['date']} amendment, which consolidated "
                    f"{consolidation['scope']} into § {target}. It is not held individually "
                    f"— only the removed sections Oregon material actually cites are, as "
                    f"their own superseded documents. For the current treatment see "
                    f"{base}.{target.split('.', 1)[-1]}.")
            # No recorded consolidation scope for this part: still true and specific about
            # what changed, without inventing where or what the content went.
            return [], (
                f"§ {part}.{sec} is NOT in the current {title} CFR {part}. It appears in an "
                f"earlier snapshot of this part but not the current text, and is not held "
                f"individually. Check whether a superseded document for it exists, or "
                f"whether the citing rule predates {part_fm.get('as_of')}.")
        dates = _snapshot_dates(base)
        also = ""
        if dates:
            texts = "text" if len(dates) == 1 else "texts"
            joined = dates[0] if len(dates) == 1 else f"{', '.join(dates[:-1])} or {dates[-1]}"
            also = f", and none in the {joined} {texts} either"
        return [], (
            f"there is no § {part}.{sec} in {title} CFR {part} as of "
            f"{part_fm.get('as_of')}{also}. Check the citation — it may name a different "
            f"title or part.")

    if fm.get("status") == "superseded":
        return [doc], (
            f"§ {part}.{sec} was REMOVED from the CFR on {fm.get('amended_on')}. What is "
            f"returned is its LAST-IN-FORCE text (as of {fm.get('as_of')}), held because "
            f"Oregon material still cites it. It is NOT current law — the current treatment "
            f"is in {fm.get('superseded_by')}, and the two may differ.")

    return [doc], None


register_scheme("cfr", CFR_RE, resolver=_cfr)


# --------------------------------------------------------------------------- Public law
# `Pub. L. 113-128`, `Public Law No. 115-224`, `PL 113-128`.
PUBLAW_RE = (r"(?i)P(?:ub(?:lic)?)?\.?\s*L(?:aw)?\.?\s*(?:No\.?\s*)?"
             r"(?P<cong>\d{2,3})\s*[-–]\s*(?P<num>\d{1,4})\b")

# Derived from what is held, so adding a public law makes it resolvable without editing this
# file -- and so this map can never claim one the corpus does not have.
_PUBLAW = {tuple(i.split("-")[1:3]): i for i in HELD if i.startswith("pl-")}


def _publaw(m, nodes=None):
    key = (m.group("cong"), m.group("num"))
    hit = _PUBLAW.get(key)
    if hit:
        return [hit], None
    return [], (
        f"Pub. L. {key[0]}-{key[1]} is not held. This corpus holds "
        f"{', '.join(sorted(_PUBLAW.values())) or 'no public laws'} — intake is scoped to "
        f"instruments Oregon is audited against or must comply with, not the statute book.")


register_scheme("public-law", PUBLAW_RE, resolver=_publaw)


# --------------------------------------------------------------------------- IRS publication
# `IRS Pub 1075`, `IRS Publication 1075 (Rev. 11-2021)`.
IRSPUB_RE = r"(?i)IRS\s+Pub(?:lication)?\.?\s*(?P<num>\d{3,4})"


def _irspub(m, nodes=None):
    num = m.group("num")
    # Read the revision off the WHOLE citation, not just what IRSPUB_RE captured.
    tok = IRS_REV_TOKEN.search(m.string or "")
    rev = f"{tok.group(1).zfill(2)}-{tok.group(2)}" if tok else ""
    doc = f"irs-pub-{num}"
    if doc not in HELD:
        # Try the revision-qualified id, which is how these are named once a revision is
        # part of the identity (irs-pub-1075-11-2021).
        doc = next((i for i in HELD if i.startswith(f"irs-pub-{num}-")), None)
        if doc is None:
            held_pubs = ", ".join(sorted(i for i in HELD if i.startswith("irs-pub-")))
            return [], (f"IRS Publication {num} is not held; this corpus holds "
                        f"{held_pubs or 'no IRS publications'}.")

    held = _version_of(doc)
    if rev and held and _norm_rev(rev) != _norm_rev(held):
        # THE REVISION IS PART OF THE IDENTITY. Requirements change between revisions, so
        # handing back 11-2021 for a citation to an earlier one is exactly the substitution
        # this corpus exists to refuse.
        return [], (
            f"IRS Publication {num} revision {rev} is NOT held — this corpus holds revision "
            f"{held} only. Requirements change between revisions, so {held} must not be "
            f"treated as an answer to a {rev} citation.")

    note = None
    if not rev and held:
        note = f"the citation named no revision; what is returned is revision {held}."
    return [doc], note


register_scheme("irs-pub", IRSPUB_RE, resolver=_irspub)


# --------------------------------------------------------------------------- CJIS
# `CJIS Security Policy 5.9.4`, `CJIS SP v6.1`, `CJIS Security Policy`.
CJIS_RE = r"(?i)CJIS(?:\s+Security)?(?:\s+Policy|\s+SP)?"

_CJIS = next((i for i in sorted(HELD) if i.startswith("cjis-")), None)


def _cjis(m, nodes=None):
    if _CJIS is None:
        return [], "no CJIS Security Policy is held by this corpus."
    # Read the version off the WHOLE citation, not just what CJIS_RE captured.
    ver, held = _declared(CJIS_VER_TOKEN, m.string), _version_of(_CJIS)

    if ver and held and ver != held:
        # The version gap this corpus RECORDED at ingest rather than resolved: Oregon cites
        # 5.6, 5.9.4 and 6.0; only 6.1 is held. Answering any of those with 6.1 is the
        # failure this whole file is shaped to prevent, so it is refused explicitly.
        gap = HELD[_CJIS].get("known_cited_versions_not_held") or []
        extra = (f" Oregon material is known to cite {', '.join(map(str, gap))}, none of "
                 f"which is held." if gap else "")
        return [], (
            f"CJIS Security Policy version {ver} is NOT held — this corpus holds {held} "
            f"only. Controls are added, renumbered and tightened between versions, so {held} "
            f"is not an answer to a {ver} citation.{extra}")

    note = None
    if not ver and held:
        note = f"the citation named no version; what is returned is version {held}."
    return [_CJIS], note


register_scheme("cjis-policy", CJIS_RE, resolver=_cjis)


# --------------------------------------------------------------------------- Act names
#
# Bare act names are how Oregon actually cites the big statutes — measured 2026-08-03:
# ~100 `WIOA` mentions, 23 `Perkins V`, ZERO section-shaped forms in either citing
# corpus, and until this scheme existed the bare names resolved to NOTHING ("no
# citation scheme recognized this format"). The resolution is the whole document plus
# a note that teaches the caller the navigation the anchors now support; `Title N`
# qualifiers (11 real occurrences for WIOA) narrow the note to that title's section
# range, derived from the document's own ### anchors — never hand-maintained.

_ACTS = {
    "pl-113-128": r"WIOA|Workforce\s+Innovation\s+and\s+Opportunity\s+Act",
    "pl-115-224": (r"Perkins\s+V|Carl\s+D\.?\s+Perkins\s+Career\s+and\s+Technical\s+"
                   r"Education\s+Act"),
}
_ROMAN = {1: "I", 2: "II", 3: "III", 4: "IV", 5: "V", 6: "VI", 7: "VII"}


def _act_sections(doc_id: str) -> list[int]:
    path = INSTRUMENTS / f"{doc_id}.md"
    if not path.is_file():
        return []
    return [int(m.group(1)) for m in
            re.finditer(r"^### SEC\. (\d+)\.", path.read_text(encoding="utf-8"), re.M)]


def _act(m, nodes=None):
    for doc_id, pat in _ACTS.items():
        if re.fullmatch(pat, m.group("act"), re.I):
            break
    else:
        return []
    secs = _act_sections(doc_id)
    title_num = m.group("title")
    if title_num:
        n = {v: k for k, v in _ROMAN.items()}.get(title_num.upper())
        in_title = sorted(s for s in secs if n and s // 100 == n)
        if in_title:
            note = (f"Title {title_num.upper()} spans SEC. {in_title[0]}–"
                    f"{in_title[-1]} ({len(in_title)} sections). The document is "
                    f"large — pass part='SEC. {in_title[0]}.' (or any section "
                    f"heading) to get_document rather than fetching the whole body.")
        else:
            note = (f"no sections numbered for Title {title_num.upper()} were found "
                    f"among the document's anchors — the title may use non-standard "
                    f"numbering; the document itself is returned.")
        return [doc_id], note
    if secs:
        return [doc_id], (f"the act's {len(secs)} sections are individually "
                          f"servable: get_document lists them under `subsections`, "
                          f"and part='SEC. NNN.' returns one section alone.")
    return [doc_id]


ACT_RE = (r"(?:the\s+)?(?P<act>" + "|".join(_ACTS.values()) + r")"
          r"(?:\s*,?\s*Title\s+(?P<title>[IVXivx]+))?")
register_scheme("federal-act-name", ACT_RE, resolver=_act)


# --------------------------------------------------------------------------- U.S. Code
# `42 U.S.C. 1396`, `20 USC § 1232g`, `29 USC § 3101`. ADR-0006 (supersedes ADR-0004): this
# corpus holds the U.S. Code sections Oregon cites, section by section, on demand -- never a
# title, never the Code speculatively, and a U.S.C. section is STILL never mapped onto a
# public law. That rule is ADR-0004's and survives its own supersession unchanged.
#
# THE REGEX IS IMPORTED FROM federal_ids.py, not redefined here (see the import comment
# above) -- the suffix group (`1320d-2`, not truncated to `1320d`) is a cross-corpus contract
# the sibling side already relies on, and a second, possibly-drifted copy here would be the
# exact class of bug that contract exists to prevent.
def _held_usc_sections() -> dict[str, dict]:
    """{document id: frontmatter} for every usc_section document actually held.

    See `_held_of_kind()` -- this is that filter, scoped to `usc_section`. ADR-0006 makes a
    partial hold the PERMANENT state of this corpus with respect to the U.S. Code, so the
    count this feeds into the refusal below changes every time a section is ingested; a
    typed number here is the same staleness bug `_held_of_kind()` already exists to close,
    with a larger blast radius, because the refusal is the one place a wrong count is served
    directly to a caller.
    """
    return _held_of_kind("usc_section")


def _usc(m, nodes=None):
    """Resolve a held U.S.C. section, or refuse by naming the real partial hold.

    THE MEMBERSHIP ANSWER AND THE REFUSAL COME FROM THE SAME LOOKUP: this looks the cited
    section up in HELD directly, and only builds the refusal -- from `_held_usc_sections()`,
    in this same call -- when that lookup misses. So "the cited section is not among them" is
    a fact this function just established, never a separate claim that could disagree with
    what the held branch would have returned.

    THE COUNT IS THE LENGTH OF THE LIST IT PRINTS, computed in the call rather than cached or
    typed (contrast `_PUBLAW`, built once at module level -- the count here must NOT follow
    that pattern, the same way `_cfr_one`'s "It holds {listing}" sentence is built fresh
    every time from `_held_cfr_parts()`). `held`, `n` and `listing` all come from ONE dict in
    ONE sentence below, so there is no arrangement in which the number printed disagrees with
    the citations printed beside it.
    """
    title, sec = m.group("title"), m.group("sec").lower()
    doc_id = f"{title}-usc-{sec}"
    fm = HELD.get(doc_id)
    if fm is not None and fm.get("instrument_kind") == "usc_section":
        currency = fm.get("currency")
        return [doc_id], (f"OLRC states this section is {currency}." if currency else None)

    held = _held_usc_sections()
    n = len(held)
    listing = sorted(hfm.get("citation", i) for i, hfm in held.items())
    unit = "section" if n == 1 else "sections"
    # NO TRUNCATION, matching `_cfr_one` (which lists all 50 held parts with no cap). A
    # cap here would contradict check_citations.py's own per-held-citation assertion --
    # "every held usc_section citation appears in the note" -- the moment the 11th
    # section landed, in a corpus ADR-0006 says will keep growing toward 742 cited
    # targets. A long note is the honest cost of a real partial hold; a note that stops
    # naming what it holds past some count is a guard that would fire on correct
    # behaviour, which is worse.
    shown = ", ".join(listing) or "none"
    return [], (
        f"{title} U.S.C. {m.group('sec')} is not held. This corpus holds {n} {unit} of the "
        f"U.S. Code — {shown} — and {title} U.S.C. {m.group('sec')} is not among them. The "
        f"codified section and the enacted text are different documents that diverge as "
        f"later acts amend the code, so a U.S. Code citation is never answered by "
        f"substituting a public law for it.")


register_scheme("usc-section", USC, resolver=_usc)
