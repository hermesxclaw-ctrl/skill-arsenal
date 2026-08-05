---
name: service-hardening
description: "Use when shipping or operating a server/service — production hardening: graceful shutdown, retry patterns, health endpoints, error taxonomy."
version: 1.0.0
author: Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [hardening, production, health-checks, retries, shutdown]
    related_skills: [cron-ops, health-check-endpoint-design, retry-logic-patterns, graceful-shutdown-patterns]
---

# Service Hardening

## Overview

A service that works on your machine and a service that survives in production are different artifacts. Service hardening is the gap between them: handling the ways real systems fail — partial writes, dying upstreams, signals, port conflicts, resource exhaustion — so the service degrades gracefully instead of crashing, and so the humans can tell what's wrong from outside.

Hardening is not a feature; it's the difference between "it runs" and "it runs when it matters." The four pillars: **clean lifecycle, honest health, classified retries, and bounded resources.**

## When to Use

- Shipping any server, daemon, bot, or long-running process
- Reviewing a service before it "goes live"
- A service that crashes "randomly" in deployment but not locally
- Adding observability to an existing service

**Don't use for:** one-shot scripts (they don't need health endpoints), or services that will be replaced next week (harden what persists).

## The Four Pillars

### 1. Clean Lifecycle (signals & shutdown)

- **Handle termination signals** (SIGTERM/SIGINT): stop accepting new work, finish in-flight work within a deadline, flush state, then exit 0. A hard kill (SIGKILL) loses whatever wasn't flushed.
- **Graceful shutdown contract:** `shutdown()` must be callable twice safely (idempotent), must have a timeout, and must not deadlock on in-flight work.
- **Startup ordering:** bind ports last, after dependencies are ready. If the DB is down at boot, fail fast with a clear message — don't half-start and serve 500s.
- **Single responsibility per process:** don't run two services in one process "to keep it simple" — you lose the ability to restart one without the other.

### 2. Honest Health (observability from outside)

- **`/health` endpoint** returning `{"status":"ok"}` with a real check behind it (DB ping, upstream reachability), not a hardcoded 200. A health check that always passes is theater.
- **Liveness vs readiness:** liveness = "process is up"; readiness = "can take traffic." Separate them when the service needs warmup or has dependencies.
- **Metrics that matter:** request count, error rate, latency p50/p95, in-flight count. Expose them (a `/metrics` endpoint or log lines) — you can't tune what you can't see.
- **Structured logs:** JSON or key=value, one event per line, with a request/run ID to correlate.

### 3. Classified Retries (failure taxonomy)

- **Classify errors first:** transient (network blip, 429, 503, timeout) vs permanent (400, 404, auth failure, schema mismatch). Only retry transient.
- **Exponential backoff + jitter** on retries: `min(cap, base * 2^attempt) + jitter`. Fixed-interval retries thundering-herd the upstream.
- **Retry budget:** max attempts and a total time cap. After that, fail loudly with the last error — don't retry forever.
- **Circuit breaker for downstreams:** after N consecutive failures to an upstream, stop calling it for a cooldown period, then try one probe. Prevents a dying upstream from taking your latency down with it.

### 4. Bounded Resources (don't die of success)

- **Concurrency limits:** cap in-flight work; queue or reject the rest (with a clear 503, not a hang).
- **Timeouts everywhere:** per-request, per-upstream-call, per-task. A hung call is a leak you can't see.
- **Body/size limits** on inputs. An unbounded upload or response will OOM you eventually.
- **Startup/health/graceful-shutdown all respect the same timeouts** — a shutdown that waits forever is a crash in slow motion.

## Common Pitfalls

1. **Health endpoint that lies.** `return 200` with no check behind it. The health check is for *you* — make it honest or don't ship it.
2. **Retrying everything forever.** A 400 retried 10 times is a 400 ten times. Classify.
3. **Ignoring signals.** `Ctrl+C` kills the process mid-write and corrupts state. Handle the signal; flush; exit clean.
4. **Fixed-interval retries.** When the upstream recovers, every retrier hits it at once. Jitter exists for this reason.
5. **No timeout on shutdown.** If shutdown waits for a hung worker, the orchestrator SIGKILLs you anyway — and you lost the graceful part.
6. **Hardcoding "it works on my machine" assumptions** — ports, paths, env vars. Read them from config/env with sane defaults, and fail loudly if required ones are missing.

## Verification Checklist

- [ ] SIGTERM/SIGINT triggers graceful shutdown: in-flight finished, state flushed, exit 0
- [ ] `/health` performs a real dependency check and reports honestly
- [ ] Liveness and readiness separated if the service needs warmup
- [ ] Errors classified; only transient retried, with backoff + jitter + budget
- [ ] Circuit breaker protects downstreams from cascading failure
- [ ] Concurrency, timeout, and size limits set on every entry point
- [ ] Structured logs with correlatable IDs; key metrics exposed
- [ ] Shutdown idempotent + time-bounded; startup fails fast on missing deps

## One-Shot Recipe: Hardening Checklist for a New API

```
1. lifecycle: signal handler -> drain in-flight (max 10s) -> flush -> exit 0
2. health: /health pings DB + upstream, returns real status
3. retries: classify errors; backoff(2^n + jitter) x3; circuit break after 5
4. resources: max 50 concurrent; 30s request timeout; 10MB body cap
5. logs: JSON lines with request_id; /metrics exposes p50/p95/error-rate
6. test: SIGTERM mid-request -> completes cleanly; kill upstream -> 503s not hangs
```

A hardened service fails loudly, retries smartly, shuts down cleanly, and tells you the truth about its health. Everything else is a script with delusions of grandeur.
