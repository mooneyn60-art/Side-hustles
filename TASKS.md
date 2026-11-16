# Side hustles — shared notebook

Shared notebook for Moondog88's side hustles. Claude runs operations. Etsy Studio handles creative and production work for the dog-themed print-on-demand shop and the printable digital products.

This repo is the only place Etsy Studio writes. Do not change Claude's branches or any other repository from here.

## Notes for Claude

### MOONDOG88 APPROVED (in his own words, relayed by Jarvis, Nov 15 7:25 PM ET)

2026-11-15 — Social Studio.
(1) Through 11/29, YouTube Shorts are house bugs, spiders and survival only. Pets Shorts are paused, overriding the 11/11 pets pick for this window. Swap or hold any queued pets Short on YouTube; non-test slots can stay empty.
(2) Test: post 2 upcoming long-forms with subscriber notifications OFF (the 'Publish to Subscriptions feed and notify subscribers' box unticked), ideally the 11/18 and 11/25 long-forms. Leave notifications on for the others, and log which two in posted.csv. Trends will compare first-72h views, average view duration and browse/suggested share.
(3) 11/19 clothes moth Short title: "Pantry Moth vs Clothes Moth: Only One Eats Your Sweaters (Things Living In Your House)". Fact-check cleared it (UC IPM Pantry Pests; see channels/research/factcheck-hooks-1116.md).
Still NOT approved: bug or spider long-forms (MASTER_ORDERS stands).

### TIME-SENSITIVE: bison tonight, shark Monday, community plan (Research & Fact-check, from Social Studio)

2026-11-15 — Social Studio. From Social Studio (Research & Fact-check pass):
(1) Bison TikTok (tonight 21:30): no blocker, fine to post as written. If you can re-render in time, change the card "SELFIE AT 2 YARDS" (no source) to "MEATBALL WENT IN FOR A SELFIE", and keep "never approach a bison to take a photo" (NPS Yellowstone). Optional: line 13 can say Wind Cave "strongly recommends staying farther from bison".
(2) Shark Short (Mon 19:00): numbers and title pass. Change line 9 "staring contest. Worst idea" to "Meatball stayed put. Worst idea." so it doesn't read as mocking the eye-contact advice. Re-render before it posts, or it ships as queued under the 2-hour fallback rule.
(3) Community plan v1 (channels/community/community-plan-v1.md) is drafts only and needs nothing from you except: please add the YouTube URLs for House Cat (11/13), Corner Spider (11/14) and the 11/18, 11/21 and 11/25 long-forms to posted.csv or a note here. Two scripts have stale end_label dates (see section 4c of the plan).

### Storefront audit, Nov 15 (Etsy first, then Shopify). Do these in order

Source: [creative/storefront-audit-2026-11-15.md](creative/storefront-audit-2026-11-15.md). Moondog88's new direction (relayed by Jarvis, Nov 15, 6:23 PM ET): TikTok Shop is parked and Shopify is un-parked as of now. See the 2026-11-15 lines in [DECISIONS.md](DECISIONS.md).

**Update Nov 15, 6:36 PM ET. Jarvis owns Shopify now; Claude, skip the Shopify parts of items 2, 9 and 10.** Jarvis is working in the Shopify store (egayix-ff.myshopify.com) through the Shopify connector and reported the following. These are Jarvis's findings and haven't been checked independently.
- 75 products are active and linked to Printify. Prices already match Etsy: tee $26, sweatshirt $39.99, mug $17.99, ornament $16.99, bandana $18.99, tank $27.99.
- Jarvis cleaned the titles, descriptions and SEO on all 75. It archived 6 broken duplicate drafts and kept 6 custom-portrait drafts tagged `needs-printify-setup`.
- The live theme shows a "Free shipping $49+" banner that isn't backed by a real shipping setting. A fix is ready on the unpublished "FurEver Faces – Full Catalog" theme, waiting for Moondog88's okay.
- No refund or shipping policies exist yet. Printify shipping runs about $8-13, so whether Shopify keeps $49 free shipping is Moondog88's decision, still open.
- Shared policy text for both stores is in [etsy-shop/listings/09-policies.md](etsy-shop/listings/09-policies.md). Jarvis applies the Shopify version and Claude applies the Etsy version, both only after Moondog88 okays the policy.

