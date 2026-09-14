#!/usr/bin/env python3
"""Assert every agent-assisted commit in this PR carries a PARSEABLE Assisted-by: trailer.

    python3 src/check_commit_trailers.py

Run in CI on `pull_request` ONLY (see ci.yml) -- never on `push` to main. #54's own
investigation found that GitHub's squash-merge -- this repo's only merge method that lands
commits on main; `squash_merge_commit_message` is `COMMIT_MESSAGES` per
`gh api repos/OregonAI/federal-reference` -- reliably breaks `git interpret-trailers
--parse`'s reading of the trailer block on the commit that actually lands on main, in two
different ways, confirmed against every agent-assisted squash-merge in this repo's history
at the time of writing (ce4d14f, 3353cf6, c0cbd55, 1990c17, 3b7270f, c1c6f5d -- six for six),
REGARDLESS of whether the branch commit was well-formed:

  * single-commit PRs (ce4d14f, from branch commit a6a9592 -- well-formed and parseable on
    the branch): GitHub inserts a blank line between each trailer line, which breaks the
    contiguous block `git interpret-trailers` requires.
  * multi-commit PRs (3353cf6, from branch tip c64b36a -- also well-formed and parseable on
    the branch): GitHub concatenates the PR's commit bodies with a `---------` separator and
    appends its OWN synthesized `Co-authored-by:` trailer at the true end of the message.
    Only that trailing line is "the trailer block" as far as `git interpret-trailers` is
    concerned -- the real, correctly-formed block earlier in the message sits before a
    non-trailer `---------` line, so it is invisible to the parser.

Meanwhile the two PRs in this repo's history merged via an actual merge commit rather than
squash (#75, #59) preserved every branch commit byte-for-byte -- `Assisted-by:` parses clean
on dcd0d41, bc10bde, and acd8622, all reachable from origin/main today. This is not an
authoring mistake; it is what this repo's squash-merge setting does to a correctly-written
trailer block, every time.

So the only seam that can PASS OR FAIL HONESTLY is the branch commit, before GitHub touches
it -- which is also the only place this can run before the fact rather than after, and the
only place a local `commit-msg` hook (this repo does not ship one) would even have a chance,
since the corruption happens at merge time on GitHub's side, not at commit time. A check
wired to `push: [main]` using a strict trailer-parse would fail on EVERY future
agent-assisted PR, correctly authored or not -- worse than no check, because a persistently
red gate on main stops meaning anything.

WHAT COUNTS AS AGENT-ASSISTED. A commit is treated as agent-assisted if its raw message TEXT
(not the parsed trailers) contains a `Claude-Session:` line or a `Co-authored-by:` line
naming Claude -- the two trailers every agent-assisted commit in this repo's actual history
carries whether or not `Assisted-by:` parses. Text detection is deliberate: a commit whose
own Assisted-by: got mangled the same way ce4d14f's did must still be CAUGHT, not silently
skipped because the very trailer that's missing is also the one a parse-based detector would
have been looking for.

CONTRIBUTING.md says "Agent-assisted commits carry an `Assisted-by:` trailer" with no
qualifier on where. #54's investigation found `Assisted-by:` is the trailer this repo's
agents actually write -- it appears, well-formed, on every branch commit checked from #92
onward, including both fixtures below -- so nothing here proposes replacing it with
`Co-authored-by:`/`Claude-Session:` as "the real" trailer. What needed reconciling was WHERE
the requirement can be checked, not WHICH trailer name is canonical: enforceable on the
branch commit pre-merge, not on the commit that lands on main.
"""
from __future__ import annotations

import os
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# Deliberately TEXT, not a parsed-trailer lookup -- see the module docstring's "WHAT COUNTS
# AS AGENT-ASSISTED" section. Matches "Claude-Session:" anywhere, or a "Co-authored-by:"
# line whose value mentions Claude, case-insensitively, anchored to the start of a line so a
# narrative paragraph that merely mentions "claude" in passing does not trip it.
_AGENT_SIGNAL = re.compile(
    r"^(?:claude-session:|co-authored-by:.*claude)", re.IGNORECASE | re.MULTILINE
)


