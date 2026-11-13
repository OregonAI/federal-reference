#!/usr/bin/env python3
"""Promote the cited controls of NIST SP 800-53 Rev. 5 into their own documents (#42).

    python3 src/split_nist_controls.py            # write every control document
    python3 src/split_nist_controls.py --check    # compare to what is committed; write nothing

Reads `_meta/cited-controls/nist-sp-800-53-r5.yml` (produced by src/scan_cited_controls.py) and
writes one `instruments/nist-sp-800-53-r5.<fam>-<n>.md` per cited control the catalog contains.
Run AFTER ingest_instruments.py has written the publication and anchor_sections.py has put the
`### ` control anchors in its snapshot.

THIS IS ADR-0003 APPLIED TO A PUBLICATION RATHER THAN A CFR PART. The held documents do not cite
800-53 as a blob; they cite named controls (4,339 tokens across 5 documents when this was
written), so the publication is held whole with its controls as `### ` headings, and a control is
promoted to its own document because a held document cites it. A control document is cut from the
publication's one snapshot (`snapshot_id`), so it cannot disagree with the publication
(src/slicing.py).

ONE DOCUMENT PER BASE CONTROL, ENHANCEMENTS INCLUDED. `AC-2(1)` is part of the AC-2 text in the
source -- it prints under `Control Enhancements:` inside AC-2 -- and a citation to it is answered
by the AC-2 document. Splitting enhancements out would mean cutting inside a control the source
does not cut inside, and would mint ids no sibling can derive from `AC-2(1)` alone.

A CITED CONTROL THE CATALOG DOES NOT HAVE IS A FINDING, NOT A DROP: it is returned in `missing`
and --check fails on it, so the cited-controls file and the catalog cannot silently disagree.

RELEASE 5.2.0. The held text is the Rev. 5 PDF of record (updates as of 2020-12-10). NIST's
listing of record says a later minor release (5.2.0, 2025-08-27) changed some controls. For each
control NIST lists, the document says so and says the held text does NOT include the change; the
list is read from `_meta/nist-sp-800-53-r5-release-5-2-0.yml` (see that file for how it was
derived), never typed here.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
import slicing  # noqa: E402
from nist_controls import PUBLICATION_ID  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
INSTRUMENTS = ROOT / "instruments"
SNAPSHOTS = ROOT / "_meta" / "snapshots"
CITED = ROOT / "_meta" / "cited-controls" / f"{PUBLICATION_ID}.yml"
RELEASE = ROOT / "_meta" / "nist-sp-800-53-r5-release-5-2-0.yml"

HEADING = re.compile(r"^### (?P<ctl>[A-Z]{2}-\d{1,2})\s+(?P<title>.+?)\s*$")
# A WITHDRAWN CONTROL is one whose body, after the heading, IS the notice `[Withdrawn: ...]`. A
# withdrawn ENHANCEMENT prints the same notice inside a live control (AC-2 has several), so a search
# of the whole body would mark AC-2 withdrawn -- it was, on the first real run.
WITHDRAWN = re.compile(r"\A\[Withdrawn:\s*(?P<why>.*?)\]", re.S)
_FURNITURE = re.compile(r"^(?:CHAPTER THREE\s+PAGE \d+|This publication is available free of "
                        r"charge from:.*)$")


def withdrawn_reason(body: str) -> str | None:
    """The reason a control is withdrawn, or None if it is not. `body` starts with the heading;
    running page headers between the heading and the notice are skipped."""
    rest = [l.strip() for l in body.splitlines()[1:] if l.strip()]
    rest = [l for l in rest if not _FURNITURE.match(l)]
    m = WITHDRAWN.match(" ".join(rest))
    return " ".join(m.group("why").split()) if m else None


def base_of(cid: str) -> str:
    """`sa-8(14)` -> `sa-8`."""
    return cid.split("(", 1)[0]


def release_changes(release: dict | None, cid: str) -> list[str]:
    """How NIST's release 5.2.0 notes list control `cid` (a base id), as phrases that quote the
    note's own categories. Empty when it does not list it."""
    if not release:
        return []
    out = []
    for key, phrase in (
            ("new_controls_or_enhancements", "adds a control or enhancement"),
            ("revised", "revises an existing control or enhancement"),
            ("discussion_updated", "updates the control discussion")):
        if any(base_of(x) == cid for x in release.get(key) or []):
            out.append(phrase)
    related = release.get("related_controls_updated") or []
    if (any(base_of(x) == cid for x in related)
            or (release.get("related_controls_updated_all_dash_01") and cid.endswith("-1"))):
        out.append("updates the related controls")
    return out


