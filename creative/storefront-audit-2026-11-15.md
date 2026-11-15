# Storefront audit: Etsy FurEver Faces first, then Shopify

**Date:** Sunday, Nov 15, 2026, evening (America/New_York). **Author:** Etsy Studio.
**Trigger:** Moondog88 via Jarvis, 6:23 PM ET. TikTok Shop is parked. Shopify is un-parked as of now. Goal: make both storefronts the best they can be.
**Method:** read-only. Nothing was edited on Claude's branches, and nothing was published, priced, or committed.
**Sources read:**
- `mooneyn60-art/skills`:
  - `claude/blissful-allen-waez05`, `skills/dropship/` (ETSY_STATE, ETSY_LISTINGS, ADS_READY, ORDER_RUNBOOK).
  - `claude/package-installation-setup-yv4j79`, `skills/dropship/` (BRIEF, HANDOFF, POLICIES_TO_PASTE).
  - `claude/youtube-monetization-strategy-m9vz6i`, `skills/etsy-factory/`.
  - `claude/great-turing-rqc91h`, `etsy-shop/`.
- `mooneyn60-art/AI-Youtube-Shorts-Generator_SamurAIGPT`, `claude/blissful-allen-waez05`, `fureverfaces/`.
- The Side-hustles notebook at main `7c43807`.
- The box folders `/workspace/etsy-listings`, `/workspace/etsy-design`, `/workspace/etsy-marketing`.

**Not reachable:**
- The Etsy shop page `etsy.com/shop/PrintanPress` (id 38484468) returned 403 to curl, and WebFetch timed out.
- No Shopify storefront URL appears in any file I read.

What is actually live on either store is **unknown**. Every live-state item below is marked unknown. No numbers were invented.

Branch names in this file are short: `blissful-allen` = `claude/blissful-allen-waez05`, `package-installation` = `claude/package-installation-setup-yv4j79`, `youtube-monetization` = `claude/youtube-monetization-strategy-m9vz6i`, `great-turing` = `claude/great-turing-rqc91h`.

Owner codes:
- **C** = Claude task.
- **ES** = Etsy Studio. The specialist is named: LS = Listings & SEO, PD = Product Designer, MA = Marketing & Ads.
- **OK** = needs Moondog88's okay.

---

## 0. Status: has Claude done the notebook tasks?

| # | Sev | Finding | Evidence | Owner |
|---|---|---|---|---|
| 0.1 | **High** | None of the notebook's tasks show as done. The notebook has no commits from Claude: all 46 commits are by Etsy Studio and Social Studio. The `blissful-allen` dropship files were last committed Nov 14, 4:26 PM ET. `SCOREBOARD.md` is still an empty template. So these are still open: the shop rename, the ETSY_STATE/BRIEF updates, the Printify costs, live listing IDs, the sample order, and the great-turing draft switch. | `git log` on Side-hustles; GitHub commits API for `skills@blissful-allen` (last commit 2026-11-14T21:26:48Z); `etsy-shop/SCOREBOARD.md` | C |
| 0.2 | **High** | We can't see what is live on Etsy. ETSY_STATE lists 75 Printify product IDs in the Etsy-linked Printify store 29754022, but no published status and no Etsy listing IDs. The public shop page is blocked. | `ETSY_STATE.md` L1-91; curl returned 403 | C |
| 0.3 | **High** | There is no evidence the approved Santa Paws samples (tee, bandana, ornament) were ordered. Real product photos and Mac-on-camera video both wait on them. | `TASKS.md` L17-21; SCOREBOARD is empty | C |

## 1. Listings: titles, 13 tags, descriptions, AI disclosure, attributes

