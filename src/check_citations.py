#!/usr/bin/env python3
"""Assert that citation resolution REFUSES the citations it must refuse.

    python3 src/check_citations.py

Run in CI. Every other check in this repo verifies that documents are well-formed; this one
verifies that the server does not give a confident wrong answer, which is the failure this
corpus is actually exposed to.

The dangerous direction is not "fails to resolve" — that is visible and self-correcting. It
is "resolves to something plausible that is not what was cited": CJIS 6.1 handed back for a
5.9.4 citation, current § 200.303 handed back for a 2019 audit's citation, a public law
handed back for a U.S. Code section. Each of those looks like a correct answer and is one an
agent would act on.

So the assertions below are mostly NEGATIVE — "this must not resolve to that" — and each one
was confirmed to fail when the behaviour it guards is removed. A check that cannot fail is
not a check.
"""
from __future__ import annotations

import pathlib
import sys
import tempfile

from corpus_toolkit import config as cfg
from corpus_toolkit.mcp.framework import CorpusFramework

CONFIG = "_meta/corpus.yml"


def main() -> int:
    fw = CorpusFramework(cfg.load(CONFIG))
    fails: list[str] = []

    # `src.citation_schemes` (this plain import) and `src.federal_ids` are only importable
    # AFTER `CorpusFramework(...)` above has run: this script is invoked as
    # `python3 src/check_citations.py`, which puts only `src/`'s own directory on
    # sys.path[0], not the repo root -- `src` (no `__init__.py`) is not a visible package
    # from inside itself. The repo root reaches sys.path as a side effect of
    # `CorpusFramework.__init__` loading the corpus's citation_module via
    # `corpus_toolkit.plugins.load_module`, which inserts it there. A prior review of this
    # file suggested hoisting these to the top as an ordinary module-level import; verified
    # that breaks the script outright (`ModuleNotFoundError: No module named 'src'`), so the
    # import stays here, done once for the whole function rather than twice.
    import src.citation_schemes as schemes
    from src.federal_ids import candidates

    def check(desc: str, ok: bool, detail: str = "") -> None:
        print(f"  {'ok  ' if ok else 'FAIL'}  {desc}")
        if not ok:
            fails.append(f"{desc}{': ' + detail if detail else ''}")

    def resolve(c: str) -> tuple[list[str], str]:
        r = fw.resolve_citation(c)
        return [m["id"] for m in r.get("matches", [])], (r.get("note") or "")

    # --- the version gap: the single substitution this corpus most needs to refuse -------
    ids, note = resolve("CJIS Security Policy 5.9.4")
    check("CJIS 5.9.4 does not resolve to the 6.1 we hold",
          "cjis-sp-6-1" not in ids, f"resolved to {ids}")
    check("CJIS 5.9.4 explains why", "not held" in note.lower(), note[:80])
    ids, _ = resolve("CJIS Security Policy 6.1")
    check("CJIS 6.1 does resolve", ids == ["cjis-sp-6-1"], f"got {ids}")

    ids, note = resolve("IRS Pub 1075 (Rev. 09-2016)")
    check("IRS rev 09-2016 does not resolve to the 11-2021 we hold",
          "irs-pub-1075" not in ids, f"resolved to {ids}")
    check("IRS wrong revision explains why", "not held" in note.lower(), note[:80])
    ids, _ = resolve("IRS Publication 1075 (Rev. 11-2021)")
    check("IRS matching revision does resolve", ids == ["irs-pub-1075-11-2021"], f"got {ids}")

    # THE REFUSALS ARE ASSERTED OVER A TABLE OF SPELLINGS, not one canonical form. Each was
    # asserted against exactly one string before, so the whole family of ordinary variants --
    # capital "Version", parentheses, commas, "Revision" spelled out -- silently returned the
    # held document while claiming the citation named no version. A refusal that only holds
    # for the spelling you happened to test is not a refusal.
    for c in ("CJIS Security Policy 5.9.4", "CJIS Security Policy, Version 5.9.4",
              "CJIS Security Policy Version 6.0", "CJIS Security Policy (v5.9.4)",
              "CJIS Security Policy v. 5.6", "cjis security policy 5.9.4",
              "CJIS Security Policy — 6.0"):
        ids, note = resolve(c)
        check(f"refused: {c!r}", not ids and "not held" in note.lower(), f"got {ids}")
    for c in ("IRS Pub 1075 (Rev. 09-2016)", "IRS Publication 1075 Revision 09-2016",
              "IRS Pub 1075 (rev. 09-2016)", "IRS Pub 1075 rev 9/2016",
              "irs publication 1075 (Rev. 10-2014)"):
        ids, note = resolve(c)
        check(f"refused: {c!r}", not ids and "not held" in note.lower(), f"got {ids}")

    # --- superseded sections: returned, but never as current law ------------------------
    for sec in ("53", "62"):
        ids, note = resolve(f"2 CFR 200.{sec}")
        check(f"2 CFR 200.{sec} resolves to its superseded document",
              ids == [f"2-cfr-200.{sec}"], f"got {ids}")
        check(f"2 CFR 200.{sec} is labelled NOT current law",
              "not current law" in note.lower() and "removed" in note.lower(), note[:80])

    # --- sections resolve to sections, not to the part ----------------------------------
    ids, _ = resolve("2 CFR 200.303")
    check("2 CFR 200.303 resolves to the section, not the part",
          ids == ["2-cfr-200.303"], f"got {ids}")
    ids, _ = resolve("2 C.F.R. § 200.303")
    check("punctuated form resolves identically", ids == ["2-cfr-200.303"], f"got {ids}")
    ids, _ = resolve("2 CFR 200")
    check("the bare part resolves to the part", ids == ["2-cfr-200"], f"got {ids}")

    # --- a section we hold inside the part, but not as its own document -----------------
    ids, note = resolve("2 CFR 200.200")
    check("an unsplit section returns the part", ids == ["2-cfr-200"], f"got {ids}")
    check("an unsplit section SAYS it returned the part instead",
          "not held as its own document" in note, note[:80])

    # --- a section that does not exist must not be claimed findable ---------------------
    ids, note = resolve("2 CFR 200.9999")
    check("a nonexistent section does not resolve", not ids, f"resolved to {ids}")
    check("a nonexistent section is not described as findable in the part",
          "look for" not in note.lower(), note[:80])

    # --- instruments this corpus does not hold ------------------------------------------
    ids, note = resolve("29 CFR 1910.147")
    check("a different CFR part does not resolve to 2 CFR 200",
          "2-cfr-200" not in ids, f"resolved to {ids}")
    check("the refusal names what IS held instead of a generic miss",
          "2 cfr 200" in note.lower(), note[:120])

    # --- #35: a SECOND held cfr_part must resolve, not just the first ---------------------
    #
    # _cfr_one used to gate on a literal ("2", "200") -- so even a part sitting right there in
    # HELD, fully loaded from its own document's frontmatter, was reported "not held". Proven
    # with a fixture rather than a real second part, per #35's own AC ("must not depend on any
    # queued ingest having landed"): HELD is the module's own dynamic map (see its docstring --
    # "read from the documents, not hard-coded"), so writing directly into it and calling
    # _cfr_one (the per-citation entry point #35 names as the key interface) exercises exactly
    # the seam a real ingest would.
    #
    # PATCHED INTO THE MODULE THE FRAMEWORK ACTUALLY SERVES FROM, not a second import of the
    # same file. `import src.citation_schemes` and the module `CorpusFramework` loaded via
    # `load_module()` are two distinct objects in `sys.modules` -- the loader namespaces the
    # served copy under a corpus-root-hashed alias precisely so two corpora sharing the
    # `src.citations` convention do not collide (see corpus_toolkit/plugins.py). Writing the
    # fixture into the plain import would prove the FUNCTION works and never touch the path a
    # sibling corpus's MCP call actually walks. Confirmed the two are distinct here: patching
    # `src.citation_schemes.HELD` alone left `fw.resolve_citation("6 CFR 37")` refusing.
    served_alias = (
        f"_corpus_{abs(hash(str(fw.config.root))) & 0xffffffff:08x}_"
        f"{fw.config.citation_module.replace('.', '_')}")
    check("the framework's registered citation module is a distinct, locatable object",
          served_alias in sys.modules, f"{served_alias!r} not in sys.modules")
    served = sys.modules[served_alias]

    _saved_held = dict(served.HELD)
    _saved_instruments = served.INSTRUMENTS
    _saved_snapshots = served._SNAPSHOTS
    _saved_consolidations = dict(served._CONSOLIDATIONS)
    tmp = tempfile.TemporaryDirectory()
    try:
        scratch = pathlib.Path(tmp.name)
        scratch_instruments = scratch / "instruments"
        scratch_snapshots = scratch / "snapshots"
        scratch_instruments.mkdir()
        scratch_snapshots.mkdir()

        # A second part's current text: § 37.72 is split out as its own document (case 1),
        # § 37.73 exists in the part but is not split (case 2). § 37.1 never existed (case 3).
        # §§ 37.99 and 37.98 show up only in a dated snapshot -- removed. 37.99 has NO
        # recorded _CONSOLIDATIONS entry at all; 37.98's entry is deliberately given a `date`
        # and `into` but no `scope` -- the exact shape of the review's own repro
        # (`_CONSOLIDATIONS['6-cfr-37'] = {'date':..., 'into':...}`, no `scope`), which
        # fabricated "Subpart A's definitions" for this part before the fix. Both must
        # produce the generic, non-fabricated note (case 4).
        (scratch_instruments / "6-cfr-37.md").write_text(
            "---\nid: 6-cfr-37\n---\n### § 37.72\ntext.\n### § 37.73\ntext.\n",
            encoding="utf-8")
        (scratch_snapshots / "6-cfr-37-2020-01-01.txt").write_text(
            "### § 37.72\ntext.\n### § 37.73\ntext.\n### § 37.99\ntext.\n### § 37.98\ntext.\n",
            encoding="utf-8")
        served._CONSOLIDATIONS["6-cfr-37"] = {"date": "2024-05-01", "into": "37.5"}

        served.INSTRUMENTS = scratch_instruments
        served._SNAPSHOTS = scratch_snapshots
        served._current_section_numbers.cache_clear()
        served._former_section_numbers.cache_clear()

        served.HELD["6-cfr-37"] = {
            "id": "6-cfr-37", "citation": "6 CFR 37", "instrument_kind": "cfr_part",
            "as_of": "2026-01-01",
        }
        served.HELD["6-cfr-37.72"] = {
            "id": "6-cfr-37.72", "citation": "6 CFR 37.72", "instrument_kind": "cfr_section",
            "as_of": "2026-01-01",
        }

        ids, note = served._cfr_one("6", "37", None)
        check("a held second part resolves to its own document, not refused",
              ids == ["6-cfr-37"], f"got {ids}, note={note!r}")
        # NOT also asserted through fw.resolve_citation() here: that path additionally
        # requires self.backend.exists(i) or a graph node for the id (see
        # CorpusFramework.resolve_citation) -- both read the REAL instruments/ and
        # _meta/graph.json, which this fixture deliberately does not touch (per #35's own
        # AC, "must not depend on any queued ingest having landed"). Faking those too would
        # mean mocking framework internals citation_schemes.py does not own, for a check
        # this file's job is not to make. `served` being the module the framework actually
        # imported closes the aliasing gap this block exists to fix; verified above that
        # patching only the plain `src.citation_schemes` import left `_cfr` (as installed in
        # the framework's `_schemes`) unaffected, which is the failure mode this guards.
        ids, note = served._cfr_one("6", "37", "72")
        check("case 1 (split section) resolves to its own document",
              ids == ["6-cfr-37.72"], f"got {ids}, note={note!r}")

        ids, note = served._cfr_one("6", "37", "73")
        check("case 2 (unsplit-but-current) returns the part, labelled as such",
              ids == ["6-cfr-37"] and "not held as its own document" in (note or ""),
              f"got {ids}, note={note!r}")

        ids, note = served._cfr_one("6", "37", "1")
        check("case 3 (never existed) refuses and says so",
              not ids and "there is no" in (note or "").lower(),
              f"got {ids}, note={note!r}")

        ids, note = served._cfr_one("6", "37", "99")
        check("case 4 (removed, no consolidation record at all) is true and NOT fabricated",
              not ids and "is not in the current" in (note or "").lower()
              and "subpart" not in (note or "").lower(),
              f"got {ids}, note={note!r}")

        ids, note = served._cfr_one("6", "37", "98")
        check("case 4b (consolidation record with no `scope`) does not fabricate one either",
              not ids and "is not in the current" in (note or "").lower()
              and "subpart" not in (note or "").lower()
              and "consolidated" not in (note or "").lower(),
              f"got {ids}, note={note!r}")

        ids, note = served._cfr_one("6", "99", None)
        check("an unheld part still refuses",
              not ids, f"got {ids}")
        check("the refusal names the held second part, not just 2 CFR 200",
              "6 cfr 37" in (note or "").lower(), (note or "")[:200])

        # A held-cfr-part id with NO matching instruments/ document -- the index and the
        # instruments directory disagreeing, which is unreachable today (`_held()` only ever
        # adds an id it found a document for) but becomes reachable the moment a document's
        # frontmatter `id` diverges from its filename. Must raise loudly rather than let
        # `_current_section_numbers` return an empty set and have `_cfr_one` report a
        # confident "there is no § 1.5 in 9 CFR 1" about a part it is simultaneously serving
        # -- the same class of false refusal #35 exists to close, one field over.
        served.HELD["9-cfr-1"] = {
            "id": "9-cfr-1", "citation": "9 CFR 1", "instrument_kind": "cfr_part",
            "as_of": "2026-01-01",
        }
        try:
            served._cfr_one("9", "1", "5")
            raised, msg = False, ""
        except RuntimeError as e:
            raised, msg = True, str(e)
        check("index/instruments mismatch raises loudly, not a false 'no such section'",
              raised and "does not exist" in msg, msg[:200] or "did not raise")

        # --- AC5: the resolver's held-part claims agree with the corpus index --------------
        # #35's own AC5: "a check exists that the resolver's 'does not hold' claims agree
        # with the corpus index, so this cannot silently recur. Its absence is what made this
        # bug invisible." Everything above proves ONE synthetic part by hand; this walks
        # EVERY part `_held_cfr_parts()` (itself sourced from HELD, i.e. the index) says is
        # held and asserts each resolves to itself through the served module -- so a
        # regression back to any literal comparison fails here even if a future edit forgets
        # to add a hand-written case for the part it breaks.
        for doc_id, fm in sorted(served._held_cfr_parts().items()):
            t, p = doc_id.split("-cfr-", 1)
            ids, note = served._cfr_one(t, p, None)
            check(f"{doc_id}: resolver agrees with the index that this part is held (AC5)",
                  ids == [doc_id], f"got {ids}, note={note!r}")
    finally:
        served.HELD.clear()
        served.HELD.update(_saved_held)
        served.INSTRUMENTS = _saved_instruments
        served._SNAPSHOTS = _saved_snapshots
        served._CONSOLIDATIONS.clear()
        served._CONSOLIDATIONS.update(_saved_consolidations)
        served._current_section_numbers.cache_clear()
        served._former_section_numbers.cache_clear()
        tmp.cleanup()

    ids, note = resolve("42 U.S.C. 1396")
    check("a U.S. Code section never resolves to a public law",
          not any(i.startswith("pl-") for i in ids), f"resolved to {ids}")
    check("the U.S. Code answer explains the code/enacted distinction",
          "u.s. code" in note.lower(), note[:80])

    ids, _ = resolve("Pub. L. 113-128")
    check("a held public law resolves", ids == ["pl-113-128"], f"got {ids}")
    ids, _ = resolve("Pub. L. 99-474")
    check("an unheld public law does not resolve", not ids, f"resolved to {ids}")

    # --- every id must be DERIVABLE from its own citation -------------------------------
    #
    # A sibling corpus resolves into this one by exact id lookup against corpus-index.json.
    # So if a document's id cannot be produced from the citation a reader would write, that
    # document is unreachable from every other corpus on the platform -- silently, because
    # nothing here fails.
    #
    # That is not hypothetical: the public laws shipped as `pl-113-128-wioa`, whose `-wioa`
    # slug no sibling can guess from "Pub. L. 113-128". This is the general form of that bug,
    # so the next one is caught at the source rather than after it is depended on.
    # src/federal_ids.py is PURE — it derives ids from the citation string alone, knowing
    # nothing about what is held. That non-circularity is the whole point: this corpus's own
    # schemes build their lookup from the held ids and so can always find them, which is
    # precisely why the `-wioa` slug survived until a sibling needed it.
    for doc_id, fm in sorted(schemes.HELD.items()):
        cite = fm.get("citation")
        # A MISSING citation USED TO SKIP THE DOCUMENT SILENTLY -- deleting the field dropped
        # its assertion and the run still reported "all guardrails hold". The guard whose job
        # is catching unreachable ids could be switched off per document by omitting a field.
        check(f"{doc_id} declares a citation", bool(cite), "no `citation:` in frontmatter")
        if not cite:
            continue
        check(f"{doc_id} is derivable from {cite!r} by a sibling",
              doc_id in candidates(cite), f"sibling would derive {candidates(cite)}")

    # THE INVERSE OF DERIVABILITY, and the assertion whose absence let the siblings answer a
    # citation this corpus refuses. Derivability alone is satisfied by an id that is too
    # COARSE: `irs-pub-1075` was derivable from every revision's citation, so a sibling doing
    # exact-id lookup hit the held revision for all of them. A wrong-version citation must
    # not derive any id this corpus holds.
    for c in ("IRS Pub 1075 (Rev. 09-2016)", "IRS Publication 1075 Revision 10-2014",
              "CJIS Security Policy 5.9.4", "CJIS Security Policy 6.0"):
        derived = candidates(c)
        check(f"a sibling cannot reach a held document from {c!r}",
              not any(d in schemes.HELD for d in derived), f"derived {derived}")

    print()
    if fails:
        print(f"FAILED {len(fails)} citation guardrail(s):", file=sys.stderr)
        for f in fails:
            print(f"  - {f}", file=sys.stderr)
        return 1
    print("All citation guardrails hold.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
