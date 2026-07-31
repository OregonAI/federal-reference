#!/usr/bin/env python3
"""Record each manifest source's drift hash. Needs `pdftotext` (poppler-utils).

    python3 src/refresh_source_hashes.py

`corpus-detect-changes` compares a freshly fetched source against `sha256:` in the manifest.
Those shipped EMPTY, so all five sources reported CHANGED on every weekly run -- the only
upstream-content guard this corpus has was a 100% false positive, which is the same as no
guard at all.

Run from the COMMITTED SNAPSHOTS, not a fresh fetch: the recorded hash must describe the
bytes this corpus actually holds, so that a later CHANGED verdict means upstream moved away
from our copy. Re-fetching here would record whatever is upstream right now and mask a real
drift that had already happened.

Separate from the ingester because it needs poppler, which the ingest path does not.
"""
from __future__ import annotations

import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
from ingest_instruments import MANIFEST, ROOT, SNAPSHOTS, write_manifest_hash  # noqa: E402


def main() -> int:
    from corpus_toolkit.sources.changes import content_hash

    manifest = yaml.safe_load(MANIFEST.read_text())
    missing, wrote = [], 0
    for src in manifest["sources"]:
        rid, fmt = src["id"], src["format"]
        raw_path = SNAPSHOTS / f"{rid}.{fmt}"
        if not raw_path.is_file():
            print(f"  SKIP  {rid}: no committed snapshot")
            continue
        try:
            sha = content_hash(raw_path.read_bytes(), fmt)
        except FileNotFoundError as e:
            print(f"  FAIL  {rid}: {e.filename} not installed")
            missing.append(rid)
            continue
        changed = write_manifest_hash(rid, sha)
        wrote += changed
        print(f"  {'wrote' if changed else 'ok   '} {rid}: {sha[:16]}…")

    print()
    if missing:
        print(f"{len(missing)} source(s) need pdftotext: install poppler-utils and re-run",
              file=sys.stderr)
        return 1
    print(f"{wrote} hash(es) updated in {MANIFEST.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
