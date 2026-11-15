# Pricing memo (recommendation only)

Written Nov 15, 2026 (America/New_York) by Etsy Studio. This is a recommendation. No prices were changed in Printify, Etsy, Shopify, or any GitHub branch. No sales, search, or margin figures are invented; only lines that already appear in the source files are quoted.

## Source lines (quoted)

From `skills/dropship/ETSY_STATE.md` on `claude/blissful-allen-waez05`:

> Prices: tee $26, sweatshirt $39.99, mug $17.99, ornament $16.99.

> Dog items: Pet Bandana (blueprint 562, Printed Mint 70, $18.99, print scale 0.29 at y 0.34) and Pet Tank Top (571, Printed Mint 70, $27.99, scale 0.9 at y 0.35).

From `skills/dropship/ETSY_LISTINGS.md` on the same branch:

> Titles are under Etsy's 140-character limit. Each listing has 13 tags, none longer than 20 characters. Tee and mug prices match the reference shop; check Printify's cost plus shipping before publishing, because $26.00 leaves a thin margin if shipping is free.

Individual listing prices in that file are written as **Price:** `$26.00` (tees), `$18.00` (mugs), `$21.99` (ornaments), and `$59.99` (wall art).

From `skills/dropship/ADS_READY.md` on the same branch, in the ad-text section:

> 2. "The doodle mom gift, sorted. Six designs, from $21.99."

That ad plan is written for the Shopify FurEver Faces store as described in the same file (“Four products: Doodle Tee, Doodle Mug, Doodle Christmas Ornament, Doodle Wall Art”).

## Conflicts

1. **Ornament — the material conflict.** `$16.99` in ETSY_STATE.md vs `$21.99` in ETSY_LISTINGS.md. Difference: $5.00. TASKS.md already blocks publishing ornament copy until Moondog88 picks one price and it is checked against actual Printify cost plus shipping. Use that one price on every Santa Paws / Snow Day / Mom / Dad ornament listing (and on any ornament drafts that are later created).

2. **Mug — a one-cent conflict.** `$17.99` in ETSY_STATE.md vs `$18.00` in ETSY_LISTINGS.md. Small, but it should still be one number on every mug listing.

3. **Wall art** is priced only in ETSY_LISTINGS.md (`$59.99`). There is no wall-art price and no Printify product id in ETSY_STATE.md.

4. **Sweatshirt, pet bandana, and pet tank** are priced only in ETSY_STATE.md (`$39.99`, `$18.99`, `$27.99`). They do not appear in ETSY_LISTINGS.md.

## Recommended consistent list (do not treat as a live change)

Until Moondog88 decides otherwise, the cleanest single list, taken only from those source lines, is:

| Product | Recommended display price | Source |
|---|---|---|
| Tee | $26.00 | Both files agree (`$26` / `$26.00`) |
| Sweatshirt | $39.99 | ETSY_STATE.md only |
| Mug | $17.99 or $18.00 — pick one | Conflict; see above |
| Ornament | $16.99 or $21.99 — pick one | Conflict; see above. Do not publish until decided. |
| Pet bandana | $18.99 | ETSY_STATE.md only |
| Pet tank top | $27.99 | ETSY_STATE.md only |
| Wall art | $59.99 | ETSY_LISTINGS.md only; confirm the product actually exists |

Recommendation on the two conflicts, still not a change: treat ETSY_STATE.md as the later operational price list (it is the Nov 14 state file after the listings were drafted, and it is the only file that prices every Printify product type). That would mean mug **$17.99** and ornament **$16.99**, if cost-plus-shipping supports them. Confirm cost before locking either one. The listings file’s warning about a thin tee margin if shipping is free still applies to the $26.00 tee.

## Does the “from $21.99” ad claim hold?

No. Against the prices in the source files, $21.99 is not the lowest price.

- If ETSY_STATE.md is used, the lowest listed prices are the ornament at **$16.99** and the mug at **$17.99**. The pet bandana at **$18.99** is also under $21.99.
- If ETSY_LISTINGS.md is used, the mug at **$18.00** is still under $21.99, even if the ornament stays at $21.99.
- The ADS_READY.md line is written as Shopify ad text for “six designs, from $21.99.” Even on a four-product Shopify set of tee / mug / ornament / wall art, the mug prices in the files ($17.99 or $18.00) sit below $21.99.

Do not keep “from $21.99” in ads unless the live catalog is changed so that $21.99 is actually the lowest price. A truthful “from” line would use whichever lowest price Moondog88 locks (for example “from $16.99” if the STATE ornament price is kept, or “from $17.99” / “from $18.00” if ornaments are higher and the mug is the floor). That is a copy recommendation only; no ad account was changed.

## Open pricing questions for Moondog88

1. Ornament: $16.99 or $21.99, after checking Printify cost plus shipping?
2. Mug: $17.99 or $18.00?
3. Should ads and the Shopify “from $21.99” line be updated to the true lowest locked price?
4. Is wall art at $59.99 actually for sale (no Printify id in ETSY_STATE.md)?
