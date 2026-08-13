# 07 — Anti-Slop Detection

Source: Caldwell fixes (double-gap, double-nav, masked tels, JSON-LD `https://***`, header nest, toothpaste pole, dot graph, fake booking) + `design-intelligence` Pitfalls.

## Pre-Ship Detector (run every time)

- [ ] `search_files` for `\+155\*\*\*\*` — 0 masked tels (real `+15596369936` only).
- [ ] `search_files` for `s3-media` / `yelpcdn` hotlinks — 0 in live (private pitch only, labeled).
- [ ] `search_files` for `gap:[^;]*gap` or `background:[^;]*background` doubles — dedupe.
- [ ] Header has ONE `topin` with `brand + nav + Call` inside; `</div></div><nav` pattern = broken nest.
- [ ] ONE nav only (top `SHOP/MENU/REVIEWS/ABOUT`), not top+middle duplicate.
- [ ] `panel` vs `panel-tos` display: `.panel{display:none}.panel.active{display:block}` + explicit `#panel-tos` override, else TOS leaks.
- [ ] JSON-LD `"@context":"https://schema.org"` not `https://***`.
- [ ] `clipPath` rect exactly matches pole rect (no bleed).
- [ ] `word-spacing: //` missing first value — `//` is a broken comment, not CSS.
- [ ] No `p5js-lite 28-particle` dot graph when no backend — kills credibility ("graph with moving dots tf").
- [ ] No fake `bookingForm + /api/book` when `backend/server.js` is not deployed — use `tel:`/`sms:` honesty.

## Repair Script

- Header nest: `</div>\n</div>\n<nav` → `</div>\n<nav` (one close only).
- Gap double: `gap:20px;gap:16px` → `gap:20px` single.
- TOS leak: add `.panel#panel-tos{display:none}.panel#panel-tos.active{display:block}`.
- JSON-LD: `https://***@type` → `https://schema.org","@type`.
- Logo bleed: slim viewBox `14×28` inside `22×34` transparent, not `32×32` striped rect in `42px pill`.

## Verify

- `terminal` `wc -c` < 60K single-file + `curl -I :8765` 200 + `vision_analyze` top bar single row, pole not bean.
