# Contributing

All changes via PR with CODEOWNER review. Before merge, the PR checklist
requires: pinned source URL reachable; retrieval date + hash recorded;
version/effective dates transcribed exactly as the source prints them;
`## Full text` verified verbatim (CI-diffed); relationships resolve;
disclaimer present; CHANGELOG updated. Reviewers set `last_verified` /
`verified_by` at approval. Agent-assisted commits carry an
`Assisted-by:` trailer, contiguous with any `Co-Authored-By:` /
`Claude-Session:` trailers (no blank line between them). CI's
`commit-trailers` job (`pull_request` only; see
`src/check_commit_trailers.py`) checks this on the PR's own branch
commits, before merge — not on the commit that lands on `main`. This
repo squash-merges, and GitHub's squash reliably breaks
`git interpret-trailers --parse`'s reading of a trailer block on the
merged commit even when it was written correctly (see #54), so a
gate on `main`'s history would fail every agent-assisted PR
regardless of whether the trailer was written right.
