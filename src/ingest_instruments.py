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


def cfr_amended_on(url: str) -> str | None:
    """The date eCFR says this TITLE was last amended, read from eCFR rather than the manifest.

    `amended_on` is half of the pair that makes this corpus's central guardrail work: with
    `as_of` it is what lets a caller tell current text from the text in force when a citing
    rule was written. Leaving it null defeats the purpose of holding current text at all.

    Derived, not transcribed. A hand-copied date in the manifest is correct until the next
    amendment and silently wrong afterwards, and this one moves often -- Title 2 was amended
    twice in the month this corpus was built.
    """
    m = re.search(r"title-(\d+)", url)
    if not m:
        return None
    try:
        req = urllib.request.Request("https://www.ecfr.gov/api/versioner/v1/titles.json",
                                     headers={"User-Agent": UA})
        data = json.load(urllib.request.urlopen(req, timeout=60))
    except Exception:                                # noqa: BLE001 — absence is reported, not fatal
        return None
    for t in data.get("titles", []):
        if str(t.get("number")) == m.group(1):
            return t.get("latest_amended_on")
    return None


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


def extract_cfr(raw: bytes) -> tuple[str, dict]:
    """eCFR part XML -> markdown, one `##` heading per section.

    Sections come from `DIV8[@TYPE='SECTION']`, whose `N` attribute is the section number.
    Appendices are kept: 2 CFR 200 has 12 of them and they carry substantive requirements,
    not just forms.
    """
    root = ET.fromstring(raw)
    out, n_sec, n_app = [], 0, 0
    for el in root.iter():
        kind = el.get("TYPE")
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
            t = _flatten(child)
            if t:
                out.append(t)
        out.append("")
        n_sec += kind == "SECTION"
        n_app += kind == "APPENDIX"
    text = re.sub(r"\n{3,}", "\n\n", "\n".join(out)).strip()
    return text, {"sections": n_sec, "appendices": n_app}


# ---------------------------------------------------------------- PDF

def page_furniture(pages: list[list[str]]) -> tuple[set[str], set[str]]:
    """Lines repeated at the top/bottom of most pages: letterhead, banners, footers."""
    if len(pages) < 4:
        return set(), set()
    top, bot = {}, {}
    for p in pages:
        for l in [x.strip() for x in p[:3] if x.strip()]:
            top[l] = top.get(l, 0) + 1
        for l in [x.strip() for x in p[-3:] if x.strip()]:
            bot[l] = bot.get(l, 0) + 1
    half = len(pages) / 2
    return ({l for l, n in top.items() if n > half},
            {l for l, n in bot.items() if n > half})


def is_page_number(line: str, npages: int) -> bool:
    s = line.strip()
    return bool(re.fullmatch(r"(page\s+)?\d{1,4}(\s*(of|/)\s*\d{1,4})?", s, re.I)) and \
        len(s) <= 18 and npages > 1


def extract_pdf(path: Path) -> tuple[str, dict]:
    reader = PdfReader(str(path))
    pages = [(p.extract_text() or "").splitlines() for p in reader.pages]
    head, foot = page_furniture(pages)
    out = []
    for lines in pages:
        for l in lines:
            s = l.strip()
            if not s or s in head or s in foot or is_page_number(s, len(pages)):
                continue
            out.append(s)
    text = re.sub(r"\n{3,}", "\n\n", "\n".join(out)).strip()
    # Same '## ' guard as the CFR path, for the same reason.
    text = re.sub(r"^(#{1,6}\s)", r" \1", text, flags=re.M)
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


def build(src: dict, text: str, sha: str, stats: dict, version: str | None) -> str:
    rid = src["id"]
    fm = {
        "schema_version": 1,
        "corpus": "federal-reference",
        "jurisdiction": "us",
        "id": rid,
        "title": src["title"],
        "doc_type": "federal_instrument",
        "citation": src["citation"],
        "authority_level": "federal",
        "issuing_body": {"cfr_part": "Office of Management and Budget",
                         "irs_publication": "Internal Revenue Service",
                         "fbi_policy": "Federal Bureau of Investigation, CJIS Division",
                         "public_law": "United States Congress"}[src["instrument_kind"]],
        "instrument_kind": src["instrument_kind"],
        "version": version,
        "as_of": time.strftime("%Y-%m-%d"),
        "amended_on": src.get("amended_on"),
        "reproduction_basis": " ".join(str(src["reproduction_basis"]).split()),
        "superseded_by": None,
        "source_url": src["url"],
        "source_format": src["format"],
        "retrieved": time.strftime("%Y-%m-%d"),
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
            (OUT_DIR / f"{rid}.md").write_text(build(src, text, sha, stats, version),
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
