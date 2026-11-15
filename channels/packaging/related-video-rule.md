# Related-video rule (draft)

Status: draft only. No Studio changes, repo edits, or posts from this file. Do not set custom Shorts cover frames.

Sources: Social Studio brief (each Short's Related video points at that week's long-form; polar bear Sat 12/5, lion Sat 12/12; include other scheduled Saturdays from the orders; no custom Shorts cover frames); MASTER_ORDERS "The bridge" and "Watch hours" / "Do all three"; `skills/oh-meatball/data/posted.csv` as of this pass (skills branch `claude/youtube-monetization-strategy-m9vz6i`); `TASKS.md` in `mooneyn60-art/Side-hustles` (Social Studio log: no Shorts logged for 11/22–11/24 or 11/26–12/4).

All times are America/New_York, matching the `posted.csv` slots.

## The rule, locked for this draft

1. **No custom Shorts cover frames.** Leave the Shorts cover on auto / unset. This is already in MASTER_ORDERS (research 93) and in the audit. Related video is a Studio field on the Short, not a custom frame.
2. **On-topic Shorts** (same creature or the same subject as the long-form, including a same-week trailer) set Related video to **that week's long-form**. MASTER_ORDERS also wants two or three 16–20 s same-creature Shorts in that long-form's week, at least a day apart, each pointing at it. The pinned question on those Shorts ends with "Full list in the Related video 👆".
3. **Off-topic Shorts** (a different show or a different creature) do **not** silently inherit the week's long-form under MASTER_ORDERS. They point at that show's playlist. The Studio brief said "each Short" points at the week's long-form. That is broader than "The bridge." **Conflict: flag for Studio.** The table below gives both targets where they differ. Recommendation: keep MASTER_ORDERS (on-topic → week's / newest long-form; other Shorts → show playlist) so a bison Short does not send viewers to a Christmas-tree long-form.
4. **Re-point every Saturday** when a Saturday long-form goes up (MASTER_ORDERS). Midweek long-forms (Wednesday 17:00) become the newest long-form from their post time until the next Saturday long-form, and they get the same-creature trailer in that midweek window (Christmas tree bugs on 11/18 19:00; Night Shift teaser on 11/25 19:00).
5. Same-creature trailers may be scheduled in the days just before a Saturday long-form and can already point at that scheduled long-form. Otherwise re-point on Saturday.

## Saturday / midweek long-form calendar

From `posted.csv` (scheduled) and MASTER_ORDERS (ordered). "Scheduled" means a row exists in `posted.csv`. "Ordered only" means the orders name a date, but there is no file in the queue yet.

| When (ET) | Long-form | Status | Notes |
|---|---|---|---|
| Fri 11/13 17:00 | Your Life as a House Cat: 8 Ways It Goes Wrong | Scheduled (already posted) | First born-as. Older than the 11/14 spider. |
| Sat 11/14 08:00 | Don't Kill the Spider in Your Corner. It Eats Bigger Spiders | Scheduled (already posted) | Newest long-form until Wed 11/18 17:00. |
| Wed 11/18 17:00 | Never Bring a Christmas Tree Inside Before You Check for This | Scheduled | Midweek. Newest from 11/18 17:00 until Sat 11/21 08:00. |
| Sat 11/21 08:00 | Don't Squish the 30-Legged Bug in Your Bathroom (Here's Why) | Scheduled | House centipede v2. Newest until Wed 11/25 17:00. |
| Wed 11/25 17:00 | What Crawls Through Your House While You Sleep | Scheduled | Night Shift v2. Newest until the next Saturday long-form that actually exists. |
| Sat 11/28 08:00 | The lion, "if ready by Thu 11/26" | Ordered only (Watch hours queue). **Not in `posted.csv`.** | Conflicts with lion on 12/12. Do not build a Related-video target for 11/28 unless Nolan confirms this date and a file is scheduled. |
| Sat 12/5 08:00 | Your Life as a Polar Bear: 8 Things You Have to Get Through | Scheduled | Studio's first named Saturday. Newest from 12/5 08:00 until 12/12. |
| Sat 12/12 08:00 | Born-as lion (title not in `posted.csv`) | Ordered only ("Do all three," 11/13; Studio brief agrees) | **Conflict:** the Watch hours list still says dog on 12/12 and lion on 11/28 if ready. This draft follows the later "Do all three" line and the Studio brief: lion on 12/12. Confirm before pointing Shorts at it. |
| Sat 12/19 08:00 | Born-as dog (title not in `posted.csv`) | Ordered only | "Do all three": dog and wolf by the data's rank on 12/19 and 12/26. Watch hours had wolf on 12/19. Confirm the animal before pointing Shorts. |
| Sat 12/26 08:00 | Born-as wolf (title not in `posted.csv`) | Ordered only | Same conflict as 12/19 if the rank or the Watch hours list is used instead. |

