# FurEver Faces — Etsy Studio Assignment 1

**Role:** Product Designer (pipeline and design quality)  
**Shop:** FurEver Faces, doodle-owner print-on-demand via Printify (and Shopify), tagline “For people owned by a doodle.”  
**Date:** 15 November 2026 (America/New_York)  
**Status:** Ready-to-use direction. Nothing in this document has been published, priced, or paid. No repo files were edited.

**Sources (read-only):**

- `mooneyn60-art/AI-Youtube-Shorts-Generator_SamurAIGPT`, branch `claude/blissful-allen-waez05`, folder `fureverfaces/`
- `mooneyn60-art/skills`, branch `claude/blissful-allen-waez05`, folder `skills/dropship/`
- `mooneyn60-art/skills`, branch `claude/youtube-monetization-strategy-m9vz6i`, folder `skills/etsy-factory/`

**Blockers / gaps (inline, also summarized at the end):**

- `skills/etsy-factory/SKILL.md` is missing on branch `claude/youtube-monetization-strategy-m9vz6i` (HTTP 404). Workflow had to be inferred from `scripts/`, `specs/`, and `products/`.
- `mooneyn60-art/Side-hustles` exists but is empty; there is no `etsy-shop/TASKS.md`.
- `fureverfaces/` has no README and no written design briefs — only art, mockups, ads, `policies.md`, and print files.
- Christmas shipping cutoff in `skills/dropship/ADS_READY.md` and listing copy is **5 December**; `fureverfaces/policies.md` still says “December [DATE]”.
- Shop-identity split: dropship notes name the Etsy shop **PrintanPress**, while logos and Shopify materials say **FurEver Faces / The Doodle Shop**. The etsy-factory printables are generic holiday/senior puzzles with no shop name at all (PDF author field: “Original printable design”).

WCAG contrast ratios below were computed from sampled pixels using the WCAG 2 relative-luminance formula, ratio `(L1 + 0.05) / (L2 + 0.05)`. They are measurements, not estimates. Items marked **idea** are recommendations, not facts found in the files.

---

## 1. Christmas push mockup and photo direction

Today is 15 November 2026. The documented last order date for Christmas delivery is **5 December 2026** — 20 days out. Current merch mockups are flat illustrated “concept images,” not photographs of real goods. `skills/dropship/ETSY_LISTINGS.md` already expects Printify to generate about ten product photos per listing on publish; those should replace the flat blanks for on-product accuracy. Lifestyle and gift-context shots still need to be added, or the grid will look like every other POD cartoon tee.

### What already exists (use these files, do not redraw the art)

| Design | Art / print file | Current mockups | Notes |
|---|---|---|---|
| **Santa Paws** — “Nice list (pending)” | `fureverfaces/v7/D-santa.jpg`, `fureverfaces/print/PRINT-santa.png` | `v7/M-orn-santa.jpg`, `v7/M-tee-santa.jpg`, `v7/M-mug-santa.jpg` (all labeled “concept image”) | Cream doodle in a Santa hat with gifts. Etsy copy exists for tee, mug, ornament, canvas. |
| **Snow Day** — “Zoomies incoming” | `fureverfaces/v8/D-snow.jpg`, `fureverfaces/print/PRINT-snow.png` | `v8/M-tee-snow.jpg`, `v8/M-mug-snow.jpg` only | Beanie + scarf doodle. Printify IDs exist for tee, sweatshirt, mug, and ornament (`orn-snow` in `ETSY_STATE.md`), but **no local ornament mockup** in `v8/` or `v9/`. |
| **Doodle Mom** — “Curls, cuddles & chaos” | `fureverfaces/v9/D-mom.jpg`, `fureverfaces/print/PRINT-mom.png` | `v9/M-tee-mom.jpg`, `v9/M-mug-mom.jpg` | Pink bandana doodle. Ornament exists in Printify state (`orn-mom`); no local ornament mockup. |
| **Doodle Dad** — “Chief treat officer” | `fureverfaces/v9/D-dad.jpg`, `fureverfaces/print/PRINT-dad.png` | `v9/M-tee-dad.jpg`, `v9/M-mug-dad.jpg` | Cap doodle. Ornament exists in Printify state (`orn-dad`); no local ornament mockup. |
| **Matching sets** | Human: Mom/Dad/Santa print files. Dog items: `fureverfaces/pet/P-mom.png`, `P-dad.png`, `P-santa.png` (and related) | `fureverfaces/ads3/ad-matching-set.png` | Ad shows a photoreal woman in a **Doodle Mom tee** plus a pink **dog tank** (“Mom’s Favorite / Don’t tell the kids”), not a bandana. Bandanas are in the catalog (Printify blueprint 562, Printed Mint). |

Older flat merch mockups in the folder root (`mockup-01-ornament-round.jpg`, `mockup-07-tee-ugly-sweater.jpg`, etc.) are a different design generation and should not be used as the Christmas hero images.

### How to make each shot (method key)

- **Printify mockup generator:** On-product accuracy (print placement, stitch, glaze, ornament rim). Use for the catalog “product itself” slots. This is the path `ETSY_LISTINGS.md` already describes.
- **AI-generated lifestyle:** Fast way to show a tree, a couch, or a matching walk when a real set is not shot yet. Must use the **actual print art**, not a regenerated dog. Watch anatomy, typography warping, and fake brand marks. Label internally as AI so listings can keep the “artwork created with AI tools” disclosure already in the copy.
- **Real photos (preferred for thumbnails):** One session with a real cream/apricot doodle (Mac appears in `fureverfaces/ff-real.jpg` and the Rookie Card / tarot samples) plus one adult in a printed tee, a decorated tree, and a printed bandana. Highest trust for Etsy; hardest to schedule before 5 December.