| # | Sev | Finding | Evidence | Fix status | Owner |
|---|---|---|---|---|---|
| 1.1 | **High** | **Our own prepared copy had internal notes inside customer-facing descriptions.** Counts: 13 of 19 in `01-christmas-push.md` and 30 of 57 in `02-catalog.md`. 16 more descriptions in 02 were missing the period after the slogan (for example "myth A cartoon"). These would have been pasted live. Examples: "ETSY_STATE.md does not state material, sizes, or care...", "ETSY_STATE.md says each dog listing should link to its human tee and back.", "(Printify blueprint 562, Printed Mint)", "link the listings to each other". The other files also have leaks: `05-backlog.md` 5 of 20, `06-valentines.md` 8 of 8 ([CONFIRM]), `07-valentine-printables.md` 3 of 3. | `etsy-shop/listings/01-christmas-push.md` L68 and L513; `02-catalog.md` L1976, L2421 and others | **Fixed in this audit, pending commit.** Cleaned copies are in `/workspace/etsy-audit/cleaned-listings/01-christmas-push.md` and `02-catalog.md`: 13 and 34 descriptions edited, 0 leaks left, AI disclosure kept on all 76. The validator passes: titles 67-95 characters, 13 tags each. 05, 06 and 07 are not pasted now, so LS cleans them before the Jan 4 drafts. | ES (LS); Etsy Studio commits |
| 1.2 | Med | Claude's only listing copy is still the stencil titles. Every title follows "Goldendoodle [Product], [Design] Doodle [Product], Doodle Mom Dad Gift, ...", tags are reused across products, and descriptions are one sentence. Any listing already live probably uses this copy (unknown). | `ETSY_LISTINGS.md` L24-50 | **Fixed by our work.** 01, 02 and 04 hold 82 rewritten listings that pass the validator. | C pastes, as drafts |
| 1.3 | Med | Material, sizes and care are missing for sweatshirts (Monster Digital bp 49), pet bandanas (Printed Mint bp 562) and pet tanks (Printed Mint bp 571). The cleaned copy now says only "printed to order". | `ETSY_STATE.md` L5, L69 | No fix. The data has to come from Printify. | C |
| 1.4 | Med | The mug size claim "11 oz or 15 oz, dishwasher and microwave safe" comes from the template. ETSY_STATE only gives "SPOKE (1) mugs (68)". | `ETSY_LISTINGS.md` L35; `ETSY_STATE.md` L5 | No fix. Verify the variants on the Printify product. | C |
| 1.5 | Med | Printables have no AI disclosure decision yet. The copy says "original designs". The 6 etsy-factory listings have `taxonomy_id: null` and 5 images each, out of the 10 Etsy allows. | `04-printables.md` L7; `products/*/listing.json` @ youtube-monetization | Open task in TASKS L71 | C confirms; PD adds images |
| 1.6 | Low | Matching tee ↔ dog item cross-links. The cleaned copy says "A matching tee for the humans is in the shop." The real link is the "Matching Human + Dog" shop section. | `08-shop-branding.md` §5 | Fixed in copy; the section setup is pending | C |
| 1.7 | Low | The hero bundle has no SKU or fulfilment method. | `01-christmas-push.md` §Hero Bundle; TASKS L70 | Open | C |

## 2. Photos and mockups

| # | Sev | Finding | Evidence | Fix status | Owner |
|---|---|---|---|---|---|
| 2.1 | **High** | The Ads gate requires new photos on the 5 hero listings. Our 2000×2000 lifestyle hero exists only for the **Santa Paws ornament and bundle** (`L-bundle-ornament-tree.jpg`). Ornament mockups exist for Snow, Mom and Dad. **Santa Paws tee, Doodle Mom tee and Doodle Dad tee have no 2000×2000 thumbnail from us.** The Santa tee crops are 1080 square and smaller, so they are social-only. | `etsy-shop/design/christmas/*`, sizes checked; DECISIONS L23-27 | Partly fixed | ES (PD): 3 tee thumbnails |
| 2.2 | Med | The Christmas flatlay, person-dog and unboxing images are approved as secondary photos for the Santa tee, ornament and bandana. They aren't uploaded anywhere yet (unknown). | TASKS L102-113 | Fixed in assets; upload pending | C |
| 2.3 | Med | Flat "concept image" mockups and custom-photo mockups (`tee-card.jpg`, `mug-mug.jpg`, `mockup-04/05/06/07/10/11`, the pop-art grid) must not go on ready-made listings or the Shopify ready-made catalog. | `fureverfaces/` root, 294 files | No fix needed; a do-not-use rule | C |
| 2.4 | Med | No real product photos exist. They depend on the 3 samples (0.3). | — | Blocked on samples | C orders; PD and Moondog88 shoot |
| 2.5 | Low | The Printables covers don't name FurEver Faces, and bingo and word search share one cover template. | AUDIT §C; design-direction | Valentine covers fixed (`/workspace/etsy-design/valentines/printable-covers`); Christmas covers open | ES (PD) |

