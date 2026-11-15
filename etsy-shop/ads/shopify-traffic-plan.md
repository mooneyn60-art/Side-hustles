# FurEver Faces Shopify Traffic Plan (DRAFT)

**Status:** Draft only. Do not post, publish, spend, change Shopify settings, products, themes, apps, or prices, or commit to GitHub until Moondog88 approves a specific action.

**Store audited:** FurEver Faces (`egayix-ff.myshopify.com`), Shopify Basic, USD, United States, timezone EST. Store contact email: mooneyn60@gmail.com. No custom domain; primary domain is the myshopify.com URL with SSL on.

**Audit date:** Sunday, November 15, 2026, America/New_York. All store figures below were read the same day from the live Shopify Admin connector (read-only) and from the public storefront. Metricool was also read read-only.

**Hard rules for anything that goes live:** Christmas order-by date is December 5, 2026. Do not use Meatball branding in shop material. Do not claim free shipping. Use only real data; anything not verified in this audit is marked **[CONFIRM]**.

---

## What the live store actually showed

### Traffic is not literally zero, but it is not customer traffic either

Shopify Analytics for the last 30 days (October 16–November 15, 2026):

- **43 sessions** and **41 online-store visitors** in total.
- **0 sessions** every day from October 16 through November 13.
- **35 sessions / 33 visitors on November 14** and **8 sessions / 8 visitors on November 15**.

Sales in the same window: **1 order**, **$39.99 gross**, **$48.78 total**.

That order is **#1001**, placed November 14, 2026, at 5:34 PM America/New_York, paid, fulfillment in progress, no fulfillment records yet. Line item: **Doodle Mom Era Sweatshirt**, size M / Sand, **$39.99**. The remaining **$8.79** is shipping (tax recorded as $0.00). The customer email is the same as the store contact email. Treat this as a **likely owner test order [CONFIRM]**, not as proof of paid demand.

Conclusion: the store was effectively dark until November 14, then received a burst of traffic consistent with setup and a test checkout. There is still no evidence of ongoing organic or paid customer traffic.

### Jarvis's 75 live Printify products, priced the same as Etsy: verified

| Status | Count | Notes |
| --- | --- | --- |
| ACTIVE | **75** | Matches Jarvis's live count exactly |
| ARCHIVED | 11 | Older combined listings and paused custom-portrait concepts |
| DRAFT | 1 | Doodle Wall Art canvas, tagged `needs-printify-setup` |
| **Total in Admin** | **87** | Online Store publication also reports 87 included products |

All 75 active products are vendor **FurEver Faces**. Printify is installed as a third-party fulfillment service (`Printify: Print on Demand`). Active prices match the ETSY_STATE merch ladder exactly:

| Product type | Active count | Price |
| --- | --- | --- |
| T-Shirt | 31 | $26.00 |
| Sweatshirt | 10 | $39.99 |
| Mug | 10 | $17.99 |
| Dog Bandana | 10 | $18.99 |
| Dog Tank Top | 10 | $27.99 |
| Ornament | 4 | $16.99 |

Product titles are unique design-level listings (for example Santa Paws, Snow Day, Doodle Mom Era, Sock Thief), not the older archived combined listings. Live descriptions include “Printed to order in the USA,” “Order by Dec 5 for Christmas delivery,” matching-set links where relevant, and an “Artwork created with AI tools” disclosure on the Santa Paws tee sampled in full. No Meatball branding and no free-shipping claims were found in active titles, SEO fields, or the homepage copy we crawled.

### Collections (15)

Automated collections exist and most have useful body copy (Christmas cutoff, printed in the USA, matching sets). **None have a custom SEO title or meta description** (all `seo.title` and `seo.description` are null). **None have a collection image** in Admin.

Storefront merchandising is healthier than some Admin counts suggest. The homepage shows **Christmas 12 items** and **Funny Doodle Crimes 24 items**, while Admin `productsCount` still reports Christmas 24, Funny 31, Premium Showstoppers 2, In Loving Memory 1, and For Grandparents 3. Those higher Admin counts appear to include archived or unpublished custom/premium items. Shoppers should be steered only to live collections.

**Homepage / frontpage issue:** the “Home page” collection (`frontpage`) contains only the **archived** product “Doodle Christmas Ornament” (handle `custom-pet-portrait-ornament`). The public `/collections/frontpage` page currently says **“No products found.”** The actual homepage is built from theme sections and other collections, so the store is not blank, but this collection should not stay pointed at an archived item.

Header nav on the live storefront: Shop All, Tees, Sweatshirts, Mugs, Matching Sets, Christmas. Footer currently exposes **Privacy policy only**.

### SEO, images, identifiers, and categories

Good:

- Every one of the 75 active products has a custom SEO title (`Product Name | FurEver Faces`) and a custom meta description. Descriptions include the design line, “Printed to order in the USA,” and “Order by Dec 5 for Christmas.”
- Products have multiple images (typical counts: tees/sweatshirts 13, dog tanks 18, bandanas 8, mugs/ornaments 4). Image URLs are `*_2048.jpg`, so they likely meet Google’s current and January 31, 2027 500×500 pixel minimum **[CONFIRM by checking a sample in Admin]**.
- Shopify product categories are set on all 75 active products audited.

Problems that will block or weaken Google Shopping and on-site SEO:

1. **Image alt text is empty on every active product audited** (all 75). This is a systematic gap, not a few missed images.
2. **No GTINs / barcodes** on any variant sampled. Expected for custom print-on-demand, but the Google feed must be set up as custom (`identifier_exists = false`) rather than left as missing identifiers.
3. **All 31 human T-shirts are in the wrong Shopify taxonomy category:** `Arts & Entertainment > Hobbies & Creative Arts > Collectibles > Sports Collectibles > Sports Fan Accessories > T-Shirts`. That is a sports-fan collectible path, not apparel. Sweatshirts are correctly in `Apparel & Accessories > Clothing > Clothing Tops > Sweatshirts`. Mugs, ornaments, and pet bandanas look correctly categorized. Dog tanks are the broader `Pet Apparel` node, which is acceptable but less precise **[CONFIRM whether a dog-shirt leaf exists]**.
4. **Shop description in Admin is blank.** Collection SEO fields are blank.
5. **Blog “News” exists and has 0 articles.**

### Policies, contact, and shipping (critical for Google and Meta)

Admin `shopPolicies` returned only a **Privacy policy** (last updated November 14, 2026). Public storefront checks on November 15, 2026:

- `/policies/refund-policy` — **404**
- `/policies/shipping-policy` — **404**
- `/policies/terms-of-service` — **404**
- `/policies/contact-information` — **404**
- `/pages/contact` — **200**, contact **form** only; no email, phone, or mailing address visible in the page body
- Footer link: Privacy policy only

The store ships to the United States plus Canada, Australia, and a long list of EU countries. The test order paid **$8.79 shipping** on a $39.99 sweatshirt to New York, which confirms shipping is not free. There is still no public shipping or returns policy, which is a hard requirement for Google Merchant Center and for Meta direct checkout (see citations in Section 1).

### Installed apps and sales channels

Installed apps visible in Admin: **Printify: Print on Demand**, Shopify Messaging, plus the Shopify Claude and Grok connector apps.

Sales channels / publications visible:

- **Online Store** — 87 products included (all statuses).
- **Shop** (Shopify Shop channel) — only **12** products included.
- **Point of Sale** — 0 products.
- **No Google & YouTube, Pinterest, or Facebook & Instagram channel** was visible in publications or app installations.

Printify fulfillment is connected. `inventoryManagement` and `trackingSupport` both read as false on the fulfillment service record. Tracking may still flow through the Printify app **[CONFIRM]**. Variant inventory numbers are large placeholders (typically 9,999 per variant).

### Metricool (read-only)

One brand is connected: brand id **8135499**, timezone America/New_York, owner giannaaggie224@gmail.com. First connection was November 15, 2026, evening America/New_York (Metricool records November 16, 2026, 00:35 Europe/Madrid).

Connected networks in brand settings:

- TikTok: **fureverfaces**
- YouTube: channel id **UCw98RQD81t_339LX5EJqcrg**

No Facebook, Instagram, or Pinterest account was present in `networksData`. No scheduled posts were returned for November 15–December 31, 2026. The brand is too new for useful traffic analytics.

**Flag:** that YouTube channel id was previously associated with Meatball Myths. Do not use Meatball branding on FurEver Faces shop or product material. **[CONFIRM]** whether this YouTube connection is intentional for FurEver Faces or should be disconnected.

---

## 1. Free channels first

Do these before any paid test. Several of them are prerequisites for Google and Meta, and they cost no ad spend.

### 1.1 Google Shopping / Merchant Center via Shopify’s Google & YouTube app

**Current state:** the Google & YouTube channel is not installed. Refund policy, Terms of Service, and shipping policy are missing. Contact info is only a form. Human tees are miscategorized. No GTINs. Alt text is empty. Starting a Performance Max campaign before this is fixed would waste budget and risk disapprovals.

**Setup steps (Jarvis, after Moondog88 okay; do not do this in this draft):**