**Etsy slots:** Up to 10 images. Image 1 is the search-grid thumbnail. Export **2000 × 2000 px, 1:1**, sRGB, for every slot including lifestyle (Etsy crops the grid to square). Optional 4:5 masters can be shot and center-cropped to 1:1 for the listing.

Suggested 10-slot order, reused across this push: (1) thumbnail lifestyle, (2) Printify on-product front, (3) detail/macro, (4) second lifestyle, (5) scale/in-hand, (6) back or second angle, (7) color/size variants, (8) matching set if any, (9) gift-context, (10) size chart / materials. Swap in design-specific shots as noted below.

### 1a. Santa Paws ornament

Ceramic round ornament with ribbon. Current concept: `fureverfaces/v7/M-orn-santa.jpg`.

| # | Shot type | Setting / props | Model / dog | Angle | Lighting | Crop | Method | Thumbnail? |
|---|---|---|---|---|---|---|---|---|
| 1 | Lifestyle, ornament on tree | Lit Christmas tree, warm indoor evening, a few wrapped gifts at the base (red/teal to echo the art, not a trademarked wrap pattern) | No person required; cream doodle optional, sitting under the tree looking up | Eye-level to slightly below the ornament, ornament sharp, bokeh lights behind | Warm practical tree lights + one soft key; avoid hard flash glare on glaze | 1:1, ornament in the upper third, room to breathe | **Real photo preferred.** AI lifestyle only if a tree cannot be shot this week | **Yes — this is the thumbnail** |
| 2 | On-product hero | Seamless warm cream (`#FFF2DE`) or Printify’s default | — | Straight-on, fill the circle, ribbon visible | Soft studio, no hot spot on the glaze | 1:1 | **Printify generator** | No |
| 3 | Macro / print quality | Same, or held at chest height | Hands only | 45°, focus on hat, “SANTA PAWS” lettering, and gold rim | Soft side light to show ceramic depth | 1:1 tight crop | Real or Printify close-up if offered | No |
| 4 | Scale in hand | Neutral sweater sleeve, maybe a second unprinted ornament for scale | Hands only | 3/4 | Window daylight | 1:1 | Real photo | No |
| 5 | Gift context | Ornament in an open craft box with tissue and a small card (“Nice list (pending)”) | Hands unwrapping, optional doodle in frame | 45° down | Soft daylight | 1:1 | Real, or AI if needed | No |

Do not use a generic “ugly sweater” flat or the memorial ornament mockup (`mockup-11-memorial-ornament.jpg`) for this listing.

### 1b. Santa Paws tee

Current concept: `fureverfaces/v7/M-tee-santa.jpg` (flat white tee on cream, “Unisex cotton tee · concept image”).

| # | Shot type | Setting / props | Model / dog | Angle | Lighting | Crop | Method | Thumbnail? |
|---|---|---|---|---|---|---|---|---|
| 1 | Lifestyle, wearer + dog | Living room or front porch with a wreath/tree edge; adult in the white or heather Santa Paws tee, cream doodle beside them | One adult (any gender) + doodle; tee must be the real print, not a restyled dog | Mid-shot, waist up, print fully readable | Open shade or window light, warm | 1:1, face and print both clear | **Real photo preferred** for thumbnail; AI lifestyle as a stand-in | **Yes** |
| 2 | On-product front | Ghost or dressed mannequin / Printify model, white and one dark colorway if offered | — | Straight front, print slightly below the collar | Even studio | 1:1 | **Printify generator** | No |
| 3 | Print detail | Same tee | — | Tight on arch type + hat + “NICE LIST (PENDING)” | Soft | 1:1 | Printify or real | No |
| 4 | Back / fit | Standing, relaxed | Same model, no need for the dog | 3/4 back and side | Same | 1:1 | Printify or real | No |
| 5 | Gift fold | Folded tee with a sprig of pine and a simple tag | Hands optional | Top-down | Daylight | 1:1 | Real or AI | No |

### 1c. Snow Day (tee first; mug and ornament as supporting)

Current concepts: `v8/M-tee-snow.jpg`, `v8/M-mug-snow.jpg`. No local ornament mockup — generate the ornament product shot in Printify from `PRINT-snow.png`.

| # | Shot type | Setting / props | Model / dog | Angle | Lighting | Crop | Method | Thumbnail? |
|---|---|---|---|---|---|---|---|---|
| 1 | Lifestyle, snow-day energy | Snowy yard, doorstep, or a mudroom bench with boots and a knit hat (orange/green to rhyme with the art, not a branded hat) | Adult in the Snow Day tee, doodle in a plain knit scarf or the matching bandana if produced | Mid-shot, slight downward smile-level, print readable | Bright overcast or open shade (cool daylight, not orange tungsten) | 1:1 | **Real if snow or a convincing cold-day porch is available; otherwise AI lifestyle** | **Yes for the tee listing** |
| 2 | On-product tee | Studio | — | Straight front | Even | 1:1 | **Printify** | No |
| 3 | Mug lifestyle | Cocoa on a windowsill, snow or bare branches outside, tee or sleeve in soft focus | Hands + optional doodle nose at the frame edge | 45° | Window side light | 1:1 | Real or AI | Thumbnail for the **mug** listing |
| 4 | Ornament on a cooler-toned tree or wreath | White lights, pine, maybe a mug nearby to cross-sell | — | Eye-level | Cooler than Santa Paws (daylight, not all-gold) | 1:1 | Real or Printify + AI scene | Thumbnail for the **ornament** listing |
| 5 | Detail | Beanie pom-pom and “ZOOMIES INCOMING” lettering, sharp | — | Macro | Soft | 1:1 | Printify or real | No |

Keep Santa Paws warm (gold lights, red/teal gifts) and Snow Day cool (daylight, pine, cocoa) so the two Christmas designs do not look like the same listing in the shop grid.

