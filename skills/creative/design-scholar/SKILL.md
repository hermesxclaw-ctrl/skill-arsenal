---
name: design-scholar
description: "Use when designing purpose-built UI, logos, or frontend that must feel human not slop."
version: 0.1.0
author: Hermes
license: MIT
metadata:
  hermes:
    tags: [Design, UI, Frontend, Branding, Originality]
    related_skills: [popular-web-designs, design-intelligence, motion, p5js]
---

# Design Scholar

## Overview

Scholar of UI, web, frontend, logo, and human-vs-AI aesthetics — focused on making every site feel uniquely purpose-built instead of copy-pasted. Does NOT generate templates blindly; it enforces purpose, originality, and token discipline. Stdlib-only, no external build deps unless a reference file says otherwise.

## When to Use

- User asks for UI design, web development, frontend polish, or design critique.
- Making a logo, mark, or wordmark that must feel ownable, not generic.
- Detecting AI slop vs human craft in a site and fixing it.
- Making a page feel unique to its purpose vs copy-paste from Dribbble/Linear/Stripe.
- Choosing type, color, spacing, motion, or layout for a specific audience/purpose.
- Reviewing a site before ship for originality, hierarchy, and accessibility.

## Prerequisites

- `terminal`, `read_file`, `write_file`, `search_files`, `patch`, `web_search`, `web_extract`, `vision_analyze` available.
- Local design DBs optional but recommended: `hermes-workspace/github-tools/ui-ux-pro-max-skill` (108K⭐) and `hermes-workspace/github-tools/awesome-design-md/design-md/` (74 brands).
- For verification: preview pane via `terminal` (`python -m http.server 8765`) and `vision_analyze`.
- Canon distilled: Rams 10 Principles (Vitsœ), Norman DOET (2013), Refactoring UI (Wathan/Schoger), Weinschenk 100 Things, Logo Design Love (Airey) + Paul Rand canon; GitHub top 5 (shadcn 121k, Ant 99k, Chakra 40k, Primer 13k, awesome-design-systems 25k) + NN/g 10 heuristics + Baymard; Rand 7-step logo test + AI slop + GSAP+Lenis. See `references/08-canon-books.md`, `references/09-github-ux.md`, `references/10-logo-motion-human.md`.

## How to Run

- Invoke through the `terminal` tool: `python src/ui-ux-pro-max/scripts/search.py "<query>" --domain <domain>` for style/type/color lookups.
- Load a chapter on demand with `skill_view` file_path `references/<file>.md`.
- Apply tokens via `write_file` to HTML/CSS, then verify with `vision_analyze` or `web_extract`.

## Quick Reference

- DB queries: `style` (aesthetics), `typography` (pairings), `color` (palettes), `product` (landing patterns), `ux` (anti-patterns), `icons` (phosphor/lucide), `landing` (structure).
- Brand tokens: `read_file` `awesome-design-md/design-md/<brand>/DESIGN.md` (e.g., `linear.app`, `stripe`, `vercel`, `figma`, `notion`).
- Motion: `motion` skill (`motion@12.23.6`) — `animate`, `stagger`, `spring`, `inView`, `scroll`.
- Logo: `references/04-logo-identity.md` (mark types, construction, testing).
- Human vs AI: `references/05-human-vs-ai-aesthetic.md` (detection + repair rules).
- Originality: `references/06-originality-purpose.md` (purpose map → form).

## Procedure

1. Inventory purpose: audience, job-to-be-done, tone, and one-line promise. See `references/06-originality-purpose.md`.
2. Choose tokens intentionally: run one `terminal` search per domain (`style`, `typography`, `color`) and pick one `awesome-design-md` brand as token baseline. Record in `:root{}`.
3. Draft layout from purpose, not template: select `references/03-design-systems-tokens.md` grid/spacing/radius/shadow rules.
4. Craft logo/mark if needed via `references/04-logo-identity.md` (construction + legibility + ownability tests).
5. Apply human-craft pass via `references/05-human-vs-ai-aesthetic.md` + `references/07-anti-slop-detection.md` (remove AI tells, add specificity).
6. Add motion only if it explains hierarchy (`references/02-frontend-architecture.md`).
7. Verify with `vision_analyze` and the checklist in `## Verification Checklist`.

## Common Pitfalls

- Loading this skill without running at least one `terminal` search or reading one brand `DESIGN.md` produces generic AI slop — the classic failure.
- Generic gradients, glassmorphism everywhere, and stock hero with overlay text signal AI templating.
- Pure black `#000` or pure white `#fff` as text on dark/light strains eyes — use `f7f8f8` / `#f5f4ed` etc.
- Over-rounded (`9999px` everywhere) and heavy drop shadows on dark surfaces kill credibility.
- Logo in a pill with `overflow:visible` stripes clips into a toothpaste bean — use strict `clipPath` + transparent container.
- Copy-paste without purpose mapping creates sameness — same Linear card on a barbershop feels dishonest.

## Verification Checklist

- Run `search_files` for `s3-media` / hotlink violations (0), `write_file` preview, then `vision_analyze` the screenshot: hierarchy, token consistency, and human-vs-AI tells per `references/05-human-vs-ai-aesthetic.md`.
- Checklist: one purpose sentence, one token source cited, logo passes 16px legibility, no AI slop flags from `references/07-anti-slop-detection.md`.

## Reference Index

Load on demand with `skill_view` file_path `references/<file>`:

- `references/01-ui-principles.md` — load when choosing hierarchy, layout, or visual weight.
- `references/02-frontend-architecture.md` — load when structuring HTML/CSS, motion, or performance.
- `references/03-design-systems-tokens.md` — load when defining color, type, spacing, radius, shadow.
- `references/04-logo-identity.md` — load when designing or critiquing a logo/mark.
- `references/05-human-vs-ai-aesthetic.md` — load when detecting or repairing AI-generated aesthetics.
- `references/06-originality-purpose.md` — load when making a site feel unique to its job, not copy-paste.
- `references/07-anti-slop-detection.md` — load when auditing before ship for generic tells.
- `references/08-canon-books.md` — load when applying Rams, Norman, Refactoring UI, Weinschenk, Airey/Rand.
- `references/09-github-ux.md` — load when choosing stack (shadcn/Geist) or applying NN/g + Baymard UX.
- `references/10-logo-motion-human.md` — load when applying Rand 7-test, de-slop, or GSAP/Lenis motion.
- `references/11-pixel-craft.md` — load when auditing at pixel level (toothpaste, gap doubles, clipPath, 16px).
- `references/12-builder-culture.md` — load when building inside constraints (Canva/Figma/Minecraft 16×16).
- `references/13-when-bad.md` — load when diagnosing why something looks bad (Gestalt/hierarchy/visceral).
- `references/14-taste-perspective.md` — load when learning perspective/taste via volume + iteration (Glass/Maeda).
- `references/glossary.md` — load when a term (e.g., `cv01`, `luminance stacking`) is unclear.
- `references/cheatsheet-decision-tables.md` — load when you need quick token/type/motion choices.
