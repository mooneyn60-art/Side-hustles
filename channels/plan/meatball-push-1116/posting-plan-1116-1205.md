# Posting plan — Mon 11/16 through Sat 12/5, 2026

**Documents only. Do not schedule, post, or change Studio or TikTok from this file.**

Times are America/New_York (ET, UTC-5). Written Mon 11/16/2026 morning.

This is the YouTube Shorts + TikTok cadence for Meatball Myths (YouTube `UCw98RQD81t_339LX5EJqcrg`, TikTok `@meatballmyths`), plus slots for the two approved retention-v2 Shorts. Every live post still needs Moondog88's explicit okay. Moondog88 posts TikTok himself unless he says otherwise.

---

## Rules used

- Focus: Would Meatball Survive? plus house bugs and spiders. News, CIA and pets are **paused**. Hold queued pet / news / CIA items; do not fill the hole with a new invented Short.
- At most **3 YouTube Shorts a day**, at least **3 hours apart**. Midweek long-form days use Shorts at 10:00 and 19:00 only.
- New Shorts run **16–18 s**. Every Short's description and Related link points to its matching **live** long-form. Teasers for a long-form that is not live yet use the spoken promise only ("Full … video linked") and do **not** point Related at it until it is up.
- Hook rule: you + home + a number or threat, under 12 words. No new bug fact-pack Shorts. No team logos or betting. Safety lines keep their condition.
- **Leave a slot empty rather than invent content.** A packaging draft or an undated long-form teaser is not a finished fill.
- TikTok cuts, under the dual-cut spec in TASKS.md and PR #1, are **61–75 s** (Creator Rewards). The approved rv2 samples are YouTube-length only (16.35 s and 17.59 s). Do not post those YT files to TikTok unless Moondog88 explicitly okays a short cut.

---

## Best-time data (from the files, not a new study)

- Metricool `getBestTimeToPostByNetwork` for **YouTube**, pulled for the Nov 15 growth plan: **4:00 PM ET is the peak hour every day**; weekends score about half of weekdays. The existing **16:00 ET** weekday slot already covers that peak. Source: `channels/research/growth-plan-longform-shorts-1115.md`.
- The same research, and the Nov 16 Shorts-ceiling note, found **no Shorts-feed effect from hour of day** once topic is controlled. Length (15–20 s) and the first-second hook matter more than clock time.
- Standing clock times taken from `posted.csv` / `open-dates-1121-1204.md` (assumed, not a formal test): weekdays 10:00, 16:00, 19:00; Sunday 14:00; Saturday evening 19:00; midweek long-forms 17:00; Saturday long-forms 08:00.
- Metricool's TikTok best-time tool is **not usable for @meatballmyths** (the connected brand is FurEver Faces). No Meatball TikTok best-hour number is in the files.

---

## The two approved rv2 Shorts (confirmed)

Both are rendered, lint-passed, mastered to about -14.1 LUFS, and **approved to post**. Jarvis did not post them. Post copy: `/workspace/meatball-animation-v2/samples/rv2_post_copy.md` (notebook copy: `channels/packaging/fix-batch-1/rv2_post_copy.md`). Lines: `/workspace/meatball-animation-v2/mb2/episodes/rv2_lines.json`.

| # | File | Duration | Render status | Promote (live long-form) | Planned YT slot |
|---|---|---|---|---|---|
| 1 | `/workspace/meatball-animation-v2/samples/rv2_house-centipede_retention-v2.mp4` | 16.35 s | **Rendered** (C v3 / rv2). No TikTok 61–75 s cut. | *3 Bugs in Your House You Should Never Kill (And 4 You Must)* `cH3HCZ8GlHk` | **Mon 11/16 10:00 ET**, replacing the held pet Short. Fallback: 11/16 **13:00 ET** (3 h before 16:00). If both are missed, Sat 11/21 19:00 and slide the daddy-longlegs slot to Sun 11/22 14:00. |
| 2 | `/workspace/meatball-animation-v2/samples/rv2_daddy-longlegs_retention-v2.mp4` | 17.59 s | **Rendered** (C v3 / rv2). No TikTok 61–75 s cut. | *Don't Kill the Spider in Your Corner. It Eats Bigger Spiders* `KWOM2-mNmww` | **Sat 11/21 19:00 ET** (first clearly open Saturday evening slot once today's 3 YT Shorts are full). |

