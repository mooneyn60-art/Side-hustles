# Pricing memo (recommendation only)

Written Nov 15, 2026 (America/New_York) by Etsy Studio; updated the same day in round 2. This is a recommendation. No prices were changed in Printify, Etsy, Shopify, or any GitHub branch. Draft copy only. No sales, search, or estimated cost figures are used; only lines that already appear in the source files are quoted, and missing Printify costs are marked “Printify cost needed,” never estimated.

## Prices and shop name for this draft (not a live change)

- Customer-facing shop name: FurEver Faces.
- `skills/dropship/ETSY_STATE.md` on `claude/blissful-allen-waez05` is the live price list: ornament **$16.99** (pending a margin check) and mug **$17.99**.
- Ads would say **“from $16.99”**.
- Shop name FurEver Faces and ornament $16.99 are resolved. See DECISIONS.md. A margin check is still needed.

## The 45% rule (quoted)

From `skills/dropship/BRIEF.md` on `mooneyn60-art/skills`, branch `claude/package-installation-setup-yv4j79`, under “Stop-ship problems found on 11/14”, item 5:

> Margins: check each price against the supplier's cost plus shipping. The ornament ($21.99) and socks ($19.99) are likely thin once shipping is paid. Rule: the supplier cost plus shipping should be ≤ 45% of the price, so ads have room. The blanket ($94.99, tagged free shipping) needs its shipping cost confirmed.

The rule applied below is that quoted sentence: **the supplier cost plus shipping should be ≤ 45% of the price**. The ornament figure in that same paragraph is $21.99, which is the older ETSY_LISTINGS.md / BRIEF.md number, not the live-list $16.99. Socks and the $94.99 blanket are in that brief for the personalized Shopify store; they are not in the cartoon ETSY_STATE.md catalog. Those product mentions are quoted only to keep the rule in context. No costs were taken from that qualitative “likely thin” line.

## Live price list (from ETSY_STATE.md)

Quoted from `skills/dropship/ETSY_STATE.md`:

> Prices: tee $26, sweatshirt $39.99, mug $17.99, ornament $16.99.

> Dog items: Pet Bandana (blueprint 562, Printed Mint 70, $18.99, print scale 0.29 at y 0.34) and Pet Tank Top (571, Printed Mint 70, $27.99, scale 0.9 at y 0.35).

Wall art at `$59.99` appears only in `skills/dropship/ETSY_LISTINGS.md` and has no Printify id in ETSY_STATE.md, so it is backlog, not on the live list. ETSY_LISTINGS.md still lists mug `$18.00` and ornament `$21.99`; those are not used as live prices in this memo.

## Max allowed cost plus shipping at each live price

Computed as 45% of the live price. Exact values are shown (not rounded away). Compare each cap to an actual Printify cost-plus-shipping figure only if one is in the source files.

| Product | Live price (ETSY_STATE.md) | Max cost + shipping (45% of price) | Printify cost + shipping in sources | Result |
|---|---|---|---|---|
| Tee | $26.00 | $11.70 | Not found | **Printify cost needed** |
| Sweatshirt | $39.99 | $17.9955 | Not found | **Printify cost needed** |
| Mug | $17.99 | $8.0955 | Not found | **Printify cost needed** |
| Ornament | $16.99 | $7.6455 | Not found | **Printify cost needed** (this is the pending margin check) |
| Pet bandana | $18.99 | $8.5455 | Not found | **Printify cost needed** |
| Pet tank top | $27.99 | $12.5955 | Not found | **Printify cost needed** |
| Santa Paws hero bundle (tee + bandana + ornament) | $61.98 | $27.891 | Not found (no item costs, and no bundle cost) | **Printify cost needed** |

No margin pass or fail can be scored. There is no Printify unit cost, no shipping cost, and no cost-plus-shipping total for any of these product types in ETSY_STATE.md, ETSY_LISTINGS.md, ADS_READY.md, ORDER_RUNBOOK.md, BRIEF.md, HANDOFF.md, or the Side-hustles TASKS.md / holiday marketing plan. Qualitative warnings exist and are quoted below; they are not costs.

Related source lines, still not costs:

- ETSY_LISTINGS.md: “Tee and mug prices match the reference shop; check Printify's cost plus shipping before publishing, because $26.00 leaves a thin margin if shipping is free.”
- Holiday marketing plan on Side-hustles main: “recalculate margin against Printify cost + Etsy fees + shipping.” No numbers are given.
- BRIEF.md, quoted above, calls the $21.99 ornament and $19.99 socks “likely thin once shipping is paid.” That ornament price is not the live $16.99 figure, and a lower retail price makes the 45% cap tighter ($7.6455 at $16.99 vs $9.8955 at $21.99), so the pending check matters more, not less. Still not a measured cost.

