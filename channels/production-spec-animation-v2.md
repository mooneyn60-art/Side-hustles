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

## Outlier study, Nov 15 2026 (28 videos, in our lane and adjacent ones)
Data: `analytics/outliers-1115/` (CSV with views, subs, views per sub, length, age, thumbnail URL, the first 5 s of speech; contact sheet with ours below; frames at 0/0.5/1.5/2.8 s for the top 8). Ratio = views ÷ the channel's subscribers: median 39x, minimum 5.4x. Thumbnail coding is Jarvis's own manual read. YouTube's public pages don't show CTR for other channels, so these patterns come from videos that won, not from measured CTR.
1. **The hook opens on "You":** 7 of the top 8 start with "You…" (the 8th is music only), with 9-14 words in the first 3 s (about 180-280 wpm). 4 of the 8 give a concrete number by 5 s ("6 minutes", "1,200 beats a minute", "50 homes").
2. **3 words or fewer on the thumbnail:** 20 of 28 (median 3). The words add to the title instead of repeating it. Hummingbird example: the title is "Why It Sucks…", the thumbnail says "It Dies EVERY NIGHT".
3. **One dominant creature, 50% or more of the frame height:** 14 of 28, and 7 of 7 in the hand-drawn "born as" group. Our old long-form thumbnails led with a narrator and props.
4. **POV or identity title formula** ("Why It Sucks to Be Born as", "Your Life as", "What If You Were"): 9 of 28 and 4 of the top 10, the most common single formula. "You/your" is in 11 of 28 titles, and a stakes word (worst, never, kill, deadliest) in 11 of 28.
5. **Short titles:** the median is 53 characters and 10 words. Ours are 60 characters.
6. **Flat, clean, bright background:** 7 of the 9 hand-drawn outliers (white, yellow or a flat colour).
7. **Length and pace:** 17 of 28 are 8 minutes or longer (median 8.4 min). The Short outliers (Sketching the Wild, 4.7M and 3.4M) change the picture every 0.5-1 s (3-4 pictures in the first 2.8 s) and use small 2-3 word captions. 12 of 28 are under a year old (the "What If You Were Born as" channel had 4 hits in Nov 2026 alone), so the format is still hot.

## CTR: what's realistic (target 10%), built on the Studio baseline from Nov 15
- **Our real numbers (Studio, read Nov 15):**
  - Long-form, last 28 days: 18.5K impressions, **2.8% CTR**, 946 views, average view duration (AVD) **1:30**.
  - Traffic: Suggested 58%, Browse 35%, Search 2.8%.
  - Lifetime CTR, bug lane: 3 Bugs Never Kill **5.44%** (1,856 impressions), Don't Kill the Spider **4.63%** (1,771), 3 More Bugs **4.37%** (1,510). Weighted **4.8%**. (6 Creatures shows 6.06%, but on only 33 impressions.)
  - Lifetime CTR, other topics: weird facts 1.82%, extinct 2.53%, wolves 1.99%, house cat 1.95%, myths 1.25%, CIA under 1%. **About 2.0%.**
  - **The bug lane gets about 2.4x the CTR.**
  - Shorts, last 28 days: 81.8K views, 46.3% stayed vs 53.7% swiped, 93.6% from the Shorts feed. Studio doesn't show feed impressions per Short.
  - Audience: 99.3% new viewers. US 20.5%, PH 9.9%, IE 9.6%, UK 9.3%. Ages 25-44. 61% mobile.
- **Official (YouTube Help, "Impressions & CTR FAQs"):**
  - Half of channels and videos sit between 2% and 10%.
  - CTR falls as Home (Browse) impressions grow and is higher from channel pages.
  - Compare like with like over time, and don't judge on small impression counts.
  - High CTR with low watch time gets fewer impressions.
