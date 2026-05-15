# Changelog

All notable changes to this plugin.

The format follows [Keep a Changelog](https://keepachangelog.com/),
and this project uses [Semantic Versioning](https://semver.org/).

## [0.3.0] — 2026-05-15

### Added
- **`fact-verifier` agent** (Opus 4.7, xhigh). Breaks the same-context
  rubber-stamp loop: it receives claim-plus-source packets only — never
  the drafted section or the drafter's reasoning — and must quote a
  verbatim supporting span or the claim is `UNSUPPORTED`. Separate
  identity + entailment checks for citations (catches fabricated,
  substituted, and post-rationalised references); numeric verdicts are
  re-checked digit-for-digit in code, not trusted from prose.
- **`scripts/fact-gate.py`** — deterministic, model-free verification
  gate. HARD-fails on `\cite` keys outside the closed `.bib` set and on
  dangling `[F<n>]` evidence tokens; emits SOFT routing warnings for
  factual lines with no evidence token and for leftover
  `MISSING-NUMBERS` / `[CITE:]` placeholders. Pure standard library.
- **Fact-Grounding Pipeline** in the orchestrator (`skills/academic`):
  F1 build a closed-set `facts.md` ledger and `cite-keys.txt` from real
  sources on disk → F2 deploy the drafter re-grounded per section → F3
  deterministic gate → F4 scoped fact-verifier → F5 structural
  accept-or-return that bounces only the failing rows (capped at two
  cycles, then escalates to the user).
- Orchestrator operating principles 7 (no fact without a source) and 8
  (targeted verification, never blanket self-critique).

### Changed
- `section-drafter` now reads the facts ledger and closed-set citation
  list before writing, tags every numeric / comparative / citation
  sentence with an evidence token (`\cite{key}` | `[F<n>]` |
  `MISSING-NUMBERS`), emits a claim manifest for the gate and verifier,
  and is explicitly told not to lift facts from adjacent prose (the
  mechanism by which one invented number became three).
- `prose-polisher` may no longer alter a number, comparison, or evidence
  token even to "fix" it — such rows go back through the pipeline, not
  through the polisher.
- Routing table: drafting / abstract / contributions / results-prose
  paths now run through the Fact-Grounding Pipeline instead of
  `section-drafter` alone.
- Plugin and marketplace descriptions updated from "eight agents" →
  "nine agents" and now mention closed-set fact-grounding.

### Notes
- Targeted verification, not blanket self-critique: the pipeline checks
  only flagged numeric / comparative / citation claims. Prose the
  verifier does not flag is left untouched, by design — forced
  whole-draft self-critique measurably degrades correct writing.

## [0.2.0] — 2026-05-13

### Added
- **`figure-specialist` agent** (Opus 4.7, high thinking) for
  Python-based result figures (matplotlib / seaborn). Strict
  anti-hallucination contract: halts with `INFO_REQUIRED` when the
  underlying CSV / NPY / prior script is not on disk. Produces a
  reproducible `.py` script, vector `.pdf`, preview `.png`, and a
  LaTeX inclusion snippet. Runs a render-and-audit loop.
- **`diagram-specialist` agent** (Opus 4.7, high thinking) for drawio
  XML method / pipeline / architecture diagrams. Output is
  GUI-editable in `/Applications/draw.io.app`. Renders headlessly via
  the installed drawio CLI when available. Anti-hallucination on
  concrete labels; schematic content allowed only when the brief
  authorises it.
- **`principles/figure-style-library.md`** capturing verified diagram
  conventions extracted from three of Fabian's shipped figures
  (SSL-overview, MERT pre-training, CPC). Includes palette, font-size
  table, mirror-pair layout, stage divider, datastore triplets,
  continuous-tile sequences, discrete-token chip rows, `$$...$$` math
  labels, stick-figure speaker icon (base64 preserved verbatim), and a
  pattern-selection cheatsheet.

### Changed
- `structure-reviewer` thinking effort lowered from xhigh to **high**
  (`think hard`). Halves the per-review token cost without losing
  the consistency + logic + cross-refs + GPS coverage.
- Orchestrator routing table updated with seven new patterns
  (figure-create, figure-revise, diagram-create, diagram-revise,
  main-method-figure-by-default, plus the existing review / draft /
  polish paths).
- README restructured around the "figures vs diagrams" split and
  cross-links to the style library.
- Plugin and marketplace descriptions updated from "six agents" →
  "eight agents".

### Removed
- README's self-imposed "max thinking is xhigh" line. The cap is still
  in effect for the agents, but it's an implementation detail, not a
  public spec.

## [0.1.0] — 2026-05-12

### Added
- Initial fork from `andrehuang/academic-writing-agents` v2.1,
  restructured for paper-only workflows (thesis work moves to a
  separate repo).
- Six agents: `supervisor-feedback`, `structure-reviewer`,
  `technical-reviewer`, `latex-layout-auditor`, `prose-polisher`,
  `section-drafter`.
- Voice and supervisor-feedback skills copied in-tree from
  Supervisor-Agent.
- Orchestrator with autonomous (no Q&A) deployment, persistent
  `.paper-writing/session.md` and `.review/` state for billing-window
  resumption.
- Token-saving defaults: scoped reads, prior-review reuse, Sonnet for
  mechanical work, batched edits, principles file cached once per
  session.
