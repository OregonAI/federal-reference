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

import pathlib
import re

import yaml

from corpus_toolkit.mcp.framework import register_scheme

INSTRUMENTS = pathlib.Path(__file__).resolve().parent.parent / "instruments"
PART_ID = "2-cfr-200"


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


def _section_numbers(text: str) -> frozenset[str]:
    """Section numbers appearing as `### § 200.NNN` headings in an extracted part text."""
    return frozenset(re.findall(r"^### §*\s*200\.(\d+)\b", text, re.M))


# Which sections the part ACTUALLY contains, current and as of the day before the 2021-02-22
# consolidation. Without these, a citation to a section that does not exist gets told to go
# find a heading that is not there — a confidently false instruction, and the kind of
# plausible-sounding wrong answer this corpus is built to refuse.
_SNAPSHOTS = INSTRUMENTS.parent / "_meta" / "snapshots"
_PART_SECTIONS = _section_numbers((INSTRUMENTS / f"{PART_ID}.md").read_text(encoding="utf-8"))
_FORMER_SECTIONS = _section_numbers(
    (_SNAPSHOTS / f"{PART_ID}-2021-02-21.txt").read_text(encoding="utf-8")) - _PART_SECTIONS


def _version_of(doc_id: str) -> str | None:
    v = (HELD.get(doc_id) or {}).get("version")
    return str(v) if v else None


def _norm_rev(s: str) -> str:
    return "".join((s or "").split()).replace("/", "-")


# --------------------------------------------------------------------------- CFR
# `2 CFR 200`, `2 C.F.R. § 200.303`, `2 CFR Part 200.303`, `2 CFR §§ 200.303`.
#
# ONE scheme covers part and section. Splitting them makes resolution depend on registration
# order, and the section form is the common one -- 188 of the 232 citations Oregon makes.
CFR_RE = (r"(?P<title>\d{1,2})\s*C\.?\s?F\.?\s?R\.?\s*(?:Part\s+)?§{0,2}\s*"
          r"(?P<part>\d{1,4})(?:\.(?P<sec>\d{1,4}))?\b")


def _cfr(m, nodes=None):
    title, part, sec = m.group("title"), m.group("part"), m.group("sec")

    if (title, part) != ("2", "200"):
        return [], (
            f"this corpus holds 2 CFR 200 (the Uniform Guidance) and does not hold "
            f"{title} CFR {part}. The citation is well-formed — it is simply outside what "
            f"has been ingested.")

    if sec is None:
        return [PART_ID], None

    doc = f"{PART_ID}.{sec}"
    fm = HELD.get(doc)

    if fm is None:
        if sec in _PART_SECTIONS:
            # The section IS inside the part we hold; it just was not split out, because only
            # the sections Oregon cites are. Returning the part is a TRUE answer, but it is a
            # different document from the one asked for, so it is labelled rather than
            # silently substituted.
            return [PART_ID], (
                f"§ 200.{sec} is not held as its own document — only the sections Oregon "
                f"cites are split out. Returning 2 CFR 200, the part that contains it; look "
                f"for the `### § 200.{sec}` heading in its full text.")

        # Not in the current part at all. Telling the caller to go find a heading that is not
        # there would be a confidently false instruction, so say what is actually true — and
        # if it was in force before the 2021-02-22 consolidation, say that, because for this
        # corpus's audit citations that is usually the real explanation.
        if sec in _FORMER_SECTIONS:
            return [], (
                f"§ 200.{sec} is NOT in the current 2 CFR 200. It existed until the "
                f"2021-02-22 amendment, which consolidated Subpart A's definitions into "
                f"§ 200.1. It is not held individually — only § 200.53 and § 200.62 are, "
                f"because those are the removed sections Oregon material actually cites. "
                f"For the current treatment see 2-cfr-200.1.")
        return [], (
            f"there is no § 200.{sec} in 2 CFR 200 as of {HELD[PART_ID].get('as_of')}, and "
            f"none in the 2021-02-21 text either. Check the citation — it may name a "
            f"different title or part.")

    if fm.get("status") == "superseded":
        return [doc], (
            f"§ 200.{sec} was REMOVED from the CFR on {fm.get('amended_on')}. What is "
            f"returned is its LAST-IN-FORCE text (as of {fm.get('as_of')}), held because "
            f"Oregon material still cites it. It is NOT current law — the current treatment "
            f"is in {fm.get('superseded_by')}, and the two may differ.")

    return [doc], None


