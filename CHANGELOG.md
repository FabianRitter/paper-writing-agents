# Changelog

All notable changes to this plugin.

The format follows [Keep a Changelog](https://keepachangelog.com/),
and this project uses [Semantic Versioning](https://semver.org/).

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