### 1d. Doodle Mom / Doodle Dad tees

Current concepts: `v9/M-tee-mom.jpg`, `v9/M-tee-dad.jpg`. These are year-round designs being pushed as gifts; they should not be forced into heavy snow/Santa styling.

| # | Shot type | Setting / props | Model / dog | Angle | Lighting | Crop | Method | Thumbnail? |
|---|---|---|---|---|---|---|---|---|
| 1 | Lifestyle portrait | Bright home interior, sofa or kitchen; wrapped gift only as a small cue, not a full Christmas set | **Mom listing:** woman or the gift-giver wearing Doodle Mom, doodle with the pink bandana look (real bandana, not a copy of a character print). **Dad listing:** man or gift-giver in Doodle Dad, doodle optional in a simple cap or the dad bandana | Mid-shot, print fully legible (“CURLS, CUDDLES & CHAOS” / “CHIEF TREAT OFFICER”) | Soft window light | 1:1 | **Real photo preferred** | **Yes, one unique thumbnail per listing** |
| 2 | On-product front | Studio, light pink tee for Mom, white or navy for Dad (idea: confirm available Bella + Canvas colors in Printify before locking) | — | Straight | Even | 1:1 | **Printify** | No |
| 3 | Pair / gift | Mom and Dad tees folded side by side, or two people + one doodle | Two adults + doodle if possible | Top-down folds, or a wide mid-shot cropped to 1:1 | Daylight | 1:1 | Real or AI | Use as slot 8 on both listings, not as both thumbnails |
| 4 | Ornament (if listed) | Tree or mantel, less “Santa” than Santa Paws — think family-room shelf | — | Eye-level | Warm but simple | 1:1 | Printify + real/AI lifestyle | Ornament thumbnail |
| 5 | Detail | Pink collar and “DOODLE MOM” arch, or cap and “DOODLE DAD” arch | — | Macro | Soft | 1:1 | Printify or real | No |

### 1e. Matching human tee + dog bandana sets

The assignment is **tee + bandana**, not the tank in `ads3/ad-matching-set.png`. Keep the tank as a second dog SKU if it already exists, but do not make the tank the set hero. Build three set stories: Doodle Mom, Doodle Dad, and Santa Paws. Print files and pet graphics already exist (`PRINT-mom.png` / `P-mom.png`, dad, santa).

| # | Shot type | Setting / props | Model / dog | Angle | Lighting | Crop | Method | Thumbnail? |
|---|---|---|---|---|---|---|---|---|
| 1 | Lifestyle, human + dog matching | Sidewalk, park, or front steps; adult in the tee, doodle wearing the **printed bandana** tied correctly (triangle at the chest, not a bib) | Adult + doodle; Mom set in blush/pink, Dad set in navy/white, Santa set with a winter coat or tree behind | Mid-shot, both prints readable. Bandana art is small — get close enough that the doodle art is visible | Open shade | 1:1, both faces and both prints in frame | **Real photo is the only convincing thumbnail for a “matching set.”** AI is a backup and often fails bandana drape | **Yes** |
| 2 | Flat lay of the set | Tee folded, bandana opened to show the print, maybe a leash and a kraft tag “One for you. One for the dog.” (line already used in the ad) | — | Top-down | Daylight, slightly warm | 1:1 | Real (easy, no model) or a careful AI flat lay using the actual art | No (good slot 2 if a live shoot slips) |
| 3 | On-product split | Printify tee mockup beside Printify bandana mockup, same background | — | Straight | Even | 1:1 | **Printify**, then a designed diptych (the current ad already uses this structure) | No |
| 4 | Bandana on dog, close | Same walk or a simple backdrop | Doodle only | 3/4, focus on the bandana print | Open shade | 1:1 | Real | No |
| 5 | Cross-link | Small end-card or last slide: “Human tee + dog bandana” with SKUs / links, no extra claims | — | Graphic | — | 1:1 | Designed graphic, not a photo | No |

**Do not** restyle the dog tank slogan onto a bandana without a dedicated bandana layout (bandana print scale in `ETSY_STATE.md` is 0.29 at y 0.34 — a full tee graphic will be tiny or cropped). See placement notes in §2.

---

## 2. Design briefs

Fit the existing merch system: bold arched varsity headline, a sitting cartoon doodle with a heavy ink outline and simple props, a short black punchline under the dog, transparent 3600 × 3600 PNG. Do not introduce a new illustration school for these two lines.

Print placement already documented in `skills/dropship/ETSY_STATE.md` (do not treat these as prices or as a publish order):

- **Tee** (Bella + Canvas style; blueprint 12, Monster Digital): scale **0.95** at **y 0.42**.
- **Mug** (blueprint 68, SPOKE): three copies at **x 0.17 / 0.50 / 0.83**, scale **0.31**.
- **Pet bandana** (blueprint 562, Printed Mint): scale **0.29** at **y 0.34**.

Art board for all three: **3600 × 3600 px PNG, sRGB, transparent background**, same as `fureverfaces/print/PRINT-*.png`.

### 2a. Valentine’s line — “Be Mine / Fur-ever Yours”

**Due mid-December 2026** so listings can sit before Valentine’s Day (14 February 2027). Not a Christmas SKU; do not put Santa hats or snow on these.

**Concept.** A cream/apricot cartoon doodle (same face language as Doodle Mom / Santa Paws) sits facing us, wearing a simple blush bandana and a heart-shaped tag on the collar — an original tag, not a sports-brand or cartoon-character heart. The dog holds or sits in front of a plain paper valentine. Two headline variants share the drawing: **BE MINE** and **FUR-EVER YOURS**. Punchlines (pick one per variant, do not stack): “Owned since day one.” or “Will trade kisses for snacks.” Mood is warm and funny, not steamy, not formal wedding stationery.