**Flag before the daddy-longlegs post (needs a title/caption fix, not a new video if you accept the spoken line):** the draft post title is "Daddy Longlegs: The Most Venomous Spider? True or False", and the pinned comment is "Did you believe this one? TRUE or FALSE before you watched." **TRUE, FALSE, and Believe are banned.** Do not invent a verdict. A title that stays inside the sourced lines is: **Daddy Longlegs Aren't the Most Venomous Spiders**. Description in `rv2_post_copy.md` is otherwise sourced (harvestman has no venom; cellar spider has venom but no proof it hurts people; "fangs too short" is a myth). Drop `#spidermyths` (the only allowed "myths" hit is inside `#meatballmyths`). Use `#daddylonglegs #cellarspider #bugsinyourhouse #meatballmyths #shorts` on YouTube. The spoken hook in the render still says "True or false?" Fixing that line needs a Claude re-render; posting with a clean title and a clean pin is the minimum if the slot is kept.

Centipede post copy is clean and can be used as written (title, description, Penn State source, Related to `cH3HCZ8GlHk`, pin "Be honest: squish it or let it live?").

---

## Long-forms in this window (not Shorts)

| When (ET) | Video | Status | Notes |
|---|---|---|---|
| Wed 11/18 17:00 | *Never Bring a Christmas Tree Inside Before You Check for This* (`christmas-tree-check.mp4`) | Already queued in `posted.csv` | **Subscriber notifications off** was asked for 11/18. Confirm the Studio toggle before the slot. |
| Sat 11/21 08:00 | *Don't Squish the 30-Legged Bug in Your Bathroom (Here's Why)* (`longform-house-centipede-v2.mp4`) | Already queued | After it is live, it can become the featured / Related target for centipede Shorts. |
| Wed 11/25 17:00 | *What Crawls Through Your House While You Sleep* (`night-shift-v2.mp4`) | Already queued | **Subscriber notifications off** was asked for 11/25. Confirm the Studio toggle. The 19:00 teaser the same day stays. |
| Wed 12/2 17:00 (assumed midweek hour; confirm) | House-spider ID long-form, *Most House Spiders Can Be Left Alone if You Identify Them* | **Script + fact-check done**; not rendered. Box files: `/workspace/drafts/longform-spider-id.{md,json}`. Voice and animation wait on Claude applying animation-v2 / audio-v2 (PRs #1 and #2 are open). | Midweek: Shorts at 10:00 and 19:00 only, left empty unless a leftover rendered teaser exists. |
| Sat 12/5 08:00 | *Your Life as a Polar Bear: 8 Things You Have to Get Through* (`born-as-polar-bear.mp4`) | Already queued | TASKS.md still asks Claude to apply the pacing rule (promise by 0:05, drop the keep-score intro, etc.) if that is not already in the queued render. |

Upcoming just after this window (do not invent Shorts for them here): cockroach born-as Wed 12/9, dust-mite born-as Wed 12/16, bed bugs Wed 12/23. All four bug long-forms are scripted and fact-checked. Teaser scripts exist; none are rendered. Book the cockroach teasers on 12/6–12/8, after this plan ends.

The lion long-form date is still unset (11/28 vs 12/12). Dog born-as is parked (pets paused). Crocodile born-as is undated. Do not book those teasers until a date is locked.

---

## Day-by-day cadence

Render-status key: **Rendered** = a finished file is named in the queue or on the box. **Needs re-render** = a file exists or is queued but is over 18 s, failed a required fact fix, or is waiting on a new hook. **Script only** = a fact-checked script/teaser exists, no picture file yet. **Length unknown** = queued, but no measured duration is on this box. **Empty** = no on-lane finished item; do not invent one.

Paths for queued YouTube Shorts are the ones in `posted.csv` / `pending-swaps.csv` (Claude skills repo: `episodes/drawn-house/…` or `episodes/hook-test/…` or `episodes/sim3d/…`). Those files are not on this box. Lengths are from `/workspace/research/2026-11-16-queued-shorts-lengths.csv` and the Shorts Editor trim note.

### Mon 11/16

| Slot (ET) | Platform | Fill | Path / file | Status | Promotes |
|---|---|---|---|---|---|
| 10:00 | YouTube | **Hold** queued pet Short *Your Dog's Tail Wag May Lean to Its Right When It Sees You* (`yt-dog-tail-wag-v6.mp4`). **Replace with rv2 house centipede** if the swap can still be made. Fallback 13:00. | `/workspace/meatball-animation-v2/samples/rv2_house-centipede_retention-v2.mp4` | Rendered (16.35 s) | `cH3HCZ8GlHk` |
| 16:00 | YouTube | Keep queued dust-mites Short (house bug). | `yt-dust-mites-v6.mp4` (Metricool id 427124618 in pending-swaps) | **Needs re-render** if possible before ~2:00 PM ET: measured **19.133 s**. Scriptwriter said keep the queued hook unless a fact-checked re-render is comfortable before then. Otherwise ship queued and log it as non-test. | `cH3HCZ8GlHk` until the 12/16 dust-mite long-form is live |
| 19:00 | YouTube | Keep queued stink-bug explainer. | `yt-stinkbug-explainer.mp4` | Rendered, **length unknown** on this box | Existing house-bug long-form (`cH3HCZ8GlHk` or *3 More Bugs* `xeAsg5ECpgw`) |
| 12:00 | TikTok | Queued `tt-naked-mole-rat.mp4` is off-lane. **Hold. Leave empty.** | `tt-naked-mole-rat.mp4` | Rendered (off-lane) | — |
| 20:15 | TikTok | Queued `tt-dog-guilty-look.mp4` is a pet. **Hold. Leave empty.** | `tt-dog-guilty-look.mp4` | Rendered (pets paused) | — |
| 21:30 | TikTok | Queued `tt-electric-eel.mp4` is off-lane. **Hold. Leave empty.** | `tt-electric-eel.mp4` | Rendered (off-lane) | — |
| — | TikTok rv2 | No 61–75 s centipede cut. **Leave empty** unless Moondog88 okays posting the 16.35 s YT file. | — | Needs Claude TikTok cut | `cH3HCZ8GlHk` |

### Tue 11/17

| Slot (ET) | Platform | Fill | Path / file | Status | Promotes |
|---|---|---|---|---|---|
| 10:00 | YouTube | Keep fungus gnats (house). | `yt-fungus-gnats-v6.mp4` | Length unknown here; Shorts Editor math said 19.28 s → 17.28 s if five 0.4 s pads are dropped. **Needs re-render** if the live file is over 18 s. | `cH3HCZ8GlHk` |
| 16:00 | YouTube | Keep carpet-beetle-window. **Use the new 1-second hook** if Claude can fact-check, re-render, and transcript-check in time; otherwise ship the queued cut. | `yt-carpet-beetle-window-v6.mp4` (id 427124763). Hook/EDL: `/workspace/drafts/shorts-hooks-1s-1115.md`, `shorts-edl-carpet-beetle-window.md` | Measured **18.233 s** (slightly over). Needs re-render to land ≤18 s and to pick up the new hook. | `cH3HCZ8GlHk` |
| 19:00 | YouTube | Keep earwig hook (house). | `yt-earwig-hook.mp4` | Rendered, **length unknown**. TASKS.md still asks where the script lives. | `cH3HCZ8GlHk` |
| 12:00 | TikTok | Keep `tt-cassowary.mp4` (WMS, on-lane). | `tt-cassowary.mp4` | Rendered (drawn-tt minute cut; differs from the YT Short). Caption must follow the TikTok template (5 topic hashtags, no `#meatballmyths`; WMS line: "General info, not safety training."). | Newest WMS long-form, or the WMS playlist if no on-topic long-form is live |
| 19:00 | TikTok | Queued `tts-dog-tail-wag.mp4` is a pet. **Hold. Leave empty.** | `tts-dog-tail-wag.mp4` | Rendered (pets paused) | — |
| 21:30 | TikTok | Queued `tt-hummingbird.mp4` is off-lane. **Hold. Leave empty.** | `tt-hummingbird.mp4` | Rendered (off-lane) | — |

### Wed 11/18 (long-form day — Shorts at 10:00 and 19:00 only)

| Slot (ET) | Platform | Fill | Path / file | Status | Promotes |
|---|---|---|---|---|---|
| 10:00 | YouTube | Keep carpenter-ant hook (house). | `yt-carpenter-ant-hook.mp4` | Rendered, **length unknown**. Script location still asked in TASKS.md. | `cH3HCZ8GlHk` |
| 17:00 | YouTube long-form | *Never Bring a Christmas Tree Inside Before You Check for This* | `christmas-tree-check.mp4` | Queued | — |
| 19:00 | YouTube | Keep Christmas-tree bugs Short. **Use the new hook** if the re-render clears in time. | `yt-christmas-tree-bugs-v6.mp4` (id 427124926). Hook/EDL: `shorts-hooks-1s-1115.md`, `shorts-edl-christmas-tree-bugs.md` | **Needs re-render**: measured **19.500 s**. Fact-check also switched the line to "put it in a shrub outside" (Penn State). | The 17:00 Christmas-tree long-form, once it is live |
| 12:00 | TikTok | Queued `tt-sea-otter.mp4` is off-lane. **Hold. Leave empty.** | `tt-sea-otter.mp4` | Rendered (off-lane) | — |
| 19:00 | TikTok | Keep bed-bug explainer (house). | `yt-bedbugs-explainer.mp4` (TikTok slot; YT-named file) | Rendered (minute-style cut, not the 16.35 s bedbug teaser) | `cH3HCZ8GlHk` or the bed-bug chapter in *3 Bugs*; the 12/23 bed-bug long-form is not live yet |
| 20:15 | TikTok | Keep Christmas-tree check cut. | `tt-christmas-tree-check.mp4` | Rendered (TikTok cut of the long-form topic; longer than the YT Short) | The 17:00 long-form |
| 21:30 | TikTok | Keep drain-fly (house). | `tt-drain-fly.mp4` | Rendered | `cH3HCZ8GlHk` |

Note: 20:15 and 21:30 are closer than the YouTube 3-hour rule. That rule is a YouTube cap. If Moondog88 wants the same spacing on TikTok, drop 21:30 and leave it empty.

### Thu 11/19

| Slot (ET) | Platform | Fill | Path / file | Status | Promotes |
|---|---|---|---|---|---|
| 10:00 | YouTube | Keep housefly hook. | `yt-housefly-hook.mp4` | Rendered, **length unknown**. Script location still asked. | `cH3HCZ8GlHk` |
| 16:00 | YouTube | Keep pantry vs clothes moth. Do **not** use the "Only One Eats Your Sweaters" title unless Moondog88 okays it (still an open title check). | `yt-pantry-vs-clothes-moth-v6.mp4` (id 427125342) | Measured **18.233 s**. Re-render only if the file is over 18 s after a pad trim. | `cH3HCZ8GlHk` |
| 19:00 | YouTube | Cluster flies. The queued title and hook still say **"Thousands."** Research's fact-check said cluster flies **must not** say "thousands." | `yt-cluster-flies-v6.mp4` (id 427125458). Replacement title already drafted: *Cluster Flies in Your House Walls Can Wake on Warm Days*. | **Needs re-render** (measured **20.000 s**) **and** the required wording fix. If that file is not ready at least 2 hours before the slot, **leave the slot empty** rather than ship a failed fact. | `cH3HCZ8GlHk` |
| 12:00 | TikTok | Queued `tts-dog-stare.mp4` is a pet. **Hold. Leave empty.** | `tts-dog-stare.mp4` | Rendered (pets paused) | — |
| 19:00 | TikTok | Keep grizzly WMS. | `tts-grizzly-wms.mp4` | Rendered (minute cut; differs from any YT grizzly Short) | WMS playlist / newest WMS long-form. Caption must include "General info, not safety training." |
| 21:30 | TikTok | Keep honey-badger WMS. | `tt-honey-badger.mp4` | Rendered (minute cut) | WMS playlist |

### Fri 11/20

| Slot (ET) | Platform | Fill | Path / file | Status | Promotes |
|---|---|---|---|---|---|
| 10:00 | YouTube | Keep fruit-fly explainer. | `yt-fruitfly-explainer.mp4` | Rendered, **length unknown** | `cH3HCZ8GlHk` |
| 16:00 | YouTube | Booklice (replaces the old humidity-instruction ending). | `yt-booklice-cupboard-v6.mp4` (id 427125573). Script in `shorts-hooks-1s-1115.md` §6. | **Needs re-render**: measured **19.767 s**. | `cH3HCZ8GlHk` |
| 19:00 | YouTube | Keep clothes-moth explainer. | `yt-clothesmoth-explainer.mp4` | Rendered, **length unknown** | `cH3HCZ8GlHk` |
| 19:00 | TikTok | Keep silverfish hook (house). | `yt-silverfish-hook.mp4` | Rendered | `cH3HCZ8GlHk` |
| 21:30 | TikTok | Queued `tt-woodpecker.mp4` is off-lane. **Hold. Leave empty.** | `tt-woodpecker.mp4` | Rendered (off-lane) | — |

### Sat 11/21

| Slot (ET) | Platform | Fill | Path / file | Status | Promotes |
|---|---|---|---|---|---|
| 08:00 | YouTube long-form | *Don't Squish the 30-Legged Bug in Your Bathroom (Here's Why)* | `longform-house-centipede-v2.mp4` | Queued | — |
| 11:00 | YouTube | Keep bison WMS. | `yt-bison-wms-v6.mp4` | Rendered (house-style WMS Short) | WMS playlist / this is on-lane |
| 14:00 | YouTube | Keep silverfish hook. | `yt-silverfish-hook.mp4` | Rendered | `cH3HCZ8GlHk` |
| 19:00 | YouTube | **Open.** The 11/15 open-dates draft filled this with a cat-falls pet Short — **do not use that.** Fill with **rv2 daddy-longlegs**, after the title/pin fix above. | `/workspace/meatball-animation-v2/samples/rv2_daddy-longlegs_retention-v2.mp4` | Rendered (17.59 s). TikTok 61–75 s cut missing. | `KWOM2-mNmww` |
| 12:00 | TikTok | Queued `tts-dog-turkey.mp4` is a pet. **Hold. Leave empty.** | `tts-dog-turkey.mp4` | Rendered (pets paused) | — |
| 19:00 | TikTok | Keep water-bug (house). | `tt-waterbug.mp4` | Rendered (minute cut) | `cH3HCZ8GlHk` |

