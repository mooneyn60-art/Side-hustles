# YouTube Shorts gap check: 11/22–11/24 and 11/26–12/04

Checked Sun 2026-11-15, about 14:20 ET. Sources are in `mooneyn60-art/skills`, branch `claude/youtube-monetization-strategy-m9vz6i`. "OM" means `skills/oh-meatball/`. I did not open Metricool itself; there is no connector here. Every scheduler source in the repo was checked.

## Verdict
**The gaps are real, and they look like the planned 7-day queue rather than a lagging log.**
- Every repo source agrees that no YouTube Short is scheduled 11/22–11/24 or 11/26–12/04.
- A third gap was found: **Sat 11/21 19:00**.
- Metricool itself was not read, so the last step is a 2-minute look in Metricool's planner.

## Evidence
1. **`OM/data/posted.csv`, the scheduling log.** YouTube rows by date:
   - 11/16–11/20: 3 a day
   - 11/21: 3, which includes the 08:00 long-form, so only 2 Shorts (11:00 bison WMS, 14:00 silverfish)
   - 11/22, 11/23, 11/24: **none**
   - 11/25: 2 (17:00 Night Shift v2 long-form, 19:00 Night Shift teaser Short)
   - 11/26–12/04: **none**
   - 12/05: 1 (08:00 polar bear long-form)
   - I counted these from the file.
2. **`OM/data/post-ids.csv`, Metricool post ids written back from Metricool's API responses (43 rows).**
   - The latest YouTube entries before December are 11/21 11:00 (bison) and 11/21 14:00 (silverfish). The next is 12/05 08:00 (polar bear).
   - There is no YouTube id for 11/22–12/04.
   - This file is not a complete list: the 11/25 Night Shift posts are in posted.csv but not here. So it supports the gap but can't prove it alone.
3. **`OM/data/board/board.json`, the "queue" list (generated 11/14 07:40).** It ends Sat 11/21, with nothing on 11/21 at 19:00.
   - It is built from posted.csv for the next 7 days (`OM/tools/board.py`, "the next 7 days from the log"), so it is not independent of item 1.
4. **`OM/data/pending-swaps.csv` (20 rows):** no slot after 11/20.
   - **`OM/data/held.csv`:** the only YouTube rows for 11/21–11/23 are old photo-style WMS Shorts held on 10/27 under "drawn only". Those were deliberately pulled, so they are not lag.
5. **Notes that say the gap is known:**
   - `OM/research/95-next-topics.md`: "The YouTube Shorts queue is empty from Sat 11/21."
   - `OM/research/102-scoreboard-1113.md`: "Days 11/14 to 11/20 have their Shorts… Sat 11/21 has two Shorts beside the long video: it needs one at 19:00 from the next batch."
   - `skills/channel-brain/SKILL.md` (v3): "Nothing is queued past 7 days unless MASTER_ORDERS says so". The daily two-topic batch fills the queue about a week ahead (`skills/channel-brain/MASTER_ORDERS.md`, "Do all three").

## Open slots this leaves (MASTER_ORDERS "Posting" slot list)
- Sat 11/21 19:00
- Sun 11/22: 3 slots (08:00 or 11:00, 14:00 or 15:00, 19:00)
- Mon 11/23 and Tue 11/24: 3 each (10:00, 16:00, 19:00)
- Wed 11/25: none needed. It is a long-form day, and the rule is 2 Shorts (10:00 and 19:00) with only 19:00 filled, so 10:00 is open.
- Thu 11/26 to Fri 12/04: 3 a day on weekdays, 3 on Sat 11/28 (a long-form day if the lion is ready; the queue in MASTER_ORDERS lists "Sat 11/28 08:00 the lion if ready by Thu 11/26") and Sun 11/29. A midweek long-form (Wed or Thu 17:00) cuts that day to 2.
- Sat 12/05: 2 Shorts beside the polar bear long-form.

## To close it out
- **In Metricool:** open the planner, filter to YouTube, and look at 11/21–12/05. If any post shows there that isn't in posted.csv, the log is lagging; add those rows to posted.csv the same day (rule in MASTER_ORDERS "Posting").