register_scheme("cfr", CFR_RE, resolver=_cfr)


# --------------------------------------------------------------------------- Public law
# `Pub. L. 113-128`, `Public Law No. 115-224`, `PL 113-128`.
PUBLAW_RE = (r"P(?:ub(?:lic)?)?\.?\s*L(?:aw)?\.?\s*(?:No\.?\s*)?"
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
IRSPUB_RE = (r"IRS\s+Pub(?:lication)?\.?\s*(?P<num>\d{3,4})"
             r"(?:\s*\(?\s*Rev\.?\s*(?P<rev>\d{1,2}\s*[-/]\s*\d{4})\s*\)?)?")


def _irspub(m, nodes=None):
    num, rev = m.group("num"), _norm_rev(m.group("rev") or "")
    doc = f"irs-pub-{num}"
    if doc not in HELD:
        held_pubs = ", ".join(sorted(i for i in HELD if i.startswith("irs-pub-")))
        return [], (f"IRS Publication {num} is not held; this corpus holds "
                    f"{held_pubs or 'no IRS publications'}.")

    held = _version_of(doc)
    if rev and held and rev != held:
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
CJIS_RE = (r"CJIS(?:\s+Security)?(?:\s+Policy|\s+SP)?\.?\s*"
           r"(?:v(?:ersion)?\.?\s*)?(?P<ver>\d+(?:\.\d+){0,2})?")

_CJIS = next((i for i in sorted(HELD) if i.startswith("cjis-")), None)


def _cjis(m, nodes=None):
    if _CJIS is None:
        return [], "no CJIS Security Policy is held by this corpus."
    ver, held = m.group("ver"), _version_of(_CJIS)

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


# --------------------------------------------------------------------------- U.S. Code
# `42 U.S.C. 1396`, `29 USC § 3101`.
#
# REGISTERED EVEN THOUGH IT NEVER RESOLVES — a deliberate exception to the rule that a
# scheme resolving nothing is worse than none. Left unmatched, a U.S.C. citation returns
# "no citation scheme recognized this format", which invites the reader to conclude the
# corpus merely failed to parse it. Matched, it returns the true and more useful statement:
# this corpus holds ENACTED PUBLIC LAWS and named federal publications, not the codified
# U.S. Code, and here are the public laws it does hold.
#
# It must never map a U.S.C. section onto a public law. The codified section and the enacted
# text are different documents, and they diverge as later acts amend the code. The seed
# sketched exactly that aliasing ("with the U.S.C. sections it created as aliases"); it is
# not implemented, because it would resolve a citation to a document that is not what was
# cited.
USC_RE = r"(?P<title>\d{1,2})\s*U\.?\s?S\.?\s?C\.?\s*(?:§{1,2}\s*)?(?P<sec>\d{1,5}[a-z]{0,2})\b"


def _usc(m, nodes=None):
    laws = ", ".join(f"{HELD[i].get('citation', i)} ({i})" for i in sorted(_PUBLAW.values()))
    return [], (
        f"this corpus does not hold the U.S. Code. It holds enacted public laws and named "
        f"federal publications: {laws or 'none'}. The codified section and the enacted text "
        f"are different documents that diverge as later acts amend the code, so "
        f"{m.group('title')} U.S.C. {m.group('sec')} is not answered by substituting one "
        f"for the other.")


register_scheme("usc-section", USC_RE, resolver=_usc)
