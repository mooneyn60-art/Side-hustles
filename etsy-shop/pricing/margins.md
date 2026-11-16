# FurEver Faces — margin check with real shipping (read-only)

**Date:** 2026-11-15, America/New_York (follow-up; shipping settings and Printify rates pulled the same evening)  
**Author:** Etsy: Pricing & Profit  
**Scope:** Read-only on the repo, Shopify Admin, and public Printify sources. No prices, products, or store settings were changed. This file is a local work product under `/workspace/etsy-pricing/`.

## Rule used

Shop rule (G6 in `creative/DEEP-DIVE-2026-11-15.md`, quoted from `skills/dropship/BRIEF.md`, restated in `etsy-shop/listings/03-pricing-memo.md` and `DECISIONS.md`):

> Supplier cost plus shipping must be at most 45% of price.

This is a **cost-ratio** cap, not a “profit ÷ price ≥ 45%” test. Official PASS/FAIL is against the cost-ratio rule only.

**Live prices** (source of truth: `skills/dropship/ETSY_STATE.md` on `mooneyn60-art/skills` branch `claude/blissful-allen-waez05`; confirmed on every active Shopify product of that type): tee $26.00, sweatshirt $39.99, mug $17.99, ornament $16.99, bandana $18.99, tank $27.99.

**Caveat on `unitCost`:** Shopify `inventoryItem.unitCost` is unlabeled. Nothing in Admin or the repo states whether it is Printify production cost only, or production plus shipping. Official scoring below uses **Case A: `unitCost` + real US Standard first-item shipping** (the live method on the Printify delivery profiles). **Case B** (`unitCost` already includes shipping; do not add shipping again) is shown for comparison and is not treated as proven. `$9.40` on the S–XL tee is below published Monster Digital blank+print starting prices, which is consistent with Case A but is not proof.

---

## Shopify shipping settings (egayix-ff.myshopify.com)

Read via Admin GraphQL `deliveryProfiles` on 2026-11-15, America/New_York. Seven profiles; `pageInfo.hasNextPage` is false. Variant counts sum to **819**, matching the full catalog (75 active + 11 archived + 1 draft).

**The $49 free-shipping / $5.99 otherwise policy in `DECISIONS.md` is not what Admin has configured.** Live merch uses Printify-managed “Standard Delivery” profiles that charge the customer Printify’s Standard first/additional rates (weight-tiered). The only free-shipping threshold in Admin is **$70**, and it applies only to the leftover General profile.

### 1. General profile (default=`true`, `coversAllItems`=`false`)

- 110 variants (the remainder after Printify profiles; not the 75 live merch types).
- Origin: merchant location **103 Babylon Ave, West Islip, New York, US** (active, ships, fulfills online orders; not a fulfillment service).
- One zone: **Domestic** (United States only). `locationsWithoutRatesCount` = 1.
- Active merchant rates (all `active=true`):
  - **Standard**, no condition: **$8.00 USD**
  - **Standard**, when `TOTAL_PRICE >= $70.00 USD`: **$0.00 USD** (free shipping)
  - **Express**, no condition: **$15.00 USD**

### 2. Printify-managed profiles (default=`false`)

These cover the live merch. Each has `originLocationCount` = 1 and `locationsCount` = 1, but the locations connection returned no nodes in this query (likely a fulfillment-service location; `includeLegacy` was not set on the successful query). `locationsWithoutRatesCount` = 1 on each (the West Islip merchant location is not rated here). No Economy or free-shipping methods. US rates are weight-tiered; the first bracket matches Printify Standard first-item, and each step equals the published additional-item amount.

