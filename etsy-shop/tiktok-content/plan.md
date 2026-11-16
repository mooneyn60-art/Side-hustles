# FurEver Faces TikTok plan: @fureverfaces (shop marketing)

Owner: Etsy Studio. Written Sun Nov 15, 2026 (ET). Status: **7 videos rendered; Metricool queueing
BLOCKED on media hosting (details below). Nothing posted, scheduled, published or uploaded.**
Separate from Social Studio and the Meatball Myths channels: no Meatball branding, characters, voice
or footage. Everything sends people to the FurEver Faces Etsy shop and Shopify store
(egayix-ff.myshopify.com).

## 1. Formats
Full specs, with hooks, caption templates, hashtags, audio and CTA, are in `formats.md`.

| # | Format | Best for |
|---|---|---|
| F1 | Product mockup slideshow | One hero product per video |
| F2 | "Gift for the doodle mom/dad" POV | Mom and Dad tees, mugs, ornaments |
| F3 | Matching set reveal (tee + dog bandana) | Santa, Mom and Dad sets; always "sold separately" |
| F4 | Christmas order-by reminder (plain facts) | Nov 23 to Dec 5 |
| F5 | "Which one is your doodle?" picks | Comment bait without fake urgency |
| F6 | Doodle-parent translation | Evergreen after Dec 5 and into Valentine's |

Rules on every post: no audio in the file (Commercial Music Library or original audio, added in the
TikTok app), "Your brand" promotional disclosure on, the AI-generated label on, and an "art made with
AI tools" footer and caption line. The CTA is "Link in bio" (our shop + Etsy). Never "free shipping,"
fake reviews or scarcity, mismatched prices, or a QR code or coupon aimed at Etsy buyers. The week-1
videos show no prices at all.

## 2. Cadence
I checked Metricool's best time to post for TikTok (brand 8135499, Nov 16–22, America/New_York). The
account was only connected today, so this is likely Metricool's general TikTok curve rather than our
own audience:
- **Peak:** 10:00 ET every day. Wed–Thu are strongest (about 1430–1470); Sat–Sun are weakest (about
  820–850).
- **Second peak:** 18:00 ET (about 1100–1390 on weekdays), then 12:00.
- **Dead zone:** 01:00–05:00.

Proposal:
- **Nov 17 to Dec 5: 1 post a day, 19 posts.** 10:00 ET by default, with 18:00 ET on two weekdays a
  week to test the evening peak. Mix: F1 ×5, F3 ×4, F5 ×3, F2 ×3, F4 ×4 (Nov 23, Nov 28, Dec 2, Dec 5).
- **Dec 6 to Dec 31: 3 a week** (Mon, Wed, Fri at 10:00 ET). Use F6 evergreen plus honest "it'll
  arrive after Christmas, still a great gift" posts. Never imply Christmas delivery after Dec 5.
- **January: 3 a week**, moving to the Valentine's line (`etsy-shop/ads/valentines-plan.md`).
- After 2 weeks, re-check Metricool analytics for our actual best hours and the top format, then
  double down.

## 3. Pipeline
`pipeline/` is ready to go into the repo as `etsy-shop/tiktok-content/pipeline/` (not committed). See
`pipeline/README.md`.
- `render.py <config.json> [--qa]`: one JSON or YAML config makes one 1080x1920 H.264 MP4, 7–15 s,
  30 fps, **no audio track**. It uses Pillow for layout (Ken Burns motion, crossfades, text cards
  inside the safe zone x 60–950 / y 210–1440) and ffmpeg for encoding. `--qa` writes a mid-slide frame
  for every slide plus a safe-zone overlay. `--check` validates length, image paths and banned copy
  (free shipping, scarcity, QR, coupon codes, star claims, and unverified `$` prices).
- `render_all.sh`: renders every config in parallel with QA.
- `fetch_images.py`: downloads Shopify product images from a saved read-only Shopify GraphQL result.
  The Shopify media are the Printify mockups that Printify pushed to the store.
- `configs/`: the 7 week-1 configs, plus `_make_week1.py`, which generates them.
- Sources: Shopify media in `assets/shopify/` (pulled read-only through the connector), and our art in
  `/workspace/etsy-design/christmas/{thumbnails,ornaments,lifestyle,social}`.
