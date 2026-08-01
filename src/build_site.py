#!/usr/bin/env python3
"""Build the GitHub Pages site into ./site/ (gitignored; produced at deploy time).

    python3 src/build_site.py

Chrome, CSS and the cross-corpus contracts live in `corpus_toolkit.site`. This file owns
only what is specific to this corpus.

THIS REPLACES the reusable publish-index workflow — the two must never both exist here,
because they fight over the `pages` concurrency group.
"""
import collections
import json
import pathlib
import sys

import yaml

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))

from corpus_toolkit import config as config_mod                       # noqa: E402
from corpus_toolkit.site import Page, Section, Tile, build            # noqa: E402

REPO = pathlib.Path(__file__).resolve().parent.parent


def stats() -> dict:
    kinds = collections.Counter()
    for p in (REPO / "instruments").rglob("*.md"):
        fm = yaml.safe_load(p.read_text().split("---", 2)[1]) or {}
        kinds[fm.get("instrument_kind", "?")] += 1
    g = json.loads((REPO / "_meta/graph.json").read_text())
    return {"docs": g["n_nodes"], "edges": g["n_edges"],
            "cfr_sections": kinds.get("cfr_section", 0), "kinds": kinds}


def main() -> int:
    s = stats()
    out = build(Page(
        config=config_mod.load(REPO / "_meta/corpus.yml"),
        repo="federal-reference",
        title="Federal Reference — the federal rules Oregon is audited against",
        description=("A non-authoritative, machine-readable mirror of the federal "
                     "instruments Oregon agencies must comply with — 2 CFR 200, CJIS, "
                     "IRS Publication 1075, WIOA and Perkins V."),
        eyebrow="United States · federal instruments",
        headline="Where Oregon's authority chain leaves the state",
        lede_html=(
            f"<b>{s['docs']} federal instruments</b> that Oregon agencies are audited "
            f"against — including <b>{s['cfr_sections']} individual sections of 2 CFR 200</b>, "
            "each separately addressable, because that is the grain an audit finding cites "
            "at."),
        disclaimer=("NON-AUTHORITATIVE reference — not the official federal text. Always "
                    "verify against eCFR, the Federal Register, or the issuing agency."),
        tiles=[
            Tile("Federal instruments", f"{s['docs']}",
                 "the ones Oregon actually cites, not a full mirror of federal law"),
            Tile("2 CFR 200 sections", f"{s['cfr_sections']}",
                 "the Uniform Guidance, split to the section an audit cites"),
            Tile("Internal edges", f"{s['edges']}",
                 "cross-references between the instruments themselves"),
        ],
        sections=[
            Section("The only corpus here that is not Oregon", """
    <ul class="plain">
      <li>Every sibling corpus stops at the state border. This one is deliberately the
        other side of it: it exists so that an Oregon audit finding citing
        <code>2 CFR 200.303</code> resolves to the text of that section instead of dangling.</li>
      <li><b>Scoped to what Oregon cites</b>, not to federal law in general. The sections
        present were selected by scanning
        <a href="https://oregonai.github.io/oregon-audits/">Audits</a> and
        <a href="https://oregonai.github.io/executive-regulatory-frameworks/">Executive
        Regulatory Frameworks</a> for the federal citations they actually make.</li>
      <li>That scoping is a deliberate limit, not an omission: a corpus that claimed to
        hold "federal law" and held 43 documents would be misleading about its own
        coverage.</li>
    </ul>"""),
            Section("Reproduction basis", """
    <ul class="plain">
      <li>Federal regulations are <b>United States government works</b> and are not subject
        to copyright, which is recorded per document rather than assumed — the
        <code>reproduction_basis</code> field states why each instrument may be mirrored.</li>
      <li>Sections carry <code>as_of</code> and <code>amended_on</code> dates: federal text
        changes, and a citation to a section is a citation to a version of it.</li>
    </ul>"""),
            Section("For agents", """
    <ul class="plain">
      <li><b>MCP server</b> — tools: <code>search_corpus</code>, <code>get_document</code>,
        <code>resolve_citation</code>, <code>corpus_overview</code>,
        <code>graph_neighbors</code>, <code>authority_chain</code>.</li>
      <li><b>Every instrument carries provenance</b> — source URL, retrieval date and a
        content hash.</li>
    </ul>"""),
        ],
        footer_note=("Unofficial and non-authoritative; not affiliated with any federal "
                     "agency or with the State of Oregon."),
    ))
    print(f"built site/ — {s['docs']} instruments, {s['cfr_sections']} CFR sections")
    print(f"  corpus-index.json: {out['index']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
