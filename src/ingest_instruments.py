#!/usr/bin/env python3
"""Fetch each manifest source, snapshot it, and write instruments/<id>.md.

  python3 src/ingest_instruments.py                # ingest everything
  python3 src/ingest_instruments.py --only 2-cfr-200
  python3 src/ingest_instruments.py --refetch      # ignore cached snapshots
  python3 src/ingest_instruments.py --check        # compare to what is committed; write nothing

Runs in no CI workflow: every source needs a live fetch, and a `cfr_part` not already
committed `status: superseded` needs a live `cfr_amended_on()` lookup too (ADR-0001's "current
text" model), so `--check` is not hermetic here the way it is in split_cfr_sections.py. Use it
by hand; src/check_part_supersession.py is the hermetic, CI-wired proof for the one thing this
module got wrong without needing the network to catch it (#77).

TWO PATHS, dispatched on `instrument_kind`, and only one of them is new here.

  cfr_part   eCFR XML. STRUCTURED, and therefore better than PDF for this: sections are
             real elements with an `N` attribute, so heading boundaries are read rather
             than inferred. No page furniture, no line-break repair.
  everything PDF via pypdf, reusing the extractor proven twice already in
  else       oregon-audits/src/ingest_audits.py — running-header detection, page numbers,
             blank collapsing. Copied rather than reimplemented.

WHY `## Full text` IS THE WHOLE DOCUMENT. federal_instrument is in the toolkit's
VERBATIM_REQUIRED set, so corpus-verify-provenance requires every line of that section to
appear IN ORDER in the snapshot at >= 70% coverage. Quoting selected passages would satisfy
that only by accident and would silently drop the rest. For a compliance corpus, dropping
part of a requirement is the worst available failure — so the whole extracted text goes in
and the check is exact rather than approximate.
"""
from __future__ import annotations

import argparse
import gzip
import io
import json
import re
import sys
import time
import urllib.request
import xml.etree.ElementTree as ET
import zipfile
from pathlib import Path

import yaml
from pypdf import PdfReader

sys.path.insert(0, str(Path(__file__).resolve().parent))
from cfr_consolidations import PART_REMOVALS  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
MANIFEST = ROOT / "_meta" / "source-manifest.yml"
SNAPSHOTS = ROOT / "_meta" / "snapshots"
OUT_DIR = ROOT / "instruments"
UA = ("OregonAI-corpus-bot/0.1 (+https://github.com/OregonAI/federal-reference; "
      "civic corpus ingest)")

# IRS publications carry their revision on the cover page and NOT in the URL, and the
# revision is part of the instrument's identity — requirements change between revisions, so
# a citation to one revision must never resolve to another's text.
IRS_REV = re.compile(r"\(\s*Rev\.?\s*(\d{1,2}[-/]\d{4})\s*\)", re.I)

# These four kinds really are constant per kind: every IRS publication comes from the IRS,
# every CJIS policy from the FBI's CJIS Division, every public law and every codified U.S.
# Code section from Congress (OLRC only codifies what Congress enacted). `cfr_part`
# is deliberately NOT in this table — see resolve_issuing_body().
ISSUING_BODY_BY_KIND = {
    "irs_publication": "Internal Revenue Service",
    "fbi_policy": "Federal Bureau of Investigation, CJIS Division",
    "public_law": "United States Congress",
    "usc_section": "United States Congress",
}

# KINDS WHOSE ISSUER IS DATA, NOT A PROPERTY OF THE KIND. `cfr_part` was the original
# member and the reason this distinction exists (2 CFR 200 is OMB's, 28 CFR 35 is DOJ's).
# `agency_guidance` joins it for the same reason and more sharply: it is a deliberately
# broad kind covering security and doctrine instruments from CMS, FNS, SSA, FEMA, CISA,
# GSA and a private standards body, so there is no issuer to key off at all. One generic
# kind with a declared issuer is honest; eight single-member kinds would encode the
# issuer in the taxonomy and still have to be read from the entry.
ISSUER_IS_PER_ENTRY = {"cfr_part", "agency_guidance"}


def resolve_issuing_body(src: dict) -> str:
    """The federal agency that issued this instrument.

    For every OTHER instrument_kind, the issuer is a property of the KIND: an IRS
    publication is always from the IRS. A CFR part is different — Title 2 Part 200 is
    OMB's, but Title 28 Part 35 is DOJ's and Title 42 Part 2 is HHS/SAMHSA's. Keying
    `cfr_part` off the kind (as this used to) stamps whichever part was ingested first onto
    every part ingested after it, which is a false attribution in a corpus whose purpose is
    letting a reader check who said what.

    So for `cfr_part` the issuer is read from the source's OWN manifest entry — data a
    reviewer can see and check at PR time, alongside `citation`, `title`,
    `reproduction_basis` — never inferred from the kind, the URL, or a previous document.

    RAISES rather than defaulting when a cfr_part entry has no declared issuer. A missing
    issuer means the manifest entry is not ready to publish; guessing OMB again (or writing
    an empty string) is exactly the silent default that produced this bug in the first
    place.
    """
    kind = src["instrument_kind"]
    if kind in ISSUER_IS_PER_ENTRY:
        body = src.get("issuing_body")
        if not body:
            raise ValueError(
                f"{src['id']!r} is a {kind} with no issuing_body declared in "
                f"{MANIFEST.name} — the issuing agency is a fact about this specific "
                "instrument and must be stated, not assumed")
        return body
    return ISSUING_BODY_BY_KIND[kind]


def cfr_amended_on(url: str) -> str:
    """The date THIS PART was last amended, from eCFR's per-section version record.

    `amended_on` is half of the pair that makes this corpus's central guardrail work: with
    `as_of` it is what lets a caller tell current text from the text in force when a citing
    rule was written.

    IT MUST BE THE PART'S DATE, NOT THE TITLE'S. This read titles.json and returned
    `latest_amended_on` for the whole of Title 2 -- which covers every part from 1 to 9903,
    so ANY amendment anywhere in the title moved it. 2 CFR 200 was published claiming
    `amended_on: 2026-07-16` when the part's last actual amendment was 2024-10-01, twenty
    months earlier. The part's own snapshot said so plainly ("[89 FR 30136, Apr. 22, 2024,
    as amended at 89 FR 79732, Oct. 1, 2024]") and so did all 29 section documents, which
    take their dates from the per-section record.

    A caller comparing a 2025 Oregon rule against that field was told the requirement
    changed after the rule when it had not -- the exact "wrong answer wearing a right
    answer's clothes" this field exists to prevent.

    RAISES rather than returning None. This used to swallow every exception, so a transient
    DNS or eCFR hiccup silently published the document with `amended_on: null` and exited 0.
    For a cfr_part that field is not optional, and a corpus that cannot date its text should
    fail loudly instead of shipping an undated requirement.
    """
    m = re.search(r"title-(\d+)", url)
    part = re.search(r"part=(\d+)", url)
    if not m or not part:
        raise ValueError(f"cannot read title/part from {url!r}")
    api = (f"https://www.ecfr.gov/api/versioner/v1/versions/title-{m.group(1)}.json"
           f"?part={part.group(1)}")
    req = urllib.request.Request(api, headers={"User-Agent": UA})
    data = json.load(urllib.request.urlopen(req, timeout=60))
    dates = [r.get("amendment_date") for r in
             (data.get("content_versions") or data.get("versions") or [])
             if r.get("amendment_date") and not r.get("removed")]
    if not dates:
        raise RuntimeError(f"eCFR returned no amendment dates for {api}")
    return max(dates)


def record_source_hash(rid: str, raw: bytes, fmt: str, url: str = "") -> str:
    """Record the hash corpus-detect-changes will compare against. Returns a status line.

    PDFs go through `pdftotext`, which is not present in every environment. When it is
    missing this SKIPS rather than writing a hash computed some other way -- a manifest hash
    produced by a different function than the detector uses is worse than an empty one,
    because an empty one is visibly unpopulated while a wrong one looks authoritative and
    reports CHANGED forever.

    THE SAME RULE COVERS `url`.lower().endswith(".zip"). `raw` here is the DECOMPRESSED
    bytes `fetch()` cached (see `_unzip_single_xml`) -- but corpus-detect-changes fetches
    this same URL for itself and hashes exactly what the wire returns, because
    `corpus_toolkit.sources.changes` has no ZIP handling at all: no zip branch, and
    `_format_for` only ever picks a text/xml/json converter. Hashing our unzipped bytes
    here would seed a baseline the detector can never reproduce -- confirmed on a
    synthetic archive: the zip bytes and their single unzipped member hash to two
    different digests -- so this source would report CHANGED on every future run, exit 0,
    forever. Skipping the write is not a gap: ADR-0015 in corpus-toolkit already seeds an
    unrecorded (`sha256: ""`) baseline on the run that first fetches a source and never
    counts an unseeded source as drift, so leaving it empty here hands the detector
    exactly the case it already handles correctly. The underlying gap -- zip-wrapped
    sources are unhashable by the detector as it stands -- is filed as
    OregonAI/corpus-toolkit#199, not fixed here: `changes.py` is a different repo.
    """
    if url.lower().endswith(".zip"):
        return f"sha256 for {rid} left unrecorded: zip-wrapped source (see docstring)"
    from corpus_toolkit.sources.changes import content_hash
    try:
        sha = content_hash(raw, fmt)
    except FileNotFoundError as e:                   # pdftotext absent
        return (f"sha256 for {rid} NOT recorded: {e.filename} unavailable — run "
                f"`python3 src/refresh_source_hashes.py` where poppler is installed")
    return f"recorded sha256 for {rid}" if write_manifest_hash(rid, sha) else ""