### Sun 11/22

| Slot (ET) | Platform | Fill | Path / file | Status | Promotes |
|---|---|---|---|---|---|
| 14:00 | YouTube | **Empty.** Open-dates had a dog-head-tilt pet Short — do not use it. Use this only as overflow if an rv2 Short missed 11/16 or 11/21. | — | Empty | — |
| 19:00 | TikTok | Queued `tt-polar-bear.mp4`, title *A Polar Bear's Fur Isn't White; and Its Skin Is Black*. Pack 98 marks "the fur is actually transparent" as unsafe. **Do not invent a rewritten line here.** Hold and leave empty unless Claude confirms the queued wording against pack 98 without using the unsafe claim. | `tt-polar-bear.mp4` | Rendered, **wording check owed** | Polar long-form is not live until 12/5 |

### Mon 11/23 – Fri 11/28 (thin week)

No finished on-lane Short remains after the 11/16–11/21 queue and the two rv2 samples. Lion teasers are script-only and the lion date is unset. Croc teasers are script-only and the croc long-form is undated. Open-dates WMS ideas (mountain lion, black bear, wolf, hippo) are packaging drafts, not rendered files. **Do not invent fills.**

| Date | YT slot (ET) | YT fill | TikTok |
|---|---|---|---|
| Mon 11/23 | 16:00 | **Empty** (was cat-slow-blink, pets) | 19:00 `tt-platypus.mp4` off-lane — **hold, leave empty** |
| Tue 11/24 | 16:00 | **Empty** (was dog-years, pets) | 19:00 `tt-wombat.mp4` off-lane — **hold, leave empty** |
| Wed 11/25 | 10:00 | **Empty** (open-dates had a croc-bite teaser; croc long-form is undated, so it is not booked) | 19:00 `tt-greenland-shark.mp4` off-lane — **hold, leave empty** |
| Wed 11/25 | 17:00 | Long-form *What Crawls Through Your House While You Sleep* (`night-shift-v2.mp4`). Notifications off, if confirmed. | — |
| Wed 11/25 | 19:00 | Keep queued night-shift teaser. File: `yt-teaser-night-shift.mp4`. **Rendered** (length not re-measured here). Promotes the 17:00 long-form. | — |
| Thu 11/26 (Thanksgiving) | 16:00 | **Empty** (was cat-lilies, pets) | No on-lane queued TikTok in `posted.csv` |
| Fri 11/27 | 16:00 | **Empty** (was a mountain-lion packaging draft, not a rendered file) | None on-lane |
| Sat 11/28 | 19:00 | **Empty.** Do not book lion teasers until the lion date is locked. No long-form is queued at 08:00 (the house-cat video was moved to 11/13). | None on-lane |

