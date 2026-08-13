# 12 — Builder Culture: From Slapping On to Pixel Craft

Source: scholar `builder-distilled.md` 99 lines — Canva Learn 20K, Figma auto-layout 15K, Rappenem sword tutorial 2600×2950, Nitgo PlanetMinecraft 15K, DantePixels 240+ weapons, Minecraft wiki, BlockBench/itch.io.

## Canva / Constrained Creativity

- Thesis (Canva Learn): design's role = concisely present ideas; tools raised consumer expectations — **constraint raises floor, not ceiling**.
- 15-principle canon: golden ratio 1.618 (dimension guide), visual hierarchy (visual flow: first landing → secondary → endpoint), sizing as visibility dial, focal weight via size+shape+color+texture+position, color sparingly (temperature contrast warm-vs-cool draws fastest, then value, then saturation), gradients = tints/shades for 3D illusion, typography hierarchy, white space as design element, grids/symmetry/asymmetry/transparency/texture as scaffolding.
- Builder trap: **template as starting constraint, not final answer** — swap hierarchy, re-balance temperature, inject one gradient/texture to break sameness. Differentiation comes from principle fluency, not tool access.

## Figma Auto-Layout as Constraint Engine

- Primitives: direction Vertical/Horizontal/Grid; spacing Padding (parent→children TRBL) + Gap (between children, fixed or Auto distributed); resizing Hug/Fill/Fixed/MinMax per axis; Ignore (ex-absolute for overlays/badges).
- Design System Builder plugin: select colors+font styles/sizes → one-click full library (Buttons, Inputs, Dropdowns, Radios, Checkboxes, Textareas, Switches, Icons) with variants, wired to Auto-Layout. Treat Figma as **constraint engine: tokens in, variants out**.

## Minecraft 16×16 Weapon Craft — Pixel Pipeline

- Canvas: `assets/minecraft/textures/item/*.png` 16×16 PNG, transparency, nearest-neighbor (no filter hides mistakes — pixel perfection required).
- 6-stroke workflow (15 min/weapon at speed): 1 Silhouette solid (45° diagonal for swords, must read at 8×8 thumbnail) → 2 Outline darkest (not #000, use ramp's darkest −10%) → 3 Base fill → 4 Shadow (cool hue-shift blue/purple) → 5 Highlight (warm yellow) → 6 1-px specular + AA cleanup.
- Palette: 3–5 colors per material, one hue ramp (iron #D0D8E0→#8A9AB0→#5A6A80→#2E3440, gold yellow→orange-brown, wood warm brown→reddish), **hue-shifting** (shadows cool, highlights warm, never just darken same hue). Outline = darkest color, AA = single midtone at diagonal jaggies, dithering = checkerboard only on >4px flats (rare on 16×16), banding = stagger shade steps (never 2px uniform band).
- Silhouette tests: black fill recognizable? 1× vs stone BG contrast? Mirror balanced? Negative space (2–3px blade/guard gap) boosts read. Reclaim outline pixels for blade width (Rappenem). BlockBench hand-test: FOV 70 → rotate Y 30° → if highlight disappears, shift HL 1px camera-facing. Hot-reload F3+T.

## Cross-Cut Thesis

- Canva/Figma templates and 16×16 grids both reward **constraint mastery**: palette/flow discipline, not maximalism. Hug/Fill/Fixed mirrors outline/fill/shadow — systems where primitives compose. Ship test: **does it read at smallest size?** (favicon / 8px inventory). If not, hierarchy/silhouette failed — add contrast, not detail.

## Recipes (copy-paste palette ramps)

- Iron: HL #E6EEF7 → BASE #A8B8CC → SHADE #5C6B84 → OUTLINE #2E3440 (+14° blue per step). Specular 1px #FFF at leading edge midpoint + AA mid pixel.
- Gold: #FFF3B0 → #FFD700 → #D4A017 → #8B5A2B (highlights yellow, shadows red-brown +8° orange).
- Wood: #8D6E3F → #6B4E2B → #3E2A16 + 1px vertical grain streaks.
- Enchant: #9B59FF→#4A00B5 at 45° + 1px white glint cross overlay.

Refs: `/tmp/builder-raw.md` 131 lines 12KB verbatim; Lospec/Aseprite/Palettinator toolchain; itch.io DantePixels.