Working assumption for the coming weeks, pending Nolan: **no 11/28 long-form in the queue, so Night Shift stays newest from Wed 11/25 17:00 until Sat 12/5 08:00; then polar bear 12/5, lion 12/12, dog 12/19, wolf 12/26.**

## Dated table: queued YouTube Shorts → Related video

"Studio target" = that week's long-form, as the brief asked. "Orders target" = MASTER_ORDERS on-topic bridge vs show playlist. "Week's long-form" is the newest long-form at that slot's time, except a same-creature trailer, which always points at its long-form.

### Still queued on Sun 11/15

| Slot (ET) | File | On-topic to week's LF? | Studio target | Orders target |
|---|---|---|---|---|
| Sun 11/15 19:00 | yt-cellar-102-v6.mp4 | Yes — cellar spider leftovers | Don't Kill the Spider in Your Corner (Sat 11/14 08:00) | Same |

### Mon 11/16–Wed 11/18 morning (week's LF: cellar spider, until 11/18 17:00)

| Slot (ET) | File | On-topic to week's LF? | Studio target | Orders target |
|---|---|---|---|---|
| Mon 11/16 10:00 | yt-dog-tail-wag-v6.mp4 | No (pet house) | Cellar spider long-form | Things Living In Your House playlist |
| Mon 11/16 16:00 | yt-dust-mites-v6.mp4 | No | Cellar spider long-form | House playlist |
| Mon 11/16 19:00 | yt-stinkbug-explainer.mp4 | No | Cellar spider long-form | House playlist |
| Tue 11/17 10:00 | yt-fungus-gnats-v6.mp4 | No | Cellar spider long-form | House playlist |
| Tue 11/17 16:00 | yt-carpet-beetle-window-v6.mp4 | No | Cellar spider long-form | House playlist |
| Tue 11/17 19:00 | yt-earwig-hook.mp4 | No | Cellar spider long-form | House playlist |
| Wed 11/18 10:00 | yt-carpenter-ant-hook.mp4 | No | Cellar spider long-form | House playlist |

### Wed 11/18 17:00–Sat 11/21 08:00 (week's LF: Christmas tree)

| Slot (ET) | File | On-topic to week's LF? | Studio target | Orders target |
|---|---|---|---|---|
| Wed 11/18 19:00 | yt-christmas-tree-bugs-v6.mp4 | Yes — Christmas tree bugs | Christmas tree long-form | Same |
| Thu 11/19 10:00 | yt-housefly-hook.mp4 | No | Christmas tree long-form | House playlist |
| Thu 11/19 16:00 | yt-pantry-vs-clothes-moth-v6.mp4 | No | Christmas tree long-form | House playlist |
| Thu 11/19 19:00 | yt-cluster-flies-v6.mp4 | No | Christmas tree long-form | House playlist |
| Fri 11/20 10:00 | yt-fruitfly-explainer.mp4 | No | Christmas tree long-form | House playlist |
| Fri 11/20 16:00 | yt-booklice-cupboard-v6.mp4 | No | Christmas tree long-form | House playlist |
| Fri 11/20 19:00 | yt-clothesmoth-explainer.mp4 | No | Christmas tree long-form | House playlist |

### Sat 11/21 08:00–Wed 11/25 17:00 (week's LF: house centipede v2)

