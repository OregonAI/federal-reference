#!/usr/bin/env python3
"""Assert `anchor_sections.anchored_md()` reproduces the anchoring pass a real ingest
applies, so `ingest_instruments.py --check` can compare against it instead of against the
unanchored text a fresh extraction produces.

    python3 src/check_check_anchoring.py

Run in CI (`generated` job), alongside check_issuing_body.py and check_part_edges.py --
same shape: only `ingest_instruments.py --check --only <id>` runs in CI, never the
corpus-wide `--check` (that needs a live eCFR lookup for every part not already
superseded), so this is the hermetic, synthetic-fixture proof for a bug only a live fetch
against an id with no committed snapshot would otherwise surface. `ci.yml`'s own
`--check --only pl-113-128`/`pl-115-224`/`irs-pub-1075` steps run the real path this
fixture-proof stands in for.

WHY THIS EXISTS. #111 reported `pl-113-128`, `pl-115-224` and `irs-pub-1075` as "drift":
`ingest_instruments.py --check` MISMATCHes all three. Measured 2026-10-01: a real
`ingest_instruments.py --only <id>` (write mode, which re-anchors afterward -- see
anchor_sections.process()'s own docstring) reproduces each committed document BYTE FOR
BYTE. The mismatch is `--check`'s own comparison never accounting for the anchoring pass
that always follows a real ingest -- it compares the freshly extracted, UNANCHORED text to
a committed, ANCHORED document, for the three RULES ids anchor_sections.py knows about.
That is a false positive in the checker, not drift in the corpus.

`anchored_md()` is the fix's seam: the exact body+conversion_notes mutation
`anchor_sections.process()` applies when it writes a RULES document, factored out so
`ingest_instruments.py --check` can apply it to its own freshly-built text before
comparing, instead of duplicating (and risking drifting from) process()'s own logic.

REVIEW NOTE (code review on `reingest-drifted-instruments`). The fixture-only checks below
prove `anchored_md()`'s mechanics against a synthetic body, but until this fix they never
touched the thing #111 was actually about: `ingest_instruments.py --check`'s comparison.
Importing `anchor_sections` alone does not exercise `ingest_instruments.py`'s `--check`
branch at all -- reverting the ingester's own hunk (the `anchored_md()` call it makes before
comparing) left this file green. `check_real_rules_ids()` below closes that: for each real
RULES id, it strips the committed document back to what a fresh, UNANCHORED extraction would
read (undo the `### ` prefix anchor_text() adds, drop the `conversion_notes` line
`anchored_md()` writes) and asserts `anchored_md()` rebuilds the committed `instruments/
<doc>.md` byte for byte -- the same hermetic reasoning `ci.yml`'s
`--check --only pl-113-128`/`pl-115-224`/`irs-pub-1075` steps use against the real ingester.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))
from anchor_sections import RULES, anchored_md  # noqa: E402

FIXTURE_MD = (
    "---\n"
    "id: pl-113-128\n"
    "content_mode: verbatim\n"
    "---\n\n"
    "## At a glance\n\nsomething\n\n"
    "## Full text\n\n"
    "SEC. 1. SHORT TITLE.\n\nSome text.\n\nSEC. 2. DEFINITIONS.\n\nMore text.\n"
)


def unanchored(snap_id: str, rule: dict, md: str) -> str:
    """Undo, on a COMMITTED document body, exactly what `anchored_md()` would do to an
    unanchored one -- the inverse of `anchor_text()` plus dropping the `conversion_notes`
    line -- so `anchored_md()` can be asserted to rebuild `md` from its own inverse.
    Only strips a `### ` prefix where the rest of the line still matches `rule["match"]`,
    so a heading-shaped line inside `## At a glance`/`## Curator notes` (never anchored in
    the first place) is left alone.
    """
    out = []
    for line in md.splitlines():
        if line.startswith("### ") and rule["match"](line[len("### "):]):
            out.append(line[len("### "):])
        else:
            out.append(line)
    stripped = "\n".join(out) + ("\n" if md.endswith("\n") else "")
    return re.sub(r"^conversion_notes:.*\n", "", stripped, count=1, flags=re.M)


def check_real_rules_ids(check) -> None:
    """The real assertion #111 needed: for every committed RULES document, `anchored_md()`
    applied to the UNANCHORED text rebuilds the committed, ANCHORED `instruments/<doc>.md`
    byte for byte. This is what `ingest_instruments.py --check` relies on when it calls
    `anchored_md()` on its own freshly extracted text before comparing -- a vacuous
    `assert True` loop over `RULES` ids proves nothing about that comparison, and does not
    even notice if `ingest_instruments.py`'s call to `anchored_md()` is reverted.
    """
    for snap_id, rule in RULES.items():
        doc_path = ROOT / "instruments" / f"{rule['doc']}.md"
        committed = doc_path.read_text(encoding="utf-8")
        rebuilt, n_new, n_total = anchored_md(snap_id, unanchored(snap_id, rule, committed))
        check(f"{snap_id}: anchored_md() rebuilds the committed {rule['doc']}.md "
              "byte for byte from its unanchored text",
              rebuilt == committed,
              f"{n_new} new, {n_total} total anchors; mismatch" if rebuilt != committed
              else "")


def main() -> int:
    fails: list[str] = []

    def check(desc: str, ok: bool, detail: str = "") -> None:
        print(f"  {'ok  ' if ok else 'FAIL'}  {desc}")
        if not ok:
            fails.append(f"{desc}{': ' + detail if detail else ''}")

    new_md, n_new, n_total = anchored_md("pl-113-128", FIXTURE_MD)
    check("anchored_md() prefixes every RULES heading with '### '",
          "### SEC. 1. SHORT TITLE." in new_md and "### SEC. 2. DEFINITIONS." in new_md,
          new_md)
    check("anchored_md() leaves non-heading lines untouched",
          "\n\nSome text.\n\n" in new_md, new_md)
    check("anchored_md() reports how many anchors it inserted", n_new == 2, f"got {n_new}")
    check("anchored_md() reports the running total", n_total == 2, f"got {n_total}")
    check("anchored_md() records a conversion_notes line", "conversion_notes:" in new_md)
    check("anchored_md() leaves the '## At a glance' section alone",
          "## At a glance\n\nsomething" in new_md, new_md)

    again, n_new2, n_total2 = anchored_md("pl-113-128", new_md)
    check("anchored_md() is idempotent -- re-anchoring an anchored body adds nothing new",
          n_new2 == 0, f"got n_new={n_new2}")
    check("anchored_md() is idempotent -- the running total does not change either",
          n_total2 == n_total, f"got n_total={n_total2}, expected {n_total}")
    check("anchored_md() is idempotent -- the text itself does not change either",
          again == new_md)

    check_real_rules_ids(check)

    print()
    if fails:
        print(f"FAILED: {len(fails)} assertion(s): {'; '.join(fails)}", file=sys.stderr)
        return 1
    print("anchored_md() reproduces anchor_sections.process()'s body+note mutation, "
          "idempotently, and rebuilds every committed RULES document byte for byte from "
          "its unanchored text.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
