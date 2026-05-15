# Paper-Writing Agents

A [Claude Code plugin](https://docs.anthropic.com/en/docs/claude-code/plugins)
that ships nine specialist agents for academic **paper** writing — tuned to
Fabian's voice and Prof. Chng Eng Siong's supervisor feedback style.

For thesis-length work, use the separate thesis-writing repository.

## Design Philosophy

Nine agents: review, draft, polish, fact-verify, results figures, method
diagrams. The orchestrator decides which to deploy and executes — it does
not run a Q&A loop with the user. Every reviewer report is written to disk
so a fresh Claude Code session can resume after the Opus 5-hour billing
window resets.

- **Voice-first.** Drafting and polishing agents read
  [`skills/academic-writing/SKILL.md`](skills/academic-writing/SKILL.md)
  before writing. The skill encodes Fabian's natural register from real
  thesis revision history.
- **Supervisor-feedback over generic writing review.** The
  `supervisor-feedback` agent simulates Prof. Chng's review style using
  dated verbatim quotes in
  [`skills/supervisor-feedback/grounded-examples.md`](skills/supervisor-feedback/grounded-examples.md).
  This replaces the generic writing-reviewer from upstream.
- **Goal–Problem–Solution rhythm.** Every paper section should follow GPS.
  The plugin itself works the same way: identify the goal, diagnose the
  problem, deploy the right agent to fix it.
- **Fact-grounding over trust.** The drafter is never the authority on a
  number or a citation. The orchestrator builds a closed-set facts ledger
  and citation list from real sources on disk; a deterministic gate
  (`scripts/fact-gate.py`) rejects unknown `\cite` keys and dangling
  evidence tokens; a scoped `fact-verifier` checks each grounded claim
  against the real source — never against the draft that produced it.
  Verification is targeted at flagged claims, not a blanket self-critique
  (which measurably degrades correct prose).
- **Token discipline.** Sonnet for mechanical work, scoped file ranges,
  cached principles file, no multi-variant drafting, no per-edit responses.
- **Session-resumable.** Plan and reviewer findings persist to
  `.paper-writing/session.md` and `.review/*.md`. No external tooling
  needed.

## The Nine Agents

| Agent | Model | Thinking | Role |
|---|---|---|---|
| `supervisor-feedback` | Opus 4.7 | xhigh | Chng-style critical review with verbatim shorthand |
| `structure-reviewer` | Opus 4.7 | high | Narrative flow, terminology, cross-refs, figure-text-caption, GPS |
| `technical-reviewer` | Opus 4.7 | xhigh | Math, methodology, results, citations, bibliography hygiene |
| `fact-verifier` | Opus 4.7 | xhigh | Claim-by-claim grounding against a real source; scoped packets only, never the full draft |
| `latex-layout-auditor` | Sonnet 4.6 | low | Compiled PDF float placement, subfigure alignment |
| `prose-polisher` | Opus 4.7 | high | Applies voice-aware edits to flagged issues |
| `section-drafter` | Opus 4.7 | max | Drafts new LaTeX sections, transitions, captions, abstracts, uses /academic-writing |
| `figure-specialist` | Opus 4.7 | high | Creates/revises Python (matplotlib) **result** figures; halts and requests data instead of inventing numbers when sources are missing |
| `diagram-specialist` | Opus 4.7 | high | Creates/revises **drawio XML** method/pipeline/architecture diagrams; output is editable in draw.io desktop |

## What's Inside

```
paper-writing-agents/
├── .claude-plugin/
│   ├── plugin.json
│   └── marketplace.json
├── agents/
│   ├── supervisor-feedback.md
│   ├── structure-reviewer.md
│   ├── technical-reviewer.md
│   ├── fact-verifier.md
│   ├── latex-layout-auditor.md
│   ├── prose-polisher.md
│   ├── section-drafter.md
│   ├── figure-specialist.md
│   └── diagram-specialist.md
├── scripts/
│   └── fact-gate.py                 # deterministic closed-set / token gate
├── principles/
│   └── academic-writing.md          # 30 principles (A1–F2)
├── skills/
│   ├── SOURCE.md
│   ├── academic/                    # Orchestrator skill (/academic)
│   ├── academic-writing/            # Fabian's voice rules (from Supervisor-Agent)
│   └── supervisor-feedback/         # Chng-style review skill
├── LICENSE
└── README.md
```

## Auto-Triggers

The orchestrator activates without an explicit slash command when Claude
detects paper-writing context:

- editing or naming any `.tex` file under a paper directory
- requests containing "review", "polish", "draft", "abstract", "introduction",
  "related work", "bibliography", "compile" near a paper file
- responding to reviewer comments on a submitted paper

If the project looks like a thesis (e.g. `thesis.tex`,
`\documentclass{thesis}`, `Chapter` files), the orchestrator defers to the
thesis repository instead.

## Manual Invocation

```
/academic review sec_method.tex
/academic polish the abstract
/academic draft a transition from method to experiments
/academic respond to reviewer 2 comments on related work
/academic check bibliography for missing fields and arXiv-to-published updates
/academic generate the cross-backbone EER bar chart from reports/test_results_full_matrix.csv
/academic revise figures/fig3_basin_width.py — make the y-axis log scale and move the legend out
```

### Figures vs Diagrams — two agents, clean split

Every paper has two flavours of figure, and they are handled by two
different agents:

| Type | Agent | Output | When |
|---|---|---|---|
| **Result figure** (bar chart, line plot, heatmap, depth profile — anything that visualises numbers) | `figure-specialist` | `figures/<name>.py` + `.pdf` + `.png` + `.tex` | "plot the EER across backbones", "show the CKA depth profile" |
| **Method / pipeline / architecture diagram** (the conceptual figure that explains *what the method does*) | `diagram-specialist` | `figures/<name>.drawio` + `.drawio.png` + `.pdf` + `.tex` | "Figure 1 explaining the three-lens diagnostic protocol", "the main method figure" |

Both agents enforce the **strict anti-hallucination policy**: they halt
with an `INFO_REQUIRED` block if the underlying data (figure-specialist)
or the concrete labels and palette (diagram-specialist) are missing.
They never invent numbers, layer indices, model names, or claim text.

Both run a render-and-audit loop: generate → read the PNG back inline →
audit against a checklist → fix → re-render. Max 4 iterations.

**Why drawio for method diagrams.** The `diagram-specialist` produces
`.drawio` XML so the user can open the file in **draw.io desktop**
(`/Applications/draw.io.app`) and fine-tune positions, colours, and
labels manually. The agent renders headlessly via the drawio CLI when
available, but the source-of-truth is the editable XML.

**Style library.** Diagram conventions live in
[`principles/figure-style-library.md`](principles/figure-style-library.md) —
palette, font sizes, mirror-pair layout, stage divider, datastore
triplets, continuous-tile sequences, discrete-token chip rows, math
labels via `$$...$$`, the stick-figure speaker icon, and the
pattern-selection cheatsheet. Patterns were extracted from real shipped
figures (the SSL-overview, MERT, and CPC diagrams). The
diagram-specialist reads this library before generating any XML.

The `figure-specialist` is **not** for method diagrams. The
`diagram-specialist` is **not** for results plots. The routing table
in the orchestrator skill enforces the split.

## How To Use (no Claude-Claw needed)

1. Open Claude Code in the paper repo:
   ```bash
   cd /path/to/your/paper
   claude
   ```
2. State the task. The orchestrator announces a one-paragraph plan and
   executes. You do not need to approve a roster of agents.
3. After agents finish, reviewer reports land in `.review/YYYY-MM-DD-<scope>.md`.
   The current plan and pending steps live in `.paper-writing/session.md`.
4. If the Opus billing window cuts you off, restart Claude Code with
   `claude --resume` (continues the same session with cached context). If
   the resume window has also expired, start a new session and say
   "continue". The orchestrator reads `.paper-writing/session.md` and picks
   up at the next pending step.

### Session State Files

| File | Purpose |
|---|---|
| `.paper-writing/session.md` | Current plan, files in scope, step status |
| `.review/YYYY-MM-DD-<scope>.md` | Full reviewer findings (Critical/Important/Minor) |

Both directories are in `.gitignore` by default — they are working state,
not part of the paper.

## Token-Saving Tactics (baked in)

The orchestrator applies these without prompting:

1. **Scope first.** Reads only the named file(s); uses anchored Grep
   patterns instead of full reads when checking a single label class.
2. **Reuse prior reviews.** If `.review/` already covers the scope and the
   file has not changed since (`git log --since=<review-date>`), skips
   redeployment.
3. **Default to one reviewer when adequate.** A "polish this paragraph"
   request is one supervisor-feedback pass, not three reviewers.
4. **Sonnet for mechanical work.** The layout auditor stays on Sonnet.
5. **Batch edits.** Polisher and drafter respond once after applying all
   edits, never per-edit.
6. **Principles file is cached.** Read once per session; agents receive
   principle keys (A1, B7, etc.) in their prompt rather than re-reading
   the file from scratch.
7. **One draft per request.** Section-drafter produces a single draft, not
   three variants.

## Customisation

### Project-level conventions

Add `.claude/CLAUDE.md` to your paper repo with:
- file layout (sections, macros file, build command)
- LaTeX conventions (`\cite` vs `\citet`, `\cref` vs `\ref`)
- any voice notes specific to a co-author or venue

The orchestrator reads it before deploying anything.

### Project-level agents

Drop additional agents into `.claude/agents/` in your paper repo. The
orchestrator auto-discovers them and adds them to the roster for the
session.

## Upstream Skills

The `academic-writing/` and `supervisor-feedback/` skill folders are copied
from `/Users/fabian/Documents/Supervisor-Agent/.claude/skills/`. See
[`skills/SOURCE.md`](skills/SOURCE.md) for the resync protocol.

## Acknowledgments

- Forked from `andrehuang/academic-writing-agents` (v2.1).
- Voice and supervisor-feedback skills derived from real PhD supervision
  with Prof. Chng Eng Siong (NTU).
- GPS rhythm and nugget concept from Michael Black's "Writing a Good
  Scientific Paper".

## License

MIT