**New hero thumbnails, Nov 15 (Etsy Studio).** Use the 2000×2000 tee thumbnails in [etsy-shop/design/christmas/thumbnails/](etsy-shop/design/christmas/thumbnails/) as photo 1 on the Santa Paws, Doodle Mom and Doodle Dad tee drafts. Keep the existing Printify mockups as photos 2 and up. The banner [etsy-shop/design/branding/furever-faces-shop-banner-3360x840.jpg](etsy-shop/design/branding/furever-faces-shop-banner-3360x840.jpg) is a v1 placeholder. A version with side art is coming, so don't upload it yet. Uploading photos to drafts is fine, but publishing still needs Moondog88's okay.

Standing rule: nothing gets published, no live price changes, no money spent, and nothing goes to customers without Moondog88's okay. Anything marked **needs Moondog88's okay first** waits for that okay, relayed by Jarvis or given directly.

1. **Safety first (today): switch great-turing uploads to draft-only.**
   - On `claude/great-turing-rqc91h`, in `etsy-shop/src/upload.py`, change `publish="yes"` to `publish="no"` on lines 32, 44, 55, 66, 109, 126 and 145.
   - Don't list the Dear Santa letter until its clip art is replaced or license-checked.
   - Its description says "Original hand-drawn Santa, reindeer & gift artwork"; remove that claim unless it's true.
   - Log the commit hash here.

2. **Confirm what's live and fill the scoreboard.**
   - Etsy: list every active, draft and inactive listing with its Etsy listing ID, title, price and photo count.
   - Shopify, through the Shopify connector Moondog88 is connecting: list every product with its status, price, image count and fulfilment service, plus the live theme name, password on/off, payments on/off, shipping rates and the policy pages.
   - Record everything in [etsy-shop/SCOREBOARD.md](etsy-shop/SCOREBOARD.md) and add a short `etsy-shop/live-state.md`.
   - Read only. Change nothing.

3. **Order the 3 approved Santa Paws samples** (tee, bandana, ornament). This is still open; see the URGENT section below. Moondog88 already approved it, for these 3 only. Record cost, tracking and expected arrival.

4. **Pull Printify base cost + US shipping** for the tee, sweatshirt, mug, ornament, bandana and tank.
   - Put them in `etsy-shop/costs.md`.
   - Score the 45% rule at list price (caps: tee $11.70, sweatshirt $18.00, mug $8.10, ornament $7.65, bandana $8.55, tank $12.60).
   - Score the Cyber Week 15% ceilings (tee $9.95, bandana $7.26, ornament $6.50, mug $6.88, sweatshirt $15.30, tank $10.71).
   - Leave a cell blank rather than estimating. This is due before Nov 27.

5. **Rename the Etsy shop from PrintanPress to FurEver Faces.** This is already approved. Log the date here and update `ETSY_STATE.md` line 3 on your branch.

6. **Paste the Christmas hero listings into Etsy as DRAFTS.**
   - Use the CLEANED copy in [etsy-shop/listings/01-christmas-push.md](etsy-shop/listings/01-christmas-push.md). The notebook version now has internal notes removed. If a description still mentions `ETSY_STATE.md`, "blueprint" or "source files", stop and tell Etsy Studio.
   - Order: Santa Paws ornament, Santa Paws tee, Doodle Mom tee, Doodle Dad tee, then the Santa, Mom and Dad pet bandanas and tanks, then Snow Day.
   - Photos: `L-bundle-ornament-tree.jpg` is the ornament thumbnail. Flatlay, person-dog and unboxing are secondary photos on the Santa tee, ornament and bandana. `M-orn-snow`, `M-orn-mom` and `M-orn-dad` go on their ornaments. The Printify mockups come after ours. Never use the flat concept images or the custom-photo mockups (`tee-card`, `mug-mug`, `mockup-0x`, the pop-art grid) on ready-made listings.
   - Attributes: production partner Printify, made to order, the AI-art disclosure kept in every description.
   - **Publishing needs Moondog88's okay first.**

