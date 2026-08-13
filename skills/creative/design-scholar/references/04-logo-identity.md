# 04 — Logo & Identity

Source: issues on Caldwell pole (toothpaste bean, clipPath overflow, black pill, centered gap) + `brandkit` / `awesome-design-md` mark studies.

## Mental Model

- A mark is **reduction**, not illustration. Best barber marks are one shape: pole, scissors, or comb — never all three.
- Ownability comes from **construction discipline**, not decoration: consistent corner radius, single stroke weight, strict clipping.

## Decision Rules

- Container: transparent when site is light; `var(--ink)` tile only when canvas is dark. Never `background:var(--ink)` on light with `overflow:visible` stripes — creates black outline bleed.
- Pole: `10×24 rx5 white` with `stroke .6–.7 #E8E6E3` inside `22×34` transparent holder. Stripes `2–2.2px` `rotate(-14)` clipped via `clipPath` whose `rect` matches pole exactly. Brass caps `1.2–1.3 r #C9A86A`.
- Wordmark: `Anton/Inter 15px` `CALDWELL` + `JetBrains Mono 8px .22em` `BARBER SHOP`. Gap `12px`, `align-items:center`. Never two gaps (`gap:20px;gap:16px`) — last wins silently.

## Build Checklist

- [ ] Mark passes 16px legibility (16×16 favicon test).
- [ ] No `clipPath` bleed outside rect (stripes clipped, not overflowing).
- [ ] No double-gap or duplicate `background` declarations.
- [ ] Single accent in mark matches site `:root --accent`.

## Pitfalls

- `40–44px` pill + `28px` striped rect inside → stripe overflow reads as toothpaste with black outline. Slim to `18×30` viewBox inside `22×34` holder.
- Mixing blue `#0A84FF` with orange without grey bridge reads candy-shop — use `grey #9CA3AF/#6B7280` as bridge.
- Scissors mark needs `1.7` stroke at `20px`; thinner vanishes, thicker looks clip-art.

## Verify

- `vision_analyze` 16px favicon + `search_files` for `gap:[^;]*gap` double-declaration.
