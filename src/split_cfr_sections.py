#!/usr/bin/env python3
"""Promote the cited sections of a CFR part into their own documents.

    python3 src/split_cfr_sections.py                       # every part with a cited-sections file
    python3 src/split_cfr_sections.py --part-id 2-cfr-200    # one part only
    python3 src/split_cfr_sections.py --refetch              # re-fetch historical snapshots

Reads `_meta/cited-sections/<part_id>.yml` (produced by src/scan_cited_sections.py) and
writes one `instruments/<part_id>.NNN.md` per cited section. Run AFTER ingest_instruments.py.

WHY SPLIT AT ALL. 85% of the section-or-part citations Oregon makes to the Uniform Guidance
are section-level (256 of 300), and § 200.303 alone accounts for 58. A corpus holding only the
part answers "2 CFR 200" and misses every one of those, so the sibling edges built in Stage 4
would resolve the least-cited form of the citation and nothing else. #21 measured the same
shape for 28 CFR Part 35 (30 of 32 citations section-level) -- see #34.

NO REFETCH FOR CURRENT SECTIONS. Their text is sliced out of the part snapshot already
committed by Stage 1, and each document points at it with `snapshot_id: <part_id>` -- the
field exists for exactly this ("documents split from, or sharing, one source file"). That
means a section document cannot disagree with the part it came from: there is one source of
truth on disk and provenance verifies both against it (src/slicing.py).

REMOVED SECTIONS ARE THE INTERESTING CASE. A section cited by Oregon material but no longer
in the CFR is a finding, not a drop: 2 CFR 200.53 and 200.62 were removed by the 2021-02-22
amendment, and Oregon audits 2020-14, 2021-13 and 2022-18 cite them anyway, because they were
in force for the fiscal years under audit. Each is ingested from a point-in-time snapshot of
the day BEFORE its removal date -- its last-in-force text -- with status `superseded` and
`superseded_by` naming the section its content moved into, WHEN that fact is recorded (see
src/cfr_consolidations.py). Resolving one to current text would hand back law that was not in
force when it was cited; dropping it would leave a real citation pointing at nothing.

#34 GENERALIZED THIS FILE FROM 2 CFR 200 ALONE. Four things used to be module-level constants
true only of that one part: the part id, the eCFR fetch URL, the section-number regex, and the
heading-stripping regex. All four are now per-part -- computed from `--part-id` or discovered
from which `_meta/cited-sections/*.yml` files are committed. Two more hardcodes travelled
alongside them and are fixed here too, both flagged by #33's own review: `issuing_body` was
the literal "Office of Management and Budget" (right for OMB's part, wrong for anyone else's)
and now comes from the part's own manifest entry, same as ingest_instruments.py's
resolve_issuing_body(); and the removed-section note's "consolidated into" claim was hardcoded
prose about Subpart A now sourced from src/cfr_consolidations.py, the same shared record
citation_schemes.py reads, so the two callers cannot describe the same amendment two different
ways.

REGENERATING 2 CFR 200 IS NOT BYTE-IDENTICAL to what was committed before this change, and
that is deliberate, not a regression: two sentences moved from a hardcoded literal to a
manifest/record read. "- Part: 2 CFR 200 (Uniform Guidance)" is now "- Part: 2 CFR 200 --
<the part's own manifest title>", and the removed-section note's phrasing now matches
citation_schemes.py's wording verbatim instead of a second, independently-worded copy of the
same fact. Every FIELD (as_of, amended_on, source_sha256, snapshot_id, the extracted body
text) is unchanged; only these two prose sentences read differently, and both are still true.
"""
from __future__ import annotations

import argparse
import datetime
import pathlib
import re
import sys
import time
import xml.etree.ElementTree as ET
from dataclasses import dataclass

import yaml

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from ingest_instruments import _flatten, fetch, resolve_issuing_body  # noqa: E402  (same extraction)
from cfr_consolidations import CONSOLIDATIONS  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parent.parent
SNAPSHOTS = ROOT / "_meta" / "snapshots"
INSTRUMENTS = ROOT / "instruments"
CITED_DIR = ROOT / "_meta" / "cited-sections"
MANIFEST = ROOT / "_meta" / "source-manifest.yml"