def write_manifest_hash(rid: str, sha: str) -> bool:
    """Record a source's content hash back into the manifest. Returns True if it changed.

    WITHOUT THIS THE DRIFT DETECTOR IS A 100% FALSE POSITIVE. corpus-detect-changes compares
    the freshly computed hash against `sha256` in the manifest, which shipped as "" for every
    source -- so all five reported CHANGED on every weekly run, forever. A check that always
    fires tells you nothing, and the only upstream-content guard this corpus has was doing
    exactly that.

    Edited as TEXT, not round-tripped through yaml.safe_dump: the manifest is hand-authored
    and its comments carry the reasoning for every intake decision. Dumping it would silently
    delete all of them.
    """
    lines = MANIFEST.read_text(encoding="utf-8").splitlines(keepends=True)
    out, in_block, changed = [], False, False
    for line in lines:
        stripped = line.strip()
        if stripped.startswith("- id:"):
            in_block = stripped.split("- id:", 1)[1].strip().strip('"\'') == rid
        if in_block and stripped.startswith("sha256:"):
            new = f'{line[:len(line) - len(line.lstrip())]}sha256: "{sha}"\n'
            changed = new != line
            out.append(new)
            in_block = False
            continue
        out.append(line)
    if changed:
        MANIFEST.write_text("".join(out), encoding="utf-8")
    return changed


def _unzip_single_xml(raw: bytes) -> bytes:
    """OLRC's release-point download is a ZIP archive holding one XML file per title
    (`xml_usc20@119-103.zip` -> `usc20.xml`), not raw XML on the wire.

    `fetch()` caches DECOMPRESSED bytes at `dest`, and `dest` for a usc_section source is
    named `<id>.xml` (see main()) -- so what lands on disk must actually be XML, or
    `source_format: xml` would be a claim about the file that is false the moment anyone
    opens it. Raises if the archive holds anything other than exactly one `.xml` member:
    a release-point ZIP with more than one XML file, or none, means this function's
    assumption about OLRC's packaging has changed and guessing which member is the title
    would be exactly the kind of silent substitution this corpus exists to refuse.
    """
    with zipfile.ZipFile(io.BytesIO(raw)) as zf:
        members = [n for n in zf.namelist() if n.lower().endswith(".xml")]
        if len(members) != 1:
            raise ValueError(
                f"expected exactly one .xml member in the release-point archive, found "
                f"{members!r}")
        return zf.read(members[0])


def fetch(url: str, dest: Path, refetch: bool) -> bytes:
    """Fetch `url`, caching the DECOMPRESSED bytes at `dest`.

    eCFR's `/full/<date>/title-N.xml` endpoint started rejecting requests with
    `406 Not Acceptable: This endpoint requires response compression` some time after
    2 CFR 200 was first ingested (its snapshot was already cached, so `fetch()` never
    re-hit the network for it and the break was silent until 34 CFR 300, the first part
    ingested since, needed a real fetch). `urllib` never decompresses on its own even when
    a request declares it can accept a compressed body, so both halves are needed: send
    `Accept-Encoding`, then undo it by hand if the response says it used it.

    OLRC's per-title USLM release point is a SECOND kind of compression, on the wire
    unconditionally rather than only when negotiated: the URL itself ends `.zip`
    (`releasepoints/us/pl/119/103/xml_usc20@119-103.zip`), and what is served is a ZIP
    archive, not XML with a Content-Encoding header. `_unzip_single_xml` undoes that
    unconditionally when the URL says so, so the cached bytes at `dest` are the XML itself.
    """
    if dest.is_file() and not refetch:
        return dest.read_bytes()
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Encoding": "gzip"})
    resp = urllib.request.urlopen(req, timeout=300)
    raw = resp.read()
    if resp.headers.get("Content-Encoding", "").lower() == "gzip":
        raw = gzip.decompress(raw)
    if url.lower().endswith(".zip"):
        raw = _unzip_single_xml(raw)
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_bytes(raw)
    return raw


# ---------------------------------------------------------------- eCFR XML

def _flatten(el) -> str:
    return " ".join("".join(el.itertext()).split())


def guard_headings(text: str) -> str:
    r"""Never let SOURCE text start a line with `## `.

    corpus_toolkit.repo.FULLTEXT_RE reads the body as `^## Full text\s*$(.*?)(?=^## |\Z)`,
    so any line beginning `## ` at column zero ends the document there. A leading space stops
    the match and normalize_ws erases it before any comparison, so nothing downstream sees it.

    THIS WAS CLAIMED AND NOT DONE. extract_pdf applied it with a comment reading "Same `## `
    guard as the CFR path" -- but the CFR path had no guard at all, which is why
    split_cfr_sections.py had to carry its own. The failure is silent AND survives CI on a
    document this size: coverage thresholds are fail 0.70 / warn 0.90, so a stray `## ` in
    the last tenth of 633,000 characters truncates the tail and still scores above 90%, and
    the in-order line check passes because a truncated document's lines are all still there
    and still in order.
    """
    return re.sub(r"^(#{1,6}\s)", r" \1", text, flags=re.M)


def extract_cfr(raw: bytes) -> tuple[str, dict]:
    """eCFR part XML -> markdown, one `###` heading per section and appendix.

    Sections come from `DIV8[@TYPE='SECTION']`, whose `N` attribute is the section number.
    Appendices are kept: 2 CFR 200 has 12 of them and they carry substantive requirements,
    not just forms.
    """
    root = ET.fromstring(raw)
    out, n_sec, n_app, n_sub = [], 0, 0, 0
    for el in root.iter():
        kind = el.get("TYPE")
        # THE PART'S OWN AUTHORITY AND SOURCE NOTE. Visiting only SECTION and APPENDIX
        # dropped 992 characters that never reached the document, and the AUTHORITY block is
        # the item that matters: it is the statutory basis for the whole part, in a corpus
        # whose entire purpose is telling a reader what a requirement rests on. A federal
        # instrument that cannot state its own authority is missing the field this corpus
        # exists to supply.
        if el.tag in ("AUTH", "SOURCE"):
            t = guard_headings(_flatten(el))
            if t:
                out.append(t)
                out.append("")
            continue
        # Subpart headings are the part's structure. Without them the document is a flat run
        # of 200 sections and a reader cannot tell that § 200.400 opens Cost Principles.
        # `###` for the same FULLTEXT_RE reason as sections — see the comment below.
        if kind in ("PART", "SUBPART"):
            head_el = el.find("HEAD")
            if head_el is not None:
                out.append(f"### {_flatten(head_el)}")
                out.append("")
                n_sub += kind == "SUBPART"
            continue
        if kind not in ("SECTION", "APPENDIX"):
            continue
        head_el = el.find("HEAD")
        head = _flatten(head_el) if head_el is not None else (el.get("N") or "")
        # THREE hashes, not two, and this is load-bearing rather than cosmetic.
        #
        # corpus_toolkit.repo.FULLTEXT_RE reads the body as
        #     ^## Full text\s*$(.*?)(?=^## |\Z)
        # so ANY line starting `## ` at column zero ends the section. Emitting section
        # headings as `## ` truncated this document to 1 character of 632,927 while looking
        # perfectly well-formed -- caught only as "coverage 0%". `### ` does not match that
        # lookahead (third character is `#`, not a space), so sections stay real markdown
        # headings and remain addressable, without terminating the section they live in.
        #
        # oregon-audits hit the same regex from the other direction: there the offending
        # `## ` came from the SOURCE text, and the fix was a leading space. Here we control
        # the heading, so the heading level is the right lever.
        out.append(f"### {head}")
        for child in el:
            if child is head_el:
                continue
            t = guard_headings(_flatten(child))
            if t:
                out.append(t)
        out.append("")
        n_sec += kind == "SECTION"
        n_app += kind == "APPENDIX"
    text = re.sub(r"\n{3,}", "\n\n", "\n".join(out)).strip()
    return text, {"sections": n_sec, "appendices": n_app, "subparts": n_sub}


# ---------------------------------------------------------------- USLM (U.S. Code, ADR-0006)

USLM_NS = "{http://xml.house.gov/schemas/uslm/1.0}"


