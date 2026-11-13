#!/usr/bin/env python3
"""Measure how many references in held documents to NIST publications resolve INSIDE the corpus.

    python3 src/measure_nist_resolution.py                 # this checkout
    python3 src/measure_nist_resolution.py --root DIR      # another checkout (e.g. `git archive origin/main`)

#42's whole point is "those chains stop dead-ending", so this measures that directly: every
reference is turned into a citation string from the document's own words and sent through the
corpus's REAL resolver (CorpusFramework.resolve_citation), and "resolves" means the resolver
returned a held document -- never a proxy such as "a document with that id exists".

It is a measurement, not a gate, and deliberately standalone: it classifies each mention with
its OWN regexes (the issue's, verbatim) rather than federal_ids.py's, so it can be run against a
checkout that predates the NIST scheme (the "before" number) and so the classification is an
independent cross-check on the resolver rather than the resolver agreeing with itself.
"""
from __future__ import annotations

import argparse
import collections
import os
import pathlib
import re
import sys

import yaml

# The issue's own patterns (#42, first comment), verbatim.
PUBS = {
    "NIST SP 800-53": (re.compile(r"800[-\u2011 ]?53[AB]?\b", re.I), "nist-sp-800-53-"),
    "FIPS 140": (re.compile(r"FIPS\s*(?:PUB\s*)?140[-\u2011 ]?\d?\b", re.I), "fips-140"),
    "NIST SP 800-63": (re.compile(r"800[-\u2011 ]?63[A-C]?\b", re.I), "nist-sp-800-63"),
}
CTRL = re.compile(r"\b([A-Z]{2})-(\d{1,2})(\(\d{1,2}\))?\b")
FAM = set("AC AT AU CA CM CP IA IR MA MP PE PL PM PS RA SA SC SI SR PT".split())
REV = re.compile(r"^[\s,(:]*(?:Rev(?:ision|\.)?\s*(\d)|r(\d))", re.I)


def held_documents(root: pathlib.Path):
    for path in sorted((root / "instruments").glob("*.md")):
        text = path.read_text(encoding="utf-8", errors="ignore")
        fm = yaml.safe_load(text.split("---", 2)[1]) or {}
        if str(fm.get("instrument_kind", "")).startswith("nist_"):
            continue            # a NIST document citing itself is not a held document citing NIST
        yield fm.get("id", path.stem), text


def mention_class(text: str, m: re.Match) -> str:
    """rev5 | rev4 | other-rev | unversioned | different-publication (800-53A/B)."""
    if m.group(0)[-1] in "ABab":          # 800-53A / 800-53B: other publications
        return "different-publication"
    r = REV.match(text[m.end():m.end() + 40])
    rev = (r.group(1) or r.group(2)) if r else None
    return {"5": "rev5", "4": "rev4", None: "unversioned"}.get(rev, "other-rev")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--root", default=str(pathlib.Path(__file__).resolve().parent.parent))
    root = pathlib.Path(ap.parse_args().root).resolve()
    os.chdir(root)
    from corpus_toolkit import config as cfg
    from corpus_toolkit.mcp.framework import CorpusFramework
    fw = CorpusFramework(cfg.load("_meta/corpus.yml"))

    cache: dict = {}

    def resolves(citation: str, prefix: str = "") -> tuple[bool, str]:
        """True iff the resolver returned a held document whose id starts with `prefix`. The
        prefix is what keeps a mention's context window (which can contain a neighbouring
        `6 CFR 37` or `CJIS` citation) from being counted as resolving the NIST reference."""
        key = (citation, prefix)
        if key not in cache:
            r = fw.resolve_citation(citation)
            cache[key] = (any(m["id"].startswith(prefix) for m in r.get("matches", [])),
                          r.get("note") or "")
        return cache[key]

    docs = list(held_documents(root))
    print(f"root: {root}\nheld documents scanned (NIST documents excluded): {len(docs)}\n")

    print("PUBLICATION MENTIONS (the issue's regexes; each sent to the resolver as the "
          "document's own words)")
    for name, (rx, id_prefix) in PUBS.items():
        total = 0
        by_class = collections.Counter()
        resolved = collections.Counter()
        per_doc = collections.Counter()
        for doc_id, text in docs:
            spans = [x.span() for x in rx.finditer(text)]
            for k, m in enumerate(rx.finditer(text)):
                cls = mention_class(text, m) if name == "NIST SP 800-53" else "n/a"
                # The window is the mention in its own words, cut at the neighbouring mentions
                # of the same publication so one citation's window cannot answer for another.
                lo = max(m.start() - 30, spans[k - 1][1] if k else 0)
                hi = min(m.end() + 90, spans[k + 1][0] if k + 1 < len(spans) else len(text))
                ctx = " ".join(text[lo:hi].split())
                ok, _ = resolves(ctx, id_prefix)
                if os.environ.get("MEASURE_VERBOSE") and not ok and cls in ("rev5", "unversioned"):
                    print(f"        [{cls} unresolved] {doc_id}: {ctx}")
                total += 1
                per_doc[doc_id] += 1
                by_class[cls] += 1
                resolved[cls] += ok
        print(f"  {name}: {total} mentions, {sum(resolved.values())} resolve inside the corpus")
        if name == "NIST SP 800-53":
            for cls in ("rev5", "unversioned", "rev4", "other-rev", "different-publication"):
                if by_class[cls]:
                    print(f"      {cls:22} {by_class[cls]:4} mentions, {resolved[cls]:4} resolve")
        print(f"      by document: {dict(per_doc.most_common())}")

    print("\nCONTROL TOKENS in documents that name 800-53 (the issue's regex, verbatim: it also "
          "matches CSF subcategories such as PR.AC-3), each sent as `NIST SP 800-53 Rev. 5 <token>`")
    tokens: collections.Counter = collections.Counter()
    for doc_id, text in docs:
        if not re.search(r"800[-‑ ]?53", text, re.I):
            continue
        for m in CTRL.finditer(text):
            if m.group(1) in FAM:
                embedded = m.start() > 0 and (text[m.start() - 1].isalnum() or text[m.start() - 1] == ".")
                tokens[(f"{m.group(1)}-{m.group(2)}{m.group(3) or ''}", embedded)] += 1
    real = {t: n for (t, emb), n in tokens.items() if not emb}
    embedded_tokens = {t: n for (t, emb), n in tokens.items() if emb}
    def control_resolves(tok: str) -> bool:
        # The matched document must be THAT control's (`nist-sp-800-53-r5.ac-2`), not merely the
        # publication: a token like `IA-0` is not a control, and the resolver answering it with
        # the whole publication is not a resolved reference.
        fam, num = tok.split("(")[0].split("-")
        return resolves(f"NIST SP 800-53 Rev. 5 {tok}", f"nist-sp-800-53-r5.{fam.lower()}-{int(num)}")[0]
    ok_tokens = sum(n for t, n in real.items() if control_resolves(t))
    bad = {t: n for t, n in real.items() if not control_resolves(t)}
    print(f"  {sum(tokens.values())} tokens by the issue's regex; {sum(embedded_tokens.values())} "
          f"of them sit inside a longer id (NIST CSF `PR.AC-3` etc. -- not 800-53 controls)")
    print(f"  {sum(real.values())} control-shaped tokens: {ok_tokens} resolve to a held control "
          f"document, {sum(bad.values())} do not")
    if bad:
        print(f"      unresolved: {dict(sorted(bad.items(), key=lambda kv: -kv[1]))}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