def guard(text: str) -> str:
    """Never let extracted text start a line with `## `.

    corpus_toolkit.repo.FULLTEXT_RE ends the body at the first such line. This has cost this
    platform a truncated document three times now -- twice from source text, once from a
    heading we emitted ourselves -- and each time the file looked perfectly well-formed. CFR
    prose is very unlikely to trip it; the guard costs nothing and the failure is silent.
    """
    return re.sub(r"^(#{1,6}\s)", r" \1", text, flags=re.M)


def sections_from(raw: bytes, part: str) -> dict[str, tuple[str, str]]:
    """{'200.303': (heading, body_text)} for every SECTION in a part XML.

    `part` is the CFR part number as a string ("200", "37") -- the heading match and the
    returned keys are both anchored on it, so a part XML never yields another part's sections
    by accident.

    Mirrors extract_cfr()'s per-element logic exactly, so a section's text here is the same
    run of lines the part document holds -- which is what makes provenance against the shared
    snapshot come out whole rather than approximately.
    """
    out: dict[str, tuple[str, str]] = {}
    p = re.escape(part)
    for el in ET.fromstring(raw).iter():
        if el.get("TYPE") != "SECTION":
            continue
        head_el = el.find("HEAD")
        head = _flatten(head_el) if head_el is not None else (el.get("N") or "")
        # \b on BOTH ends. Missing the leading boundary let a short part number match inside
        # a longer one -- part "1" matched "§ 21.5" at "1.5", yielding the wrong key "1.5".
        # Harmless for part 200 (why this shipped) and for 37/35/99, but this generalization's
        # whole point is that the part number is now an input, so it stops being harmless the
        # day a one- or two-digit part is processed. scan_cited_sections.patterns() already
        # anchors both ends; sections_from() and subject() (^-anchored, so safe already) were
        # the odd pair out.
        m = re.search(rf"\b{p}\.(\d+)\b", head or "")
        if not m:
            continue
        body = [f"### {head}"]
        for child in el:
            if child is head_el:
                continue
            # Guard the EXTRACTED text only, never the heading we emit ourselves. Applying it
            # to the assembled body rewrote `### § 200.53 …` to ` ### § 200.53 …`, which broke
            # the slicer's `^### ` anchor and, worse, made the section text stop matching the
            # part it was cut from — the one property this file exists to preserve.
            t = guard(_flatten(child))
            if t:
                body.append(t)
        out[f"{part}.{m.group(1)}"] = (head, "\n".join(body))
    return out


def subject(head: str, part: str) -> str:
    """'§ 200.303 Internal controls.' -> 'Internal controls'."""
    s = re.sub(rf"^\s*§*\s*{re.escape(part)}\.\d+\s*", "", head or "").strip()
    return s.rstrip(".").strip() or "Untitled section"


def manifest_entry(part_id: str) -> dict:
    """This part's own `_meta/source-manifest.yml` entry -- the one place issuing_body,
    citation, and title are declared for a specific cfr_part, checked by a reviewer at PR
    time. Raises rather than guessing when the id is not a manifest source at all: that means
    ingest_instruments.py has not been pointed at this part yet, which this script cannot
    recover from any more than it could recover a missing part snapshot."""
    manifest = yaml.safe_load(MANIFEST.read_text())
    for src in manifest["sources"]:
        if src["id"] == part_id:
            return src
    raise SystemExit(f"error: {part_id!r} is not a source in {MANIFEST.relative_to(ROOT)}")


@dataclass(frozen=True)
class PartCtx:
    """Everything about ONE part that every section document it splits into shares."""
    part_id: str        # "2-cfr-200"
    title: str           # "2"
    part: str            # "200"
    part_title: str      # the manifest's own `title` -- the part's full official name
    issuing_body: str
    part_as_of: str
    part_retrieved: str


@dataclass(frozen=True)
class HistCtx:
    """Everything about ONE historical (last-in-force) snapshot a removed section is cut from."""
    hist_id: str
    hist_url: str
    hist_retrieved: str
    last_in_force: str


def part_dates(part_id: str) -> tuple[str, str]:
    """(as_of, retrieved) from the part document.

    Inherited rather than restated. A section carries the SAME bytes as the part it was cut
    from, so a section claiming a different as_of than its part would be asserting two
    different dates for one piece of text -- and in a corpus where the whole argument is
    "the version is part of the identity", that is the last field to let drift.
    """
    fm = yaml.safe_load((INSTRUMENTS / f"{part_id}.md").read_text().split("---")[1])
    return str(fm["as_of"]), str(fm["retrieved"])


