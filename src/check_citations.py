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

import sys

from corpus_toolkit import config as cfg
from corpus_toolkit.mcp.framework import CorpusFramework

CONFIG = "_meta/corpus.yml"


def main() -> int:
    fw = CorpusFramework(cfg.load(CONFIG))
    fails: list[str] = []

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
    import src.citation_schemes as schemes
    from src.federal_ids import candidates
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
