# 05 — Human vs AI Aesthetic

Source: 2026-07-22 Olo audio-bar failure (skill loaded but not used) + `design-intelligence` Anti-Patterns + `popular-web-designs` human benchmarks (Linear/Stripe/Claude).

## Human Signals

- **Specificity**: real NAP `3734 S Mooney Blvd`, real hours `Tue–Fri 8–5`, real rating `4.4★ 116` — not "★★★★★ Trusted by 10K+". Human sites leak locality.
- **Token citation**: Linear's `cv01 ss03` + `510` weight + `-1.056px` at 48px is a *decision* with a source. AI picks Inter 600 generic.
- **Constraint honesty**: "No online booking — call or text" is more trustworthy than a fake form with no backend.
- **Editorial pacing**: Claude's parchment `f5f4ed`, warm sand `e8e6dc`, and serif hierarchy feel like a paper salon vs JSON-blue glass.

## AI Tells (detector)

- [ ] Overused glassmorphism (frost everywhere), purple-blue gradients, stock hero with center-text overlay.
- [ ] Corporate blue `#2563EB` default, pill `9999px` on everything, heavy drop shadows on dark surfaces.
- [ ] Generic hero stats ("10K+ happy clients"), no PlaceID/coords, masked `+155****` tels.
- [ ] Same Linear card repeated 6× with different emoji — layout without purpose variation.
- [ ] Motion that decorates: parallax on every section, but no `stagger` that reveals information order.

## Repair Rules

- Run one `terminal` search per domain before writing CSS (`style`, `typography`, `color`). Load one `awesome-design-md` brand file and quote its hexes in a header comment.
- Replace fake booking with honest affordance (`tel:`/`sms:`) when no backend exists.
- Swap gradients for luminance steps or warm sand gradients (Claude method: cream→sand→stone).

## Verify

- `Anti-slop` check: if screenshot could be any SaaS by swapping logo, fail — add locale-specific detail per `references/06-originality-purpose.md`.
