---
name: systematic-debugging
description: "Use when debugging a failure — 4-phase root-cause method: reproduce, isolate, instrument, fix-with-evidence. No guessing."
version: 1.0.0
author: Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [debugging, root-cause, reproduction, testing]
    related_skills: [test-driven-development, requesting-code-review]
---

# Systematic Debugging

## Overview

Debugging by intuition is how you fix one bug and create two. Systematic debugging is a 4-phase method that treats every failure as a hypothesis to be tested, not a memory to be searched: **reproduce → isolate → instrument → fix with evidence**. The method buys you three things: you fix the actual root cause instead of a symptom, you don't reintroduce the bug (the regression test proves it), and you can hand the investigation to anyone at any point because it's documented.

The core rule: **never fix what you haven't reproduced, and never claim fixed what you haven't verified.**

## When to Use

- Any bug, crash, failing test, or "it worked before" regression
- Investigating a failure reported by someone else (you have no direct observation)
- Intermittent failures (the method's structure is what makes these tractable)
- Before escalating: "I tried everything" is not a debugging strategy

**Don't use for:** one-line typos you can see at a glance (just fix them), or designing features (that's not debugging).

## Phase 1 — Reproduce

The bug is not real until you can make it happen on demand.

1. Get the exact input, environment, and steps from the reporter. "It broke" is not an input; "click X, paste Y, see Z on Windows 10 with this config" is.
2. Reproduce it yourself in the smallest possible case. Strip away everything not needed to trigger it. If you can't reproduce, you don't have a bug — you have a rumor.
3. **Record the reproduction as a command or test.** If it can't be scripted, it can't be verified later. Completion criterion: a one-liner that reliably triggers the failure.

## Phase 2 — Isolate

Find the smallest component whose change causes the failure.

1. **Binary search the moving parts.** Comment out halves, toggle features, swap inputs — find the minimal delta between "works" and "breaks."
2. Check the boundary conditions: empty input, max input, unicode, timestamps, timezones, first-run vs subsequent.
3. **Read the actual code path**, not the one you remember. Trace the failing value from input to symptom. Look at the file on disk — the code you think is there may not be what runs (stale build, cached module, wrong branch).
4. Form a hypothesis with a *prediction*: "if X is the cause, then changing X will change the symptom in way Y."

Completion criterion: you can point at one component and say "this is where the failure originates," with the trace to back it.

## Phase 3 — Instrument

Prove the hypothesis with evidence, not vibes.

1. Add the minimal logging/print/trace that shows the actual values flowing through the suspect path. Don't guess what the value is — print it.
2. Check the **inputs to the suspect component**, not just the output. Garbage in, garbage out: the component may be innocent and the caller may be poisoning it.
3. Test the hypothesis's prediction: apply the change you predicted would alter the symptom and confirm it does.
4. Look for the same flaw in **sibling call paths** — if the bug is "caller forgets to null-check," the same callers have the same bug. Fix the class, not the instance.

Completion criterion: the log output confirms the mechanism end-to-end, and you can state the root cause in one sentence: "component X fails because input Y is Z when it should be W."

## Phase 4 — Fix with Evidence

1. **Write the failing test first** (or convert your reproduction into a regression test). Watch it fail — that proves it tests the bug.
2. Apply the minimal fix. No drive-by refactors — the fix is the fix.
3. Run the test; watch it pass. Run the surrounding suite; confirm nothing else broke.
4. Re-run the original reproduction one-liner on the fixed code — the exact thing that failed before must now pass.
5. Document the root cause and fix where the next person will look (commit message, code comment, or runbook).

## Common Pitfalls

1. **Fixing the symptom.** The error message is not the bug. "File not found" usually means a path bug upstream; "null reference" means a missing guard earlier. Trace to the root.
2. **The memory bug.** "I remember this code does X" — read the file. Stale builds, cached bytecode, and wrong branches are silent liars.
3. **Skipping reproduction.** Fixing an unreproduced bug is prayer. If you can't reproduce, you can't verify, and you'll "fix" it three times.
4. **One fix, zero regression test.** The bug will come back with its friends. The test is the only thing that makes the fix permanent.
5. **Tunnel vision.** After three failed attempts on the same component, stop and widen: is the input even reaching it? Is the deployment current? Is the assumption about the environment wrong?
6. **Fixing the class vs the instance.** If a null-check was missing in one place, it's missing in its siblings. Fix all of them or the bug just moves.

## Verification Checklist

- [ ] Reproduction is scripted (command or test) and reliable
- [ ] Root cause stated in one sentence with evidence from instrumentation
- [ ] Regression test written and observed failing before the fix
- [ ] Minimal fix applied; test passes; surrounding suite green
- [ ] Original reproduction re-run on fixed code and passes
- [ ] Sibling call paths checked for the same flaw
- [ ] Root cause + fix documented for the next person

## One-Shot Recipe: Intermittent Failure

```
1. REPRODUCE: collect the failing input from the reporter, run it 10x, 
   confirm it fails ≥1x. Script it: `while true; do <cmd>; done` with a fail-trap.
2. ISOLATE: binary-search the inputs/features. Find the minimal failing case.
3. INSTRUMENT: add value-printing at each hop of the suspect path. Run until
   it fails; read the actual values. Predict, then confirm.
4. FIX: write regression test -> watch it fail -> minimal fix -> test passes
   -> original repro passes -> check sibling paths -> document.
```

The 4 phases are not optional flavor; they are a dependency chain. Skipping reproduce makes isolate guesswork, and skipping isolate makes fix a lottery.