**Art style.** Existing FurEver Faces cartoon: thick rounded outlines, big eyes, visible curls, flat color with simple cheek and ear shading. No photoreal collage, no watercolor wash, no anime redesign.

**Palette (hex).**

| Role | Hex | Use |
|---|---|---|
| Berry (brand wordmark) | `#C2185B` | “BE MINE” / “FUR-EVER YOURS” arch on light tees; hearts |
| Berry shadow / small type on light | `#8B123F` | Tag lettering, thin rules — not for large fills |
| Blush | `#F7C6D6` | Bandana, cheek, mug lip idea |
| Cream | `#FFF2DE` | Backgrounds in lifestyle graphics only; not a tee ink |
| Ink | `#1A1A1A` | Outlines and the punchline |
| Warm gold | `#C9A227` | Small tag ring or spark dots (sparingly) |

Do not put `#C2185B` on a maroon or black tee without a cream or white underbase; that pair is only 3.58:1 on black (see §5).

**Typography.** Headline: the same heavy, slightly condensed varsity / collegiate sans used on “SANTA PAWS” and “DOODLE MOM,” arched over the dog, all caps. Punchline: compact bold grotesque, straight, all caps or title case to match “Nice list (pending).” Optional very small script only for the words “fur-ever yours” on the **collar tag**, not for the main arch (avoids a Coca-Cola-like script lockup). No handwriting font that mimics a licensed greeting-card brand.

**Layout per product.**

- **Tee:** Arch headline (~top 22% of the square), doodle + tag in the middle, punchline under the paws with clear space above the hem. Keep a safe margin so scale 0.95 at y 0.42 does not clip the arch at the collar or the punchline at the waist. One graphic, centered, no all-over pattern.
- **Mug:** The same stack, but tighter: shorten the arch or flatten it slightly so it survives the wrap. Because the mug uses three copies around the cup, the design must read as a self-contained badge — no elements that only make sense as a wide panorama. Leave transparent padding so handles do not eat the face.
- **Bandana:** Redesign, do not shrink the tee file. Center a **circular or rounded-square badge** (doodle head + short title) in the print area that lands at scale 0.29, y 0.34. Prefer “BE MINE” or a small heart + “FUR-EVER YOURS” in one line. No tiny punchline (it will be unreadable on fabric). Keep important ink inside a safe circle; bandana corners fold out of view.

**Variants.** (1) Headline **BE MINE** + punchline “Owned since day one.” (2) Headline **FUR-EVER YOURS** + punchline “Will trade kisses for snacks.” Same drawing. Tee colorways, idea: white, soft pink, cream/ivory if the blank exists; avoid dark colors unless the art is re-separated for light ink. Mug: white ceramic, 11 oz / 15 oz as already used. Bandana: blush and a berry/navy cloth if Printed Mint offers them — confirm in catalog before promising colors.

**Do.** Original doodle, original typography, generic hearts. Keep Mac’s likeness out of this ready-made line (Mac’s photo belongs on personalized Rookie Card / tarot only). Proof the bandana on a mockup at the real scale before publishing.

**Don’t.** No Disney/Pixar dogs, no Snoopy, no official candy-brand logos, no interlocking sports monograms, no “I love NY”-style copycats, no real rose-brand packaging, no photoreal couple stock that you then “add a dog” to for the merch art. No “Barbie” pink lockups or other owned wordmarks.

### 2b. “Doodle Resolutions” — January line

**Timing.** Design and list in December, after the Christmas merch is shot, so the line is live for New Year gift-to-self and early January. Not a Christmas tree SKU.

**Concept.** The same cartoon doodle, this time in a plain sweatband or sitting next to a tiny notepad. Headline: **DOODLE RESOLUTIONS**. Under the dog, a short list of joke resolutions in three tight lines, not a paragraph: “1. Steal fewer socks” / “2. Share the bed” / “3. Come when called (we’ll see).” Alternate one-liner if the list feels too small on the mug or bandana: “New year. Same zoomies.” Tone is dry and affectionate, like “Nice list (pending),” not gym-bro or diet-shame.

**Art style.** Identical cartoon system. Props stay generic: a plain sweatband, a blank notepad, a tennis ball. No January-1 party hats that look like a licensed mascot, no champagne-brand labels.

**Palette (hex).** Winter, not Valentine berry.

| Role | Hex | Use |
|---|---|---|
| Forest | `#1F4D3A` | Headline (already the christmas-theme primary in etsy-factory) |
| Slate | `#22385C` | Optional second colorway / sweatband | 
| Ink | `#1A1A1A` | Outlines and the list |
| Cream | `#FFF2DE` | Lifestyle backgrounds only |
| Gold accent | `#C9A227` | Small stars or the notepad band, sparingly |
| Paper tint | `#E7EFE9` | Notepad fill |

**Typography.** Same arched varsity headline. The three resolutions in a compact bold grotesque, left-aligned as a short list under the dog on the tee; centered one-liner on mug and bandana if the list shrinks poorly. Numbers in forest green, not a sports-league font.

**Layout per product.**

- **Tee:** Arch “DOODLE RESOLUTIONS,” doodle in the middle, three-line list under the paws. Same 3600² board and tee placement as §2a. Do not let the list drop into the hem; if it crowds, drop to the one-liner.
- **Mug:** Prefer the one-liner version, or a two-line abbreviation (“Steal fewer socks / Share the bed”) plus the doodle. Badge composition for the three-around-the-mug placement.
- **Bandana:** Badge: doodle in a sweatband + “NEW YEAR. SAME ZOOMIES.” or just “DOODLE RESOLUTIONS.” No three-line list at bandana scale.