1. Write and publish a **Refund / return policy** and **Terms of Service** in Shopify Admin → Settings → Policies. Also write a **Shipping policy** that states actual rates, that shipping is not free, and the **December 5, 2026** US order-by cutoff for Christmas delivery. Put refund policy and terms in the **footer menu**, which Shopify and Google both expect.
2. Put visible contact information on `/pages/contact` (the form already counts as one method; also add the store email so it is readable without submitting the form).
3. Confirm a valid payment provider is active **[CONFIRM]**.
4. In Admin, add the **Google & YouTube** sales channel. Connect a Google account and create or connect a Google Merchant Center account. The store domain `egayix-ff.myshopify.com` will be claimed automatically unless it is already claimed elsewhere **[CONFIRM no prior claim]**.
5. In the channel, automatically import shipping settings only from the **general** shipping profile, and only after US rates are accurate. Shopify warns that custom shipping profiles do not sync correctly. Start the feed with the **United States** as the target country. International shipping can wait; a December 5 US cutoff should not be promised for every destination **[CONFIRM international cutoffs before advertising them]**.
6. Sync products only after the feed fields below are clean, at least for the Christmas heroes. Then monitor Merchant Center diagnostics and fix disapprovals before any paid spend.

**Feed requirements and how our catalog actually looks:**