def _release_note(release: dict, changes: list[str]) -> str:
    return (f"\n> **Release {release['release']} postdates this text.** NIST's listing of record "
            f"([{release['source_url']}]({release['source_url']})) says that on {release['issued']} it "
            f"issued release {release['release']} of SP 800-53, which "
            + " and ".join(changes) + " for this control. The text below is the Rev. 5 PDF "
            f"of record and does NOT include that change; read NIST's own list of the "
            f"changes ([summary]({release['changes_summary_url']})) before relying on this "
            f"control's text.\n")


def build_control(parent: dict, text: str, entry: dict, release: dict | None) -> str | None:
    """The document for one cited control, or None when the catalog has no such control."""
    cid = entry["id"]
    doc_id = f"{parent['id']}.{cid}"
    try:
        body = slicing.slice(doc_id, parent["id"], text).rstrip("\n")
    except LookupError:
        return None
    head = HEADING.match(body.splitlines()[0])
    if head is None:
        raise ValueError(f"{doc_id}: first line of the slice is not a control heading: "
                         f"{body.splitlines()[0]!r}")
    ctl, title = head.group("ctl"), head.group("title")
    citation = f"NIST SP 800-53 Rev. 5 {ctl}"
    fm = {
        "schema_version": 1,
        "corpus": "federal-reference",
        "jurisdiction": "us",
        "id": doc_id,
        "title": f"{citation} — {title}",
        "doc_type": "federal_instrument",
        "citation": citation,
        "authority_level": "federal",
        "issuing_body": parent["issuing_body"],
        "instrument_kind": "nist_control",
        "version": parent["version"],
        "as_of": parent["as_of"],
        "amended_on": parent["amended_on"],
        "reproduction_basis": parent["reproduction_basis"],
        "superseded_by": None,
        "source_url": parent["source_url"],
        "source_format": "pdf",
        "snapshot_id": parent["id"],
        "retrieved": parent["retrieved"],
        "source_sha256": parent["source_sha256"],
        "status": "current",
        "content_mode": "verbatim",
        "relationships": {"related": [parent["id"]]},
        "maintainer": "@morficflux",
        # Left EMPTY on purpose; a human sets them at PR approval.
        "last_verified": "",
        "verified_by": "",
    }
    head_yaml = yaml.safe_dump(fm, sort_keys=False, allow_unicode=True, width=100).rstrip()
    n = entry["citations"]
    docs = ", ".join(f"{d} ×{c}" for d, c in sorted(
        entry["documents"].items(), key=lambda kv: (-kv[1], kv[0])))
    enh = entry.get("enhancement_citations") or 0
    parts = [f"---\n{head_yaml}\n---\n", "## At a glance\n",
             f"**{citation}** — {title}\n\n"
             f"- Issued by: {parent['issuing_body']}\n"
             f"- Publication: NIST SP 800-53 Rev. 5 — Security and Privacy Controls for "
             f"Information Systems and Organizations ([{parent['id']}](./{parent['id']}.md))\n"
             f"- Version: {parent['version']} (September 2020, includes updates as of "
             f"2020-12-10)\n"
             f"- Text as of: {parent['as_of']}\n"
             f"- Cited by held documents: {n} time{'s' if n != 1 else ''} ({docs})"
             + (f", {enh} of them naming an enhancement of this control" if enh else "") + "\n"
             f"- Reproduction basis: {parent['reproduction_basis']}\n"]
    why = withdrawn_reason(body)
    if why:
        parts.append(
            f"\n> **Withdrawn in Rev. 5.** The source prints this control as withdrawn: "
            f"\"{why}\" It is held because documents held here cite it by name. "
            f"Withdrawal is NIST's, not this corpus's, and is stated in the source, not "
            f"inferred from the control's absence.\n")
    parts.append(
        "\n_NON-AUTHORITATIVE copy of one control, cut from the SP 800-53 Rev. 5 snapshot this "
        "corpus holds. Whether and how this binds a given agency depends on the instrument that "
        "incorporates it — read it at the source URL before relying on it. This copy is the "
        "Rev. 5 text of record, which is not necessarily the text a citing document meant "
        "(a document citing Rev. 4 is not answered by it)._\n")
    changes = release_changes(release, cid)
    if changes:
        parts.append(_release_note(release, changes))
    parts.append("\n## Full text\n\n" + body + "\n")
    return "\n".join(parts)


