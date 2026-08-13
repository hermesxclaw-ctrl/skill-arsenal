# 06 — Originality & Purpose

Source: request requirement — "purpose it was given vs copy paste, originality, and purpose" + `popular-web-designs` catalog (182 pullable templates) + `ui-ux-pro-max` product domain.

## Mental Model

- **Template is a material, not a site.** You quarry Linear for `08090a + Inter 510 + 8px + ring border`, Stripe for pricing tables, Airbnb for scroll-snap — then assemble for *one* promise.
- Originality = **purpose-specific assembly + locale detail**, not novelty for novelty. A barbershop that feels like a SaaS docs site is *unoriginal* even if polished.

## Purpose Map → Form

| Purpose (job) | Tone | Layout tells | Example (Caldwell) |
|---|---|---|---|
| Find & get there (local search) | Neighborly, fast | Map-first, NAP + hours + PlaceID above fold | SHOP combined map+bunker, chip `MON CLOSED` etc |
| Scan price without surprise | Blunt, printed | Flat price grid, headliner card ringed, no tricks | `$25/$30/$38` headliner `#EA580C` ring |
| Trust via others | Peer, not corporate | Scroll-snap reviews with source attribution | 6 reviews `Barberhead/Birdeye` `★★★★☆` honest |
| Decide vibe | Venue at midnight, not template | About with locality + competitor context, not lorem | Jan 11 2022 guitar-jam → IG 22 ghost |

## Decision Rules

- Inventory **one sentence** of purpose before layout: "Help a Visalia driver decide in 20s if this Mooney Blvd shop is open, in price, and worth the drive." That sentence deletes Find Us as separate, deletes booking form, deletes dot graph.
- Combine or delete sections whose job duplicates another (we combined Shop+Find Us, deleted Book as separate when no backend).
- Fuse at most 3 template sources per page, cite each in a `<!-- sources: linear.app + stripe + airbnb scroll-snap -->` comment so use is verifiable.

## Verify

- Cover the logo: can a visitor still tell this is a Mooney Blvd barbershop vs any Stripe clone? If not, add locale (map, PlaceID, street mention, price wall photo).

Refs: `popular-web-designs/templates/*.md` catalog; `ui-ux-pro-max` product: barber shop landing.
