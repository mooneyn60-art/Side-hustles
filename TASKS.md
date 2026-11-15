# Side hustles — shared notebook

Shared notebook for Moondog88's side hustles. Claude runs operations. Etsy Studio handles creative and production work for the dog-themed print-on-demand shop and the printable digital products.

This repo is the only place Etsy Studio writes. Do not change Claude's branches or any other repository from here.

## Notes for Claude

### Decisions (2026-11-15)

Logged in [DECISIONS.md](DECISIONS.md). Resolved there:

1. **Shop name: FurEver Faces.** Decided by Moondog88. Use it on every customer-facing surface (listing copy, images, covers, ads, Shopify). Keep "For people owned by a doodle" as the hero line, and "The Doodle Shop" as a secondary tag only.
2. **Price list = `ETSY_STATE.md`.** Tee $26, sweatshirt $39.99, mug $17.99, ornament $16.99, bandana $18.99, tank $27.99. `ETSY_LISTINGS.md` and `ADS_READY.md` are copy templates. "From $21.99" is wrong; the line is "from $16.99". No live price changes without Moondog88's okay.
3. **$49 Shopify free shipping kept.** Otherwise $5.99. Tee + bandana alone is $44.99 and does not qualify. Bundles that clear $49: tee + bandana + ornament $61.98, tee + tank $53.99, sweatshirt + bandana $58.98. Etsy shipping is set separately and still needs Moondog88's okay before any change.
4. **Custom photo art paused.** Ready-made cartoon merch only for Christmas. The Shopify "no photo upload" setting stays. The proof workflow stays in `ORDER_RUNBOOK.md` for later.
5. **Etsy Ads: $3/day test, not on.** About $30 over 10 days on five hero listings (Santa Paws ornament, Santa Paws tee, Doodle Mom tee, Doodle Dad tee, large-print Christmas word search), and only after the new titles, tags, and real-photo thumbnails are up. Awaiting Moondog88's approval. No Pinterest or Facebook paid spend; organic only, per the holiday marketing plan.

Still open, and only these:

1. **Approve the Etsy Ads test** ($3/day, as above).
2. **Approve the Etsy shop rename** from PrintanPress to FurEver Faces. Branding is FurEver Faces now; the live Etsy rename waits for this okay.
3. **`ETSY_STATE.md` public repo privacy.** The file on `claude/blissful-allen-waez05` holds the Etsy shop id, Printify store ids, Printify product ids, and a Make.com scenario id. No API tokens were found. Decide whether those IDs should move out of the public repo.

### Prioritized tasks and deadlines

All dates are America/New_York. Today, when this notebook started, was Sunday, Nov 15, 2026. Thanksgiving is Thursday, Nov 26. The dog shop's Christmas ship cutoff in the files is Dec 5.

1. **This week (by Wed, Nov 18):** Confirm what is actually live on Etsy and Shopify. Printify product IDs exist as of Nov 14, but the files do not prove listings are published. Shopify, as of Nov 14, still needed the store password removed, payments turned on, and a test order (Nolan only). There is no sales or performance data in the source files.
2. **This week, as soon as #1 is clear:** If the six finished printables are not live, publish them now (Christmas word search, Christmas bingo, Christmas would-you-rather, Thanksgiving word search, Thanksgiving bingo, large-print seniors word search). Do not spend this week building more Thanksgiving SKUs — Thanksgiving is Nov 26, and the Oct 15 research said those needed to be live in October.
3. **This week:** Build and list Christmas trivia (already planned in `skills/etsy-factory/research/demand.md` at $3.49). Put FurEver Faces on every printable cover, and make bingo vs word search visually distinct.
4. **Before Dec 5:** For physical dog merch, lead with a short Christmas list, not the full Printify spray: Santa Paws ornament and tee, Snow Day, Doodle Mom/Dad, and the matching human-tee + dog-bandana sets (Santa / Mom / Dad). Write the missing listing copy for those dog bandanas and tanks. Use the rewritten listings in this repo (see Production log). Ornament price on the record is $16.99 from `ETSY_STATE.md`; check the margin before anything goes live (see the tasks below). The Santa tee + dog bandana pair does not cross the $49 Shopify free-shipping line. At `ETSY_STATE.md` prices it is $26 + $18.99 = $44.99, which is $4.01 short. Bundles that do clear $49: tee + tank $53.99, sweatshirt + bandana $58.98, tee + bandana + ornament $61.98. Shopify keeps the $49 threshold.
5. **Custom photo art is paused** through the Christmas cutoff. Do not sell the personalized Rookie Card / tarot / memorial / photo-on-product line until the end-to-end test below has passed and Moondog88 relaunches it. `ADS_READY.md` and the Shopify policies still disagree on whether custom art is offered; align the policies with ready-made only.
6. **By mid-December:** Valentine's doodle merch (tee/mug/bandana) plus a Valentine's large-print word search and classroom bingo, so listings can index before February. Suggested printable price $2.99–$3.49 and merch at current tee/mug prices — ideas only, not verified market data.
7. **First week of January:** Ship the already-planned sinking-funds/budget planner ($4.99) and weekly meal planner ($3.99), plus a light "Doodle Resolutions" cartoon if capacity allows.

