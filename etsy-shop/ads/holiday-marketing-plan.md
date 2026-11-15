# DRAFT — FurEver Faces holiday marketing plan (through Dec 5, 2026)

**Status: DRAFT.** Nothing in this document goes live. No ad spend, no posts, no coupons, and no price or listing changes without Moondog88's explicit okay.

Written 2026-11-15 (America/New_York) from a read-only review of GitHub sources. No numbers or performance stats were invented. Where a fact is missing, the text uses a **[CONFIRM]** placeholder. Conflicting figures from different source files are shown side by side, not averaged.

---

## How to read this draft

- **Shop context in the files:** doodle-owner print-on-demand merch (Etsy shop recorded as PrintanPress, shop id 38484468, Printify store 29754022) plus printable PDF kits. Brand name used in the merch docs is FurEver Faces. A Shopify store (Printify store 29751070) also appears in the launch checklist. **[CONFIRM]** which storefront is the public holiday storefront, and whether the public shop name is FurEver Faces or PrintanPress.
- **Price lists used below:**
  - `ETSY_STATE.md` (2026-11-14, later update the same day): tee $26, sweatshirt $39.99, mug $17.99, ornament $16.99, pet bandana $18.99, pet tank top $27.99. This is the only file that lists Printify product ids, including sweatshirts, ornaments for Santa/Snow/Mom/Dad, and matching dog bandanas/tanks.
  - `ETSY_LISTINGS.md`: tee $26.00, mug $18.00, ornament $21.99, wall art $59.99. No sweatshirt, bandana, or tank prices. Wall art does not appear in `ETSY_STATE.md`.
  - Printable prices from `etsy-factory/research/demand.md` and each product's `listing.json` (they match): Christmas word search $3.99, Christmas would-you-rather $2.99, large-print seniors word search $4.99, Christmas bingo $3.49, Thanksgiving bingo $3.49, Thanksgiving word search $3.49.
- **Until Moondog88 confirms which merch prices are live on Etsy, treat `ETSY_STATE.md` as the later Printify record and `ETSY_LISTINGS.md` as listing-copy proposals.** Bundle math is shown from both where they disagree.

---

## 1. Holiday promo plan through Dec 5, 2026

Christmas shipping cutoff in the merch files: **"Order by Dec 5 for Christmas delivery"** (`ETSY_LISTINGS.md`, `ADS_READY.md`). `ADS_READY.md` also sets **Dec 5** as the end date for Meta ads ("the last order date for Christmas").

### Hero list (physical merch)

Promote a short hero set, not the full catalog:

| Hero | What the files actually have | Listing copy (titles / slogans) | Listing-copy prices (`ETSY_LISTINGS.md`) | Printify-state prices (`ETSY_STATE.md`) |
|---|---|---|---|---|
| Santa Paws ornament | `orn-santa` in state; full ornament listing copy | Title: "Goldendoodle Ornament, Santa Paws Doodle Christmas Ornament…". Art: Santa hat, wrapped gifts, words "Santa Paws" / "Nice list (pending)" | $21.99 | $16.99 |
| Santa Paws tee | `tee santa` in state; full tee listing copy | Title: "Goldendoodle T-Shirt, Santa Paws Doodle Shirt…". Same art and slogan. Bella + Canvas, S–2XL | $26.00 | $26 |
| Snow Day | `tee snow`, `mug-snow`, `sw-snow`, `orn-snow` in state; listing copy for **tee and mug only** (no ornament or sweatshirt copy) | Title pattern: "Goldendoodle T-Shirt, Snow Day Doodle Shirt…". Art: beanie and scarf, words "Snow Day" / "Zoomies incoming" | Tee $26.00, mug $18.00 | Tee $26, mug $17.99, sweatshirt $39.99, ornament $16.99 |
| Doodle Mom / Doodle Dad | `tee mom` / `tee dad`, mugs, sweatshirts; ornaments `orn-mom`, `orn-dad` in state; listing copy for **tee and mug only** | Mom: pink bandana, "Doodle Mom" / "Curls, cuddles & chaos". Dad: baseball cap, "Doodle Dad" / "Chief treat officer" | Tee $26.00, mug $18.00 each | Tee $26, mug $17.99, sweatshirt $39.99, ornament $16.99 |
| Matching tee + dog bandana | State has `band-mom`, `band-dad`, `band-santa`, `band-fam` (and other designs). **No bandana listing titles or prices in `ETSY_LISTINGS.md`.** Dog items: Pet Bandana, Printed Mint, $18.99. "Each dog listing links to its human tee and back." | **[CONFIRM]** live listing titles for the bandanas | Bandana price not in that file | Bandana $18.99; matching tee $26 |

Related items that exist in state but are not in the short hero list: Santa/Snow/Mom/Dad sweatshirts at $39.99; Santa/Mom/Dad mugs; pet tank tops at $27.99 (`tank-mom`, `tank-dad`, `tank-santa`, `tank-fam`, and others). **[CONFIRM]** whether those should be supporting SKUs or held back.

### Bundle math vs a $49 free-shipping line

**[CONFIRM] the $49 free-shipping threshold itself.** No shop shipping policy, free-shipping threshold, or $49 figure appears in any file reviewed. `ETSY_LISTINGS.md` only warns: "check Printify's cost plus shipping before publishing, because $26.00 leaves a thin margin if shipping is free." Do not turn free shipping on until margin is checked.

If a $49 free-shipping threshold is approved, this is the additive math from documented prices. No bundle discount is assumed, because none is in the files.

**Using `ETSY_STATE.md` (later Printify prices):**

| Combination | Math | vs $49 |
|---|---|---|
| Hero idea: matching tee + dog bandana | $26 + $18.99 = **$44.99** | **$4.01 short** — does not cross $49 |
| Tee + pet tank top (matching set also in state) | $26 + $27.99 = **$53.99** | Crosses by $4.99 |
| Sweatshirt + bandana | $39.99 + $18.99 = **$58.98** | Crosses by $9.98 |
| Tee + ornament | $26 + $16.99 = **$42.99** | $6.01 short |
| Tee + mug | $26 + $17.99 = **$43.99** | $5.01 short |
| Tee + bandana + ornament | $26 + $18.99 + $16.99 = **$61.98** | Crosses by $12.98 |
| Wall art | No wall-art price in this file | — |

**Using `ETSY_LISTINGS.md` (listing-copy prices; no bandana price):**

