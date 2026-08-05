---
name: bounded-autonomy-loop
description: "Use when operating autonomously for a bounded duration with checkpointed state, heartbeat reporting, and a hard stop contract."
version: 1.0.0
author: Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [autonomy, loops, checkpoints, state, reliability]
    related_skills: [multi-agent-orchestration, state-persistence, graceful-shutdown-patterns]
---

# Bounded Autonomy Loop

## Overview

Running an agent unattended is a reliability problem before it is a cleverness problem. A bounded autonomy loop is a self-contained execution contract: a defined time budget, a checkpointed state file so progress survives crashes, a heartbeat so anyone watching knows it is alive, and a hard stop so it never spins forever. This skill is the distilled pattern for any "work while I'm gone" task — research batches, site builds, data migrations, multi-hour job hunts.

The loop turns "go do a thing" into "run this cycle N times, save state after every cycle, report every M minutes, stop when budget or goal is hit — whichever comes first."

## When to Use

- User says "keep going," "work until X," "run overnight," or any bounded unattended mission
- Recurring batch work that must survive process restarts (research pipelines, archive builds)
- Any task where losing progress on a crash would be expensive (long migrations, large scrapes)
- Cron-style work that needs more intelligence than a fixed schedule allows

**Don't use for:** single-shot tasks (call the tool once), interactive work the user is watching, or anything requiring user decisions mid-flight (those need a pause-and-ask contract instead).

## The Loop Contract

```
while budget_remaining and not goal_met and not stop_requested:
    do_one_unit_of_work()          # one atomic, completable slice
    persist_state()                # write state AFTER each unit, before next
    heartbeat()                    # emit liveness signal
    check_budget()                 # hard stop when exhausted
```

### The Three State Files

1. **State file** (`state.json`) — what has been done, what's next, cursor position. Written after EVERY unit. This is the crash-recovery contract: on restart, read state, resume from cursor. Never derive "what's done" from memory; derive it from the file.
2. **Log file** (`run.log`) — append-only narrative of what happened each cycle. One line per unit minimum. This is the post-mortem evidence.
3. **Heartbeat** — a timestamped liveness marker (a line in the log, a file mtime, or a status endpoint). If the heartbeat stops advancing, the loop is dead.

### The Hard Stop Contract

- **Budget**: a wall-clock deadline (not "number of steps" — steps are unreliable). Check it before each unit, not after: `if time_elapsed + unit_estimate > deadline: stop`.
- **Goal**: an explicit, checkable completion predicate. "Done" means the predicate returns true, not "I feel like it's done."
- **Stop request**: a sentinel file the operator can drop (`STOP`) that the loop checks each cycle. This is how a human kills a runaway loop without attaching to the process.

## Steps

1. **Write the contract first.** Before any work: state file path, log path, deadline (ISO timestamp), completion predicate, unit-of-work definition. Put it in a `MISSION.md` at the work root. Completion criterion: the mission file exists and a fresh session could resume from it with zero prior knowledge.
2. **Make units atomic and small.** A unit is the smallest slice that leaves the system in a valid state if interrupted mid-slice. For a research batch: one entity per unit. For a migration: one table. If a unit takes more than ~15 minutes, split it.
3. **Persist state after every unit.** Write the cursor, counts, and next action to `state.json` before starting the next unit. Completion criterion: kill the process mid-run, restart, and the loop resumes at the exact right place — test this once deliberately.
4. **Emit a heartbeat each cycle.** Timestamped line in the log. If the operator checks liveness, they can see "cycle 47 at 14:03, 38 units done, 12 to go."
5. **Check the budget before each unit.** Hard stop when elapsed + estimate > deadline. On stop: write a final state line, flush logs, exit cleanly with a summary.
6. **Handle failure as a retry, not a crash.** Per-unit retry with backoff (3 attempts), then mark the unit as failed in state and continue — never let one poison unit kill the whole loop. Record the failure in the log.
7. **End with a report.** Final message must include: units completed, units failed, time used, state file location, and the exact command to resume. No "I would have done more" — just the numbers.

## Common Pitfalls

1. **Budget in steps, not time.** Steps are unreliable (each varies wildly). Always budget wall-clock time.
2. **State written before, not after, the unit.** If you persist after the unit and crash during it, the unit runs twice on resume. Persist the cursor before starting the next unit.
3. **Goal predicate too vague.** "Finish the research" fails. "All 250 slugs have a dossier in `out/` with ≥3 citations" passes. Write the predicate so a different agent could check it.
4. **No stop sentinel.** A loop without a kill switch is a liability. The `STOP` file costs nothing and saves everything.
5. **Silent death.** If the loop crashes and no heartbeat was logged, nobody knows. The heartbeat is not optional.
6. **Poison unit kills the batch.** One bad URL, one malformed record — isolate it, log it, move on. The loop's job is throughput, not perfection.

## Verification Checklist

- [ ] `MISSION.md` exists with deadline, completion predicate, unit definition, state/log paths
- [ ] A deliberate mid-run kill + restart resumed at the correct cursor (tested once)
- [ ] Heartbeat timestamp advances each cycle
- [ ] STOP sentinel file halts the loop within one cycle
- [ ] Failed units are recorded and skipped, not fatal
- [ ] Final report has units done, failed, time used, resume command

## One-Shot Recipe: Overnight Batch

```bash
# Mission root
mkdir -p ~/work/batch && cd ~/work/batch
# Contract
cat > MISSION.md <<'EOF'
deadline: 2026-08-06T06:00:00-07:00
completion: every slug in input/slugs.txt has output/<slug>.md
unit: one slug (fetch -> draft -> save)
state: state.json | log: run.log | stop: STOP
EOF
# Loop (pseudocode — adapt to your tools)
while ! goal_met && now < deadline && ! stop_file: 
    slug = next_from_state()
    try: process(slug); mark_done(slug)
    except: retry(3); mark_failed(slug)
    persist_state(); log_cycle()
report()
```

The same skeleton scales from 20 entities to 20,000 — only the unit definition changes.
