# Decisions log (Etsy Studio)

## 2026-11-15

### 1. Customer-facing shop name: FurEver Faces
Decided by Moondog88. Use "FurEver Faces" on every customer-facing surface: listing copy, images, covers, ads and Shopify. Keep "For people owned by a doodle" as the hero line, and use "The Doodle Shop" as a secondary tag only. Renaming the Etsy shop from PrintanPress is a live change, so it waits for Moondog88's okay before Claude does it.

### 2. Live price list: ETSY_STATE.md is the source of truth
Chosen by Etsy Studio. ETSY_STATE.md (skills/dropship, branch claude/blissful-allen-waez05) is the state file that matches the Printify products that actually exist. ETSY_LISTINGS.md and ADS_READY.md are copy templates. The reference prices are tee $26, sweatshirt $39.99, mug $17.99, ornament $16.99, bandana $18.99 and tank $27.99.
- Ornament: keep $16.99 as the record. Claude should check Printify base cost plus shipping and Etsy fees. If margin is thin, propose $19.99 to Moondog88 instead of jumping to $21.99.
- All copy, ads and the "from $X" line must use these numbers. "From $21.99" is wrong, and the honest line is "from $16.99".
- No live price changes without Moondog88's okay.

### 3. Free shipping: $49 on Shopify stays
Chosen by Etsy Studio. The Shopify policy (fureverfaces/policies.md) already sets free shipping at $49+ and $5.99 otherwise, so we keep it. Bundles are built to clear it: tee + bandana + ornament $61.98 (hero), tee + tank $53.99, sweatshirt + bandana $58.98. Tee + bandana alone is $44.99, which does NOT qualify, so it must not be marketed as free shipping.
- Etsy shipping is set separately in Etsy. Any change there, including a free-shipping threshold, is a pricing change and needs Moondog88's okay.

### 4. Custom photo art: paused, ready-made only for Christmas
Chosen by Etsy Studio. The shop stays on ready-made cartoon merch and the Shopify "no photo upload" setting stays as it is. Payments, a test order and the proof-email step are all untested. Selling custom work we can't reliably deliver before the Dec 5 cutoff risks bad reviews in our first season.
- Remove or soften custom-art promises in the Shopify policies so they match. The proof-first workflow stays in ORDER_RUNBOOK for later.
- Relaunch plan: once Claude passes one full end-to-end test (photo in, proof sent, Printify order placed), launch the personalized Rookie Card and "The Good Boy" tarot as a separate "Your dog, your art" collection. Lead with the digital PDF version after Dec 5, then the printed versions for Valentine's.

### 5. Etsy Ads: small capped test, not on yet
Chosen by Etsy Studio. This needs Moondog88's okay before anything turns on.
- Proposed: $3/day (about $30 over 10 days) on 5 hero listings only: Santa Paws ornament, Santa Paws tee, Doodle Mom tee, Doodle Dad tee and the large-print Christmas word search.
- Start only after those listings have the new titles and tags and real-photo thumbnails, since ads on weak listings waste money.
- Review after 7-10 days on views, clicks, orders and spend per order. Pause physical items at the Dec 5 cutoff, and keep the printable running through Christmas.
- No Pinterest or Facebook paid spend for now. Organic only, per etsy-shop/ads/holiday-marketing-plan.md.
