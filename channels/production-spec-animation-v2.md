# Production spec: animation and editing, v2 (Meatball Myths YouTube Shorts + TikTok)

**Owner:** Social Studio lane. **Written:** Sun Nov 15, 2026, about 8:00 PM ET, by Jarvis (Moondog88: "if you can animate the videos better then completely take over"). Companion to [production-spec-audio-v2.md](production-spec-audio-v2.md).
**Evidence:** [analytics/data/visual-motion-1115.jsonl](analytics/data/visual-motion-1115.jsonl), measured with [analytics/data/visual-motion.py](analytics/data/visual-motion.py) on 12 of our videos and 4 niche outliers. Prototype: [production/mb2/](production/mb2/README.md).
**Status:** proposal. The style pick (A, B or C) is Moondog88's. Nothing is posted, and no channel setting changes.

## What the measurements say
| Video | Views | Shots/min | Avg shot (s) | Note |
|---|---|---|---|---|
| Ours: Grizzly WMS #3 (posted) | 944 | 9.3 | 6.5 | constant camera drift (motion 5.5) but the **same picture for 6.5 s** |
| Ours: House centipede | 2,289 | 7.9 | 7.6 | |
| Ours: Dog guilty look | 3 | 36 | 1.7 | fast cuts didn't save a weak topic and hook |
| Ours: Mommy longlegs | 1,908 | 69.7 | 0.9 | |
| Sketching the Wild: White Tigers Short | 4.6M | 103 | 0.6 | an illustrated new composition every 0.6 s, emotive close-ups, speech bubbles |
| Zoozle: Born as a Hummingbird (long) | 2.6M | 11 | 5.5 | long-form: static frames, rich art, story |
| lianna_anima: Big cats no big dogs (TikTok) | 212K | ~0 hard cuts | | a new drawing pops in on every phrase over a fixed background |
| **Our v2 prototypes (same script)** | | **45 (planned shots)** | **1.3** | A rig / B panels / C hybrid |

Takeaway: **motion isn't our problem. Picture change, readability and character acting are.** Our renders drift the camera constantly but keep the same composition for 6-8 s. The characters are small (Meatball is about 12% of frame height), the animals share one sausage body, and the picture rarely acts out the words. The outliers change the *picture* (not the camera) every 0.6-2 s, frame the face big, and show the verb happening.

## Rules for every new Short (from Nov 17 renders)
1. **New composition every 1.0-2.0 s** on Shorts (2-4 s on long-form). A camera move inside the same framing doesn't count. Anchor each shot to a spoken word.
2. **Frame 0 = the threat, mid-action, close-up.** The animal's face fills at least 40% of the frame with motion on frame 0 (roar, lunge). Series tag for 1.8 s only.
3. **Characters big:** Meatball's body is at least 25% of frame width in a two-shot and at least 60% in a reaction close-up. One close-up reaction per Short.
4. **Act the verb:** "chase" = a chase, "knocks you down" = an impact frame (2-frame black silhouette, white flash, shake, stars), "play dead" = the actual pose with the condition on the card.
5. **Species silhouettes:** every animal gets 2-3 tells (bear: shoulder hump, claws, round ears; dog: ears, tail, snout length; cat: ears, whiskers, tail). Stop reusing one quadruped body.
6. **Acting rig:** blinks every ~3 s, brows per emotion, lip flap from the voice envelope, squash and stretch on landings and hits, anticipation before a zip-off.
7. **Comic grammar:** 1-2 gags acted on screen (the treadmill run, the POW burst), comic marks (!, stars, sweat), and a speed-line or radial-line layer on action.
8. **Kinetic captions:** 1-3 words, Anton 112 px, popped with a spring, keyword in yellow at 124 px, centred at y≈1430 (above the TikTok UI). Cards top-centre, popped row by row; a fact card keeps its source chip.
9. **Loop:** the last shot returns to the frame-0 composition, so the cut to the replay is seamless.
10. **Whip transitions:** 3-frame white smear on cuts; whoosh SFX only on location changes (audio spec §4).