| Requirement | Official rule | FurEver Faces finding | What to do |
| --- | --- | --- | --- |
| Store not in private mode; payment provider | [Shopify: Google & YouTube channel requirements](https://help.shopify.com/en/manual/online-sales-channels/marketplaces/google/requirements) | Store is publicly reachable. Payment provider **[CONFIRM]**. | Confirm payments before connecting the channel. |
| Refund policy and Terms of Service in the footer | Same Shopify help page: “You need to add a Refund Policy and Terms of Service to your online store… These policies must be available in your footer menu.” | Both policy URLs are **404**. Footer has Privacy only. | Write them. No free-shipping language. Include the Dec 5 cutoff and the existing “no returns for wrong size; replace if damaged or misprinted” stance already used on the Santa Paws tee, once Moondog88 okays the wording. |
| Contact information visible | Shopify, citing Merchant Center: at least one of mailing address, phone, email, or a contact form. | Contact form exists; no email/phone/address on the page. | Keep the form; add the store email in the page body. |
| Shipping information on offers | Shopify: businesses in certain countries must include shipping cost on ads and free listings or the offer is disapproved. US is in that group. | Test order shipping was $8.79 on a $39.99 sweatshirt. No public shipping policy. Store ships to many countries. | Publish accurate US rates. Do not claim free shipping. Do not import messy multi-country rates into the US feed. |
| `google_product_category` / Shopify category | Shopify: add a Google product category or Google will auto-assign and you may hit errors. Apparel also needs age group, gender, color, and size when required. | Sweatshirts, mugs, ornaments, and bandanas look correctly categorized. **All 31 tees are under Sports Collectibles > Sports Fan Accessories > T-Shirts.** | Recategorize every human tee to an Apparel T-shirt path (not sports collectibles) before sync. Fill apparel attributes. |
| GTIN / MPN / `identifier_exists` | Google: [Identifier exists](https://support.google.com/merchants/answer/6324478) is for products that do not have a GTIN, MPN, or brand. Google explicitly lists “Custom goods or one-of-a-kind products, like custom T-shirts, art, or handmade goods,” and says to submit `identifier_exists` as `no` / `false` and leave GTIN and MPN blank when those identifiers do not exist. Shopify’s channel docs also say that if a GTIN exists it must be added, and that products without a GTIN need an MPN and brand in the channel. | **Zero barcodes/GTINs** on audited variants. SKUs are long Printify numeric IDs. Brand should be FurEver Faces. These are custom printed designs, not branded wholesale tees with manufacturer GTINs. | In the Google & YouTube app, treat them as custom products and set `identifier_exists = false`. Use brand **FurEver Faces**. Do not invent GTINs. If the Shopify app still requires an MPN, **[CONFIRM]** using the existing Printify SKU rather than fabricating numbers. Do not mark `identifier_exists` false if a real GTIN later appears. |
| Images | Shopify/Google: as of January 31, 2027, main and additional images must be at least 500×500. | Images exist and URL names suggest 2048-px assets; **alt text is blank on all 75 products.** Alt is not a Merchant Center required field, but it is required for on-site SEO and accessibility. | Confirm pixel size on a sample. Add descriptive alt text, starting with the 12 Christmas-tagged products (example: “Cream goldendoodle in a Santa hat on a unisex tee, Santa Paws, FurEver Faces”). |
| Titles and descriptions | Google free-listings guidance: keep titles, descriptions, and images descriptive and include attributes such as size or gender. | SEO titles and metas are already written and include the Dec 5 cutoff. | Keep them. Do not add free-shipping or Meatball language. |

Citations:

- [Shopify Help: Google & YouTube channel requirements](https://help.shopify.com/en/manual/online-sales-channels/marketplaces/google/requirements)
- [Google Merchant Center: Identifier exists `[identifier_exists]`](https://support.google.com/merchants/answer/6324478)
- [Google Merchant Center: Show your products for free on Google](https://support.google.com/merchants/answer/13692890) (Shopify-specific)

**Free listings timeline (honest):** For stores that create Merchant Center through the Google & YouTube app and meet eligibility, “approved products can automatically start appearing on the Shopping tab in relevant search results.” Google also says products “aren't guaranteed to show,” and “If you're new to online selling, then it might take time before your products appear in relevant search results.” There is no official same-day promise. Plan on **account verification plus product review taking several days, sometimes longer**, and treat “live in free listings” as **[CONFIRM]** only after Merchant Center shows the Christmas heroes as approved. Do not start paid ads until that happens. December 5 is only about 20 days from this audit, so this work has to start immediately after approval to have any chance of free impressions before the cutoff.

### 1.2 Pinterest app: catalog, product pins, rich pins, Verified Merchant

**Current state:** no Pinterest sales channel or app was visible in Shopify publications or app installs. Metricool has no Pinterest account connected. Moondog88 already posts Pinterest personally (see the existing posting pack).

**What to do:**

- In Shopify Admin, **[CONFIRM]** whether a current official Pinterest sales channel or catalog app is still offered. It was not installed and was not listed in the publications we could see. If it exists, install it after Moondog88 okays the connection, sync the catalog, and publish the 75 active products (or at least Christmas + best-seller sets).
- If no Shopify Pinterest channel is available, connect a **Pinterest Business** account, claim `https://egayix-ff.myshopify.com`, and add a product catalog / feed by Pinterest’s current method **[CONFIRM the 2026 setup path in Pinterest Business]**.
- Shopify product pages already have titles, descriptions, prices, and images, which is what product rich pins need. After the website is claimed, enable rich pins / product pins in Pinterest and validate a product URL **[CONFIRM in Pinterest’s current validator]**.
- **Pinterest Verified Merchant** is a Pinterest-side badge for merchants who meet Pinterest’s catalog, website, and quality requirements. It can help trust, but it is not required to post product pins, and approval is not guaranteed before December 5. Treat it as optional / later **[CONFIRM current eligibility]**.
- Organic product pins remain the fastest Pinterest lever we already have: use the drafts in `/workspace/etsy-marketing/christmas-pins.md` and `/workspace/etsy-marketing/posting-pack.md`, pointing to **Shopify product URLs** (or Etsy URLs if that is the chosen destination for a given pin). Do not claim free shipping. Do not use Meatball branding.

### 1.3 Facebook & Instagram app: catalog and shop

**Current state:** the Facebook and Instagram by Meta sales channel is not installed. Metricool has no Facebook or Instagram account connected. Store policies required for Meta checkout are missing.

**Current US eligibility and checkout status (as of this audit’s Shopify Help read):**

Shopify’s [Selling on Meta](https://help.shopify.com/en/manual/online-sales-channels/agentic-storefronts/meta) page states that customers can complete purchases through a Shopify-powered **direct checkout on Meta surfaces**. Requirements include:

- Selling to customers in a listed country, which **includes the United States**.
- Products eligible for Shopify Catalog.
- For shoppable ads, the **Facebook and Instagram by Meta** sales channel with product syncing on.
- Agreement to Shopify’s Agentic Storefronts Supplemental Terms.
- **Terms of service, Privacy policy, and Return and refund policy** completed in Settings → Policies.

“Purchasing in direct checkouts is activated by default for eligible stores,” but it is shown only to customers in the listed countries (the US is one). If direct checkout is turned off, customers can still discover products and are redirected to the online store. There are no extra Meta checkout fees beyond standard payment processing, per that page.

**This store is not eligible today**, because refund/terms policies are missing and the Meta sales channel is not installed. Eligibility at the moment Jarvis connects the app should be **[CONFIRM]** again, because Meta and Shopify have been changing shop/checkout terms.

Practical plan before December 5: install the Facebook and Instagram by Meta channel after policy work and Moondog88 okay; connect a Business portfolio, a Facebook Page, and a professional Instagram account **[CONFIRM those accounts exist and are branded FurEver Faces, not Meatball]**; sync the catalog; use shop tags and link-in-bio. Treat full US checkout-on-Meta as a bonus if the store qualifies, not as the reason to spend time here this week. Organic posting can start as soon as bios and product links are ready.

### 1.4 Shopify SEO: collections, titles, meta descriptions, alt text, and the blog question

**Already in good shape:** product SEO titles and meta descriptions on all 75 active products.

**Fix first (high leverage, still not a traffic miracle):**

- Add **alt text** to every image, starting with the 12 live Christmas products and the homepage/collection feature images.
- Write collection SEO titles and metas (they are all empty). Reuse the existing collection body copy; keep the Dec 5 cutoff on Christmas, ornaments, and under-$25.
- Recategorize the 31 tees off the sports-collectible path.
- Replace the archived ornament on the frontpage collection with a live Christmas hero (Santa Paws tee or the Santa Paws / Snow Day set).
- Hide or empty Admin collections that still describe paused custom work (**In Loving Memory**, **Premium Showstoppers**, and possibly **For Grandparents**) so they cannot be reached with promises we are not selling.
- Add a short shop description in Admin and an About page if one is needed for Google contact/about completeness **[CONFIRM]**.
- Publish only 12 products to the Shop channel so far; if Shop is intended as a discovery surface, publish the rest after review **[CONFIRM]**.

**Is a blog worth doing before December 5?** No, not for organic SEO. A new Shopify store with 43 sessions, no custom domain authority, and a blog named “News” with zero posts will not rank in time to move Christmas orders. SEO for a new domain is measured in months, not 20 days. One **gift-guide landing page** (not a blog program) can still be useful as a destination for email, Pinterest, and later Google ads — for example “Goldendoodle Christmas gift ideas, order by Dec 5.” That is a conversion page, not an SEO strategy. Do not spend the next two weeks writing blog posts.

### 1.5 Email capture: Shopify Forms pop-up, no-discount offer, short welcome flow

**Current state:** Shopify Forms is not among the installed apps we could see.

Proposal (after Moondog88 okay; Jarvis installs and configures, no discount codes that break margin or contradict Etsy rules):

- Install **Shopify Forms** and add a pop-up plus a footer embed. Do not use a percentage off, free shipping, or “cheaper than Etsy” offer.
- **Offer idea:** a free digital printable, for example a one-page “Doodle Christmas Gift Checklist” or a simple coloring page, delivered as a download. This is not a merch discount. Alternative: “early access to the Valentine drop” if the printable is not ready **[CONFIRM which asset we can actually deliver before launch]**.
- Show the pop-up after a short delay or on exit intent, not immediately, and exclude it from checkout.
- **Welcome flow (three emails, all honest):**
  1. Welcome + the download or early-access confirmation. No sale language.
  2. Two days later: two or three real best-seller or Christmas heroes with **live Shopify titles and prices**, the **December 5** order-by date, and a reminder that shipping is calculated at checkout (do not say free shipping).
  3. A few days later: invite to follow @fureverfaces on TikTok / Pinterest / Instagram once those bios point at the store. Mac-on-camera content is fine.
- Collect the list **off Etsy** (Shopify pop-up, social bios, videos). Do not use Etsy messages, listings, or packaging to bribe Etsy buyers onto this list with a Shopify coupon (see 1.6).

### 1.6 Cross-promo from Etsy: current rules, Printify inserts, and allowed alternatives

#### Etsy rules (current as of this audit)

We could not retrieve the full HTML of Etsy’s legal policy page in this audit (the official URL returns a JS wall / timed out on fetch). Jarvis or Moondog88 should re-open the official page before anything is added to listings, messages, or packaging:

- Official policy: [Off-Platform Transactions Policy](https://www.etsy.com/legal/policy/off-platform-transactions-policy/1254654515806) (Etsy House Rules / Seller Policy set). Prior official-page indexing in this project recorded a last-updated date of **October 5, 2026 [CONFIRM on the live page]**.

Indexed language from that official policy page, to be confirmed on the live document, prohibits instructing members to pay or purchase off Etsy, including through “a personal website, social media shop, or another online marketplace”; sharing off-platform contact details to complete a transaction; offering incentives such as discounts, free items, or cheaper shipping to shop off Etsy; and using QR codes to direct members off Etsy.

Etsy Help pages that **were** fetched in full on November 15, 2026:

From [How to Protect Yourself from Off-Platform Transaction Scams](https://help.etsy.com/hc/en-us/articles/43587499349399-How-to-Protect-Yourself-from-Off-Platform-Transaction-Scams):

> “We don't allow sellers to use QR codes to direct buyers off Etsy. If you see a QR code in any Etsy surface including in a listing, Convo, or shop UI that asks you to scan it to complete a purchase off platform or get a deal, don't scan it.”

> “Sellers are allowed to share links to their own websites and social media. But if you click a link and leave Etsy, you're no longer covered by our purchase protections. Always make sure you're completing your purchase on Etsy before entering any payment information.”

> “The only ways to pay for an Etsy order are through Etsy checkout or through our approved Square integration for in-person purchases.”

From [How to Edit Your Shop’s About Section](https://help.etsy.com/hc/en-us/articles/115015628487-How-to-Edit-Your-Shop-s-About-Section):

> “Links: Share places buyers can get the latest news from your shop, such as a website, blog, or social media profile.”

**Plain reading for FurEver Faces:**

- **Do not**, in Etsy listings, Etsy Messages, shop announcements, packaging, or inserts that go out with Etsy orders, tell buyers to purchase the same item on Shopify, offer a Shopify discount, cheaper shipping, a free item, or a QR code that sends them to Shopify to buy or “get a deal.”
- A website or social link in the **About / shop basics Links** field is something Etsy Help explicitly allows. That is not a license to use the About page, listing text, or a Convo to complete or incentivize an off-Etsy sale. Keep any About link factual (brand + social), not a “buy it cheaper on our website” pitch.
- If we cannot confirm the live legal policy text at the moment of posting, default to the stricter reading: **no off-Etsy purchase instructions and no off-Etsy purchase incentives anywhere on Etsy surfaces or in Etsy-origin packaging.**

#### Printify packaging inserts and packing slips

Printify **does** support official **packaging inserts**, but they are not universal, and they are not a custom packing-slip designer.

From [What are packaging inserts?](https://help.printify.com/hc/en-us/articles/15939864611345-What-are-packaging-inserts):

> “Packaging inserts are customizable cards added to eligible orders to help you connect with customers and promote your brand. You can use them to share a short message, encourage reviews, offer discounts, or highlight your social channels.”

Common uses listed there include a branded thank-you, a discount code, a QR code linking to reviews, and social media links. Pricing is **$0.15** (Premium) or **$0.25** (Free plan) per insert. Specs: 6×4 inches, 170 gsm, **single-sided**. “Inserts are not available for Express Delivery orders. Orders with inserts are routed only to Print Providers that support them.” “Printify currently supports one active insert design at a time.”

Supported products are **not** a blanket yes for tees, bandanas, ornaments, mugs, or sweatshirts. Printify’s own rule is:

> “You can find supported products by applying the Inserts filter in the Printify Catalog. Products that support branded inserts will display a ‘Branded inserts’ badge next to the Print Provider option on the product page.”

Until someone checks that badge for the actual providers on this catalog, support is **[CONFIRM]** for Monster Digital (tees/sweatshirts), SPOKE (mugs), Duplium (ornaments), and Printed Mint (bandanas/tanks), if those are still the assigned providers.

From [Can I insert additional items into the package?](https://help.printify.com/hc/en-us/articles/4483630325009-Can-I-insert-additional-items-into-the-package):

> “Unfortunately, we do not offer the service of including additional items in the package. However, you have the option to set up packaging inserts for your store, which can help showcase your brand identity.”

So we **cannot** slip our own printed cards, stickers, or flyers into Printify shipments except through Printify’s insert feature (and only when the provider supports it).

From [How are the products packaged?](https://help.printify.com/hc/en-us/articles/4483601818385-How-are-the-products-packaged), packing-slip / label branding is limited:

> “The shipping label specifies your store name and the return address. It is possible to set up a custom return address for your orders.”

> “Printify’s name does not appear anywhere on the package or the shipping label.”

> “Please note that the Print Providers listed below don’t support custom shipping labels, which means that your store name will not be displayed on the shipping label (instead, it will say ‘Fulfillment Center’, ‘Shipping Department’, or ‘Store’, for example).”

**Printed Mint is on that do-not-support-custom-labels list.** If bandanas and tanks still ship from Printed Mint, those packages will not show the FurEver Faces store name on the label **[CONFIRM current providers]**. We found no official Printify Help article that offers a fully custom branded packing-slip design (logo, marketing copy, Shopify URL). Do not plan on a custom packing slip.

**Do not enable a Shopify-directing insert on Etsy-origin orders.** A thank-you card with a Shopify URL, QR code, or “15% off at our website” in an Etsy shipment would conflict with Etsy’s off-platform rules cited above. If inserts are used at all before December 5, use them only on the **Shopify Printify store** (if it is a separate Printify store), and keep the copy to thank-you + social handles — no “buy on Etsy instead,” and no off-platform coupon language that would be unsafe if the same design were ever applied to Etsy orders. Because Printify allows only one active insert design at a time, a single shared Printify store is a real risk **[CONFIRM whether Etsy and Shopify use separate Printify stores]**.

#### Allowed alternatives

Safe places to send people to Shopify (or to a link-in-bio that includes Shopify):

- TikTok, Instagram, Pinterest, YouTube, and Facebook **profile bios** and link-in-bio tools (Metricool already has TikTok @fureverfaces).
- Organic posts and Social Studio videos that are not on Etsy surfaces.
- The Shopify email pop-up and welcome flow.
- An Etsy About **website / social link**, without purchase incentives or “complete this order on our site” language.

Do not rely on Etsy listing descriptions, Conversations, packing slips, or Etsy-origin inserts to grow Shopify traffic.

---

## 2. One small paid test (recommendation only)

**Recommendation only. Do not spend until Moondog88 approves this exact test, and do not start it until Merchant Center has approved the Christmas products.**

**Channel:** Google Ads **Performance Max** with the Merchant Center product feed (Shopping), United States only.

**Why this channel, not Pinterest ads:** the catalog is product-heavy and keyword-intent is clear (“goldendoodle Christmas shirt,” “doodle mom sweatshirt,” “funny dog bandana”). Google free listings plus a small PMax test can use the same cleaned feed. The store has no Pinterest or Meta ads account connected in Metricool, and Pinterest intent is usually colder. PMax is still a recommendation, not a guarantee; new accounts can spend inefficiently, which is why the cap and stop rules are tight.

**When to start:** the first morning after Christmas hero products show as **approved** in Merchant Center, and not before refund, terms, and shipping policies are live in the footer. If that approval has not happened by **Friday, November 27, 2026, America/New_York**, **skip paid spend for this Christmas** and stay on free listings plus organic social. A late start still burns money after the practical order window.

**Dates:** start on approval (target window November 24–December 4 if the feed is ready); **hard end 11:59 PM America/New_York on December 4, 2026**. Do not run ads on December 5 or after. Buyers need time to complete checkout on the cutoff day.

**Budget:** **$5 per day**. **Total cap: $50** (or $5 × remaining days through December 4, whichever is lower). This is the same “small test, hard cap” shape as the $3/day Etsy ads tests, sized slightly higher because Shopping CPCs on apparel are often higher.

**Geo and assets:** United States only. Asset group built from live Christmas products only (titles and prices in Section 3). No free-shipping claims. No Meatball creative. Mention the December 5 order-by date in assets where character limits allow.

**Success metric:** at least **one paid Shopify order** attributed to the campaign with contribution after product cost, shipping, and fees still inside the 45% cost ceiling **[CONFIRM live Printify costs before launch]**. Secondary learning metrics (not success by themselves): click-through rate, add-to-carts, and Merchant Center approval remaining clean.

**Stop rules:**

- Pause immediately if Merchant Center or Google Ads disapproves the account or the Christmas products.
- Pause if **$25 is spent with zero add-to-carts**.
- Pause if the first conversion’s cost would exceed the 45% cost ceiling / leave no contribution **[CONFIRM]**.
- Pause at the $50 cap even if results are good; extending spend is a separate Moondog88 decision.
- Pause at the December 4 end date regardless of results.

This is not approval to launch. It is a written recommendation for Moondog88 to accept, change, or reject.

---

## 3. Video plugs for Social Studio

Social Studio owns the videos. We only supply product facts and hook lines. Feature **Mac** on camera where it fits. Use shop tags or link-in-bio to the Shopify product URL (`https://egayix-ff.myshopify.com/products/{handle}`). Do not say free shipping. Do not use Meatball branding. Say “order by December 5 for Christmas delivery” when the video will still be in market before that date.

Priority plugs, all prices taken from live Shopify:

| Product (live Shopify title) | Price | Handle | Hook / plug angle |
| --- | --- | --- | --- |
| Santa Paws Goldendoodle Christmas T-Shirt | $26.00 | `santa-paws-goldendoodle-christmas-t-shirt` | Mac in a Santa hat, then the tee: “Nice list (pending).” Best single Christmas hook. |
| Santa Paws Goldendoodle Christmas Sweatshirt | $39.99 | `santa-paws-goldendoodle-christmas-sweatshirt` | Same art, colder-weather version. “The December dog-walk uniform.” |
| Santa Paws Goldendoodle Christmas Mug | $17.99 | `santa-paws-goldendoodle-christmas-mug` | Coffee-with-Mac, stocking-stuffer price, under $25. |
| Santa Paws Goldendoodle Christmas Ornament | $16.99 | `santa-paws-goldendoodle-christmas-ornament` | Hang it on a tree next to Mac. Lowest-price Christmas keepsake. |
| Santa's Favorite Dog Bandana | $18.99 | `santas-favorite-dog-bandana` | Put the bandana on Mac. “Nice list. Mostly.” |
| Santa's Favorite Dog Tank Top | $27.99 | `santas-favorite-dog-tank-top` | Matching set with the bandana and the Santa Paws human tee. |
| Snow Day Goldendoodle Winter T-Shirt | $26.00 | `snow-day-goldendoodle-winter-t-shirt` | “Zoomies incoming.” Snow / beanie / scarf art. |
| Snow Day Goldendoodle Winter Sweatshirt | $39.99 | `snow-day-goldendoodle-winter-sweatshirt` | Same hook, warmer garment. |
| Snow Day Goldendoodle Coffee Mug | $17.99 | `snow-day-goldendoodle-coffee-mug` | Under $25 companion to the Snow Day tee. |
| Snow Day Goldendoodle Christmas Ornament | $16.99 | `snow-day-goldendoodle-christmas-ornament` | Second tree ornament if Santa Paws is already used. |
| Doodle Mom Christmas Ornament | $16.99 | `doodle-mom-christmas-ornament` | Gift-for-her / mom hook. No custom-photo claims. |
| Doodle Dad Christmas Ornament | $16.99 | `doodle-dad-christmas-ornament` | Gift-for-him / dad hook. |
| Doodle Mom Era Sweatshirt | $39.99 | `doodle-mom-era-sweatshirt` | Everyday (non-Santa) bestseller energy; this is the garment on the shop’s first paid test checkout. |
| Doodle Mom Era T-Shirt | $26.00 | `doodle-mom-era-t-shirt` | Lighter-price version of the same line. |
| Bed Hog Goldendoodle T-Shirt + Bed Hog Dog Bandana | $26.00 and $18.99 | `bed-hog-goldendoodle-t-shirt`, `bed-hog-dog-bandana` | Matching-set comedy: Mac hogging the bed, then the bandana on Mac. |
| Alleged Sock Thief Dog Bandana + Sock Thief Goldendoodle T-Shirt | $18.99 and $26.00 | `alleged-sock-thief-dog-bandana`, `sock-thief-goldendoodle-t-shirt` | “Wanted in 3 laundry rooms” / “No comment.” |

Suggested 10-second tag line for creators (they can rewrite): “This is the Santa Paws tee — $26, printed to order in the USA, order by December 5 for Christmas. Shop link in bio.”

---

## 4. Ranked first three actions

| Rank | Action | Owner | Needs Moondog88 okay? |
| --- | --- | --- | --- |
| **1** | Publish a refund/return policy, terms of service, and shipping policy (no free-shipping claims; state the Dec 5, 2026 US cutoff and real shipping). Add refund + terms to the footer. Put the store email on the Contact page. Replace the archived ornament on the frontpage collection with a live Christmas hero. Hide or empty In Loving Memory / Premium collections that still describe paused custom products. | **Jarvis** (Shopify Admin). Claude / our team can draft policy text for review. | **Yes** — Moondog88 must okay policy wording before it is published. |
| **2** | After policies are live: install the Google & YouTube channel, connect Merchant Center, set custom-product / `identifier_exists = false`, brand FurEver Faces, recategorize all 31 human tees off Sports Collectibles, add apparel attributes, and add alt text at least on the 12 Christmas products. Do not start the paid test until those products are approved. | **Jarvis** (Shopify Admin and Google account connection). Our team can supply alt-text and category lists. | **Yes** — connecting a Google account and creating Merchant Center needs Moondog88’s okay. Paid spend is a separate okay on Section 2. |
| **3** | Point TikTok @fureverfaces (and Pinterest / Instagram / Facebook bios, once those accounts are confirmed) at the Shopify store or a link-in-bio that includes it. Moondog88 posts from the existing posting pack and shop-tags or links the products in Section 3. Social Studio uses the plugs above. Do not promote Shopify as a purchase path on Etsy listings, messages, or packaging. | **Moondog88 posting.** Our team supplies the product list, hooks, and pin/post copy already drafted. Social Studio owns the videos. | **Posting to existing social accounts:** Moondog88 is already the poster; no spend required. **Yes** if a new link-in-bio tool, a new account, or a Printify insert is involved. **Confirm** the YouTube connection is not Meatball-branded before any FurEver Faces video goes there. |

---

## [CONFIRM] checklist

- Payment provider on the Shopify store is active and ready for Merchant Center.
- Live Printify unit costs and shipping for the 45% cost ceiling, before any paid test.
- Whether Etsy and Shopify use separate Printify stores (this decides if a Shopify-only insert is safe).
- Insert and custom-label support for the actual current providers, especially Printed Mint (no custom shipping labels, per Printify Help).
- Official Off-Platform Transactions Policy text on the live Etsy legal page (last-updated date and exact wording) before any Etsy About link is added.
- Whether the Metricool YouTube channel `UCw98RQD81t_339LX5EJqcrg` should stay connected to this brand.
- Whether Facebook, Instagram, and Pinterest business accounts already exist under FurEver Faces.
- Whether a current official Pinterest sales channel still appears in the Shopify Admin channel list.
- International Christmas cutoffs, if anything outside the US will be advertised.
- Image pixel dimensions on a sample of live mockups.
- Frontpage theme sections: confirm no leftover free-shipping banner (none was visible in the November 15 storefront crawl).
- Order #1001 is an owner test and can be ignored as demand signal.

---

*End of draft. No Shopify, Metricool, Etsy, or GitHub changes were made while preparing this plan.*
