# 01 — UI Principles

Source: inventory of `design-intelligence` (108K UI/UX Pro Max + 74 brand DESIGN.md), `motion`, `popular-web-designs` (54 systems). Structure below — not a copy of style CSVs.

## Mental Model

- UI is **luminance hierarchy**, not decoration. Order surfaces by lightness: canvas → panel → elevated. Text follows: primary → secondary → tertiary → quaternary.
- **Density is honesty.** A barbershop needs high scannability (hours/price/map), not SaaS brochure density. Density choice is an information-design decision (§ product domain).
- **Motion explains hierarchy**, not vibes. If motion doesn't clarify what is primary, kill it (see `motion` stagger vs gratuitous parallax).

## Decision Rules

- Define `:root` tokens before any component. Max 7 colors: canvas/panel/surface/text/muted/accent/border. Cite one `awesome-design-md` brand as baseline per project.
- Typography: 3 weights max (400 read / 500–510 emphasize / 590 announce). At display sizes, use negative tracking (-1.0 to -1.6px at 48–72px). Enable `font-feature-settings: "cv01","ss03"` for Inter/Geist.
- Spacing: 8px base. Scale 4/8/12/16/24/32/48/64/96. Never mix 7px/11px micro-tweaks unless brand file justifies it (Linear does).
- Use **one** accent. On Linear, indigo `#5e6ad2` only on CTA/active. On a barber site, orange is job-specific (warmth) — but still single.

## Frameworks

- **Luminance stacking (Linear model):** bg `0.02 → 0.04 → 0.05` white opacity steps for elevation on dark; on light, `warm-clay/cream` steps.
- **Ring-not-shadow on dark:** `0 0 0 1px rgba(255,255,255,.08)` for border-as-shadow. Real shadows fail on `08090a`.

## Anti-Patterns

- Overused glassmorphism (blur everywhere), purple-blue gradients, stock hero + overlay, corporate blue, pill-everywhere, generic shadow stacks.

## Verify

- Printed tokens list in comment header + `vision_analyze` screenshot compares to brand baseline (Spotify/Stripe/Linear bar).

Refs: `awesome-design-md/design-md/linear.app/DESIGN.md` §§1–3; `ui-ux-pro-max/styles.csv` Nature Distilled / Minimal & Direct.
