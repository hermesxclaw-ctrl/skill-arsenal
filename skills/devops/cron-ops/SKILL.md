---
name: cron-ops
description: "Use when designing, auditing, or repairing scheduled jobs — resilient cron design: idempotency, health checks, watchdogs, failure recovery."
version: 1.0.0
author: Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [cron, scheduling, watchdogs, reliability, automation]
    related_skills: [bounded-autonomy-loop, graceful-shutdown-patterns, health-check-endpoint-design]
---

# Cron-Ops: Resilient Scheduled Jobs

## Overview

A cron job that fails silently is worse than no job — it's a promise of work that never happened. Cron-ops is the discipline of designing scheduled jobs that survive their own failures: idempotent so reruns are safe, observable so silence means "nothing to do" rather than "dead," and self-healing so a transient error doesn't cascade into a missed week of work.

Every job needs an answer to three questions before it's production-worthy: **What happens if it runs twice? What happens if it dies mid-run? How do I know it's working?**

## When to Use

- Designing a new recurring job (daily digest, hourly sync, weekly backup)
- Auditing an existing job farm for silent failures
- A job that "used to work" and now quietly doesn't
- Any scheduled task where a missed run has a cost

**Don't use for:** one-shot tasks (schedule them as on-demand, not cron), or jobs where the schedule itself is the product (that's a queue, not a cron).

## Design Rules

### 1. Idempotency (the non-negotiable)

A rerun must produce the same result as the first run. This is what makes retries safe.

- **Natural keys, not counters:** key rows/files by content hash or business ID, so re-processing the same item updates rather than duplicates.
- **Upsert, never blind insert:** `INSERT ... ON CONFLICT DO UPDATE` or `mkdir -p` semantics everywhere.
- **State in the artifact, not in memory:** a processing job should be able to resume from its own output ("all files in `out/` with a valid schema" = done).
- **Test it:** run the job twice back-to-back and diff the outputs. Identical = idempotent.

### 2. Observability (silence is a signal)

- **Empty output = success with nothing to do** (for watchdog-style jobs). Distinguish "no work" from "crashed" — non-zero exit or error output must be loud.
- Log one line per run: timestamp, outcome, counts. Keep the log append-only.
- If the platform supports it, deliver on a channel the human actually reads (Telegram/DM for failures, local file for routine).

### 3. Failure Recovery (three layers)

1. **Retry with backoff** for transient failures (network, rate limits): 3 attempts, exponential backoff. Distinguish transient (retry) from permanent (alert) errors.
2. **Watchdog:** a separate job that checks whether the main job actually ran. "Last run timestamp older than 2× the schedule interval" → alert. This catches the case where the scheduler itself dies.
3. **Manual escape hatch:** a documented one-command re-run (`hermes cron run <job>` or the equivalent) so a missed run is recoverable without archaeology.

### 4. Resource Discipline

- Bound every job: timeout on the run, cap on output size, guard on disk usage.
- Don't overlap: a lock file or "already running" check so a slow run and the next scheduled run don't collide.
- Know what the job touches and clean up after itself (temp files, partial downloads).

## Common Pitfalls

1. **No idempotency.** The retry (which WILL happen) duplicates data, and now you have a second bug to clean up. Idempotency first, always.
2. **Silent failure.** Job exits 0 with a stack trace swallowed, or exits non-zero but nobody's watching. If failure isn't loud, it isn't a job — it's a suggestion.
3. **No watchdog.** The scheduler dies, everything looks "healthy" (nothing reports), and the week's work quietly didn't happen. Watchdogs are how you catch the scheduler's death.
4. **Overlapping runs.** A slow job + the next tick = two processes writing the same state. Lock it.
5. **Retrying permanent failures forever.** A 404 is not going to become a 200 on attempt 4. Classify errors; only retry the transient class.
6. **Jobs that assume the machine state.** "The server is running," "the mount is up," "the key is loaded." Jobs should check their own prerequisites or fail loudly, not assume.

## Verification Checklist

- [ ] Job run twice → identical output (idempotency tested)
- [ ] Failure mode is loud (non-zero exit + visible error, or alert delivered)
- [ ] Watchdog checks "did it run" with a real threshold, not just "is it alive"
- [ ] Transient errors retried with backoff; permanent errors alerted
- [ ] No overlapping runs possible (lock or skip-if-running)
- [ ] One-command manual re-run documented and working
- [ ] Resource bounds set (timeout, output cap, cleanup)

## One-Shot Recipe: A Job That Can't Fail Silently

```
JOB: daily data sync
- idempotent: upsert by natural key; rerun-safe by design
- script exits non-zero on ANY failure with the error to stderr
- cron delivers: empty stdout = silent (nothing to report);
  non-empty = the alert; non-zero exit = error alert
- watchdog (separate 1h job): "last sync > 26h ago" -> alert
- manual re-run: documented one-liner, tested
- lock file prevents overlap; 30-min timeout bounds the run
```

If you only remember one thing: **idempotency makes retries safe, observability makes failures visible, and a watchdog makes scheduler death survivable.** Those three convert a cron job from a liability into infrastructure.