def hist_retrieved(part_id: str, hist_xml: pathlib.Path, fetched: bool,
                    removed_secs: list[str]) -> str:
    """`retrieved` for SUPERSEDED sections cut from THIS historical snapshot -- not the part.

    This used to be inherited from the part, justified by the same reasoning as `part_dates`:
    a section carries the same bytes as the part, so it inherits the part's dates. That
    argument does NOT apply here. The superseded sections are cut from a different file — the
    point-in-time snapshot — fetched at a different time from a different URL. Inheriting the
    part's date made two documents assert a retrieval that belonged to bytes they were not cut
    from, and it moved every time the part was re-ingested.

    `removed_secs` are the section-number suffixes (e.g. ["53", "62"]) that share THIS
    snapshot, so a re-run without --refetch can recover a previously published `retrieved`
    from whichever of them already has a committed document, instead of hardcoding which
    sections that could be.
    """
    if fetched:
        return time.strftime("%Y-%m-%d")
    for sec in removed_secs:
        doc = INSTRUMENTS / f"{part_id}.{sec}.md"
        if doc.is_file():
            try:
                fm = yaml.safe_load(doc.read_text(encoding="utf-8").split("---")[1])
            except (IndexError, yaml.YAMLError):
                continue
            if (fm or {}).get("retrieved"):
                return str(fm["retrieved"])
    return time.strftime("%Y-%m-%d", time.localtime(hist_xml.stat().st_mtime))


def committed_amended_on(part_id: str, sec: str) -> str | None:
    """`amended_on` already committed for SEC's document -- what --check trusts instead of
    eCFR's versions endpoint (see the `vers` assignment in run_part()).

    ecfr_versions() is a live network call with nothing committed to compare against -- unlike
    the historical snapshot (which has a `.xml`/`.txt` file on disk) or the cited-sections file
    (which has its own committed YAML), there is no local anchor for "is this section's
    amendment date still accurate upstream." #58 found this the same way it found the
    historical-snapshot fetch: --check must not reach the network, and where it genuinely
    cannot answer without doing so, it trusts what is already on disk rather than guessing
    `None`, which would make every current section's document read as stale for a field
    --check has no offline way to verify in the first place. Same "recover a previously
    published field from a committed document" shape as hist_retrieved().

    THE KNOWN LIMIT OF "TRUSTS": trusting the document IS the document is not verifying it --
    a hand-edited `amended_on` in an already-committed document now round-trips through this
    function unchallenged, since it is read back from the very file `--check` then diffs
    against. #73 tracks whether a genuinely independent offline anchor (a candidate: the part
    snapshot's own `<CITA>` source notes) is worth building; this function is the honest
    interim, not the fix.
    """
    doc = INSTRUMENTS / f"{part_id}.{sec.split('.', 1)[1]}.md"
    if not doc.is_file():
        return None
    try:
        fm = yaml.safe_load(doc.read_text(encoding="utf-8").split("---")[1])
    except (IndexError, yaml.YAMLError):
        return None
    # Frontmatter that parses but not to a mapping (a hand-mangled `---\nsome scalar\n---`)
    # is exactly the malformed-document case this function exists to survive, same as a
    # missing file or unparseable YAML above -- `isinstance` here rather than widening the
    # `except`, which would also swallow an unrelated AttributeError from deeper in PyYAML.
    if not isinstance(fm, dict):
        return None
    return fm.get("amended_on")


def _target_doc(part_id: str, consolidation: dict | None, default: str | None) -> str | None:
    """The document id a recorded consolidation's `into` section lands in, or `default` when
    no consolidation is recorded for this part.

    Pulled out because this exact expression was written three times with a DIFFERENT
    `default` in each copy (None in build() and run_part()'s current-section loop, `part_id`
    in run_part()'s removed-section loop) -- the divergence is load-bearing (it decides
    whether an unrecorded consolidation yields `superseded_by: null` or `superseded_by:
    <part_id>`), so a reader had to diff three near-identical lines to learn the rule instead
    of reading one parameter.
    """
    if consolidation and consolidation.get("into"):
        return f"{part_id}.{consolidation['into'].split('.', 1)[-1]}"
    return default