| Slot (ET) | File | On-topic to week's LF? | Studio target | Orders target |
|---|---|---|---|---|
| Sat 11/21 11:00 | yt-bison-wms-v6.mp4 | No (Would Meatball Survive? #5) | House centipede v2 | Would Meatball Survive? playlist |
| Sat 11/21 14:00 | yt-silverfish-hook.mp4 | No | House centipede v2 | House playlist |
| Sun 11/22–Tue 11/24 | *(no YouTube rows in `posted.csv`)* | — | House centipede v2, if a house or centipede Short is added | Same-creature trailers → centipede v2; other house Shorts → house playlist; WMS or pet Shorts → their show playlist. TASKS.md and the audit flag this hole. A cats/turkey Short in this window is a pet video, not a centipede trailer. |

There is no house-centipede Short in this window in the queue. MASTER_ORDERS asked for two or three 16–20 s same-creature trailers. That is a gap, not a reason to retarget unrelated Shorts.

### Wed 11/25 17:00–Sat 12/5 08:00 (week's LF: Night Shift v2, unless a 11/28 lion long-form is later scheduled)

| Slot (ET) | File | On-topic to week's LF? | Studio target | Orders target |
|---|---|---|---|---|
| Wed 11/25 19:00 | yt-teaser-night-shift.mp4 | Yes — Night Shift teaser | Night Shift v2 | Same |
| Thu 11/26 | Bears vs Lions Short, if Nolan picks option B and it is built | No (WMS; animals, not house bugs) | Night Shift v2, under a literal "each Short" reading | Would Meatball Survive? playlist, until a WMS long-form (lion, 11/28 or 12/12) exists to point at |
| Thu 11/26–Fri 12/4 | *(no YouTube rows in `posted.csv`)* | — | Night Shift v2 for any Short in this hole, under the Studio reading; polar-bear trailers may already point at the Sat 12/5 polar bear | Night Shift teaser already covers the on-topic slot. Add 1–2 more Night Shift fact Shorts if they are made before the week turns. Polar-bear trailers (2–3, at least a day apart) should point at the 12/5 polar bear, even if they go up a few days early. Pet or chocolate Shorts → house playlist, not Night Shift. |

### Week of Sat 12/5 (polar bear) — no Shorts in `posted.csv` after 11/25 except this long-form

| Slot (ET) | File | On-topic to week's LF? | Studio target | Orders target |
|---|---|---|---|---|
| Sat 12/5 08:00 | born-as-polar-bear.mp4 | (this is the long-form) | — | — |
| Sat 12/5–Fri 12/11 | *(no Shorts queued)* | — | Polar bear long-form | 2–3 polar-bear Shorts, different facts, at least a day apart, Related video = polar bear long-form. Other Shorts → show playlist. Re-point existing on-topic links on Saturday 12/5. |

### Week of Sat 12/12 (lion, ordered only)

No Shorts and no long-form file in `posted.csv`. If the lion long-form is scheduled at 12/12 08:00, that week's on-topic Shorts (lion facts, or a Bears vs Lions recut only if the script is the same animals) point at it. Confirm 12/12 vs 11/28 before any links are set. Re-point on Saturday 12/12.

### Week of Sat 12/19 (dog, ordered only) and Sat 12/26 (wolf, ordered only)

Same pattern, once the animal and the file are confirmed: 2–3 same-creature Shorts that week, Related video on the Saturday long-form, re-point that Saturday. Nothing in `posted.csv` yet.

## Cover frames

Do not upload or set a custom Shorts cover / frame for any row in this table. Related video is the only Studio link this rule changes.

## Gaps

- Empty YouTube dates: 11/22, 11/23, 11/24, then 11/26 through 12/4, and every date after 12/5 in 2026 except the 12/5 polar bear long-form itself (no 12/12, 12/19, or 12/26 file yet).
- No same-creature Shorts queued for house centipede v2, polar bear, lion, dog, or wolf.
- Sat 11/28 lion vs Sat 12/12 lion, and dog/wolf date swap, are unresolved in MASTER_ORDERS itself.
- Studio "every Short → week's long-form" vs MASTER_ORDERS "on-topic Shorts → long-form; others → playlist" is unresolved.
- This file cannot see whether Related video is already set in YouTube Studio for the queued Shorts. The table is the intended mapping, not a live read-back.
