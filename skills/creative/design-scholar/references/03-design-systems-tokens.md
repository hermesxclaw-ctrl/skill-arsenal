# 03 — Design Systems & Tokens

Source: `awesome-design-md/design-md/*.md` (74 brands, sampled `linear.app`, `claude`, `stripe`-adjacent), `ui-ux-pro-max` color/type domains.

## Mental Model

- A design system is a **promise**: same promise → same tokens. Caldwell's promise is "phone-first neighborhood chairs" → warm accent, high scannability, not SaaS indigo.
- **Toke discipline > palette breadth.** Linear proves near-monochrome + one indigo wins over rainbow.

## Decision Tables

| Context | Canvas | Panel | Surface | Text | Muted | Border | Accent |
|---|---|---|---|---|---|---|---|
| Linear dark | #08090a | #0f1011 | #191a1b | #f7f8f8 | #8a8f98 | rgba(255,255,255,.08) | #5e6ad2 |
| Barber warm-light | #FFFBF7 | #FFFFFF | #F8F6F3 | #0A0A0E | #6B7280 | #E8E6E3 | #EA580C |
| Claude parchment | #f5f4ed | #faf9f5 | #e8e6dc | #141413 | #87867f | #f0eee6 | #c96442 |

- Radius scale: micro 2 / standard 4 / comfortable 6 / card 8 / panel 12 / pill 9999 — use 6 for buttons, 8 for cards, 9999 only for chips.
- Shadow on dark: ring `0 0 0 1px` + luminance step. On light: `0 1px 0 rgba(.04), 0 8px 24px rgba(.06)` — never heavy.

## Typography Pairs

- **Inter + JetBrains Mono** (Linear, Vercel Geist): pragmatic, geometric via `cv01`/`ss03`. Best for barber/service sites needing clarity.
- **Anthropic Serif + Anthropic Sans** (Claude): warm, editorial — for salons that want parchment humanism, not tech.
- Sizes: display `48–72/-1.0to-1.6` / `h2 20/590/-0.24` / body `15–16/400/-0.165` / mono `11–12/500`.

## Verify

- `read_file` the cited `DESIGN.md`, copy its `## 2. Color Palette` hexes verbatim into `:root` comment, then diff.

Refs: `awesome-design-md/design-md/linear.app/DESIGN.md` §§2–4; `.../claude/DESIGN.md` §§2–4.
