# Queue audit: Meatball Myths, Nov 16–30, 2026 (times are ET)

Read-only audit by the Shorts Editor, run Mon 11/16 ~8:45 PM ET. Nothing was created, changed, rescheduled, deleted or sent.

**Summary:** 42 Meatball posts are queued 11/16–11/25 in the repo queue (20 YouTube: 17 Shorts + 3 long-forms; 22 TikTok). After 11/25 nothing is queued, except the 12/5 polar long-form, which is outside the window. Metricool brand 8135499 holds **no Meatball posts**. It holds 3 off-brand Etsy-printable Shorts on the Meatball YouTube channel plus 20 @fureverfaces shop TikToks. Main problems:
- **TikTok spacing:** 5 days (11/16–11/20) have TikToks less than 3 h apart.
- **Old look:** every queued Meatball video I could open (13 files) uses the old stick-figure rig or the low-poly 3D look, not the locked cartoon kit.
- **Length:** no Short is over 20 s. Cluster flies sits right at 20.000 s.
- **Amazon:** none found in anything I could read. The real Meatball captions in the old Metricool brand were not readable.

## Sources read
- **Metricool:** `getBrandSettings` returned 1 brand, 8135499 "fureverfaces" (TikTok = @fureverfaces, YouTube = UCw98RQD81t_339LX5EJqcrg, the Meatball channel). `getScheduledPosts` covered 2026-11-16 00:00 to 11-30 23:59 ET (America/New_York, extendedRange on) and returned 23 posts.
- **Repo queue:** The posting queue is `skills/oh-meatball/data/posted.csv` (with `post-ids.csv` and `pending-swaps.csv`) on mooneyn60-art/skills, branch `claude/youtube-monetization-strategy-m9vz6i`. I fetched it raw on 11/16 at ~8:40 PM ET. It is newer than the box copies in /workspace/skills-readonly (dated 11/15).
- **Side-hustles main** (commit c3004e5, 11/16 8:37 PM ET): `channels/plan/meatball-push-1116/posting-plan-1116-1205.md`, `tiktok-blockers.md`, `channels/team/schedule.md` and TASKS.md (HOUSE STYLE LOCKED and 1K-JAIL FIXES of 11/16 8:18–8:20 PM, PLAN SWITCH of 6:43 PM). **There is no READ.md or READY.md anywhere in Side-hustles main.** A repo-wide name and content search found none.
- **Media:** I downloaded the 17 Metricool media URLs logged in `post-ids.csv` and in today's Metricool response, ran ffprobe on each and looked at 4 frames per file. These are the URLs as last logged. If a post's media was swapped later in the old brand, I could not see it.
- **Local files:** `/workspace/research/2026-11-16-queued-shorts-lengths.csv`, `/workspace/drafts/tiktok-samples-1116/`, `/workspace/drafts/shorts-push-1116/` (scripts only, nothing rendered, so nothing queued from it).

## Look key
- **Stick-figure (seen):** I opened the frames. Meatball is a ball head on a black stick body, the "Meatball 2.0" rig that `channels/animation/kit-v1.md` l.93 says not to use. HOUSE STYLE (TASKS.md l.52-55) says "No stick figure, no stock footage, no other styles", and 1K-JAIL #5 says "Re-skin the older queued Shorts before they post, or hold them."
- **3D low-poly (seen):** This is the hook-test/sim3d 3D style. It is an "other style", not the cartoon kit.
- **Stick-figure? (unverified):** No media URL. The guess comes from the `drawn-house`/`drawn-tt` episode folder, the same pipeline as the stick-figure files I opened.
- **3D? (unverified):** No media URL. The guess comes from the `sim3d`/`hook-test` folder; research/69 calls sim3d "the 3D version".
- **Product/stock graphics (seen):** Etsy printable mockups on a red background, with no Meatball.

## Table: all queued posts, 11/16–11/30 (ET)