**Variants.** (1) List version, tee-led. (2) One-liner version, mug- and bandana-led. Optional colorways: white and heather / forest tee if a light-ink separation is made. No “2027” in the main lockup (it dates the leftover inventory); a small year can live on a hangtag graphic, not the print.

**Do.** Keep it evergreen, funny, and on-model with Snow Day / Santa Paws. A digital one-page “Doodle Resolutions” PDF can piggyback later (idea), but it is not required for this brief.

**Don’t.** No “Dry January” alcohol-brand parodies, no official workout-brand marks, no new-year characters from movies, no photoreal calendar apps.

---

## 3. Premium gift plan — personalized Rookie Card and “The Good Boy” tarot

**Exclude the pop-art grid** (`fureverfaces/design-pop.jpg` and `wall-pop.jpg`). This plan covers only:

- **Rookie Card** — sample art `fureverfaces/design-card.jpg`, wall concept `fureverfaces/wall-card.jpg`, tee concept `fureverfaces/tee-card.jpg`. Cream card, gold starburst, pet photo cutout, name (sample: MAC), red “ROOKIE CARD” pill, joke stats (Zoomies, Snack Detection, Comes When Called, Cuteness).
- **The Good Boy** tarot — sample art `fureverfaces/design-tarot.jpg`, wall concept `fureverfaces/wall-tarot.jpg`. Navy field, gold frame and roman numeral (sample: XIX), sunburst, pet photo, title **THE GOOD BOY**, subtitle “{Name} · bringer of joy, taker of snacks.”

Both are original layouts. Do not add Topps, Panini, Pokémon, or Rider–Waite publisher marks, holofoil brand stamps, or copies of a specific published tarot’s decorative border.

Current wall mockups are illustrated rooms with a cartoon plant (the plant covers part of the Rookie Card stats). They are not photograph-grade and should not be the paid-listing heroes.

### Printed formats

Only formats with a public Printify catalog or already-used shop reference are listed as verified. Anything else is **to verify** in the live catalog before a product is built. No prices are set here.

**Verified**

- **Gallery-wrapped canvas**, 12 × 16 in and 16 × 20 in. Already specified in `ETSY_LISTINGS.md` for cartoon wall art. Best everyday wall gift for both designs. Note the quality limit in `ORDER_RUNBOOK.md`: personalized art is generated at 640 × 800 and simply enlarged, which is “fine for a mug or ornament and soft on a 16 × 20 canvas.” Prefer **12 × 16** until the render pipeline is bumped (idea: generate at 2400 × 3000 or larger, which the runbook already does as a second step — confirm the upscale is not just a stretch).
- **Framed posters**, black or white wooden frames, museum-grade / archival paper. Verified from Printify’s custom posters page (`https://printify.com/custom-posters/`). Strong “ready to hang” gift, especially the tarot. Confirm exact frame sizes in the catalog before listing.
- **Acrylic prints**, including French-cleat hanging (Printify catalog product paths `/app/products/921/.../acrylic-prints/` and `/app/products/928/.../acrylic-prints-french-cleat-hanging/`; provider Acrylic Idea Factory lists multiple sizes from 12 × 12 up to 24 × 36). High-end look for the navy tarot and the yellow Rookie Card. Confirm which sizes this shop’s Printify account can actually fulfill to US addresses.
- **Acrylic sign with wooden stand**, 5.1 × 7.9 in and 7.9 × 11.8 in, 3 mm acrylic, described on Printify’s custom acrylic signs page. Excellent desk-size Rookie Card or tarot “object” — closer to a gift you set on a shelf than a poster.
- **Greeting card packs** (flat or folded; envelopes on select products). Printify documents a **5-pack multi-design** (`/app/products/1232/.../multi-design-greeting-cards-5-pack`) and packs of **8 / 16 / 24** (`/app/products/819/.../greeting-cards-8-16-and-24-pcs`). Good for a “pet card” or a short Good Boy set. These are packs; whether they arrive in a rigid gift **box** is **to verify**.
- **Aluminum / metal signs**, indoor, matte aluminum, described at `https://printify.com/custom-metal-signs/`. Usable as bold wall signage. This is a **sign** product, not a confirmed fine-art HD metal photo print.

**To verify before offering**

- **Photo Block** — named on Acrylic Idea Factory’s Printify shipping-rates page, but the exact catalog SKU and sizes were not confirmed from a full product page in this pass.
- **Boxed card set** as a single rigid-box SKU (as opposed to a card pack in a mailer).
- **Fine-art metal photo prints** that are not aluminum signs.
- Any foil, velvet, or collector-case packaging — Printify standard cartons are not gift-box retail packaging. If a “premium unboxing” is promised, it would need a verified pack-in or a separate fulfillment step, which this shop does not currently have.

**Idea (not verified as a Printify item):** a small digital-plus-print bundle (physical 8 × 10 or acrylic stand + the PDF in §3c) sold as one Etsy listing with two fulfillment paths. Only do this if Etsy/Printify can split a physical SKU and a digital file cleanly — **to verify**.

### Personalization flow

Follow the existing manual path in `skills/dropship/ORDER_RUNBOOK.md`. Do not invent a new app. Today’s steps, written as the customer-facing and studio-facing flow:

1. **Checkout.** Customer buys a format (canvas, framed poster, acrylic, etc.) and enters **pet name** plus uploads a **pet photo**. (The Shopify ready-made merch path in `ADS_READY.md` currently says “no custom art and no photo upload.” That is a conflict: personalized Rookie Card / tarot cannot launch on a storefront that cannot collect a photo. See problems.)
2. **Studio.** Download the photo and name. Cut the pet out (`rembg`, model noted in the runbook). Drop the cut-out and the name into the HTML template for Rookie Card or tarot. Do not run the “Royal / Santa Paws” image-to-image style on these two — the samples are photographic cut-outs on designed frames, not restyled cartoons.
3. **Stats and lines.** Rookie Card: keep the four stat labels; idea — let the customer optionally set the four numbers, otherwise use a funny default set (the sample uses 99 / 100 / 12 / 100). Tarot: customer supplies the name; subtitle can stay “bringer of joy, taker of snacks” or accept a short custom epithet (character limit, idea: 40 characters). Roman numeral can stay XIX or be a harmless chosen number; do not imply a licensed deck’s numbering system as a selling point.
4. **Proof.** Email a proof from the store inbox. Free edits until approval. Nothing prints until the customer says yes. This is already in `fureverfaces/policies.md`.
5. **Print.** Manual Printify order, US provider, approved file placed on the chosen blank, then tracking pasted back into Shopify or Etsy.
6. **Time.** Timed test on 14 November 2026 (Mac, Royal style — a different style) was 3.6 minutes of machine time plus an estimate of about 10 minutes of human work. Proof email, Printify order, and fulfilment were **not** timed. Plan more than that for a new template until it is rehearsed.

Name on the card should be set in the existing heavy grotesque (Rookie) or the gold serif title face (tarot), never in a customer-uploaded font.

### Packaging and presentation

What Printify will actually ship is provider-standard (bag, box, or mailer). Do not promise a collector tin.

**Idea, if a pack-in is possible later:** a one-color belly band or card that says “FurEver Faces — The Doodle Shop” and “Proof approved {date}, printed for {Name}.” Until that exists, presentation is on the product and in the listing photography: real (or carefully mocked) framed tarot on a shelf, Rookie Card acrylic stand on a desk, canvas hung without the cartoon plant covering the stats.

Shoot new heroes the same way as §1: Printify or a real frame for on-product truth; one real interior for thumbnail. Retire `wall-card.jpg` / `wall-tarot.jpg` as listing thumbnails.

### 3c. Digital PDF after the 5 December shipping cutoff

From 5 December 2026, physical Christmas delivery is no longer a safe promise (`ADS_READY.md`, listing copy). Personalized art can still be a gift if it is delivered as a file.

**Offer (idea, not yet built):** an instant-download PDF of the approved Rookie Card or The Good Boy tarot, sold as its own digital listing and/or offered as a backup to anyone who misses the ship-by date.

- Pages: (1) a cover with FurEver Faces + the pet’s name, (2) an 8 × 10 in print page, (3) an 11 × 14 in print page, (4) a simple “print at home as a folded card” page (front / back), (5) a one-line thank-you / personal-use license. Optional 16 × 20 page only if the source render is sharp enough.
- Deliver after the same proof-approval step, or generate a preview watermarked and release the clean PDF on approval — do not auto-send a raw first draft.
- Promote from 5 December on the physical listings (“missed the ship-by date? get the printable today”) and on the shop home. This is the post-cutoff gift path, not a replacement for the premium physical formats above.

---

## 4. Printable cover fixes

These files live on `mooneyn60-art/skills`, branch `claude/youtube-monetization-strategy-m9vz6i`. There is no `SKILL.md`. Covers are generated by `skills/etsy-factory/scripts/factory/kit.py` (`Doc.cover`) and listing images by `skills/etsy-factory/scripts/factory/images.py` (`image_cover`). Neither writes a shop name. The PDF author is hardcoded as “Original printable design.”

### Files to change (actual names)

**Christmas Bingo**

- PDF covers (page 1 of): `skills/etsy-factory/products/christmas-bingo/christmas-bingo-letter.pdf`, `christmas-bingo-a4.pdf`
- Preview of that page: `.../christmas-bingo/preview/page-01.png`
- Etsy listing image 1: `.../christmas-bingo/images/01-cover.jpg` (also `02-inside.jpg` … `05-how.jpg`)

**Christmas Word Search Large Print**

- `.../christmas-word-search-large-print/christmas-word-search-large-print-letter.pdf`, `christmas-word-search-large-print-a4.pdf`
- `.../christmas-word-search-large-print/preview/page-01.png`
- `.../christmas-word-search-large-print/images/01-cover.jpg`

**Same problem, same fix, other pairs**

- Thanksgiving Bingo: `products/thanksgiving-bingo/thanksgiving-bingo-letter.pdf`, `thanksgiving-bingo-a4.pdf`, `preview/page-01.png`, `images/01-cover.jpg`
- Thanksgiving Word Search: `products/thanksgiving-word-search-large-print/thanksgiving-word-search-large-print-letter.pdf` (and `-a4.pdf`, `preview/page-01.png`, `images/01-cover.jpg`)
- Also add the shop name (but not a bingo/word-search split) to `products/christmas-would-you-rather/` and `products/large-print-word-search-seniors/` covers (`images/01-cover.jpg` and their `preview/page-01.png`).

Themes in `kit.py`: Christmas uses `primary="#1F4D3A"`, `secondary="#B23A3A"`, `accent="#C9A227"`, `paper="#FBF6EC"`, ornament `snowflake`. Thanksgiving uses leaf ornaments and rust/olive. Both bingo and word-search products **share the same theme**, so the covers are almost twins.

### What is wrong (observed)

- **No shop name** on the PDF title page or on `01-cover.jpg`. The listing headline is only the product title (“Christmas Bingo” / “Christmas Word Search”).
- **Bingo vs word search are not distinct at a glance.** Christmas pair: same cream ground, same scattered snowflakes, same Young Serif + Bricolage lockup (green first line, red second line), same gold double-rule frame, same three green pills, same red “INSTANT DOWNLOAD” badge, same fanned-page composition. Only the words and the peeking interior pages differ. Thanksgiving bingo vs word search repeat the same issue in rust/olive.
- In a grid thumbnail, a buyer can easily open the wrong listing.

### Fix A — Shop name on every cover

