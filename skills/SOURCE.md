# Skill Provenance

The `academic-writing/` and `supervisor-feedback/` skill folders in this
directory were **copied** (not symlinked, not submoduled) from:

```
/Users/fabian/Documents/Supervisor-Agent/.claude/skills/academic-writing/
/Users/fabian/Documents/Supervisor-Agent/.claude/skills/supervisor-feedback/
```

The copy was made on 2026-05-12.

## Why copied, not synced

The Supervisor-Agent repo is the canonical owner of the voice and feedback
rules. This plugin embeds a frozen snapshot so the paper-writing workflow is
self-contained and reproducible.

## Resync protocol

When the upstream skills change in a way you want here:

```bash
rsync -av --delete \
  /Users/fabian/Documents/Supervisor-Agent/.claude/skills/academic-writing/ \
  /Users/fabian/Documents/paper-writing-agents/skills/academic-writing/

rsync -av --delete \
  /Users/fabian/Documents/Supervisor-Agent/.claude/skills/supervisor-feedback/ \
  /Users/fabian/Documents/paper-writing-agents/skills/supervisor-feedback/
```

Then commit with a message noting the sync date.

## What lives where

| Skill | Purpose in this repo |
|---|---|
| `academic-writing/` | Voice profile (Section 10 of SKILL.md) and prose rules. Read by every drafting / polishing agent so output matches Fabian's natural register. |
| `supervisor-feedback/` | Chng Eng Siong review style. Drives the `supervisor-feedback` agent. Contains `grounded-examples.md` with dated verbatim ES quotes. |
| `academic/` | Orchestrator skill specific to this plugin (not from Supervisor-Agent). |