Slots before ~8:45 PM 11/16 have passed. Whether they published is unverified, because the old Metricool brand (7521392, the one in post-ids.csv) no longer shows in the connected Metricool account.

| Date/time ET | Platform | Title / slug | Length | Look | Source | Flags |
|---|---|---|---|---|---|---|
| Mon 11/16 10:00 | YT Short | yt-dog-tail-wag-v6 "Your Dog's Tail Wag May Lean to Its Right…" | 17.8 s (documented, not measured) | Stick-figure? (unverified) | repo | slot passed |
| Mon 11/16 12:00 | TikTok | tt-naked-mole-rat | unknown | Stick-figure? (unverified) | repo | Under 3 h from the 12:25–12:36 live batch; slot passed |
| Mon 11/16 16:00 | YT Short | yt-dust-mites-v6 "Female Dust Mites in Your Bed Lay About 50 Eggs" | 19.133 s (ffprobe) | Stick-figure (seen) | repo | Old look; over the 18 s test cap; same channel and minute as the Metricool printable Short; slot passed |
| Mon 11/16 16:00 | YT Short | "POV: Your Kid Gets a Letter BACK from Santa" (Etsy printables) | 14.000 s (ffprobe) | Product graphics (seen) | Metricool (PUBLISHED) | Off-brand on the Meatball channel; collides with dust-mites |
| Mon 11/16 19:00 | YT Short | yt-cat-lilies-v6 "True Lilies Are Poisonous to Cats…" | 18.967 s (ffprobe) | Stick-figure (seen) | repo | Old look; the plan and lengths CSV list the stinkbug explainer here instead; slot passed |
| Mon 11/16 19:00 | TikTok | tt-bison-wms "What to Do If a Bison Charges You" | 88.833 s (ffprobe) | Stick-figure (seen) | repo | Old look; over the 75 s spec; under 3 h from 20:15 and 21:30; slot passed |
| Mon 11/16 20:15 | TikTok | tt-dog-guilty-look | unknown | Stick-figure? (unverified) | repo | 1 h 15 m after 19:00; slot passed |
| Mon 11/16 21:30 | TikTok | tt-electric-eel | unknown | Stick-figure? (unverified) | repo | 1 h 15 m after 20:15 and 2.5 h after 19:00 (**still upcoming tonight**) |
| Tue 11/17 10:00 | YT Short | yt-fungus-gnats-v6 | unknown (no file) | Stick-figure? (unverified) | repo | Length gap |
| Tue 11/17 10:00 | TikTok | "This doodle made the list. Mostly." | — | — | Metricool (@fureverfaces) | Not Meatball |
| Tue 11/17 12:00 | TikTok | tt-cassowary | unknown | Stick-figure? (unverified) | repo | — |
| Tue 11/17 15:00 | TikTok | "This doodle is Mom's favorite." | — | — | Metricool (@fureverfaces) | Not Meatball |
| Tue 11/17 16:00 | YT Short | yt-carpet-beetle-window-v6 | 18.233 s (ffprobe) | Stick-figure (seen) | repo | Old look; collides with the Metricool elf Short |
| Tue 11/17 16:00 | YT Short | "Your Christmas Elf Is Coming Back…" (Etsy printables) | 14.000 s (ffprobe) | Product graphics (seen) | Metricool (PENDING) | Off-brand on the Meatball channel; same minute as carpet-beetle; 4 YT Shorts that day |
| Tue 11/17 18:00 | TikTok | "POV: she says she doesn't need anything…" | — | — | Metricool (@fureverfaces) | Not Meatball |
| Tue 11/17 19:00 | YT Short | yt-earwig-hook "1 Ear Case in 10 Centuries" | unknown (no file) | 3D? (unverified) | repo | Length gap |
| Tue 11/17 19:00 | TikTok | tt-shark-wms "What to Do If a Shark Comes Close" | 86.867 s (ffprobe) | Stick-figure (seen) | repo | Old look; over 75 s; 2.5 h before 21:30; the plan had tts-dog-tail-wag here |
| Tue 11/17 21:30 | TikTok | tt-hummingbird | unknown | Stick-figure? (unverified) | repo | Under 3 h after 19:00 |
| Wed 11/18 10:00 | YT Short | yt-carpenter-ant-hook | unknown (no file) | 3D? (unverified) | repo | Length gap |
| Wed 11/18 10:00 | TikTok | "Matching with the dog. On purpose." | — | — | Metricool (@fureverfaces) | Not Meatball |
| Wed 11/18 12:00 | TikTok | tt-sea-otter | unknown | Stick-figure? (unverified) | repo | — |
| Wed 11/18 16:00 | YT Short | "Breaking News: You Made Santa's Nice List" (Etsy printables) | 14.000 s (ffprobe) | Product graphics (seen) | Metricool (PENDING) | Off-brand on the Meatball channel; 1 h before the 17:00 long-form, which breaks the midweek "Shorts at 10:00 and 19:00 only" rule |
| Wed 11/18 17:00 | YT long-form | christmas-tree-check "Never Bring a Christmas Tree Inside…" | unknown | unverified | repo | Subscriber-notifications-off toggle still to confirm (per plan) |
| Wed 11/18 18:00 | TikTok | "Yes, that's this doodle." | — | — | Metricool (@fureverfaces) | Not Meatball |
| Wed 11/18 19:00 | YT Short | yt-christmas-tree-bugs-v6 | 19.500 s (ffprobe) | Stick-figure (seen) | repo | Old look; over 18 s |
| Wed 11/18 19:00 | TikTok | yt-bedbugs-explainer (YT-named file) | unknown | 3D? (unverified, sim3d) | repo | Under 3 h before 20:15 |
| Wed 11/18 20:15 | TikTok | tt-christmas-tree-check | unknown | Stick-figure? (unverified) | repo | 1 h 15 m after 19:00 |
| Wed 11/18 21:30 | TikTok | tt-drain-fly | unknown | Stick-figure? (unverified) | repo | 1 h 15 m after 20:15 |
| Thu 11/19 10:00 | YT Short | yt-housefly-hook | unknown (no file) | 3D? (unverified) | repo | Length gap |
| Thu 11/19 10:00 | TikTok | "Nice list (pending)." | — | — | Metricool (@fureverfaces) | Not Meatball |
| Thu 11/19 12:00 | TikTok | tts-dog-stare "Why Does My Dog Stare at Me?" | 25.200 s (ffprobe) | Stick-figure (seen) | repo | Old look; under 61 s, so it misses Creator Rewards |
| Thu 11/19 15:00 | TikTok | "A gift for this doodle's person. $17.99." | — | — | Metricool (@fureverfaces) | Not Meatball |
| Thu 11/19 16:00 | YT Short | yt-pantry-vs-clothes-moth-v6 | 18.233 s (ffprobe) | Stick-figure (seen) | repo | Old look |
| Thu 11/19 18:00 | TikTok | "Chief treat officer." | — | — | Metricool (@fureverfaces) | Not Meatball |
| Thu 11/19 19:00 | YT Short | yt-cluster-flies-v6 "Why Thousands of Flies…" | 20.000 s (ffprobe) | Stick-figure (seen) | repo | Old look; right at the 20 s limit; plan says the "thousands" wording must be fixed or the slot left empty |
| Thu 11/19 19:00 | TikTok | tts-grizzly-wms | unknown | Stick-figure? (unverified) | repo | Under 3 h before 21:30 |
| Thu 11/19 21:30 | TikTok | tt-honey-badger | unknown (no media URL in post-ids) | Stick-figure? (unverified) | repo | 2.5 h after 19:00 |
| Fri 11/20 10:00 | YT Short | yt-fruitfly-explainer | unknown (no file) | 3D? (unverified, sim3d) | repo | Length gap |
| Fri 11/20 10:00 | TikTok | "This doodle has 24 hours to get off the naughty list." | — | — | Metricool (@fureverfaces) | Not Meatball |
| Fri 11/20 15:00 | TikTok | "This doodle is Dad's best friend." | — | — | Metricool (@fureverfaces) | Not Meatball |
| Fri 11/20 16:00 | YT Short | yt-booklice-cupboard-v6 | 19.767 s (ffprobe) | Stick-figure (seen) | repo | Old look; over 18 s |
| Fri 11/20 18:00 | TikTok | "A gift for the doodle mom." | — | — | Metricool (@fureverfaces) | Not Meatball |
| Fri 11/20 19:00 | YT Short | yt-clothesmoth-explainer | unknown (no file) | 3D? (unverified, sim3d) | repo | Length gap |
| Fri 11/20 19:00 | TikTok | yt-silverfish-hook (YT file) | 18.698 s (ffprobe) | 3D low-poly (seen) | repo | Old look; under 61 s; same file also queued on YT 11/21 14:00; 2.5 h before 21:30 |
| Fri 11/20 21:30 | TikTok | tt-woodpecker | unknown (no media URL in post-ids) | Stick-figure? (unverified) | repo | 2.5 h after 19:00 |
| Sat 11/21 08:00 | YT long-form | longform-house-centipede-v2 | unknown | 3D? (unverified, sim3d) | repo | — |
| Sat 11/21 10:00 | TikTok | "The whole family made the list this year." | — | — | Metricool (@fureverfaces) | Not Meatball |
| Sat 11/21 11:00 | YT Short | yt-bison-wms-v6 | 19.433 s (ffprobe) | Stick-figure (seen) | repo | Old look; same topic as tt-bison-wms 11/16 |
| Sat 11/21 12:00 | TikTok | tts-dog-turkey "Can Dogs Eat Turkey?" | 25.133 s (ffprobe) | Stick-figure (seen) | repo | Old look; under 61 s |
| Sat 11/21 14:00 | YT Short | yt-silverfish-hook "Your Book Has a Night Visitor" | 18.698 s (ffprobe) | 3D low-poly (seen) | repo | Old look; duplicate file (also TikTok 11/20) |
| Sat 11/21 15:00 | TikTok | "Zoomies incoming. $17.99." | — | — | Metricool (@fureverfaces) | Not Meatball |
| Sat 11/21 18:00 | TikTok | "This doodle is shopping for his mom. Unsupervised." | — | — | Metricool (@fureverfaces) | Not Meatball |
| Sat 11/21 19:00 | TikTok | tt-waterbug | unknown | Stick-figure? (unverified) | repo | — |
| Sun 11/22 10:00 | TikTok | "Which one is your doodle? Be honest." | — | — | Metricool (@fureverfaces) | Not Meatball |
| Sun 11/22 15:00 | TikTok | "A tee for this doodle's person. $26.00." | — | — | Metricool (@fureverfaces) | Not Meatball |
| Sun 11/22 18:00 | TikTok | "Christmas order-by date: Dec 5." | — | — | Metricool (@fureverfaces) | Not Meatball |
| Sun 11/22 19:00 | TikTok | tt-polar-bear "A Polar Bear's Fur Isn't White…" | unknown | Stick-figure? (unverified) | repo | Plan: wording check owed ("transparent fur" is marked unsafe in pack 98) |
| Mon 11/23 10:00 | TikTok | "POV: gift for the doodle mom." | — | — | Metricool (@fureverfaces) | Not Meatball |
| Mon 11/23 18:00 | TikTok | "Your doodle is going on the tree this year." | — | — | Metricool (@fureverfaces) | Not Meatball |
| Mon 11/23 19:00 | TikTok | tt-platypus | unknown | Stick-figure? (unverified) | repo | — |
| Tue 11/24 19:00 | TikTok | tt-wombat | unknown | Stick-figure? (unverified) | repo | — |
| Wed 11/25 17:00 | YT long-form | night-shift-v2 "What Crawls Through Your House While You Sleep" | unknown | unverified | repo | Notifications-off toggle to confirm (per plan) |
| Wed 11/25 19:00 | YT Short | yt-teaser-night-shift | unknown (no file) | Stick-figure? (unverified) | repo | Length gap |
| Wed 11/25 19:00 | TikTok | tt-greenland-shark | unknown | Stick-figure? (unverified) | repo | — |
| 11/26–11/30 | — | nothing queued on either platform | — | — | repo + Metricool | Empty |