### Sun 11/29 – Tue 12/1 (spider-ID teasers — script only)

Three fact-checked teasers for the Wed 12/2 long-form, in `/workspace/drafts/spider-id-teasers.md`. Nothing is rendered. Claude must render in C v3 / rv2 with audio-v2, 16–18 s, before these slots. If a teaser is not rendered at least 2 hours before its slot, **leave that slot empty**. Do not point Related at the long-form until 12/2 is live.

| Slot (ET) | Fill | Runtime in script | Status | Promotes |
|---|---|---|---|---|
| Sun 11/29 14:00 YT | `spider-kansas` | 17.28 s | Script only | Spoken promise only until 12/2 |
| Mon 11/30 16:00 YT | `spider-four-inch` | 17.89 s | Script only | Same |
| Tue 12/1 16:00 YT | `spider-jaws` | 17.28 s | Script only | Same |
| Matching TikTok | Same topics, only if a 61–75 s cut is rendered | — | Needs Claude `--cut tiktok` | Same rule on Related |

### Wed 12/2 (spider-ID long-form day)

| Slot (ET) | Fill | Status |
|---|---|---|
| 10:00 YT Short | **Empty** | Do not invent a fourth spider Short |
| 17:00 YT long-form | Spider-ID long-form | Script + fact-check done; **needs Claude render**. Files: `/workspace/drafts/longform-spider-id.{md,json}` |
| 19:00 YT Short | **Empty** | — |
| TikTok | **Empty** unless a 61–75 s teaser or a long-form cut exists | — |