Add a small, consistent lockup to **both** the PDF page 1 (`Doc.cover` in `kit.py`) **and** the 2000 × 2000 listing image (`image_cover` in `images.py`), so the download matches the thumbnail.

**Which name.** These printables are generic party/senior puzzles, not doodle merch. Putting “The Doodle Shop” on a large-print senior word search would be confusing. Use the **actual Etsy shop the file will be sold under**. If that is FurEver Faces, set the lockup to **FurEver Faces** in the wordmark berry or in theme ink,  optionally with a very small “Printable games” descriptor — not “The Doodle Shop.” If they will be sold on PrintanPress, use that name instead. Do not invent a third brand. Confirm the shop before typesetting; this is an identity conflict already sitting in the repos.

**Placement (same on all products):** a single line at the **top** of the PDF frame, above the ornaments, and a matching line at the **top** of `01-cover.jpg` (or just under the outer margin, above the big title). Example treatment: small caps or Work Sans Bold, letter-spaced, in `ink` (`#1E2A24` for Christmas, `#3B2A20` for Thanksgiving, `#1D2433` for seniors). No large logo medallion that fights the title. Repeat a still-smaller name in the PDF footer on inside pages (idea) so printed tables at a party still carry the shop.

### Fix B — Make bingo vs word search visually distinct

Keep the same type families (Young Serif display, Bricolage / Work Sans UI) so the catalog still looks like one maker, but change **structure, color emphasis, and icon** so the genre is obvious at 200 px.

**Bingo covers** (Christmas and Thanksgiving):

- **Layout:** Lean into the grid. Behind or beside the title card, show a **5×5 bingo card** as the dominant silhouette (the peeking pages already do this faintly — make it the left-hand hero, larger, with a visible B-I-N-G-O header row). Title card can shift slightly right or sit on top of one card, not a perfectly symmetric fan of three identical frames.
- **Color:** Keep forest/red for Christmas, rust/olive for Thanksgiving, but give bingo a **solid dark header bar** (Christmas: `#1F4D3A`; Thanksgiving: `#9C4A26`) with the title in cream `#FBF6EC`. This reads as a “game board.”
- **Icon:** A simple original **bingo ball** or a 5×5 grid mark beside the title, and in the “INSTANT DOWNLOAD” badge. Do not use a licensed lottery or TV-bingo logo.
- **Title treatment:** One line “Christmas Bingo” (or stacked “Christmas” / “Bingo”) with **Bingo** in the display serif, larger than the event name. Subline stays “30 unique cards + calling cards.” Pills can stay, but one pill should say “BINGO” in a distinct shape (rounded square, not the same capsule as word search).

**Word search covers:**

- **Layout:** Lean into the **letter grid**. One peeking page should be a large, sharp fragment of the 15×15 puzzle (already true in the current Christmas word-search `01-cover.jpg` — push it further: bigger grid, fewer competing snowflakes). Title card can be narrower, like a bookmark over the grid, or placed at the top with the grid filling the lower two-thirds.
- **Color:** Invert the emphasis. Christmas word search: **cream title on a deep forest panel is reserved for bingo**; word search stays cream paper but uses **red `#B23A3A` as the main title color** and forest only for small labels. Thanksgiving word search: title in olive `#6B7A3A` with rust only for accents — the opposite of bingo’s rust header.
- **Icon:** An original **magnifying glass over a letter grid**, or a simple “ABC” block, used in the badge instead of the same roundel as bingo. Seniors word search can keep this icon and add “LARGE PRINT” as a wide banner, not a tiny pill.
- **Title treatment:** “Christmas Word Search” with **Word Search** as the dominant line; the words “Large Print” as a clear yellow-gold (`#C9A227`) bar under the title, not only a pill. Subline stays puzzle-count + answer keys.

**Shared rules for both types:** keep US Letter + A4 in the footer strip; keep “instant download.” After the change, a buyer should identify the genre from the silhouette and the header color alone, without reading the title. Rebuild `images/01-cover.jpg` and `preview/page-01.png` from the new PDF so they cannot drift apart.

---

## 5. Logo fix — “The Doodle Shop” contrast

### Files inspected

| File | Use | Tagline contrast |
|---|---|---|
| `fureverfaces/logo/mac-shopify-logo.png` (1400 × 360, **black** background) | Shopify / dark header | **Fails.** This is the problem file. |
| `fureverfaces/logo/mac-banner.png` (1600 × 400, cream banner) | Light banner | Tagline “THE DOODLE SHOP” is fine; the smaller descriptor is weaker but still AA for normal text. |
| `fureverfaces/logo/mac-icon.png` (1000 × 1000, circular, cream) | Icon / avatar | “THE DOODLE SHOP” in black on cream is fine. Note: the arc reads **FUREVER FACES** (all caps), not the camel-case **FurEver Faces** used on the banner. |
| `fureverfaces/logo/mac.png` | Doodle mascot only, no type | N/A |

### Colors actually in the files (sampled)

| Token | Hex | Where |
|---|---|---|
| Black background | `#000000` | Shopify logo (dominant fill) |
| Wordmark berry (mode of solid title fill) | `#C2185B` | “FurEver Faces” on the black logo and the cream banner |
| Tagline, dark (mode of non-black tagline pixels on the Shopify file) | `#14100E` | “THE DOODLE SHOP” on black — and, at `#14110F`, the same line on the cream banner |
| Banner / icon cream | `#FFF2DE` (banner field mode); corners also `#FFE3BD`; icon field `#FFF3E0` / `#FFD9A8` | Light lockups |
| Banner descriptor (mean of the “Funny tees…” line) | about `#665641` | Line under “THE DOODLE SHOP” on `mac-banner.png` |

### Computed contrast ratios