def _uslm_find_section(root, title: str, sec: str):
    """The `<section>` element for `{title} USC {sec}`, by its USLM `identifier`.

    Walks the whole parsed title tree rather than reaching for it with XPath: ElementTree's
    supported subset cannot select on an attribute VALUE for a namespaced tag in one
    expression, and a linear scan of a tree already parsed in memory is cheap next to the
    network fetch that produced it.
    """
    ident = f"/us/usc/t{title}/s{sec}"
    for el in root.iter(f"{USLM_NS}section"):
        if el.get("identifier") == ident:
            return el
    return None


def usc_currency(root) -> str:
    """OLRC's own currency stamp, transcribed and reformatted to the wording ADR-0006 names.

    The title's `<meta><docPublicationName>` carries the release point as
    `Online@119-103` — Congress 119, law 103. OLRC's own download page states the identical
    fact in prose: *"All files are current through Public Law 119-103."* That is the exact
    phrase ADR-0006 asks this field to carry ("current through Pub. L. N"), so the release
    point is reformatted into it rather than left in OLRC's internal `Online@` shorthand,
    which no reader outside OLRC's own tooling would recognize as a currency statement.

    Raises rather than guessing when the tag is missing or does not parse — a `currency`
    this corpus cannot read from the source is not one it should publish.
    """
    el = root.find(f"{USLM_NS}meta/{USLM_NS}docPublicationName")
    text = (el.text or "").strip() if el is not None else ""
    m = re.match(r"Online@(\d+)-(\d+)$", text)
    if not m:
        raise ValueError(f"cannot read a release point from docPublicationName={text!r}")
    return f"current through Pub. L. {m.group(1)}-{m.group(2)}"


def usc_amended_on(section_el) -> str:
    """The most recent amendment date for THIS section, from its own `<sourceCredit>`.

    Every amending Pub. L. in a USLM sourceCredit carries a machine-readable
    `<date date="YYYY-MM-DD">` beside the citation prose — the section's amendment history
    is read structurally, the same way `cfr_amended_on` reads eCFR's version API rather than
    parsing a date out of running text. Raises when a section carries no sourceCredit or no
    dated amendment: an undated `amended_on` is not a fact this corpus can state.
    """
    credit = section_el.find(f"{USLM_NS}sourceCredit")
    if credit is None:
        raise ValueError("section has no <sourceCredit>; cannot state amended_on")
    dates = [d.get("date") for d in credit.iter(f"{USLM_NS}date") if d.get("date")]
    if not dates:
        raise ValueError("<sourceCredit> carries no dated amendment; cannot state amended_on")
    return max(dates)


# Structural elements that carry their OWN `<num>`/`<heading>` and therefore need to
# recurse rather than be flattened whole. Everything else that shows up as a child of one
# of these (`content`, `chapeau`, `continuation`, `sourceCredit`, a note's own `<p>`) has no
# num/heading of its own, so flattening IT whole in one `_flatten()` call cannot fuse it
# with a sibling's text -- the failure mode below is specific to elements that DO carry a
# label, because USLM keeps that label and the body as siblings with no whitespace between
# them on the wire.
_USLM_CONTAINERS = {f"{USLM_NS}{t}" for t in
                    ("subsection", "paragraph", "subparagraph", "clause", "subclause",
                     "note", "notes")}


def _emit_uslm_child(child, out: list[str]) -> None:
    """One child of a USLM structural element -> one or more lines appended to `out`."""
    if child.tag in _USLM_CONTAINERS:
        _render_uslm(child, out)
    else:
        t = guard_headings(_flatten(child))
        if t:
            out.append(t)


def _render_uslm(el, out: list[str]) -> None:
    """Append `el`'s own num+heading as one line, then one line per child in turn.

    `_flatten()` joins `itertext()` over a whole subtree with no separator inserted at
    element boundaries, and USLM keeps `<num>`, `<heading>`, and the body (`<content>`,
    nested `<paragraph>`s, ...) as SIBLING elements with no whitespace between them in the
    wire XML. Calling `_flatten()` on a whole `<subsection>` therefore ran a heading's last
    word into the next element's first word with nothing between them -- "...regulations"
    immediately followed by "Not later than 240 days..." became "regulationsNot..." -- and
    collapsed every (1)/(A)/(i) paragraph in the subsection onto one line, tokens that exist
    nowhere in the pinned source. Recursing per element instead, the way `extract_cfr` walks
    `HEAD` and each `P` rather than the whole `DIV8`, keeps each fact on its own line and
    never runs two source strings together that the source itself kept apart.
    """
    num_el = el.find(f"{USLM_NS}num")
    heading_el = el.find(f"{USLM_NS}heading")
    num_text = _flatten(num_el) if num_el is not None else ""
    heading_text = _flatten(heading_el) if heading_el is not None else ""
    label = f"{num_text} {heading_text}".strip()
    if label:
        out.append(guard_headings(label))
    for child in el:
        if child in (num_el, heading_el):
            continue
        _emit_uslm_child(child, out)


def extract_usc(root, title: str, sec: str):
    """Parsed USLM title tree -> (markdown, stats, the `<section>` element) for ONE cited
    section, current text per ADR-0001.

    Only the CITED section is extracted, never the title — ADR-0006 holds sections, on
    demand, and never holds a title as a document — so the committed document and its own
    provenance stay small even though the fetched title XML (tens of megabytes) is not.
    `guard_headings` runs over every emitted line for the same `FULLTEXT_RE` reason
    `extract_cfr` carries it: any source line starting `## ` at column zero would silently
    truncate the document there.

    KEEPS the source credit and the statutory notes, not the operative text alone. For a
    codified section those are part of what OLRC publishes AS the section — the amendment
    history IS the provenance a compliance reader needs — and dropping part of what a
    citing rule relies on is this corpus's worst failure mode.

    Takes an already-parsed `root`, not raw bytes, so a caller needing BOTH the text and a
    fact read from elsewhere in the same tree (the title's currency stamp, this section's
    own amendment date) parses the multi-megabyte document once rather than once per fact.
    RETURNS the located `<section>` element too, alongside the text and stats, for that
    same reason one level further: `main()` needs it again for `usc_amended_on()`, and this
    function has already walked the whole tree to find it once. A second call to
    `_uslm_find_section` for the same id would be a second full linear scan of that tree for
    an element the caller already has in hand.
    """
    section_el = _uslm_find_section(root, title, sec)
    if section_el is None:
        raise ValueError(f"no <section> for {title} USC {sec} in the raw USLM")

    heading_el = section_el.find(f"{USLM_NS}heading")
    num_el = section_el.find(f"{USLM_NS}num")
    heading = _flatten(heading_el) if heading_el is not None else ""
    out = [f"### § {sec} {heading}".rstrip()]
    n_sub = 0
    for child in section_el:
        if child in (heading_el, num_el):
            continue
        if child.tag == f"{USLM_NS}subsection":
            n_sub += 1
        _emit_uslm_child(child, out)
    text = re.sub(r"\n{3,}", "\n\n", "\n".join(out)).strip()
    return text, {"subsections": n_sub}, section_el


# ---------------------------------------------------------------- PDF

# How many non-blank lines at each end of a page count as "where furniture lives". Used
# both to LEARN furniture and to REMOVE it -- the two must agree, or the extractor deletes
# text in places it never looked for a pattern.
FURNITURE_BAND = 3


def page_furniture(pages: list[list[str]]) -> tuple[set[str], set[str]]:
    """Lines repeated at the top/bottom of most pages: letterhead, banners, footers."""
    if len(pages) < 4:
        return set(), set()
    top, bot = {}, {}
    for p in pages:
        for l in [x.strip() for x in p[:FURNITURE_BAND] if x.strip()]:
            top[l] = top.get(l, 0) + 1
        for l in [x.strip() for x in p[-FURNITURE_BAND:] if x.strip()]:
            bot[l] = bot.get(l, 0) + 1
    half = len(pages) / 2
    return ({l for l, n in top.items() if n > half},
            {l for l, n in bot.items() if n > half})


def is_page_number(line: str, npages: int) -> bool:
    s = line.strip()
    return bool(re.fullmatch(r"(page\s+)?\d{1,4}(\s*(of|/)\s*\d{1,4})?", s, re.I)) and \
        len(s) <= 18 and npages > 1


def extract_pdf(path: Path) -> tuple[str, dict]:
    """PDF -> text, stripping page furniture ONLY where page furniture can occur.

    THE BAND IS THE WHOLE POINT. Both filters used to run against every line on every page,
    so any body line that happened to be a bare number was deleted wherever it appeared.
    That is not hypothetical -- it removed real text from a shipped document:

        CJIS SP 6.1  "... FIPS PUB 200; March" + "2006"   -> the year deleted
        CJIS SP 6.1  "... NIST Special Publication 800-" + "124" -> the number deleted

    Both are wrapped entries in the incorporated-by-reference appendix, where the standard's
    identifier lands on its own line. Silently truncating the identifier of an incorporated
    standard is precisely the wrong-document failure a compliance corpus cannot afford, and
    nothing caught it -- see check_extraction.py for why provenance structurally could not.

    page_furniture() only ever LEARNS from the first and last three non-blank lines, so
    applying what it learned outside that band was never justified: a running header that
    also occurs as body prose would be erased document-wide.
    """
    reader = PdfReader(str(path))
    pages = [(p.extract_text() or "").splitlines() for p in reader.pages]
    head, foot = page_furniture(pages)
    out = []
    for lines in pages:
        stripped = [l.strip() for l in lines]
        filled = [i for i, s in enumerate(stripped) if s]
        # Same 3-line band page_furniture() learns from, measured in NON-BLANK lines so a
        # page with leading blank lines does not shift the band off the header.
        band = set(filled[:FURNITURE_BAND]) | set(filled[-FURNITURE_BAND:])
        for i, s in enumerate(stripped):
            if not s:
                continue
            if i in band and (s in head or s in foot or is_page_number(s, len(pages))):
                continue
            out.append(s)
    text = re.sub(r"\n{3,}", "\n\n", "\n".join(out)).strip()
    text = guard_headings(text)
    return text, {"pages": len(reader.pages)}


