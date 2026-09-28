#!/usr/bin/env python3
"""Fetch every distinct `source_url` in the corpus and report failures.

    python3 src/check_source_urls.py

WHY THIS EXISTS. ci.yml excludes `instruments/` from the link check, for a good reason: those
documents are verbatim federal text and federal text cites URLs that died years ago. A 2016
publication citing a page that went away in 2019 is an accurate copy, not link rot, and
"fixing" one would mean editing federal text.

The comment justifying that exclusion then claimed our OWN links were still covered -- "every
document's frontmatter source_url is fetched by the drift job in scheduled.yml". They are
not. corpus-detect-changes iterates the five MANIFEST sources and never opens a document.
With 38 section documents added, 28 distinct `source_url`s were being checked by nothing at
all, while a comment said they were checked. This is that check, made real.

Network-dependent, so it belongs in the scheduled job rather than a per-PR gate.
"""
from __future__ import annotations

import gzip
import os
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
UA = ("OregonAI-corpus-bot/0.1 (+https://github.com/OregonAI/federal-reference; "
      "civic corpus link check)")

# Hosts that refuse this check's automated request FROM GITHUB'S RUNNERS, by the exact status
# they refuse with. An entry is a fact about OUR ACCESS, never a claim about upstream: a 403
# cannot tell a block from a withdrawn page, so it is reported as unverifiable, not as fine
# and not as gone. It stays out of the exit code ONLY while the host answers with the
# recorded status; a 404, a timeout or any other code still fails. A 2xx on a runner prints
# `unblock` so the entry is removed rather than outliving the block it records -- a 2xx
# from anywhere else proves nothing about the runners, so it does not.
KNOWN_BLOCKED: dict[str, dict] = {
    "www.cisa.gov": {
        "status": 403,
        "since": "2026-09-14",
        "evidence": "runners: 403 every weekly run since 2026-09-14, 200 on 2026-09-03. "
                    "2026-09-28 from a residential connection, this script's own request "
                    "got 200 and the CPG v1.0.1 PDF byte-identical to "
                    "_meta/snapshots/cisa-cpg.pdf, while curl got 403 -- the block keys "
                    "on network and client, not on the document.",
    },
}


def main() -> int:
    urls: dict[str, list[str]] = {}
    for path in sorted((ROOT / "instruments").glob("*.md")):
        fm = yaml.safe_load(path.read_text().split("---", 2)[1])
        if fm.get("source_url"):
            urls.setdefault(fm["source_url"], []).append(fm["id"])

    print(f"  {len(urls)} distinct source_url(s) across {sum(len(v) for v in urls.values())} "
          f"documents")
    bad, blocked, unblocked = [], [], []
    for url, ids in sorted(urls.items()):
        known = KNOWN_BLOCKED.get(urllib.parse.urlsplit(url).hostname or "")
        # eCFR's /full/ endpoint 406s a request with no Accept-Encoding ("This endpoint
        # requires response compression") -- the same defect ingest_instruments.fetch()
        # was fixed for (#66). Sent here too so this gate reports a real reachability
        # failure, not one this corpus's own request shape manufactures.
        req = urllib.request.Request(
            url, headers={"User-Agent": UA, "Accept-Encoding": "gzip"}, method="GET")
        try:
            with urllib.request.urlopen(req, timeout=90) as r:
                code = r.status
                if r.headers.get("Content-Encoding", "").lower() == "gzip":
                    gzip.decompress(r.read())  # confirms the body actually decodes
        except urllib.error.HTTPError as e:
            code = e.code
        except Exception as e:                       # noqa: BLE001 — reported, not raised
            print(f"  FAIL  {url}\n          {type(e).__name__}: {e}  ({len(ids)} document(s))")
            bad.append(url)
            continue
        if known and code == known["status"]:
            print(f"  BLOCKED  {url}  HTTP {code}, known since {known['since']} -- cannot "
                  f"verify  ({len(ids)} document(s))")
            blocked.append(url)
        elif code >= 400:
            print(f"  FAIL  {url}  HTTP {code}  ({len(ids)} document(s))")
            bad.append(url)
        else:
            print(f"  ok    HTTP {code}  {url}")
            if known and os.environ.get("GITHUB_ACTIONS") == "true":
                unblocked.append(url)

    print()
    if blocked:
        print(f"{len(blocked)} source_url(s) unverifiable: their host blocks this check "
              f"(KNOWN_BLOCKED). Not counted as failures; not confirmed reachable either.")
    for url in unblocked:
        print(f"  unblock: {url} answered 2xx on a runner -- remove its host from "
              f"KNOWN_BLOCKED.")
    if bad:
        print(f"{len(bad)} of our own source_url(s) are unreachable", file=sys.stderr)
        return 1
    if not blocked:
        print("Every source_url this corpus publishes is reachable.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
