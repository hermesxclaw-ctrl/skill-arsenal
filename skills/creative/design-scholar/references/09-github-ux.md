# 09 — GitHub Stack & Real UX Research

Source: scholar extracts `/tmp/github-distilled.md` 96 lines — 5 repos starred + NN/g + Baymard + Refactoring prescription, Firecrawl billed→fell back to gh search + curl.

## Top 5 GitHub Design-System Repos

1. **shadcn/ui** `shadcn-ui/ui` 121k — copy-paste Radix+Tailwind, own the code, CSS variables, `tweakcn` editor to remix Geist/Linear tokens. De-facto starter for marketing + booking. MIT.
2. **Ant Design** `ant-design/ant-design` 99k — enterprise React, opinionated spacing/type; borrow form validation, not visual weight for customer barber page.
3. **Chakra UI** `chakra-ui/chakra-ui` 40k — accessible style-props, rapid polish; pick shadcn OR Chakra, not both.
4. **Primer CSS** `primer/css` 13k (GitHub) — KTLO utils; real system is `primer/react`; reference for restrained trustworthy UI.
5. **awesome-design-systems** `alexpate/awesome-design-systems` 25k — meta-resource: 100+ production systems (Linear/Stripe/Apple/Vercel/Polaris etc) with tags.

Archived: `geist-org/geist-ui` 4.5k styled-jsx era over — survives as `vercel/geist-font` 3.5k + Tailwind patterns. Linear recipe: dark, 1px ~8% borders, 6px radius, ⌘K.

## NN/g 10 Heuristics (Nielsen 1994) — barbershop mapping

1 Visibility of status — Step 2/3 + immediate confirmation. 2 Match real world — "Cut + Beard — 30 min — $35" + scissors icon. 3 User control — Change/Cancel visible, undo without calling. 4 Consistency — one primary CTA style. 5 Error prevention — disable past/full slots, confirm double-book. 6 Recognition > recall — show selected barber photo + service in time-picker. 7 Flexibility — tap + tel: + walk-in, not one funnel. 8 Aesthetic+minimalist — one accent, kill carousels/15 nav links. 9 Recover from errors — "That slot filled — 3 nearby times" inline, not vanishing toast. 10 Help — searchable FAQ "Do you take walk-ins?" with concrete steps.

## Baymard — Booking Funnel (e-comm transferable, 70k sessions)

69% abandonment, 17% "too long/complicated" — every extra field costs conversions. Barber: name+phone+service+time only (no address). Guest booking (no account). Inline validation + progress indicator > end error dump. Trust at CTA: "Free cancellation · Pay at shop · 4.9★". Mobile thumb zone: sticky bottom primary CTA.

## 7 Concrete Barber Prescriptions

1 Stack shadcn+Tailwind+Geist Sans, one accent (amber/emerald). 2 IA: Hero 1 CTA → Services 3-card grid (price+duration+Book) → Barbers → Reviews (real names) → Hours/Map, no mega-nav. 3 Booking funnel 3 steps (Service → Barber+Time → Confirm) inline errors, disabled past/full, 2-tap reschedule. 4 Trust next to CTA per Baymard. 5 Type+space 4 tokens, Inter/Geist, max-w-6xl, generous whitespace (Refactoring: systematize, start with too much space, 2× outer gutters). 6 Heuristics audit every state (empty/loading/error/success) before ship. 7 Pin `awesome-design-systems` + shadcn docs + NN/g poster — sample restraint, not enterprise chrome.

Refs: `/tmp/github-raw.md` (165 lines, gh search stars, READMEs, NN/g extracts, Baymard nav, Refactoring TOC).