- No secrets anywhere. `queue/week1-metricool-review-payloads.json` has the exact
  `createScheduledPostForReview` payloads, with two placeholders: the media URL and the reviewer email.

## 4. First week (Nov 17–23)
Metricool brand **8135499** ("fureverfaces") has TikTok **@fureverfaces**. The same brand also links
YouTube channel UCw98RQD81t_339LX5EJqcrg, the former Meatball Myths channel. Every payload uses
`providers: [{"network":"tiktok"}]` only, so nothing goes to YouTube.

| Date | Time ET | Format | Product | Hook (on screen) | Caption (before AI/CTA line and hashtags) | File | Metricool status |
|---|---|---|---|---|---|---|---|
| Tue Nov 17 | 10:00 | F1 slideshow | Santa Paws ornament | "Your doodle is going on the tree this year." | He's on the nice list. Pending. 🎄 The Santa Paws ornament: a cartoon doodle in a Santa hat, on a round ceramic ornament with a ribbon. Order by Dec 5 for Christmas delivery. | `renders/2026-11-17-santa-paws-ornament.mp4` (10.6 s) | Not queued: blocked on media URL |
| Wed Nov 18 | 18:00 | F2 POV | Doodle Mom tee | "POV: she says she doesn't need anything for Christmas." | She doesn't need anything. She has a doodle. She needs this. The Doodle Mom tee: curls, cuddles & chaos, on a unisex cotton tee, S to 2XL. | `renders/2026-11-18-doodle-mom-tee.mp4` (10.6 s) | Not queued: blocked |
| Thu Nov 19 | 10:00 | F3 matching set | Doodle Dad tee + Dad's Best Friend bandana | "Matching with the dog. On purpose." | His: Doodle Dad, chief treat officer. The dog's: Dad's Best Friend. Sold separately, worn together, judged by the neighbors. | `renders/2026-11-19-doodle-dad-matching-set.mp4` (10.4 s) | Not queued: blocked |
| Fri Nov 20 | 10:00 | F5 picks | Santa Paws, Doodle Mom, Doodle Dad and Snow Day ornaments | "Which one is your doodle? Be honest." | 1 Santa Paws: nice list (pending). 2 Doodle Mom: curls, cuddles & chaos. 3 Doodle Dad: chief treat officer. 4 Snow Day: zoomies incoming. Tell us your number. 👇 | `renders/2026-11-20-which-ornament-is-your-doodle.mp4` (11.4 s) | Not queued: blocked |
| Sat Nov 21 | 10:00 | F1 slideshow | Santa Paws mug | "He's on the nice list. Pending." | For the coffee you drink while your doodle eats the wrapping paper. The Santa Paws mug, 11 oz or 15 oz, dishwasher and microwave safe. Order by Dec 5 for Christmas delivery. | `renders/2026-11-21-santa-paws-mug.mp4` (10.2 s) | Not queued: blocked |
| Sun Nov 22 | 10:00 | F3 matching set | Santa Paws tee + Santa's Favorite bandana + Santa Paws ornament | "The whole family made the list this year." | Yours: the Santa Paws tee. Theirs: the Santa's Favorite bandana. One for the tree: the Santa Paws ornament. Each sold separately. Order by Dec 5 for Christmas delivery. | `renders/2026-11-22-santa-paws-matching-set.mp4` (11.8 s) | Not queued: blocked |
| Mon Nov 23 | 18:00 | F4 order-by | Snow Day ornament, tee and mug | "Christmas order-by date: Dec 5." | Plain facts: everything is printed to order, so order by Dec 5 for Christmas delivery. After that we still make and ship it, it just may arrive after the 25th. Snow Day: zoomies incoming. | `renders/2026-11-23-order-by-dec-5-snow-day.mp4` (10.4 s) | Not queued: blocked |

Every caption ends with: "Art made with AI tools. Printed to order. Link in bio for our shop and
Etsy." followed by 3–5 hashtags, always including #fureverfaces. Full text is in each config's
`caption_full`.

