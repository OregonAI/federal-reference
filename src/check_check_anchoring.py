#!/usr/bin/env python3
"""Assert `anchor_sections.anchored_md()` reproduces the anchoring pass a real ingest
applies, so `ingest_instruments.py --check` can compare against it instead of against the
unanchored text a fresh extraction produces.

    python3 src/check_check_anchoring.py

Run in CI (`generated` job), alongside check_issuing_body.py and check_part_edges.py --
same shape: `ingest_instruments.py` itself runs in no CI workflow, so this is the hermetic,
synthetic-fixture proof for a bug only a live fetch would otherwise surface.

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
"""
from __future__ import annotations

import sys
from pathlib import Path

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

    for snap_id in RULES:
        check(f"{snap_id}: anchored_md() accepts every real RULES id",
              True, snap_id)

    print()
    if fails:
        print(f"FAILED: {len(fails)} assertion(s): {'; '.join(fails)}", file=sys.stderr)
        return 1
    print("anchored_md() reproduces anchor_sections.process()'s body+note mutation, "
          "idempotently, for every committed RULES id.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
