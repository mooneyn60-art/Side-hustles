# DRAFT — FurEver Faces Cyber Week sale (Nov 27–Dec 1, 2026)

**Status: DRAFT.** Nothing in this document goes live. No Etsy sale is created, no prices change, and no discount is advertised without Moondog88's explicit okay.

Written 2026-11-15 (America/New_York) for Moondog88's approval. Read-only sources only. No costs or performance stats were invented.

---

## Decision used in this draft

- **Brand:** FurEver Faces (confirmed for this assignment). The Etsy admin shop name in `ETSY_STATE.md` is still PrintanPress; `TASKS.md` still lists the customer-facing name as a decision awaiting Moondog88. Sale title and buyer-facing copy use FurEver Faces.
- **List prices:** `skills/dropship/ETSY_STATE.md` on `claude/blissful-allen-waez05` applies: tee $26, sweatshirt $39.99, mug $17.99, ornament $16.99, pet bandana $18.99, pet tank $27.99. Lowest merch price: **from $16.99**.
- **Hero bundle:** tee + bandana + ornament = $26 + $18.99 + $16.99 = **$61.98**, which clears the $49 free-shipping line at list price.
- **$49 free shipping:** documented in `fureverfaces/policies.md` (Shopify policy draft): orders of $49 or more, free standard shipping; under $49, $5.99. **[CONFIRM]** that the same threshold is set on the Etsy shop, not only in the Shopify draft. `POLICIES_TO_PASTE.md` does not name $49; it says shipping costs are shown at checkout.
- **`DECISIONS.md`:** not found in `mooneyn60-art/Side-hustles` on `main`, including in commit `c959b28`. The written “decisions awaiting Moondog88” are in `TASKS.md`.

---

## Recommended discount: 15% off

**Proposed rate: 15% off the selected listings below, from 12:00 a.m. Friday, Nov 27, 2026 through 11:59 p.m. Tuesday, Dec 1, 2026, America/New_York.**

Why 15%, and not 10% or 20%:

1. **The only discount percentage already in the files is 10%**, as a welcome-signup idea in `skills/dropship/BRIEF.md` (`claude/package-installation-setup-yv4j79`). Cyber Week should be better than a routine signup offer, so 10% is too soft for Black Friday / Cyber Monday.
2. **The hero bundle must still clear $49 after the sale**, or the free-shipping promise breaks. Per-item, rounded to the cent:
   - 10% off: $23.40 + $17.09 + $15.29 = **$55.78** (clears by $6.78)
   - **15% off: $22.10 + $16.14 + $14.44 = $52.68 (clears by $3.68)**
   - 20% off: $20.80 + $15.19 + $13.59 = **$49.58** (clears by only $0.58 — rounding, a missing ornament, or a tax/shipping quirk could drop it under $49)
   - 21% off: $20.54 + $15.00 + $13.42 = **$48.96** (fails)
3. **Margin room is unconfirmed.** No Printify base cost or Printify shipping dollar amount appears in any reviewed file. `ETSY_LISTINGS.md` already warns that $26.00 “leaves a thin margin if shipping is free.” `BRIEF.md` says the ornament at the *higher* $21.99 price (and socks at $19.99) is “likely thin once shipping is paid.” At the live $16.99 ornament price, that risk is greater, not smaller. Going to 20% without costs would be reckless.
4. **The 45% rule** (`BRIEF.md`, exact words): “the supplier cost plus shipping should be ≤ 45% of the price, so ads have room.” That is a **cost cap of 45% of price**, not a 45% profit-after-fees target. At a sale, the test should use the **sale price**. Until costs are confirmed, 15% leaves more headroom under that cap than 20%.

If confirmed Printify cost + shipping on any included SKU is greater than 45% of its 15% sale price, **exclude that listing from the sale** (or run a lower discount on a separate sale). Do not invent a deeper “original” price. `BRIEF.md`: never fake discounts from a made-up original price.

---

## Etsy Sales & Discounts settings (to enter after approval)

**[CONFIRM]** the exact labels in today's Etsy Seller dashboard (Marketing → Sales & Discounts, or equivalent). The fields to set:

