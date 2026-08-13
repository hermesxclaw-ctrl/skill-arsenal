# 02 — Frontend Architecture

Source: `motion` v12 SKILL.md + references (`core-components`, `core-transitions`, `core-stagger`, `values-*`), `popular-web-designs` component notes. Incremental build — not a corpus dump.

## Mental Model

- **HTML is the design system.** Tokens live in `:root`, not inline. Components read tokens, never hardcode hex.
- **Motion is layered:** (a) stagger burst for headlines, (b) scroll reveal (`inView`) for section entry, (c) spring hover for affordance. Each at different stiffness/damping.

## Decision Rules

- Load `motion@12` via ESM `importmap` (`https://cdn.jsdelivr.net/npm/motion@12.23.6/+esm`). Three calls cover most sites: `animate`, `stagger`, `inView`. Add `useScroll` only for parallax.
- Single-file discipline for pitch demos: keep `<60K`, one `<style>`, one `<script type="module">` for motion, JSON-LD for SEO.
- Hash routing for tabbed sites: `activate(name)` toggles `.panel.active` + `aria-selected` + `history.replaceState`. Keep TOS as `panel-tos` outside `.wrap` with explicit `display:none/block`.

## Patterns

- **Headline burst:** wrap words in `.char` spans (`opacity:0, y:10`), then `animate(chars, {opacity:1,y:[10,0]}, {duration:.42, delay:stagger(.016), easing:[.16,1,.3,1]})`.
- **Reveal:** `inView(card, () => animate(card,{opacity:1,y:[10,0]},…), {margin:"-40px"})` + `motion-hidden` initial.
- **Hover elastic:** `animate(card,{scale:1.012,y:-2},{type:'spring',stiffness:420,damping:18})` / leave `420/22`. Buttons `1.04` at `500/18`.

## Pitfalls

- Pure `y` drift without `opacity` looks like a bug. Always pair.
- Animating stripes via `y:[0,6] repeat:Infinity linear` needs `motion` not CSS — CSS `translateY` clashes with `motion` transforms.
- On light canvas, `0 10px 28px rgba(.08)` is the shadow ceiling; beyond = AI sheen.

## Verify

- `terminal` net: `curl -I :8765` 200 + `curl -s | grep importmap` 1.
