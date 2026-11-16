# Etsy: Listings & SEO — Expert Brief (FurEver Faces)
Updated: 2026-11-16
## Role (2 lines)
I own every FurEverFacesDoodles listing's titles, 13 tags, descriptions, attributes, photo order and price positioning, and the search performance that comes from them.
I never publish new listings or change prices (or shipping or ads) without Moondog88's OK. Research is read-only, and every number below links to its source.

## Current state (our shop data, 5 bullets max, with numbers + source file)
- **Shop and sales:** the shop is https://www.etsy.com/shop/FurEverFacesDoodles, renamed from PrintanPress. It has 75 active listings (31 tees, 10 mugs, 10 sweatshirts, 10 bandanas, 10 dog tanks, 4 ornaments) and 0 sales per Shop Manager. Listing list: `/workspace/shopify/etsy-listings.csv`.
- **SEO rewrite log:** `/workspace/shopify/etsy-seo-changes-1116.csv` had 84 change rows covering 53 unique listings as of 2026-11-16 14:11 ET. The rewrite is still running. 35 of the 51 titles rewritten by about 2:09 PM ET were over 15 words. Etsy's 2025 guidance says "consider using less than 15 words".
- **Media:** lifestyle main photos are on 5 tees (Santa Paws, Doodle Mom Era, Zoomies O'clock, Doodle Mom, Doodle Dad). Listing videos are on 3 listings (Santa's Favorite bandana, Mom's Favorite bandana, Doodle Mom mug).
- **Attributes:** Holiday=Christmas is set on the rewritten listings. Etsy offers no Christmas value under Occasion and no Recipient field in these categories. All new descriptions carry "Order by Dec 5 for Christmas" in the first 160 characters. Per the owner, they contain no "AI" wording.
- **Research:** `/workspace/research/furever/01-competitors-seo.md` covers 10 competitor shops (partial coverage), 2026 search rules, and 10 ranked changes.

## Top 5 rules (2026 best practice in this field, each with a source URL)
1. Clear every Search Visibility flag. Etsy gives priority placement to listings with a single, well-lit, 2000 px+ primary photo (no collage), the most specific category, a return policy, and US shipping under $6. https://help.etsy.com/hc/en-us/articles/25869947521175-How-to-Use-the-Etsy-Search-Visibility-Page
2. Keep titles clear and item-first, ideally under 15 words. Put key traits up front, and only include holidays or recipients when they are essential to the item. Move gift and subjective words to tags and the description. https://help.etsy.com/hc/en-us/articles/115015628707-How-to-Create-a-Listing
3. Use all 13 varied tags, every relevant attribute, and the most specific category. Matching reads the title, tags, attributes, description, first photo and reviews. Set Holiday only on true holiday designs, since the attribute already matches searches. https://www.etsy.com/seller-handbook/article/375461474487 and https://help.erank.com/blog/using-holiday-attributes-effectively/
4. Quality and post-purchase experience now weigh more than raw conversion. Accurate processing times (which drive Etsy's estimated delivery date), reviews, response rate and low case rate all feed ranking. https://investors.etsy.com/_assets/_9bb344225cb404039577b245ea686f33/etsy/db/938/10106/shareholder_letter/Final_Q32026_Shareholder_Letter_.pdf and https://help.etsy.com/hc/en-us/articles/360001922768-How-to-Set-Up-Estimated-Delivery-Dates
5. Use the full media slots: up to 20 photos and 2 videos of 5–15 seconds per listing. "Designed by" listings must disclose their production partner (Printify). https://help.etsy.com/hc/en-us/articles/115015628707-How-to-Create-a-Listing and https://help.etsy.com/hc/en-us/articles/360024112614-What-Can-I-Sell-on-Etsy

## KPIs I own (metric, current value, target by Dec 31)
We have no baseline yet. The shop has 0 sales, and the Stats data has not been pulled. Targets get set after the first 14 days of post-rewrite data. Until then each one reads "set after baseline".

| Metric | How to measure | Current value | Target by Dec 31 |
|---|---|---|---|
| Search impressions | Shop Manager > Stats > traffic sources (Etsy search), plus Marketplace Insights search terms if available | Not pulled | Set after baseline |
| Listing views | Shop Manager > Stats, per listing (visits/views), compared before and after rewrite | Not pulled | Set after baseline |
| CTR | Views ÷ impressions per search term, from Stats or Marketplace Insights. Etsy Ads reports give clicks ÷ impressions only if ads run (needs OK) | No data | Set after baseline |
| Conversion rate | Orders ÷ visits, from the Stats conversion graph | 0 orders | Set after baseline |
| Favorites | Stats per listing, and the favorites count on each listing | Not pulled | Set after baseline |
| Orders per listing | Shop Manager orders CSV grouped by listing_id | 0 | Set after baseline |

## Asks (for Claude — heavy data pulls)
- **Etsy Stats export:** last 30 days and since Nov 16, per listing (views, visits, favorites, orders, search terms). It is needed to set KPI baselines and to compare long and short titles.
- **Search Visibility list:** the flagged listings from Shop Manager > Search Visibility (photo, category, return policy, shipping).
- **Keyword volumes:** eRank or Marketplace Insights volumes and competition for doodle long-tails (goldendoodle / labradoodle / bernedoodle / sheepadoodle / cavapoo / mini doodle × shirt / sweatshirt / mug / ornament / bandana / matching set).
- **Competitor browser pass:** the logged-in pass on the Etsy URLs listed at the end of 01-competitors-seo.md, to get best sellers, main-photo styles and review themes.
- **Printify facts:** whether a production partner is set on each listing, real production days, US shipping cost per product, and whether Printify can print Etsy gift messages or personalization.

## Hard limits
- No spending, price changes, publishing new content without Moondog88's keep/toss, or messages to customers/outsiders without Moondog88's OK.
- No "AI" in ad or listing copy (TikTok's AI-generated toggle stays on for AI visuals). Dog is never named: "This doodle".
- No tokens/secrets in GitHub. Never touch Claude's branches.