## 3. Shop branding (name, title, banner, icon, About, announcement)

| # | Sev | Finding | Evidence | Fix status | Owner |
|---|---|---|---|---|---|
| 3.1 | **High** | The rename from PrintanPress to FurEver Faces is approved but not done. ETSY_STATE line 3 still says PrintanPress. | `ETSY_STATE.md` L3; DECISIONS L6 | Approved; waiting on Claude | C |
| 3.2 | Med | The `08-shop-branding.md` draft has internal notes inside customer copy. The announcement says "This announcement does not offer free shipping." The About says "The name customers should see is FurEver Faces." and "Sources describe Mac as...". The [CONFIRM] personal details are unanswered. | `etsy-shop/listings/08-shop-branding.md` L33, L48, L50 | No fix yet. LS rewrites a clean paste-ready version once Moondog88's details arrive. | ES (LS) + OK |
| 3.3 | Med | The shop title, announcement, About and sections aren't approved to paste. The working title pick is "FurEver Faces \| For people owned by a doodle" (44 characters). | 08 §1; TASKS L91 | Draft exists | OK |
| 3.4 | Low | The banner `logo/mac-banner.png` is 1600×400, which is Etsy's minimum for the large banner. The text is centered, so mobile crops are a risk. The icon `mac-icon.png` at 1000×1000 is fine. | sizes checked | Re-export at 3360×840 with text inside a safe zone | ES (PD) |
| 3.5 | Low | The Shopify logo tagline is near-black (#14100E) on a black header, so "THE DOODLE SHOP" can't be read. | `logo/mac-shopify-logo.png`; design-direction | Open (TASKS L162) | C, or PD re-exports |

## 4. Policies (shipping, returns, processing, Dec 5 cutoff)

| # | Sev | Finding | Evidence | Fix status | Owner |
|---|---|---|---|---|---|
| 4.1 | **High** | **Two policy texts conflict, and neither fits the ready-made line.** `fureverfaces/policies.md` is built around photo proofs, has $49 free / $5.99, and still has a "December [DATE]" placeholder. `POLICIES_TO_PASTE.md` says Dec 5 and "shipping shown at checkout", has no $49, and its cancellation rule mentions proofs. Custom art is paused, so both need a ready-made version. | `policies.md` L6-L26; `POLICIES_TO_PASTE.md` L15-30 | No fix. ES drafts one ready-made policy set for Etsy and Shopify. | ES (LS) drafts, OK, C pastes |
| 4.2 | **High** | Live Etsy policy settings are unknown: processing time, shipping profile, returns/exchanges, and whether any free-shipping threshold is set. | TASKS L29 | Unknown | C reports |
| 4.3 | Med | Marketing drafts still imply Etsy free shipping. `organic-content-2wk.md` L101 and L288-302 say "still clears our $49 free-shipping line" and "the bundle still gets free shipping" (tagged [CONFIRM]). This conflicts with the no-free-shipping-claims rule. `posting-pack.md`, which is what Moondog88 posts from, is compliant. | `etsy-shop/ads/organic-content-2wk.md` | No fix | ES (MA) |
| 4.4 | Low | The Dec 5 cutoff is consistent across our copy. Claude's BRIEF still says "Order by Dec 10" and "Dec 8-12". | `BRIEF.md` L16, L47 | Decided (DECISIONS L38); BRIEF update open | C |

## 5. Pricing consistency and the 45% rule

| # | Sev | Finding | Evidence | Fix status | Owner |
|---|---|---|---|---|---|
| 5.1 | **High** | No Printify base cost or shipping figure exists anywhere, so the 45% rule can't be scored for any product. The Cyber Week sale starts Nov 27 only for products under the ceilings. | 03-pricing-memo L44; SCOREBOARD | Open (TASKS L23-30) | C |
| 5.2 | Med | Claude's files still carry old prices: ETSY_LISTINGS has ornament $21.99 and mug $18.00, ADS_READY says "from $21.99", and BRIEF has ornament $21.99. The record (ETSY_STATE + DECISIONS) is tee $26, sweatshirt $39.99, mug $17.99, ornament $16.99, bandana $18.99, tank $27.99. Live Etsy prices are unknown. | `ETSY_LISTINGS.md` L35; `ADS_READY.md` L39; `BRIEF.md` L36 | Our copy is fixed. Claude's files and the live check are open. | C |
| 5.3 | Low | Our `holiday-marketing-plan.md` still shows $21.99 and $18.00 alternative lines (L58-61, L379). | etsy-shop/ads | Superseded by DECISIONS; mark or remove | ES (MA) |
| 5.4 | Med | Shopify prices differ from the Etsy record. BRIEF lists the Shopify ornament at $21.99, socks $19.99 and a sherpa blanket $94.99, which are custom-line products. There's no parity rule yet. | `BRIEF.md` L13, L36 | Needs a decision | OK |

## 6. Etsy vs Shopify consistency

| # | Sev | Finding | Evidence | Owner |
|---|---|---|---|---|
| 6.1 | **High** | **The Shopify catalog doesn't match the Etsy catalog, and Claude's own files disagree about Shopify:**<br>- BRIEF and HANDOFF describe 10 custom pet-portrait products (ornaments, mugs, socks, tee, canvas, bandana, sherpa blanket, memorial ornament), with pet-photo upload fields built into an *unpublished* theme, "FurEver Faces – Holiday Chaos (TARS fixes)".<br>- ADS_READY describes 4 products × 6 ready-made designs and "No custom art and no photo upload".<br>- Etsy is the 75-product ready-made cartoon line.<br>- DECISIONS #4 pauses custom art.<br>What is in the store today is unknown. | `BRIEF.md` L13; `HANDOFF.md` L14; `ADS_READY.md` L8-10; DECISIONS L18-21 | C reads the store through the Shopify connector (Jarvis); OK on the direction |
| 6.2 | **High** | Shopify fulfilment: the products are "set to manual fulfillment at Nolan's home location; none is linked to Printify". A Printify Shopify store (29751070) exists but isn't wired to these products. | `HANDOFF.md` L19; `ETSY_STATE.md` L3 | C |

## 7. Shopify specifics

All live settings are **unknown** until someone reads the store through the Shopify connector. As of Nov 14 the files say the following.

| # | Sev | Finding | Evidence | Owner |
|---|---|---|---|---|
| 7.1 | **High** | Launch blockers as of Nov 14: store password on, Shopify Payments off, no test order, and **no product had a single image** (`featuredMedia: null`). | `ADS_READY.md` L12-16; `BRIEF.md` L30 | Moondog88 (password, payments); C (images) |
| 7.2 | **High** | Theme: the TARS-fixed theme is unpublished, and the live theme is unknown. The TARS theme adds photo-upload fields and removes "Buy it now". That suits the paused custom line, not ready-made. | `HANDOFF.md` L14 | C reviews; OK to publish |
| 7.3 | Med | Policies: see 4.1. Contact email, privacy policy, About page and Contact page are all unknown. | `BRIEF.md` L37-42 | ES drafts; C pastes after OK |
| 7.4 | Med | Free shipping: DECISIONS keeps $49 free / $5.99 below. Whether the Shopify shipping rates are actually set that way is unknown. Hero bundle tee + bandana + ornament = $61.98 clears it; tee + bandana = $44.99 doesn't. | DECISIONS L14-16 | C verifies |
| 7.5 | Med | No file documents the home page, collections, navigation, product SEO titles/meta, or apps (reviews, abandoned-cart email, Google free listings, Shop Pay/Apple Pay). BRIEF's day 3-5 list was never confirmed. | `BRIEF.md` L82-88 | C audits via connector; ES writes the copy |
| 7.6 | Med | Product copy parity: Shopify has no rewritten copy. Our Etsy copy (cleaned 01/02) can be reused nearly word for word on Shopify. Shopify allows longer titles, so use the Etsy title as the SEO title and a short product name as the H1. | — | ES (LS) adapts; C pastes as drafts |
| 7.7 | Low | BRIEF says an empty draft product, "Untitled Nov 14 at 11:34 AM", should be deleted. Whether it still exists is unknown. | `BRIEF.md` L35 | C, after OK |

## 8. Safety and separation

| # | Sev | Finding | Evidence | Owner |
|---|---|---|---|---|
| 8.1 | **High** | `great-turing` `etsy-shop/src/upload.py` still sends 7 printables with `publish="yes"` (lines 32, 44, 55, 66, 109, 126, 145) through the Make.com Etsy upload. They carry "© DoodleDesignAndCo". The Dear Santa letter says "Original hand-drawn Santa, reindeer & gift artwork" while its art is flagged as Irasutoya-style clip art. Branch last committed Nov 15, 2:01 PM ET. | `skills@great-turing:etsy-shop/src/upload.py` | C (switch to `publish="no"`; hold Dear Santa) |
| 8.2 | Low | Meatball references are still inside Etsy-side files: `organic-content-2wk.md` L13, L23, L368; `posting-pack.md` L28; `valentines-plan.md` L503; `holiday-marketing-plan.md` L485, L553; `08-shop-branding.md` L63. These are references, not branding, but the org rule wants strict separation. `etsy-shop/tiktok-shop/products.md` is clean. | grep of etsy-shop/ | ES (MA, LS) |
| 8.3 | Low | `ETSY_STATE.md` in a public repo exposes the shop id, Printify store and product ids, and a Make.com scenario id. No tokens were found. | `ETSY_STATE.md` L3-4 | Still open (TASKS L130) |
| 8.4 | Info | TikTok Shop is parked. The Printify-drafts task stays in TASKS, not urgent. | Jarvis relay, 6:23 PM ET | — |

## 9. What our prepared work already fixes vs. no fix yet

**Already fixed, waiting on paste, approval or commit:**
- Titles and tags for 82 listings (01, 02, 04).
- Descriptions with the AI disclosure. The internal-note leak was fixed in `cleaned-listings/`.
- Price lines aligned to ETSY_STATE.
- The Dec 5 cutoff in all copy.
- Santa Paws hero and secondary lifestyle photos, plus the Snow, Mom and Dad ornament mockups.
- Social crops and the posting pack (no free-shipping claims).
- Draft shop title and sections.
- Cyber Week plan and ceilings.
- Valentine copy and art.
- TikTok product brief (parked).

**No fix yet:**
- Live-state check and Etsy listing IDs (0.2).
- Printify costs and the 45% check (5.1).
- Sample order (0.3).
- Shop rename (3.1).
- Tee thumbnails for the Santa, Mom and Dad tees (2.1).
- Sweatshirt, bandana and tank specs (1.3).
- One ready-made policy set (4.1).
- Clean About and announcement (3.2).
- Banner re-export (3.4).
- The whole Shopify direction, catalog, fulfilment, theme, nav and apps (6.1, 6.2, 7.x).
- great-turing publish flag (8.1).
- Meatball reference scrub (8.2).