def parse_trailers(message: str) -> dict[str, list[str]]:
    """Run `git interpret-trailers --parse` and return {lowercased key: [values]}.

    This is the ONLY function in this file that decides what "parses as a trailer" means --
    every other function either produces text for this to parse or reads its result. Do not
    reimplement trailer-block detection anywhere else in this script.
    """
    out = subprocess.run(
        ["git", "interpret-trailers", "--parse"],
        input=message, capture_output=True, text=True, check=True,
    ).stdout
    trailers: dict[str, list[str]] = {}
    for line in out.splitlines():
        if ":" not in line:
            continue
        key, _, value = line.partition(":")
        trailers.setdefault(key.strip().lower(), []).append(value.strip())
    return trailers


def is_agent_assisted(message: str) -> bool:
    """True if the commit's raw text carries an agent-authorship signal (see module doc)."""
    return bool(_AGENT_SIGNAL.search(message))


def missing_assisted_by(message: str) -> bool:
    """True if this commit LOOKS agent-assisted but Assisted-by: does not PARSE as a trailer.

    False for a commit with no agent signal at all -- this function answers "is this commit
    in violation", not "is Assisted-by present", and a plain human/bot commit is never in
    violation of a rule that only binds agent-assisted commits.
    """
    if not is_agent_assisted(message):
        return False
    return "assisted-by" not in parse_trailers(message)


def commits_in_range(base: str, head: str) -> list[tuple[str, str]]:
    """[(sha, full message)] for every non-merge commit reachable from head but not base."""
    out = subprocess.run(
        ["git", "log", "--no-merges", "--format=%H", f"{base}..{head}"],
        cwd=ROOT, capture_output=True, text=True, check=True,
    ).stdout
    shas = [s for s in out.splitlines() if s]
    result = []
    for sha in shas:
        msg = subprocess.run(
            ["git", "log", "-1", "--format=%B", sha],
            cwd=ROOT, capture_output=True, text=True, check=True,
        ).stdout
        result.append((sha, msg))
    return result


# --- fixtures: real commit-message tails from origin/main and its PR branches, extracted
# programmatically (never hand-retyped) during #54's investigation. Each tuple is
# (sha, message-tail). The two SQUASH_* fixtures are the ACTUAL corrupted text sitting on
# origin/main right now; the two BRANCH_* fixtures are the tip of the same two PRs' branches
# before GitHub squashed them -- proof the corruption is GitHub's, not the author's.

SQUASH_SINGLE_COMMIT_CORRUPTED = (
    "ce4d14febb1507887c485d07589e440f9ac11f4e",
    "range/suffix boundary itself are pinned in check_citations.py,\n"
    "confirmed to fail (9 assertions) when the fix is reverted.\n\n"
    "Assisted-by: Claude Opus 5 <noreply@anthropic.com>\n\n"
    "Claude-Session: https://claude.ai/code/session_01X4yjPGpFa22asqjQqA3RLe\n\n"
    "Co-authored-by: Claude Opus 5 <noreply@anthropic.com>\n",
)

SQUASH_MULTI_COMMIT_CORRUPTED = (
    "3353cf6b130bcca21c541dd7af388714ca15a7dd",
    "\nAssisted-by: Claude Opus 5 <noreply@anthropic.com>\n"
    "Claude-Session: https://claude.ai/code/session_01X4yjPGpFa22asqjQqA3RLe\n"
    "Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>\n\n"
    "---------\n\n"
    "Co-authored-by: Claude Opus 5 <noreply@anthropic.com>\n",
)

BRANCH_SINGLE_COMMIT_WELL_FORMED = (
    "a6a95925d5c989b46c1e9d5a325e1f38a5e44c84",
    "range/suffix boundary itself are pinned in check_citations.py,\n"
    "confirmed to fail (9 assertions) when the fix is reverted.\n\n"
    "Assisted-by: Claude Opus 5 <noreply@anthropic.com>\n"
    "Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>\n"
    "Claude-Session: https://claude.ai/code/session_01X4yjPGpFa22asqjQqA3RLe\n\n",
)

BRANCH_MULTI_COMMIT_WELL_FORMED = (
    "c64b36acdf2d66f213cfe18eee1dcc0a235a62ce",
    "reverted, before this commit. The `links` (lychee) job was not run locally --\n"
    "`instruments/` is already excluded and no new non-instrument URL was added.\n\n"
    "Assisted-by: Claude Opus 5 <noreply@anthropic.com>\n"
    "Claude-Session: https://claude.ai/code/session_01X4yjPGpFa22asqjQqA3RLe\n"
    "Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>\n\n",
)

