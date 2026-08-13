# Glossary

- **cv01 / ss03** — OpenType features for Inter/Geist; `cv01` alternate `a`, `ss03` geometric alternates. Loaded via `font-feature-settings: "cv01","ss03"`.
- **Luminance stacking** — Linear elevation on dark via `rgba(255,255,255, 0.02→0.05)` steps, not shadow darkness.
- **Ring border** — `0 0 0 1px rgba(255,255,255,.08)` for border-as-shadow on dark.
- **510 weight** — Linear signature between regular 400 and medium 500; subtle emphasis without shouting.
- **PlaceID** — `ChIJrws4bSYvlYARgvYNqRzUvwg` Google Maps place identifier for Caldwell.
- **ClipPath bleed** — Stripe rect overflowing pole rect when clip mismatch — reads as toothpaste.
- **Stagger** — `motion` `stagger(0.016)` delay between `.char` spans for jitter-style burst.
- **InView** — `motion` `inView(el, fn, {margin:"-40px"})` scroll reveal guard.
- **Anti-slop** — Checklist in `references/07-anti-slop-detection.md` — pre-ship human-craft audit.
- **Purpose map** — Table in `references/06-originality-purpose.md` mapping job→tone→layout.

# Cheatsheet — Decision Tables

## Color Quick Pick

- Dark SaaS (Linear): `#08090a` / `#0f1011` / `#191a1b` / `#f7f8f8` / `#5e6ad2`
- Warm service (barber): `#FFFBF7` / `#FFFFFF` / `#F8F6F3` / `#0A0A0E` / `#EA580C`
- Parchment salon (Claude): `#f5f4ed` / `#faf9f5` / `#e8e6dc` / `#141413` / `#c96442`

## Type Quick Pick

- Service clarity: `Inter 500 20px 590 -0.24` + `JetBrains Mono 11px 500` (Linear)
- Editorial warmth: `Anthropic Serif 500 52px 1.2` + `Anthropic Sans 16px 400 1.6` (Claude)

## Motion Quick Pick

- Burst: `.char stagger 0.016 duration .42 easing [.16,1,.3,1]`
- Reveal: `inView margin -40px duration .45`
- Hover card: `spring 420/18 scale 1.012 y -2` / leave `420/22`
- Logo stripe idle: `y:[0,6] 1.2s linear infinite`
- Logo hover: `spring 480/16 scale 1.08 rotate 1`

## Layout Quick Pick

- Single nav only (top `SHOP/MENU/REVIEWS/ABOUT`), not top+middle duplicate.
- Combine Shop+Find Us when locality is the funnel (Caldwell: map in SHOP).
- Scroll-snap reviews with source attribution > bubble templates.