# ---------------------------------------------------------------- document

def cited_section_ids(part_id: str) -> list[str]:
    """Document ids for the sections split out of `part_id` (e.g. `2-cfr-200`), in citation
    order.

    Read from _meta/cited-sections/<part_id>.yml -- the same committed per-part list
    split_cfr_sections.py works from -- so the part's edges and the section documents cannot
    disagree about which sections exist.

    #34: this used to read one hardcoded file (_meta/cited-sections.yml) and prefix every id
    with the literal "2-cfr-200." -- correct for the one part that existed, and silently
    wrong for any other: a second part's cited-sections file lived at a path this function
    never looked at, so ITS part document would publish `relationships: {}` -- indistinguishable
    from a part Oregon genuinely cites nothing from, for the wrong reason. Absence of a file
    for `part_id` still returns [] -- a part not yet run through src/scan_cited_sections.py
    correctly has no known cited sections yet, which is not an error.
    """
    path = ROOT / "_meta" / "cited-sections" / f"{part_id}.yml"
    if not path.is_file():
        return []
    doc = yaml.safe_load(path.read_text()) or {}
    return [f"{part_id}.{e['section'].split('.', 1)[1]}"
            for key in ("current", "removed") for e in (doc.get(key) or [])]


# Which intake SIGNAL a cited-sections entry's `cited_in` tag names, for prose that reports a
# measured citation count without conflating the signals CONTEXT.md's "three intake signals"
# entry says must never be conflated ("Writing 'most-cited' without naming the signal is how
# that conflation happens"). `audits` is oregon-audits' body-text citations -- the same word
# the ORIGINAL hand-written 45 CFR 75 note used ("Oregon's single audits cite Part 75").
# `erf` is executive-regulatory-frameworks' -- Oregon's own rules, not a second audits count.
_SIGNAL_LABELS = {"audits": "Oregon's single audits", "erf": "Oregon rules"}


def citation_signal_counts(part_id: str) -> dict[str, int]:
    """{signal: total citations}, summed from _meta/cited-sections/<part_id>.yml's own
    per-section `citations` counts, grouped by `cited_in` -- the same committed file
    `cited_section_ids()` just above already reads, so a part's edges and its own citation
    count cannot disagree about which committed source they come from.

    #77 review (P3): the "27 vs 28" discrepancy in 45 CFR 75's hand-written note was resolvable
    from this exact file, which the ingester already reads -- CHANGELOG's original claim that
    "no live source in this ingester computes a part-level citation count" was true only in the
    narrowest sense. Both `current` AND `removed` entries count: a removed section cited by an
    audit conducted while it was in force is a real, measured citation, not one that stops
    counting when the section does -- the whole reason 45 CFR 75's sections are held as
    `superseded` documents rather than dropped.

    Returns {} for a part with no committed cited-sections file (never scanned yet) -- absence
    of data, not a zero worth publishing as a fact.
    """
    path = ROOT / "_meta" / "cited-sections" / f"{part_id}.yml"
    if not path.is_file():
        return {}
    doc = yaml.safe_load(path.read_text()) or {}
    counts: dict[str, int] = {}
    for key in ("current", "removed"):
        for e in (doc.get(key) or []):
            for sig in (e.get("cited_in") or []):
                counts[sig] = counts.get(sig, 0) + int(e.get("citations") or 0)
    return counts


def _default_curator_note(rid: str) -> str:
    """A plain, fully-DERIVED "why we hold it" sentence for a part superseded for the FIRST
    time -- used only when `existing_curator_note()` finds nothing already committed to
    preserve (see that function's docstring for why the two cases are different).

    Built from `citation_signal_counts()` alone: a total and a per-signal breakdown, never an
    unsignaled aggregate and never an adjective ("heavily cited", "frequently referenced").
    AGENTS.md: "Prefer counts and reproductions over adjectives." This is deliberately less
    specific than a human curator could write for a real case -- it does not know WHY the
    counts matter (45 CFR 75's own preserved note adds "against awards made before that
    date", the ADR-0001/ADR-0003 legal rationale, which is not a fact this function can
    derive from the citation counts alone) -- but every word in it is something the corpus
    can prove today, which is the bar AGENTS.md's hard rule 1 sets.
    """
    counts = citation_signal_counts(rid)
    if not counts:
        return "It is held because Oregon material cites sections within it."
    total = sum(counts.values())
    n_secs = len(cited_section_ids(rid))
    breakdown = ", ".join(
        f"{n} from {_SIGNAL_LABELS.get(sig, sig)}"
        for sig, n in sorted(counts.items(), key=lambda kv: -kv[1]))
    return (f"It is held because Oregon material cites sections within it {total} "
            f"time{'s' if total != 1 else ''} across the {n_secs} section"
            f"{'s' if n_secs != 1 else ''} held here — {breakdown}.")


# The generator-owned trailer's fixed boundary phrase. existing_curator_note() splits on it
# to recover just the CURATED leading clause a human (or _default_curator_note()) wrote,
# stripping the generator-owned caveats build() always appends fresh after it -- see both
# docstrings for why the caveats (in particular the successor-naming "drop-in" clause) must
# never be part of what gets preserved verbatim.
_CURATOR_NOTE_BOUNDARY = "**The current definition may differ.**"


def existing_curator_note(doc_path: Path) -> str | None:
    """The curator's "why we hold it" sentence already committed for a superseded part's
    whole-part note, read back from `doc_path` -- the CURATED half of that note AGENTS.md
    hard rule 2 confines to curator content, as opposed to the mechanical removal-date/
    successor half build() derives fresh every run. Returns None when nothing is committed
    yet, so build() can fall back to `_default_curator_note()` instead of fabricating a "why
    we hold it" story for a part superseded for the first time.

    #77 review (P1/P2/P3): the original fix rendered THIS half from scratch too, and in doing
    so (a) dropped the ONE thing this ingester cannot derive -- 45 CFR 75's measured "28 audit
    citations" figure -- replacing it with unmeasured, unsignaled prose ("Oregon material
    cites sections... for periods when they were in force") that CONTEXT.md's own "three
    intake signals" entry names as exactly the conflation to avoid, and (b) dropped the
    ADR-0001/ADR-0003 legal rationale clause ("against awards made before that date") that
    explains why a superseded part is held at all. Same "read the file this run is about to
    overwrite" shape `_recorded_retrieved()` and `existing_supersession()` already use, one
    function up and two functions up respectively -- a curator's sentence accepted into the
    committed document at PR time has nowhere else to live, the same argument
    `existing_supersession()`'s own docstring makes for `status`/`superseded_by`/`amended_on`.

    Parses the whole-part blockquote generically (lines starting with `>`, split on the first
    lone `>` line into paragraphs) rather than matching build()'s current exact wording, so a
    hand-wrapped original (four ~90-char `> ` lines) and this generator's own single-line
    output both read back the same logical sentence. Returns None on anything that does not
    parse as at least two blockquote paragraphs -- a document with no whole-part note yet is
    the same "nothing to preserve" case as a document that does not exist, not a malformed-
    document case (see existing_supersession()'s docstring for why THAT one fails closed
    instead: a missing note here just means _default_curator_note() runs, which is safe by
    construction, whereas a missing status/superseded_by there means republishing removed law
    as current, which is not).
    """
    if not doc_path.is_file():
        return None
    block_lines: list[str] = []
    for line in doc_path.read_text(encoding="utf-8").splitlines():
        if line.startswith(">"):
            block_lines.append(line)
        elif block_lines:
            break
    paragraphs: list[list[str]] = [[]]
    for line in block_lines:
        if line.strip() == ">":
            paragraphs.append([])
        else:
            paragraphs[-1].append(line)
    if len(paragraphs) < 2:
        return None
    curator_lines = [l[1:].lstrip() for para in paragraphs[1:] for l in para]
    text = " ".join(l for l in (s.strip() for s in curator_lines) if l)
    if not text:
        return None
    return text.split(_CURATOR_NOTE_BOUNDARY, 1)[0].strip() or None


