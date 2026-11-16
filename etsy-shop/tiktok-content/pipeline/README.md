# FurEver Faces TikTok renderer

Turns product images into silent 1080x1920 (9:16) MP4 slideshows, 7–15 s, with
text cards kept inside TikTok's safe zone. One config file = one video.
Built for @fureverfaces only (shop marketing). No Meatball assets, characters or voice.

Repo home: `etsy-shop/tiktok-content/pipeline/` in Side-hustles.

## Requirements
- Python 3.9+ with Pillow (`pip install pillow`); PyYAML only if you use `.yaml` configs.
- ffmpeg + ffprobe on PATH.
- Fonts are bundled in `fonts/` (Poppins, SIL OFL 1.1, see `fonts/OFL.txt`).

## Run
```bash
python3 render.py --check configs/*.json          # validate length, banned phrases, image paths
python3 render.py --qa configs/2026-11-17-santa-paws-ornament.json
./render_all.sh                                    # all configs, 4 in parallel (JOBS=n to change)
```
Output goes to the config's `output` path (week 1: `../../renders/<id>.mp4`).
`--qa` also writes one frame from the middle of each slide plus a red safe-zone overlay to
`renders/qa/<id>-sNN.jpg` and `<id>-safezone.jpg`. **Look at every QA frame for typos and
covered product art before queueing.**

## How it works
1. Each slide builds a background (blurred, cream-tinted copy of the image, or a solid brand
   colour) at 108% of frame size, then places the product image (`fit: contain` inside `box`,
   or `fit: cover` full-bleed). A `images: [...]` list makes a 2- or 4-up grid with optional
   number badges (`labels`).
2. Text cards are drawn once per slide with Pillow, laid out inside the safe zone:
   x 60–950, y 210–1440 (TikTok's top tabs, right action rail and bottom caption bar stay clear).
   `top` cards stack down from the top, `bottom` cards stack up from the footer line, `middle` centres.
3. Frames are generated in Python (eased Ken Burns: `zoom_in`, `zoom_out`, `pan_left`, `pan_up`,
   `none`; 0.4 s crossfades; text fades in) and piped to ffmpeg → H.264 High, yuv420p, CRF 18,
   30 fps, `+faststart`, **no audio track** (`-an`). Add sound in the TikTok app.
4. `validate()` rejects: totals outside 7–15 s, missing images, unknown styles, and banned copy
   (free shipping, scarcity like "only N left"/"selling out"/"last chance", QR, coupon/promo code,
   star ratings, "best seller"). Any `$` price in captions or on screen requires
   `prices_verified_on` in the config (prices must match the live store that day).

## Config schema (JSON; YAML works the same)
```jsonc
{
  "id": "2026-11-17-santa-paws-ornament",        // also the output file name
  "output": "../../renders/2026-11-17-santa-paws-ornament.mp4",  // relative to the config file
  "fps": 30, "motion_scale": 1.08,
  "transition": {"type": "crossfade", "duration": 0.4},
  "footer": "FurEver Faces · art made with AI tools",   // small line on every slide
  "slides": [
    {"image": "@design/christmas/social/santa-ornament-tree-tiktok-1080x1920.jpg",
     "fit": "cover", "focus": [0.5, 0.5], "duration": 3.0, "motion": "zoom_in",
     "texts": [{"text": "Your doodle is going on the tree this year.", "style": "hook"}]},
    {"image": "@assets/shopify/santa-paws-goldendoodle-christmas-ornament-1.jpg",
     "box": [60, 360, 1020, 1240], "bg": "blur", "duration": 2.8, "motion": "zoom_out",
     "texts": [{"text": "Santa Paws ornament", "style": "hook"},
               {"text": "Nice list (pending).", "style": "body", "position": "bottom"}]},
    {"images": ["a.jpg", "b.jpg", "c.jpg", "d.jpg"], "labels": ["1","2","3","4"],
     "box": [60, 470, 1020, 1350], "duration": 3.2, "texts": [...]}
  ],
  // planning fields (ignored by the renderer, used by plan.md / Metricool queue):
  "post_date": "2026-11-17", "post_time_et": "10:00", "format": "F1 ...", "product": "...",
  "hook": "...", "caption": "...", "hashtags": ["#goldendoodle", "..."], "caption_full": "...",
  "tiktok": {"commercialContentOwnBrand": true, "isAigc": true, "privacyOption": "PUBLIC_TO_EVERYONE"}
}
```
- Image refs: local path (relative to the config), `@design/...` (default `../../etsy-design`,
  override with `FF_DESIGN_ROOT`; in the repo point it at `etsy-shop/design`), `@assets/...`
  (default `../assets`, override `FF_ASSETS_ROOT`), or an `https://` URL (Shopify CDN / Printify
  mockup), cached in `.cache/` (git-ignored).
- Text styles: `hook` (black on white), `body`, `cta` (cream on berry #C2185B), `fact`
  (cream on forest #1F4D3A), `small`. Optional per-text `size`, `color`, `card`. Use `\n` to force breaks.
- Slide length 2.4–3.2 s reads well; 4–5 slides lands at 10–12 s.

## Getting product images
- Shopify (read-only through the Shopify connector): run the GraphQL query in `fetch_images.py`'s
  docstring, save the JSON, then `python3 fetch_images.py that.json --out ../assets/shopify`.
  Shopify media for these products are the Printify mockups Printify pushed to the store.
- Our own art: `etsy-design/christmas/{thumbnails,ornaments,lifestyle,social}` and `branding/`.
- No tokens or secrets live in this folder. Do not add any.

## Automating it (Claude or Etsy Studio)
1. Copy a week-1 config, change images/text/date. Or edit `configs/_make_week1.py` and re-run it.
2. `./render_all.sh configs/<new>.json`, then review the QA frames.
3. Queue in Metricool **for review only** (`createScheduledPostForReview`), never direct publish.
   Metricool's API takes media as a **public URL**, so the MP4 must be hosted somewhere Metricool
   can fetch it first (see `../plan.md`, "Blocked: media hosting").
