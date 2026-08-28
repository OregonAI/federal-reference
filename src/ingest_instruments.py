#!/usr/bin/env python3
"""Fetch each manifest source, snapshot it, and write instruments/<id>.md.

  python3 src/ingest_instruments.py                # ingest everything
  python3 src/ingest_instruments.py --only 2-cfr-200
  python3 src/ingest_instruments.py --refetch      # ignore cached snapshots

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
import json
import re
import sys
import time
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

import yaml
from pypdf import PdfReader

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

# These three kinds really are constant per kind: every IRS publication comes from the IRS,
# every CJIS policy from the FBI's CJIS Division, every public law from Congress. `cfr_part`
# is deliberately NOT in this table — see resolve_issuing_body().
ISSUING_BODY_BY_KIND = {
    "irs_publication": "Internal Revenue Service",
    "fbi_policy": "Federal Bureau of Investigation, CJIS Division",
    "public_law": "United States Congress",
}


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
    if kind == "cfr_part":
        body = src.get("issuing_body")
        if not body:
            raise ValueError(
                f"{src['id']!r} is a cfr_part with no issuing_body declared in "
                f"{MANIFEST.name} — the issuing agency is a fact about this specific part "
                "and must be stated, not assumed")
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


def record_source_hash(rid: str, raw: bytes, fmt: str) -> str:
    """Record the hash corpus-detect-changes will compare against. Returns a status line.

    PDFs go through `pdftotext`, which is not present in every environment. When it is
    missing this SKIPS rather than writing a hash computed some other way -- a manifest hash
    produced by a different function than the detector uses is worse than an empty one,
    because an empty one is visibly unpopulated while a wrong one looks authoritative and
    reports CHANGED forever.
    """
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


def fetch(url: str, dest: Path, refetch: bool) -> bytes:
    if dest.is_file() and not refetch:
        return dest.read_bytes()
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    raw = urllib.request.urlopen(req, timeout=300).read()
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

def cited_section_ids() -> list[str]:
    """Document ids for the sections split out of 2 CFR 200, in citation order.

    Read from _meta/cited-sections.yml -- the same committed list split_cfr_sections.py
    works from -- so the part's edges and the section documents cannot disagree about which
    sections exist.
    """
    path = ROOT / "_meta" / "cited-sections.yml"
    if not path.is_file():
        return []
    doc = yaml.safe_load(path.read_text()) or {}
    return [f"2-cfr-200.{e['section'].split('.', 1)[1]}"
            for key in ("current", "removed") for e in (doc.get(key) or [])]


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
          as_of: str, retrieved: str) -> str:
    rid = doc_id(src, version)
    fm = {
        "schema_version": 1,
        "corpus": "federal-reference",
        "jurisdiction": "us",
        "id": rid,
        "title": src["title"],
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
        "reproduction_basis": " ".join(str(src["reproduction_basis"]).split()),
        "superseded_by": None,
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
        "status": "current",
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
        **({"relationships": {"related": cited_section_ids()}} if rid == "2-cfr-200" else {}),
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
             + (f" (upstream last amended {fm['amended_on']})" if fm.get("amended_on") else "")
             + f"\n- Extent: {stat_line}\n"
             f"- Reproduction basis: {fm['reproduction_basis']}\n"]
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
    args = ap.parse_args()

    sys.path.insert(0, str(ROOT / "src"))
    from corpus_toolkit.repo import hash_snapshot

    sources = yaml.safe_load(MANIFEST.read_text())["sources"]
    if args.only:
        sources = [s for s in sources if s["id"] == args.only] or sys.exit(
            f"no manifest source with id {args.only!r}")

    OUT_DIR.mkdir(exist_ok=True)
    SNAPSHOTS.mkdir(parents=True, exist_ok=True)
    ok = failed = 0
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

            if src["instrument_kind"] == "cfr_part":
                text, stats = extract_cfr(raw)
                src = {**src, "amended_on": src.get("amended_on") or cfr_amended_on(src["url"])}
            else:
                text, stats = extract_pdf(snap)
            if len(text) < 2000:
                raise ValueError(f"only {len(text)} chars extracted — scanned or broken")

            version = src.get("version")
            if src["instrument_kind"] == "irs_publication" and not version:
                version = irs_revision(text, snap)

            (SNAPSHOTS / f"{rid}.txt").write_text(text, encoding="utf-8")
            sha = hash_snapshot(rid, fmt, SNAPSHOTS)
            # The MANIFEST hash is a different quantity from the document's source_sha256,
            # and conflating them is a trap I fell into once already. `source_sha256` is
            # hash_snapshot() -- our extractor's output. The manifest's is what
            # corpus-detect-changes will compute on a fresh fetch, via the TOOLKIT's
            # converter. Storing ours there swaps one permanent false positive for another
            # while looking fixed. Verified: content_hash on the committed XML equals what
            # the drift job computed from the live URL, to the character.
            note = record_source_hash(rid, raw, fmt)
            if note:
                print(f"    {note}")
            doc_path = OUT_DIR / f"{doc_id(src, version)}.md"
            as_of, retrieved = source_dates(src, snap, fresh, doc_path)
            doc_path.write_text(
                build(src, text, sha, stats, version, as_of, retrieved),
                encoding="utf-8")
            ok += 1
            print(f"  {rid:22} {len(text):>9,} chars  {stats}  version={version}")
            if fresh:
                time.sleep(2)
        except Exception as e:                       # noqa: BLE001 — reported, not hidden
            failed += 1
            print(f"  {rid:22} FAILED: {type(e).__name__}: {e}", file=sys.stderr)

    print(f"\n{ok} ingested, {failed} failed.")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