| Combination | Math | vs $49 |
|---|---|---|
| Tee + ornament | $26.00 + $21.99 = **$47.99** | **$1.01 short** |
| Tee + mug | $26.00 + $18.00 = **$44.00** | $5.00 short |
| Wall art alone | **$59.99** | Crosses by $10.99 |
| Tee + bandana | Bandana price **[CONFIRM]** — not in this file | — |

**Recommendation (still DRAFT, needs okay):** do not advertise "tee + bandana hits free shipping" unless prices or the threshold change. If the $49 line is approved on `ETSY_STATE.md` prices, the combinations that actually clear it are **tee + tank ($53.99)**, **sweatshirt + bandana ($58.98)**, or **tee + bandana + ornament ($61.98)**. **[CONFIRM]** whether to (a) change the threshold, (b) add a documented bundle SKU/discount, or (c) promote the combinations that already clear $49.

### Dated calendar (Nov 15–Dec 5, then digital-only)

All dates are America/New_York. Thanksgiving 2026-11-26 is from `etsy-factory/research/demand.md`. Black Friday / Small Business Saturday / Cyber Monday dates are the calendar days after that Thursday.

| Date | Moment | Draft actions (do not run until approved) |
|---|---|---|
| Sun Nov 15–Wed Nov 25 | Prep window (today is Nov 15; 12 days to Black Friday) | **[CONFIRM]** live Etsy prices, which hero listings are published, and whether printables are already listed. Fix ad/listing copy discrepancies in section 4. Draft (do not publish) sale coupons and shipping-cutoff banners. Build Pinterest boards and pin copy (section 2). Join / read rules for Facebook groups (section 3). Decide Etsy Ads test vs holiday budget (section 5). If Thanksgiving printables are live, they can still be pushed as last-minute digital for Nov 26. |
| Thu Nov 26 | Thanksgiving | Physical merch: light "order by Dec 5" reminders only, no invented sale %. Printables: Thanksgiving bingo ($3.49) and Thanksgiving large-print word search ($3.49) as instant downloads for same-day play. Christmas printables can start riding along as "print tonight for the long weekend." |
| Fri Nov 27 | Black Friday | If a sale is approved, this is the first paid-promo and on-site sale day for hero merch + Christmas printables. Keep the cutoff visible: order physical items by Dec 5. |
| Sat Nov 28 | Small Business Saturday | Value-first, shop-local/independent tone in Facebook groups (only where rules allow; see section 3). Same hero SKUs. No separate discount is in the files; **[CONFIRM]** whether SBS gets its own code or continues the BF offer. |
| Sun Nov 29 | In-between day | Organic pins and group-safe posts only, unless a multi-day code is still running. |
| Mon Nov 30 | Cyber Monday | Second sale pulse, if approved. Good day to start or raise Etsy Ads on hero listings (section 5). Restate Dec 5 cutoff. |
| Tue Dec 1–Thu Dec 4 | Last physical-order week | Urgency copy already in the listings: "Order by Dec 5 for Christmas delivery." Pause any campaign that cannot arrive in time. Begin shifting creative toward instant PDF printables for people who will miss the cutoff. |
| Fri Dec 5 | Christmas shipping cutoff | Last day to take physical orders for Christmas, per `ADS_READY.md` and `ETSY_LISTINGS.md`. End or pause physical-merch ads the same day (`ADS_READY.md` end date). |
| After Dec 5 | Digital printables only | Instant PDF angle: Christmas word search, bingo, would-you-rather, and the evergreen seniors large-print book. These ship nothing; the listing copy already says "This is a digital product. No physical item will be shipped." Position as last-minute Christmas Eve / party / classroom / caregiver activities. Thanksgiving kits can stay up but should not be the lead after the holiday. |

### Etsy sale / coupon ideas (suggestions only — no rates exist in the files)

No sale calendar, coupon codes, or "% off" figures appear in the reviewed files. Any rate below is a **[CONFIRM]** suggestion, not a documented policy. Do not publish until approved, and recalculate margin against Printify cost + Etsy fees + shipping.

