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

## Which style
- **A, Rig v2 (procedural):** $0, fully consistent, fastest. The art is simpler than the outliers.
- **B, Illustrated panels:** closest to what the 4.6M Short looks like, and the strongest picture. Each Short needs about 6-8 generated images plus a reference sheet to keep Meatball on-model. Risk: Meatball drifts slightly between images (visible in the samples), and YouTube/TikTok AI-content disclosure applies (the AI label is already ON per standing orders).
- **C, Hybrid:** the style clash between flat rig and painted panels is visible. Recommend against unless the rig is restyled to match.
- **Jarvis recommendation:** B for the hook and payoff shots on WMS and pet Shorts, A for in-between action and for volume days. Then upgrade the rig art toward B's line weight so C stops clashing. Test before locking: alternate A and B on the same series for 6 Shorts each, judged on viewed-vs-swiped and average % viewed at 48 h.

## Render gate additions (postkit)
- Shots/min ≥ 30 on Shorts (planned shots from the timeline, not frame diff).
- No framing held over 2.5 s on Shorts.
- Frame 0 motion > 0 and the subject's face visible (manual check on the contact sheet).
- Loudness -14 ±0.5 LUFS, TP ≤ -1.0 (audio spec §5).