def existing_relationships(doc_path: Path) -> dict:
    """Curator-added relationship edges already committed, read back so a re-ingest does not
    erase them -- the same "read the file this run is about to overwrite" shape
    `existing_curator_note()` and `existing_supersession()` use one function up and two
    functions up respectively.

    THIS CORPUS'S GRAPH IS "hand-authored or written by its own ingester" (build_graph.py's
    own module docstring). `related`/`superseded_by` are mechanically derived per kind below
    (cited_section_ids() for an in-force cfr_part, `[superseded_by]` for a superseded one) --
    but a CROSS-INSTRUMENT edge this ingester has no way to derive on its own (34 CFR 99
    implementing 20 USC 1232g; 42 CFR 2 being the stricter-than comparison to 45 CFR 160/164)
    is exactly the curator content AGENTS.md hard rule 2 anticipates, and it has nowhere else
    to live: these are `federal_instrument` documents, `## Full text` is exact-match verbatim
    (check_extraction.py), and a doc_type in VERBATIM_REQUIRED has no `## Cross-references`
    body section to hold it either (that section's own template note licenses only in-repo
    RELATIVE-PATH links for other doc_types; this corpus's frontmatter `relationships` block
    is what a sibling-relationship graph actually reads). So the edge is added directly to
    frontmatter, once, and preserved here across every later regeneration.

    Returns {} for a document that does not exist yet or carries no `relationships` block --
    the same "nothing to preserve" case `existing_curator_note()` returns None for.
    """
    if not doc_path.is_file():
        return {}
    fm = yaml.safe_load(doc_path.read_text(encoding="utf-8").split("---", 2)[1]) or {}
    return fm.get("relationships") or {}


def merge_relationships(auto: dict, existing: dict) -> dict:
    """Union `auto` (this run's mechanically DERIVED edges) with `existing` (whatever was
    already committed, per `existing_relationships()`), per REL_KEY, deduped and order-
    preserving (auto's own targets first, so `related`'s own split-section ids stay in
    `cited_section_ids()`'s order when nothing curated has been added yet).

    EVERY KEY IN `auto` IS KEPT, even an empty list -- a cfr_part with zero cited sections
    still publishes `relationships: {related: []}` (the #34 fix: distinguishing a real "zero
    sections cited" part from one whose relationships block was never written at all). A key
    present only in `existing` -- `implements`/`implemented_by` today, since neither is ever
    auto-derived -- is added only if it still has targets. A key BOTH sides declare --
    `related`, for a cfr_part that has both its own split sections AND a curated comparison
    edge -- unions rather than one replacing the other, so re-ingesting 42 CFR 2 to pick up a
    new split section does not silently drop its hand-wired edge to 45 CFR 160/164, or vice
    versa.
    """
    merged = dict(auto)
    for key, vals in existing.items():
        combined = list(dict.fromkeys([*(merged.get(key) or []), *(vals or [])]))
        if combined:
            merged[key] = combined
    return merged


def doc_id(src: dict, version: str | None) -> str:
    """The document id, with the version in it when the version IS the identity.

    CJIS already worked this way (`cjis-sp-6-1`), and the asymmetry cost us: IRS shipped as
    `irs-pub-1075`, so a sibling deriving an id from `IRS Pub 1075 (Rev. 09-2016)` produced
    an EXACT HIT on the 11-2021 document. Sibling resolution is exact-id lookup against an
    index of [title, doc_type, path] -- no version field -- so the id is the only place a
    version can live where a sibling can see it. federal-reference refused that citation
    while oregon-audits and ERF answered it.

    The snapshot keeps the manifest id (`snapshot_id`), so files on disk do not churn when a
    new revision is ingested alongside the old one.
    """
    if src["instrument_kind"] == "irs_publication" and version:
        return f"{src['id']}-{version}"
    return src["id"]


# The eCFR point-in-time API pins the date IN THE URL. That date, not today's, is what the
# text is as of.
CFR_POINT_IN_TIME = re.compile(r"/full/(\d{4}-\d{2}-\d{2})/")


def _recorded_retrieved(doc_path: Path) -> str | None:
    """The `retrieved` already published for this document, if any."""
    if not doc_path.is_file():
        return None
    try:
        fm = yaml.safe_load(doc_path.read_text(encoding="utf-8").split("---")[1])
    except (IndexError, yaml.YAMLError):
        return None
    value = (fm or {}).get("retrieved")
    return str(value) if value else None


def existing_supersession(doc_path: Path) -> tuple[str, str | None, str | None]:
    """(status, superseded_by, amended_on) already committed at `doc_path`, or
    ("current", None, None) when nothing is committed there yet.

    #77: `build()` used to hardcode `status: "current"` and `superseded_by: None`
    unconditionally, so re-running this ingester over a WHOLLY SUPERSEDED part (45 CFR 75,
    removed from the CFR in its entirety 2025-10-01, hand-published superseded in dcd0d41)
    would republish it as current law on the next run.

    Mirrors split_cfr_sections.part_facts()'s reading of these same three fields from a
    part document's own frontmatter -- the model #78 built for the sibling problem in the
    SECTION splitter, and the one this fix is told to match rather than invent a second one.
    Not the SAME function: part_facts() requires the file to already exist (it only ever
    runs AFTER this module has ingested the part at least once) and also reads `as_of` and
    `retrieved`, which the caller here already has from source_dates(). It also cannot be
    imported from split_cfr_sections.py without that module importing back from this one
    (`from ingest_instruments import _flatten, fetch, resolve_issuing_body`) -- a real
    import cycle, not a style choice, so this is a second reader of the same three fields
    rather than one shared function. `_meta/source-manifest.yml` is not the alternative
    either: it is hand-authored on purpose (ADR-0005), and a field there would be a THIRD
    copy of a fact the document already carries.

    Reading the very file this ingester is about to overwrite sounds circular until you
    notice `_recorded_retrieved()`, two functions up, already does exactly this for
    `retrieved`, for the same reason: a fact a human accepted into the committed document at
    PR time has nowhere else to live.

    FAILS CLOSED on a document that EXISTS but cannot be read, unlike a document that does
    not exist at all. Those are different facts and used to return the same tuple: a missing
    file legitimately has never been ingested (there is nothing to be wrong about, so
    "current" is simply the right default for the very first ingest), but a file that IS
    there and fails to parse (no `---` delimiter, invalid YAML, or frontmatter that parsed to
    something other than a mapping) is a part document this ingester cannot read -- and
    "cannot read" is not evidence of "current". `part_facts()` (this function's own model,
    named above) does not tolerate that case either: it lets the exception propagate rather
    than defaulting. #77's review (finding S5) found this function doing the opposite of its
    own model, in the direction of the bug it exists to prevent: a bad merge that mangles 45
    CFR 75's frontmatter used to make this return ("current", None, None) exactly as if the
    part had never been superseded at all, so `main()` would go on to call the live
    `cfr_amended_on()` and republish removed federal law as current text -- reached THROUGH
    the function #77 wrote to stop it. Raising here instead means main()'s per-source
    `except Exception` reports a loud FAILED for that one source and writes nothing, rather
    than silently treating a document it could not read as one that needed no protecting.
    """
    if not doc_path.is_file():
        return "current", None, None
    text = doc_path.read_text(encoding="utf-8")
    try:
        fm = yaml.safe_load(text.split("---")[1])
    except IndexError:
        raise ValueError(
            f"{doc_path} exists but has no '---' frontmatter delimiter to read "
            "status/superseded_by/amended_on from -- refusing to treat an unreadable part "
            "document as though it were current (see this function's own docstring, #77 "
            "review finding S5)") from None
    except yaml.YAMLError as e:
        raise ValueError(
            f"{doc_path} exists but its frontmatter does not parse as YAML ({e}) -- same "
            "refusal as the missing-delimiter case above") from e
    if not isinstance(fm, dict):
        raise ValueError(
            f"{doc_path}'s frontmatter parsed but is not a mapping "
            f"({type(fm).__name__}) -- same refusal as the two cases above")
    return (str(fm.get("status") or "current"),
            (str(fm["superseded_by"]) if fm.get("superseded_by") else None),
            (str(fm["amended_on"]) if fm.get("amended_on") else None))


def _id_to_citation(doc_id_: str) -> str:
    """"2-cfr-200" -> "2 CFR 200", for naming a successor part in prose. Returns the id
    unchanged if it is not a bare `<title>-cfr-<part>` id -- a successor need not be a CFR
    part at all, and guessing a citation shape for something that is not one would be
    exactly the kind of invented fact AGENTS.md's anti-fabrication rules forbid."""
    m = re.match(r"^(\d+)-cfr-(\d+)$", doc_id_)
    return f"{m.group(1)} CFR {m.group(2)}" if m else doc_id_


