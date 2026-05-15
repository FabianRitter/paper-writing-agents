#!/usr/bin/env python3
"""
fact-gate.py — deterministic, non-LLM verification gate for the /academic
paper-writing orchestrator.

This script is the *mechanical* half of the fact-grounding pipeline. It does
not judge whether a claim is true; it enforces two things that can be checked
without a model, and therefore cannot be talked around by a drafter agent:

  1. CLOSED-SET CITATIONS (hard). Every \\cite-family key used in the drafted
     .tex must exist in the supplied .bib closed set. A key that is not in the
     .bib is a fabricated reference. This is the single highest-leverage,
     lowest-cost check (see Citation-Grounded Code Comprehension,
     arXiv:2512.12117; BibTeX-hallucination two-stage, arXiv:2604.03159).

  2. FACTS-LEDGER TOKEN RESOLUTION (hard). Every [F<n>] evidence token used
     in the drafted .tex must be defined in the orchestrator-owned facts
     ledger (.paper-writing/facts.md). A dangling [F<n>] means the drafter
     invented an evidence pointer.

It also emits SOFT warnings (never fails the gate) the orchestrator routes to
the fact-verifier agent:

  3. FACTUAL LINES WITHOUT AN EVIDENCE TOKEN. A line carrying a number,
     percentage, or comparison verb but no \\cite / [F<n>] / allowed
     placeholder. These are the lines a verifier must check against a real
     source.

  4. LEFTOVER PLACEHOLDERS. MISSING-NUMBERS / [CITE: ...] markers that are
     legitimate mid-draft but must not survive to submission.

Exit code: 2 if any HARD violation, else 0. SOFT warnings never change the
exit code — they are advisory routing signals, not a reason to reject prose
the drafter is probably right about (deliberate: blanket rejection / blanket
self-critique degrades good text — Snorkel self-critique paradox).

Pure standard library. Python 3.8+.

Usage:
  python3 fact-gate.py --tex sec_method.tex [sec_intro.tex ...] \\
      --bib refs.bib [more.bib | bibdir/] \\
      --facts .paper-writing/facts.md \\
      [--manifest .paper-writing/claims-method.md] [--json]
"""

from __future__ import annotations

import argparse
import glob
import json
import os
import re
import sys

# --- citation commands recognised (natbib + biblatex + base) -----------------
_CITE_CMD = (
    r"cite|citep|citet|citeauthor|citeyear|citeyearpar|citealp|citealt|"
    r"Citep|Citet|Citealp|Citealt|textcite|Textcite|parencite|Parencite|"
    r"autocite|Autocite|footcite|fullcite|citenum|citetext"
)
_CITE_RE = re.compile(
    r"\\(?:" + _CITE_CMD + r")\*?\s*(?:\[[^\]]*\]\s*)*\{([^}]*)\}"
)
_BIB_ENTRY_RE = re.compile(r"@(\w+)\s*\{\s*([^,\s}]+)\s*,", re.IGNORECASE)
_NON_ENTRY_TYPES = {"comment", "string", "preamble", "set", "xdata"}

_FTOKEN_RE = re.compile(r"\[F\d+\]")

# A line is "factual-looking" if it carries a measured quantity or a
# comparative claim. Kept deliberately conservative — SOFT only.
_NUMERIC_RE = re.compile(
    r"(?<![A-Za-z])\d+\.\d+(?![A-Za-z])"          # decimals: 4.77
    r"|\d+\s?%"                                    # percentages: 12%
    r"|\bSOTA\b|\bstate[- ]of[- ]the[- ]art\b"
)
_COMPARATIVE_RE = re.compile(
    r"\b("
    r"outperform\w*|surpass\w*|exceed\w*|beat\w*|"
    r"better than|worse than|higher than|lower than|"
    r"compared (?:to|with)|relative to|"
    r"improv\w*|gain\w*|reduc\w* .{0,30}? by|"
    r"increase\w* .{0,30}? by|decrease\w* .{0,30}? by"
    r")\b",
    re.IGNORECASE,
)
_PLACEHOLDER_RE = re.compile(r"MISSING-NUMBERS?|\[CITE:|\\thesisrevision")

# Lines that are structurally not prose claims.
_SKIP_LINE_RE = re.compile(
    r"^\s*%"                                       # comment line
    r"|^\s*\\(?:label|ref|cref|Cref|eqref|input|include|usepackage|"
    r"documentclass|begin|end|hline|midrule|toprule|bottomrule|"
    r"includegraphics|caption\b)"                  # pure structural commands
)


def _strip_comment(line: str) -> str:
    """Remove a trailing LaTeX comment (unescaped %)."""
    out = []
    prev = ""
    for ch in line:
        if ch == "%" and prev != "\\":
            break
        out.append(ch)
        prev = ch
    return "".join(out)


def _collect_bib_keys(bib_args):
    keys = set()
    files = []
    for a in bib_args:
        if os.path.isdir(a):
            files.extend(sorted(glob.glob(os.path.join(a, "**", "*.bib"),
                                          recursive=True)))
        else:
            files.extend(sorted(glob.glob(a)))
    for f in files:
        try:
            with open(f, encoding="utf-8", errors="replace") as fh:
                txt = fh.read()
        except OSError as e:
            print(f"  ! could not read bib {f}: {e}", file=sys.stderr)
            continue
        for m in _BIB_ENTRY_RE.finditer(txt):
            if m.group(1).lower() in _NON_ENTRY_TYPES:
                continue
            keys.add(m.group(2).strip())
    return keys, files


