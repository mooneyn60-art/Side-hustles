# Side hustles — shared notebook

Shared notebook for Moondog88's side hustles. Claude runs operations. Etsy Studio handles creative and production work for the dog-themed print-on-demand shop and the printable digital products.

This repo is the only place Etsy Studio writes. Do not change Claude's branches or any other repository from here.

## Notes for Claude

### URGENT before Nov 27 — Cyber Week cost check

Source: [etsy-shop/ads/cyber-week-sale-draft.md](etsy-shop/ads/cyber-week-sale-draft.md). The 15% sale is **approved** (Nov 27 12:00am to Dec 1 11:59pm ET). It still does not start until the costs pass. Use no deeper discount. See the 2026-11-15 approval in [DECISIONS.md](DECISIONS.md). Also on file: [etsy-shop/ads/organic-content-2wk.md](etsy-shop/ads/organic-content-2wk.md) and [etsy-shop/ads/ads-test-tracker.md](etsy-shop/ads/ads-test-tracker.md).

1. **Fill in Printify base cost and US shipping** for the tee, bandana, ornament, mug, sweatshirt, and tank. Put the figures in [etsy-shop/SCOREBOARD.md](etsy-shop/SCOREBOARD.md) or a new `etsy-shop/costs.md`. Leave a cell blank until it comes from Printify. Do not estimate.
2. **At the 15% Cyber Week price, cost plus shipping must stay at or under:** tee $9.95, bandana $7.26, ornament $6.50, mug $6.88, sweatshirt $15.30, tank $10.71. Any product over its ceiling gets left out of the sale.
3. **Confirm the live Etsy listing URLs and the Etsy shipping settings.** The $49 free-shipping threshold is Shopify's. Etsy's threshold is unconfirmed. Do not advertise free shipping on Etsy until the live setting is known.
4. **Once the costs pass, schedule the approved Etsy sale** in Etsy Sales & Discounts for the qualifying listings only, and log which listings are included.

### Approved by Moondog88 (relayed via Jarvis, 2026-11-15)

Logged in [DECISIONS.md](DECISIONS.md). The earlier Etsy Ads proposal and the shop-rename item are approved.

1. **Rename the Etsy shop** from PrintanPress to FurEver Faces. This is approved. After the rename, log the date in this notebook.
2. **Etsy Ads test, after the listings are ready.** Once the 5 hero listings (Santa Paws ornament, Santa Paws tee, Doodle Mom tee, Doodle Dad tee, large-print Christmas word search) have their new titles and photos live, turn on Etsy Ads for those 5 only, at $3/day for 10 days (about $30 total). Set a reminder to pause physical items on Dec 5. Record the start date, end date, and daily results in [etsy-shop/SCOREBOARD.md](etsy-shop/SCOREBOARD.md). Do not raise the budget or add listings without new approval.

### Nov 16–Dec 5 posting pack

Source: [etsy-shop/ads/posting-pack.md](etsy-shop/ads/posting-pack.md).

Moondog88 posts the posting-pack himself. Before he can start, fill each `[LINK: ...]` placeholder in `posting-pack.md` with the live Etsy URL once that listing is published, and commit the result. Posts whose listing isn't live yet must wait.

### TOP priority (from the deep dive)

Source: [creative/DEEP-DIVE-2026-11-15.md](creative/DEEP-DIVE-2026-11-15.md). Do these before the rest of the notes. Record results in [etsy-shop/SCOREBOARD.md](etsy-shop/SCOREBOARD.md). Leave a cell blank until it comes from a dashboard. Do not publish anything without Moondog88's okay.

1. **Fill `etsy-shop/SCOREBOARD.md` daily** from the Etsy and Shopify dashboards (views, favorites, orders, revenue, ad spend) and from Printify (cost plus shipping).
2. **Confirm what is actually published on Etsy.** Of the 75 Printify dog products and the 6 built printables, record which are live and write their listing IDs on the scoreboard.
3. **Pull Printify base costs and check the 45% rule.** Supplier cost plus shipping must be at most 45% of price (G6 in the deep dive). Report any listing that fails. Do not change a live price without Moondog88's okay.
4. **SAFETY: great-turing uploads are set to publish.** On branch `claude/great-turing-rqc91h`, the upload script sends to Etsy through Make.com with `publish="yes"`. Switch it to draft-only so nothing publishes without Moondog88's okay.
5. **Dear Santa letter art.** Replace or license-check the Irasutoya-style clip art before any listing. Do not list that product until the art is cleared.
6. **One printables plan.** Merge the etsy-factory work and the great-turing printables work into one plan. Which shop sells them is the open decision below.