Already live (not queued, listed for context): the 7 TikTok cuts in `/workspace/drafts/tiktok-samples-1116/`, 61.3–71.6 s each. TASKS.md l.79 dates the "11/16 12:25-12:36 PM batch" and says it is stuck at 3–6 views. Their contact sheets also show the stick-figure rig.

Counts:
- **Meatball, repo queue:** YouTube 20 (17 Shorts + 3 long-forms), TikTok 22.
- **Metricool brand 8135499:** YouTube 3 (off-brand printables on the Meatball channel, 1 already published), TikTok 20 (all @fureverfaces shop posts, 1 already published, not Meatball).

## Flag list
1. **TikToks less than 3 h apart:**
   - 11/16: 19:00, 20:15, 21:30. Also the 7-post live batch at 12:25–12:36, 25–36 min after the 12:00 slot.
   - 11/17: 19:00 → 21:30.
   - 11/18: 19:00, 20:15, 21:30.
   - 11/19: 19:00 → 21:30.
   - 11/20: 19:00 → 21:30.
   - The @fureverfaces Metricool TikToks are all at least 3 h apart (10:00/15:00/18:00).
2. **Old look (seen in frames), stick-figure:** dust-mites, carpet-beetle-window, christmas-tree-bugs, pantry-vs-clothes-moth, cluster-flies, booklice-cupboard, cat-lilies, bison-wms (YT) and on TikTok tt-bison-wms, tt-shark-wms, tts-dog-stare, tts-dog-turkey.
3. **Old look (seen), 3D low-poly:** yt-silverfish-hook (queued on both TikTok and YT).
4. **Look unverified:** all 12 `drawn-tt` TikToks, tt-dog-guilty-look, tt-christmas-tree-check, tt-drain-fly, tts-grizzly-wms, the 5 sim3d/hook-test YT Shorts without media (earwig, carpenter-ant, housefly, fruitfly, clothesmoth), the drawn-house fungus-gnats Short and night-shift teaser, the dog-tail-wag Short, yt-bedbugs-explainer, and the 3 long-forms. The folder names point to the same old pipelines. Per 1K-JAIL #5 these need a re-skin or a hold.
5. **Stock/product look, off-brand:** 3 Etsy-printable Shorts (Santa letter, elf letter, nice list) are queued in Metricool on the Meatball YouTube channel. Two are pending (11/17 16:00, 11/18 16:00) and one was published 11/16 16:00. Two sit at the same minute as a Meatball Short, which makes 4 YT Shorts on 11/16 and 11/17. The 11/18 one breaks the midweek "10:00 and 19:00 only" rule.
6. **YT Shorts over 20 s:** none measured. Cluster-flies is exactly 20.000 s, at the limit. Unmeasured: fungus-gnats, earwig, carpenter-ant, housefly, fruitfly, clothesmoth, night-shift teaser, plus dog-tail-wag (17.8 s, documented only). 8 measured Shorts run 18.2–19.8 s, over the 16–18 s test target but within the 20 s rule.
7. **TikTok length:**
   - Under 61 s, so they miss Creator Rewards: tts-dog-stare (25.2 s), tts-dog-turkey (25.1 s), yt-silverfish-hook (18.7 s).
   - Over the 75 s spec: tt-bison-wms (88.8 s), tt-shark-wms (86.9 s).