def build_documents(parent: dict, text: str, cited: dict, release: dict | None):
    """({doc id: markdown}, [cited control ids the catalog does not contain])."""
    docs: dict[str, str] = {}
    missing: list[str] = []
    for entry in cited["controls"]:
        md = build_control(parent, text, entry, release)
        if md is None:
            missing.append(entry["id"])
        else:
            docs[f"{parent['id']}.{entry['id']}"] = md
    return docs, missing


def _frontmatter(path: Path) -> dict:
    return yaml.safe_load(path.read_text(encoding="utf-8").split("---", 2)[1]) or {}


def run(check: bool) -> int:
    parent_path = INSTRUMENTS / f"{PUBLICATION_ID}.md"
    parent = _frontmatter(parent_path)
    text = (SNAPSHOTS / f"{PUBLICATION_ID}.txt").read_text(encoding="utf-8")
    cited = yaml.safe_load(CITED.read_text(encoding="utf-8"))
    release = yaml.safe_load(RELEASE.read_text(encoding="utf-8")) if RELEASE.is_file() else None
    docs, missing = build_documents(parent, text, cited, release)

    problems: list[str] = []
    if missing:
        problems.append(f"cited control(s) the catalog does not contain: {', '.join(missing)} "
                        f"-- the cited-controls file lists a token that is not an SP 800-53 "
                        f"Rev. 5 control; re-run src/scan_cited_controls.py")
    on_disk = {p.stem for p in INSTRUMENTS.glob(f"{PUBLICATION_ID}.*.md")}
    for orphan in sorted(on_disk - set(docs)):
        problems.append(f"ORPHAN {orphan}: a control document with no cited-controls entry")
    related = (parent.get("relationships") or {}).get("related") or []
    if sorted(related) != sorted(docs):
        problems.append(f"{PUBLICATION_ID}: relationships.related does not list exactly its "
                        f"{len(docs)} control documents (re-run ingest_instruments.py "
                        f"--only {PUBLICATION_ID})")

    if check:
        for doc_id, md in sorted(docs.items()):
            path = INSTRUMENTS / f"{doc_id}.md"
            if not path.is_file():
                problems.append(f"MISSING {doc_id}")
            elif path.read_text(encoding="utf-8") != md:
                problems.append(f"STALE {doc_id}")
        if problems:
            print("; ".join(problems[:20]) + (f" … {len(problems) - 20} more"
                                              if len(problems) > 20 else ""), file=sys.stderr)
            print("re-run: python3 src/split_nist_controls.py", file=sys.stderr)
            return 1
        print(f"{len(docs)} NIST control documents match the cited-controls list.")
        return 0

    for orphan in sorted(on_disk - set(docs)):
        print(f"  note: {orphan}.md has no cited-controls entry (left in place)")
    if missing:
        print("error: " + problems[0], file=sys.stderr)
        return 1
    for doc_id, md in docs.items():
        (INSTRUMENTS / f"{doc_id}.md").write_text(md, encoding="utf-8")
    print(f"wrote {len(docs)} control documents")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check", action="store_true")
    return run(ap.parse_args().check)


if __name__ == "__main__":
    sys.exit(main())