### Christmas listing drafts (Listings & SEO)

Source: [etsy-shop/listings/01-christmas-push.md](etsy-shop/listings/01-christmas-push.md) (19 listings in round 2), [etsy-shop/listings/02-catalog.md](etsy-shop/listings/02-catalog.md), [etsy-shop/listings/03-pricing-memo.md](etsy-shop/listings/03-pricing-memo.md). Validator: [etsy-shop/listings/generate_listings.py](etsy-shop/listings/generate_listings.py). Round 2 notes are in the next section.

1. **Paste into Etsy as drafts only.** Use the Christmas listing copy in `etsy-shop/listings/01-christmas-push.md`. Include the Santa Paws ornament and the Doodle Mom tee from `etsy-shop/listings/02-catalog.md`. Publishing waits for Moondog88's okay. Do not set any listing live.
2. **Typo-check the funny-tee wording** against the `fureverfaces` print PNGs before those drafts are saved.
3. **Fill in material, sizes, and care** for the sweatshirts, bandanas, and tanks from the Printify product specs. Do not guess.
4. **Do not paste the 20 drafts that have no Printify ID.** They are backlog in [etsy-shop/listings/05-backlog.md](etsy-shop/listings/05-backlog.md) and will not be created now (9 mugs, 5 ornaments, 6 wall art). Focus on products that already exist. Mug price on the record is $17.99 from `ETSY_STATE.md`, not $18.00. See the 2026-11-15 line appended to [DECISIONS.md](DECISIONS.md).

### Listings round 2

Source: [etsy-shop/listings/01-christmas-push.md](etsy-shop/listings/01-christmas-push.md) (19), [etsy-shop/listings/02-catalog.md](etsy-shop/listings/02-catalog.md) (57), [etsy-shop/listings/04-printables.md](etsy-shop/listings/04-printables.md) (6), [etsy-shop/listings/05-backlog.md](etsy-shop/listings/05-backlog.md) (20), [etsy-shop/listings/03-pricing-memo.md](etsy-shop/listings/03-pricing-memo.md). Checker: [etsy-shop/listings/validate_markdown.py](etsy-shop/listings/validate_markdown.py). Shop name and ornament price are resolved in [DECISIONS.md](DECISIONS.md).

1. **On your own branches, update `ETSY_STATE.md`** so the shop name is FurEver Faces (the rename is approved), and update `BRIEF.md` so the ornament is $16.99 and the Christmas order-by date is Dec 5 for physical items, not Dec 10. Etsy Studio will not edit those branches.
2. **The "Hero bundle" entry in `01-christmas-push.md` has no bundle SKU yet.** Fulfil it as the 3 Santa Paws products on one order, or make it a single Printify listing. Your choice. It should stay a draft until you decide.
3. **Confirm whether the 6 printables use any AI-generated art**, because Etsy requires disclosure if they do. Copy currently says "original designs".

### Valentine's 2027

Source: [etsy-shop/listings/06-valentines.md](etsy-shop/listings/06-valentines.md) and [etsy-shop/ads/valentines-plan.md](etsy-shop/ads/valentines-plan.md). Eight merch concepts (tee, mug, bandana). The art is not made yet. The earlier mid-January draft target is replaced. See the 2026-11-15 Valentine timeline line in [DECISIONS.md](DECISIONS.md): art by Dec 18, drafts ready for review Jan 4, publishing approval by Jan 8, pins start Jan 10. Pins never link to drafts.

1. **Confirm Feb 5 as the Valentine's order-by date** for physical items, using real Printify production and shipping times. Feb 5 is a working date until you confirm it.
2. **Once Product Designer's art is ready, create the 8 Valentine products as unpublished drafts.** Drafts ready for review Jan 4. Do not publish them.

### Valentine printables

Source: [etsy-shop/listings/07-valentine-printables.md](etsy-shop/listings/07-valentine-printables.md). Specs are in the 2026-11-15 Valentine printables line in [DECISIONS.md](DECISIONS.md). Use the same formats as the Christmas printables. Proposed prices (word search $3.99, bingo $3.49, cards $2.99) need Moondog88's okay before going live. The shop is still TBD.

1. **Build these 3 Valentine printables with the etsy-factory pipeline** using those specs: a 24-puzzle word search (about 30 pages, answer key, Letter and A4 PDFs), bingo with 30 cards and 40 calling words, and "From the Dog" classroom cards (24 cards, 8 designs × 3, plus a blank-name version). Aim for drafts by Jan 4.
2. **Keep the upload draft-only (`publish=no`).** Confirm the AI-art disclosure if any art is AI-generated.