def _collect_fact_ids(facts_path):
    if not facts_path or not os.path.isfile(facts_path):
        return set(), False
    with open(facts_path, encoding="utf-8", errors="replace") as fh:
        return set(_FTOKEN_RE.findall(fh.read())), True


def _manifest_lines(manifest_path):
    """Line numbers the drafter explicitly declared non-factual / covered.

    The manifest may list `cover: <file>:<line>` entries. Any line so listed
    is treated as drafter-attested and excluded from SOFT coverage warnings.
    """
    covered = set()
    if not manifest_path or not os.path.isfile(manifest_path):
        return covered
    with open(manifest_path, encoding="utf-8", errors="replace") as fh:
        for ln in fh:
            for m in re.finditer(r"([^\s:]+\.tex):(\d+)", ln):
                covered.add((os.path.basename(m.group(1)), int(m.group(2))))
    return covered


def main() -> int:
    ap = argparse.ArgumentParser(description="Deterministic fact gate.")
    ap.add_argument("--tex", nargs="+", required=True)
    ap.add_argument("--bib", nargs="*", default=[])
    ap.add_argument("--facts", default=None)
    ap.add_argument("--manifest", default=None)
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    bib_keys, bib_files = _collect_bib_keys(args.bib)
    fact_ids, facts_present = _collect_fact_ids(args.facts)
    covered = _manifest_lines(args.manifest)

    hard, soft = [], []

    for tex in args.tex:
        if not os.path.isfile(tex):
            hard.append({"file": tex, "line": 0, "kind": "MISSING_FILE",
                         "detail": "drafted .tex not found"})
            continue
        base = os.path.basename(tex)
        with open(tex, encoding="utf-8", errors="replace") as fh:
            raw_lines = fh.readlines()

        for i, raw in enumerate(raw_lines, 1):
            line = _strip_comment(raw).rstrip("\n")
            if not line.strip():
                continue

            # (1) closed-set citation check — HARD
            for m in _CITE_RE.finditer(line):
                for key in (k.strip() for k in m.group(1).split(",")):
                    if not key:
                        continue
                    if bib_files and key not in bib_keys:
                        hard.append({
                            "file": base, "line": i, "kind": "UNKNOWN_CITE",
                            "detail": f"\\cite{{{key}}} not in .bib closed set",
                        })

            # (2) facts-ledger token resolution — HARD
            for tok in _FTOKEN_RE.findall(line):
                if facts_present and tok not in fact_ids:
                    hard.append({
                        "file": base, "line": i, "kind": "DANGLING_FACT",
                        "detail": f"{tok} not defined in facts ledger",
                    })

            # (4) leftover placeholders — SOFT
            if _PLACEHOLDER_RE.search(line):
                soft.append({
                    "file": base, "line": i, "kind": "PLACEHOLDER",
                    "detail": "mid-draft placeholder; must not reach submission",
                })

            # (3) factual line without an evidence token — SOFT
            if _SKIP_LINE_RE.search(line):
                continue
            is_factual = bool(_NUMERIC_RE.search(line) or
                              _COMPARATIVE_RE.search(line))
            if not is_factual:
                continue
            has_token = bool(_CITE_RE.search(line) or _FTOKEN_RE.search(line)
                             or _PLACEHOLDER_RE.search(line))
            if has_token or (base, i) in covered:
                continue
            soft.append({
                "file": base, "line": i, "kind": "UNCITED_CLAIM",
                "detail": "factual/comparative line with no evidence token; "
                          "route to fact-verifier",
                "text": line.strip()[:200],
            })

    if not bib_files:
        soft.append({"file": "-", "line": 0, "kind": "NO_BIB",
                     "detail": "no .bib supplied — closed-set check skipped"})
    if args.facts and not facts_present:
        soft.append({"file": "-", "line": 0, "kind": "NO_FACTS",
                     "detail": "facts ledger not found — [F] check skipped"})

    result = {
        "pass": len(hard) == 0,
        "hard_violations": hard,
        "soft_warnings": soft,
        "bib_keys": len(bib_keys),
        "fact_ids": len(fact_ids),
    }

    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print(f"fact-gate: {'PASS' if result['pass'] else 'FAIL'} "
              f"({len(bib_keys)} bib keys, {len(fact_ids)} fact ids)")
        if hard:
            print(f"\nHARD violations ({len(hard)}) — gate fails, return to "
                  f"drafter with these rows:")
            for v in hard:
                print(f"  ✗ {v['file']}:{v['line']} [{v['kind']}] "
                      f"{v['detail']}")
        if soft:
            print(f"\nSOFT warnings ({len(soft)}) — route to fact-verifier, "
                  f"do NOT auto-reject:")
            for w in soft:
                loc = (f"{w['file']}:{w['line']}"
                       if w["line"] else w["file"])
                print(f"  · {loc} [{w['kind']}] {w['detail']}")
        if not hard and not soft:
            print("  clean.")

    return 2 if hard else 0


if __name__ == "__main__":
    sys.exit(main())