| Setting | Draft value |
|---|---|
| **Sale type** | Percentage off (a sale on selected listings, not a coupon code, and not a shop-wide “all listings” sale) |
| **% off** | **15%** |
| **Start** | Friday, Nov 27, 2026, 12:00 a.m. America/New_York |
| **End** | Tuesday, Dec 1, 2026, 11:59 p.m. America/New_York (covers Black Friday, Small Business Saturday, Cyber Monday, and the following Tuesday) |
| **Listings** | Only the included list below. Do not apply shop-wide. |
| **Minimum order** | **None.** A minimum would block standalone printable purchases ($2.99–$4.99) and single ornaments. Free shipping is a separate $49 threshold, not a sale minimum. |
| **Sale title** (internal / on-sale badge) | FurEver Faces Cyber Week — 15% off |
| **Buyer-facing message** | See the text below. |

### Buyer-facing message (draft)

> Cyber Week at FurEver Faces: 15% off our Christmas doodle merch and instant printable games, Friday, Nov 27 through Tuesday, Dec 1. For people owned by a doodle. Ready-made cartoon designs — pick a design and a product, printed to order in the USA. Order physical gifts by Dec 5 for Christmas delivery. Free standard shipping on orders of $49 or more **[CONFIRM this is also set on Etsy]**. The Santa Paws (or matching Mom/Dad) tee + dog bandana + ornament bundle is $61.98 before the sale and $52.68 after 15% off, so it still qualifies for free shipping. Instant PDF games are delivered immediately — no shipping, and they still work after Dec 5. Artwork on the merch was created with AI tools.

Do not add invented stock limits, “bestseller” badges, or a fake compare-at price.

---

## Listings in the sale

Include only hero and supporting SKUs that have an `ETSY_STATE.md` price, plus the Christmas / evergreen printables that already have listing files. **[CONFIRM]** each is actually published on Etsy before adding it to the sale.

### Physical merch (ready-made cartoons only)

Use `ETSY_STATE.md` prices. Prefer the rewritten titles in `Side-hustles/listings/` where they exist.

**Hero (lead with these):**

- Santa Paws tee — $26 (`tee santa`)
- Santa Paws ornament — $16.99 (`orn-santa`). Rewritten title: “Santa Paws Goldendoodle Christmas Ornament, Cute Doodle Tree Decor, Funny Gift for Doodle Mom”
- Matching Santa Paws pet bandana — $18.99 (`band-santa`)
- Snow Day tee — $26 (`tee snow`)
- Snow Day ornament — $16.99 (`orn-snow`) — listing copy still missing in `ETSY_LISTINGS.md`; include only if the live listing exists **[CONFIRM]**
- Doodle Mom tee — $26 (`tee mom`). Rewritten title: “Doodle Mom Shirt, Goldendoodle Mama Tee, Curls Cuddles & Chaos, Cute Cartoon Dog Mom Gift”
- Doodle Dad tee — $26 (`tee dad`)
- Doodle Mom ornament — $16.99 (`orn-mom`) — same copy gap **[CONFIRM]**
- Doodle Dad ornament — $16.99 (`orn-dad`) — same copy gap **[CONFIRM]**
- Matching Doodle Mom pet bandana — $18.99 (`band-mom`)
- Matching Doodle Dad pet bandana — $18.99 (`band-dad`)

**Supporting, same designs (include if live):**

- Santa Paws / Snow Day / Doodle Mom / Doodle Dad mugs — $17.99
- Santa Paws / Snow Day / Doodle Mom / Doodle Dad sweatshirts — $39.99
- Matching pet tanks for Santa / Mom / Dad (`tank-santa`, `tank-mom`, `tank-dad`) — $27.99
- Doodle Parents tee / mug / bandana / tank (`tee fam`, `mug-fam`, `band-fam`, `tank-fam`) at the same category prices — optional supporting family gift, not the first hero

### Digital printables

- Christmas Word Search, Large Print, 24 puzzles — $3.99 (rewritten listing in `listings/christmas-word-search-large-print.md`)
- Christmas Would You Rather, 60 questions — $2.99
- Christmas Bingo, 30 cards — $3.49
- Large Print Word Search for Seniors, 40 puzzles — $4.99

Digital items have no shipping; they do not need the $49 threshold and remain useful after Dec 5.

---

## Listings excluded (do not add to this sale)

