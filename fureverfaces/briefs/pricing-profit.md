# Pricing & Profit — Expert Brief (FurEver Faces)
Updated: 2026-11-16

## Role (2 lines)
Pricing & Profit for FurEver Faces on Etsy, Shopify, and the parked TikTok Shop.
I recommend prices only; Moondog88 approves every change.

## Current state (our shop data, 5 bullets max, with numbers + source file)
- All six live types fail the 45% cost+ship rule under Case A (`unitCost` + Printify US Standard first-item): tee S–XL 55.19% ($14.35 vs a $11.70 cap), tee 2XL 63.23%, sweatshirt S–XL 57.84% / 2XL 63.17%, mug 67.26%, ornament **128.13%**, bandana 85.47% / 92.47%, tank 83.21%. Source: `/workspace/etsy-pricing/margins.md` (2026-11-15) and `/workspace/research/furever/03-printify-margins.md` (2026-11-16).
- Live lists: tee $26, sweatshirt $39.99, mug $17.99, ornament $16.99, bandana $18.99, tank $27.99. `unitCost`: tee $9.40 / $11.49 2XL, sweatshirt $14.34 / $16.47 2XL, mug $4.81, ornament $4.68, bandana $10.54 / $11.87, tank $17.30. Source: Shopify Admin inventory + `/workspace/etsy-pricing/margins.md`.
- Duplium ornaments ship from Ontario, Canada; US Standard first-item is **$17.09**. Several US-side ceramic blanks publish **$5.89 / $0.69**. If Etsy buyer shipping is $0, the current ornament loses **$7.24** before ads; bandanas and tanks are near zero or negative once Offsite Ads apply. Source: `/workspace/research/furever/03-printify-margins.md`; [Duplium shipping](https://printify.com/shipping-rates/duplium/).
- Shopify $49 free / $5.99 is **not** configured. The only free-shipping threshold found is **$70** on the General profile (leftover variants); merch sits on Printify Standard profiles. Source: Shopify `deliveryProfiles`, `/workspace/etsy-pricing/margins.md`.
- Etsy buyer shipping, observed AOV, weekly profit, and whether `unitCost` is Free or Premium / production-only or already includes shipping are **MISSING**. Source: `/workspace/research/furever/03-printify-margins.md`, Remaining gaps.

## Top 5 rules (2026 best practice in this field, each with a source URL)
1. **Etsy US fees:** $0.20 per listing or auto-renewal, a **6.5%** transaction fee on item + shipping (not US sales tax), and US payment processing of **3% + $0.25**. Sources: [Etsy Fees & Payments Policy](https://www.etsy.com/legal/fees/), [payment processing help](https://help.etsy.com/hc/en-us/articles/115015628847-What-are-Payment-Processing-Fees-for-Selling-on-Etsy) (retrieved 2026-11-16).
2. **Offsite Ads:** **15%** of attributed order value (before the ad fee), or **12%** once the shop has made $10,000 in any consecutive 365-day period; shops under $10k may opt out. Source: [How Etsy's Offsite Ads Work](https://help.etsy.com/hc/en-us/articles/360000338367-How-Etsy-s-Offsite-Ads-Work) (retrieved 2026-11-16).
3. **Printify Premium vs Free:** Premium is up to **20% off most catalog production** (up to 33% on select new products) and **does not discount shipping**; it is $39/month or $299/year. Confirm whether current `unitCost` already reflects a Premium price before buying the plan. Source: [Printify Pricing](https://printify.com/pricing/) (retrieved 2026-11-16).
4. **Shipping and the holiday surcharge:** Price from real Printify first- and additional-item US rates, not a flat estimate. A **$0.40 per-order** US-destination surcharge applies **October 15, 2026–January 17, 2027** (per order, not per parcel; not in the catalog tables). Sources: [Printify shipping rates](https://printify.com/shipping-rates/), [Holiday Shipping Surcharge 2026](https://help.printify.com/hc/en-us/articles/28893325248145-Holiday-Shipping-Surcharge-2026).
5. **45% cost+ship rule:** Supplier cost + shipping must be **≤ 45% of price** (shop rule G6; this is a cost-ratio, not profit ÷ price ≥ 45%). Official scoring uses list price as the denominator and Case A (`unitCost` + Standard first-item). **Open question:** whether buyer-paid shipping belongs in that denominator. Source and application: `/workspace/etsy-pricing/margins.md` and `/workspace/research/furever/03-printify-margins.md` (internal shop rule; no public third-party URL).

## KPIs I own (metric, current value, target by Dec 31)
Targets below are recommendations only until Moondog88 approves.

| KPI | Definition | Current value | Target by Dec 31, 2026 | Data source |
|---|---|---|---|---|
| Margin per order | Amount collected from the buyer minus `unitCost`, Printify shipping, the $0.40 surcharge when in effect, and Etsy fees (plus Offsite Ads when attributed). Tax excluded. | No shop-wide average (order feed **MISSING**). Modeled Case A examples (2026-11-16): tee S–XL **$12.81** if shipping is passed through and there are no ads, or **$8.33** if buyer shipping is $0; Duplium ornament **−$7.24** if buyer shipping is $0. | Every live SKU cash-positive even if buyer shipping is $0 and a 15% Offsite Ad applies. | `/workspace/research/furever/03-printify-margins.md` (modeled). Live average: **MISSING**. |
| AOV | Average amount collected per order (item + buyer shipping, tax excluded). | **MISSING** | Start weekly tracking from Shopify and Etsy; no dollar target until a baseline is read. | Sales reports / `SCOREBOARD.md` (empty). |
| Profit per week | Sum of order-level margins in the week. | **MISSING** | Start weekly tracking; no dollar target until a baseline is read. | Same as AOV. |
| Cost+ship % per SKU | (`unitCost` + Printify US Standard first-item) ÷ list price. Official PASS is ≤ 45%. | Case A (2026-11-15/16): tee 55.19% / 63.23%, sweatshirt 57.84% / 63.17%, mug 67.26%, ornament 128.13%, bandana 85.47% / 92.47%, tank 83.21%. All **FAIL**. | **≤ 45%** on every live SKU, via approved price, provider, or unpublish decisions. | `/workspace/etsy-pricing/margins.md`, `/workspace/research/furever/03-printify-margins.md`. |

## Hard limits
- No spending, price changes, publishing new content without Moondog88's keep/toss, or messages to customers/outsiders without Moondog88's OK.
- No "AI" in ad or listing copy (TikTok's AI-generated toggle stays on for AI visuals). Dog is never named: "This doodle".
- No tokens/secrets in GitHub. Never touch Claude's branches.

## Open gaps
- Etsy buyer shipping for this shop is **MISSING**, so every Etsy cash margin is a labeled scenario, not a live setting.
- `unitCost` composition (Free vs Premium; production-only vs production + shipping) is **unconfirmed**.
- Observed AOV, weekly profit, conversion, order counts, Shopify Payments live rate, and Offsite Ads enrollment / trailing-12-month sales are **MISSING**.
- Official per-provider Free/Premium bases for several alternative blanks (US ornaments, totes, blankets, phone cases) are **MISSING** or only third-party; those products should not be priced until a Printify catalog price is confirmed.
