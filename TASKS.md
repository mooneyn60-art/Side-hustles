# Side hustles — shared notebook

Shared notebook for Moondog88's side hustles. Claude runs operations. Etsy Studio handles creative and production work for the dog-themed print-on-demand shop and the printable digital products.

This repo is the only place Etsy Studio writes. Do not change Claude's branches or any other repository from here.

## Notes for Claude

### Decisions awaiting Moondog88 (block publishing until answered)

1. **Shop name, customer-facing:** PrintanPress (the Etsy shop name in `skills/dropship/ETSY_STATE.md` on `claude/blissful-allen-waez05`, shop id 38484468) vs FurEver Faces (the brand in logos, policies, ads, and listing docs). Recommendation from the Nov 15 audit: use FurEver Faces everywhere customers see the shop; do not lead with PrintanPress.
2. **Ornament price:** $16.99 in `skills/dropship/ETSY_STATE.md` vs $21.99 in `skills/dropship/ETSY_LISTINGS.md`. Check actual Printify cost plus shipping, then pick one price and use it in every Santa Paws / Snow Day / Mom / Dad ornament listing. Do not paste listing copy live until this is decided.
3. **Shopify "no photo upload" vs the custom-art runbook:** `ADS_READY.md` says no custom art and no photo upload. `ORDER_RUNBOOK.md` is a photo-to-art flow (pet name and pet photo, proof before print). Personalized Rookie Card / tarot cannot check out on a storefront that cannot collect a photo. Decide which setting is live before that line is advertised. Detail is in [etsy-shop/design/design-direction-2026-11-15.md](etsy-shop/design/design-direction-2026-11-15.md).
4. **Whether `ETSY_STATE.md` should leave the public repo:** On `claude/blissful-allen-waez05` it holds the Etsy shop id, Printify store ids, Printify product ids, and a Make.com scenario id. No API tokens were found. Decide whether those shop, store, product, and Make.com IDs should move out of the public repo.

### Prioritized tasks and deadlines

All dates are America/New_York. Today, when this notebook started, was Sunday, Nov 15, 2026. Thanksgiving is Thursday, Nov 26. The dog shop's Christmas ship cutoff in the files is Dec 5.

1. **This week (by Wed, Nov 18):** Confirm what is actually live on Etsy and Shopify. Printify product IDs exist as of Nov 14, but the files do not prove listings are published. Shopify, as of Nov 14, still needed the store password removed, payments turned on, and a test order (Nolan only). There is no sales or performance data in the source files.
2. **This week, as soon as #1 is clear:** If the six finished printables are not live, publish them now (Christmas word search, Christmas bingo, Christmas would-you-rather, Thanksgiving word search, Thanksgiving bingo, large-print seniors word search). Do not spend this week building more Thanksgiving SKUs — Thanksgiving is Nov 26, and the Oct 15 research said those needed to be live in October.
3. **This week:** Build and list Christmas trivia (already planned in `skills/etsy-factory/research/demand.md` at $3.49). Put a shop name on every printable cover once decision 1 is made, and make bingo vs word search visually distinct.
4. **Before Dec 5:** For physical dog merch, lead with a short Christmas list, not the full Printify spray: Santa Paws ornament and tee, Snow Day, Doodle Mom/Dad, and the matching human-tee + dog-bandana sets (Santa / Mom / Dad). Write the missing listing copy for those dog bandanas and tanks. Use the rewritten listings in this repo (see Production log) after the ornament price is decided. The Santa tee + dog bandana pair does not cross a $49 free-shipping line. At `ETSY_STATE.md` prices it is $26 + $18.99 = $44.99, which is $4.01 short. Bundles that do clear $49: tee + tank $53.99, sweatshirt + bandana $58.98, tee + bandana + ornament $61.98. The $49 threshold is **[CONFIRM]**.
5. **Before advertising custom art:** Do not sell the personalized Rookie Card / tarot / memorial / photo-on-product line until Shopify payments, a test order, and the proof-email step actually work. `ADS_READY.md` and the Shopify policies still disagree on whether custom art is offered.
6. **By mid-December:** Valentine's doodle merch (tee/mug/bandana) plus a Valentine's large-print word search and classroom bingo, so listings can index before February. Suggested printable price $2.99–$3.49 and merch at current tee/mug prices — ideas only, not verified market data.
7. **First week of January:** Ship the already-planned sinking-funds/budget planner ($4.99) and weekly meal planner ($3.99), plus a light "Doodle Resolutions" cartoon if capacity allows.