### Thu 12/3 – Fri 12/4

| Date | YT 16:00 | TikTok |
|---|---|---|
| Thu 12/3 | **Empty.** Open-dates had a polar-fast trailer from pack 98. That is a packaging draft, not a finished teaser script in the bug-teaser style, and it has not been rendered. Do not invent it. | Empty |
| Fri 12/4 | **Empty** (same for polar-cubs / polar-swim drafts). | Empty |

Cockroach teasers (`/workspace/drafts/cockroach-teasers.md`: `roach-30000` 16.66 s, `roach-crack` 17.28 s, `roach-eggcase` 17.28 s) are script-only and belong on 12/6–12/8 for the Wed 12/9 long-form, just after this plan.

### Sat 12/5

| Slot (ET) | Fill | Status |
|---|---|---|
| 08:00 YT long-form | Polar bear born-as, already queued (`born-as-polar-bear.mp4`) | Confirm the pacing-rule edit is in the queued render. |
| Later YT Short | **Empty** unless a rendered polar teaser exists (none found in the teaser style of the bug episodes). | — |
| TikTok | **Empty** unless a 61–75 s polar cut exists. | — |

---

## Slot counts (YouTube Shorts only, 11/16–12/5)

Long-forms are not counted as Shorts.

| | Count | Notes |
|---:|---:|---|
| Standing YouTube Short slots listed in the day-by-day tables | **33** | 11/16–17 and 11/19–20: 3 each; 11/18 and 11/25 and 12/2: 2 Short slots (midweek long-form days); 11/21: 3 (bison, silverfish, rv2); 11/22–24, 11/26–12/1, 12/3–5: 1 assumed Short slot each |
| Filled with a **rendered** on-lane Short or the approved rv2 samples (assuming the 11/16 10:00 swap and the 11/19 cluster-flies re-render both land) | **18** | 11/16 (3), 11/17 (3), 11/18 (2), 11/19 (3), 11/20 (3), 11/21 (3), 11/25 19:00 (1) |
| Filled **script only** (spider teasers, need Claude) | **3** | 11/29, 11/30, 12/1 |
| **Empty** on-lane Short slots | **12** | 11/22 14:00; 11/23–24 16:00; 11/25 10:00; 11/26–28; 12/2 10:00 and 19:00; 12/3–4 16:00; 12/5 later Short. If the cluster-flies fix misses the window, 11/19 19:00 becomes a 13th empty slot. If the 11/16 10:00 rv2 swap misses and no fallback is used, that slot is empty too. |
| Held (pets / off-lane) and not replaced with invented content | see day-by-day | Replacements were not invented |