8. **Duplicates:**
   - yt-silverfish-hook.mp4 is queued on TikTok 11/20 19:00 and on YT 11/21 14:00.
   - Bison runs on both platforms (TikTok 11/16, YT 11/21; different cuts).
   - The queued silverfish and dust-mite topics repeat topics of 11/16's live TikTok samples.
9. **Repo queue vs plan/CSV disagreements:**
   - 11/16 19:00 YT is now cat-lilies in posted.csv, but the plan and the lengths CSV say stinkbug explainer. The stinkbug explainer is no longer in the queue.
   - 11/17 19:00 TikTok is now tt-shark-wms; the plan says tts-dog-tail-wag (hold).
   - tt-bison-wms at 11/16 19:00 TikTok is not in the plan.
   - The plan's "hold pets / off-lane" calls predate the 6:43 PM PLAN SWITCH (pets are main again), so they may be stale.
10. **Metricool vs repo:** I couldn't cross-check. Every Meatball Metricool id in post-ids.csv is under brand 7521392, which the connected Metricool account no longer lists. Metricool 8135499 has zero Meatball posts. The two queues overlap only on the shared YouTube channel (flag 5).
11. **Amazon:** zero mentions in the 23 Metricool captions, in the posted.csv titles, in the TikTok samples' captions.md and in shorts-push-1116.
12. **Side note (not asked; seen in frames):** on-screen profanity, partly masked: "F**KING" (bison-wms TikTok, dog-stare), "SH*T" (bison-wms TikTok), "HELL" (cat-lilies), "DAMN" (carpet-beetle, pantry moth).