| Profile | Variants | US zone method | US first bracket (0–0.33 lb) | Additional step (matches catalog) |
|---|---:|---|---:|---:|
| Standard: Monster Digital, Kids clothes, Long-sleeve, T-Shirt, Tank Top, V-neck | 465 | Standard Delivery, 4–10 business days | **$4.95** | +$2.40 |
| Standard: Monster Digital, Hoodie, Sweatshirt | 150 | Standard Delivery, 4–10 business days | **$8.79** | +$2.09 |
| Standard: SPOKE Custom Products, 125, 68,Mug,11oz | 10 | Standard Delivery, 4–10 business days | **$7.29** | +$3.09 |
| Standard: Duplium, 537,Home Decor | 4 | Standard Delivery, 8–20 business days | **$17.09** | +$1.59 |
| Standard: Printed Mint, BP-562 Pet Bandana, Pet Bandana Collar | 20 | Standard Delivery, 6–11 business days | **$5.69** | +$0.99 |
| Standard: Printed Mint, BP-571 Pet Tank Tops | 60 | Standard Delivery, 6–11 business days | **$5.99** | +$0.99 |

International zones also exist on each Printify profile (Canada, Australia where present, a 27-country group, Rest of the World). This check scores **US** only. First brackets on those zones also match the public Printify destination tables (for example Monster Digital tees: CA $9.69, AU $12.99, EU $13.49, ROW $10.39).

---

## Printify US shipping rates (first item / each additional)

Printify IDs from `skills/dropship/ETSY_STATE.md` on `claude/blissful-allen-waez05`, confirmed in the public catalog (`GET https://api.printify.com/v1/catalog/blueprints.json`, unauthenticated, 2026-11-15) and in the Shopify profile names above.

| Type | Blueprint | Provider | Product (catalog title) |
|---|---:|---|---|
| Tee | 12 | 29 Monster Digital | Bella+Canvas 3001 Unisex Jersey Short Sleeve Tee |
| Sweatshirt | 49 | 29 Monster Digital | Gildan 18000 Unisex Heavy Blend Crewneck Sweatshirt |
| Mug | 68 | 1 SPOKE Custom Products | Mug 11oz |
| Ornament | 537 | 41 Duplium | Ceramic Ornament, 1-Pack |
| Bandana | 562 | 70 Printed Mint | Pet Bandana (Evergreen) |
| Tank | 571 | 70 Printed Mint | Pet Tank Top (Doggie Skins 3902) |

### Rates used for official scoring (US Standard, all sizes)

