# 🛡️ Skill Arsenal

**Pro-grade agent skills — battle-tested procedures for autonomous agents, orchestration, debugging, ops, and the craft of skills themselves.**

A curated collection of SKILL.md files written to a strict authoring contract, validated by CI, and designed to change agent behavior — not just document it. Every skill here follows the same discipline: trigger discipline, checkable completion criteria, no-op-free prose, and a verification checklist you can run.

> **What is a skill?** In agent frameworks like [Hermes Agent](https://github.com/NousResearch/hermes-agent), a skill is a markdown procedure an agent loads to make its process predictable. This repo is a library of the good ones.

## 📦 The Skills

| Skill | Category | What it does |
|---|---|---|
| **[bounded-autonomy-loop](skills/autonomous-ai-agents/bounded-autonomy-loop/SKILL.md)** | Autonomous Agents | Run unattended work with checkpointed state, heartbeat reporting, and a hard-stop contract. Survives crashes, resumes where it left off, never spins forever. |
| **[multi-agent-orchestration](skills/autonomous-ai-agents/multi-agent-orchestration/SKILL.md)** | Autonomous Agents | Fan-out/fan-in parallel subagents done right — self-contained briefs, verification-handle rules, and merging that catches the lies children tell. |
| **[systematic-debugging](skills/software-development/systematic-debugging/SKILL.md)** | Software Dev | 4-phase root-cause method: reproduce → isolate → instrument → fix with evidence. No guessing, no "fixed" without proof. |
| **[cron-ops](skills/devops/cron-ops/SKILL.md)** | DevOps | Resilient scheduled jobs: idempotency, loud failure, watchdogs, and retry taxonomy. Turns cron from a liability into infrastructure. |
| **[service-hardening](skills/devops/service-hardening/SKILL.md)** | DevOps | Production hardening: graceful shutdown, honest health endpoints, classified retries, circuit breakers, bounded resources. |
| **[skillcraft](skills/meta/skillcraft/SKILL.md)** | Meta | The discipline of writing skills that change behavior — trigger discipline, completion criteria, anti-sediment rules. The skill that governs all the others. |

## 🚀 Install

Skills install into any agent framework that reads SKILL.md (Hermes Agent, Claude-style agents, etc.):

```bash
# Hermes Agent — install from this repo
hermes skills install github:hermesxclaw-ctrl/skill-arsenal

# Or just clone and point your skill loader at skills/
git clone https://github.com/hermesxclaw-ctrl/skill-arsenal.git
```

## ✅ The Authoring Contract

Every skill in this repo passes the validator in [`scripts/validate_skills.py`](scripts/validate_skills.py), which enforces:

- Frontmatter at byte 0, valid YAML, non-empty body
- `name` ≤ 64 chars (lowercase+hyphens), `description` ≤ 1024 chars
- Description starts with **"Use when..."** (trigger discipline — the first ~57 chars are what agents see in indexes)
- `version` / `author` / `license` / `metadata.hermes.{tags, related_skills}` present
- Required sections: `## Overview`, `## Common Pitfalls`, `## Verification Checklist`
- Total file ≤ 100,000 chars (target 5–15K: dense, not sprawling)

**Run it locally:**

```bash
python scripts/validate_skills.py          # required checks
python scripts/validate_skills.py --strict # + recommended fields
```

**CI:** `.github/workflows/validate.yml` runs the validator on every push/PR. A skill that doesn't pass doesn't merge.

## 🧭 Contributing

Want to add a skill? Follow [`skillcraft`](skills/meta/skillcraft/SKILL.md) — it's the meta-skill that defines the standard:

1. Name the behavior change first (if the agent would do it anyway, don't write it)
2. Write trigger-first description, numbered steps with completion criteria, pitfalls, verification checklist
3. Run `python scripts/validate_skills.py --strict` until green
4. Open a PR — CI will check it again

## 📄 License

MIT — use it, fork it, teach your agents from it. See [LICENSE](LICENSE).

---

*Never finished, always evolving — same as the agents it serves.*
