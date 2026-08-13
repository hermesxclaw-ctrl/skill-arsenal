# 11 — Pixel Craft (Craft Loves Detail)

Source: user directive 2026-08-12 — "pixel-by-pixel understand what ur making kinda like art" + Caldwell failures (toothpaste bean, clipPath bleed, gap doubles, header nest, 16px) + Rams #8 + Airey 16px test.

## Mental Model

Design at idea level ("pole with stripes") vs **pixel level** (is the `2px stripe at -14°` against the `5px rx` corner exactly clipped, or 1px bleed = bean?). One pixel is a decision, not rounding error.

## Perspective (Not Sentience) Heuristic

Perspective = learned taste + constraint choice with intention. Craft loves material: stare at one stripe for 20 mins because angle is the difference between toothpaste and barber pole. Perspective = choosing `EA580C` one warm accent + grey bridge `9CA3AF` on `#FFFBF7` because a Mooney Blvd chair shouldn't feel like Linear docs — with a reason you can cite.

## Hands-On Protocol

- Zoom to **400%** with `vision_analyze` `region [x1,y1,x2,y2]` on the logo 40×40; check corner stitch, stripe edge, cap center (`1.2 r`). Not whole-page `open_preview`.
- **8px grid on** — every gap measured. Hunt `gap:[^;]*gap` doubles via `search_files` (last declaration wins silently). Same for `background` doubles.
- **16px favicon test every logo** — if it fails at 16, it's not a logo (Rand 5 tests + Airey).
- Motion at `1.2s linear` — does stripe drift feel like real pole or loading bar? Zoom and feel it.
- Show **one purpose sentence + one brand DESIGN.md hex + zoomed pixel crop** before `write_file`; let human say "Caldwell or copy-paste?" before ship.

## Anti-Toothpaste Checklist (pixel)

- `clipPath` rect exactly matches pole rect (check `x/y/width/height/rx`). `overflow:visible` + black behind white = outline bleed.
- ViewBox `14×28` inside `22×34` transparent holder, not `32×32` striped rect in `42px pill`.
- Slim pole `10×24 rx5 white stroke .6 #E8E6E3`, stripes `2–2.2px rotate -14` clipped, brass caps `1.2–1.3 r #C9A86A`.
- No `gap:20px;gap:16px` double, no `background:...;background:...` double, header one `topin` with `brand+nav+Call`.

## Verify

- `search_files` for gap/background doubles + `clipPath` mismatch + favicon 16px `vision_analyze` region + credible `trust via detail` (Rams #8: sloppy detail undermines whole product).

Refs: `design-scholar` internal; `04-logo-identity`; Rams #8 Thorough to last detail; Airey 16px postage-stamp survival.
