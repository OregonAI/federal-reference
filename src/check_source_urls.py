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
import sys
import urllib.error
import urllib.request
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
UA = ("OregonAI-corpus-bot/0.1 (+https://github.com/OregonAI/federal-reference; "
      "civic corpus link check)")


def main() -> int:
    urls: dict[str, list[str]] = {}
    for path in sorted((ROOT / "instruments").glob("*.md")):
        fm = yaml.safe_load(path.read_text().split("---", 2)[1])
        if fm.get("source_url"):
            urls.setdefault(fm["source_url"], []).append(fm["id"])

    print(f"  {len(urls)} distinct source_url(s) across {sum(len(v) for v in urls.values())} "
          f"documents")
    bad = []
    for url, ids in sorted(urls.items()):
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
        if code >= 400:
            print(f"  FAIL  {url}  HTTP {code}  ({len(ids)} document(s))")
            bad.append(url)
        else:
            print(f"  ok    HTTP {code}  {url}")

    print()
    if bad:
        print(f"{len(bad)} of our own source_url(s) are unreachable", file=sys.stderr)
        return 1
    print("Every source_url this corpus publishes is reachable.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