Source-of-truth files (read only; do not edit Claude's branches):

- `mooneyn60-art/skills`, branch `claude/blissful-allen-waez05`: `skills/dropship/ETSY_LISTINGS.md`, `ETSY_STATE.md`, `ADS_READY.md`, `ORDER_RUNBOOK.md`
- `mooneyn60-art/AI-Youtube-Shorts-Generator_SamurAIGPT`, branch `claude/blissful-allen-waez05`: `fureverfaces/`
- `mooneyn60-art/skills`, branch `claude/youtube-monetization-strategy-m9vz6i`: `skills/etsy-factory/`

### Holiday marketing plan (draft)

[etsy-shop/ads/holiday-marketing-plan.md](etsy-shop/ads/holiday-marketing-plan.md) — promo plan through Dec 5, Pinterest, Facebook doodle groups, and corrected `ADS_READY` copy with placeholders. Nothing in it goes live without Moondog88's okay. Shopify free shipping at $49 is kept ([DECISIONS.md](DECISIONS.md)). At `ETSY_STATE.md` prices, Santa tee + dog bandana is $26 + $18.99 = $44.99 ($4.01 short). Bundles that do clear $49: tee + tank $53.99, sweatshirt + bandana $58.98, tee + bandana + ornament $61.98. The Etsy Ads proposal is now a $3/day test and is still awaiting Moondog88's approval. Organic Pinterest and Facebook only until then.

### Design direction (2026-11-15)

Source: [etsy-shop/design/design-direction-2026-11-15.md](etsy-shop/design/design-direction-2026-11-15.md). Do not edit Claude's branches from this notebook; these are the tasks to pick up there.

1. **Before the Dec 5 cutoff:** Build the Christmas listing photos from the shot lists in that file. Export every slot at 2000×2000, 1:1, in the 10-slot order (thumbnail lifestyle, Printify on-product front, detail/macro, second lifestyle, scale/in-hand, back or second angle, color/size variants, matching set if any, gift-context, size chart / materials). Real photos are preferred for thumbnails.
2. **Make the missing ornament mockups** for Snow Day, Doodle Mom, and Doodle Dad. Printify has `orn-snow`, `orn-mom`, and `orn-dad`; `fureverfaces/` has no local ornament mockup for those three.
3. **Fix the logo tagline color** from `#14100E` to `#FFF2DE` on `fureverfaces/logo/mac-shopify-logo.png` ("THE DOODLE SHOP" on the black Shopify lockup).
4. **Replace the 640×800 upscaled pipeline art** with higher-res output for print. Personalized renders start at 640×800 and are enlarged, which is soft on a 16×20 canvas.
5. **Fill the "December [DATE]" placeholder** in `fureverfaces/policies.md` with Dec 5, so it matches the Christmas cutoff already in the ads and listings.
6. **Give each printable type its own cover layout and add the shop name FurEver Faces.** Bingo and word search currently share one template with the title swapped, and the covers do not name the shop.

### From the decisions log

Source: [DECISIONS.md](DECISIONS.md).

1. **Use FurEver Faces branding everywhere** customers see the shop: listing copy, images, covers, ads, and Shopify. Hero line stays "For people owned by a doodle." "The Doodle Shop" is a secondary tag only. Do not rename the live Etsy shop from PrintanPress until Moondog88 approves that change.
2. **Correct "from $21.99" to "from $16.99"** in ad copy. All copy, ads, and "from $X" lines use the `ETSY_STATE.md` prices.
3. **Check the ornament margin** against Printify cost plus fees and report it. Keep $16.99 as the record. If the margin is thin, propose $19.99 to Moondog88 instead of jumping to $21.99. No live price change without that okay.
4. **Align the Shopify policies with "ready-made only for now."** Soften or remove custom-art promises so they match the paused photo-upload setting. Keep the proof workflow in `ORDER_RUNBOOK.md` for later.
5. **Run one end-to-end custom-art test** (photo in, proof, Printify order) before the relaunch. After that test passes, the personalized Rookie Card and "The Good Boy" tarot can come back as a separate "Your dog, your art" collection: digital PDF after Dec 5, printed versions for Valentine's.

- 2026-11-15 — Social Studio: first weekly brief added at channels/weekly-briefs/2026-11-16-weekly-brief.md (from Trends & Analytics). Key gaps: no Shorts logged for 11/22–11/24 or 11/26–12/4. Top idea: Bears vs Lions (the actual animals) for the 11/26 game.
- 2026-11-15 — Social Studio: URGENT for tonight's Sun 11/15 21:30 ET slot: TikTok minute cut of bison-wms is drafted at channels/scripts/tt-bison-wms.md (+ .json, tt-grizzly-wms shape) by Scriptwriter. Facts checked against live NPS pages (table inside). Still needs your second-model check, render, postkit lint and transcript check before scheduling. Posting still needs Moondog88's okay.
- 2026-11-15 — Social Studio: metadata (titles, descriptions, tags, TikTok captions, pinned comments) for the nine queued drawn-house bug Shorts (11/14–11/20) is at channels/packaging/bug-shorts-1114-1120.md, from Packaging & Thumbnails. It passes postkit lint except one warning: 5 hashtags vs lint's 4, which follows the written orders (3 topic + #meatballmyths + #shorts), so please reconcile the lint rule. Needs your second-model check before applying; soonest is tonight 19:00 ET cellar-102. The 11/14 slots are already live, so leave them unless Moondog88 okays changes.

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

### 2026-11-15 — Etsy Studio

2026-11-15, Etsy Studio, decisions logged in DECISIONS.md.

File: [DECISIONS.md](DECISIONS.md)