## House style: C v2 "unified hybrid" (Moondog88, Nov 15 2026)
**Decided:** keep C (hybrid). A-only and B-only are tossed as standalone styles. Reference render: `06_C_v2_unified_grizzly.mp4` (Jarvis's box; code `production/mb2/render.py hybrid2`).
- **Panels** carry the money shots: frame 0 (hook), the decision beat (play dead / squish it / run), the fight or payoff, and the loop shot. **Rig** carries the action beats between them (chase, race, gag, reaction close-up).
- **One reference sheet, every time:** `production/mb2/art/meatball_ref_sheet_v1.jpg` is passed as the first reference image on every panel generation, plus one existing panel for the location and lighting. Never generate Meatball without it. A panel where Meatball drifts (cap shape, eye size, limb style) is regenerated, not used.
- **Rig matched to the panels:** silhouette ink line 11 px on screen and interior lines 7 px, constant at any zoom (`characters.ow()`). Ink is #1A1410. Meatball palette is #6E3D22 body, #4A2715 shadow, #8F5534 light, sauce #D42A22 to #9A1A14 with a white gloss. The bear is #6B4428 with #4A2E1A shadow, a #A87347 muzzle, and no pale belly. Shading is a soft painted gradient with one shadow tone, and fur-tuft edges on furry animals.
- **Same world:** rig shots stand on a painted plate generated in the panel style for that location (one plate per location, mirror-tiled for scrolling). No flat procedural skies or snow when a panel shows a different place.
- **One finish over everything:** shared grade (slightly warm), paper grain (overlay, 50%), and a 0.8 px soften on rig layers so vectors match the upscaled panels.
- **Matched transitions:** every panel<->rig cut is a diagonal ink-brush wipe (0.24 s) with a whoosh. Rig<->rig and panel<->panel cuts keep the 3-frame white whip. The loop shot ends on frame 0's framing.
- **AI label ON** (panels are generated images), per standing orders.

## Topic lane and cadence (Moondog88, Nov 15 2026)
- **Lane:** Would Meatball Survive? (big dangerous animals) plus house bugs and spiders (Things Living In Your House). **Paused:** news, CIA/nukes, pets.
- **Bug long-forms are allowed** again. This overrides the MASTER_ORDERS 11/11 "no new bug videos" rule.
- **Cadence:** 3 Shorts a day, unchanged.

## Thumbnails (Moondog88, Nov 15 2026)
- **Kept directions:** "TOO SLOW" (chase) and "PLAY DEAD?" (question). **Tossed:** "DON'T RUN".
- **v2 rules** (samples in `channels/packaging/thumbs-v2/`, plus `*_168.png` phone checks): one huge Meatball face with one clear emotion, one dominant threat, a flat clean background (yellow, teal, red), 2 words in Anton with 28-30 px black outline, exactly one red word, and words kept out of the bottom-right timestamp zone. The art comes from the same reference sheet. Every thumbnail must read at 168x94. These follow `packaging/thumbnail-spec-two-styles-1115.md` on main, except that PLAY DEAD? uses a flat teal field instead of white (white reads weaker at 168 px). Moondog88 decides which spec wins.
- `thumb_v2_3_dont-move.png` is a third candidate in the PLAY DEAD? family, for keep-or-toss.

## Render gate additions (postkit)
- Shots/min ≥ 30 on Shorts (planned shots from the timeline, not frame diff).
- No framing held over 2.5 s on Shorts.
- Frame 0 motion > 0 and the subject's face visible (manual check on the contact sheet).
- Loudness -14 ±0.5 LUFS, TP ≤ -1.5 dBTP, measured on the final encoded file (audio spec §5). mb2 lands -14.1 / -2.0.
- Panel art: Meatball matches the reference sheet (manual check on the contact sheet).
