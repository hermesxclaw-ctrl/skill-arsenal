# 13 — When It Looks Bad: Diagnostic

Source: scholar `bad-distilled.md` 100 diagnostics + `bad-raw.md` 3634 lines — Gestalt (wiki 2286), Aesthetic-Usability (NNGroup), Uncanny Valley 3415, Visual Hierarchy 363, IxDF Gestalt 811, Refactoring UI 438, Laws of UX, Baymard 737, Canva Learn 403-block fallback.

## 1) Gestalt Violations — Brain Says "Wrong" Before Words

- Thesis: whole ≠ sum of parts; brain groups via Prägnanz (simplicity). Ambiguous grouping = unease.
- Proximity: related spaced apart / unrelated crammed → grouping noise. Similarity: same function different colors/shapes → false categories. Continuity: misaligned edges/jagged grids → scan stutters. Closure: incomplete shapes force mental fill-in → fatigue. Figure/ground collapse: low contrast / busy bg → illegible. Near-symmetry (≈symmetry) reads as mistake, not intention → cheap. Common fate: animated elements move incoherently → glitchy. Fix: enforce 8/16/24 spacing, consistent similarity, align to grid, close shapes. Squint test: groups survive blur? If not, proximity/contrast off.

## 2) Visual Hierarchy Failures — Nothing to Look At First

- Hierarchy = perceived order via size/weight/color/contrast/position/whitespace. Flat (headline=body=caption → eye wanders), inverted (decorative dominates, CTA recedes), too many levels (5+ sizes + 4 colors → none wins). Rules: 1.25× type scale (12/14/16/20/24/30), one accent for primary action, neutrals for structure, whitespace as hierarchy (proximity+padding > color). F/Z reading patterns place anchors accordingly. WCAG AA (4.5:1 body, 3:1 large) doubles as hierarchy+a11y. 3-second test: can stranger name primary action? If not, hierarchy failed.

## 3) Inconsistent Spacing / Color — System Collapse

- 4/8pt scale violated → ambiguous spacing (equal gaps between unrelated groups). Kill by making gaps identical or clearly different (Refactoring: ambiguous spacing!). Vertical rhythm broken → jagged scan. Neutral ramp noisy (too many grays, no tint) → cheap. Shadows/radius inconsistent → elevation lies. Fix: systematize 4 spacing values, 3 font sizes, 1 radius scale (Refactoring: systematize everything), never deviate.

## 4) Generic Stock + AI Uncanny Valley

- Stock cliché (same barber pole, same Inter 700 hero) signals "found, not made." AI tells at 400%: kerning irregular, grid drift 1px, temperature flat (no hue shift), 3 identical cards with gradient "Most popular" pill. Creepy when nearly right but micro-off — invest in real photos (even phone) + honest specificity (PlaceID, street, hours).

## 5) Good Function Still Fails — Visceral Level (Norman)

- Norman 3 levels: visceral (look/feel) → behavioral (works) → reflective (meaning). Beautiful-but-broken forgives; ugly-but-functional doesn't — visceral bypasses rationalization. Aesthetic-usability effect (NNGroup, 50ms first impression): pretty is perceived as more usable, tolerates minor usability bugs. Arcadis/FitBit cases: aesthetic lift raised task success without changing flow. Checklist (5s): Does it feel warm/inviting at a glance? Would you trust your hair to this? If visceral fails, behavioral never gets tried.

## Repair Order

1 Squint/blur for grouping → 2 3-second primary-action test → 3 Squint spacing grid → 4 Kill generic stock/slop (left-align, weight 500 not 700, solid dark+radial not gradient) → 5 Warm the visceral (material texture, specific locality).

Refs: bad-raw 125KB concatenated dumps; IxDF/Wiki Gestalt; NNGroup aesthetic-usability.