## Proposed TikTok slots (@meatballmyths)
These are for spacing only. Each post keeps its own content flags above, and nothing was changed. The pattern is 10:00 (test) / 14:00 / 19:00 (anchor) ET, which is 2–3 a day, at least 4 h apart and never batched. I moved only already-queued items and invented none.

| Day | 10:00 (test) | 14:00 | 19:00 (anchor) |
|---|---|---|---|
| Mon 11/16 | — | — | (passed) Move tonight's 21:30 tt-electric-eel to Sun 11/22 10:00 |
| Tue 11/17 | tt-cassowary (was 12:00) | tt-hummingbird (was 21:30) | tt-shark-wms |
| Wed 11/18 | tt-sea-otter (was 12:00) | yt-bedbugs-explainer (was 19:00) | tt-christmas-tree-check (was 20:15; 2 h after the 17:00 long-form) |
| Thu 11/19 | tts-dog-stare (was 12:00) | tt-honey-badger (was 21:30) | tts-grizzly-wms |
| Fri 11/20 | tt-drain-fly (was 11/18 21:30) | tt-woodpecker (was 21:30) | yt-silverfish-hook |
| Sat 11/21 | tts-dog-turkey (was 12:00) | — | tt-waterbug |
| Sun 11/22 | tt-electric-eel (moved) | — | tt-polar-bear (only if the wording check passes) |
| Mon 11/23 | open | — | tt-platypus |
| Tue 11/24 | open | — | tt-wombat |
| Wed 11/25 | open | — | tt-greenland-shark |
| Thu 11/26–Mon 11/30 | open | open | open (nothing queued; fill only with new 61–75 s chapter cuts once they're rendered) |

## Data gaps
- No READ.md or READY.md exists in Side-hustles main. The real queue is posted.csv in the skills repo, and the Side-hustles posting plan only describes it.
- Old Metricool brand 7521392 (the Meatball queue ids) is not visible to the connected Metricool account. So I couldn't confirm whether those posts are still scheduled, already published, or changed, and I couldn't read their captions. For the same reason, I couldn't check Amazon mentions in the real Meatball captions; I checked titles only.
- @meatballmyths isn't connected to Metricool (TikTok is @fureverfaces), so there's no TikTok schedule I can verify there.
- 28 of the 42 Meatball slots have no media URL or file on the box, so their length and look are unverified.
- Media were judged from the last logged URL; later media swaps would not show.
- The status of the 11/16 slots that have passed is unverified.