def source_dates(src: dict, snap: Path, fresh: bool, doc_path: Path) -> tuple[str, str]:
    """(as_of, retrieved) — from the SOURCE, never from the wall clock.

    Both fields used to be `time.strftime` at every run, which made two false claims.

    `retrieved` is the field a reviewer uses to decide whether a snapshot is stale, and
    stamping it on a cached run moved it FORWARD every time the ingester ran — so the older
    a snapshot got, the fresher it claimed to be. It now advances only when bytes were
    actually fetched; otherwise the published date is carried forward, falling back to the
    snapshot's mtime for a document that does not exist yet.

    `as_of` is the date the TEXT is as of, which for eCFR is pinned in the URL itself
    (`/full/2026-07-29/`) — the document claimed 2026-07-30 while its own `source_url` said
    otherwise. For the PDFs there is no versioned URL: the file at that address is whatever
    is there today, so the date we pulled it is genuinely the best statement of what the
    text is as of, and as_of tracks retrieved rather than inventing precision.
    """
    if fresh:
        retrieved = time.strftime("%Y-%m-%d")
    else:
        retrieved = (_recorded_retrieved(doc_path)
                     or time.strftime("%Y-%m-%d", time.localtime(snap.stat().st_mtime)))
    pinned = CFR_POINT_IN_TIME.search(src["url"])
    return (pinned.group(1) if pinned else retrieved), retrieved


def build(src: dict, text: str, sha: str, stats: dict, version: str | None,
          as_of: str, retrieved: str, status: str = "current",
          superseded_by: str | None = None, curator_note: str | None = None,
          existing_rel: dict | None = None) -> str:
    """`status`/`superseded_by` default to the values every part document had before #77 --
    a brand-new part, or one no caller has told this function is superseded, is current. The
    caller (main()) is what actually derives them per-part via `existing_supersession()`;
    check_section_split.py's two direct `build()` calls exercise fixtures that are neither,
    so they keep passing and keep getting "current" documents, unchanged.

    `existing_rel`, from `existing_relationships()`, is any curator-added cross-instrument
    edge already committed (see that function's own docstring) -- unioned with whatever this
    run derives mechanically via `merge_relationships()`, never replacing it. None (the
    check_section_split.py fixtures' default) is treated as {}, same as a document that does
    not exist yet.

    `curator_note`, from `existing_curator_note()`, is the CURATED half of a superseded
    whole-part note ("why we hold it") -- see that function's docstring (#77 review, P1/P2/
    P3). None when nothing is committed yet; `_default_curator_note()` covers that case
    below, inline, rather than being threaded as a second optional argument here.
    """
    rid = doc_id(src, version)
    superseded = status == "superseded"
    if superseded and not src.get("amended_on"):
        # #77 review (S2): without this, a superseded part with no recorded `amended_on`
        # (an incomplete edit -- `status: superseded` set by hand without also setting the
        # date -- or a synthetic caller that forgets it) built `"(SUPERSEDED None)"` nowhere
        # in the title at all (the title marker's own guard is `superseded and
        # src.get("amended_on")`, so it silently OMITS the marker instead) while the body
        # below fabricated "**removed from the CFR in its entirety on None**" -- a federal-
        # law document stating a fact that does not exist, AGENTS.md hard rule 1, and losing
        # the one mechanism (:888 above) a sibling corpus's [title, doc_type, path] lookup
        # depends on to see the supersession at all. `amended_on` is not optional metadata
        # for a superseded part; it is the removal date the rest of this function is built
        # around, so a superseded part without one is refused rather than published broken.
        raise ValueError(
            f"{rid!r} is status='superseded' but has no amended_on -- the removal date is "
            "load-bearing (the title marker and the body's removal sentence both need it) "
            "and must not be published as a fabricated 'None'")
    # See merge_relationships()'s own docstring for what "auto" means per kind/status, and
    # existing_relationships()'s for why a curator-added cross-instrument edge (read into
    # `existing_rel` by the caller, from whatever is already committed) is unioned in rather
    # than derived here.
    _auto_rel = ({"related": [superseded_by] if superseded_by else []}
                 if superseded and src["instrument_kind"] == "cfr_part" else
                 {"related": cited_section_ids(rid)}
                 if src["instrument_kind"] == "cfr_part" else {})
    _rel = merge_relationships(_auto_rel, existing_rel or {})
    fm = {
        "schema_version": 1,
        "corpus": "federal-reference",
        "jurisdiction": "us",
        "id": rid,
        # THE TITLE CARRIES THE SUPERSESSION, same reasoning as split_cfr_sections.build():
        # a sibling corpus resolving through corpus-index.json's [title, doc_type, path] rows
        # sees only the title, and `status: superseded` in frontmatter is invisible there.
        "title": (f"{src['title']} (SUPERSEDED {src.get('amended_on')})"
                  if superseded and src.get("amended_on") else src["title"]),
        "doc_type": "federal_instrument",
        "citation": (f"{src['citation']} (Rev. {version})"
                     if src["instrument_kind"] == "irs_publication" and version
                     else src["citation"]),
        "authority_level": "federal",
        "issuing_body": resolve_issuing_body(src),
        "instrument_kind": src["instrument_kind"],
        "version": version,
        "as_of": as_of,
        "amended_on": src.get("amended_on"),
        # ADR-0006's deliberate exception to *version is identity*: OLRC's own release-point
        # stamp, reformatted into the "current through Pub. L. N" wording ADR-0006 names --
        # NOT verbatim; see usc_currency()'s own docstring for what it is transcribed FROM
        # and reformatted INTO. A U.S.C. section has no
        # siblings to disambiguate by a version in the id — only a history — so this rides
        # as a field instead. Present ONLY on usc_section; every other kind leaves it unset
        # rather than publishing a `currency: null` that means nothing for a CFR part.
        **({"currency": src["currency"]} if src["instrument_kind"] == "usc_section" else {}),
        "reproduction_basis": " ".join(str(src["reproduction_basis"]).split()),
        "superseded_by": superseded_by,
        # Carried into the DOCUMENT, not left in the manifest. src/citation_schemes.py names
        # these when it refuses a citation to a version we do not hold ("Oregon cites 5.6,
        # 5.9.4 and 6.0, none of which is held") -- and a refusal that cannot say what is
        # missing is much weaker than one that can.
        **({"known_cited_versions_not_held":
            [str(v) for v in src["known_cited_versions_not_held"]]}
           if src.get("known_cited_versions_not_held") else {}),
        "source_url": src["url"],
        "source_format": src["format"],
        # Snapshot files stay keyed by the MANIFEST id even when the document id gains a
        # revision, so ingesting a second revision adds a document without renaming files.
        **({"snapshot_id": src["id"]} if rid != src["id"] else {}),
        "retrieved": retrieved,
        "source_sha256": sha,
        "status": status,
        # federal_instrument is in VERBATIM_REQUIRED, so this is not a free choice — the
        # doc_type IS the assertion that we may reproduce, and CI then requires that we did.
        "content_mode": "verbatim",
        # The graph is OUTBOUND-ONLY: framework.graph() indexes edges by e["from"] and never
        # builds a reverse index, so graph_neighbors("2-cfr-200") lists the sections split out
        # of it only if the PART carries the edges as well. A section -> part edge alone would
        # leave the part a dead end -- you could walk up from § 200.303 but never find it by
        # starting at the part it lives in.
        #
        # If a listed section has no document yet (split_cfr_sections.py not run), frontmatter
        # validation fails with "does not resolve to any document". That is deliberate: a loud
        # dangling edge beats a part that quietly claims no sections.
        #
        # #34: gated on `rid == "2-cfr-200"` -- a literal id -- before. Every other cfr_part
        # ingested silently got NO relationships block at all, indistinguishable from a part
        # genuinely cited at zero sections, which is the same "wrong answer that looks like a
        # right one" #33 was about one field over. Gated on the KIND now, so it applies to
        # whichever part is being built, the same fix #33 made for issuing_body.
        #
        # #77: a WHOLLY SUPERSEDED part is the one case where `cited_section_ids(rid)` is the
        # wrong edge to publish. Every id it would return names one of THIS part's own
        # (equally superseded) split sections -- outbound edges into a dead end, the exact
        # failure the comment above names for the opposite gap. What a reader actually needs
        # from a gone part's own edge is where the LIVE text moved to, so this points at
        # `superseded_by` instead -- and 45 CFR 75's committed `relationships.related:
        # [2-cfr-200]` (dcd0d41) is exactly that, not its own seven split sections.
        #
        # THE AUTO-DERIVED HALF ONLY -- unioned with any curator-added cross-instrument edge
        # via merge_relationships() below (see existing_relationships()'s own docstring for
        # why that half cannot be derived here: FERPA's statute/regulation edge, and the
        # 42 CFR 2 <-> 45 CFR 160/164 comparison edge, are judgements no ingester makes on its
        # own authority). Applies to every kind now, not only cfr_part, so a usc_section (no
        # auto-derived edge of its own) can still carry and preserve a curated one.
        **({"relationships": _rel} if (src["instrument_kind"] == "cfr_part" or _rel) else {}),
        "maintainer": "@morficflux",
        # Written EMPTY on purpose; a human sets them at PR approval. An ingester that
        # stamps a verification it did not perform is worse than a blank.
        "last_verified": "",
        "verified_by": "",
    }
    head = yaml.safe_dump(fm, sort_keys=False, allow_unicode=True, width=100).rstrip()

    stat_line = ", ".join(f"{v} {k}" for k, v in stats.items())
    gap = src.get("known_cited_versions_not_held") or []
    parts = [f"---\n{head}\n---\n", "## At a glance\n",
             f"**{src['citation']}** — {src['title']}\n\n"
             f"- Issued by: {fm['issuing_body']}\n"
             f"- Version: {version or 'not versioned'}\n"
             f"- Text as of: {fm['as_of']}"
             + (f" (removed from the CFR {fm['amended_on']})"
                if superseded and fm.get("amended_on") else
                f" (upstream last amended {fm['amended_on']})" if fm.get("amended_on") else "")
             + (f"\n- {fm['currency']} (OLRC)" if fm.get("currency") else "")
             + f"\n- Extent: {stat_line}\n"
             f"- Reproduction basis: {fm['reproduction_basis']}\n"]
    if superseded and src["instrument_kind"] == "cfr_part":
        # #77: the whole-part note. WHY it was removed is rendered from PART_REMOVALS
        # (cfr_consolidations.py) rather than hand-written a third time -- the same record
        # split_cfr_sections.build() already renders into each removed section's own
        # whole-part sentence (#78). A part with no entry there still gets a true, less
        # specific sentence, the same fallback ladder `why`/`scope` use everywhere else in
        # this pair of modules.
        why = (PART_REMOVALS.get(rid) or {}).get("why")
        successor = _id_to_citation(superseded_by) if superseded_by else None
        drop_in = (f", and do not treat {successor} as a drop-in replacement without "
                   f"comparing them" if successor else "")
        # #77 review (P1/P2/P3): the SECOND paragraph -- "why we hold it" -- is curator
        # content per AGENTS.md hard rule 2, not a mechanical fact this ingester derives on
        # its own authority the way the removal date/successor above are. `curator_note`
        # (from `existing_curator_note()`, read back by main() from whatever is already
        # committed at this part's own path) is used verbatim when present; only a part
        # superseded for the FIRST time -- nothing committed yet to preserve -- falls back to
        # `_default_curator_note()`'s plain, fully-derived sentence. The caveats after it
        # (current-definition-may-differ, the successor-naming drop-in warning, no-section-
        # correspondence) stay generator-owned and always fresh, because `drop_in` is
        # data-dependent (the successor) in a way a preserved sentence must not go stale on.
        note = curator_note or _default_curator_note(rid)
        parts.append(
            f"\n> **This part no longer exists.** It was removed from the CFR in its "
            f"entirety on **{fm['amended_on']}**"
            + (f" — {why}" if why else "")
            + f". The text below is its **last-in-force** text, as of {fm['as_of']}.\n>\n"
            f"> {note} {_CURATOR_NOTE_BOUNDARY} Do not read "
            f"this as current law{drop_in} — no specific section-to-section "
            f"correspondence is recorded here.\n")
    if superseded:
        parts.append(
            "\n_NON-AUTHORITATIVE copy. This is a federal requirement and carries penalties "
            "state policy does not — read it at the source URL before relying on it. This is "
            f"**superseded** text, as it stood on {fm['as_of']}, and is NOT current law._\n")
    else:
        parts.append(
            "\n_NON-AUTHORITATIVE copy. This is a federal requirement and carries penalties "
            "state policy does not — read it at the source URL before relying on it. This copy "
            "is CURRENT text, which is not necessarily the text in force when a rule citing it "
            "was written._\n")
    if gap:
        parts.append(
            "\n> **Version gap.** Oregon material cites version(s) "
            + ", ".join(gap)
            + " of this instrument, which are NOT held here. A citation to one of those is "
              "not answered by the text below, and must not be treated as if it were.\n")
    if src["instrument_kind"] == "usc_section":
        parts.append(
            "\n> **Partial hold (ADR-0006).** This corpus holds the U.S. Code sections "
            "Oregon cites, section by section, on demand — never a title, and never the "
            "Code speculatively. The set held changes as sections are cited; `usc-section` "
            "in `src/citation_schemes.py` names the current count and refuses any other "
            "U.S.C. citation by name rather than by silence.\n")
    parts.append("\n## Full text\n\n" + text + "\n")
    return "\n".join(parts)