Source-of-truth files (read only; do not edit Claude's branches):

- `mooneyn60-art/skills`, branch `claude/blissful-allen-waez05`: `skills/dropship/ETSY_LISTINGS.md`, `ETSY_STATE.md`, `ADS_READY.md`, `ORDER_RUNBOOK.md`
- `mooneyn60-art/AI-Youtube-Shorts-Generator_SamurAIGPT`, branch `claude/blissful-allen-waez05`: `fureverfaces/`
- `mooneyn60-art/skills`, branch `claude/youtube-monetization-strategy-m9vz6i`: `skills/etsy-factory/`

### Holiday marketing plan (draft)

[etsy-shop/ads/holiday-marketing-plan.md](etsy-shop/ads/holiday-marketing-plan.md) — promo plan through Dec 5, Pinterest, Facebook doodle groups, corrected `ADS_READY` copy with placeholders, and an Etsy Ads suggestion ($1–$3/day test or $5/day). Nothing in it goes live without Moondog88's okay. Open **[CONFIRM]** items are in Appendix D. The $49 free-shipping threshold in that plan is **[CONFIRM]**. At `ETSY_STATE.md` prices, Santa tee + dog bandana is $26 + $18.99 = $44.99 ($4.01 short). Bundles that do clear $49: tee + tank $53.99, sweatshirt + bandana $58.98, tee + bandana + ornament $61.98.

### Design direction (2026-11-15)

Source: [etsy-shop/design/design-direction-2026-11-15.md](etsy-shop/design/design-direction-2026-11-15.md). Do not edit Claude's branches from this notebook; these are the tasks to pick up there.

1. **Before the Dec 5 cutoff:** Build the Christmas listing photos from the shot lists in that file. Export every slot at 2000×2000, 1:1, in the 10-slot order (thumbnail lifestyle, Printify on-product front, detail/macro, second lifestyle, scale/in-hand, back or second angle, color/size variants, matching set if any, gift-context, size chart / materials). Real photos are preferred for thumbnails.
2. **Make the missing ornament mockups** for Snow Day, Doodle Mom, and Doodle Dad. Printify has `orn-snow`, `orn-mom`, and `orn-dad`; `fureverfaces/` has no local ornament mockup for those three.
3. **Fix the logo tagline color** from `#14100E` to `#FFF2DE` on `fureverfaces/logo/mac-shopify-logo.png` ("THE DOODLE SHOP" on the black Shopify lockup).
4. **Replace the 640×800 upscaled pipeline art** with higher-res output for print. Personalized renders start at 640×800 and are enlarged, which is soft on a 16×20 canvas.
5. **Fill the "December [DATE]" placeholder** in `fureverfaces/policies.md` with Dec 5, so it matches the Christmas cutoff already in the ads and listings.
6. **Give each printable type its own cover layout and add the shop name.** Bingo and word search currently share one template with the title swapped, and the covers do not name the shop.

- 2026-11-15 — Social Studio: first weekly brief added at channels/weekly-briefs/2026-11-16-weekly-brief.md (from Trends & Analytics). Key gaps: no Shorts logged for 11/22–11/24 or 11/26–12/4. Top idea: Bears vs Lions (the actual animals) for the 11/26 game.

## Production log

When Claude's usage runs out, Etsy Studio does the production work (listing copy, design files, product prep) and logs each item here: date, what was done, file paths, and what Claude should pick up next.

### 2026-11-15 (America/New_York) — Etsy Studio

What was done: Read-only creative audit of both the FurEver Faces dog shop and the etsy-factory printables, then the first commit on `main` in this notebook. Produced a full audit (snapshot, what's strong, what's weak, 10 upgrades) plus 3 rewritten ready-to-paste listings (Santa Paws ornament, Doodle Mom tee, Christmas word search large print), with titles, 13 tags, full descriptions, and price notes.

Committed on `main`:

- [creative/AUDIT-2026-11-15.md](https://github.com/mooneyn60-art/Side-hustles/blob/main/creative/AUDIT-2026-11-15.md)
- [listings/santa-paws-ornament.md](https://github.com/mooneyn60-art/Side-hustles/blob/main/listings/santa-paws-ornament.md)
- [listings/doodle-mom-tee.md](https://github.com/mooneyn60-art/Side-hustles/blob/main/listings/doodle-mom-tee.md)
- [listings/christmas-word-search-large-print.md](https://github.com/mooneyn60-art/Side-hustles/blob/main/listings/christmas-word-search-large-print.md)
- This file: [TASKS.md](https://github.com/mooneyn60-art/Side-hustles/blob/main/TASKS.md)

What Claude should pick up next:

- Get Moondog88's two decisions (shop name; ornament price) and apply them before pasting the ornament listing live.
- Confirm live vs draft status on Etsy and Shopify (no sales data was in the source files).
- If the six finished printables are not live, publish them; build Christmas trivia this week. Do not spend time on more Thanksgiving SKUs.
- Write missing listing copy for the Santa/Mom/Dad dog bandanas and tanks before adding more cartoon designs.
- Do not advertise custom pet-photo art until Shopify payments, a test order, and the proof-email step actually work.

### 2026-11-15 — Etsy: Marketing & Ads

2026-11-15, Etsy: Marketing & Ads, holiday marketing plan drafted (promo plan to Dec 5, Pinterest, Facebook doodle groups, corrected ADS_READY copy with placeholders, Etsy Ads suggestion of $1-3/day test or $5/day pending Moondog88 approval); open [CONFIRM] items in Appendix D.

File: [etsy-shop/ads/holiday-marketing-plan.md](etsy-shop/ads/holiday-marketing-plan.md)

### 2026-11-15 — Etsy: Product Designer

2026-11-15, Etsy: Product Designer, design direction delivered (Christmas shot lists, Valentine's and Doodle Resolutions briefs, Rookie Card/tarot premium formats, printable cover fixes, logo contrast fix).

File: [etsy-shop/design/design-direction-2026-11-15.md](etsy-shop/design/design-direction-2026-11-15.md)
