#!/usr/bin/env python3
"""Assert every in-force cfr_part's own `relationships.related` lists its own split sections.

    python3 src/check_part_edges.py

Run in CI (`generated` job, alongside check_section_split.py).

WHY THIS EXISTS (#104). `graph_neighbors(<part-id>)`/`authority_chain` walk a document's own
`relationships.related`, and the graph is outbound-only (see ingest_instruments.build()'s own
comment on this) -- so a section links back to its part, but the part only links forward to
its sections if its OWN frontmatter carries those edges. `split_cfr_sections.py --check`
verifies the SECTION side of that pair (every split section's own `related: [<part_id>]`);
nothing verified the reverse, so a part whose `cited-sections` file grew after its last
`ingest_instruments.py` run quietly became a graph dead end reachable only downward. #104's
survey found 9 real parts in exactly that state (112 missing edges total), all from the
2026-09-01 mass ingest -- the same drift `34-cfr-99` had before this session's #26/#27 fix.

THE SUPERSEDED-PART CARVE-OUT IS DELIBERATE, NOT A GAP. `ingest_instruments.build()` points a
WHOLLY SUPERSEDED part's `related` at `[superseded_by]` instead of its own (equally superseded)
split sections -- a reader at a gone part needs to be pointed at where the live text moved to,
not into a dead end of its own history. 45 CFR 75 is exactly this case: `cited_section_ids()`
names 7 sections `related` correctly does NOT include, and that is #104's own stated logic for
a superseded part, not a 10th part this gate missed. The synthetic fixture below proves this
gate does not flag that shape; the real-data loop below skips every `status: superseded`
document for the same reason #104's own reproduce script did.

This is the real-data half of the proof (same shape as `split_cfr_sections.py --check`, which
also walks the real committed corpus rather than only synthetic fixtures) plus one synthetic
fixture for the superseded carve-out, which the real corpus holds only one example of (45 CFR
75) and this gate must not rely on staying true by accident.
"""
from __future__ import annotations

import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
from ingest_instruments import cited_section_ids, merge_relationships  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
INSTRUMENTS = ROOT / "instruments"


def missing_edges(related: list[str], cited: list[str]) -> list[str]:
    """Ids `cited` names that `related` does not -- order-independent, dedupe-tolerant."""
    return sorted(set(cited) - set(related or []))


def main() -> int:
    fails: list[str] = []

    def check(desc: str, ok: bool, detail: str = "") -> None:
        print(f"  {'ok  ' if ok else 'FAIL'}  {desc}")
        if not ok:
            fails.append(f"{desc}{': ' + detail if detail else ''}")

    # --- synthetic: a SUPERSEDED part must not be required to list its own split sections --
    # mirrors ingest_instruments.build()'s own auto-derivation for a superseded cfr_part:
    # `related` is `[superseded_by]`, never `cited_section_ids(rid)`.
    auto = merge_relationships({"related": ["2-cfr-200"]}, {})
    check("a superseded part's auto-derived edge points at superseded_by, not its own "
          "sections", auto == {"related": ["2-cfr-200"]}, repr(auto))

    # --- synthetic: an in-force part missing a real edge IS caught -------------------------
    missing = missing_edges(related=["7-cfr-280.1", "7-cfr-280.2"],
                             cited=["7-cfr-280.1", "7-cfr-280.2", "7-cfr-280.3"])
    check("a part missing one of its cited sections is flagged",
          missing == ["7-cfr-280.3"], repr(missing))

    # --- synthetic: a part that already lists every cited section is NOT flagged -----------
    missing = missing_edges(related=["7-cfr-280.1", "7-cfr-280.2"],
                             cited=["7-cfr-280.1", "7-cfr-280.2"])
    check("a part listing every cited section is not flagged", missing == [], repr(missing))

    # --- real data: every non-superseded cfr_part's related is a superset of its own
    # cited_section_ids() -- the actual #104 claim, against the real committed corpus
    checked = 0
    for path in sorted(INSTRUMENTS.glob("*.md")):
        fm = yaml.safe_load(path.read_text(encoding="utf-8").split("---", 2)[1])
        if fm.get("instrument_kind") != "cfr_part" or fm.get("status") == "superseded":
            continue
        checked += 1
        rid = fm["id"]
        related = (fm.get("relationships") or {}).get("related") or []
        missing = missing_edges(related, cited_section_ids(rid))
        check(f"{rid}: relationships.related lists every one of its own split sections",
              not missing, f"missing {missing}")

    check(f"at least one real cfr_part was checked (not a vacuously empty loop)", checked > 0,
          f"checked {checked}")

    print()
    if fails:
        print(f"FAILED: {len(fails)} assertion(s): {'; '.join(fails)}", file=sys.stderr)
        return 1
    print(f"every one of {checked} non-superseded cfr_part documents lists its own split "
          "sections; a superseded part is correctly exempted.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