## The $61.98 hero bundle

$61.98 is the sum of the live list prices: $26 + $18.99 + $16.99. That addition is already written in TASKS.md and in `etsy-shop/ads/holiday-marketing-plan.md` on Side-hustles main (“Tee + bandana + ornament | $26 + $18.99 + $16.99 = **$61.98**”). No bundle discount is in the files. The holiday plan also says: “Any bundle SKU or bundle discount (none documented).”

Against the 45% rule, supplier cost plus shipping for the three items together must be ≤ **$27.891**. Because no Printify costs or shipping figures are in the sources, the bundle is also **Printify cost needed**. It cannot be marked as passing or failing the rule.

The listing copy in `01-christmas-push.md` is a bundle-copy draft only. Fulfillment is not documented: there is no Printify bundle product and no Etsy bundle listing id in the source files. If it were offered, it would have to ship as the three existing Santa Paws Printify products (tee, pet bandana, ornament) on one customer order, or an equivalent shop-side workflow. The $49 free-shipping threshold mentioned with this bundle in TASKS.md and the holiday plan is marked **[CONFIRM]** and is not treated as a live policy here.

## Does “from $16.99” hold against the live list?

Yes, against the ETSY_STATE.md live list used in this round. The lowest live price is the ornament at **$16.99**. The next live prices are the mug at $17.99 and the pet bandana at $18.99, then the tee at $26.00. Wall art at $59.99 is not on that live list. The older ad line in ADS_READY.md (“Six designs, from $21.99.”) does not hold against this live list and should not be reused.

This is a copy recommendation only. No ad account was changed.

## Printables (for reference; not in the 45% merch rule)

The 45% rule in BRIEF.md is about supplier cost plus shipping on physical print-on-demand items. The six finished printables are digital downloads. Their source prices, unchanged, are: Christmas word search $3.99; Christmas bingo $3.49; Christmas would-you-rather $2.99; large-print seniors word search $4.99; Thanksgiving bingo $3.49; Thanksgiving word search $3.49. Those figures are from each product's `listing.md` / `listing.json` on `claude/youtube-monetization-strategy-m9vz6i`. The Christmas word search $3.99 is also in `skills/etsy-factory/research/demand.md`, as quoted in the notebook rewrite.

## Conflicts with DECISIONS.md / TASKS.md

Shop name and ornament price are resolved in `DECISIONS.md`.

Conflicts and tensions with this draft:

1. **Shop name is resolved: FurEver Faces.** See DECISIONS.md. It was not published yet, and the Etsy shop name recorded in ETSY_STATE.md remains PrintanPress (shop id 38484468) until Claude renames it. The rename is approved.
2. **Ornament price is resolved: $16.99.** See DECISIONS.md. ETSY_LISTINGS.md still lists $21.99; that conflict is closed. A margin check is still needed, and Printify cost is still needed. That check does not reopen the price.
3. **BRIEF.md vs the live list and the Dec 5 cutoff.** BRIEF.md prices the ornament at $21.99 and talks about a last safe US order date “around Dec 8-12” and a “Order by Dec 10” example. The merch listings and ADS_READY.md use Dec 5. BRIEF.md is also written for the personalized Shopify store (photo upload, memorial ornament, socks, blanket), which is a different line than the cartoon catalog in ETSY_STATE.md. The 45% rule is still the rule this assignment asked to apply.
4. **New TASKS.md decisions that do not change these prices but are still open:** (3) Shopify “no photo upload” / ADS_READY.md vs the custom-art ORDER_RUNBOOK.md flow; (4) whether ETSY_STATE.md (shop, store, product, and Make.com ids) should leave the public repo. This memo does not resolve those.
5. **$49 free-shipping threshold** in TASKS.md and the holiday plan is **[CONFIRM]**, not a documented live policy. Bundle copy must not claim free shipping until that is confirmed.

## Recommendation (still not a live change)

Keep the live ETSY_STATE.md list as the consistent merch price list in draft copy: tee $26.00, sweatshirt $39.99, mug $17.99, ornament $16.99, pet bandana $18.99, pet tank $27.99. Use “from $16.99” in ads only after the ornament margin check: pull actual Printify cost plus shipping for every type (and for the three-item bundle), and confirm each is ≤ the 45% cap above. If the ornament fails that check at $16.99, do not advertise “from $16.99” and do not treat $16.99 as locked. The 20 no-id drafts, including wall art at $59.99, stay in backlog until the products exist and have costs.