### Shop branding (draft)

Source: [etsy-shop/listings/08-shop-branding.md](etsy-shop/listings/08-shop-branding.md).

1. **Do not paste `08-shop-branding.md` into Etsy until Moondog88 okays it** and fills in the **[CONFIRM]** personal details (Mac's details, the shop origin story, the contact path).
2. **Check whether the production and shipping times in `POLICIES_TO_PASTE.md`** (2–5 days production, 3–8 days shipping) also hold for Etsy orders. Then write the Etsy cancellation and refund rules for print-on-demand items, and add the size chart and materials for the tees, sweatshirts, bandanas, and tanks from Printify specs.

### Christmas pins and Dec 1–5 countdown

Source: [etsy-shop/ads/christmas-pins.md](etsy-shop/ads/christmas-pins.md) and [etsy-shop/ads/christmas-countdown-dec1-5.md](etsy-shop/ads/christmas-countdown-dec1-5.md). **Resolved:** Moondog88 posts all Pinterest, Facebook group, and TikTok content personally. Agents prepare the posts and never post them. Mac can be on camera. See [DECISIONS.md](DECISIONS.md).

1. **After the Christmas listings are live, put each real Etsy URL into the [CONFIRM] links in `christmas-pins.md`.**
2. **The bundle pin only goes up once a bundle listing exists.** Until then, link the 3 Santa Paws items separately.
3. **On Dec 6, take down the Dec 5 "last day to order" shop announcement and pin, and switch to the printables copy.**

### Christmas images from Product Designer

Files: [etsy-shop/design/christmas/ornaments/](etsy-shop/design/christmas/ornaments/), [etsy-shop/design/christmas/lifestyle/](etsy-shop/design/christmas/lifestyle/), and [etsy-shop/design/christmas/social/](etsy-shop/design/christmas/social/).

- Upload the Snow, Mom and Dad ornament mockups to their Etsy listing drafts.
- Use `L-bundle-ornament-tree.jpg` as the hero thumbnail for the Santa Paws ornament and the bundle. It stays the hero thumbnail.
- `L-bundle-flatlay.jpg` is fixed and approved as a secondary photo, and the hold is lifted. "NICE LIST" now reads correctly. It can go on the Santa Paws tee, ornament, and bandana. It is not a thumbnail.
- `L-bundle-person-dog` and `L-bundle-unboxing` are cleaned and fine as secondary photos, not thumbnails. They can go on the Santa Paws tee, ornament, and bandana.
- Social crops for the posting pack (square, Pinterest 1000×1500, TikTok 1080×1920) are in `etsy-shop/design/christmas/social/`.
- These are AI scenes with the real print art composited in. Keep the AI-assisted disclosure in the listings.
- Full-res PNGs are on the shared box at `/workspace/etsy-design/christmas/`.
- Valentine art (8 merch, 3 printable covers) is on the box at `/workspace/etsy-design/valentines/` for the Jan 4 drafts.

### Decisions (2026-11-15)

Logged in [DECISIONS.md](DECISIONS.md). Resolved there:

1. **Shop name: FurEver Faces. Resolved.** See [DECISIONS.md](DECISIONS.md). Decided by Moondog88. Use it on every customer-facing surface (listing copy, images, covers, ads, Shopify). Keep "For people owned by a doodle" as the hero line, and "The Doodle Shop" as a secondary tag only. The live Etsy rename from PrintanPress to FurEver Faces is **approved**.
2. **Ornament price: $16.99. Resolved.** See [DECISIONS.md](DECISIONS.md). Price list = `ETSY_STATE.md`: tee $26, sweatshirt $39.99, mug $17.99, ornament $16.99, bandana $18.99, tank $27.99. `ETSY_LISTINGS.md` and `ADS_READY.md` are copy templates. "From $21.99" is wrong; the line is "from $16.99". No live price changes without Moondog88's okay. The Christmas order-by date for physical items is Dec 5 everywhere, which overrides the Dec 10 in `BRIEF.md`.
3. **$49 Shopify free shipping kept.** Otherwise $5.99. Tee + bandana alone is $44.99 and does not qualify. Bundles that clear $49: tee + bandana + ornament $61.98, tee + tank $53.99, sweatshirt + bandana $58.98. Etsy shipping is set separately and still needs Moondog88's okay before any change.
4. **Custom photo art paused.** Ready-made cartoon merch only for Christmas. The Shopify "no photo upload" setting stays. The proof workflow stays in `ORDER_RUNBOOK.md` for later.
5. **Etsy Ads: $3/day test, approved, not on yet.** About $30 over 10 days on five hero listings (Santa Paws ornament, Santa Paws tee, Doodle Mom tee, Doodle Dad tee, large-print Christmas word search). **Approved** by Moondog88. It starts only after those listings have their new titles and photos live. Pause physical items on Dec 5. Do not raise the budget or add listings without new approval. No Pinterest or Facebook paid spend; organic only, per the holiday marketing plan.
6. **Cyber Week sale: approved.** 15% off selected listings, Nov 27 12:00am to Dec 1 11:59pm ET. Only products at or under the 15% cost ceilings. Any product over its ceiling stays out. Use no deeper discount. It is scheduled only after the Printify costs pass.
7. **Mac on camera: approved.** Mac, the real cream/apricot doodle, can be featured on camera in posts and videos.
8. **Who posts: resolved.** Moondog88 posts all Pinterest, Facebook group, and TikTok content personally. Agents prepare the posts and never post them.

Still open:

1. **`ETSY_STATE.md` public repo privacy.** The file on `claude/blissful-allen-waez05` holds the Etsy shop id, Printify store ids, Printify product ids, and a Make.com scenario id. No API tokens were found. Decide whether those IDs should move out of the public repo.
2. **Which shop holds the printables:** PrintanPress, renamed to FurEver Faces, or a new DoodleDesignAndCo shop. See the deep dive (G9 and the ranked plan). Waiting on Moondog88. Don't create a second shop.
3. **Shopify timing:** parked until after Christmas. Do not launch (password, payments, test order) before Dec 26. The store stays up as-is: no changes, no deletion. It's reversible. All holiday effort goes to Etsy.

### Prioritized tasks and deadlines

All dates are America/New_York. Today, when this notebook started, was Sunday, Nov 15, 2026. Thanksgiving is Thursday, Nov 26. The dog shop's Christmas ship cutoff in the files is Dec 5.

1. **This week (by Wed, Nov 18):** Confirm what is actually live on Etsy. Printify product IDs exist as of Nov 14, but the files do not prove listings are published. There is no sales or performance data in the source files. Shopify launch (password off, payments on, test order) is parked until after Christmas. Do not spend time on it before Dec 26. The store stays up as-is.
2. **This week, as soon as #1 is clear:** If the six finished printables are not live, publish them now (Christmas word search, Christmas bingo, Christmas would-you-rather, Thanksgiving word search, Thanksgiving bingo, large-print seniors word search). Do not spend this week building more Thanksgiving SKUs — Thanksgiving is Nov 26, and the Oct 15 research said those needed to be live in October.
3. **This week:** Build and list Christmas trivia (already planned in `skills/etsy-factory/research/demand.md` at $3.49). Put FurEver Faces on every printable cover, and make bingo vs word search visually distinct.
4. **Before Dec 5:** For physical dog merch, lead with a short Christmas list, not the full Printify spray: Santa Paws ornament and tee, Snow Day, Doodle Mom/Dad, and the matching human-tee + dog-bandana sets (Santa / Mom / Dad). Write the missing listing copy for those dog bandanas and tanks. Use the rewritten listings in this repo (see Production log). Ornament price on the record is $16.99 from `ETSY_STATE.md`; check the margin before anything goes live (see the tasks below). The Santa tee + dog bandana pair does not cross the $49 Shopify free-shipping line. At `ETSY_STATE.md` prices it is $26 + $18.99 = $44.99, which is $4.01 short. Bundles that do clear $49: tee + tank $53.99, sweatshirt + bandana $58.98, tee + bandana + ornament $61.98. Shopify keeps the $49 threshold.
5. **Custom photo art is paused** through the Christmas cutoff. Do not sell the personalized Rookie Card / tarot / memorial / photo-on-product line until the end-to-end test below has passed and Moondog88 relaunches it. Aligning the Shopify policies with ready-made only is parked until after Christmas. Do not change the store before Dec 26.
6. **By mid-December:** Valentine's doodle merch (tee/mug/bandana) plus a Valentine's large-print word search and classroom bingo, so listings can index before February. Suggested printable price $2.99–$3.49 and merch at current tee/mug prices — ideas only, not verified market data.
7. **First week of January:** Ship the already-planned sinking-funds/budget planner ($4.99) and weekly meal planner ($3.99), plus a light "Doodle Resolutions" cartoon if capacity allows.

Source-of-truth files (read only; do not edit Claude's branches):

- `mooneyn60-art/skills`, branch `claude/blissful-allen-waez05`: `skills/dropship/ETSY_LISTINGS.md`, `ETSY_STATE.md`, `ADS_READY.md`, `ORDER_RUNBOOK.md`
- `mooneyn60-art/AI-Youtube-Shorts-Generator_SamurAIGPT`, branch `claude/blissful-allen-waez05`: `fureverfaces/`
- `mooneyn60-art/skills`, branch `claude/youtube-monetization-strategy-m9vz6i`: `skills/etsy-factory/`

### Holiday marketing plan (draft)

[etsy-shop/ads/holiday-marketing-plan.md](etsy-shop/ads/holiday-marketing-plan.md) — promo plan through Dec 5, Pinterest, Facebook doodle groups, and corrected `ADS_READY` copy with placeholders. Nothing in it goes live without Moondog88's okay. Shopify free shipping at $49 is kept ([DECISIONS.md](DECISIONS.md)). At `ETSY_STATE.md` prices, Santa tee + dog bandana is $26 + $18.99 = $44.99 ($4.01 short). Bundles that do clear $49: tee + tank $53.99, sweatshirt + bandana $58.98, tee + bandana + ornament $61.98. The Etsy Ads $3/day test is **approved**. It starts only after the 5 hero listings have their new titles and photos live. Organic Pinterest and Facebook only; no paid spend on those channels. **Resolved:** Moondog88 posts the Pinterest, Facebook group, and TikTok content personally. Agents prepare those posts and never post them. Mac can be on camera.

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

1. **Use FurEver Faces branding everywhere** customers see the shop on Etsy: listing copy, images, covers, and ads. Hero line stays "For people owned by a doodle." "The Doodle Shop" is a secondary tag only. The live Etsy rename from PrintanPress to FurEver Faces is **approved**; do it and log the date. Shopify store branding is parked until after Christmas. The store stays as-is.
2. **Correct "from $21.99" to "from $16.99"** in ad copy. All copy, ads, and "from $X" lines use the `ETSY_STATE.md` prices.
3. **Check the ornament margin** against Printify cost plus fees and report it. Keep $16.99 as the record. If the margin is thin, propose $19.99 to Moondog88 instead of jumping to $21.99. No live price change without that okay.
4. **Align the Shopify policies with "ready-made only for now."** Parked until after Christmas. Do not change the store before Dec 26. Keep the proof workflow in `ORDER_RUNBOOK.md` for later.
5. **Run one end-to-end custom-art test** (photo in, proof, Printify order) before the relaunch. Parked until after Christmas; this is a Shopify launch task. After that test passes, the personalized Rookie Card and "The Good Boy" tarot can come back as a separate "Your dog, your art" collection: digital PDF after Dec 5, printed versions for Valentine's.

- 2026-11-15 — Social Studio: first weekly brief added at channels/weekly-briefs/2026-11-16-weekly-brief.md (from Trends & Analytics). Key gaps: no Shorts logged for 11/22–11/24 or 11/26–12/4. Top idea: Bears vs Lions (the actual animals) for the 11/26 game.
- 2026-11-15 — Social Studio: URGENT for tonight's Sun 11/15 21:30 ET slot: TikTok minute cut of bison-wms is drafted at channels/scripts/tt-bison-wms.md (+ .json, tt-grizzly-wms shape) by Scriptwriter. Facts checked against live NPS pages (table inside). Still needs your second-model check, render, postkit lint and transcript check before scheduling. Posting still needs Moondog88's okay.
- 2026-11-15 — Social Studio: metadata (titles, descriptions, tags, TikTok captions, pinned comments) for the nine queued drawn-house bug Shorts (11/14–11/20) is at channels/packaging/bug-shorts-1114-1120.md, from Packaging & Thumbnails. It passes postkit lint except one warning: 5 hashtags vs lint's 4, which follows the written orders (3 topic + #meatballmyths + #shorts), so please reconcile the lint rule. Needs your second-model check before applying; soonest is tonight 19:00 ET cellar-102. The 11/14 slots are already live, so leave them unless Moondog88 okays changes.
- 2026-11-15 — Social Studio (creative director): full deep dive and creative audit at https://cursor.com/canvas/store-959fd15d-66ea-464e-a6af-8ac8f2415014/4774d0bc-99bc-40d9-bc8b-c27f5ad06153
- 2026-11-15 — Social Studio DECISION, Bears vs Lions: option B, the actual animals for the Thanksgiving game (11/26), with sourced weights and speeds, no invented winner, and no team logos or betting. Skip the rushed test and a second dog-turkey video. Scriptwriter is drafting it; packaging follows.
- 2026-11-15 — Social Studio DECISION, monetization: YouTube subs are met, but long-form hours are about 10.5 per 28 days. Priority is weekly long-forms (polar bear 12/5, lion 12/12) plus midweek long-forms, with each Short's Related video pointed at that week's long-form. TikTok: make more 65-90s original cuts (Creator Rewards pays only for videos over 1 minute; Duets and Stitches don't count).
- 2026-11-15 — Social Studio: please fill the empty YouTube Short dates (11/22-11/24 and 11/26-12/04). Scripts and packaging from the team will land in channels/scripts/ and channels/packaging/.
- 2026-11-15 — Social Studio: TikTok minute cut of shark-wms for Mon 11/16 19:00 ET is at channels/scripts/tt-shark-wms.md (+ .json), about 88.9s, with facts matched to live ISAF pages. It needs your second-model check and render. Noodle the dog is planted at L3 with a payoff at L14, but the drawn-house schema has no Noodle key, so Studio needs to draw those shots.
- 2026-11-15 — Social Studio: bison has two variants. The original tt-bison-wms is one swear per line (Nolan's 11/11 rule). tt-bison-wms-v2 has fewer swears and plants Noodle early. Moondog88 picks; use the original for tonight unless told otherwise.
- 2026-11-15 — Social Studio: Trends reads are in channels/analytics/. Pause custom Shorts cover frames: the only Short with one, dog guilty-look, is stuck at 3 views. Pet/WMS Shorts are level with bugs (median ~922 vs 1,100, small sample). Confirmed open YouTube Short slots: 11/21 19:00, 11/22-11/24, 11/25 10:00, 11/26-12/04. Please pull Windsor retention for the new Shorts.
- 2026-11-15 — Social Studio: audit packaging from Packaging & Thumbnails is in channels/packaging/: title-formula.md (5 locked rewrites), thumbnail-concepts.md, tiktok-caption-template.md, bears-vs-lions.md, can-cats-eat-turkey.md, related-video-rule.md, kw/kw-studio-assignments.csv. Rulings: (1) TikTok hashtags follow MASTER_ORDERS (five topic tags, no brand tag); Social Studio's earlier 3+brand suggestion is withdrawn. (2) Related video: on-topic Shorts point at that week's long-form, others at the show playlist, as MASTER_ORDERS says. (3) The Saturday long-form order (lion 11/28 vs 12/12, dog 12/12 vs 12/19, wolf 12/26) follows CALENDAR_REALISTIC; please confirm with Nolan. Bears vs Lions and cats-turkey copy are draft-only until fact packs exist. Everything needs your second-model check before applying.
- 2026-11-15 — Social Studio + Etsy Studio: FurEver Faces TikTok Shop launch plan (prep only) is at channels/tiktok-shop/launch-plan.md. It has 8 products and 8 shop-tagged Meatball/Noodle videos at 15:00 ET, 3-4 a week, Nov 17-Dec 3. Shop posts stay separate from the 65-90s Creator Rewards cuts. Nothing is listed or published until Moondog88 okays the checklist at the top.
- 2026-11-15 — Social Studio: (1) Bears vs Lions Short + minute-cut drafts and both fact packs are in channels/ (facts/bears-vs-lions.md, facts/cats-turkey.md, scripts/bears-vs-lions-v6-yt.json, scripts/tts-bears-vs-lions.json ~19.9s, scripts/tt-bears-vs-lions.json ~89.6s); nothing is approved to post. The TikTok minute cut is a DRAFT in a 4-5 swear style that is NOT the current rule; a one-swear-per-line default version is coming and will replace it as the default. (2) Correction from Social Studio: hashtags follow MASTER_ORDERS per platform: YouTube descriptions keep three topic tags then #meatballmyths then #shorts last (line 101); the five-topic-tags, no-brand rule is TikTok captions only (line 103). (3) Staging issues for Claude's pipeline: two animals in the Bears vs Lions scripts use a nonstandard other_creature key, and Noodle has no character key yet; please add proper keys or say which existing key to use.
- 2026-11-15 — Social Studio: Mac-on-camera versions of the 8 shop-tagged videos, with the no-Mac fallbacks, are at channels/tiktok-shop/mac-videos.md. PREP ONLY. Mac on camera is pending Moondog88's direct yes and a STYLE LOCK exception, so nothing here is approved to post.
- 2026-11-15 — Social Studio: Bears vs Lions and Can Cats Eat Turkey scripts are ready for Claude's second-model check and render. channels/scripts/tt-bears-vs-lions.json now replaces the earlier draft as the one-swear-per-line default (~91.8s); tt-bears-vs-lions-v2.json is the lighter alternative. New: cats-turkey-v6-yt.json and tts-cats-turkey.json (YouTube Short ~18.7s), tt-cats-turkey.json (TikTok minute cut ~91.8s), plus cats-turkey.md and bears-vs-lions.md. The cats Short still needs an episode number and an on-topic Related video target. Facts cite channels/facts/. Nothing is approved to post.
- 2026-11-15 — Social Studio: (1) packaging for Bears vs Lions and Can Cats Eat Turkey, the 14 open YouTube Short slots 11/21-12/04 (some slot times assumed; adjust to the real queue), and the 8 TikTok Shop captions are drafts needing the second-model check; nothing approved to post or schedule. Files: channels/packaging/bears-vs-lions.md, can-cats-eat-turkey.md, open-dates-1121-1204.md, tiktok-shop-captions.md. (2) postkit lint still expects 4 YouTube hashtags but MASTER_ORDERS line 101 gives 5 (3 topic, #meatballmyths, #shorts); please fix the lint. (3) CALENDAR_REALISTIC.md is a Shorts episode bank, not a Saturday long-form calendar, so the long-form order after the 12/5 polar bear is unset: question for Nolan. (4) Shop videos 2 and 6 hooks are being rewritten off the WMS frame and the AI-art disclosure moved before the question; updated files to follow.
- 2026-11-15 — Social Studio: character bible (channels/meatball-bible.md) plus Why Dogs Lick (~73s TT: channels/scripts/tt-dogs-lick.json, dogs-lick.md; facts channels/facts/dogs-lick.md), Why Cats Knead (~89s TT: tt-cats-knead.json, cats-knead.md; facts cats-knead.md) and December chocolate (YT Short ~19.9s: chocolate-v6-yt.json, tts-chocolate.json, chocolate.md; facts chocolate.md; call-your-vet line on last card and description) are drafted; they need the second-model check with sources re-fetched, render, Noodle/Sauce character keys, and episode number/Related fields; nothing approved to post.
- 2026-11-15 — Social Studio: (1) Why Dogs Lick and Why Cats Knead now have YouTube Shorts too (channels/scripts/dogs-lick-v6-yt.json, tts-dogs-lick.json, dogs-lick-short.md; cats-knead-v6-yt.json, tts-cats-knead.json, cats-knead-short.md). Packaging replacements: channels/packaging/why-dogs-lick.md and why-cats-knead.md. Proposed house numbers #71 dogs lick (Sun 12/06 14:00 ET) and #72 cats knead (Mon 12/07 16:00 ET), Related = house playlist; second-model check owed. (2) Two TikTok-native originals (channels/scripts/tt-native-pov.json/.md and tt-native-comment-reply.json/.md, a reusable comment-reply template with a {{COMMENT_TEXT}} slot, no Duets/Stitches) need new drawn-house layers before they can render properly: a first-person camera, drawn source-page plates, and a comment-reply bar. Without them they fall back to ordinary rooms; please build or say what's feasible. Social Studio approved the POV format as a test: jokes stay on Meatball's actions, never on the viewer's looks, smarts or choices. Nothing approved to post.
- 2026-11-15 — Social Studio: (1) Social Scriptwriter is drafting the lion born-as fact pack and 'Your Life as a Lion' script (8-12 min, same structure as your polar born-as), aiming for Thu 11/26 so the Sat 11/28 slot in MASTER_ORDERS line 217 is possible, else 12/12 per line 69; tell us if you already have lion work so we don't duplicate. See channels/packaging/longform-polar-lion.md. (2) MASTER_ORDERS' watch-hours line still lists dog for 12/12, which contradicts line 69 (lion 12/12, dog 12/19); please reconcile. (3) Social team will not write a separate polar long-form; yours stands.
- 2026-11-15 — Social Studio: 'Your Life as a Lion: 8 Things You Have to Get Through' long-form is drafted (~9:37 at 194.5 wpm, about 10:21 at the polar video's pace; same keys as your polar born-as script; mild words only), aiming for Sat 11/28 if ready by Thu 11/26, otherwise 12/12. Files: channels/facts/lion-bornas.md, channels/facts/polar-bear-additions.md (additions only to Claude's polar pack), channels/scripts/longform-lion-bornas.json, longform-lion-bornas.md, lion-teasers.md. Revisions are coming: the Kruger lines s9.l3/s9.l4 get cut unless an official page is found, the Stander citation is being fixed, and teaser 2 is switching to the resting-lion Short. For Claude: second-model fact check, render, and transcript check; the JSON's builder 'drawn_polarlife' is a guess, so a lion shot set is needed; check TTS pronunciation of 'estrus' and 'Etosha'; reconcile MASTER_ORDERS line 217 (dog 12/12) with line 69 (lion 12/12, dog 12/19); polar-bear-additions.md adds USFWS/Parks Canada safety and NPS rows if useful. Nothing approved to post.
- 2026-11-15 — Social Studio: lion revisions done. Title 'Your Life as a Lion: 8 Things You Have to Get Through', ~9:12 at 194.5 wpm (~9:55 at polar pace). Files replaced: channels/facts/lion-bornas.md, channels/scripts/longform-lion-bornas.json, longform-lion-bornas.md, lion-teasers.md. Kruger lines s9.l3/s9.l4 kept, now citing the official SANParks page https://www.sanparks.org/parks/kruger/useful-information/vital-information (it returns 403 to plain curl, so the checker should fetch it with a web-fetch tool). Stander citation corrected to 1992 (Behav Ecol Sociobiol 29:445-454). Takeover chapter trimmed, no Short mentions cub-killing. Teaser dates: Plan A 11/23, 11/24, 11/27 for an 11/28 long-form; Plan B 12/8, 12/9, 12/11 for 12/12. Pronunciation and lion shot-set needs are in the script's 'For Claude' list. Second-model check, render, transcript check still owed; nothing approved to post.

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

- Shop name and ornament price are resolved in [DECISIONS.md](DECISIONS.md) (FurEver Faces; ornament $16.99). Apply those before pasting the ornament listing live.
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

### 2026-11-15 — Etsy Studio

2026-11-15, Etsy Studio, deep dive vs goals (creative/DEEP-DIVE-2026-11-15.md) and scoreboard template.

Files: [creative/DEEP-DIVE-2026-11-15.md](creative/DEEP-DIVE-2026-11-15.md), [etsy-shop/SCOREBOARD.md](etsy-shop/SCOREBOARD.md)

### 2026-11-15 — Etsy: Listings & SEO

2026-11-15, Etsy: Listings & SEO, 95 listings rewritten (16 Christmas push, 79 catalog) plus pricing memo; validator at etsy-shop/listings/generate_listings.py.

Files: [etsy-shop/listings/01-christmas-push.md](etsy-shop/listings/01-christmas-push.md), [etsy-shop/listings/02-catalog.md](etsy-shop/listings/02-catalog.md), [etsy-shop/listings/03-pricing-memo.md](etsy-shop/listings/03-pricing-memo.md), [etsy-shop/listings/generate_listings.py](etsy-shop/listings/generate_listings.py)

### 2026-11-15 — Etsy: Listings & SEO, round 2

Listings & SEO round 2, 19 Christmas plus 57 catalog plus 6 printables plus 20 backlog, all 12 funny-tee slogans typo-checked against the PNGs.

Files: [etsy-shop/listings/01-christmas-push.md](etsy-shop/listings/01-christmas-push.md), [etsy-shop/listings/02-catalog.md](etsy-shop/listings/02-catalog.md), [etsy-shop/listings/03-pricing-memo.md](etsy-shop/listings/03-pricing-memo.md), [etsy-shop/listings/04-printables.md](etsy-shop/listings/04-printables.md), [etsy-shop/listings/05-backlog.md](etsy-shop/listings/05-backlog.md), [etsy-shop/listings/validate_markdown.py](etsy-shop/listings/validate_markdown.py)

### 2026-11-15 — Etsy: Product Designer

Product Designer, Christmas ornament mockups (Snow/Mom/Dad), 4 bundle lifestyle images, 8 Valentine merch files, 3 Valentine printable covers.

Files: [etsy-shop/design/christmas/ornaments/](etsy-shop/design/christmas/ornaments/), [etsy-shop/design/christmas/lifestyle/](etsy-shop/design/christmas/lifestyle/). Full-res PNGs and Valentine art are on the shared box at `/workspace/etsy-design/christmas/` and `/workspace/etsy-design/valentines/`.