def _removal_clause(consolidation: dict | None, target_doc: str | None) -> str:
    """The clause naming WHAT happened to a removed section's content, generalized from the
    single hardcoded 'when the definitions in Subpart A were consolidated into § 200.1'.

    Mirrors citation_schemes.py's own fallback ladder exactly (see its `_cfr_one`): a
    `scope` names WHAT moved, an `into` with no `scope` still names WHERE without guessing
    what, and no record at all stays true and generic rather than inventing either.
    """
    if consolidation and consolidation.get("into") and target_doc:
        target = consolidation["into"]
        if consolidation.get("scope"):
            return f"when {consolidation['scope']} were consolidated into [§ {target}](./{target_doc}.md)"
        return f"when its content was consolidated into [§ {target}](./{target_doc}.md)"
    return "and no successor section is recorded here"


def build(ctx: PartCtx, sec: str, head: str, body: str, meta: dict, sha: str,
          amended_on: str | None, superseded_by: str | None,
          hist: HistCtx | None = None, consolidation: dict | None = None,
          supersedes: list[str] | None = None) -> str:
    live = superseded_by is None
    doc_id = f"{ctx.part_id}.{sec.split('.', 1)[1]}"
    citation = f"{ctx.title} CFR {sec}"
    subj = subject(head, ctx.part)
    target_doc = _target_doc(ctx.part_id, consolidation, None)
    fm = {
        "schema_version": 1,
        "corpus": "federal-reference",
        "jurisdiction": "us",
        "id": doc_id,
        # THE TITLE CARRIES THE SUPERSESSION, and that is load-bearing rather than cosmetic.
        # A sibling corpus resolves into this one through `corpus-index.json`, whose rows are
        # [title, doc_type, path] -- no `status`, no `version`. So an audit resolving
        # `2 CFR 200.53` gets back a title and nothing else, and without the marker it reads
        # as current law. Frontmatter `status: superseded` is invisible across that boundary.
        "title": (f"{citation} — {subj}" if live else
                  f"{citation} — {subj} (SUPERSEDED {meta['removed_on']})"),
        "doc_type": "federal_instrument",
        "citation": citation,
        "authority_level": "federal",
        "issuing_body": ctx.issuing_body,
        "instrument_kind": "cfr_section",
        "version": None,
        "as_of": ctx.part_as_of if live else hist.last_in_force,
        "amended_on": amended_on,
        "reproduction_basis":
            "17 U.S.C. § 105 — edition of the CFR published by the U.S. government",
        "superseded_by": superseded_by,
        "source_url": (f"https://www.ecfr.gov/current/title-{ctx.title}/section-{sec}" if live
                       else hist.hist_url),
        "source_format": "xml",
        # Shared with the part document rather than duplicated. One source of truth on disk,
        # so a section cannot silently drift from the part it was cut out of.
        "snapshot_id": ctx.part_id if live else hist.hist_id,
        "retrieved": ctx.part_retrieved if live else hist.hist_retrieved,
        "source_sha256": sha,
        "status": "current" if live else "superseded",
        "content_mode": "verbatim",
        "relationships": {"related": [ctx.part_id]},
        "maintainer": "@morficflux",
        # Left EMPTY on purpose; a human sets them at PR approval. An ingester that stamps a
        # verification it did not perform is worse than a blank.
        "last_verified": "",
        "verified_by": "",
    }
    if supersedes:
        fm["relationships"]["supersedes"] = supersedes

    head_yaml = yaml.safe_dump(fm, sort_keys=False, allow_unicode=True, width=100).rstrip()
    cites = meta["citations"]
    parts = [f"---\n{head_yaml}\n---\n", "## At a glance\n",
             f"**{citation}** — {subj}\n\n"
             f"- Issued by: {ctx.issuing_body}\n"
             f"- Part: {ctx.title} CFR {ctx.part} — {ctx.part_title}\n"
             f"- Text as of: {fm['as_of']}"
             + (f" (section last amended {amended_on})" if amended_on else "")
             + f"\n- Cited by Oregon material: {cites} time{'s' if cites != 1 else ''} "
               f"({', '.join(meta['cited_in'])})\n"
             f"- Reproduction basis: {fm['reproduction_basis']}\n"]

    if live:
        parts.append(
            f"\n_NON-AUTHORITATIVE copy of one section, cut from the {ctx.title} CFR "
            f"{ctx.part} snapshot this corpus holds. This is a federal requirement and "
            f"carries penalties state policy does not — read it at the source URL before "
            f"relying on it. This copy is CURRENT text, which is not necessarily the text in "
            f"force when a document citing it was written._\n")
    else:
        clause = _removal_clause(consolidation, target_doc)
        drop_in_warning = (
            f", and do not treat § {consolidation['into']} as a drop-in replacement without "
            f"comparing them.\n"
            if consolidation and consolidation.get("into") else ".\n")
        parts.append(
            f"\n> **This section no longer exists.** It was removed from the CFR on "
            f"**{meta['removed_on']}**, {clause}. The text below is its **last-in-force** "
            f"text, as of {hist.last_in_force}.\n>\n"
            f"> It is held because Oregon material still cites it {cites} "
            f"time{'s' if cites != 1 else ''} — those citations were made for fiscal years "
            f"when this section was in force. **The current definition may differ.** Do not "
            f"read this as current law" + drop_in_warning +
            f"\n_NON-AUTHORITATIVE copy of one section, as it stood on {hist.last_in_force}. "
            f"Read it at the source URL before relying on it. This is **superseded** text and "
            f"is NOT current law._\n")

    parts.append("\n## Full text\n\n" + body + "\n")
    return "\n".join(parts)