| Type | First item | Additional item | Sources (retrieved 2026-11-15, America/New_York) |
|---|---:|---:|---|
| Tee | **$4.95** | **$2.40** | [Monster Digital shipping page](https://printify.com/shipping-rates/monster-digital/) (Unisex Jersey Short Sleeve Tee, US Standard, 2–5 business days); [v1 catalog shipping API](https://api.printify.com/v1/catalog/blueprints/12/print_providers/29/shipping.json) (US profile `first_item.cost` 495 / `additional_items.cost` 240 cents); Shopify profile first bracket $4.95, next $7.35 = 4.95+2.40 |
| Sweatshirt | **$8.79** | **$2.09** | [Monster Digital shipping page](https://printify.com/shipping-rates/monster-digital/) (Unisex Heavy Blend Crewneck Sweatshirt, US Standard); [v1 API](https://api.printify.com/v1/catalog/blueprints/49/print_providers/29/shipping.json) (879 / 209 cents); Shopify first bracket $8.79, next $10.88 = 8.79+2.09 |
| Mug 11oz | **$7.29** | **$3.09** | [SPOKE Custom Products shipping page](https://printify.com/shipping-rates/spoke-custom-products/) (Mug 11oz, US Standard); [v1 API](https://api.printify.com/v1/catalog/blueprints/68/print_providers/1/shipping.json) (729 / 309 cents); Shopify first bracket $7.29, next $10.38 = 7.29+3.09 |
| Ornament | **$17.09** | **$1.59** | [Duplium shipping page](https://printify.com/shipping-rates/duplium/) (Ceramic Ornament, 1-Pack, United States, 5–15 business days); Shopify profile first bracket $17.09, next $18.68 = 17.09+1.59, labeled 8–20 business days. **The v1 shipping API for blueprint 537 / provider 41 returned `Unauthenticated` without a token.** Canada on the same page is cheaper ($8.29 first / $0.99 additional, 2–5 days), which is consistent with a non-US origin shipping into the US. |
| Bandana | **$5.69** | **$0.99** | [Printed Mint shipping page](https://printify.com/shipping-rates/printed-mint/) (Pet Bandana, US, 2–5 business days); Shopify first bracket $5.69, next $6.68 = 5.69+0.99, labeled 6–11 business days. **v1 shipping API for 562 / 70 returned `Unauthenticated`.** |
| Tank | **$5.99** | **$0.99** | [Printed Mint shipping page](https://printify.com/shipping-rates/printed-mint/) (Pet Tank Top, US, 2–5 business days); Shopify first bracket $5.99, next $6.98 = 5.99+0.99, labeled 6–11 business days. **v1 shipping API for 571 / 70 returned `Unauthenticated`.** |

Catalog API shape (costs in cents) matches [Printify developer docs](https://developers.printify.com/). The v2 shipping endpoints required auth (HTTP 401). Unauthenticated `GET` of a single blueprint or provider record was inconsistent (some 200, some `Unauthenticated`); titles above that failed the single-resource endpoint still appear in the public `blueprints.json` list and on the shipping-rate pages.

### Also published, not used as the live Shopify method

| Type | Method | First | Additional | Sources |
|---|---|---:|---:|---|
| Tee | Economy (US, 4–8 business days) | $4.49 | $2.09 | [Monster Digital page](https://printify.com/shipping-rates/monster-digital/); [v1 API](https://api.printify.com/v1/catalog/blueprints/12/print_providers/29/shipping.json) (449 / 209 cents) |
| Sweatshirt | Economy (US, 4–8 business days) | $7.99 | $2.09 | [Monster Digital page](https://printify.com/shipping-rates/monster-digital/); [v1 API](https://api.printify.com/v1/catalog/blueprints/49/print_providers/29/shipping.json) (799 / 209 cents) |
| Mug 11oz | Economy (US, 4–8 business days) | $6.69 | $2.99 | [SPOKE page](https://printify.com/shipping-rates/spoke-custom-products/); [v1 API](https://api.printify.com/v1/catalog/blueprints/68/print_providers/1/shipping.json) (669 / 299 cents) |
| Tee (subset of variants) | Express | $7.99 | $2.40 | [v1 API](https://api.printify.com/v1/catalog/blueprints/12/print_providers/29/shipping.json) (third US profile, 30 of 318 variant IDs); [Printify shipping options](https://help.printify.com/hc/en-us/articles/4483626155409-What-are-Printify-s-shipping-options) (Express $7.99 + $2.40 additional, Bella+Canvas 3001 front prints). **Not a row on the public Monster Digital table, and no Express method on the Shopify Printify tee profile.** |

Ornament, bandana, and tank have **no Economy row** on their public US tables (a single US rate each).

### Holiday surcharge (in effect today)

From **October 15, 2026 through January 17, 2027**, Printify adds a **$0.40 USD surcharge per US-destination order** (per order, not per parcel; not baked into the catalog tables; not auto-synced into store prices). Sources: [Printify shipping-rates index](https://printify.com/shipping-rates/) and [Holiday Shipping Surcharge 2026](https://help.printify.com/hc/en-us/articles/28893325248145-Holiday-Shipping-Surcharge-2026). Official Case A PASS/FAIL below is **`unitCost` + Standard first-item** without the surcharge (already a FAIL on every type). The surcharge is shown as an add-on to merchant cost.

Multi-item rule (same Print Provider): same product type uses first + additional; a t-shirt plus a sweatshirt is **first + first**. Source: [How are shipping costs calculated for multiple items?](https://help.printify.com/hc/en-us/articles/4483643971473-How-are-shipping-costs-calculated-for-multiple-items).

---

## (a) What already exists, and where

| Path | What it contains for pricing/cost |
|---|---|
| `etsy-shop/finance/` | **Does not exist** on `mooneyn60-art/Side-hustles` `main`. |
| `etsy-shop/SCOREBOARD.md` | Empty template only. |
| `etsy-shop/listings/03-pricing-memo.md` | Recommendation only (2026-11-15). Live price list, 45% caps. No actual Printify figures at the time it was written. |
| `DECISIONS.md` | Live prices, **$49 Shopify free / $5.99 otherwise** (not what Admin now has), Cyber Week 15% only under the ceilings, ornament $16.99 pending a margin check. |
| `TASKS.md` | Open work: pull Printify costs, score 45% and Cyber Week, fill the scoreboard, ornament check, Shopify shipping decision. Notes the “Free shipping $49+” banner may not match the real setting — **confirmed: it does not.** |
| `skills/dropship/ETSY_STATE.md` (branch `claude/blissful-allen-waez05`) | Live prices, Printify IDs. No unit costs or shipping amounts. |
| Same branch: `ETSY_LISTINGS.md` | “$26.00 leaves a thin margin if shipping is free.” No dollar costs. |
| Shopify Admin (this pass) | `unitCost` on all 75 active products; delivery profiles, zones, and rates as above. Compare-at is null on every variant. |

---

## (b) Shopify store and catalog

- **Store name:** FurEver Faces
- **Domain:** egayix-ff.myshopify.com
- **Plan:** Basic
- **Currency:** USD
- **Country:** United States

**Product count:** 87 total — 75 ACTIVE, 11 ARCHIVED, 1 DRAFT.

Active catalog (75): 31 tees, 10 sweatshirts, 10 mugs, 4 ornaments, 10 bandanas, 10 tanks. Prices are uniform by type.

`unitCost` (unchanged from the first pass): tee $9.40 S–XL / $11.49 2XL; sweatshirt $14.34 S–XL / $16.47 2XL; mug $4.81; ornament $4.68; bandana $10.54 (20×10) / $11.87 (27×13); tank $17.30 (all sizes).

Archived/draft items are not rescored here.

---

## (c) Official 45% scores — Case A (`unitCost` + US Standard first-item)

Caps: exact 45% of list, and that figure rounded to the nearest cent. Official FAIL if `unitCost` + Standard first-item **exceeds** the exact 45% cap.

| Type / size | List | unitCost | Printify US Standard first | Cost + ship | Cost % of list | 45% cap (exact / rounded) | Official |
|---|---:|---:|---:|---:|---:|---|---|
| Tee S–XL | $26.00 | $9.40 | $4.95 | $14.35 | 55.19% | $11.70 / $11.70 | **FAIL** |
| Tee 2XL | $26.00 | $11.49 | $4.95 | $16.44 | 63.23% | $11.70 / $11.70 | **FAIL** |
| Sweatshirt S–XL | $39.99 | $14.34 | $8.79 | $23.13 | 57.84% | $17.9955 / $18.00 | **FAIL** |
| Sweatshirt 2XL | $39.99 | $16.47 | $8.79 | $25.26 | 63.17% | $17.9955 / $18.00 | **FAIL** |
| Mug 11oz | $17.99 | $4.81 | $7.29 | $12.10 | 67.26% | $8.0955 / $8.10 | **FAIL** |
| Ornament | $16.99 | $4.68 | $17.09 | $21.77 | **128.13%** | $7.6455 / $7.65 | **FAIL** (shipping alone exceeds list) |
| Bandana 20×10 | $18.99 | $10.54 | $5.69 | $16.23 | 85.47% | $8.5455 / $8.55 | **FAIL** (already failed on unitCost alone) |
| Bandana 27×13 | $18.99 | $11.87 | $5.69 | $17.56 | 92.47% | $8.5455 / $8.55 | **FAIL** (already failed on unitCost alone) |
| Tank (all sizes) | $27.99 | $17.30 | $5.99 | $23.29 | 83.21% | $12.5955 / $12.60 | **FAIL** (already failed on unitCost alone) |

Adding the in-effect **$0.40 US order surcharge** raises every cost % by about 1.5–2.4 points (tee S–XL 56.73%, ornament 130.49%) and does not change any official result.

Economy, if it were used instead of Standard (tees, sweatshirts, and mugs only; **not** configured on the Shopify profiles), is still a FAIL: tee S–XL $13.89 (53.42%), sweatshirt S–XL $22.33 (55.84%), mug $11.50 (63.92%).

### Minimum list price to pass Case A at Standard first-item (no surcharge)

| Type / size | Min list (cost+ship ≤ 45%) | Current list |
|---|---:|---:|
| Tee S–XL | $31.89 | $26.00 |
| Tee 2XL | $36.53 | $26.00 |
| Sweatshirt S–XL | $51.40 | $39.99 |
| Sweatshirt 2XL | $56.13 | $39.99 |
| Mug 11oz | $26.89 | $17.99 |
| Ornament | $48.38 | $16.99 |
| Bandana 20×10 | $36.07 | $18.99 |
| Bandana 27×13 | $39.02 | $18.99 |
| Tank | $51.76 | $27.99 |

With the $0.40 surcharge, each minimum is about $0.89 higher (tee S–XL $32.78).

### Case B (only if `unitCost` already includes shipping — unproven)

Do not add Printify shipping again. Then: bandanas and tanks still **FAIL** on unitCost alone (55.50% / 62.51% and 61.81%). Tee S–XL 36.15%, tee 2XL 44.19%, sweatshirt S–XL 35.86%, sweatshirt 2XL 41.19%, mug 26.74%, ornament 27.55% would be under the cap. This case is recorded so the unlabeled-cost caveat is not ignored; it is **not** the official score.

---

## (d) Cyber Week 15% off (Nov 27–Dec 1, America/New_York)

Approved only where cost + shipping is under the ceiling (45% of the 15%-off price, already verified as nearest-cent rounding): tee $9.95, bandana $7.26, ornament $6.50, mug $6.88, sweatshirt $15.30, tank $10.71.

| Type / size | 15% off price | Ceiling | unitCost | + Standard first | vs ceiling | Official |
|---|---:|---:|---:|---:|---|---|
| Tee S–XL | $22.10 | $9.95 | $9.40 | $14.35 | Over by $4.40 | **FAIL** |
| Tee 2XL | $22.10 | $9.95 | $11.49 | $16.44 | Over by $6.49 | **FAIL** (unitCost alone already over) |
| Sweatshirt S–XL | $33.99 | $15.30 | $14.34 | $23.13 | Over by $7.83 | **FAIL** |
| Sweatshirt 2XL | $33.99 | $15.30 | $16.47 | $25.26 | Over by $9.96 | **FAIL** (unitCost alone already over) |
| Mug 11oz | $15.29 | $6.88 | $4.81 | $12.10 | Over by $5.22 | **FAIL** |
| Ornament | $14.44 | $6.50 | $4.68 | $21.77 | Over by $15.27 | **FAIL** |
| Bandana 20×10 | $16.14 | $7.26 | $10.54 | $16.23 | Over by $8.97 | **FAIL** |
| Bandana 27×13 | $16.14 | $7.26 | $11.87 | $17.56 | Over by $10.30 | **FAIL** |
| Tank | $23.79 | $10.71 | $17.30 | $23.29 | Over by $12.58 | **FAIL** |

**No live merch type qualifies for the approved 15% Cyber Week sale under Case A.** To hold a 15% off sale and still meet the 45% rule at Standard first-item, list prices would need to start at about $37.52 (tee S–XL), $42.98 (tee 2XL), $60.47 (sweatshirt S–XL), $66.04 (sweatshirt 2XL), $31.63 (mug), $56.92 (ornament), $42.43 / $45.91 (bandanas), $60.89 (tank).

Case B would still block Cyber Week on bandanas, tanks, tee 2XL, and sweatshirt 2XL. Tee S–XL, sweatshirt S–XL, mug, and ornament would be under the ceiling only if shipping is already inside `unitCost`.

---

## (e) Can Shopify afford free shipping over $49?

**Not under the 45% rule, if `unitCost` is production-only (Case A). And that policy is not what the store is running today.**

Current Admin behavior for live merch: the customer **pays Printify Standard** (calculated / weight-tiered). There is no $49 free threshold and no $5.99 flat rate on those profiles. The only free threshold is **$70 on the General profile** (110 non-Printify-profile variants).

If free shipping over $49 were turned on, the shop would collect $0 shipping and still pay Printify Standard + the $0.40 US surcharge. The 45% rule uses supplier cost + shipping versus **list price**, so collecting shipping from the customer does not improve the official ratio; it only changes cash and net profit.

Realistic $49+ baskets, Case A, US Standard, different types = first + first, same type = first + additional:

| Basket | List | unitCost | Printify ship | + surcharge | Cost + ship | Cost % | Est. Shopify fee (2.9% + $0.30 on list) | Est. net if shipping is free |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Sweatshirt + tee (S–XL) | $65.99 | $23.74 | $8.79 + $4.95 = $13.74 | $0.40 | $37.88 | **57.40% FAIL** | $2.21 | $25.90 |
| Two tees (S–XL) | $52.00 | $18.80 | $4.95 + $2.40 = $7.35 | $0.40 | $26.55 | **51.06% FAIL** | $1.81 | $23.64 |
| Sweatshirt + mug | $57.98 | $19.15 | $8.79 + $7.29 = $16.08 | $0.40 | $35.63 | **61.45% FAIL** | $1.98 | $20.37 |
| Sweatshirt + ornament | $56.98 | $19.02 | $8.79 + $17.09 = $25.88 | $0.40 | $45.30 | **79.50% FAIL** | $1.95 | $9.73 |
| Sweatshirt + bandana 20×10 | $58.98 | $24.88 | $8.79 + $5.69 = $14.48 | $0.40 | $39.76 | **67.41% FAIL** | $2.01 | $17.21 |
| Two sweatshirts (S–XL) | $79.98 | $28.68 | $8.79 + $2.09 = $10.88 | $0.40 | $39.96 | **49.96% FAIL** | $2.62 | $37.40 |

Every realistic $49+ basket still misses the 45% cap under Case A. Two sweatshirts come closest and still fail. The ornament pairing is especially poor because Duplium’s US first-item rate is $17.09.

Shopify Payments is still an **estimate** of 2.9% + $0.30 (Basic); the live card rate was not read from billing.

---

## (f) Is the $26 tee priced right?

**No, not under Case A and the 45% rule.**

- S–XL: $9.40 + $4.95 = $14.35, which is 55.19% of $26 (cap $11.70). Needs a list of **$31.89** (or $32.78 with the surcharge) to pass at Standard, before a 15% sale.
- 2XL is worse: $16.44, 63.23% of $26. Needs **$36.53**.
- Economy would not save it ($13.89 / 53.42%).
- If the shop gives the tee away with free shipping, estimated net after unitCost, Standard postage, surcharge, and the 2.9%+$0.30 fee estimate is about **$10.20** (39% of list) — a profit, but not a 45% cost-ratio pass. If the customer pays the live Standard $4.95, estimated net is about **$15.00**.

`ETSY_LISTINGS.md` was right that $26 is thin if shipping is free. With real Standard postage added to `unitCost`, $26 fails even when the customer pays shipping, because the shop rule is cost+shipping versus list, not versus list+postage collected.

Case B would call S–XL acceptable (36.15%) and 2XL barely under (44.19%, only $0.21 of room). That reading is only valid if `unitCost` already includes shipping, which has not been shown.

---

## Fee-inclusive profit (partial; labeled)

Etsy published US seller fees, verified 2026-11-15: listing $0.20; transaction 6.5% of item price + shipping charged (not US sales tax); processing 3% + $0.25 on the total including shipping (tax excluded here). Sources: etsy.com/sell, etsy.com/legal/fees/, Etsy Help on payment processing. **Etsy shipping charged to the buyer is still MISSING**, so Etsy net profit is not officially scored.

Shopify fee below uses the Basic estimate 2.9% + $0.30, not a billing-page rate.

Example, one S–XL tee, Case A, US Standard, surcharge on:

- Customer pays live Standard $4.95: collected $30.95 − $9.40 − $4.95 − $0.40 − $1.20 fee ≈ **$15.00** net (57.69% of the $26 list; this is profit÷list, not the shop rule).
- Customer pays $0 shipping: collected $26.00 − $9.40 − $4.95 − $0.40 − $1.05 fee ≈ **$10.20** net (39.23% of list).

---

## Yes/no questions for Moondog88

1. **Confirm whether Shopify `unitCost` is Printify production only.** Official Case A treats it that way. If it already includes shipping, say so; several types would then be scored under Case B instead.
2. **Approve pulling or not running the 15% Cyber Week sale on live merch?** Under Case A, every type fails the approved ceilings.
3. **Approve raising list prices to the Case A minima** (tee about $32–$37, sweatshirt $51–$56, mug about $27, ornament about $48, bandana $36–$39, tank about $52), or dropping types that cannot clear 45%?
4. **Do not turn on free shipping over $49** under the current prices and Case A? Admin does not have that policy now; enabling it would give away $7–$26 of Printify postage on $49+ baskets and still fail the 45% rule.
5. **Ornament / Duplium:** US first-item shipping is $17.09 against a $16.99 list (128% cost ratio). Approve changing provider, raising the price to about $48, or unpublishing until that is fixed?
6. **Align the storefront banner and `DECISIONS.md` with live Admin rates** (Printify Standard calculated rates on merch; General profile $8 / free at $70 / Express $15)?

---

## Remaining gaps

- Labeled **Printify base / production cost** (as opposed to Shopify `unitCost`) is still MISSING from the repo and was not taken from an authenticated Printify shop. Public starting prices exist on catalog pages but were not used as official cost.
- Whether `unitCost` includes shipping is still unconfirmed.
- Printify v1 shipping API for Duplium 537/41 and Printed Mint 562/70 and 571/70 was **not reachable without auth**; those rates come from public shipping pages plus the Shopify Printify profiles, which agree with each other.
- Express tee variant IDs were not mapped to size/color (variants.json for blueprint 12 / provider 29 required auth). Express is not the live Shopify method.
- Etsy shipping profiles, listing IDs, and shipping charged to the buyer: **MISSING**.
- `SCOREBOARD.md` is still an empty template.
- Shopify Payments live rate: not read from billing (2.9%+$0.30 remains an estimate).
- Printify fulfillment-service origin addresses: location nodes on those profiles were not returned in the successful query.
- Delivery customizations and discount codes were not queried; none were needed to explain the rates already on the delivery profiles.

---

## Sources checklist

- Shopify Admin GraphQL `deliveryProfiles` for egayix-ff.myshopify.com, 2026-11-15.
- https://printify.com/shipping-rates/monster-digital/
- https://printify.com/shipping-rates/spoke-custom-products/
- https://printify.com/shipping-rates/duplium/
- https://printify.com/shipping-rates/printed-mint/
- https://printify.com/shipping-rates/ (holiday surcharge banner)
- https://help.printify.com/hc/en-us/articles/28893325248145-Holiday-Shipping-Surcharge-2026
- https://help.printify.com/hc/en-us/articles/4483626155409-What-are-Printify-s-shipping-options
- https://help.printify.com/hc/en-us/articles/4483643971473-How-are-shipping-costs-calculated-for-multiple-items
- https://api.printify.com/v1/catalog/blueprints.json
- https://api.printify.com/v1/catalog/blueprints/12/print_providers/29/shipping.json
- https://api.printify.com/v1/catalog/blueprints/49/print_providers/29/shipping.json
- https://api.printify.com/v1/catalog/blueprints/68/print_providers/1/shipping.json
- https://developers.printify.com/