| Excluded | Why |
|---|---|
| Thanksgiving bingo ($3.49) and Thanksgiving word search ($3.49) | Thanksgiving is Thursday, Nov 26. This sale starts Nov 27. Do not discount stale holiday goods. |
| Unbuilt printables (Christmas trivia, classroom jobs, sinking-funds planner, meal planner) | Planned in `demand.md`, not built. |
| Custom / personalized photo art (Rookie Card, tarot, license, memorial, ugly sweater, “World's Okayest Human,” etc.) | `TASKS.md` and `BRIEF.md`: do not advertise this line until payments, a test order, and the proof-email step work. `ADS_READY.md` and the runbook still disagree on whether custom art is offered. No custom-art price is in the Etsy state file. |
| Wall art ($59.99 in `ETSY_LISTINGS.md` only) | No Printify id in `ETSY_STATE.md`. |
| Funny tees and extra dog sets (glow, velcro, sock, bed, surf2, zoom, mud, treat, squirrel, teddy, want, cool, etc.) | Printify ids exist; no listing copy in `ETSY_LISTINGS.md` and not on the short Christmas hero list. **[CONFIRM]** and keep them out of Cyber Week unless they are live and copy-complete. |
| Any listing whose confirmed Printify cost + shipping is **> 45% of the 15% sale price** | Fails the `BRIEF.md` rule. Exclude it, or do not start the sale until costs are checked. See the table below. |
| Shopify-only draft products (socks $19.99, sherpa blanket $94.99 in `BRIEF.md`) | Not in the Etsy state price list. |

---

## Margin table

### How the 45% rule is applied

Exact rule, `BRIEF.md` (2026-11-14):

> Rule: the supplier cost plus shipping should be ≤ 45% of the price, so ads have room.

On a sale, “the price” is the **sale price**. Pass = (Printify base + shipping) ≤ 0.45 × sale price. Fail = above that cap.

### Costs: not in the files

A search of `ETSY_STATE.md`, `ETSY_LISTINGS.md`, `BRIEF.md`, `HANDOFF.md`, `POLICIES_TO_PASTE.md`, `fureverfaces/policies.md`, the Side-hustles audit, listings, and design direction found **no Printify base cost and no Printify shipping dollar amount** for tees, bandanas, ornaments, mugs, sweatshirts, or tanks. Providers are named in `ETSY_STATE.md` (Monster Digital for tees/sweatshirts, SPOKE for mugs, Duplium for ornaments, Printed Mint for bandanas/tanks) but without prices.

**Every physical row below has Cost = [CONFIRM]. No merch listing can be marked pass or fail on the 45% rule until those numbers are filled in.** Do not invent catalog averages.

`BRIEF.md` already flags the older $21.99 ornament as “likely thin once shipping is paid.” That is a warning, not a measured cost. At the live $16.99 ornament price, treat ornaments as **higher risk** and confirm cost first.

### Etsy fees used (assumption, labeled)

`etsy-factory/research/demand.md` (citing Gelato, Marmalead, and Checkoutpage, not this shop's dashboard):

- Listing fee $0.20 per listing, renews every 4 months **or on sale**
- Transaction fee **6.5%**
- US payment processing **3% + $0.25**

**These rates are used below as an assumption and are labeled as such.** **[CONFIRM]** the live fee schedule, whether offsite-ads fees also apply (not in the files; not included here), and whether processing's $0.25 is per order or per listing. The per-listing table treats a **single-item order** (includes one $0.25). A three-item hero bundle pays the $0.25 once; that case is in the bundle note.

The $0.20 listing-renewal-on-sale is a shop-level cost when the sale is created or a listing is sold, **not** baked into each unit in the table.

Fee formula used: `fees = round(0.095 × sale price + 0.25, 0.01)`.

“After-fee leftover” = sale price − assumed fees. That leftover still has to cover Printify cost + shipping. It is **not** profit and **not** a margin vs the 45% rule.

### Physical merch (cost unknown — no 45% pass/fail)

| Listing (category) | List price | 15% sale price | Cost (Printify base + shipping) | Assumed Etsy fees | After-fee leftover | 45% cost cap at sale price | 45% rule |
|---|---:|---:|---|---:|---:|---:|---|
| Tee (Santa Paws, Snow Day, Doodle Mom, Doodle Dad, Doodle Parents) | $26.00 | $22.10 | **[CONFIRM]** | $2.35 | $19.75 | $9.95 | **Cannot score** — need cost. If cost + ship > $9.95, FAIL: exclude or do not discount this SKU. |
| Pet bandana (Santa, Mom, Dad, Fam) | $18.99 | $16.14 | **[CONFIRM]** | $1.78 | $14.36 | $7.26 | **Cannot score.** Fail if cost + ship > $7.26. |
| Ornament (Santa, Snow Day, Mom, Dad) | $16.99 | $14.44 | **[CONFIRM]** | $1.62 | $12.82 | $6.50 | **Cannot score. Higher risk:** `BRIEF.md` already called the *higher* $21.99 ornament likely thin after shipping. Confirm this row first. Fail if cost + ship > $6.50. |
| Mug | $17.99 | $15.29 | **[CONFIRM]** | $1.70 | $13.59 | $6.88 | **Cannot score.** Fail if cost + ship > $6.88. |
| Sweatshirt | $39.99 | $33.99 | **[CONFIRM]** | $3.48 | $30.51 | $15.30 | **Cannot score.** Fail if cost + ship > $15.30. |
| Pet tank top | $27.99 | $23.79 | **[CONFIRM]** | $2.51 | $21.28 | $10.71 | **Cannot score.** Fail if cost + ship > $10.71. |

At list price, the 45% caps would be: tee $11.70, bandana $8.55, ornament $7.65, mug $8.10, sweatshirt $18.00, tank $12.60. A 15% sale tightens each cap. If a SKU already fails at list price, it must stay out of the sale (and should be repriced, separately, with Moondog88's okay).

If free shipping is granted on a $52.68 bundle, Printify shipping for three items is paid by the shop and must be included in the bundle cost, not ignored because the buyer paid $0 shipping. **[CONFIRM]** whether Printify charges shipping per line or consolidates.

### Digital printables (cost assumed $0)

Assumption, labeled: a digital PDF has **$0 Printify cost and $0 shipping**. If a platform file fee exists, **[CONFIRM]** and add it.

| Listing | List price | 15% sale price | Cost | Assumed Etsy fees | Profit (sale − cost − fees) | Profit margin on sale price | 45% cost cap | 45% rule |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| Christmas word search, 24 puzzles | $3.99 | $3.39 | $0 (digital assumption) | $0.57 | $2.82 | 83.2% | $1.53 | **PASS** under the $0-cost assumption (cost 0% ≤ 45%) |
| Christmas would-you-rather | $2.99 | $2.54 | $0 (digital assumption) | $0.49 | $2.05 | 80.7% | $1.14 | **PASS** under the same assumption |
| Christmas bingo | $3.49 | $2.97 | $0 (digital assumption) | $0.53 | $2.44 | 82.2% | $1.34 | **PASS** under the same assumption |
| Large-print word search for seniors | $4.99 | $4.24 | $0 (digital assumption) | $0.65 | $3.59 | 84.7% | $1.91 | **PASS** under the same assumption |

No digital listing fails the 45% rule on that assumption. They remain in the sale.

### Hero bundle at 15% off, and the $49 line

| | Amount |
|---|---:|
| List: tee + bandana + ornament | $26.00 + $18.99 + $16.99 = **$61.98** |
| After 15% off (per-item, rounded) | $22.10 + $16.14 + $14.44 = **$52.68** |
| vs $49 free-shipping threshold | **Still clears, by $3.68** |
| Assumed Etsy fees on a $52.68 order (one $0.25 processing fee) | $5.25 |
| After-fee leftover, before Printify cost + shipping | $47.43 |
| Combined 45% cost cap on $52.68 | $23.71 |

**The sale price of the hero bundle still clears $49.** That is why 15% was chosen instead of 20% ($49.58, only $0.58 of cushion) or 21% ($48.96, fails).

The bundle cannot be scored against the 45% rule until the three Printify costs (and whether shipping is charged once or three times) are confirmed. If combined cost + shipping > $23.71, the bundle fails the rule at 15% off — **[CONFIRM]** and either drop the sale or exclude the failing SKU (most likely the ornament, given the brief's warning).

A buyer who purchases only the tee + bandana at sale pays $22.10 + $16.14 = **$38.24**, which is **under $49** and would pay **$5.99** shipping if that Shopify policy is also live on Etsy. Do not claim that the two-item set ships free. The holiday plan already showed the list-price pair at $44.99, also short of $49.

---

## Approval checklist for Moondog88

- [ ] Approve **15% off**, Nov 27 12:00 a.m. through Dec 1 11:59 p.m. America/New_York, selected listings only, no minimum order.
- [ ] Confirm live Etsy shipping is free at $49, $5.99 below.
- [ ] Fill in Printify base + shipping for tee, bandana, ornament (at least), then mug, sweatshirt, and tank. Re-run the 45% test on **sale** prices. Exclude any SKU that fails.
- [ ] Confirm which of the included listings are actually published.
- [ ] Confirm current Etsy fee rates and whether offsite-ads fees apply.
- [ ] Confirm the buyer-facing shop name on the sale badge (this draft uses FurEver Faces).

Until the cost cells are filled, **this sale should not go live.** The 15% rate and the $49 bundle math are ready; the merch margin pass/fail is not.

---

*End of DRAFT. No sale, spend, or price change without Moondog88's okay.*