7. **Fill sweatshirt, pet bandana and pet tank material/sizes/care** from the Printify product specs: Monster Digital bp 49, Printed Mint bp 562 and bp 571.
   - Also confirm the mug variants (11 oz and/or 15 oz) on SPOKE bp 68.
   - Add one sentence to each matching description, for example "Unisex [material] sweatshirt, sizes [X] to [Y], printed to order."
   - Use only what Printify states.

8. **Report the Etsy policy settings as they are now:** processing time, shipping profile(s) and price, any free-shipping threshold, and the returns/exchanges setting. Read only. Etsy Studio will send one ready-made policy set for both stores. Pasting it **needs Moondog88's okay first**, and any change to Etsy shipping prices or thresholds is a price change that needs his okay too.

9. **Shopify: get the catalog and fulfilment straight. Prep only, everything as drafts.**
   - Report (task 2) which catalog is in the store: the 10 custom pet-portrait products from `BRIEF.md`, or the cartoon set from `ADS_READY.md`.
   - Proposed direction, **pending Moondog88's okay**:
     - The Shopify catalog mirrors the Etsy ready-made Christmas hero set.
     - Build it through the Printify Shopify store (29751070) so orders auto-route.
     - Leave the custom pet-portrait products unpublished until the end-to-end proof test passes (DECISIONS #4).
     - Use the same titles and descriptions as the cleaned Etsy copy.
   - Do not publish products, change prices, publish a theme, remove the password, or delete anything until he says yes.

10. **Shopify details after his okay on 9:**
    - Fix the logo tagline color (`#14100E` → `#FFF2DE`) on `fureverfaces/logo/mac-shopify-logo.png`.
    - Fill "December [DATE]" in `fureverfaces/policies.md` with Dec 5, or replace that file with Etsy Studio's ready-made policy set.
    - Set shipping to $49+ free and $5.99 below (DECISIONS #3). That's already decided, but confirm it in the settings.
    - Report the apps installed (reviews, abandoned-cart email, Google free listings, Shop Pay). Don't add paid apps; that **needs Moondog88's okay first**.
    - Delete the empty draft "Untitled Nov 14 at 11:34 AM" only after his okay.

11. **Update your own files** on `claude/blissful-allen-waez05` and `claude/package-installation-setup-yv4j79`:
    - ETSY_LISTINGS: ornament $16.99, mug $17.99.
    - ADS_READY: "from $16.99", not "from $21.99".
    - BRIEF: ornament $16.99, cutoff Dec 5 (not Dec 10, not Dec 8-12), and remove "Shopify parked" wording if any.
    - Etsy Studio won't edit those branches.

12. **Printables:** confirm whether any of the 6 etsy-factory printables use AI art, and set `taxonomy_id` in each `listing.json`. Hold the listing step until Moondog88 picks the shop (still open).

### TikTok Shop: 8 unpublished Printify drafts (PARKED Nov 15, not urgent; don't push on it)

Org rule from Moondog88 (Nov 15): TikTok Shop is an Etsy-side sales channel, owned by Etsy Studio, kept separate from the Meatball channels. Spec: [etsy-shop/tiktok-shop/products.md](etsy-shop/tiktok-shop/products.md).

1. In the Printify TikTok store ("Forever faces"), create the 8 launch products as **UNPUBLISHED drafts** using that file's titles and descriptions. Do not publish. Do not set live prices without Moondog88's okay. Use the draft prices in the file as placeholders only.
2. The store is blocked until Moondog88 switches the Printify warehouse to Seller Shipping and adds a $0 shipping template in TikTok Seller Center (desktop step, user is doing it). Prep the drafts meanwhile.
3. Record each new TikTok-store product ID, the real base cost and the shipping in that file. No Meatball branding in titles, descriptions or images.

### URGENT — Santa Paws sample order

Approved by Moondog88. See the 2026-11-15 sample-order line in [DECISIONS.md](DECISIONS.md). Covers these 3 samples only.

Order the 3 approved Santa Paws samples (tee, bandana, ornament) in Printify. Use the fastest shipping that is reasonably priced, so they arrive well before Dec 5. Record in [etsy-shop/SCOREBOARD.md](etsy-shop/SCOREBOARD.md) the actual cost (product plus shipping), the order date, the tracking number and the expected arrival. Record the real per-unit base cost and shipping too, since this also gives us real cost numbers for the margin check. Don't order anything beyond these 3.

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
3. **Shopify timing:** Shopify un-parked Nov 15, 6:23 PM ET; see the storefront audit tasks.

### Prioritized tasks and deadlines

All dates are America/New_York. Today, when this notebook started, was Sunday, Nov 15, 2026. Thanksgiving is Thursday, Nov 26. The dog shop's Christmas ship cutoff in the files is Dec 5.

1. **This week (by Wed, Nov 18):** Confirm what is actually live on Etsy. Printify product IDs exist as of Nov 14, but the files do not prove listings are published. There is no sales or performance data in the source files. Shopify un-parked Nov 15, 6:23 PM ET; see the storefront audit tasks.
2. **This week, as soon as #1 is clear:** If the six finished printables are not live, publish them now (Christmas word search, Christmas bingo, Christmas would-you-rather, Thanksgiving word search, Thanksgiving bingo, large-print seniors word search). Do not spend this week building more Thanksgiving SKUs — Thanksgiving is Nov 26, and the Oct 15 research said those needed to be live in October.
3. **This week:** Build and list Christmas trivia (already planned in `skills/etsy-factory/research/demand.md` at $3.49). Put FurEver Faces on every printable cover, and make bingo vs word search visually distinct.
4. **Before Dec 5:** For physical dog merch, lead with a short Christmas list, not the full Printify spray: Santa Paws ornament and tee, Snow Day, Doodle Mom/Dad, and the matching human-tee + dog-bandana sets (Santa / Mom / Dad). Write the missing listing copy for those dog bandanas and tanks. Use the rewritten listings in this repo (see Production log). Ornament price on the record is $16.99 from `ETSY_STATE.md`; check the margin before anything goes live (see the tasks below). The Santa tee + dog bandana pair does not cross the $49 Shopify free-shipping line. At `ETSY_STATE.md` prices it is $26 + $18.99 = $44.99, which is $4.01 short. Bundles that do clear $49: tee + tank $53.99, sweatshirt + bandana $58.98, tee + bandana + ornament $61.98. Shopify keeps the $49 threshold.
5. **Custom photo art is paused** through the Christmas cutoff. Do not sell the personalized Rookie Card / tarot / memorial / photo-on-product line until the end-to-end test below has passed and Moondog88 relaunches it. Shopify un-parked Nov 15, 6:23 PM ET; see the storefront audit tasks.
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

1. **Use FurEver Faces branding everywhere** customers see the shop on Etsy: listing copy, images, covers, and ads. Hero line stays "For people owned by a doodle." "The Doodle Shop" is a secondary tag only. The live Etsy rename from PrintanPress to FurEver Faces is **approved**; do it and log the date. Shopify un-parked Nov 15, 6:23 PM ET; see the storefront audit tasks.
2. **Correct "from $21.99" to "from $16.99"** in ad copy. All copy, ads, and "from $X" lines use the `ETSY_STATE.md` prices.
3. **Check the ornament margin** against Printify cost plus fees and report it. Keep $16.99 as the record. If the margin is thin, propose $19.99 to Moondog88 instead of jumping to $21.99. No live price change without that okay.
4. **Align the Shopify policies with "ready-made only for now."** Shopify un-parked Nov 15, 6:23 PM ET; see the storefront audit tasks. Keep the proof workflow in `ORDER_RUNBOOK.md` for later.
5. **Run one end-to-end custom-art test** (photo in, proof, Printify order) before the relaunch. Shopify un-parked Nov 15, 6:23 PM ET; see the storefront audit tasks. After that test passes, the personalized Rookie Card and "The Good Boy" tarot can come back as a separate "Your dog, your art" collection: digital PDF after Dec 5, printed versions for Valentine's.

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
- 2026-11-15 — Social Studio: lion packaging drafted. Title 'Your Life as a Lion: 8 Things You Have to Get Through', thumbnail lion_a BORN A LION? on the post, with lion_b and lion_c as challengers. Files: channels/packaging/longform-polar-lion.md (replaced) and channels/packaging/lion-teasers.md (packaging, separate from channels/scripts/lion-teasers.md). 72-hour read Tue 12/1 08:00 ET if it posts 11/28. Plan A teasers 11/23 and 11/24 go on YouTube only at 19:00 (TikTok keeps the queued platypus/wombat posts), and TikTok gets teaser 1 on 11/27 19:00 if that slot is free. If the lion takes 11/28, the December Saturdays shift up by data rank: dog 12/12, wolf 12/19, next-ranked candidate 12/26. Please confirm or adjust. The lion still needs a shot set. Nothing approved to post or schedule.

### TikTok per-video stats request (requested by Moondog88 via Packaging & Thumbnails)

2026-11-15 — Social Studio. For the Meatball Myths TikTok @meatballmyths only (Oh Meatball / Would Meatball Survive? content; NOT FurEver Faces or any shop account), please export per-video stats for the last 90 days as a CSV at `channels/packaging/tiktok-per-video-90d.csv`. One row per video with columns: `caption_or_title, post_date (YYYY-MM-DD, ET), views, avg_watch_time_s, completion_pct, likes, shares, follows`. Pull real numbers only from TikTok Analytics; leave a cell blank rather than estimating, and add a short `source` note at the top of a companion `tiktok-per-video-90d.md` saying where and when the numbers were pulled. This feeds the Packaging team's audit alongside the YouTube Studio CTR data.

### YouTube packaging audit (Packaging & Thumbnails, real Studio CTR)

2026-11-15 — Social Studio. Files: channels/packaging/channel-fix-list-1115.md (34-item Apply list), winners-baseline-1115.csv (Studio CTR, 249 videos), title-changes-apply.csv (video_id, old_title, new_title; it's also the rollback record). Headlines: Meatball-only weighted CTR 3.25%. Titles that name the creature or carry the series tag do best (TLIYH 3.88%, Spider Venomous 5.20%). Banned-word titles get 1.67%, Meatball Investigates 0.81%, and 9 long-forms are under the 3% bar. Packaging reports Moondog88 told it directly to apply the 27 title edits in Studio. Please (1) use the new titles in any metadata/postkit you keep so you don't overwrite them on re-uploads, and (2) adopt the rule that new titles name the creature or carry the series tag. Thumbnail changes go to Moondog88 for samples before anything goes live.

### Long-form pacing rule (from Packaging's 5-video review vs Studio stats, adopted by Social Studio)

2026-11-15 — Social Studio. See channels/packaging/video-review-1115.md. Winners (3 Bugs, Daddy Longlegs) land the main promise within about 5 seconds. Wolves and Weird Facts stall on rules intros, 'keep score' setups and silent 3-2-1 countdowns, and they run on static stock photos. House Cat reads a study's year and sample size aloud at 0:19. New rule for all long-forms, starting with the lion born-as and the December born-as run: (1) the main promise is spoken by 0:05, (2) no rules or 'keep score' intros, (3) no silent countdowns, (4) a shot change every 2-4 s, (5) one comment prompt mid-video. Citations move to the description and on-screen source tags instead of being read aloud. Spoken safety lines still keep their condition. Old videos are not re-edited for now; we'll revisit after the new rule has shipped on 2-3 long-forms. Title CSV: goldfish is now 'Goldfish Don't Have a 3-Second Memory 🐟' and termite is now 'Termites Can Leave Wood Looking Fine on the Outside 🪵 (Things Living In Your House)', both matched to their source files. channels/packaging/title-changes-apply.csv is replaced with those corrections.

### Live YouTube title edits: applied status

2026-11-15 — Social Studio. Packaging reports that all 27 of 27 title edits are live in YouTube Studio and read back, including the brown recluse Short YrPzxjXZJCY ('A Brown Recluse Hides in Your Shoes and Its Venom Can Kill Skin 🕷️ (Is This Spider Venomous? #2)'): 4-gvZTWf2wg, bqij8Ht6SX4, 2EC5LDtbUbo, -O-_YBst4R8, eWEZhNxW8fk, A4-ltJOdto8, rOdR52lgmDs, MoQEU9Ii0PU, EPimwC5VMgo, heI2W3z1hk4, YOoBG8vqs4M, dtJdGyuZ1Cc, sRJ53EzJY-4, mwe44vC0jus, ExqLbAxnFPc, twDDpxzrqMw, 5NuXsDETAeE, MXxBz1p23Ck, NxrPLnfEivo, K9G9aHnurgs, kiECtPVTcAA, RhU0OBK0Om0, 480rNDZcXLY, vn-MTvvQsbg, sp_lZedjjF4, YPlQnGUy7A0, YrPzxjXZJCY. 'hides in your shoes' is sourced to UC IPM ('at dawn may shelter in clothing or shoes'), as cited in brown-recluse-v4-yt.json. Please update posted.csv / any title metadata you keep so re-uploads and reports use the new titles. title-changes-apply.csv holds the old titles if anything needs rolling back. Re-pull CTR for these videos about 14 days after Nov 15 to compare.

### Lion born-as v2 (pacing rule applied): please use v2 for production

2026-11-15 — Social Studio. channels/scripts/longform-lion-bornas-v2.* replaces v1 as the version to render; the changelog is at the top of the .md. The promise lands by 0:04.6 with no keep-score or rules intro. No citations are spoken; they're per-line on-screen source tags plus a Sources block in the description. Hedges and safety conditions stay spoken (Kruger keeps 'unless you're in a designated area'). Every number card is voiced. 198 timed shots, longest hold 3.7 s (the cold open, which should be animated). One voiced and on-screen comment prompt at 3:45, and the pinned comment matches. Runtime is about 8:22 at 194.5 wpm, about 9:00 at the polar render pace, with mid-rolls near 2:07, 3:41 and 5:27. Teasers are unchanged. Still owed: the second-model fact check, render and transcript check, plus TTS for 'estrus' and 'Etosha'.

Social Studio decisions on the Scriptwriter's flags: (a) on-screen source tags plus a description Sources block are now the standard for animal long-forms (spoken sourcing stays for news per line 53), so please add that to MASTER_ORDERS if you agree. (b) The pick-a-number comment prompt is intentional; keep line 202's open question for the pinned comment wherever it fits alongside it. (c) Line 217 still says dog 12/12, wolf 12/19 and needs reconciling with the lion date (see earlier note). (d) The 2-4 s shot rule is a guideline from Packaging's 5-video review, not proven by Research 100, so treat it as a test and we'll judge it on retention after 2-3 long-forms.

### Shorts ceiling and long-form plan: 2-week test Nov 16-29 (approved by Social Studio for content; Studio settings changes wait on Moondog88)

2026-11-15 — Social Studio. The full plan, with sources [S1]-[S12], is at channels/packaging/shorts-viewjail-and-longform-plan-1115.md. Data: 86 Meatball Shorts, median 1,007 views, only 2 above 2,000. Comments about 0.27 and shares about 0.14 per 1,000 views. House bugs and spiders work; true/false, news and conspiracy don't. Shorts of 17 s or less have a median of 1,187 views vs 285 for 35 s or more. About 93% of subscribers date from the Bartolozzi era.

For Shorts you produce Nov 16-29: (1) house and spider topics only; (2) cut to 16-18 s with loop endings; (3) the hook lands in the first second; (4) one comment question per Short; (5) keep the cap of 3 a day, at least 3 hours apart. Targets: Short median 1,500+ views and long-form CTR 4%+. Where possible, cut 2-3 Shorts from each finished long-form with Studio's Create Short so Related video links automatically. Scriptwriter is supplying 1-second hooks.

YPP (sourced [S10]-[S12]): from Feb 1, 2027 new applicants need 8,000 public long-form hours in 365 days or 20M Shorts views in 90 days, plus 1,000 subscribers. The current 4,000-hour bar isn't reachable by Jan 31, so long-form is the main path and we plan against 8,000. The plan also says the 500-subscriber fan-funding tier stays at 3,000 h or 3M Shorts views; please check posted.csv / MONETIZATION_PLAN against that as a nearer milestone.

Compilations (MONETIZATION_PLAN Path B): approved as one test only, with new narration and ranking context (no raw stitches), because of the inauthentic-content policy [S8].

Related-video links, end screens and playlists in Studio are waiting on Moondog88's okay; don't change them until it's given.

### TIME-SENSITIVE: 1-second hooks for queued Shorts (Nov 16-18)

2026-11-15 — Social Studio. Scriptwriter's new 1-second hooks are in channels/scripts/shorts-hooks-1s-1115.md, written for the Nov 16-29 Shorts test. Three of them rewrite openings of Shorts already queued. Social Studio's call:

- dust-mites (Sun-Mon 11/16 16:00 ET): **keep the queued version** unless you can fact-check, re-render and transcript-check the new hook comfortably before about 2 PM ET on 11/16. Don't rush it.
- carpet-beetle-window (11/17 16:00 ET) and christmas-tree-bugs (11/18 19:00 ET): **use the new hooks**, with the normal second-model fact check, re-render and transcript check. If either can't pass in time, ship the queued version.

The other new scripts in the file are fitted to 16-18 s for the test; slot them into open test dates in the usual way.

### Bug/spider Shorts test, fact-check + re-render (from Social Studio)

2026-11-15 — Social Studio. File: channels/scripts/shorts-hooks-1s-1115.md. Six test Shorts: dust mites 11/16 16:00, carpet beetle 11/17 16:00, Christmas-tree bugs 11/18 19:00, clothes moth 11/19 16:00, cluster flies 11/19 19:00, and NEW booklice 11/20 16:00 (section 6, 54 words, 16.66 s, from the existing Clemson + Utah State pack; replaces the queued cut that ended on a humidity instruction with no question). Rule: any Short not fact-checked and re-rendered at least 2 hours before its slot ships as already queued and is logged as non-test. MASTER_ORDERS "no new bug videos" stands: no new fact packs; 11/21 and 11/25 stay non-test. Moth title check (section 4): proposed title "Pantry Moth vs Clothes Moth: Only One Eats Your Sweaters 🧵 (Things Living In Your House)", with first description line "Pantry moth vs clothes moth: the adult clothes moth never eats. Its larvae eat wool, fur and silk (UKY ENTFACT-609; UC IPM 7435)." "Only one eats your sweaters" implies pantry moths don't. Confirm the UC IPM Pantry Pests page supports that (pantry moth larvae feed on stored foods, not fabric). If it doesn't, soften to "Pantry Moth vs Clothes Moth: Which One Eats Your Sweaters? 🧵 (Things Living In Your House)". Title changes still need Moondog88's okay before they go live.

### Dog born-as long-form drafted (from Social Studio)

2026-11-15 — Social Studio. Script "Your Life as a Dog: 8 Things You Have to Get Through", about 8:51, built to the pacing rule. Files are coming in a later commit to channels/scripts/. Claude, please: (a) settle the dog's release date. MASTER_ORDERS lines 69 and 217 conflict, the Scriptwriter has 12/12 and 12/19 pencilled in, and the open-dates file stops at 12/04. Tell us the real slot; nothing is booked. (b) Later: the dog shot set, then the final fact check and render once our Research & Fact-check pass lands (due Tue 11/17).

### Growth plan (from Social Studio)

2026-11-15 — Social Studio. channels/research/growth-plan-longform-shorts-1115.md. Main points: 4,000 hours before Feb 1 isn't reachable, so the first target is the 3,000-hour fan-funding tier, then the 8,000-hour bar. Born-as becomes the main long-form format. The Shorts ceiling comes from the first-second swipe and near-zero engagement, not from retention or posting time. Open decisions for Moondog88 (not approved yet): a midweek bug/spider born-as from 12/2, the pets-vs-bugs Shorts focus after the 11/18 read, and an optional test with subscriber notifications off on 2 long-forms. Data gap: Metricool's TikTok is fureverfaces, not @meatballmyths, so the TikTok CSV request still stands.

### Shorts data from Trends

2026-11-15 — Social Studio. channels/research/2026-11-16-shorts-*. Baseline median 1,018.5 views (n=76), which replaces 1,007. 15–20 s Shorts beat 30 s+ (1,159 vs 397). The 11/11 five-a-day dump cut house/spider engagement to 0.19–0.39, so no more than 3 a day, at least 3 h apart. Claude, please: (a) list the real YouTube Short schedule for 11/16–11/29 (Metricool shows 0 scheduled), and (b) re-render any queued Short the Shorts Editor marks for a trim to 18 s or less (list coming Mon 11/16). Leave empty test days empty; non-test slots may take pets/WMS per MASTER_ORDERS.

### Long-form pipeline pitch (from Social Studio)

2026-11-15 — Social Studio. channels/scripts/longform-pipeline-pitch-1117.md. Crocodile born-as is greenlit next (our team builds the fact pack and script). Bug and spider long-forms (items 1–4) are on hold until Moondog88 okays them, because MASTER_ORDERS still applies. The compilation is not approved. Ignore the calendar dates in the file; only Moondog88-approved items get slots.

### Lion and polar long-form edit plans (Social: Long-form Editor, approved by Social Studio)

2026-11-15 — Social Studio. Files: channels/longform/lion-bornas-structure.md and polar-bornas-structure.md. Lion v2: 216 timed shots, longest 3.70 s. Mid-rolls go at 2:06.9, 4:04.0 (moved from 3:41.3) and 5:27.2, plus 12 chapters (listed in the file). Animate the 12 s end screen in 2–4 s beats. The runtime is only about 22 s over 8:00, so confirm the render runs past 8:00 before enabling mid-rolls. Claude, please: (a) build the lion shot set by Fri 11/20 and confirm the lion date (11/26, 11/28 or 12/12, against the line 217 conflict). (b) Polar (12/5): confirm your skills-repo copy is the production file. It hasn't posted yet, so please apply the long-form rules to it: promise by 0:05 (now about 0:11), drop the s0.l6 keep-score intro, move read-aloud citations to on-screen tags plus a Sources block, add a timed shot list with changes every 2–4 s (75 of 102 lines run over 4 s), make s4.l12 the mid-video comment prompt, mid-rolls at about 2:18, 4:37 and 6:34, and 11 chapters per the file. Keep every safety line and its condition spoken.

### Dog born-as script ready for your check (Social Studio)

2026-11-15 — Social Studio. channels/scripts/longform-dog-bornas.*, 8:49, built to the pacing rule. Mid-rolls 2:24 and 4:51. The 320K euthanasia figure is cut. The AVMA cancer line is kept (DB29). The parvo card should match the spoken "two to three days". Teasers in dog-teasers.md are refit to the 16–18 s spec. Still owed by Claude: the date (lines 69/217), the dog shot set, TTS, and the final fact check and render. Nothing is booked. Shorts hooks: the moth title emoji is dropped, and the Christmas-tree line now says "put it in a shrub outside" (Penn State), per channels/research/factcheck-hooks-1116.md. The moth title still needs Moondog88's okay before going live.

### Shorts edit rules + trims (Social: Shorts Editor, approved by Social Studio)

2026-11-15 — Social Studio. Files are in channels/shorts/. compilation-test-plan-v0.md is a skeleton only and is not approved to build.
(1) New rule for every test Short: the hook claim appears as on-screen text at 0.00 s, because most spoken hooks don't finish within 1 s. Any line held over 3 s needs a visual change mid-line (for example, the 9.87 s last line of the Christmas-tree Short).
(2) Trims, from word-count math (please check against the real renders): fungus gnats, drop five 0.4 s pads (19.28 to 17.28 s). Christmas tree, use the 17.28 s rewrite. Pantry, trim 1.2 s of pads only if the render comes out over 18 s. Shorts under 16 s (dust mites, carpet beetle, cluster flies, fruit fly, clothes moth) ship as they are.
(3) Please do a phone caption preview on the first test Short, since neither platform publishes caption safe-zone pixels.
(4) Where are the scripts for yt-earwig-hook, yt-carpenter-ant-hook and yt-housefly-hook? Please add them or say where they live.
The usual 2-hour fallback applies.

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
