---
name: multi-agent-orchestration
description: "Use when dispatching parallel subagents or orchestrating multi-worker pipelines — fan-out/fan-in, result merging, and child-claim verification."
version: 1.0.0
author: Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [orchestration, subagents, parallel, delegation, fan-out]
    related_skills: [bounded-autonomy-loop, subagent-delegation-patterns]
---

# Multi-Agent Orchestration

## Overview

The difference between a demo and a system is what happens when workers fail. Multi-agent orchestration is the discipline of running N workers in parallel and recombining their output into something trustworthy: clear task boundaries, isolated contexts, verified results, and a merge step that catches the lies children tell.

Subagent summaries are **self-reports, not verified facts**. A child claiming "uploaded successfully" or "file written" may be wrong, lazy, or hallucinating. The orchestrator's core job is verification — every claim that touches the outside world gets checked before it enters the final result.

## When to Use

- A workload splits cleanly into independent slices (research per-entity, scraping per-domain, builds per-module)
- The work would flood your context with intermediate data if done inline
- Parallel workers meaningfully beat serial (network-bound batches, independent file work)
- You need results from several angles and want them comparable

**Don't use for:** tasks needing shared mutable state, tasks with hidden dependencies between slices, or tiny jobs where dispatch overhead exceeds the work itself.

## The Fan-Out/Fan-In Pattern

### 1. Design the Slice Contract (before dispatch)

Every child needs a **self-contained brief**: goal, context, output format, and a verification handle requirement. A child that doesn't know the conversation must be told everything — language, tone, file paths, expected output shape. Write the brief so a stranger could execute it.

**The verification-handle rule:** for any task with external side effects (uploads, remote writes, publishing), require the child to return a verifiable handle — a URL, an ID, an absolute path — and verify it yourself afterward. A summary saying "done" is not a handle.

### 2. Dispatch

- Batch parallel dispatch when slices are independent (up to the concurrency limit)
- Isolate contexts: each child gets its own context, terminal session, and toolset
- Match toolsets to the task — don't give every child the full arsenal; cheaper children are faster children
- Pin the model per worker type if the platform supports it (draft workers get the cheap model, review workers get the good one)

### 3. Verify Before Merge

For each child result, in order:

1. **Shape check** — did it return the promised structure (fields present, counts right)?
2. **Handle check** — does the URL/path/ID actually resolve? Fetch the URL, stat the file, read back the content. Do not trust the claim.
3. **Content spot-check** — sample the output for hallucination markers: invented citations, confident numbers with no source, boilerplate that ignores the brief.
4. **Failure audit** — if a child failed, did it say *why*? A child that reports failure with a root cause is more useful than one that fakes success.

### 4. Merge

- Combine verified outputs into the final artifact
- Reconcile overlaps: dedupe entities, resolve conflicting claims (keep the one with a source)
- Tag per-item provenance: which worker produced which piece, so problems trace back
- Run the merged artifact through one final validation pass (schema check, link check, count check)

## Common Pitfalls

1. **Trusting self-reports.** The #1 orchestration failure. "Uploaded" without a URL you fetched yourself is unverified. Verify every external side effect.
2. **Slices that aren't actually independent.** Two children writing the same file, or one child's output needed by another. Design the slice boundaries on a dependency graph first.
3. **Skipping the brief.** Children that "know nothing of this conversation" produce garbage when the brief assumes shared context. Write it self-contained, every time.
4. **Unbounded fan-out.** More workers than the platform allows, or more than the target API can take. Respect concurrency limits; queue the rest.
5. **Merging without provenance.** When a bad item appears in the final artifact, you need to know which worker made it. Tag everything.
6. **No retry policy.** A transient failure (network blip, rate limit) kills the batch instead of retrying with backoff. Distinguish transient from permanent failures.

## Verification Checklist

- [ ] Every child brief is self-contained (stranger could execute it)
- [ ] External side effects verified: URL fetched, file stat'd, content read back
- [ ] Every child's output passes shape check before merge
- [ ] Merged artifact passed a final validation pass
- [ ] Per-item provenance recorded (worker → output)
- [ ] Retry policy handled transient failures; permanent failures logged with root cause

## One-Shot Recipe: Parallel Research Batch

```
slices: [entity-a, entity-b, entity-c, ...]   # independent, N at a time
brief: "Research <entity>. Return JSON: {name, culture, type, summary, citations[]}.
        Each citation MUST be a real URL you fetched. Save to out/<entity>.json.
        Respond in English."
dispatch: parallel batch, leaf workers, web+file toolsets only
verify:  for each: file exists? JSON parses? citations[] non-empty?
         spot-check 2 URLs per child actually resolve
merge:   concat into corpus.json, dedupe by name, tag worker_id per item
final:   corpus.json passes count check (len == slices) -> ship
```

Orchestration is 20% dispatching and 80% verification. Spend your effort there.