HUMAN_OR_BOT_COMMIT_NO_SIGNAL = (
    "7fcb84c84148a558b238bfe8fd4286ae4c453087",
    "chore: move the corpus-toolkit serving pin to v1.36.1 (#91)\n\n"
    "Co-authored-by: corpus-bot <actions@github.com>\n",
)


def main() -> int:
    fails: list[str] = []

    def check(desc: str, ok: bool, detail: str = "") -> None:
        print(f"  {'ok  ' if ok else 'FAIL'}  {desc}")
        if not ok:
            fails.append(f"{desc}{': ' + detail if detail else ''}")

    # --- hermetic proof: the two real corrupted commits on main are CAUGHT ------------------
    for name, (sha, text) in (
        ("SQUASH_SINGLE_COMMIT_CORRUPTED", SQUASH_SINGLE_COMMIT_CORRUPTED),
        ("SQUASH_MULTI_COMMIT_CORRUPTED", SQUASH_MULTI_COMMIT_CORRUPTED),
    ):
        check(f"{name} ({sha[:7]}): looks agent-assisted", is_agent_assisted(text))
        check(f"{name} ({sha[:7]}): Assisted-by does not parse (the real defect)",
              "assisted-by" not in parse_trailers(text))
        check(f"{name} ({sha[:7]}): missing_assisted_by() flags it -- the check CAN fail",
              missing_assisted_by(text))

    # --- hermetic proof: the two real branch-side commits the corrupted ones came from PASS -
    for name, (sha, text) in (
        ("BRANCH_SINGLE_COMMIT_WELL_FORMED", BRANCH_SINGLE_COMMIT_WELL_FORMED),
        ("BRANCH_MULTI_COMMIT_WELL_FORMED", BRANCH_MULTI_COMMIT_WELL_FORMED),
    ):
        check(f"{name} ({sha[:7]}): looks agent-assisted", is_agent_assisted(text))
        check(f"{name} ({sha[:7]}): Assisted-by parses clean, same author intent as its "
              "squashed descendant",
              "assisted-by" in parse_trailers(text))
        check(f"{name} ({sha[:7]}): missing_assisted_by() does not flag it",
              not missing_assisted_by(text))

    # --- a commit with no agent signal at all is never in violation -------------------------
    sha, text = HUMAN_OR_BOT_COMMIT_NO_SIGNAL
    check(f"HUMAN_OR_BOT_COMMIT_NO_SIGNAL ({sha[:7]}): not agent-assisted",
          not is_agent_assisted(text))
    check(f"HUMAN_OR_BOT_COMMIT_NO_SIGNAL ({sha[:7]}): missing_assisted_by() does not flag it",
          not missing_assisted_by(text))

    # --- the live check: every agent-assisted commit actually introduced by this PR ---------
    base = os.environ.get("TRAILER_CHECK_BASE_SHA")
    head = os.environ.get("TRAILER_CHECK_HEAD_SHA", "HEAD")
    if base:
        commits = commits_in_range(base, head)
        print(f"\n  Checking {len(commits)} commit(s) in {base[:7]}..{head[:7] if len(head) > 7 else head}:")
        for sha, msg in commits:
            subject = msg.splitlines()[0] if msg.splitlines() else "(empty)"
            if missing_assisted_by(msg):
                check(f"{sha[:7]} {subject}: carries Assisted-by:", False,
                      "agent-assisted (Claude-Session: or Co-authored-by: naming Claude) "
                      "but Assisted-by: does not parse as a trailer")
            else:
                check(f"{sha[:7]} {subject}: not in violation", True)
    else:
        print("\n  TRAILER_CHECK_BASE_SHA not set -- skipping the live PR-range check "
              "(expected for a local run; ci.yml sets it from the PR's base sha).")

    print()
    if fails:
        print(f"FAILED {len(fails)} check(s):", file=sys.stderr)
        for f in fails:
            print(f"  - {f}", file=sys.stderr)
        return 1
    print("Every agent-assisted commit in scope carries a parseable Assisted-by: trailer.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