TikTok in the same window: **8 on-lane keeps** if Wed 11/18 keeps all three queued house/WMS cuts (cassowary 11/17 12:00; bed bugs 11/18 19:00, Christmas-tree 11/18 20:15, drain-fly 11/18 21:30; grizzly 11/19 19:00, honey-badger 11/19 21:30; silverfish 11/20 19:00; water-bug 11/21 19:00). That becomes 6 if the two 11/18 late-evening TikToks are dropped to mirror the YouTube 3-hour spacing. **Held / empty:** every pet and off-lane queued TikTok listed above, plus every rv2/teaser day until a 61–75 s cut exists.

---

## Where Claude must render

See `tasks-for-claude.md` for the paste-ready TASKS block. In this plan, Claude is on the hook for:

1. Audio-v2 + animation-v2 / rv2 pipeline (PRs #1 and #2 are open, not merged).
2. TikTok **61–75 s** cuts of the two rv2 Shorts, then of later teasers (`--cut tiktok`).
3. Re-renders of queued YouTube Shorts that are over 18 s or that failed a required wording fix: dust mites, fungus gnats (if over), carpet beetle (hook + trim), Christmas-tree bugs (hook + trim + Penn State line), cluster flies (**required** "thousands" fix + trim), booklice.
4. Spider-ID long-form render for 12/2, and the three spider teasers for 11/29–12/1.
5. Optional, only after a date is locked: polar pacing-rule edit (12/5 is already queued), cockroach teasers for 12/6–8, lion or croc teasers.
6. Do **not** render new pet, news, or CIA Shorts. Do **not** build new bug fact-pack Shorts.

---

## Where TikTok versions differ

- Spec: YouTube 15–20 s (rv2 lint, loop ending, -14 LUFS). TikTok 61–75 s, same hook, a retention beat every 5–8 s, loop ending. This is new as of the Nov 15 dual-cut order. **None of the rv2 or bug-teaser TikTok cuts exist yet.**
- Existing queued TikToks in `posted.csv` are older **minute cuts** (`tt-` / `tts-` / some `yt-` files reused). They are not the new dual-cut format. On-lane ones can still ship as already queued, with a TikTok caption (5 topic hashtags, no brand tag; WMS safety line where it applies) and Moondog88 posting them.
- Captions are not interchangeable with YouTube descriptions. Template: `/workspace/packaging/tiktok-caption-template.md` (and the notebook copy). The rv2 post copy is YouTube-shaped and must be rewritten for TikTok before any TikTok post.
- Metricool cannot schedule `@meatballmyths` (see `tiktok-blockers.md`).

---

## Needs Moondog88's okay

- Posting either rv2 Short (already approved to post, but each go-live still needs his okay, and the daddy-longlegs title/pin fix should be accepted first).
- Holding today's 10:00 pet Short and swapping in the centipede, if that slot has not already fired.
- Holding the other pet and off-lane TikTok / YouTube items listed above.
- Subscriber notifications off on the 11/18 and 11/25 long-forms.
- The "Only One Eats Your Sweaters" moth title, if anyone wants to use it.
- Any TikTok post, including posting a YT-length rv2 file instead of waiting for a 61–75 s cut.
- Booking a lion or crocodile date (teasers stay unscheduled until then).