WCAG 2 AA is **4.5:1** for normal text and **3:1** for large text (18 pt or 14 pt bold and up). AAA is **7:1** / **4.5:1**.

| Pair | Ratio | AA normal | AA large | AAA normal | AAA large |
|---|---:|---|---|---|---|
| **Current tagline `#14100E` on Shopify black `#000000`** | **1.11:1** | Fail | Fail | Fail | Fail |
| Same tagline, median sample `#14110F` on `#000000` | 1.12:1 | Fail | Fail | Fail | Fail |
| Wordmark `#C2185B` on `#000000` | 3.58:1 | Fail | Pass | Fail | Fail |
| Descriptor `#665641` on cream `#FFF2DE` (banner only) | 6.39:1 | Pass | Pass | Fail | Pass |
| Tagline `#14110F` on cream `#FFF2DE` (banner / icon) | 17.02:1 | Pass | Pass | Pass | Pass |
| Wordmark `#C2185B` on cream `#FFF2DE` | 5.32:1 | Pass | Pass | Fail | Pass |

The almost-invisible line is specifically **“THE DOODLE SHOP” on `mac-shopify-logo.png`**. At 1.11:1 it is barely a vibration in the black, not readable type. The cream banner and the circular icon do not have this bug. A secondary issue: the berry wordmark on black (3.58:1) is acceptable only if that wordmark is treated as **large** text; it fails AA for normal-sized type.

### Concrete fixes (in preference order)

**1. Preferred — light tagline on the black logo, no other redesign.**  
On `mac-shopify-logo.png` only, change “THE DOODLE SHOP” from `#14100E` to:

| New tagline on `#000000` | Ratio | AA / AAA |
|---|---:|---|
| `#FFFFFF` | 21.00:1 | AAA normal and large |
| `#FFF2DE` (banner cream, recommended for brand consistency) | 19.01:1 | AAA normal and large |
| `#F0C088` (peach sampled from the mascot fur) | 12.60:1 | AAA normal and large |

Use **`#FFF2DE` at the same weight and tracking as today.** Do not lighten the tagline by “adding opacity of white over black” without checking the result — the current color is already a near-black brown and is why it fails.

**2. Alternate — keep dark type, change the ground.**  
Place “THE DOODLE SHOP” on a cream pill or a full cream bar (`#FFF2DE`) and keep `#14110F` type (17.02:1, AAA). This also works if the header behind the logo is not always pure black.

**3. Do not** “fix” the tagline by painting it in the current berry `#C2185B` on black (3.58:1 — still fails AA normal, and would merge visually with the wordmark).

**4. Optional wordmark tweak, black backgrounds only.**  
If the Shopify header ever renders “FurEver Faces” below large-text size, bump the berry on **black only** to `#CA4077` (4.51:1, AA normal pass). Do not use `#CA4077` on the cream banner — that pair is 4.21:1 and **fails** AA normal. Keep `#C2185B` on cream (5.32:1). Two context-specific berries are better than one hex that fails on one of the grounds.

**5. Banner descriptor (optional, not the assigned bug).**  
“Funny tees and gifts for people owned by a doodle” at `#665641` on `#FFF2DE` is 6.39:1 (AA pass, AAA fail). To hit AAA normal (7:1), darken toward `#1A1A1A` (15.75:1) or at least the tagline brown `#14110F` (17.02:1).

**6. Consistency idea.**  
Use **FurEver Faces** (camel case) on the circular icon as well as the banner, so the shop name does not appear as two different trademarks.

Export a corrected `mac-shopify-logo.png` at 1400 × 360 (and a 2×) after the type change; do not ship a new mascot for this fix.

---

## Appendix — problems found in this pass

These are observations for the team, not changes made to any repo.

1. **Missing skill file:** `skills/etsy-factory/SKILL.md` is not on branch `claude/youtube-monetization-strategy-m9vz6i`.
2. **Empty notebook repo:** `mooneyn60-art/Side-hustles` is an empty public repo (created 15 November 2026); no `etsy-shop/TASKS.md` or backlog.
3. **No FurEver Faces README or design brief** in `fureverfaces/`; `policies.md` still has “December [DATE]” while ads and listings say 5 December.
4. **Conflicting product models** across dropship docs: `ADS_READY.md` describes a password-gated Shopify shop with four ready-made products and **no photo upload**; `ORDER_RUNBOOK.md` describes a personalized photo-to-art flow with proof emails; `ETSY_STATE.md` lists a much larger Etsy/Printify catalog including bandanas and tanks. Personalized Rookie Card / tarot cannot check out until a storefront actually collects a name and photo.
5. **Mockup quality:** merch mockups are flat “concept images”; wall art concepts are illustrated interiors that crop or cover card stats; the matching-set ad uses a photoreal tee on a person but a flat dog tank, and it is not a bandana set.
6. **Printable brand and genre:** no shop name on covers; Christmas (and Thanksgiving) bingo vs word search share one template and are hard to tell apart in a grid; PDF author is a generic string.
7. **Logo:** `mac-shopify-logo.png` tagline is 1.11:1 on black; circular icon spelling does not match the banner wordmark.
8. **Pipeline quality note (already in the runbook):** personalized renders start at 640 × 800 and are enlarged; soft on 16 × 20 canvas.
9. **Public operational identifiers:** `skills/dropship/ETSY_STATE.md` on a public fork contains Etsy shop id, Printify store ids, a long list of Printify product ids, and a Make.com scenario id. No API tokens or passwords were found in the files read for this assignment. Those identifiers are not copied here; consider whether they should live in a public repo.
10. **Missing local mockups** for Snow Day / Doodle Mom / Doodle Dad ornaments, even though Printify product ids for those ornaments are listed in `ETSY_STATE.md`.

No secrets were copied out of the repos. No commits, publishes, prices, or purchases were made.