QA: every slide's mid-frame was extracted (`renders/qa/<id>-sNN.jpg`) and checked by eye for typos,
safe-zone fit and covered product art. Three videos were re-rendered after fixes (a CTA card covering
a bandana, a card covering the Snow Day slogan, and a flat-lay crop cutting off "Santa Paws"). All 7
are 1080x1920 H.264 at 30 fps with a video stream only (no audio), 10.2–11.8 s long.

### Blocked: media hosting (why nothing is queued)
`createScheduledPostForReview` accepts media only as **public URLs** (or Google Drive/Dropbox links
that Metricool imports). The MP4s exist only on the box. No Drive or Dropbox connector is connected to
Grok Bot, and the Shopify connector is read-only for this task, so there is no sanctioned host. I did
not upload anywhere. Any one of these unblocks it:
1. **Shopify Files (recommended):** Moondog88 OKs uploading the 7 MP4s to the store's Files (Content >
   Files) through the Shopify connector. Shopify's CDN gives public URLs on a host we already own.
   That's a write to Shopify, so it needs his yes.
2. **Google Drive:** Moondog88 connects Google Drive to Grok Bot and links the same Drive in Metricool
   (Settings > Connections). I upload to a "FurEver Faces TikTok" folder, which needs link sharing on
   for Metricool to fetch.
3. **Manual:** Moondog88 or Jarvis drags the 7 MP4s into the Metricool planner himself. Captions and
   settings are copy-paste ready in the payloads file.

Also needed before queueing:
- **Reviewer email.** The tool requires one. The Metricool owner login on brand 8135499 is
  giannaaggie224@gmail.com. Is that Moondog88's reviewer address? Metricool emails reviewers.
- Review approval needs a Metricool plan with team management. If the plan lacks it, the tool returns
  an error and we fall back to drafts or manual upload.

Payload settings: `autoPublish: false`, so after approval Metricool sends a push to his phone to finish
in TikTok, which is where the Commercial Music Library audio gets added. `approvalSystem: any`,
`commercialContentOwnBrand: true`, `isAigc: true`, `autoAddMusic: false`, and public visibility. Never
direct-publish and never use createScheduledPost.

## 5. Needs Moondog88's okay (via Jarvis)
1. **How to host the MP4s for Metricool:** Shopify Files, Google Drive, or manual upload (see above).
2. **Reviewer email** for Metricool review (giannaaggie224@gmail.com?) and confirmation that the plan
   has team management.
3. **Approve each of the 7 queued posts** in Metricool (all held for review), then add a Commercial
   Music Library sound in the TikTok app when the push comes.
4. **The YouTube link** on Metricool brand 8135499 (UCw98RQD81t_339LX5EJqcrg, formerly Meatball
   Myths): keep it, or disconnect it from the FurEver Faces brand. We never post to it either way.
5. **Bio link on @fureverfaces:** either a link-in-bio page listing Shopify and Etsy (for example
   TikTok's own bio link, a Shopify page at /pages/links, or a Linktree-style tool), or Shopify alone
   in the bio with Etsy mentioned. TikTok may require a Business account to show a clickable website
   link. Until a bio link exists, "link in bio" doesn't work.
6. **The cadence:** 1 a day through Dec 5, then 3 a week.
7. **The AI disclosure approach:** an on-screen footer, a caption line, and TikTok's AI-generated
   label on every post.

## 6. Flags for the team
- **Santa bandana mismatch:** `etsy-shop/tiktok-shop/products.md` says the Santa Paws pet bandana
  carries the Santa Paws cartoon. The live Shopify bandana is "Santa's Favorite," with a red heart.
  The videos show the live Shopify item. Check what Etsy actually sells.
- **Etsy availability:** each SKU's Etsy availability is unverified, because products.md has no Etsy
  listing IDs. The "our shop + Etsy" CTA assumes the shown products are live on Etsy; Shopify is
  confirmed (all shown products are active there).
- **Concept images:** the Doodle Mom, Doodle Dad and Snow Day ornament images are concept images
  (each carries "Ceramic ornament · concept image"), not Printify mockups. The Shopify ornament listing
  photos are the Printify mockups. Swap them in if we'd rather not show concept art.
- **Bandana mockups:** the Printify bandana mockups with a dog show a short-haired dog, not a doodle,
  so week 1 uses the flat bandana shots only.