PART_ID_RE = re.compile(r"^\d+-cfr-\d+$")


def discover_part_ids() -> list[str]:
    """Every committed `<title>-cfr-<part>.yml` stem in _meta/cited-sections/.

    Filtered by shape, not just glob("*.yml") -- a stray file there (a README, an editor
    backup) used to reach run_part()'s `part_id.split("-cfr-", 1)` unpack and crash CI with a
    bare ValueError traceback instead of the named error every other failure in this file
    produces.
    """
    if not CITED_DIR.is_dir():
        return []
    stems = sorted(p.stem for p in CITED_DIR.glob("*.yml"))
    bad = [s for s in stems if not PART_ID_RE.match(s)]
    if bad:
        raise SystemExit(
            f"error: {CITED_DIR.relative_to(ROOT)}/ contains file(s) that are not a "
            f"<title>-cfr-<part>.yml part id: {', '.join(bad)}")
    return stems


def run_part(part_id: str, args: argparse.Namespace) -> int:
    """Process one CFR part end to end. Returns 0 on success, 1 on any failure."""
    from corpus_toolkit.repo import hash_snapshot
    from scan_cited_sections import (CURRENT_COMMENT, REMOVED_COMMENT, UNRESOLVABLE_COMMENT,
                                      ecfr_versions, static_header)

    title, part = part_id.split("-cfr-", 1)

    cited_path = CITED_DIR / f"{part_id}.yml"
    if not cited_path.is_file():
        print(f"error: {cited_path} missing — run src/scan_cited_sections.py first",
              file=sys.stderr)
        return 1
    cited_raw_lines = cited_path.read_text(encoding="utf-8").splitlines()
    cited = yaml.safe_load("\n".join(cited_raw_lines))
    # A part with no removed (or, in principle, no current) sections gets a bare `removed:`
    # key in the generated YAML, which loads as None rather than []. 7 of the 8 queued
    # instruments have zero removed sections -- 2 CFR 200 is the one part whose two removals
    # hid this. Same guard ingest_instruments.cited_section_ids() already uses one file over.
    cited["current"] = cited.get("current") or []
    cited["removed"] = cited.get("removed") or []
    cited["unresolvable"] = cited.get("unresolvable") or []

    # HEADER STALENESS, checked without re-running the scan (which needs the sibling repos CI
    # cannot reach -- see scan_cited_sections.py's module docstring). A committed cited-sections
    # file was once `git mv`'d without being regenerated: its own "Regenerate with:" line kept
    # advertising a command missing --title/--part, and its "current" comment named a specific
    # year. Neither is scan-derived, so both can be checked against the CURRENT generator here,
    # every PR, with no network call.
    header_mismatch = None
    if args.check:
        expected_top = static_header(int(title), int(part))
        if cited_raw_lines[:len(expected_top)] != expected_top:
            header_mismatch = "the top comment block (regenerate command / CI-cannot-reach note)"
        elif CURRENT_COMMENT not in cited_raw_lines:
            header_mismatch = "the 'current:' comment line"
        elif "removed:" in cited_raw_lines:
            ridx = cited_raw_lines.index("removed:")
            if cited_raw_lines[ridx - len(REMOVED_COMMENT):ridx] != REMOVED_COMMENT:
                header_mismatch = "the 'removed:' comment block"
        # The generator has written an `unresolvable:` block unconditionally since #66 (see
        # scan_cited_sections.py) -- a file regenerated before that key existed, or hand-moved
        # the way the header-staleness check above was written to catch, would otherwise pass
        # `--check` while missing it entirely, which is exactly the drift this whole block
        # exists to catch one field over.
        if header_mismatch is None:
            if "unresolvable:" not in cited_raw_lines:
                header_mismatch = "the 'unresolvable:' key (missing entirely)"
            else:
                uidx = cited_raw_lines.index("unresolvable:")
                if cited_raw_lines[uidx - len(UNRESOLVABLE_COMMENT):uidx] != UNRESOLVABLE_COMMENT:
                    header_mismatch = "the 'unresolvable:' comment block"

    part_xml = SNAPSHOTS / f"{part_id}.xml"
    if not part_xml.is_file():
        print(f"error: {part_xml} missing — run src/ingest_instruments.py first",
              file=sys.stderr)
        return 1

    src = manifest_entry(part_id)
    issuing_body = resolve_issuing_body(src)
    part_as_of, part_retrieved = part_dates(part_id)
    current = sections_from(part_xml.read_bytes(), part)
    print(f"  part snapshot: {len(current)} sections")

    ctx = PartCtx(part_id=part_id, title=title, part=part, part_title=src["title"],
                  issuing_body=issuing_body, part_as_of=part_as_of, part_retrieved=part_retrieved)

    part_txt = (SNAPSHOTS / f"{part_id}.txt").read_text(encoding="utf-8")

    # THE INVARIANT, CHECKED RATHER THAN ASSERTED IN A COMMENT. Every current section's text
    # must appear verbatim in the part snapshot it shares. A comment in Stage 1 claimed a
    # guard the code did not implement and 2 CFR 200 shipped 1 character of 633,121 looking
    # perfectly well-formed; the lesson is to make the claim executable. This catches any
    # divergence between this extractor and extract_cfr(), including whitespace.
    for entry in cited["current"]:
        sec = entry["section"]
        if sec in current and current[sec][1] not in part_txt:
            print(f"error: {sec} text does not appear verbatim in {part_id}.txt — this "
                  f"extractor has diverged from extract_cfr()", file=sys.stderr)
            return 1
    print(f"  verified: all {len(cited['current'])} current sections appear verbatim in the "
          f"part snapshot")

    part_sha = hash_snapshot(part_id, "xml", SNAPSHOTS)
    # #58: ecfr_versions() is a live fetch of eCFR's versions endpoint, with no committed file
    # behind it -- reaching it unconditionally is the same "verify or fetch" ambiguity #58
    # names, one call earlier than the historical-snapshot fetch this issue was filed against.
    # --check skips it; committed_amended_on() (used below, per section) is the offline
    # substitute.
    vers = {} if args.check else ecfr_versions(int(title), int(part))
    consolidation = CONSOLIDATIONS.get(part_id)

    # --- historical snapshots, ONE PER DISTINCT removal date -----------------------------
    # #34: this used to be one hardcoded LAST_IN_FORCE date for the whole part, correct only
    # because 2 CFR 200's two removed sections share one amendment. Grouping by each removed
    # entry's OWN `removed_on` (already recorded per-section by scan_cited_sections.py) makes
    # a part whose removed sections came from different amendments work the same way, and is
    # exactly equivalent to the old behaviour when they do not.
    by_date: dict[str, list[dict]] = {}
    for entry in cited["removed"]:
        by_date.setdefault(entry["removed_on"], []).append(entry)

    stale: list[str] = []

    def emit(path, text: str) -> None:
        """Write, or in --check mode record a mismatch.

        WITHOUT --check THESE FILES WERE UNGATED. _meta/cited-sections/<part>.yml says
        "GENERATED -- do not hand-edit" and its section documents are generated from it, but
        nothing compared them: edit either side and CI stayed green, which is the exact
        failure the `generated` job exists to prevent and which this repo's own AGENTS.md
        forbids.
        """
        if args.check:
            if not path.is_file() or path.read_text(encoding="utf-8") != text:
                stale.append(path.name)
        else:
            path.write_text(text, encoding="utf-8")

    # --- historical snapshots, ONE PER DISTINCT removal date, --check NEVER FETCHES ONE ----
    # #58: this loop used to fetch and write unconditionally, so a `--check` run over a part
    # whose historical snapshot was missing (or `--refetch` combined with `--check`, rejected
    # in main() before this ever runs) reached the network and mutated the working tree from a
    # step whose job is verification. `--check` now refuses instead: a missing snapshot is
    # reported the same way a stale document or an orphan is, and the .txt derivation below
    # goes through `emit()` like every other generated file, so nothing under `--check` writes.
    hist_by_date: dict[str, HistCtx] = {}
    hist_secs: dict[str, dict[str, tuple[str, str]]] = {}
    missing_hist: dict[str, str] = {}   # removed_on -> the snapshot path --check could not read
    for removed_on, entries in sorted(by_date.items()):
        last_in_force = (datetime.date.fromisoformat(removed_on)
                          - datetime.timedelta(days=1)).isoformat()
        hist_id = f"{part_id}-{last_in_force}"
        hist_xml = SNAPSHOTS / f"{hist_id}.xml"
        url = (f"https://www.ecfr.gov/api/versioner/v1/full/{last_in_force}"
               f"/title-{title}.xml?part={part}")
        if not hist_xml.is_file():
            if args.check:
                missing_hist[removed_on] = str(hist_xml.relative_to(ROOT))
                continue
            print(f"  fetching {last_in_force} point-in-time snapshot …")
            # Same call ingest_instruments.fetch() makes for the current snapshot -- reused
            # here rather than a second urlopen so the eCFR-compression fix (both endpoints
            # are the same `/full/` shape) lives in one place, not two.
            fetch(url, hist_xml, refetch=True)
            fetched = True
        elif args.refetch:
            # Unreachable under --check: main() rejects --check+--refetch outright, since
            # "re-fetch, but verify only" is not a coherent request. The branch stays explicit
            # here rather than trusting that a caller several stack frames away enforced it.
            print(f"  re-fetching {last_in_force} point-in-time snapshot …")
            fetch(url, hist_xml, refetch=True)
            fetched = True
        else:
            fetched = False
        retrieved = hist_retrieved(part_id, hist_xml, fetched,
                                    [e["section"].split(".", 1)[1] for e in entries])
        hsecs = sections_from(hist_xml.read_bytes(), part)
        print(f"  {last_in_force} snapshot: {len(hsecs)} sections")

        # The historical .txt is what provenance matches the superseded sections against, so
        # it must be the SAME extraction the documents were cut from, not a re-derivation.
        # Routed through emit() so --check compares it instead of writing it -- it used to
        # write unconditionally, the other half of #58.
        hist_text = re.sub(
            r"\n{3,}", "\n\n",
            "\n\n".join(hsecs[k][1] for k in sorted(hsecs, key=lambda s: int(s.split(".")[1])))
        ).strip()
        emit(SNAPSHOTS / f"{hist_id}.txt", hist_text)

        hist_by_date[removed_on] = HistCtx(hist_id=hist_id, hist_url=url,
                                            hist_retrieved=retrieved,
                                            last_in_force=last_in_force)
        hist_secs[removed_on] = hsecs

    written = 0
    for entry in cited["current"]:
        sec = entry["section"]
        if sec not in current:
            print(f"error: {sec} is listed as current but absent from the part snapshot",
                  file=sys.stderr)
            return 1
        head, body = current[sec]
        amended = (committed_amended_on(part_id, sec) if args.check
                   else (vers.get(sec) or {}).get("amendment_date"))
        out = INSTRUMENTS / f"{part_id}.{sec.split('.', 1)[1]}.md"
        # A removed section's target lands HERE, among the current sections, if this section
        # IS that consolidation's `into` -- computed from the shared record, not hardcoded to
        # any one section number.
        target_doc = _target_doc(part_id, consolidation, None)
        supersedes = None
        if target_doc and out.name == f"{target_doc}.md":
            # #57: the record is only TRUE of removed sections from the amendment its own
            # `date` names. `by_date.values()` (every removal, from every amendment) used to
            # be swept in here unconditionally -- a section removed by a LATER amendment would
            # gain a `supersedes` back-edge to an earlier consolidation it had nothing to do
            # with. `by_date.get(consolidation.get("date"), [])` is exactly the removed entries
            # that amendment actually produced -- `.get`, not `[...]`, because cfr_consolidations
            # .py's own docstring requires `scope`, not `date`; a record with no `date` matches
            # no `removed_on` and yields no supersedes edge instead of crashing run_part().
            ids = [f"{part_id}.{e['section'].split('.', 1)[1]}"
                   for e in by_date.get(consolidation.get("date"), [])] if consolidation else []
            supersedes = ids or None
        emit(out, build(ctx, sec, head, body, entry, part_sha, amended, None,
                         supersedes=supersedes))
        written += 1

    for entry in cited["removed"]:
        sec = entry["section"]
        removed_on = entry["removed_on"]
        if removed_on in missing_hist:
            # #58: --check only. The snapshot this removed section would be cut from was not
            # committed, and --check refuses to fetch it -- reported once below, not per
            # section; nothing to build here without the bytes.
            continue
        hist = hist_by_date[removed_on]
        hsecs = hist_secs[removed_on]
        if sec in current:
            print(f"error: {sec} is listed as removed but IS in the current part snapshot",
                  file=sys.stderr)
            return 1
        if sec not in hsecs:
            print(f"error: {sec} absent from the {hist.last_in_force} snapshot too",
                  file=sys.stderr)
            return 1
        head, body = hsecs[sec]
        hist_sha = hash_snapshot(hist.hist_id, "xml", SNAPSHOTS)
        # #57: this removed section only gets the shared record's `into`/`scope` when the
        # record's OWN `date` is the amendment that actually removed IT -- not any consolidation
        # recorded anywhere for the part. A mismatch falls back to `entry_consolidation=None`,
        # the same generic "no successor section is recorded here" clause a part with no
        # record at all already gets from _removal_clause().
        entry_consolidation = (consolidation if consolidation
                                and consolidation.get("date") == removed_on else None)
        target_doc = _target_doc(part_id, entry_consolidation, part_id)
        out = INSTRUMENTS / f"{part_id}.{sec.split('.', 1)[1]}.md"
        emit(out, build(ctx, sec, head, body, entry, hist_sha, entry["removed_on"], target_doc,
                         hist=hist, consolidation=entry_consolidation))
        written += 1
        print(f"    {sec} superseded -> {target_doc}  ({entry['citations']} citations)")

    if args.check:
        # An EXTRA section document nobody generates is drift too -- a hand-added file, or one
        # left behind when a section drops out of the citation list.
        expected = {f"{part_id}.{e['section'].split('.', 1)[1]}.md"
                    for e in cited["current"] + cited["removed"]}
        orphans = sorted(p.name for p in INSTRUMENTS.glob(f"{part_id}.*.md")
                         if p.name not in expected)
        if stale or orphans or header_mismatch or missing_hist:
            for n in stale:
                print(f"  STALE    {n}", file=sys.stderr)
            for n in orphans:
                print(f"  ORPHAN   {n} — not in {cited_path.relative_to(ROOT)}", file=sys.stderr)
            for removed_on, path in sorted(missing_hist.items()):
                print(f"  MISSING SNAPSHOT  {path} — needed for the section(s) removed "
                      f"{removed_on}; --check does not fetch it", file=sys.stderr)
            if header_mismatch:
                print(f"  STALE HEADER  {cited_path.relative_to(ROOT)} — {header_mismatch} does "
                      f"not match what src/scan_cited_sections.py writes for {title} CFR {part} "
                      f"today", file=sys.stderr)
                print(f"\nRe-run: python3 src/scan_cited_sections.py --erf ../oregon-policy-repo "
                      f"--audits ../oregon-audits --title {title} --part {part}", file=sys.stderr)
            if stale or orphans or missing_hist:
                print(f"\nRe-run: python3 src/split_cfr_sections.py --part-id {part_id}",
                      file=sys.stderr)
            return 1
        print(f"  {written} section documents are current")
        return 0

    print(f"  wrote {written} section documents")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                  formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--part-id", help="process only this cfr_part id (e.g. 2-cfr-200); "
                    "default: every part with a committed _meta/cited-sections/*.yml")
    ap.add_argument("--refetch", action="store_true",
                    help="re-fetch historical snapshots even if committed")
    ap.add_argument("--check", action="store_true",
                    help="verify the committed section documents match what this would write")
    args = ap.parse_args()

    if args.check and args.refetch:
        # #58: --check is a read-only, offline verification step -- "re-fetch, but only
        # verify" is not a coherent request, so refuse it outright rather than defining what
        # it would mean.
        print("error: --check and --refetch are mutually exclusive -- --check verifies what "
              "is already committed and never fetches", file=sys.stderr)
        return 1

    part_ids = [args.part_id] if args.part_id else discover_part_ids()
    if not part_ids:
        print(f"error: no {CITED_DIR.relative_to(ROOT)}/*.yml found — run "
              f"src/scan_cited_sections.py first", file=sys.stderr)
        return 1

    bad = False
    for part_id in part_ids:
        print(f"-- {part_id} --")
        if run_part(part_id, args) != 0:
            bad = True
    return 1 if bad else 0


if __name__ == "__main__":
    raise SystemExit(main())
