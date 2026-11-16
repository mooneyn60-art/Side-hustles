# Meatball Myths: pet-POV visual kit v1

Status: **draft for Social Studio to review and commit.** Intended repo path: `channels/animation/kit-v1.md`. Box copy: `/workspace/animation/kit-v1.md`. Written Mon Nov 16, 2026 (ET). Nothing here was committed, pushed, rendered or posted.

Scope: the new pet-POV story long-forms (born-as and survival stories told from the pet's point of view), plus their 9:16 crops. The spoken voice, facts, safety lines and script rules stay as they are in `channels/meatball-bible.md` and the fact-checked scripts. This kit covers only how things look and move.

## 0. Source labels (read first)

Every spec line carries one of these tags:

- **[REPO]**: stated in `mooneyn60-art/side-hustles` (main, commit `77f687b`, Nov 16 2026 17:41 ET). File named next to it.
- **[BOX]**: an existing house asset or code on the shared box that is **not in the repo** (Jarvis's `meatball-animation-v2/` rig and art, the v6/v6b thumbnail drafts, the pfp drafts, the read-only copy of Claude's `oh-meatball` tools). Path named next to it.
- **[SAMPLED]**: a color I measured off one of those existing images. It matches the art but is not written down anywhere as a brand value.
- **[DERIVED]**: my own spec, written to match the existing look. Treat it as a proposal.
- **[PROPOSED – NEEDS APPROVAL]**: a design that does not exist yet (Noodle's and Sauce's cartoon model sheets).

What the repo has and doesn't have: `channels/` has **no image files at all**: no thumbnails, no pfp, no character art, and no style guide that describes how Meatball looks. The repo describes who Meatball, Noodle and Sauce are and how they act (`meatball-bible.md`, `shorts-push-1116/gags-1116.md`). It also has the renderer color configs for the generic dog and cat in the v6 pet Shorts (`scripts/dogs-lick-v6-yt.json`, `scripts/cats-knead-v6-yt.json`). Everything visual about the **cartoon Meatball** below comes from the box assets, so it is tagged [BOX] or [SAMPLED].

---

## 1. Character sheet spec

### 1.1 Meatball (lead): existing on-model look

**Canonical references (use these, nothing else):**
- `meatball-animation-v2/mb2/art/meatball_ref_sheet_v1.jpg`: 10-pose cartoon ref sheet [BOX]. Copy: `/workspace/animation/refs/meatball_ref_sheet_v1.jpg`
- `meatball-animation-v2/mb2/characters.py`: Jarvis's v2 puppet rig. Its palette and line weights are "sampled from art/meatball_ref_sheet_v1.jpg" (code comment) [BOX]
- v6b thumbnail sprite `drafts/thumbs-v6-1116/_work/mb-v6b-cH3HCZ8GlHk.png` and sheet `before-after-sheet-v6b.png` ("v6b SAMPLE (not live)") [BOX]. Copies are in `/workspace/animation/refs/`
- Cartoon pfp draft `drafts/meatball-pfp-v2-1116/pfp-final-c.png` [BOX]
- Rig render `meatball-animation-v2/work/character_ref.png` and panel art `mb2/art/p4_playdead_v2.jpg` [BOX]

**Silhouette.** One round, slightly lumpy ball (an 18-point wobble of ±3.5% on the radius in the rig) [BOX characters.py]. A glossy red tomato-sauce cap sits on the top third, and **3–5 drips** run down over the forehead [BOX ref sheet, rig]. Thin black stick arms and legs, with **solid black ball hands** and **solid black oval feet** [BOX]. No neck, no nose, no ears, no clothes by default. The silhouette has to read as a ball with a red top even at 168 px. The repo's thumbnail rule says a small Meatball turns into a "brown dot" (`packaging/thumbnail-concepts.md`, `thumbnail-spec-two-styles-1115.md`) [REPO].

**Proportions** (rig units: body radius r = 100) [BOX characters.py]:
| Part | Value |
|---|---|
| Body | circle r = 100 (lumpy) |
| Sauce cap | top ~35% of the body (y −108 to about −40), drips reach eye-brow level |
| Eyes | two tall ovals, half-width 27 × half-height 32 (shock 31 × 38), centers at x ±34, y −14 (they nearly touch the brow line) |
| Pupils | round, r 12 (shock 8), white catchlight r 3.5 offset up-left |
| Brows | one thick dash per eye, 44 wide, sitting on the sauce or just under it |
| Mouth | centered at y +44 |
| Legs | from y +92, two segments 75 + 70, stroke 9, oval foot r 26 |
| Arms | from body sides (x ±84, y +20), two segments 72 + 66, stroke 8.5, ball hand r 15 (fists r 21) |
| Standing height | about 2.6 r from the top of the cap to the soles |

**Palette.** Rig values, sampled from the ref sheet by Jarvis [BOX characters.py]:
| Role | Hex | Tag |
|---|---|---|
| Body brown (base) | `#6e3d22` | [BOX] |
| Body shadow (lower-right) | `#4a2715` | [BOX] |
| Body light (upper-left) | `#8f5534` | [BOX] |
| Specks | body shadow tone at ~90% opacity, 14 dots | [BOX] |
| Highlight blob, upper-left | `#b07448` at ~60% | [BOX] |
| Sauce top / bottom gradient | `#e8392e` → `#9a1a14` (mid value `#d42a22`) | [BOX] |
| Sauce gloss | white at ~75%, small oval upper-left of the cap | [BOX] |
| Ink (outlines, limbs, pupils) | near-black. The rig `INK` comes from `kit.py`. Claude's older `mascot.py` uses `#111111` | [BOX] |
| Eye whites | `#ffffff` | [BOX] |
| Open mouth / tongue | `#5a0f0f` / `#e2595a` | [BOX] |
| Sweat drop | `#8fd3ff` (the v6b sprite measures `#80cffd`) | [BOX] / [SAMPLED] |

**Line and shading.** Silhouette outline **~11 px**, interior lines (eyes, mouth, sauce edge) **~7 px** at 1080-px frame width, kept constant on screen whatever the scale [BOX characters.py `OUT_PX`, `IN_PX`]. Flat fill plus one soft radial shade: light upper-left, one shadow tone lower-right [BOX]. No hatching and no texture beyond the specks. Rounded joins and caps everywhere [BOX `drawn_kit.py` docstring].

**Expressions (10).** The first 8 are the rig's named `FACES` [BOX characters.py]. 9–10 are on the ref sheet and in the v6b thumbs [BOX]:
| # | Name (file key) | Eyes | Brows | Mouth | Extras |
|---|---|---|---|---|---|
| 1 | `neutral` | open ovals, pupils centered | flat | small smile curve | – |
| 2 | `shock` | ovals bigger, pupils small | raised, inner ends up | open O | arms up, sweat drop |
| 3 | `scared` | open, pupils small | inner ends way up | wobbly open frown | 1–3 sweat drops |
| 4 | `determined` | open | inner ends down | flat, slight frown | fists |
| 5 | `smug` | half-lidded | slightly lowered | lopsided smirk | pupils pushed to one side (v6b "smug") |
| 6 | `hurt` | squeezed shut `> <` | inner ends up | open, wavy | – |
| 7 | `happy` | open, or closed arcs for big laughs | raised | big open grin, tongue showing | – |
| 8 | `angry` | open | steep V | down-curve | fists up |
| 9 | `side-eye` | pupils parked hard to one side | one brow tilted | flat | v6b "sideeye" thumb |
| 10 | `dizzy` | spirals (ref sheet) or X eyes (rig `dizzy`) | worried | wobbly | after impacts only |

Expressions **snap** between clean drawings and are never morphed through ugly in-betweens. That is the house rule in Claude's `mascot.py` docstring (research/41) [BOX].

**Turnaround views needed** [DERIVED]: front, 3/4 left, 3/4 right (mirror is fine), side profile (the eyes slide toward the facing side, the far eye shrinks to a sliver, and the drips follow the curve), back (sauce cap from behind with no drips, plain brown ball, limbs only), top-down (red disc with drips at the rim, for the cat's-eye high shots).

**Poses needed:**
- Already in the house rig [BOX characters.py / mascot.py]: stand, run cycle, arms up, fists, behind-neck, point, kick, flat legs (lying), present, shrug, think, wave, facepalm.
- New for pet-POV [DERIVED]: crawl on all fours with cardboard ears (born-as, `longform/dog-bornas-revision-1116.md` s1.l2 "the guy in the cardboard ears" [REPO]), curled asleep in a pet bed, belly slide, hanging from a counter edge by one hand, squashed flat, peeking around a door frame, sitting in a cardboard box.

**Do:**
- Keep the red cap and drips in every frame. They are the brand detail (Claude's `mascot.py` comment, "the brand detail") [BOX].
- Make Meatball large in any thumbnail (≥ 35% of frame height) or leave him out [REPO `thumbnail-spec-two-styles-1115.md`].
- Keep everything drawn. No real photos or footage (`meatball-bible.md`, MASTER_ORDERS "keep it all drawn" in `tiktok-shop/launch-plan.md`) [REPO].
- Act gags with the body, at home, with household props [REPO `gags-1116.md`].

**Don't:**
- Don't mix this ball look with the older **stick-figure "Meatball 2.0" rig** (small head on a long stick body, parsley fleck on the cap, `skills-readonly/.../tools/mascot.py`). That is what the box's `pubcheck/pfp.jpg` shows (copy: `refs/pfp.jpg`) [BOX]. One look per video.
- No nose, no teeth, no clothes, no extra sauce colors, and no parsley fleck on the ball look.
- Don't put Meatball in a shot with a real dangerous animal, and never touch a spider or bug [REPO `gags-1116.md`].
- No team marks, logos or uniforms (`packaging/thumbnail-concepts.md` §3) [REPO]. No copyrighted characters. Don't copy other creators' designs: the competitor clips in `meatball-animation-v2/ref/comp_*.mp4` are for pacing study only [BOX].

### 1.2 Noodle, his dog: no cartoon model exists. [PROPOSED – NEEDS APPROVAL]

**What exists:**
- Identity and behavior: Meatball's dog. He "ends up with Meatball's food or prop", always as an action on screen, "never a feeling or motive said as fact" [REPO `meatball-bible.md`]. He's referred to as "him" and wears a **collar** [REPO `gags-1116.md` #3]. He can stand on his hind legs and has worn a holiday bandana [REPO `tiktok-shop/launch-plan.md`].
- Color/shape: the v6 pet Shorts in which Noodle is the gag dog render a generic dog with `color #c8743c`, `dark #8f4f24`, `belly #f1dcc0`, `ears: floppy`, `tail: thin`, `whiskers: false`, `mood: happy` [REPO `scripts/dogs-lick-v6-yt.json`, `chocolate-v6-yt.json`, `tt-dogs-lick.json`]. That is the drawn-house renderer, not the cartoon ball style. The config is labeled "dog", not "Noodle".
- **No breed, size, markings, collar color or cartoon drawing is defined anywhere.**

**Proposed spec** (restyles the existing renderer colors into Meatball's style):
- Silhouette: chunky bean-shaped body, short sturdy legs with rounded paws, big head (about 40% of body length), long floppy ears that hang to the jaw, thin tail. Readable as "dog" from the side silhouette alone. [PROPOSED]
- Scale: Meatball's standing height ≈ Noodle's shoulder height, so Noodle can carry Meatball's props, and Meatball, in his mouth. [PROPOSED]
- Palette: coat `#c8743c`, shade `#8f4f24`, belly/muzzle `#f1dcc0` (all [REPO] renderer values). Ears a darker brown in the shade tone. Nose and outlines ink. Collar: plain red, no text and no logo, with a round silver tag. [PROPOSED]
- Line/shading: the same ~11 / ~7 px outline weights, flat fill and single shade tone as Meatball. [PROPOSED]
- Eyes: **same eye design as Meatball** (white ovals, round pupils, catchlight, dash brows) so the cast matches. [PROPOSED]
- Expressions (8): `happy` (repo mood), `alert` (ears up, head tilt), `sniff` (nose down, eyes half shut), `mouth-full` (prop in mouth, tail up), `zoomies` (ears flying, tongue out), `sleepy` (curled, eyes closed), `guilty-look` (eyes side, ears back; drawing only, never captioned as guilt), `startled` (big eyes, ears up). [PROPOSED]
- Turnaround: front, 3/4, side, back, plus a **low front "looming" view** for the cat's-eye and Meatball-scale shots. [PROPOSED]
- Poses: walk, trot, run (gallop cycle), sit, lie down, hind-leg stand, carry-in-mouth, play bow, sniff walk. [PROPOSED]
- Concept image (proposed only): `/workspace/animation/PROPOSED-noodle-sauce-concept-v1.jpg`. It shows Meatball about the dog's height, larger than the proposed scale.

### 1.3 Sauce, his cat: no cartoon model exists. [PROPOSED – NEEDS APPROVAL]

**What exists:**
- Identity and behavior: Meatball's cat. She "does the opposite of what Meatball wants and walks off", acted, never stated as a feeling or motive. Tag line "Sauce walked off." [REPO `meatball-bible.md`]. Referred to as "her" ("Sauce flattens her ears"). She swats, bats, paws and tips props over [REPO `gags-1116.md` #2, #4, #5, #6, #7, #11, #12]. Shown asleep on the pad [REPO `scripts/longform-dog-bornas.json` pinned comment].
- Color/shape: the v6 cat Shorts render a generic cat with `color #e39a4a`, `dark #b06f2a`, `belly #f6e3c8`, `ears: pointed`, `tail: thin`, `whiskers: true`, `mood: smug` [REPO `scripts/cats-knead-v6-yt.json`, `cats-turkey-v6-yt.json`]. That is the drawn-house renderer, and the config is labeled "cat", not "Sauce".
- **No markings, size or cartoon drawing is defined.** Note: the orange house cat in the v6 "RAW DEAL?" thumbnail (`viD-nbPdaxk`) is the long-form's subject cat, not Sauce [BOX].

**Proposed spec:**
- Silhouette: compact rounded body, triangle ears, thin upright tail with a slight hook, whiskers. Clearly paler and yellower than Noodle so the two never merge at small sizes. [PROPOSED]
- Scale: sitting height ≈ Meatball's standing height. [PROPOSED]
- Palette: coat `#e39a4a`, shade `#b06f2a`, chest/belly `#f6e3c8` ([REPO] renderer values). Inner ears pink. No collar, so she reads differently from Noodle. [PROPOSED]
- Line/shading/eyes: same as Meatball. Default eyelids half-lowered (repo `mood: smug`). [PROPOSED]
- Expressions (8): `smug` (half-lidded, repo mood), `deadpan stare`, `ears-flat` (repo gag), `wide-eyed` (pupils huge), `swat` (paw raised, eyes narrowed), `walk-off` (back view, tail up, the signature exit), `asleep` (loaf, eyes closed), `yawn`. [PROPOSED]
- Turnaround: front sit, 3/4, side walk, **back walking away** (the most-used view), top-down loaf. [PROPOSED]
- Poses: sit, loaf, walk away, swat, bat a prop off a ledge, perch, jump up, stretch, groom. [PROPOSED]

### 1.4 File naming [DERIVED]

`mm_<kind>_<subject>_<view-or-expr>_<variant>_v<NN>.<ext>`, lowercase, hyphens inside words.
- Characters: `mm_char_meatball_expr-shock_front_v01.png`, `mm_char_noodle_turn-34_v01.png`, `mm_char_sauce_pose-walkoff_back_v01.png`
- Scenes: `mm_scene_dogeye_kitchen_bg-far_v01.png` (layers: `bg-far`, `bg-mid`, `fg`, `fx`)
- Props: `mm_prop_cardboard-ears_v01.png`
- Thumbnail proofs keep the repo rule: `NAME_168.jpg` [REPO `thumbnail-spec-two-styles-1115.md`]
- Any unapproved pet art carries the `PROPOSED-` prefix until Social Studio or Moondog88 approves it.

---

## 2. Reusable scene types

All scenes: 16:9 master at 1920×1080. Parallax layers export as separate transparent PNGs. Shared house palette values come from Claude's `drawn_kit.py` `PAL` [BOX]: `wall #c9b89a`, `floor #8a6f55`, `wood #b07a45`, `bulb #fff2a8`, `window #9fd3ee`, `night #1b2440`, `night2 #26315a`. The repo's v6 scene names are reused where they exist: `kitchen`, `bedroom`, `bathroom`, `study`, `basement`, `garden`, with `scene_p.time: night` [REPO v6 JSON].

**Text-safe zones (all scenes)** [DERIVED unless tagged]:
- 16:9: keep cards and captions inside a 5% title-safe margin (96 px sides, 54 px top/bottom). Captions sit in the bottom band y 880–1010. Never put a character's face in that band during speech. Cards go upper-left or upper-right (mirrors the thumbnail rule "words top-left or top-right, never bottom-right" [REPO]).
- 9:16 crop from the 16:9 master: the crop is a **608 px-wide column** (1080 × 9/16) at full height. Key action and faces must sit inside the column the shot note names in `crop_916.focus_x` (default center, x 656–1264). In the rebuilt 1080×1920 vertical: cards at `card.y: 470`, captions 66 px at `caption_y: 1180` [REPO `shorts/shorts-edit-spec.md`]. Treat roughly the top 240 px, the bottom 660 px and the right-side button column as no-text zones. These are unofficial third-party measurements of TikTok's ads overlay, not an organic rule [REPO `shorts/shorts-edit-checklist-v1.md` §4].

### S1. Inside-the-body (`inside`)
- **Use:** born-as "inside you" beats (stomach, bloodstream, nose, ear) where a fact line explains the body. Cutaway only. It never carries a joke inside a fact or safety line [REPO bible].
- **Layout:** a soft tube or chamber filling the frame, curving away to a vanishing point at center-right. Meatball rides in from the left in his **cardboard-box boat with a spatula paddle** (an existing prop, `gags-1116.md` #8 [REPO]).
- **Camera:** eye level with Meatball, medium-wide, slow push-in (1.00→1.08) [DERIVED].
- **Palette/lighting:** warm pinks and corals (body wall `#e9a0a0`, shade `#c46a6a`, fluid highlights `#ffd6d0`) [DERIVED]. No gore and no realistic organs. Drawn particles only. Mirrors the dog long-form note "no gore, no sick-puppy close-ups" [REPO `longform-dog-bornas.json` `art_needed`].
- **Parallax layers:** `bg-far` (tube depth gradient), `bg-mid` (wall folds), `fg` (floating particles), `fx` (bubbles).
- **Props:** box boat, spatula, drawn particles (virus = simple spiky ball, no real micrograph), arrow sign.
- **Text-safe:** cards upper-right. The tube's open center is the 9:16 focus column.

### S2. Dog's-eye view (`dogeye`), Noodle POV
- **Use:** "you are the dog" moments. The world looms and Meatball is the giant-seeming human stand-in or the target of Noodle's chase.
- **Layout:** the floor fills the lower 45%. Table and chair legs tower as foreground frames left and right. The underside of the table or counter edge cuts across the top.
- **Camera:** lens height about a dog's eye (≈ 0.4 m scaled), **wide lens (≈ 18–24 mm look) with gentle barrel curve**, slight upward tilt. Optional soft dark vignette. Shots run as slow drift-forward (sniff walk) or a quick head-turn pan [DERIVED].
- **Palette/lighting:** the environment gets a **POV grade**: reds pulled toward olive/brown, blues and yellows kept, overall contrast −10%. This is an art grade only, never stated on screen as a vision fact. **Meatball and other cast members are never graded**; the red cap stays red [DERIVED].
- **Parallax layers:** `fg` (table and chair legs, fast), `bg-mid` (cabinets, fridge), `bg-far` (back wall, window), `fx` (dust motes, vignette).
- **Props:** food bowl, dropped sandwich (the recurring Noodle steal [REPO bible]), sock (dog long-form s1.l10 [REPO]), ball, leash on a hook.
- **Text-safe:** cards top-center between the table edge and the frame top. For 9:16, center the focus column on the target object.
- Reference render: `/workspace/animation/scene-dogs-eye-kitchen-v1.jpg`.

### S3. House at night (`night`)
- **Use:** survival-story tension, sleep beats, "something moved" beats. Bed-bug and lamp scenes already use night rooms [REPO `gags-1116.md` #1].
- **Layout:** a room in deep blue. One warm light source (lamp, fridge glow, nightlight). Long floor shadows.
- **Camera:** locked wide establishing for ≤ 2 s, then a slow push toward the light source or a pan along the hallway [DERIVED].
- **Palette/lighting:** `night #1b2440` / `night2 #26315a` base, `bulb #fff2a8` and `glow #fff6c8` pools [BOX `drawn_kit.py`]. Characters get a cool rim on the dark side; the glow side stays true color [DERIVED].
- **Parallax layers:** `bg-far` (window with moon), `bg-mid` (furniture silhouettes), `fg` (door frame or couch arm), `fx` (light pool, flicker mask).
- **Props:** lamp, flashlight (existing gag prop [REPO `gags-1116.md` #1, #4]), clock, pet bed, nightlight.
- **Text-safe:** cards go in the dark areas, never over the light pool.

### S4. Clock / timer overlay (`clock`)
- **Use:** "the clock starts" beats (the dog long-form chapter "The clock" [REPO `longform-dog-bornas.json`]), countdowns, age milestones, the "how long until" survival beat. Bed-bug Short #1 already has a "clock face slides" card [REPO `gags-1116.md`].
- **Layout:** a full-scene overlay. A big analog clock face or a ring timer slides in from the top-right over any running scene. The scene keeps moving underneath.
- **Camera:** the underlying scene keeps its move. The overlay itself does a pop-in (overshoot), and its hand ticks in 0.25 s steps [DERIVED].
- **Palette/lighting:** paper face `#fbf6e6` with ink numerals, sauce-red hand `#d42a22` for the active segment, translucent scrim `#000000` at 25% behind it [DERIVED, colors from [BOX] palettes].
- **Layers:** `scene` (any S-type), `scrim`, `clock-face`, `clock-hand`, `label`.
- **Props:** analog clock, stopwatch (existing gag prop, croc Short #7 [REPO]), calendar page flip, egg timer.
- **Text-safe:** the label sits under the clock and only states the line's sourced number with its hedge (e.g. "ABOUT DAY 13-19" from the card text [REPO]). No unsourced numbers.

### S5. Cat's-eye high perch (`cateye`), Sauce POV
- **Use:** Sauce watching from the fridge top or bookshelf, then the walk-off. Overhead reveals of Meatball's plan failing.
- **Layout:** a steep top-down 60–75° view from a shelf or fridge top. Meatball and Noodle are small on the floor. The perch edge and one paw sit in the foreground.
- **Camera:** high angle, normal lens (≈ 35 mm look), slow tilt-down or a lazy pan following Meatball [DERIVED].
- **Palette/lighting:** true house colors with slightly cooler shadows. No POV grade, so it contrasts with S2 [DERIVED].
- **Parallax layers:** `fg` (perch edge and paw), `bg-mid` (counters), `bg-far` (floor).
- **Props:** the knocked-off object (mug, calculator, goggles, map: existing Sauce gags [REPO `gags-1116.md`]), shelf plants.
- **Text-safe:** cards upper area away from the perch edge. In 9:16, the focus column holds Meatball's top-down red disc.

### S6. Giant-food scale view (`giantfood`)
- **Use:** the kitchen and food-bowl beats (dog long-form chapters "The kitchen" and "The food bowl" [REPO]), toxic-food warnings, and the Meatball-is-tiny comedy.
- **Layout:** a countertop or bowl rim at frame bottom. Oversized food items (sandwich, grapes, chocolate tin) tower behind it. Meatball stands at counter level for scale.
- **Camera:** low macro angle at counter height, push-in or a slow orbit pan [DERIVED].
- **Palette/lighting:** warm daylight. Food in flat saturated colors. Any food flagged as a hazard gets the normal card, never a skull or gore [DERIVED + REPO safety-card rules].
- **Parallax layers:** `fg` (bowl rim or crumbs), `bg-mid` (food items), `bg-far` (kitchen wall `#c9b89a`).
- **Props:** food bowl, sandwich, chocolate tin (repo thumbnail concept "LEAVE THE TIN" [REPO `thumbnail-concepts.md` §5]), measuring spoon.
- **Text-safe:** the safety card is **pinned across its cut** [REPO `gags-1116.md` rules] at the top. Gags never go on a safety line [REPO `dog-bornas-revision-1116.md`].

### S7 (bonus). Outside world / vet (`outside`)
- **Use:** shelter, vet table, parked car, yard: the dog long-form's later chapters [REPO `longform-dog-bornas.json` chapters].
- **Layout:** the vet table seen from table height, or a car interior seen from the back seat at pet height.
- **Camera:** pet-height, medium lens. A heat shimmer distortion layer for the parked-car chapter ("thermometers and heat shimmer, no charts" [REPO `dog-bornas-revision-1116.md` §6]).
- **Palette:** clinic `#e8f0f2` / `#9fb8c0` [DERIVED]. Car interior `#3d4a57` [BOX `drawn_kit.py` `hull`] with sun-yellow window glare.
- **Layers:** `bg-far` (window/outside), `bg-mid` (table or seats), `fg` (stethoscope or seat edge), `fx` (shimmer).
- **Props:** vaccine card, thermometer, carrier, leash.
- **Text-safe:** same as S6. Safety lines play clean with no gag and no scream sting [REPO].

---

## 3. Gag library: 10 physical Meatball gags

Timing at **30 fps** [DERIVED]. Sound cues use **only the existing v2 SFX kit names**: `whoosh, boing, pop, scratch, thud, hit, tink, click, step, sting, splash, crunch, plate, stamp, case` (`zap` is marked "unused, too sharp"). Limits: **max 2 cues per line, 0.5 s apart**, and no line cue in the first ~0.42 s after a cut, because `cut_whoosh` fires 80 ms before each beat [REPO `shorts-push-1116/sound-cues.md`].

House rules for every gag [REPO `meatball-bible.md`, `gags-1116.md`, `dog-bornas-revision-1116.md`]: actions only, with no captioned feeling or motive for any pet. The gag acts out the script's existing joke line and adds no words, numbers, dangers or instructions. Gags happen at home. Long-forms get one physical gag every 30–45 s. Never on a safety line.

| # | Gag | Trigger / use case | Beats (frames @30 fps) | SFX |
|---|---|---|---|---|
| G1 | **Squish** | Something lands on or closes on Meatball (Noodle sits on him, a pillow drops, a cupboard door) | f0–3 anticipation: he looks up, eyes `shock` · f4 impact: body squash to (1.35 w, 0.55 h), eyes `hurt` · f5–14 hold squashed · f15–20 pop back with overshoot (0.9 w, 1.15 h) · f21–26 settle 1.0 · f27–40 `dizzy` blink | `thud`@f4, `pop`@f15 |
| G2 | **Bonk & bounce** | He walks into a fridge, a door or a glass door (dog long-form s1.l4 "walked straight into the fridge" [REPO]) | f0–8 walk in, eyes shut or `neutral` · f9 contact: squash on the impact side (0.75 w) · f10–18 bounce back ~1 r with an arc, rotation −20° · f19–22 land with squash (1.2, 0.8) · f23–45 sit, `dizzy` | `boing`@f9, `thud`@f19 |
| G3 | **Roll away** | Knocked over on a slope or hallway. Escape beats | f0–5 tip, limbs tuck in · f6–40 roll as a ball (one full rotation per ~10 frames, sauce cap spinning), limbs hidden · f41–46 stop against a wall, squash · f47–55 limbs pop out, `dizzy` | `whoosh`@f6, `thud`@f41 |
| G4 | **Sauce splat** | A hard landing (falls off a counter or the couch) | f0–6 fall with stretch (0.85, 1.2) · f7 impact squash (1.4, 0.6) · f7–9 the sauce cap flings 3–4 red blobs outward, cap visibly thinner · f10–30 `hurt`→`neutral` · f31–45 blobs slide back and re-form the cap with drips (**the cap must be whole again by the end of the gag**) [DERIVED] | `splash`@f7, `pop`@f31 |
| G5 | **Carried off** | Noodle picks Meatball (or his prop) up and trots away, the recurring Noodle beat [REPO bible] | f0–10 Noodle enters, Meatball oblivious · f11–14 grab: Meatball lifted, limbs dangle · f15–50 Noodle trots off screen (step cycle), Meatball's legs swing, eyes `side-eye` to camera | `step`@f15, `step`@f30 |
| G6 | **Batted off the ledge** | Sauce paws Meatball or his prop off a counter or shelf [REPO gags #2, #4, #6] | f0–12 Sauce sits, `deadpan` · f13–16 one paw tap · f17–30 Meatball or prop slides and drops (ease-in) · f31 floor impact · f32–60 Sauce walks off (back view, tail up) | `tink`@f13, `thud`@f31 |
| G7 | **Tangled** | A sheet, map, blinds or tape wraps him [REPO gags #2, #5, #10, #12] | f0–10 he grabs the item · f11–24 spin, 2 rotations while the wrap builds · f25–30 stop wrapped as a cylinder, one arm out · f31–45 wiggle (±6° rotation, 3 cycles) · f46–55 optional pop free | `whoosh`@f11, `pop`@f46 |
| G8 | **Belly slide** | Chasing something across a wood floor in socks [REPO gags #7, #11] | f0–8 run cycle · f9–12 dive, body stretches (0.8, 1.25) · f13–40 slide on his belly, limbs back, speed lines · f41 hits a door frame or rug edge · f42–55 sits up, `shock` or holding the rescued prop | `scratch`@f13, `hit`@f41 |
| G9 | **Chase lap** | Noodle takes the food or prop and Meatball chases him around the island or bed [REPO gags #1, #3, #7] | f0–6 the steal (from G5) · f7–20 Meatball runs after him (run cycle, arms swinging) · f21–36 whip-pan to follow · f37–50 the pair crosses the frame again in the other direction (the lap) · f51–60 Meatball trips, Noodle keeps going | `whoosh`@f21, `thud`@f51 |
| G10 | **Pet-door wedge** | He tries to follow a pet through the pet flap or a narrow gap | f0–10 runs at the flap · f11–14 head and body enter, then stop; flap squeezes the body to (0.8, 1.1) · f15–40 legs kick behind (4 kicks), flap wobbles · f41–44 pops through with a stretch · f45–55 lands, squash, `dizzy` | `hit`@f11, `pop`@f41 |

Pacing note: each gag runs 1.3–2.0 s (40–60 frames), so it fits one 2–3 s shot or splits across two cuts at the impact frame [DERIVED].

---

## 4. Motion rules for Claude's render pipeline

### 4.1 Cadence
- **Story long-forms (16:9):** a new shot or a listed visual change every **2–3 s**. **Max static time 3.0 s** (no frame without a listed change for longer than 3.0 s). **No single shot over 5.0 s** even with in-shot moves [REPO Social Studio 11/16 ruling in `longform/dog-bornas-revision-1116.md`: "a new shot every 2-3 s with no held shot over 5 s"]. This sits inside the brief's 1–3 s band.
- **9:16 crops / Shorts:** a new picture every **1–2 s, no gap over 2.0 s** [REPO `shorts/shorts-edit-spec.md`, 11/15 house order]. When cutting a 9:16 from a long-form, add mid-shot changes (push, pose swap, overlay pop) so no still holds over 2.0 s.
- **Physical gag:** one every **30–45 s** in long-forms [REPO ruling]. One per Short [REPO `gags-1116.md`].
- **Cuts land on line breaks or punctuation** when possible [REPO `gags-1116.md`]. Splitting a line into shots keeps the line's total duration [REPO `dog-bornas-revision-1116.md`].
- **No charts, pie charts or document shots.** Use objects instead (carriers in a line, stamp pads) [REPO `dog-bornas-revision-1116.md`].

### 4.2 Allowed change types (exhaustive; anything else needs approval)
| `type` | What it is | Default duration | Easing |
|---|---|---|---|
| `cut` | hard cut to a new shot | 0 frames | – |
| `push_in` | camera scale up on a focus point | whole shot, scale 1.00→1.08 (strong: →1.20 over ≥ 0.6 s) | ease-in-out |
| `pull_out` | reverse push | whole shot, 1.08→1.00 | ease-in-out |
| `pan` | lateral camera move | 0.8–2.0 s, ≤ 25% frame width per second | ease-in-out |
| `whip_pan` | fast pan with motion blur, used inside G9 [REPO gags #3] | 6–8 frames | ease-in, blur on |
| `pose_swap` | character changes pose | 4–6 frames (BIG moves: shock, shrug, wave, laugh get a 3-frame anticipation crouch) | ease-back (slight overshoot) |
| `expr_swap` | face snaps to a new expression | 0–2 frames (snap, no morph) | – |
| `char_enter` / `char_exit` | character hops or walks in or out. Meatball "hops in" ≈ 0.40–0.45 s, hop height ≈ 200–220 px | 0.4–0.7 s | ease-back |
| `overlay_pop` | card, chip, clock or stamp appears | 8 frames: scale 0→1.10→1.00 | ease-back |
| `overlay_out` | card leaves | 6 frames, slide or scale to 0 | ease-in |
| `gag_insert` | a G1–G10 gag from §3 | 40–60 frames | per gag beats |
| `scene_swap` | change to another S-type scene | cut, or 6-frame whoosh-wipe | ease-in-out |
| `parallax_drift` | layers drift at different speeds (counts as a change only together with another change) | whole shot | linear |

Easing definitions follow the house rig: `ease_inout` and `ease_back` (overshoot c = 0.6), "eased, anticipating, slightly overshooting transitions". Reaction holds: shock 1.2 s, laugh 1.5 s, wave 1.4 s, then the character moves on. Max gesture hold 1.1 s [BOX `skills-readonly/.../tools/mascot.py`; `characters.py`]. Durations not in those files are [DERIVED].

### 4.3 Caption and overlay rules
- **Cards** state only the script line's sourced number or phrase, hedge kept ("ABOUT", "MAY") [REPO `meatball-bible.md`, `longform-dog-bornas.json` card fields]. Hand-lettered heavy caps with a thick black outline. Headline yellow `#ffd34d` around 80 px, sub-line white about 48 px (v6 card rows) [REPO `scripts/dogs-lick-v6-yt.json`]. Exactly one red word per thumbnail [REPO `thumbnail-spec-two-styles-1115.md`].
- **No feeling or motive captions** for Noodle or Sauce, no face cards, no added words on gag beats [REPO `gags-1116.md`].
- **Safety cards** stay pinned on screen across their cut until the safety line ends [REPO `gags-1116.md`]. Safety lines are clean: no gag, no scream sting, music ducked [REPO `dog-bornas-revision-1116.md`].
- **Burned-in captions:** 9:16 at 66 px, `caption_y: 1180` [REPO]. 16:9 long-form captions go in the bottom band y 880–1010 [DERIVED].
- **At most 2 overlays on screen at once** (card + chip, or clock + label) [DERIVED].
- **No outro cards**, no Subscribe or Follow on Shorts [REPO bible]. Long-form end screens stay animated, never a still over 5 s [REPO `dog-bornas-revision-1116.md`].
- **SFX:** v2 kit names only, ≤ 2 per line, ≥ 0.5 s apart, `cut_whoosh: true` [REPO `sound-cues.md`].

### 4.4 Shot-note format (machine-friendly YAML)

It extends the existing long-form JSON `segments[].lines[].shots[] {t, dur, vis}` shape [REPO `scripts/longform-dog-bornas.json`], so each shot still maps to a script line id. Proposed fields [DERIVED]:

```yaml
episode: <slug>            # e.g. dog-bornas
fps: 30
canvas: [1920, 1080]
crops: ["9:16"]
shots:
  - id: <line_id>.<letter>   # s1.l1.a  (script line id + shot letter)
    line: <line_id>          # links to the voiced line; the line text is never edited here
    start: <seconds>         # absolute video time
    dur: <seconds>           # 0.5–3.0 normal; 5.0 hard max
    scene: <S-type>/<variant>   # inside | dogeye | night | clock | cateye | giantfood | outside | v6 rooms
    chars:                   # optional
      - {id: meatball|noodle|sauce, pose: <pose>, expr: <expr>, pos: [x, y], scale: <float>, facing: l|r}
    action: <one sentence, actions only>
    changes:                 # every listed change type with its time inside the shot
      - {type: <allowed type>, at: <s from shot start>, dur: <s>, ease: ease_inout|ease_back|linear, params: {...}}
    camera: {type: static|push_in|pull_out|pan|whip_pan, from: [x, y, scale], to: [x, y, scale], ease: <ease>}
    overlay:                 # 0–2 items
      - {kind: card|chip|clock|stamp|safety, text: "<from script card>", at: <s>, zone: top-left|top-right|top-center, pinned: true|false}
    gag: G1..G10 | null
    sfx: ["<kit name>@<s from shot start>"]   # ≤2 per line, ≥0.5 s apart
    crop_916: {focus_x: <px in 1920 master>}  # center of the 608-px column
    notes: <optional>
```

Validation a renderer can run: every `dur` ≤ 5.0. No interval over 3.0 s (16:9) or 2.0 s (9:16) without an entry in `changes` or a cut. `sfx` names are in the v2 kit list. A `safety` overlay has `pinned: true` and the shot has `gag: null`. `overlay` length ≤ 2.

### 4.5 Worked example (~29 s): dog born-as, chapter 1 open

Spoken lines, ids and times are copied unchanged from `scripts/longform-dog-bornas.json` s1.l0–s1.l5 [REPO]. The s1.l5 split (1.7 + 1.7) follows `longform/dog-bornas-revision-1116.md` [REPO]. Shots, cameras, gags and SFX are [DERIVED]. Total 21.6 → 50.9 s = **29.3 s, 13 shots, longest shot 2.93 s**.

```yaml
episode: dog-bornas
fps: 30
canvas: [1920, 1080]
crops: ["9:16"]
shots:
  - id: s1.l0.a           # "Number one. The whelping box."
    line: s1.l0
    start: 21.6
    dur: 1.54
    scene: dogeye/whelping-box
    action: Number card whips in over the puppy pile.
    changes: [{type: overlay_pop, at: 0.0, dur: 0.27, ease: ease_back}]
    camera: {type: push_in, from: [960, 600, 1.0], to: [960, 600, 1.06], ease: ease_inout}
    overlay: [{kind: card, text: "1 OF 8: THE WHELPING BOX", at: 0.0, zone: top-center, pinned: false}]
    gag: null
    sfx: ["pop@0.1"]
    crop_916: {focus_x: 960}
  - id: s1.l1.a           # "For about your first two weeks, you can't see or hear..."
    line: s1.l1
    start: 23.1
    dur: 2.37
    scene: dogeye/whelping-box
    action: Puppy nose-first, crawling in a slow circle; mother curls around the litter.
    changes: [{type: parallax_drift, at: 0.0, dur: 2.37, ease: linear}, {type: overlay_pop, at: 0.6, dur: 0.27, ease: ease_back}]
    camera: {type: pan, from: [800, 620, 1.05], to: [1100, 620, 1.05], ease: ease_inout}
    overlay: [{kind: card, text: "EYES AND EARS CLOSED", at: 0.6, zone: top-left, pinned: false}]
    gag: null
    sfx: []
    crop_916: {focus_x: 960}
  - id: s1.l1.b
    line: s1.l1
    start: 25.5
    dur: 2.37
    scene: clock/whelping-box
    action: Timeline chip slides on over the litter.
    changes: [{type: overlay_pop, at: 0.0, dur: 0.27, ease: ease_back}]
    camera: {type: push_in, from: [960, 560, 1.0], to: [960, 560, 1.08], ease: ease_inout}
    overlay: [{kind: chip, text: "BIRTH TO ABOUT DAY 13", at: 0.0, zone: top-right, pinned: false}]
    gag: null
    sfx: ["click@0.5"]
    crop_916: {focus_x: 1000}
  - id: s1.l1.c
    line: s1.l1
    start: 27.9
    dur: 2.37
    scene: dogeye/whelping-box
    action: Mother noses a stray puppy back into the pile.
    changes: [{type: cut, at: 0.0, dur: 0}]
    camera: {type: push_in, from: [1050, 640, 1.08], to: [1050, 640, 1.16], ease: ease_inout}
    overlay: []
    gag: null
    sfx: []
    crop_916: {focus_x: 1050}
  - id: s1.l2.a           # "Meet the guy in the cardboard ears. That's Meatball..."
    line: s1.l2
    start: 30.2
    dur: 2.93
    scene: kitchen/living-rug-day
    chars: [{id: meatball, pose: curled, expr: neutral, pos: [900, 760], scale: 1.0, facing: r}]
    action: Reveal Meatball curled in a dog bed, wearing cardboard ears; close on one ear flopping.
    changes: [{type: char_enter, at: 0.0, dur: 0.45, ease: ease_back}, {type: push_in, at: 1.4, dur: 1.5, ease: ease_inout}]
    camera: {type: push_in, from: [900, 700, 1.0], to: [900, 560, 1.25], ease: ease_inout}
    overlay: []
    gag: null
    sfx: ["boing@0.45"]
    crop_916: {focus_x: 900}
  - id: s1.l2.b
    line: s1.l2
    start: 33.13
    dur: 2.93
    scene: kitchen/living-rug-day
    chars: [{id: meatball, pose: present, expr: happy, pos: [900, 760], scale: 1.0, facing: r}]
    action: He holds up a rubber stamp, flips it from RAW to SWEET.
    changes: [{type: pose_swap, at: 0.0, dur: 0.17, ease: ease_back}, {type: overlay_pop, at: 1.5, dur: 0.27, ease: ease_back}]
    camera: {type: static, from: [960, 600, 1.1], to: [960, 600, 1.1], ease: linear}
    overlay: [{kind: stamp, text: "RAW / SWEET", at: 1.5, zone: top-right, pinned: false}]
    gag: null
    sfx: ["stamp@1.5"]
    crop_916: {focus_x: 900}
  - id: s1.l3.a           # "His dog, Noodle, is the real dog."
    line: s1.l3
    start: 36.1
    dur: 2.0
    scene: kitchen/living-rug-day
    chars: [{id: noodle, pose: sit, expr: happy, pos: [1100, 780], scale: 1.0, facing: l}]
    action: Noodle sits beside the dog bed, tail thumping.
    changes: [{type: char_enter, at: 0.0, dur: 0.5, ease: ease_back}]
    camera: {type: push_in, from: [1100, 640, 1.0], to: [1100, 640, 1.06], ease: ease_inout}
    overlay: []
    gag: null
    sfx: []
    crop_916: {focus_x: 1100}
  - id: s1.l3.b           # "His cat, Sauce, is everybody else."
    line: s1.l3
    start: 38.1
    dur: 2.01
    scene: cateye/fridge-top
    chars: [{id: sauce, pose: loaf, expr: smug, pos: [960, 300], scale: 1.0, facing: l}]
    action: Sauce on the fridge top, looking down at the room.
    changes: [{type: scene_swap, at: 0.0, dur: 0}]
    camera: {type: pan, from: [900, 400, 1.0], to: [1000, 420, 1.0], ease: ease_inout}
    overlay: []
    gag: null
    sfx: []
    crop_916: {focus_x: 960}
  - id: s1.l4.a           # "Meatball kept his eyes shut for the full experience."
    line: s1.l4
    start: 40.1
    dur: 2.4
    scene: kitchen/day
    chars: [{id: meatball, pose: crawl, expr: neutral, pos: [500, 780], scale: 1.0, facing: r}]
    action: Meatball crawls across the kitchen in cardboard ears, eyes squeezed shut.
    changes: [{type: pan, at: 0.0, dur: 2.4, ease: linear}, {type: expr_swap, at: 1.2, dur: 0.0, ease: linear}]
    camera: {type: pan, from: [600, 640, 1.0], to: [1100, 640, 1.0], ease: linear}
    overlay: []
    gag: null
    sfx: ["step@0.6", "step@1.3"]
    crop_916: {focus_x: 800}
  - id: s1.l4.b           # "He walked straight into the fridge."
    line: s1.l4
    start: 42.5
    dur: 2.4
    scene: kitchen/day
    chars: [{id: meatball, pose: walk, expr: neutral, pos: [1250, 780], scale: 1.0, facing: r}]
    action: He walks into the fridge door and bounces back onto the floor.
    changes: [{type: gag_insert, at: 0.3, dur: 1.5, ease: ease_back}]
    camera: {type: push_in, from: [1250, 620, 1.05], to: [1250, 620, 1.15], ease: ease_inout}
    overlay: []
    gag: G2
    sfx: ["boing@0.6", "thud@1.25"]
    crop_916: {focus_x: 1250}
  - id: s1.l4.c           # "Sauce watched, then walked off. Hell of a start."
    line: s1.l4
    start: 44.9
    dur: 2.6
    scene: cateye/fridge-top
    chars: [{id: sauce, pose: walk-off, expr: smug, pos: [960, 320], scale: 1.0, facing: r}, {id: meatball, pose: flat, expr: dizzy, pos: [960, 900], scale: 0.4, facing: r}]
    action: Top-down from the fridge; Meatball flat on the floor below; Sauce stands and walks off out of frame.
    changes: [{type: cut, at: 0.0, dur: 0}, {type: pose_swap, at: 0.9, dur: 0.17, ease: ease_back}, {type: char_exit, at: 1.2, dur: 0.7, ease: ease_inout}]
    camera: {type: static, from: [960, 540, 1.0], to: [960, 540, 1.0], ease: linear}
    overlay: []
    gag: null              # the acted 'Sauce walked off' payoff, not a gag insert
    sfx: ["step@1.2"]
    crop_916: {focus_x: 960}
  - id: s1.l5.a           # "Somewhere around day thirteen to nineteen, your eyes and ears open."
    line: s1.l5
    start: 47.5
    dur: 1.7
    scene: dogeye/whelping-box
    action: A puppy's eye cracks open (POV blur to sharp).
    changes: [{type: cut, at: 0.0, dur: 0}, {type: push_in, at: 0.0, dur: 1.7, ease: ease_inout}]
    camera: {type: push_in, from: [960, 540, 1.1], to: [960, 540, 1.2], ease: ease_inout}
    overlay: []
    gag: null
    sfx: []
    crop_916: {focus_x: 960}
  - id: s1.l5.b
    line: s1.l5
    start: 49.2
    dur: 1.69
    scene: dogeye/whelping-box
    action: Ears lift and the room fades in around the litter.
    changes: [{type: pull_out, at: 0.0, dur: 1.69, ease: ease_inout}, {type: overlay_pop, at: 0.2, dur: 0.27, ease: ease_back}]
    camera: {type: pull_out, from: [960, 540, 1.2], to: [960, 540, 1.0], ease: ease_inout}
    overlay: [{kind: card, text: "EYES OPEN: ABOUT DAY 13-19", at: 0.2, zone: top-left, pinned: false}]
    gag: null
    sfx: []
    crop_916: {focus_x: 960}
```

Check: 13 YAML shots cover 29.3 s. Starts are copied from the script's rounded times, so neighbors overlap or gap by up to 0.07 s; the renderer should snap each shot's start to the previous shot's end. The longest is 2.93 s and no 3.0 s window lacks a change. The one gag (G2) and the Sauce walk-off payoff both sit inside the joke line s1.l4, and no gag is placed on a fact or safety line. All SFX names are from the v2 kit. For the 9:16 cut, s1.l1.a–c and s1.l4.a need an extra mid-shot change to meet the 2.0 s Shorts rule (they already have pans or pushes running).

---

## 5. Reference images

Existing house references copied for this kit (box only, not in the repo): `/workspace/animation/refs/`
- `meatball_ref_sheet_v1.jpg`: canonical cartoon ref sheet (from `meatball-animation-v2/mb2/art/`)
- `character_ref.png`: v2 rig render (from `meatball-animation-v2/work/`)
- `mb-v6b-cH3HCZ8GlHk.png`, `before-after-sheet-v6b.png`: v6b thumbnail sprite and sheet (from `drafts/thumbs-v6-1116/`)
- `pfp-final-c.png`: cartoon pfp draft (from `drafts/meatball-pfp-v2-1116/`); `pfpB_shock_navy.png`: earlier pfp draft (from `/tmp`)
- `pfp.jpg`: the pfp saved in `pubcheck/` (older stick-figure rig look)
- `v3_thumb_1_too-slow.png`, `p4_playdead_v2.jpg`: illustrated panel art (from `meatball-animation-v2/`)

Generated for this kit [DERIVED, made from the refs above]:
- `/workspace/animation/meatball-expression-sheet-v1.jpg`: 8 on-model expressions (neutral, shock, scared, determined, smug, hurt, happy, dizzy)
- `/workspace/animation/scene-dogs-eye-kitchen-v1.jpg`: S2 dog's-eye view, background graded, Meatball not graded
- `/workspace/animation/PROPOSED-noodle-sauce-concept-v1.jpg`: **proposed only**. Noodle and Sauce in the house style using the repo renderer colors. Meatball is drawn about dog height here, larger than the proposed scale in §1.2.

## 6. Open items needing approval
1. **Noodle and Sauce cartoon designs do not exist.** Approve or replace §1.2–1.3 and the proposed concept image (breed/shape, collar color, markings, scale vs Meatball).
2. **Which pfp is live?** `pubcheck/pfp.jpg` (stick-figure rig) vs the cartoon `pfp-final-c.png`. The kit assumes the cartoon ball look is canonical for new long-forms, as the brief says ("v6 thumbs, pfp").
3. **The v6/v6b thumbnails are marked "not live" samples** on the box. Confirm they are the approved look.
4. **No brand palette is written down in the repo.** The hex values come from Jarvis's rig (`characters.py`, sampled from the ref sheet) and the repo renderer configs. Consider committing §1.1's palette as the official one.
5. **Renderer gap:** the drawn-house renderer that made the v6 Shorts uses a generic dog/cat (`creature_cfg`), not the cartoon rig. Pet-POV long-forms need Noodle and Sauce added to Jarvis's `mb2` rig, or to Claude's builder, before this kit can render. The dog long-form's `builder` field already says a dog shot set "would be needed" [REPO `longform-dog-bornas.json`].
6. Scene palettes for S1, S6 and S7 and all durations not cited above are [DERIVED] and can be changed freely.
