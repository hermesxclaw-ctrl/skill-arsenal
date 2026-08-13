# 10 — Logo, Motion & Human vs AI

Source: scholar extracts `/tmp/logo-motion-distilled.md` 149 lines — 8 pages via DDGS+fetch (Firecrawl billed): Rand 7-test, AI slop ×2, GSAP+Lenis ×2, craft, Jitter, Butter.

## Paul Rand 7-Step Logo Test (1991 AIGA "Logos, Flags, and Escutcheons")

"A logo does not sell; it identifies." Score 1–10 each → /70. Bing old logo = 36 (failed distinctive/memorable). 7: Distinctive (unique, not confused), Visible (noticeable by colour/size/concept), Adaptable (16px→billboard, mono→colour, print→digital), Memorable (special ingredient, avoids cliché), Universal (cross-culture), Timeless (not trend colours), Simple (distilled via repeated reduction, balanced). NeXT 28° 100pp spec = craft signal. Encode as geometry (SVG) + document construction grid. Fail build if adaptable/simplicity not met (must render legibly at 24px mono).

## Why AI Slop Happens

LLMs = average of narrow corpus (Tailwind + shadcn + 200 Vercel templates + YC 22-24). RLHF rewards safe → median 2024 = purple gradient + 3 cards + Inter 700 + centered. Same corpus across Lovable/Cursor/Claude/v0/Bolt — tool switch doesn't fix.

5 tells + fixes (Rottoways): 1 Purple gradient hero (violet→indigo white centered) → solid dark + single warm radial corner or noise texture / vignetted photo (atmospheric not gradient-y). 2 Three identical feature cards (equal icon+heading) → asymmetry: 60/40 hero+secondary / vertical alternating / tabbed. 3 Inter 700 headlines (-0.02) → 500/400 large, Fraunces/Geist swap (500 = considered, 700 = trying). 4 Centered everything → left-align body, reserve center for one true hero. 5 "Most popular" gradient pill → single-colour outline or subtle scale, no gradient badge. Deeper: no taste (polish without judgment) + no loop (one-shot → eyeball → manual fix). Data: AI PRs 1.7× issues, 2.74× vulns (Dec 2025, 470 PRs); CHI 2025 AI systematically inaccessible markup. Fix pattern: design-system level distinct corpus + closed loop **guardrails → critique (10-item bar) → fix top issue → re-evaluate until pass** + self-correction ("no gradients on hero" recorded). Ref impl `npx skills add educlopez/ui-craft`.

## Craft vs Factory

Factory: fast, scalable, repeatable (hundreds of variants in seconds) — good for exploration. Craft = imperfection+labour+touch: stencil cut, ink letter, silkscreen smudges, graffiti drips, layered textures = energy AI-polished vectors lack. Hybrid recommended: **AI foundations (patterns/textures/compositions) → hand rework (paint/collage/scan/stencil) → digitize**. AI-drafted logo → hand-drawn stencil refinement → vectorise = unreplicable uniqueness. Dribbble/Behance human signal: deliberate imperfection, material texture (paper grain, ink bleed), construction grids, asymmetry, custom lettering — absent from median AI without explicit constraint.

## Jitter / Motion Principles

Jitter BM-03: linear = robotic; **Slow down** (entering: arrives fast, eases to stop), **Accelerate** (exiting), **Smooth/Natural** (between), **Linear** only for never-stopping (spinner/BG). Butter 3 foundations: 1 Easing (choose metaphor: table-slide decisive vs spring overshoot), 2 Staggering (`progress = frameCount%period - 3*i`, random seed for less structure), 3 Secondary motion (overlapping subtle bounce/sway post-entrance: `bounce=6*cos(progress*0.06)`, `swayAngle=PI*0.02*cos(progress*0.03+i*1.5)` — overlap, not sequence). Code: `period=3*60`, `map(0,2*60,0,1,true)`, `lerp(-height,0,entranceProgress)`, elastic `2**(-10*st)*sin((st-s)*2PI/p)+1`.

GSAP+Lenis production: **Lenis first, GSAP second, single RAF**. `ReactLenis root autoRaf:false` + `gsap.ticker.add(raf)` where `raf = (time) => { lenis.raf(time); ScrollTrigger.update(); }` + `gsap.ticker.lagSmoothing(0)`, on unmount `gsap.ticker.remove(raf)`. Also `ScrollTrigger.scrollerProxy` + `refresh` on `lenis.resize()`. Animate only `transform`+`opacity` (compositor), never top/width/margin on scroll. One RAF (disable Lenis autoRaf). `refresh` after fonts/images/route changes. Lazy below fold. Video scrub: map scroll%→currentTime throttled every 3rd frame desktop, canvas sequence mobile via Video.js. Mobile: disable Lenis on `pointer:coarse` (native inertia), CSS scroll-snap for pinned, fixes iOS Safari flicker. A11y: respect `prefers-reduced-motion`, `gsap.matchMedia()`, `lenis.scrollTo('#section')` for anchors. Restraint: 4 interactions (pinned horizontal + word reveal + parallax + video scrub) competed → keep 2 strongest; Lighthouse 85 desktop / 72 mobile; reduced-motion fallback day one.

Refs: `/tmp/logo-motion-raw.md` 241 lines verbatim; URLs: brandsthatpunch Rand test, smoothui AI slop, rottoways AI generic, shobhitverma GSAP+Lenis, hontran smooth-scroll, brandson craft, jitter BM-03, butter video blog.