Fee context that *is* in `demand.md` (for digital listings; cited from third-party fee explainers, not from this shop's dashboard): listing fee $0.20 per listing (renews every 4 months or on sale); 6.5% transaction fee; US payment processing 3% + $0.25. **[CONFIRM]** current Etsy fee schedule and whether offsite-ads fees also apply before setting a discount.

Suggested coupon types to consider (structure only):

1. **Sitewide or hero-collection sale code** for Nov 27–30, **[% off — CONFIRM]**. If used, write the sale price from the confirmed live list price; do not reuse the stale "$21.99 from" line in `ADS_READY.md`.
2. **Abandoned-cart offer** (Etsy can message shoppers who leave items in cart): a time-limited **[% off or free shipping — CONFIRM]** on the same cart, with the Dec 5 cutoff in the message for physical items.
3. **Favorited-item offer:** same caution; only if Etsy sales tools are on. **[CONFIRM]** whether the shop has Etsy Sales / Promoted Offers enabled.
4. **Free-shipping threshold:** only after **[CONFIRM]** of the threshold and margin. As shown above, tee + bandana at `ETSY_STATE.md` prices is $44.99 and does not clear $49. A threshold of **[CONFIRM]** that matches real basket sizes would be more honest than forcing a $49 line onto a $44.99 pair.
5. **Digital-only code after Dec 5**, if a merch sale code would confuse shoppers about shipping. Printable list prices are $2.99–$4.99; a steep % off on a $2.99 item may not be worth the fee drag — **[CONFIRM]** whether printables go on sale at all.

### Last-minute digital printables after Dec 5

Ready product files and listing copy already exist in `skills/etsy-factory/products/` on branch `claude/youtube-monetization-strategy-m9vz6i`. **[CONFIRM]** which of these are actually published on Etsy today.

| Product | Price | Why it works after the shipping cutoff |
|---|---|---|
| Christmas Word Search, Large Print, 24 puzzles | $3.99 | Instant PDF, US Letter + A4, advent-style "one a day," senior-friendly large print |
| Christmas Would You Rather, 60 questions | $2.99 | Instant party/icebreaker; family-friendly; lowest printable price in the files |
| Christmas Bingo, 30 unique cards | $3.49 | Parties, classrooms, office, senior centers; print-at-home |
| Large Print Word Search for Seniors, 40 puzzles | $4.99 | Evergreen; caregivers, activity directors, "gift for grandma" tags; not Christmas-dependent |
| Thanksgiving bingo / word search | $3.49 each | Only relevant through Nov 26; do not lead with these after Thanksgiving |

Listing policies already written into each `listing.json` / `listing.md`: personal, family, and classroom use; do not resell or share files; instant download, returns not accepted; all puzzles/questions/artwork original. Demand research (`demand.md`, written 2026-10-15) said Christmas listings should have been live by early November to be indexed before the December search peak — **[CONFIRM]** go-live dates, because today is already Nov 15.

---

## 2. Pinterest plan

No Pinterest board names, pins, or posting cadence exist in the reviewed files. Everything in this section is a **draft proposal**. **[CONFIRM]** whether a business Pinterest account exists, and do not publish pins until approved.

### Suggested board names

Merch:

- Goldendoodle Gifts
- Doodle Mom and Doodle Dad
- Santa Paws Christmas Dog
- Snow Day Doodle Style
- Matching Dog and Owner Outfits

Printables:

- Christmas Word Search Large Print
- Christmas Party Games Printable
- Christmas Bingo for Kids and Adults
- Large Print Puzzles for Seniors
- Thanksgiving Printables (use through Nov 26, then stop pinning as a lead)

### Pin titles and descriptions

Titles and descriptions reuse keywords already in `ETSY_LISTINGS.md` tags and in each printable's `listing.json` tags. Swap in the live Etsy URL before posting. **[CONFIRM]** live URLs. Do not state a price in a pin until the live price is confirmed, because merch prices disagree across files.

#### Santa Paws ornament (3–5 pins)

1. **Title:** Goldendoodle Santa Paws Christmas Ornament  
   **Description:** Cute cartoon goldendoodle Christmas ornament for doodle moms and dads. Santa Paws, "Nice list (pending)." A pet Christmas tree decor gift for goldendoodle, labradoodle, and bernedoodle lovers. Printed to order. Order by Dec 5 for Christmas delivery. **[CONFIRM price and URL]**

2. **Title:** Santa Paws Doodle Ornament — Dog Lover Tree Decor  
   **Description:** Holiday pet Christmas ornament with a doodle in a Santa hat and wrapped gifts. Search-friendly keywords from the listing: doodle ornament, dog ornament, santa paws, christmas dog, goldendoodle gift, labradoodle gift, bernedoodle gift.

3. **Title:** Christmas Dog Ornament for Doodle Mom and Dad  
   **Description:** A small doodle-owner Christmas gift for the tree. Same Santa Paws design as the matching tee. **[CONFIRM]** whether a merch + printable pin is wanted; keep physical vs digital clear.

4. **Title:** Nice List (Pending) — Goldendoodle Santa Paws  
   **Description:** Quote the listing slogan only: a doodle in a Santa hat with wrapped gifts, words "Santa Paws" and "Nice list (pending)." Order by Dec 5 for Christmas delivery.

#### Santa Paws tee (3–5 pins)

1. **Title:** Goldendoodle Santa Paws T-Shirt — Doodle Mom Dad Gift  
   **Description:** Unisex doodle shirt, Bella + Canvas S–2XL, printed to order in the USA. Tags from the listing: doodle shirt, dog mom shirt, santa paws, christmas dog, dog christmas gift, goldendoodle gift, labradoodle gift, bernedoodle gift. **[CONFIRM price]**

2. **Title:** Santa Paws Doodle Shirt for Christmas  
   **Description:** Cute cartoon dog lover tee for goldendoodle, labradoodle, and bernedoodle people. "Nice list (pending)." Order by Dec 5 for Christmas delivery.

3. **Title:** Funny Christmas Dog Shirt — Goldendoodle Gift  
   **Description:** A holiday doodle mom / doodle dad gift. Same Santa Paws art as the ornament, so they can be given together. **[CONFIRM]** bundle language; do not claim free shipping on this pair unless the math and policy are confirmed.

4. **Title:** Christmas Doodle Tee — Labradoodle and Bernedoodle Too  
   **Description:** Breed-first title style from the listing docs: lead with goldendoodle, then the slogan, then who it is for.

#### Snow Day (3–5 pins)

1. **Title:** Snow Day Goldendoodle T-Shirt — Zoomies Incoming  
   **Description:** Cute cartoon doodle in a beanie and scarf. Winter dog / snow dog / christmas dog gift for doodle moms and dads. **[CONFIRM price]**

2. **Title:** Snow Day Doodle Mug for Cozy Winter Coffee  
   **Description:** Goldendoodle coffee mug, "Snow Day" / "Zoomies incoming." Dog mom mug, winter dog, snow dog. **[CONFIRM]** 11 oz / 15 oz availability as written in the listing copy.

3. **Title:** Winter Doodle Shirt for Goldendoodle, Labradoodle, Bernedoodle  
   **Description:** Unisex cotton tee, printed to order. Keywords: winter dog, snow dog, doodle shirt, dog lover tee, goldendoodle gift.

4. **Title:** Snow Day Doodle Christmas Gift  
   **Description:** Note: Snow Day tee/mug listing copy in `ETSY_LISTINGS.md` does **not** include the "Order by Dec 5" sentence that Santa Paws listings have. **[CONFIRM]** adding the cutoff before pinning a shipping date.

5. **Title:** Snow Day Doodle Ornament **[CONFIRM — listing copy missing]**  
   **Description:** `ETSY_STATE.md` has `orn-snow`. There is no ornament listing title in `ETSY_LISTINGS.md`. Do not pin an ornament price or title until copy and the live listing are confirmed.

#### Doodle Mom / Doodle Dad (3–5 pins)

1. **Title:** Doodle Mom T-Shirt — Curls, Cuddles & Chaos  
   **Description:** Goldendoodle doodle mom shirt, cute cartoon dog in a pink bandana. Keywords: doodle mom shirt, dog mom shirt, dog mom gift, goldendoodle gift, labradoodle gift, bernedoodle gift. **[CONFIRM price]**

2. **Title:** Doodle Dad T-Shirt — Chief Treat Officer  
   **Description:** Goldendoodle doodle dad shirt, cute cartoon dog in a baseball cap. Keywords: doodle dad shirt, dog dad gift, goldendoodle gift, dog lover tee.

3. **Title:** Doodle Mom and Doodle Dad Gift Set  
   **Description:** Matching mom/dad tees and mugs. Listing copy says to list these first: "they are what doodle owners search for." Do not invent a set price; none is in the files. **[CONFIRM]** whether a combined listing or two-item cart is the offer.

4. **Title:** Doodle Mom Mug — Goldendoodle Coffee Cup  
   **Description:** Ceramic mug, dishwasher and microwave safe (per listing copy). Dog mom mug, doodle mom gift.

5. **Title:** Doodle Mom Era / Best Doodle Dad (supporting pins)  
   **Description:** Extra designs in the third batch: "Doodle Mom Era" / "This one is permanent"; "Best Doodle Dad" / "According to the dog"; "Doodle Parents" / "Yes, these are our kids." Use as supporting pins, not the first hero.

#### Matching tee + dog bandana (3–5 pins)

1. **Title:** Matching Doodle Mom Shirt and Dog Bandana  
   **Description:** Human tee + pet bandana in the same Doodle Mom design. State file: each dog listing links to its human tee and back. **[CONFIRM]** live URLs and prices. Do not claim this pair reaches free shipping; at $26 + $18.99 it is $44.99.

2. **Title:** Matching Doodle Dad and Dog Bandana Set  
   **Description:** Doodle Dad tee and matching pet bandana (`band-dad`). Printed to order. **[CONFIRM]** bandana listing title (none in `ETSY_LISTINGS.md`).

3. **Title:** Santa Paws Matching Dog and Owner Christmas Outfit  
   **Description:** Santa Paws tee (`tee santa`) and `band-santa`. Holiday matching-outfit pin. **[CONFIRM]** that both listings are published.

4. **Title:** Goldendoodle Matching Dog Bandana and Owner Tee  
   **Description:** Keywords: goldendoodle gift, doodle mom gift, dog bandana, matching dog and owner. If promoting a free-shipping story, use a combination that actually clears the confirmed threshold (see section 1).

#### Christmas word search, large print (3–5 pins)

1. **Title:** Christmas Word Search Large Print — 24 Holiday Puzzles  
   **Description:** 24 printable Christmas word searches in big, bold, easy-to-read letters. Instant PDF, US Letter and A4. Large print 15x15 grids, no backwards words, answer key included. Senior activities, holiday party game, advent activity, gift for grandma. Price in files: $3.99. **[CONFIRM]** live URL.

2. **Title:** Large Print Christmas Word Search for Seniors and Adults  
   **Description:** Tags from the listing: xmas word search, christmas puzzles, large print puzzles, printable word find, senior activities, brain games seniors, classroom christmas, advent activity.

3. **Title:** 24 Christmas Word Searches — Printable Advent Activity  
   **Description:** Do one a day, or print for a holiday gathering. Instant digital download; no physical item ships. After Dec 5 this is a last-minute gift they can print tonight.

4. **Title:** Easy Christmas Word Find PDF — No Backwards Words  
   **Description:** Easy mode: words run forward, down, and diagonally only. Comfortable for seniors and anyone who prefers bigger text.

#### Christmas bingo (3–5 pins)

1. **Title:** Christmas Bingo Printable — 30 Unique Cards  
   **Description:** Holiday party game for kids, adults, classrooms, office parties, and senior centers. 30 unique cards, 40 calling cards, caller's checklist, how-to-play page. Instant PDF, US Letter and A4. Price in files: $3.49.

2. **Title:** Christmas Bingo Game for Family and Classroom  
   **Description:** Tags: christmas bingo, xmas bingo, holiday bingo, christmas game, holiday party game, classroom christmas, family game night, kids christmas game, office party game.

3. **Title:** Printable Holiday Bingo — Big Easy-to-Read Words  
   **Description:** Words are big so young kids, teens, and grandparents can play together. Print at home, as many copies as needed for personal, family, or classroom use (no resale).

4. **Title:** Instant PDF Christmas Party Game — Bingo  
   **Description:** Last-minute after Dec 5: download, print, and play the same day. No shipping.

#### Christmas would-you-rather (3–5 pins)

1. **Title:** Christmas Would You Rather — 60 Printable Questions  
   **Description:** 60 original, family-friendly Christmas would-you-rather questions as cut-out cards and numbered sheets. Instant PDF. Price in files: $2.99.

2. **Title:** Christmas Icebreaker Game for Kids and Adults  
   **Description:** Tags: would you rather, christmas game, holiday party game, family game night, christmas icebreaker, kids christmas game, classroom christmas, office party game, christmas eve game.

3. **Title:** Printable Christmas Eve Conversation Cards  
   **Description:** No prep: print and play in minutes. Dinner table, classroom brain break, or office party. Instant download.

4. **Title:** Family-Friendly Christmas Party Game PDF  
   **Description:** Listing examples in the copy: "Would you rather live in a gingerbread house or an igloo?" Keep pins family-safe. After Dec 5, pitch as a same-night game.

#### Large-print word search for seniors (3–5 pins)

1. **Title:** Large Print Word Search for Seniors — 40 Easy Puzzles  
   **Description:** 40 original easy word searches in extra-large 15x15 grids, no backwards words, answer key included. Instant PDF. Price in files: $4.99. Tags: senior activities, brain games seniors, elderly activities, gift for grandma, dementia activities, memory care, activity pages.

2. **Title:** Easy Large Print Puzzles for Adults and Caregivers  
   **Description:** Familiar themes in the listing: garden flowers, backyard birds, baking day, old-fashioned candy, the seasons. A screen-free brain break for seniors, activity directors, and caregivers.

3. **Title:** Printable Brain Games for Seniors — Instant PDF  
   **Description:** Evergreen, not tied to the Dec 5 merch cutoff. Good pin to keep running after Christmas shipping ends.

4. **Title:** Gift for Grandma — Large Print Word Search Book  
   **Description:** Digital gift they can print at home or at a shop. For personal, family, and classroom use; not for resale (per listing policy).

### Suggested posting cadence (not in the files — [CONFIRM])

No historical pin schedule exists, so this is a suggestion only:

- **Nov 15–25:** 1–2 pins per day, mix of merch hero + Christmas printables. Front-load Santa Paws and large-print word search. If Thanksgiving printables are live, include those through Nov 26 only.
- **Nov 27–30 (BF–CM):** 2 pins per day on hero merch and Christmas games, using approved sale language only.
- **Dec 1–5:** 1–2 pins per day; every merch pin includes the Dec 5 cutoff.
- **After Dec 5:** merch pins paused or stripped of "arrives by Christmas" claims; 1 pin per day on instant printables (word search, bingo, would-you-rather, seniors book).

Reuse each pin title on a different board no more than the platform's current healthy-repin practice; **[CONFIRM]** the account's preferred frequency. Use listing mockup images from Printify (merch) and `products/*/images/01-cover.jpg` through `05-how.jpg` (printables) once those assets are confirmed cleared for Pinterest.

---

## 3. Facebook doodle-group approach

`ADS_READY.md` already says: "Share in doodle owner Facebook groups where the rules allow it." No group names, post copies, or promo-day calendar exist in the files. This section is a tactics draft. **Do not post until Moondog88 approves, and never post in a group whose rules you have not read that day.**

### Kinds of groups to look for (not a list of specific groups)

- Breed groups: goldendoodle, labradoodle, bernedoodle (the audience named in `ADS_READY.md` and in every merch title/tag).
- Local doodle meetup / doodle-walk groups.
- Doodle-owner buy/sell/trade or "sale Sunday" threads, if a group has a dedicated promo day.
- Holiday gift-idea threads in those same groups, when admins open them.
- For printables: senior-activity, caregiver, memory-care activity, classroom-teacher, and family-game-night groups — these match tags already in the printable listings ("senior activities", "dementia activities", "classroom christmas", "family game night"). Keep merch and printables in the right rooms; do not drop a tee link in a caregiver-activity group unless the post is about the large-print puzzles.

**[CONFIRM]** any groups Moondog88 already belongs to before joining new ones.

### Rules-respecting tactics

1. **Read the rules every time** before posting. Many breed groups ban shop links, or allow them only on a promo day or in a pinned thread.
2. **Promo-day threads only** when that is the rule (buy/sell Saturday, "small business Sunday," holiday gift megathread). If there is no promo window, do not drop a link.
3. **Ask an admin first** when the rules are unclear, or when you want to post a shop link outside a designated thread. Save the approval.
4. **Value-first:** lead with a useful or funny doodle moment (the slogan, a genuine tip, a printable activity idea), not a hard sell. No fake urgency and no invented discounts.
5. **Disclose** that it is your shop. The merch listings already require stating that artwork was made with AI tools (`ETSY_LISTINGS.md` step 3) — carry that honesty into group posts if you show the art.
6. **One post, not spam:** do not cross-post the same link to every group in one sitting; stagger and tailor. Never argue in comments if a post is removed.
7. **After Dec 5:** if a physical order cannot arrive for Christmas, say so and point to instant printables instead.

### Sample post copies (draft only)

Prices below use `ETSY_STATE.md` when a merch price is stated, and printable `listing.json` prices, and are still **[CONFIRM]** against the live listing. Do not post a free-shipping claim for tee + bandana.

**Post A — breed group, value-first, promo day only**

> Happy [promo-day name, if the group has one] from a fellow doodle person. We made a small set of cartoon doodle gifts for goldendoodle, labradoodle, and bernedoodle people — including Santa Paws ("Nice list (pending)") on a tee and a Christmas ornament. Printed to order in the USA. The listings say to order by Dec 5 for Christmas delivery. Happy to share the shop link if that's allowed here; otherwise I can DM it. Artwork was made with AI tools.

**Post B — buy/sell or gift-thread, matching set, honest math**

> If anyone is looking for a matching doodle-mom (or doodle-dad) tee and a dog bandana in the same design: the human tee is $26 and the pet bandana is $18.99 in our current price list **[CONFIRM live prices]**. That's $44.99 together. I won't claim that hits a free-shipping minimum until we've confirmed our shipping policy. Order by Dec 5 if you need it for Christmas.

**Post C — Small Business Saturday, admin-approved if required**

> Small Business Saturday hello. We're a small doodle-owner shop (FurEver Faces / **[CONFIRM public shop name]**). Hero designs right now are Santa Paws, Snow Day ("Zoomies incoming"), and Doodle Mom / Doodle Dad. I can share links if the group allows them today. Physical orders: Dec 5 is the Christmas cutoff we have written on the listings.

**Post D — caregiver / senior-activity group, printables only**

> If you're planning a Christmas activity for seniors or a family gathering, we have a large-print Christmas word search (24 puzzles, $3.99) and an evergreen large-print word search for seniors (40 easy puzzles, $4.99). Instant PDF, big letters, no backwards words, answer key included. Personal, family, or classroom use — not for resale. Because it's a download, it still works after shipping cutoffs. I can share the listing if links are allowed here.

Do not use Post A–C in senior/caregiver groups. Do not use Post D as a merch dump.

---

## 4. ADS_READY fix (exact problem lines, then corrected copy)

Source: `https://github.com/mooneyn60-art/skills/blob/claude/blissful-allen-waez05/skills/dropship/ADS_READY.md` (written 2026-11-14). The file is a Shopify + Meta (Facebook/Instagram) launch plan, not an Etsy Ads plan. Corrected variants below are for reuse on Meta, Etsy, or organic posts once prices and policies are confirmed. **Do not run the original lines as-is.**

### Problem line 1 — custom art

Exact line from `ADS_READY.md`:

> No custom art and no photo upload. Each order is a design plus a product.

What other files say:

- `ORDER_RUNBOOK.md` (same folder, also 2026-11-14) is a **custom photo-to-art** workflow: the Shopify line item has "Pet name" and "Pet photo"; art is cut out, styled (Royal / Santa Paws / animated, or Mugshot / License / Tarot / Rookie Card / Pop Art), a proof is emailed, and nothing prints until the customer says yes. Timed test: Mac, Royal style, machine total **215 s (3.6 min)**; estimate "roughly 15 minutes per order." This directly contradicts "no custom art and no photo upload."
- `ETSY_LISTINGS.md` describes **ready-made cartoon designs** (one design + one product), with the instruction: "On each listing, name Printify as the production partner and state that the artwork was made with AI tools." No photo-upload or custom-portrait offer appears in that file.
- `etsy-factory` has **no custom-art policy** for merch. Printable policies are: original puzzles/questions/artwork; personal, family, and classroom use; do not resell, share, or redistribute; instant download, returns not accepted.

**[CONFIRM]** which policy is live on each storefront (Etsy ready-made vs Shopify custom photo art vs both). Until that is confirmed, ad copy must not promise custom portraits, and must not claim "no custom art" if the Shopify custom flow is still offered.

Corrected variants (ready-made Etsy merch, if that is the live policy):

> For people owned by a doodle. Ready-made cartoon designs — pick a design and a product, printed to order. No photo upload on these listings. Artwork created with AI tools. Order by Dec 5 for Christmas.

> These are ready-made doodle designs (Santa Paws, Snow Day, Doodle Mom, Doodle Dad, and more), printed to order on tees, mugs, ornaments, and matching dog bandanas. Not a custom pet portrait. **[CONFIRM]** if custom photo art is still offered on Shopify; if yes, say so on a separate page and do not mix the two offers in one ad.

Corrected variants (if custom photo art is still a live offer — language taken from the runbook, not invented):

> Custom doodle art from your pet's photo: you send the photo and the pet's name, we send a proof, and nothing prints until you say yes. Edits are free. **[CONFIRM price — no custom-art price is in any file].** Plan extra time before the Dec 5 cutoff; the timed art test was about 15 minutes of work per order, not including the proof email and Printify checkout.

### Problem line 2 — "from $21.99"

Exact line from `ADS_READY.md`:

> The doodle mom gift, sorted. Six designs, from $21.99.

Why it is wrong or stale:

- "$21.99" matches only the **ornament** price in `ETSY_LISTINGS.md`. It is not the lowest price in that same file (mug is $18.00). Wall art in that file is $59.99.
- The later `ETSY_STATE.md` price list is lower on ornaments and mugs: ornament **$16.99**, mug **$17.99**, bandana **$18.99**, tee **$26**, tank **$27.99**, sweatshirt **$39.99**. There is no $21.99 in `ETSY_STATE.md`.
- "Six designs" is stale even by `ADS_READY.md`'s own store section (His Majesty, Santa Paws, DJ Dood, Dapper Dood, Good Boy (Allegedly), Road Dogs). `ETSY_LISTINGS.md` then adds a second batch of eight designs and a third batch of mom/dad/parents designs. `ETSY_STATE.md` lists many more Printify products, including funny tees and dog sets, added later on 2026-11-14.
- Printable PDFs start at **$2.99** (Christmas would-you-rather) if those listings are in the same shop — do not mix "from $2.99" into a merch ad unless the ad clearly means digital.

Corrected merch variants — use only after **[CONFIRM]** of the live lowest physical price:

> If live prices follow `ETSY_STATE.md`:  
> The doodle mom gift, sorted. Ready-made doodle tees, mugs, ornaments, and matching dog bandanas. Ornaments from $16.99, tees $26, bandanas $18.99. Order by Dec 5 for Christmas.

> If live prices follow `ETSY_LISTINGS.md`:  
> The doodle mom gift, sorted. Ready-made doodle designs on tees ($26.00), mugs ($18.00), and ornaments ($21.99). Order by Dec 5 for Christmas.

> Safer, no "from" price until confirmed:  
> The doodle mom gift, sorted. Santa Paws, Snow Day, Doodle Mom, Doodle Dad, and matching dog bandanas, printed to order. Order by Dec 5 for Christmas. Prices on the listing.

Corrected Santa Paws variants (replace ad text 3 in `ADS_READY.md`, "Santa Paws is coming. Doodle ornaments for the tree. Order by Dec 5."):

> Santa Paws is coming. Goldendoodle Santa Paws ornament ("Nice list (pending)"), printed to order. **[CONFIRM: $16.99 or $21.99]**. Order by Dec 5 for Christmas.

> Santa Paws tees ($26) and ornaments **[CONFIRM price]**, plus a matching dog bandana ($18.99 in the Printify state file). Order by Dec 5.

Do not reuse "Six designs, from $21.99" in Etsy titles, Pinterest pins, Facebook posts, or Meta ads.

Other `ADS_READY.md` lines to treat as Shopify/Meta-specific, not automatically valid for Etsy: suggested **$5 a day**, one campaign, three ads; audience US ages 25–60, interests Goldendoodle, Labradoodle, Bernedoodle, dog lovers; link to "the store home page"; stop rule "pause any ad that spends $30 with no add-to-cart"; "Meta ad account with a card. None is connected yet"; Shopify password and payments still need Nolan. **[CONFIRM]** whether those Shopify gates are still open, and whether Meta will be used at all this season. Etsy Ads are covered separately in section 5.

---

## 5. Etsy Ads recommendation

No Etsy Ads account status, spend history, ROAS, CTR, or conversion figures appear in any reviewed file. **There are no shop performance numbers to quote.** Budgets below are **suggestions only**. Do not turn ads on without Moondog88's okay.

### Which listings to advertise

Start narrow, on the hero list, and only on listings that are **[CONFIRM]** published, correctly priced, and showing the Dec 5 cutoff:

**First wave (test and, if approved, holiday spend):**

- Santa Paws ornament
- Santa Paws tee
- Snow Day tee (and mug if the listing is live)
- Doodle Mom tee and Doodle Dad tee
- Matching dog bandanas for mom, dad, and Santa, once those listings are live and linked to the human tees

**Second wave, only if first-wave listings are already spending efficiently, or as cheap supporting SKUs:**

- Snow Day / Mom / Dad ornaments and sweatshirts (state file has the product ids; several lack listing copy)
- Instant printables, especially Christmas large-print word search ($3.99) and Christmas would-you-rather ($2.99), which can keep spending after Dec 5 because they do not ship

**Do not advertise yet (until confirmed live and copy-complete):** wall art ($59.99 in listing copy only; no Printify id in `ETSY_STATE.md`); funny tees / extra dog sets that have Printify ids but no `ETSY_LISTINGS.md` copy; any custom-photo product with no public price.

### Suggested daily budget tiers (suggestions, not historical spend)

| Tier | Suggested daily budget | When to use |
|---|---|---|
| Test | **$1–$3 / day** total, on 2–4 hero listings | Now through ~Nov 26, or until a sale is approved. Enough to see if ads deliver impressions and clicks without a big commitment. |
| Holiday | **$5 / day** total | Suggestion aligned with the only budget figure in the files (`ADS_READY.md` suggested $5 a day for Meta — that is not an Etsy Ads result). Consider this for Nov 27–Dec 5 on the same hero listings, if the test is not wasting spend. |
| After Dec 5 | Pause physical merch ads. **[CONFIRM]** a small test ($1–$3 / day) on printables only, or pause all paid ads. | Physical orders can miss Christmas after the cutoff. |

These are not forecasts. They are caps to ask permission for.

### How to judge after 7–14 days (no invented benchmarks)

Because this shop has **no recorded Etsy Ads history**, do not use made-up target ROAS or CTR percentages. After 7–14 days, read Etsy's own ad report and judge with:

- **Spend vs sales attributed to ads (ROAS):** revenue from ads ÷ ad spend. If spend is material and attributed sales are zero at the end of the window, pause or rewrite the listing/ad. There is no shop-specific ROAS target in the files.
- **CTR:** if impressions are coming in and almost no one is clicking, fix the thumbnail/title before raising budget.
- **Conversion:** clicks that become orders or, for printables, instant downloads. A clicky ad that never converts usually means price, shipping, or listing trust — not "need more budget."
- **Order date vs Dec 5:** from about Dec 1, also judge whether an order can still arrive for Christmas. Stop sending paid traffic to physical listings that will miss the cutoff.
- **Fee awareness:** Etsy Ads fees stack on top of the sale/transaction/processing fees cited in `demand.md`. Recheck margin, especially on $2.99–$4.99 printables and on the thin $26 tee margin flagged in `ETSY_LISTINGS.md`.

The Meta stop rule in `ADS_READY.md` ("pause any ad that spends $30 with no add-to-cart") is **not** an Etsy Ads metric (Etsy does not use add-to-cart the same way). Do not apply it blindly to Etsy. For an Etsy test at $1–$3 / day, $30 is 10–30 days of spend — too late for a Dec 5 cutoff. **Suggestion:** review at 7 days and again at 14 days, and pause a listing's ads sooner if it spends its test budget with no attributed orders and no useful click-through. **[CONFIRM]** the exact pause rule Moondog88 wants.

### When to pause

- A listing spends its approved test or holiday budget with no attributed orders after the agreed review window.
- Creative or price on the live listing still uses the stale "from $21.99" or "no custom art" language if that language is false for that listing.
- Dec 5 is reached, for any physical merch ad.
- Printify / production / shipping delays mean the cutoff is no longer honest — **[CONFIRM]** live production times before Black Friday.
- Moondog88 says stop.

---

## Appendix A — Source inventory (read-only review)

No local clones of these repos were on the box. GitHub was read through the cursor-github connector. `gh` on the box is not logged in, so it could not be used as a fallback.

### 1. `mooneyn60-art/skills`, branch `claude/blissful-allen-waez05`

Folder `skills/dropship/` (no subfolders). Last commit on this branch: 2026-11-14, "Update Etsy state with funny tees and dog sets."

| File | URL |
|---|---|
| `ADS_READY.md` | https://github.com/mooneyn60-art/skills/blob/claude/blissful-allen-waez05/skills/dropship/ADS_READY.md |
| `ETSY_LISTINGS.md` | https://github.com/mooneyn60-art/skills/blob/claude/blissful-allen-waez05/skills/dropship/ETSY_LISTINGS.md |
| `ETSY_STATE.md` | https://github.com/mooneyn60-art/skills/blob/claude/blissful-allen-waez05/skills/dropship/ETSY_STATE.md |
| `ORDER_RUNBOOK.md` | https://github.com/mooneyn60-art/skills/blob/claude/blissful-allen-waez05/skills/dropship/ORDER_RUNBOOK.md |

`skills/etsy-factory/` and `fureverfaces/` are **not** on this branch. `etsy-factory` is also absent from default `main`.

### 2. FurEver Faces ads folder

**Not found** in `mooneyn60-art/skills` (either branch above), and **not found** as a folder in `mooneyn60-art/Side-hustles`.

`ADS_READY.md` and `ETSY_LISTINGS.md` reference assets in **"the shorts repo"**: `fureverfaces/ads/ad1.jpg`, `ad2.jpg`, `ad3.jpg` (1080 x 1350) and `fureverfaces/print/` (`PRINT-king.png`, `PRINT-santa.png`, `PRINT-dj.png`, `PRINT-tux.png`, `PRINT-pray.png`, `PRINT-car.png`; also `PRINT-<name>.png` for later designs).

A repo named `mooneyn60-art/fureverfaces` could not be read: the GitHub connector returned `scm_repo_not_accessible` (it may be private, not granted to Cursor's GitHub App, or may not exist). Repository search for `fureverfaces` under `mooneyn60-art` returned 0 results. It did not appear in the 26 repos the connected account owns. Collaborator/org membership listing was empty. **Do not assume the ads images are available until that repo or the shorts repo is identified and access is granted.**

### 3. `mooneyn60-art/skills`, branch `claude/youtube-monetization-strategy-m9vz6i`

`skills/etsy-factory/` (no `SKILL.md` at the folder root):

- Research / price list for printables: https://github.com/mooneyn60-art/skills/blob/claude/youtube-monetization-strategy-m9vz6i/skills/etsy-factory/research/demand.md
- Specs: `skills/etsy-factory/specs/{christmas-bingo,christmas-word-search-large-print,christmas-would-you-rather,large-print-word-search-seniors,thanksgiving-bingo,thanksgiving-word-search-large-print}.json`
- Built products, each with `listing.json`, `listing.md`, Letter/A4 PDFs, and pin-ready images: https://github.com/mooneyn60-art/skills/tree/claude/youtube-monetization-strategy-m9vz6i/skills/etsy-factory/products
- Scripts (generators, not shop policy): `skills/etsy-factory/scripts/`

`skills/dropship/` is **not** on this branch. Oh Meatball material lives here (`skills/oh-meatball/`) but is a YouTube/TikTok playbook for "Meatball Myths"; it has **no Etsy or FurEver Faces cross-promo plan**. `ADS_READY.md` only says: "Add the store link to the bio of the existing pet channel." **[CONFIRM]** whether that channel is Meatball Myths (`@meatballmyths` / YouTube `UCw98RQD81t_339LX5EJqcrg`).

### 4. `mooneyn60-art/Side-hustles`

https://github.com/mooneyn60-art/Side-hustles — public, default branch `main`, created 2026-11-15, **empty repository** (`size: 0`). `GET contents` returned: `This repository is empty.` There is no `etsy-shop/` folder and no `etsy-shop/ads/` conventions to follow yet.

Suggested convention for a later, approved delivery (not created in this pass):

```
etsy-shop/
  README.md                 # shop name, storefront URLs, which price list is live
  ads/
    README.md               # channel mix, spend rules, "DRAFT until Moondog88 okays"
    holiday-plan.md         # this plan, once approved
    etsy-ads.md             # budgets, listing ids, pause rules
    pinterest/              # board list, pin copy, cadence
    facebook-groups.md      # rules notes, approved post copy
    calendar-2026-holiday.md
    performance/            # leave empty until real reports exist; never invent stats
  listings/                 # or pointers to skills/dropship + etsy-factory
```

---

## Appendix B — Existing ad-plan summary (as written, before this draft)

From `ADS_READY.md` unless noted:

- **Channels:** Meta (Facebook and Instagram) ads; free traffic on TikTok and Instagram daily; doodle-owner Facebook groups where rules allow; store link on the existing pet-channel bio. **No Etsy Ads plan and no Pinterest plan** in the files. No sales/coupon calendar. No written Oh Meatball merch cross-promo beyond that possible bio link.
- **Budgets:** "Nolan sets it. Suggested $5 a day, one campaign, three ads." Stop rule: pause any ad that spends $30 with no add-to-cart. Meta ad account "None is connected yet."
- **Products (in that file only):** Doodle Tee, Doodle Mug, Doodle Christmas Ornament, Doodle Wall Art; six designs. This is already behind `ETSY_STATE.md`.
- **Audience / keywords:** US, 25–60; interests Goldendoodle, Labradoodle, Bernedoodle, dog lovers. Listing tags in `ETSY_LISTINGS.md` are the keyword list for Etsy/Pinterest (doodle shirt, doodle mom gift, santa paws, etc.). Printable keywords are in each `listing.json`.
- **Timeline:** written 2026-11-14; ads wasted until Shopify password is removed, payments are on, and one test order is placed; end date Dec 5.
- **Real performance numbers in the merch/ads files:** none for Etsy Ads, Meta ads, Pinterest, or sales. The only measured figures in this set are the **art-timing test** in `ORDER_RUNBOOK.md` (cut-out 6 s; Royal art 208 s; enlarge under 1 s; machine total **215 s (3.6 min)**; estimate ~15 minutes per custom order) and **third-party keyword estimates** in `demand.md` (RankHero, Sep 2025–Sep 2026), plus Etsy fee cites. Oh Meatball `KNOWLEDGE.md` has YouTube/TikTok view stats; those are for the video channel, not the Etsy shop, and should not be used as shop performance.

---

## Appendix C — What is missing or stale as of Nov 15, 2026

- Holiday peak is already underway (Black Friday is in 12 days; Christmas keyword demand was supposed to be listed by early November per `demand.md`).
- No live confirmation that merch or printables are published, or that Shopify gates in `ADS_READY.md` are done.
- `ADS_READY.md` is one day old but already stale on design count, prices ("from $21.99"), custom-art policy, and channel (Shopify/Meta vs Etsy).
- Snow Day / Mom / Dad ornament and sweatshirt listing copy is missing; bandana/tank listing copy is missing; funny tees have Printify ids but no listing text in `ETSY_LISTINGS.md`.
- Snow Day tee/mug descriptions omit the Dec 5 cutoff sentence.
- No sale calendar, coupon amounts, free-shipping policy, or $49 threshold in the files.
- No Etsy Ads, Pinterest, or Facebook-group playbook beyond one sentence each.
- Ads creative (`fureverfaces/ads/`) and print files (`fureverfaces/print/`) were not readable in the repos available to this review.
- `Side-hustles` is empty, so there is no notebook convention in place.
- Thanksgiving printables are still timely through Nov 26, then should stop leading.

---

## Appendix D — Every [CONFIRM] item and every source-file discrepancy

### [CONFIRM] items (facts not in the files, or live status unknown)

1. Public shop name and primary holiday storefront (FurEver Faces vs PrintanPress; Etsy vs Shopify vs both).
2. Which merch price list is live on Etsy (`ETSY_STATE.md` vs `ETSY_LISTINGS.md`).
3. Whether wall art is a live product (in listing copy at $59.99; absent from `ETSY_STATE.md`).
4. Whether sweatshirts, Mom/Dad/Snow ornaments, bandanas, tanks, and funny tees are published, and their live titles.
5. Whether etsy-factory printables are published on Etsy, and their live URLs / go-live dates.
6. Free-shipping policy and any $49 (or other) threshold; margin if shipping is free.
7. Any bundle SKU or bundle discount (none documented).
8. Sale / coupon percents, dates, abandoned-cart and favorited-item offers, and whether Etsy Sales tools are enabled.
9. Current Etsy fee schedule and offsite-ads fees before discounting.
10. Custom-art policy per storefront, and a custom-portrait price if that offer is live (no custom price in any file).
11. Whether Shopify password, payments, and test order in `ADS_READY.md` are done; whether a Meta ad account is now connected; whether Meta will be used this season.
12. Location of `fureverfaces/ads/` and `fureverfaces/print/` (shorts repo / fureverfaces repo not accessible).
13. Whether Meatball Myths is the "existing pet channel" for a bio link; no merch cross-promo plan is written.
14. Pinterest account, board creation, and posting cadence.
15. Facebook groups Moondog88 already belongs to.
16. Live production/shipping times, to keep the Dec 5 cutoff honest.
17. Etsy Ads on/off, approved test and holiday budgets, and the exact pause rule.
18. Whether printables should go on sale at all given $2.99–$4.99 list prices.

### Source-file discrepancies (do not invent a middle value)

| Topic | File A | File B | Note |
|---|---|---|---|
| Custom art | `ADS_READY.md`: "No custom art and no photo upload." | `ORDER_RUNBOOK.md`: full custom photo-art + proof workflow | `ETSY_LISTINGS.md` is ready-made AI cartoon designs only. `etsy-factory` has no merch custom-art policy. |
| "From" price | `ADS_READY.md`: "from $21.99" | `ETSY_LISTINGS.md`: ornaments $21.99, but mugs $18.00 are lower. `ETSY_STATE.md`: ornaments $16.99, mugs $17.99; no $21.99 | Do not use $21.99 as the shop floor. |
| Mug price | `ETSY_LISTINGS.md`: $18.00 | `ETSY_STATE.md`: $17.99 | Off by $0.01. |
| Ornament price | `ETSY_LISTINGS.md`: $21.99 | `ETSY_STATE.md`: $16.99 | Material gap; changes bundle math vs $49. |
| Wall art | `ETSY_LISTINGS.md` / `ADS_READY.md`: product at $59.99 | `ETSY_STATE.md`: no wall-art price or Printify id | |
| Design count | `ADS_READY.md`: four products, six designs | `ETSY_LISTINGS.md`: 24 listings, then 8 more, then mom/dad batch. `ETSY_STATE.md`: many more SKUs including dog sets and funny tees | |
| Tee + bandana vs $49 | Steering assumption that this bundle crosses $49 | `ETSY_STATE.md`: $26 + $18.99 = $44.99, short of $49 | $49 threshold itself is not in the files. |
| Dec 5 cutoff in copy | Santa Paws (and first-batch) listings include "Order by Dec 5" | Snow Day and mom/dad listing descriptions omit it | |
| Shop / channel | `ADS_READY.md`: Shopify store, Meta ads, password still on | `ETSY_STATE.md`: Etsy shop PrintanPress + Printify Etsy and Shopify stores | Dual storefront, one ad plan. |
| Printable prices | `demand.md` planned prices | Each `listing.json` `price` field | These **match** (not a conflict): $3.99 / $2.99 / $4.99 / $3.49 / $3.49 / $3.49. |

---

*End of DRAFT. No spend, posts, coupons, or price changes without Moondog88's okay.*