- **Community-observed (not official):** Browse 2-5%, Suggested 3-8% (one 2025 agency report: 9.5%), Search 5-15%.
- **Our traffic mix is 93% Suggested + Browse.** So 10% overall would put us in about the top tier. Realistic targets (estimates):
  - Bug-lane long-forms: overall **6-7% within 60 days** (from 4.8%).
  - Search traffic and the first 48 h from subscribers: **10%+**.
  - Browse: **4-6%**.
  - Shorts are judged on stayed vs swiped: **from 46% to 55-60% stayed**.
  - AVD matters as much as CTR: **from 1:30 to 3:00** (40% or more of a 6-8 min video).

## Packaging checklist (every upload; Jarvis or Claude ticks it in the upload log)
1. **Lane:** Would Meatball Survive? or Things Living In Your House (bugs, spiders). Anything else waits for Moondog88.
2. **Title:** 55 characters or fewer, written as "you/your" plus a situation or stakes, or the POV formula ("Your Life as…", "What If You…"). One number if it's sourced. No series tag in long-form titles: the series goes in the playlist and the first description line.
3. **Thumbnail:** 3 words or fewer, exactly one red word, and the words add something the title doesn't say. One huge Meatball face with one clear emotion, plus one dominant threat in the top half of the frame, close to him. Flat clean background. Art comes from `art/meatball_ref_sheet_v1.jpg`.
4. **Safe zones:** nothing important in the bottom-right 20% × 15% (the timestamp badge). Words go top-left or top-right.
5. **168x94 test:** export `*_168.png`. Every word and both faces must read. If not, cut a word or zoom the art.
6. **Frame 0 matches the thumbnail:** same threat, same pose, same colours. The spoken words in the first 5 s include the thumbnail's promise.
7. **Hook:** the first words are "You…", 9-14 words in 3 s, a sourced number by 5 s where one exists, and a choice or question that pays off later (the comment trigger).
8. **Pace:** Shorts change the picture every 0.5-1.2 s (3 or more pictures in the first 3 s). Long-forms hold 2-4 s per picture.
9. **Truthfulness:** the thumbnail and title never claim more than the video shows (clickbait costs watch time and impressions, per YouTube's FAQ).
10. **Review:** after 7 days and 1,000+ impressions, log CTR by traffic source and average view duration. Don't change the thumbnail before then.

## On-screen captions spec (Shorts + TikTok)
- **Burned in, Anton:** 112 px, with the keyword in yellow at 124 px. Black outline at 18% of the size plus a soft shadow. 1-3 words per group and at most 16 characters per line.
- **Word-by-word highlight:** the word being spoken turns yellow (#FFD21F) and scales to 1.08× for its duration. Planned for mb2; the v3 sample still pops a whole group at once.
- **Safe zone (community and ads-placement guidance, not a YouTube help article):** keep captions centred, inside x 90-900 and y 1180-1500. Leave the bottom 400 px clear (title, description, sound bar), the right 160 px clear (like, comment and share buttons) and the top 220 px clear. Fact cards stay in the top band y 260-700.
- **Upload an SRT** of the exact script on YouTube (we have exact word timings from TTS) rather than relying on auto-captions. On TikTok, turn on auto-captions and also say the search phrase out loud in the first line.

## Post captions, descriptions and hashtags
- **Official, YouTube:** hashtags can go in the title or the description. Up to 3 from the description show by the title. A video with more than 60 hashtags has all of them ignored. "Ordinary descriptive tags or repetitive sentences in the description" are prohibited. **Audit finding:** our long-form descriptions end with comma-separated keyword lists, and we should cut those. Shorts use 4-7 hashtags with a varied lead tag. Long-forms use none.
- **Official, TikTok:** "How TikTok recommends videos #ForYou" lists video information such as captions, sounds and hashtags as signals. Creator Rewards adds "search value" to its formula, and search views count after 30 s (Creator Academy). Creator Search Insights shows in-demand and content-gap searches.
- **YouTube Short template:** title "[you/stakes line, 55 characters or fewer] [1 emoji]". Description: line 1 answers the search question in one sentence with the keyword. Line 2 is the source. Line 3 is "Full video: [newest long-form in the series]". The last line has 3-4 hashtags.
- **YouTube long-form template:** 2-3 sentences that restate the promise with the keyword, then chapters, sources, and 3 hashtags at the end. No keyword lists.
- **TikTok template:** "[the search phrase, lowercase, exactly as people type it] [emoji] [one sentence answer with a sourced number] [a question for the comments]" followed by 3-5 hashtags.
- **Hashtag sets** (the first 3 show on YouTube; [x] = the creature or animal):
  - YouTube, WMS: `#wouldyousurvive #[x]attack #meatballmyths` (Shorts may add `#shorts` last)
  - YouTube, Things Living In Your House: `#[x] #bugsinyourhouse #meatballmyths` (Shorts may add `#thingslivinginyourhouse #shorts`)
  - TikTok, WMS: `#wouldyousurvive #[x]facts #animalfacts #learnontiktok #meatballmyths`
  - TikTok, house bugs: `#[x] #bugsinyourhouse #bugtok` (spiders: `#spidertok`) `#learnontiktok #meatballmyths`

## Monetization timeline (estimates; thresholds checked Nov 15 2026 on YouTube Help)
- **Fan funding tier, available in the US:** 500 subscribers, 3 public uploads in 90 days, and either 3,000 public long-form watch hours in 12 months or 3M Shorts-feed views in 90 days. Unchanged after Feb 1, 2027.
- **Ads tier:** 1,000 subscribers and either 4,000 hours in 12 months or 10M Shorts views in 90 days. **From Feb 1, 2027, for channels not yet in YPP: 8,000 hours or 20M Shorts views.** Getting in before Feb 1 locks in the current bar. Shorts-feed watch time never counts toward hours.
- **Where we are (Studio Earn tab, Nov 10):** 1,017 subscribers.
  - **10 public watch hours**, about 24 by Nov 15 (estimate: 28-day views × AVD gives about 0.85 h a day).
  - **26K qualifying Shorts views** in 90 days. That's about 40% of public Shorts views (an estimate). It lines up with the 46% stayed rate, so assume about 45% of public views count from now on.
  - Studio shows **"Apply now" for the fan-funding tier**, but the Earn tab shows the thresholds not met. Moondog88 should check what that button covers before applying, and Jarvis won't apply.
- **A, current trajectory** (about 2.9K public Shorts views a day, 0.85 h a day): neither tier reached. That's about 0.1M counted Shorts views per 90 days, and 3,000 hours would take about 9 years.
- **B, the plan works:**
  - Assumptions: by mid-Jan, Shorts average about 75K public views a day (median about 8K × 3 a day plus a 500K breakout every 2 weeks; bug Shorts top out at about 2K today). Long-forms reach 3K impressions a day × 5% CTR × 3:00 AVD, about 7 h a day.
  - Fan-funding tier via Shorts around **Apr 2, 2027**.
  - Ads tier not reached in 2027 (8,000 hours or 20M after Feb 1).
- **C, upside:**
  - Assumptions: a format hits, so Shorts reach about 250K public views a day by early Jan and long-forms about 40 h a day.
  - Fan-funding tier around **Jan 3, 2027**. Ads tier via hours around **Jun 24, 2027** at the 8,000 bar.
  - **With one bug long-form outlier by about Jan 10 (about 80K views at 3:00 AVD, which is 4,000 hours), the ads tier comes around Jan 11, 2027, under the old bar.**
- **Takeaway:**
  - The only realistic way into the ads tier before the bar doubles on **Feb 1, 2027** is one long-form outlier. At a 3:00 AVD it needs about 80K views; at today's 1:30 it needs 160K.
  - So long-form packaging (CTR) and retention (AVD) are the levers. Hours count over 12 months, Shorts over 90 days.
  - Shorts are the realistic path to the fan-funding tier (3M counted, about 33K counted or 75K public views a day).
- **TikTok:** already in Creator Rewards (Moondog88). Videos must run over 1 minute with at least 1,000 For You views, and qualified views need 5 s or more (30 s or more from Search). Our TikToks run 64-92 s, so they qualify on length.