def irs_revision(text: str, pdf_path: Path) -> str:
    """The revision of an IRS publication, from TWO independent places that must agree.

    The revision is part of the instrument's identity: Pub 1075 (Rev. 11-2021) states
    different requirements from (Rev. 11-2016), so a citation to one must never be answered
    with the other's text. That makes guessing it worse than failing.

    Both the document body and the PDF's own /Title metadata carry it. Either alone can be
    wrong -- metadata goes stale when a file is re-saved, and body text can be a reference
    to a PRIOR revision rather than this one (this document mentions 2016 and 2014 in its
    change history). Requiring agreement is what makes the answer trustworthy, and a
    disagreement is a real signal rather than an inconvenience, so it raises.
    """
    from_text = IRS_REV.search(text)
    meta = PdfReader(str(pdf_path)).metadata or {}
    from_meta = IRS_REV.search(str(meta.get("/Title") or ""))
    a = from_text.group(1) if from_text else None
    b = from_meta.group(1) if from_meta else None
    if a and b and a != b:
        raise ValueError(f"revision disagrees: body says {a!r}, PDF /Title says {b!r} — "
                         "resolve by hand rather than picking one")
    rev = a or b
    if not rev:
        raise ValueError("no revision found in the body or the PDF metadata; the revision "
                         "is part of this instrument's identity and must not be guessed")
    return rev


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--only", metavar="ID")
    ap.add_argument("--refetch", action="store_true")
    # #77: there was no gate at all on what this script writes for a PART document -- the
    # sibling section-splitter has had one since #58/#78 (`split_cfr_sections.py --check`);
    # this is the missing one. Builds every source in memory and compares it to what is
    # already committed; writes nothing, exits 1 on any mismatch. See existing_supersession()
    # for the one place this stays hermetic on purpose: a cfr_part already committed
    # `status: superseded` trusts its own committed amended_on/superseded_by rather than
    # asking eCFR's live versions endpoint about a part that is no longer there to describe.
    ap.add_argument("--check", action="store_true",
                    help="compare every document to what this ingester would write; "
                         "write nothing, exit 1 on any mismatch")
    args = ap.parse_args()

    if args.check and args.refetch:
        print("error: --check and --refetch are mutually exclusive -- --check verifies "
              "what is already committed against cached snapshots; --refetch replaces "
              "them. Running both leaves it unclear afterward which one actually happened.",
              file=sys.stderr)
        return 1

    sys.path.insert(0, str(ROOT / "src"))
    from corpus_toolkit.repo import hash_snapshot

    sources = yaml.safe_load(MANIFEST.read_text())["sources"]
    if args.only:
        sources = [s for s in sources if s["id"] == args.only] or sys.exit(
            f"no manifest source with id {args.only!r}")

    OUT_DIR.mkdir(exist_ok=True)
    SNAPSHOTS.mkdir(parents=True, exist_ok=True)
    ok = failed = 0
    ingested_ids: set[str] = set()
    for src in sources:
        rid, fmt = src["id"], src["format"]
        try:
            # VALIDATED BEFORE ANY SIDE EFFECT, not just before the document is written.
            # resolve_issuing_body() needs nothing from the fetch -- for `cfr_part` it reads
            # only `src["issuing_body"]`, already in hand from the manifest -- so calling it
            # here means a manifest entry missing its issuer fails before this run touches
            # disk at all. Moved here after a `--only` run against a synthetic incomplete
            # entry left `_meta/snapshots/<id>.txt` written and `_meta/source-manifest.yml`'s
            # sha256 line edited despite the ValueError, because both used to happen inside
            # this same try block but ABOVE the `build()` call that is resolve_issuing_body's
            # only other caller. That half-ingested state (manifest entry now looks hashed
            # and current, snapshot text present, no document) is exactly the shape
            # check_extraction.py does not expect: `docs[sid][0][1]` assumes every manifest
            # source with a committed raw snapshot owns at least one document, and crashes
            # with an unhandled KeyError instead of reporting a clean FAIL — filed as #53
            # rather than fixed here, since check_extraction.py is a different review
            # surface and the underlying fragility is general, not specific to this path.
            resolve_issuing_body(src)
            snap = SNAPSHOTS / f"{rid}.{fmt}"
            fresh = not snap.is_file() or args.refetch
            raw = fetch(src["url"], snap, args.refetch)

            # DISPATCHED ON instrument_kind, NEVER ON `fmt`. USLM is `format: xml`, same as
            # eCFR — the first source to be BOTH is exactly what makes this load-bearing: a
            # format-keyed dispatch would run a USLM title through extract_cfr, which reads
            # `TYPE="SECTION"` attributes USLM does not have and returns silently EMPTY text
            # (confirmed: 0 chars on Title 20's own XML) rather than raising, which the
            # `len(text) < 2000` guard below would then report as "scanned or broken" -- a
            # true-sounding diagnosis of the wrong file. check_extraction.py's dispatch must
            # agree with this one, or the checker re-derives a different "expected" than what
            # was actually committed and reports a fidelity defect that is really a disagreement
            # about which extractor ran.
            part_status, part_superseded_by = "current", None
            if src["instrument_kind"] == "cfr_part":
                text, stats = extract_cfr(raw)
                part_status, part_superseded_by, committed_amended_on = \
                    existing_supersession(OUT_DIR / f"{rid}.md")
                if part_status == "superseded":
                    # #77: the part is gone from the CFR in its entirety (45 CFR 75,
                    # dcd0d41). Nothing LIVE describes it any more -- cfr_amended_on() asks
                    # eCFR's versions endpoint what the part IS today, and a wholly-removed
                    # part is answered by neither "current" nor a clean history, the same
                    # gap split_cfr_sections.committed_amended_on() exists to name for the
                    # analogous per-section case. So this trusts the date already accepted
                    # into the document at PR time rather than asking a live source a
                    # question it cannot answer.
                    src = {**src, "amended_on": committed_amended_on}
                else:
                    src = {**src,
                           "amended_on": src.get("amended_on") or cfr_amended_on(src["url"])}
            elif src["instrument_kind"] == "usc_section":
                usc_title, usc_sec = src["id"].split("-usc-", 1)
                usc_root = ET.fromstring(raw)
                text, stats, section_el = extract_usc(usc_root, usc_title, usc_sec)
                src = {**src,
                       "amended_on": src.get("amended_on") or usc_amended_on(section_el),
                       "currency": usc_currency(usc_root)}
            elif src["instrument_kind"] == "agency_guidance":
                # THE ONE KIND THAT SPANS FORMATS, so it is the one place format has to be
                # consulted -- and that is not a violation of the rule above, it is the
                # other half of it. That rule exists because two KINDS shared one format
                # (eCFR XML and USLM XML), so format could not identify the extractor. Here
                # one kind spans two formats: CMS and FEMA publish PDFs, FNS and the two
                # private standards bodies publish HTML pages. Kind alone cannot identify
                # the extractor either. Both rules reduce to: dispatch on whichever of the
                # two actually determines the parser, and never guess.
                #
                # Before this, the `else` below ran extract_pdf() on everything that was not
                # CFR or U.S.C. That held only because every other kind happened to be a
                # PDF; an HTML entry reached a PDF parser and died with PdfStreamError,
                # which reads as a corrupt download rather than "this was never a PDF".
                if fmt == "html":
                    from corpus_toolkit.html_to_text import html_to_text
                    text = html_to_text(raw)          # takes bytes, not str
                    stats = {"chars": len(text)}
                elif fmt == "pdf":
                    text, stats = extract_pdf(snap)
                else:
                    raise ValueError(
                        f"{rid}: agency_guidance supports format html or pdf, not {fmt!r} "
                        "— declare one rather than letting a parser be guessed")
            else:
                text, stats = extract_pdf(snap)
            if len(text) < 2000:
                raise ValueError(f"only {len(text)} chars extracted — scanned or broken")

            version = src.get("version")
            if src["instrument_kind"] == "irs_publication" and not version:
                version = irs_revision(text, snap)

            # BOTH WRITES BELOW ARE GUARDED ON `not args.check`. --check's whole contract is
            # "compare every source to what is committed; write nothing" (see the flag's own
            # --help text and this module's docstring), but before this fix both ran
            # unconditionally, above the `if args.check:` branch several lines down. Measured
            # damage from running `--check` in a clean copy: the freshly extracted `text` --
            # UNANCHORED, because anchor_sections.py's re-anchoring pass below only ever runs
            # when `ingested_ids` is non-empty, and --check never adds to it -- overwrote the
            # committed, anchored .txt for every RULES source (pl-113-128, pl-115-224,
            # irs-pub-1075: 157/29/69 anchors each, stripped to 0), which then failed
            # `anchor_sections.py --check`, a CI gate (.github/workflows/ci.yml). Writing the
            # manifest's sha256 back (write_manifest_hash(), reached via record_source_hash())
            # is the same class of side effect one line lower. Neither write is needed to
            # PRODUCE `built` for comparison below -- hash_snapshot() reads whatever .txt is
            # ALREADY on disk (falling back to the raw snapshot) rather than the one just
            # written, by its own docstring ("never re-derived from the source at verification
            # time"), so skipping the write under --check does not change what `sha` is.
            if not args.check:
                (SNAPSHOTS / f"{rid}.txt").write_text(text, encoding="utf-8")
            sha = hash_snapshot(rid, fmt, SNAPSHOTS)
            # The MANIFEST hash is a different quantity from the document's source_sha256,
            # and conflating them is a trap I fell into once already. `source_sha256` is
            # hash_snapshot() -- our extractor's output. The manifest's is what
            # corpus-detect-changes will compute on a fresh fetch, via the TOOLKIT's
            # converter. Storing ours there swaps one permanent false positive for another
            # while looking fixed. Verified: content_hash on the committed XML equals what
            # the drift job computed from the live URL, to the character.
            if not args.check:
                note = record_source_hash(rid, raw, fmt, src["url"])
                if note:
                    print(f"    {note}")
            doc_path = OUT_DIR / f"{doc_id(src, version)}.md"
            as_of, retrieved = source_dates(src, snap, fresh, doc_path)
            # #77 review (P1/P2/P3): read back BEFORE build() overwrites the file, same shape
            # as existing_supersession() above -- None for a part superseded for the first
            # time, in which case build() falls back to _default_curator_note() itself.
            curator_note = (existing_curator_note(doc_path) if part_status == "superseded"
                             else None)
            built = build(src, text, sha, stats, version, as_of, retrieved,
                          status=part_status, superseded_by=part_superseded_by,
                          curator_note=curator_note,
                          existing_rel=existing_relationships(doc_path))
            if args.check:
                committed = doc_path.read_text(encoding="utf-8") if doc_path.is_file() else None
                if committed != built:
                    failed += 1
                    print(f"  {rid:22} MISMATCH — committed document does not match what "
                          f"this ingester would write", file=sys.stderr)
                    continue
                ok += 1
                # #77 review (P8): a superseded part's `amended_on` was TRUSTED from the
                # committed document rather than verified (there is no live endpoint left to
                # verify it against -- eCFR 404s for a wholly-removed part, not just its
                # sections). Plain success output used to read as though every field had been
                # checked; #73 named this exact gap for the analogous per-SECTION case
                # (split_cfr_sections.committed_amended_on()) and its fix was disclosure, not
                # silence: "a green --check read as though it had not [verified]." Same fix,
                # here, for the one field this ingester echoes rather than checks.
                disclosed = ("  — amended_on ECHOED, NOT VERIFIED (superseded part; eCFR has "
                              "no live record for a part that no longer exists at all, see "
                              "committed_amended_on()'s docstring in split_cfr_sections.py, "
                              "#73)" if part_status == "superseded" else "")
                print(f"  {rid:22} ok — matches committed document{disclosed}")
                continue
            doc_path.write_text(built, encoding="utf-8")
            ok += 1
            ingested_ids.add(rid)
            print(f"  {rid:22} {len(text):>9,} chars  {stats}  version={version}")
            if fresh:
                time.sleep(2)
        except Exception as e:                       # noqa: BLE001 — reported, not hidden
            failed += 1
            print(f"  {rid:22} FAILED: {type(e).__name__}: {e}", file=sys.stderr)

    print(f"\n{ok} matched, {failed} mismatched." if args.check
          else f"\n{ok} ingested, {failed} failed.")

    # RE-APPLY THE POST-PROCESSING THIS RUN JUST UNDID.
    #
    # anchor_sections.py inserts `### ` anchors into BOTH the snapshot .txt and the
    # document body, and records the fact in conversion_notes. This loop regenerates
    # both FROM THE SOURCE, so a re-ingest of an anchored document silently drops every
    # anchor and the note describing them. Measured on pl-113-128: 157 anchors in each
    # file before, 0 after, conversion_notes gone, 317 lines rewritten.
    #
    # ci.yml runs `anchor_sections.py --check`, so this could never reach main -- but
    # the recovery was "re-ingest, watch CI go red, remember that a second script owns
    # part of this document, re-run it". A step that undoes another step's work and
    # leaves a gate to notice is not finished; it has delegated its cleanup to whoever
    # reads the failure.
    #
    # Idempotent by construction, so re-anchoring costs nothing when nothing was lost.
    # Never reached under --check: nothing above added to `ingested_ids` without writing.
    if ingested_ids:
        from anchor_sections import RULES as _ANCHOR_RULES, process as _anchor
        touched = {i for i in ingested_ids
                   if i in _ANCHOR_RULES or any(r["doc"] == i for r in _ANCHOR_RULES.values())}
        if touched:
            print(f"\nre-anchoring {len(touched)} document(s) this run regenerated: "
                  f"{', '.join(sorted(touched))}")
            rc = _anchor(check=False, only=touched)
            if rc:
                print("  anchoring reported a problem — the documents above are NOT in "
                      "their committed shape", file=sys.stderr)
                return 1
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
