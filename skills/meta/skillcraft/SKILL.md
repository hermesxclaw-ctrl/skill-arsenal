---
name: skillcraft
description: "Use when authoring, editing, or auditing agent skills — the discipline of writing procedural knowledge that actually changes agent behavior."
version: 1.0.0
author: Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [skill-authoring, meta, documentation, procedures]
    related_skills: [bounded-autonomy-loop, systematic-debugging, multi-agent-orchestration]
---

# Skillcraft: Authoring Skills That Change Behavior

## Overview

A skill is not documentation. Documentation describes; a skill **changes behavior**. The test of a good skill is simple: would the agent have done this anyway without reading it? If yes, the skill is noise. If no, it's load-bearing. Skillcraft is the discipline of writing procedural knowledge that survives contact with a fresh session — compact enough to load cheaply, specific enough to override defaults, and structured so the agent knows when it's done.

This skill is the meta-skill: it governs how every other skill in this library is written, and it's the one to reach for when a skill isn't working.

## When to Use

- Writing a new skill from scratch
- Editing a skill that "doesn't work" (the agent ignores it)
- Auditing a skill library for drift, duplication, and sediment
- Teaching someone else how to write skills

**Don't use for:** writing documentation for humans (that's a README), or capturing raw data (that's a file, not a procedure).

## The Skill Test

Before writing anything, answer: **what behavior changes when this skill loads?** If you can't name the behavior, don't write the skill. Every line that doesn't serve that behavior change is a line to cut.

## Writing Rules

### 1. Trigger discipline

- Description must start with "Use when <trigger>" and complete the trigger class within the first ~57 characters (that's the window shown in skill indexes).
- Bad: "This skill contains detailed guidance for debugging." Good: "Use when debugging a failure — 4-phase root-cause method."
- List counter-triggers ("Don't use for:") — knowing when NOT to load a skill is half the trigger.

### 2. Process predictability, not identical output

A skill's job is to make the agent reliably follow the same useful discipline — not to produce byte-identical output. Optimize for: same phases, same verification, same failure handling. The content varies; the method doesn't.

### 3. Information hierarchy

- **Always-needed steps** live in SKILL.md.
- **Branch-specific or bulky reference** lives in `references/`, `templates/`, or `scripts/`, pointed to only when needed.
- If SKILL.md is pushing past ~15K chars, something should move to a reference file.

### 4. Completion criteria on every step

Every ordered step ends with "how do I know it's done?" — checkable, and exhaustive when it matters:
- Weak: "summarize changes." Strong: "every modified file accounted for in the commit list."
- A step without a completion criterion is where agents rush or stall.

### 5. Strong leading words, zero no-op prose

- Use compact concepts the agent already knows: "tight loop," "tracer bullet," "root cause," "fan-out/fan-in." One strong word replaces a paragraph.
- Cut every sentence that wouldn't change behavior if deleted. "Be careful," "be thorough," "use best practices" — all no-ops. Replace with a checkable criterion.
- If a line survives the "would the agent do this anyway?" test, delete it.

### 6. Co-locate rules with the concept

Don't scatter one idea across the file. Definition, caveat, example, and verification for a concept live near each other. One source of truth per meaning; prune duplication relentlessly.

### 7. Sediment is the enemy

Skills rot by accretion: every "one more thing" patch layers advice on advice. When adding a rule, remove the old wording it replaces. A healthy skill gets shorter or sharper over time — never just longer.

## Structure

```
# Title (concept, not task)
## Overview            (what + why, 1-2 paragraphs)
## When to Use         (triggers + counter-triggers)
## Core sections       (numbered steps w/ completion criteria, tables, recipes)
## Common Pitfalls     (numbered: mistake -> fix)
## Verification Checklist (checkbox list of post-action verifications)
## One-Shot Recipes    (optional: named scenario -> concrete command sequence)
```

Frontmatter: `name` (lowercase, hyphens, ≤64 chars), `description` (≤1024 chars, trigger first), `version`, `author`, `license`, `metadata.hermes.tags` + `related_skills`.

## Common Pitfalls

1. **Documentation, not behavior.** Describes the domain instead of changing what the agent does. Kill it with the Skill Test.
2. **Generic advice.** "Be careful with edge cases" — the agent already "knew" that and it didn't help. Replace with a checkable criterion.
3. **No completion criteria.** Steps without "how do I know it's done" let agents rush or stall. Fix the step, not the agent.
4. **Sprawl.** Everything visible all the time = nothing memorable. Push bulk behind references.
5. **Duplication drift.** The same rule in three places decays differently. Keep one source of truth.
6. **Trigger buried.** Description that takes 100 chars to say what it's for — nobody loads it. Front-load the trigger.
7. **Never updating.** A skill written once and never touched rots as the system changes. Audit on use; patch immediately when you find a gap.

## Verification Checklist

- [ ] Skill Test passed: a named behavior change exists, and every line serves it
- [ ] Description starts "Use when..." with trigger complete in ~57 chars
- [ ] Counter-triggers listed ("Don't use for:")
- [ ] Every numbered step has a checkable completion criterion
- [ ] No no-op prose ("be careful," "best practices" without a criterion)
- [ ] Co-located rules; one source of truth per meaning
- [ ] Under ~15K chars; bulky material pushed to references/
- [ ] Pitfalls are mistake→fix pairs, not warnings
- [ ] Verification checklist is exhaustive for the skill's purpose

## One-Shot Recipe: Skill Triage (fixing a skill that doesn't work)

```
1. Re-read it as a stranger. Would you know when to load it, what to do,
   and when you're done? If no, the trigger or criteria are the problem.
2. Apply the Skill Test line-by-line: delete every line that wouldn't
   change behavior. Watch the file shrink 30-50%.
3. Add completion criteria to any step where "done" is ambiguous.
4. Check the description truncation: trigger visible in first 57 chars?
5. Patch, then verify in a fresh session (skill loaders cache at start).
```

A great skill is a contract: load it, follow it, verify it, done. Everything else is a wiki page wearing a costume.
