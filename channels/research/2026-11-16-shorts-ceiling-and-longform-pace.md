# Shorts ceiling and long-form pace: Meatball Myths YouTube

Prepared Sun 11/15/2026, about 19:30 ET, for Mon 11/16 4 PM ET. Everything was read only:
- Metricool: only getBrandSettings, getAnalyticsAvailableMetrics, getAnalyticsDataByMetrics and getScheduledPosts.
- Repo: read only, no writes.
- Nothing was created, updated or scheduled.

Blanks mean no data; nothing is estimated. Every figure has a source and an n.
Per-Short table: `/workspace/research/2026-11-16-shorts-90d.csv`, 119 rows.

**Sources**
- **MC**: Metricool brand 8135499, YouTube channel UCw98RQD81t_339LX5EJqcrg, "videos published in range" metrics, 8/17–11/15.
  - Pulled 11/15 about 18:55 ET.
  - Newest video it has was published 11/11 19:02 ET.
  - Its view counts match the Windsor 11/14 reads in research/115 for 8 of 8 Shorts, so treat them as roughly 11/14 values.
- **Repo**: `mooneyn60-art/skills`, branch `claude/youtube-monetization-strategy-m9vz6i`.
  - Paths start at `skills/oh-meatball/` unless they start with `skills/`.
  - Newest commit read: 0d6db9c, 11/15 13:36 ET.
- **YouTube Help**: "YPP overview & eligibility" (support.google.com/youtube/answer/72851) and "Changes to YPP" (answer/12843009), read via web search 11/15.

## Top line
1. **The ceiling is real, and it sits around 1,000–1,200 views.**
   - Of 76 Meatball Shorts in MC, 39 reached 1,007 and only 8 reached 1,500. The highest is 2,390.
   - House-bug and spider Shorts have a median of 1,115 (n=44), but only 8 of 44 passed 1,500.
   - Research 68 calls this pattern "tested on ~1K viewers and stop there".
2. **Length is the only bucket with a clear edge.** 15–20 s Shorts have a median of 1,159 (n=23) and account for 6 of the 8 Shorts over 1,500. 30 s and longer: median 397 (n=9, small). Hour of day shows no pattern; research 100 also found nothing in about 166 comparisons.
3. **Newer Shorts are doing worse, but the drop is confounded.**
   - House-bug and spider Shorts in the week of 11/9 have a median of 412.5 (n=10), against 1,155 (n=18) the week before.
   - 5 of those 10 were posted on 11/11, a 5-Short day. Four of them got 30–305 views at an engaged share of 0.30–0.39, which Windsor reads as swiped away, not held back (research/115).
   - New pet and WMS Shorts read 873–1,100 at 17–51 h (n=6, excluding one stalled Short).
   - Verdict: a topic or format problem, not a clear audience mismatch. It still needs Studio's "viewed vs. swiped away" to confirm.
4. **The earlier Bartolozzi audience is a separate world.**
   - The 24 deleted Certified Bart clips had a median of 3,717.5 (MC).
   - Deleted videos don't count toward YPP (YouTube Help).
   - 709 of the 883 subscribers gained 6/17–10/12 came from India against only 436 Indian views (`skills/bart-clips/research/03_own_channel.md`), so part of the 1,010 subscriber base isn't a Meatball audience.
5. **Long-form pace:**
   - Current pace is 10.4 long-form hours in 28 days, about 2.6 h a week (Windsor, research/115, n=8 long videos).
   - At that pace a rolling 12 months holds at most about 135 hours, so 3,000, 4,000 or 8,000 hours are never reached.
   - Holding 4,000 in a rolling year needs about 76.9 h a week (29.6× current).
   - Reaching 4,000 by 1/31/2027 (before the 8,000-hour rule starts for new applicants) needs about 362.6 h a week.
   - This is arithmetic from the cited figures, not a forecast.
6. **CTR:** only the channel-wide long-form figure exists: 2.50% over 28 days to 11/11 (Studio paste in `skills/channel-brain/KNOWLEDGE.md`). The test target is 4%+. Per-video CTR is Studio only.
7. **The 1,007 median isn't in the repo or in Metricool.** I searched the repo branch and the Metricool pull. My own medians:
   - 1,018.5 for n=76 (MC).
   - 940.5 for n=88 (MC plus newer repo reads).
   - 1,000 for n=76 (public counts 11/12, `research/data/100-shorts-table.csv`).
   - 932 for the newest 12 (`data/board/board.json`).

## 1. Every Short, last 90 days (8/17–11/15)
The full table is in the CSV, 119 rows. Columns: era, post date/time ET, title, video ID, length (s) and source, views with as-of time and source, viewed-vs-swiped proxy and its label, average % viewed, likes, comments, shares, subscribers gained, topic, style, first-second hook type, first sentence, words in the first 3 s.

| Era | n | Views data | Median views | Notes |
|---|---|---|---|---|
| Meatball, in MC | 76 | MC, roughly 11/14 | 1,018.5 | Published 10/15–11/11 |
| Meatball, after 11/11 | 18 (12 with a count) | Repo scoreboards (research/102, /117, data/board/board.json), reads at 17–51 h | 893.5 | 6 posted 11/14–11/15 have no read; views are blank |
| Bartolozzi (Certified Bart clips, `skills/bart-clips`) | 24 | MC (deleted videos, title shows as "Deleted video") | 3,717.5 | 8/17–9/15. Titles, lengths and engaged share only where `bart-clips/research/03_own_channel.md` names the ID or the views match its top-10 table. The 5:23 long video HNHO_0wmbJg is left out |
| Meatball, deleted 10/15 upload | 1 | MC | 1 | No title |

**Column coverage, Meatball Shorts (n=94).**
- Length: 79.
- Views: 88.
- Engaged share (proxy): 71.
- Average % viewed: 71.
- Likes, comments and shares: 76.
- Subscribers gained: 66.
- Hook type: 89.
- First sentence: 50.

Field notes:
- **Viewed vs. swiped away is blank for every Short.** It's only in YouTube Studio > Analytics > Content > Shorts. The nearest field, used here and labeled in the CSV, is Windsor engaged share (engaged views ÷ views).
  - Sources: `research/data/100-shorts-table.csv` (Windsor to about 11/10) and research/115 (8 Shorts, 11/10–11/11).
  - For Bart clips: engaged/views from vidIQ in `bart-clips/research/03`.
- **Average % viewed** is Windsor (100-shorts-table, research/115). For Bart clips it's vidIQ (03 §2a).
- **Subscribers gained** is Windsor via 100-shorts-table. MC has no per-video subscriber metric.
- **Likes, comments and shares** are MC.
- **Hook type** comes from the opening styles described in `research/68-hook-ab-test.md`, mapped from the style column of 100-shorts-table and the episode column of `data/posted.csv`:
  - NEW punch-in plus 2-line hook text.
  - v6 close-up plus title stamp.
  - 3D explainer.
  - Older formats.
  - The first sentence is from `research/data/96-openings-our-shorts.csv` (n=50, whisper transcripts).

## 2. Patterns against the 1,007 median
Analysis set: the 76 Meatball Shorts in MC. All have the same as-of time (roughly 11/14) and were at least 3 days old, past the day-0 window (a Short earns 85% of its views on day 0, research 100 in `skills/channel-brain/KNOWLEDGE.md`). Newer Shorts are added only in the week cohorts. Columns "≥1,007" and "≥1,500" are counts.

**Which median:**
- 1,007 is from the brief. I couldn't find it in the repo or MC.
- Computed: 1,018.5 (n=76, MC); 940.5 (n=88, with newer repo reads); 1,000 (n=76, public 11/12, 100-shorts-table); 1,039 (n=66, Windsor views, 100-shorts-table); 932 (newest 12, board.json).

**Posting hour (ET)**

| Bucket | n | Median views | ≥1,007 | ≥1,500 | n with engaged share | Median engaged share | n with avg % viewed | Median avg % viewed | Flag |
|---|---|---|---|---|---|---|---|---|---|
| 06–11 | 18 | 731 | 8 | 1 | 17 | 0.427 | 17 | 75.2 |  |
| 12–15 | 24 | 1,031.5 | 14 | 2 | 22 | 0.406 | 22 | 70.7 |  |
| 16–18 | 18 | 1,038 | 10 | 3 | 18 | 0.412 | 18 | 64.0 |  |
| 19–23 | 16 | 817.5 | 7 | 2 | 14 | 0.459 | 14 | 65.3 |  |

**Length** (lengths from 100-shorts-table; "no length data" is mostly the soap-opera parts)

| Bucket | n | Median views | ≥1,007 | ≥1,500 | n with engaged share | Median engaged share | n with avg % viewed | Median avg % viewed | Flag |
|---|---|---|---|---|---|---|---|---|---|
| under 15 s | 3 | 1,129 | 2 | 0 | 3 | 0.500 | 3 | 121.6 | small n (<10) |
| 15–20 s | 23 | 1,159 | 16 | 6 | 23 | 0.453 | 23 | 81.9 |  |
| 20–30 s | 32 | 1,022.5 | 18 | 1 | 32 | 0.408 | 32 | 59.0 |  |
| 30–45 s | 7 | 397 | 2 | 0 | 7 | 0.376 | 7 | 61 | small n (<10) |
| 45 s+ | 2 | 430.5 | 0 | 0 | 2 | 0.408 | 2 | 38.2 | small n (<10) |
| no length data | 9 | 35 | 1 | 1 | 4 | 0.385 | 4 | 109.8 | small n (<10) |

**Topic**

| Bucket | n | Median views | ≥1,007 | ≥1,500 | n with engaged share | Median engaged share | n with avg % viewed | Median avg % viewed | Flag |
|---|---|---|---|---|---|---|---|---|---|
| WMS | 4 | 1,126.5 | 3 | 0 | 4 | 0.377 | 4 | 58.6 | small n (<10) |
| case files / mysteries | 6 | 57.5 | 0 | 0 | 6 | 0.385 | 6 | 46.3 | small n (<10) |
| house bug | 32 | 1,124.5 | 23 | 6 | 32 | 0.456 | 32 | 79.3 |  |
| old soap-opera format | 5 | 18 | 0 | 0 | 0 |  | 0 |  | small n (<10) |
| other animals | 17 | 667 | 5 | 0 | 17 | 0.328 | 17 | 62.7 |  |
| spider | 12 | 1,094.5 | 8 | 2 | 12 | 0.447 | 12 | 70.8 |  |

**First-second hook type (research 68 styles)**

| Bucket | n | Median views | ≥1,007 | ≥1,500 | n with engaged share | Median engaged share | n with avg % viewed | Median avg % viewed | Flag |
|---|---|---|---|---|---|---|---|---|---|
| 3D explainer open | 6 | 820 | 3 | 1 | 6 | 0.468 | 6 | 75.1 | small n (<10) |
| NEW punch-in + 2-line hook text (research 68) | 4 | 551 | 2 | 0 | 4 | 0.395 | 4 | 54 | small n (<10) |
| blank (soap-opera parts) | 5 | 18 | 0 | 0 | 0 |  | 0 |  | small n (<10) |
| older format (real photo / quiz / case / soap) | 33 | 866 | 12 | 1 | 33 | 0.370 | 33 | 61 |  |
| teaser | 1 | 1,664 | 1 | 1 | 1 | 0.529 | 1 | 118.5 | small n (<10) |
| v6 close-up + title stamp (research 68) | 27 | 1,159 | 21 | 5 | 27 | 0.459 | 27 | 83 |  |

The hook types overlap with era and topic, so this isn't a clean test. The NEW punch-in group (n=4) includes the two 11/11 flops at 47 and 30 views; research 68 says to read that test in Studio. Research 96 part 2 (n=50, Windsor): the opening mechanics explain little once length is held fixed. Words in the first 3 s show a weak link with engaged share (rho +0.28, p 0.049, across 28 tests run).

**House-bug and spider only, by length** (controls for topic):

****

| Bucket | n | Median views | ≥1,007 | ≥1,500 | n with engaged share | Median engaged share | n with avg % viewed | Median avg % viewed | Flag |
|---|---|---|---|---|---|---|---|---|---|
| under 15 s | 3 | 1,129 | 2 | 0 | 3 | 0.500 | 3 | 121.6 | small n (<10) |
| 15–20 s | 20 | 1,159.5 | 15 | 6 | 20 | 0.456 | 20 | 86.0 |  |
| 20–30 s | 14 | 1,088 | 12 | 1 | 14 | 0.477 | 14 | 60.4 |  |
| 30–45 s | 3 | 395 | 1 | 0 | 3 | 0.430 | 3 | 56 | small n (<10) |
| no length data | 4 | 285.5 | 1 | 1 | 4 | 0.385 | 4 | 109.8 | small n (<10) |

### Do newer Shorts do worse? (week cohorts, Monday start)
**All Meatball Shorts with a count (MC plus repo reads; the week of 11/9 includes 12 Shorts read at 17–51 h)**

| Bucket | n | Median views | ≥1,007 | ≥1,500 | n with engaged share | Median engaged share | n with avg % viewed | Median avg % viewed | Flag |
|---|---|---|---|---|---|---|---|---|---|
| 2026-10-12 | 5 | 18 | 0 | 0 | 0 |  | 0 |  | small n (<10) |
| 2026-10-19 | 16 | 961 | 8 | 1 | 16 | 0.322 | 16 | 62.2 |  |
| 2026-10-26 | 24 | 992.5 | 12 | 1 | 24 | 0.439 | 24 | 60.4 |  |
| 2026-11-02 | 20 | 1,140.5 | 14 | 4 | 20 | 0.456 | 20 | 86.0 |  |
| 2026-11-09 | 23 | 873 | 6 | 2 | 11 | 0.390 | 11 | 75.2 |  |

**House-bug and spider only, MC**

| Bucket | n | Median views | ≥1,007 | ≥1,500 | n with engaged share | Median engaged share | n with avg % viewed | Median avg % viewed | Flag |
|---|---|---|---|---|---|---|---|---|---|
| 2026-10-19 | 2 | 1,830 | 2 | 1 | 2 | 0.396 | 2 | 92.8 | small n (<10) |
| 2026-10-26 | 14 | 1,088 | 11 | 1 | 14 | 0.496 | 14 | 63.5 |  |
| 2026-11-02 | 18 | 1,155 | 14 | 4 | 18 | 0.470 | 18 | 89.2 |  |
| 2026-11-09 | 10 | 412.5 | 4 | 2 | 10 | 0.385 | 10 | 86.7 |  |

Reading:
- House-bug and spider Shorts climbed from 1,088 (week of 10/26, n=14) to 1,155 (week of 11/2, n=18), then fell to 412.5 (week of 11/9, n=10).
- In the 11/9 week, 5 of the 10 were the 11/11 five-Short day: 1,055, 305, 197, 47, 30. Two more 11/10 Shorts were low: 520 and 266.
- Engaged share for those six low Shorts was 0.19–0.39, against 0.43–0.59 for the four that passed 1,000 (MC, Windsor via 100-shorts-table and research/115). Viewers who were shown them swiped.
- The pet and WMS Shorts posted 11/12–11/13 read 873–1,100 at 17–51 h (n=6; the dog guilty-look Short at 3 views is left out as stalled, research/117).
- A falling engaged share would point to audience mismatch. The two weeks with enough data say otherwise: 0.4385 (n=24) for the week of 10/26 and 0.456 (n=20) for 11/2. The 11/9 week is 0.39 (n=11) on partial Windsor data.
- Not shown, needs Studio: impressions ("shown in feed") per Short, viewed vs. swiped away, and returning vs. new viewers by week.

**Context: the Bartolozzi era (deleted, n=24, MC).**
- Median 3,717.5; top was 71,397 (kuVrpi1LAqQ).
- `bart-clips/research/03`: the top 10 averaged 21.4 s and 100% average viewed; the bottom 10 averaged 63.9 s and 40%.
- Same lesson as section 2: short Shorts win.

## 3. Long-forms
Per video:
- Views, watch minutes and average view duration (AVD) are MC, as of roughly 11/14.
- % viewed is Windsor (`research/data/100-longform-table.csv`, data to 11/10; n=views in that window).
- 28-day minutes are Windsor (`data/longform-hours.csv`, 11/14).
- **CTR is blank for every video: Studio only.**

| Published (ET) | Title | Length (s) | Views (MC) | AVD s (MC) | % viewed (Windsor) | Watch hours lifetime (MC) | 28-day min (Windsor) | CTR |
|---|---|---|---|---|---|---|---|---|
| 2026-11-11 17:04 | 3 More Bugs in Your House You Should Never Kill (And 5 You Must) | 277 | 2 | 157 |  | 0.09 | 5 | needs Studio |
| 2026-11-07 08:04 | 3 Bugs in Your House You Should Never Kill (And 4 You Must) | 274 | 208 | 74 | 42.84 | 4.33 | 257 | needs Studio |
| 2026-11-05 17:04 | Why the CIA Says "We Can Neither Confirm Nor Deny" | 518 | 3 | 178 | 51.32 | 0.15 | 8 | needs Studio |
| 2026-11-01 17:03 | I Ranked Every Creature Living In Your House From Harmless to Deadly | 538 | 5 | 42 | 9.92 | 0.06 |  | needs Studio |
| 2026-10-29 17:04 | 6 Creatures Living In Your House Right Now (You Never See Them) | 393 | 2 | 43 | 21.85 | 0.02 |  | needs Studio |
| 2026-10-27 14:02 | Conspiracy Theories That Turned Out To Be TRUE | 340 | 5 | 93 | 68.89 | 0.13 | 5 | needs Studio |
| 2026-10-26 14:01 | Weird Animal Facts You Didn't Know (3 Are Fake. Can You Spot Them?) | 617 | 136 | 63 | 11.0 | 2.40 | 141 | needs Studio |
| 2026-10-25 14:04 | Animals Thought Extinct Found Alive (One Was Hiding on a Rock for 80 Years) | 424 | 126 | 56 | 15.7 | 1.99 | 111 | needs Studio |
| 2026-10-24 10:31 | How Wolves Became Dogs (The Funny History of Man's Best Friend) | 501 | 163 | 29 | 20.79 | 1.35 | 75 | needs Studio |
| 2026-10-23 11:10 | 12 Animal Myths You've Believed Your Whole Life (Disney Faked One) | 678 | 5 | 32 | 4.78 | 0.04 |  | needs Studio |
| 2026-10-22 10:32 | Everything You Know About Animals Is WRONG | 135 | 43 | 33 | 41.8 | 0.40 | 22 | needs Studio |
| 2026-11-13 17:00 | Your Life as a House Cat: 8 Ways It Goes Wrong | | 42 (public, 45 h, research/117) | | | | | needs Studio |
| 2026-11-14 08:00 | Don't Kill the Spider in Your Corner. It Eats Bigger Spiders | | 116 (public, 30 h, research/117) | | | | | needs Studio |
| 2026-09-03 (Bart era, deleted) | HNHO_0wmbJg (5:23 per bart-clips/03) | 323 | 2,585 | 15 | | 10.85 | | n/a (deleted: does not count) |

Lifetime long-form watch hours across the 11 live long videos in MC: **10.96 h** (n=11, all published 10/22–11/11, so all inside the 12-month window). The house cat and spider videos (11/13, 11/14) have no hours data yet.

**Studio only:**
- CTR and impressions per video.
- The official 12-month "public watch hours" count (YPP card in Studio > Earn).
- % viewed for the 3 newest long videos.

**Channel-wide CTR on record:**
- 2.50% (Studio, 28 days to 11/11, `skills/channel-brain/KNOWLEDGE.md`).
- 2.07% (Studio AI, about 11/03, `research/64-studio-ai-1103.md`).

### Current pace
| Figure | Value | Source | n |
|---|---|---|---|
| Long-form hours, last 28 days | 10.6 h | Studio paste 11/11, `skills/channel-brain/KNOWLEDGE.md` | channel |
| Long-form hours, last 28 days | 10.4 h (624 min) | Windsor, `research/115-scoreboard-1114.md` | 8 long videos |
| Weekly pace used below | **2.6 h/week** (10.4 ÷ 4) | arithmetic from the Windsor line | |
| Hours banked in the rolling 12 months (nearest available) | **10.96 h** | MC lifetime watch minutes, 11 live long videos | 11 |
| Minutes per long view | 0.91 | research 100 (`skills/channel-brain/KNOWLEDGE.md`) | 28 days |

### Pace math (arithmetic from the figures above, not a forecast)
YPP rules (YouTube Help, answer 72851 and 12843009):
- **4,000** qualified public long-form hours in the last 12 months plus 1,000 subscribers is today's ads tier.
- **8,000** hours in the last 365 days applies to new applicants from 2/1/2027.
- **3,000** hours plus 500 subscribers is the fan-funding and Shopping tier only, not ads.
- Shorts-feed hours, deleted, private and unlisted videos, and ad campaigns don't count. So the Bart-era hours and the September ad views (bart-clips/03 §1b) don't count.

Because the window rolls, the most a steady pace P can ever hold is 52 × P. At 2.6 h/week that's 135.2 h.

| Target | Hours still needed (target − banked) | Weeks at 2.6 h/wk (simple; ignores roll-off) | Can 2.6 h/wk ever reach it in a rolling 12 months? | Weekly pace to hold it in a rolling 12 months (target ÷ 52) | Multiple of current | Weekly pace to reach it in 26 weeks | Weekly pace to reach it by 1/31/2027 (11 weeks from 11/16) | Long views a week at 0.91 min/view, for the 52-week pace |
|---|---|---|---|---|---|---|---|---|
| 3,000 h | 2,989.04 | 1,149.6 | No (max 135.2 h) | 57.7 h | 22.2× | 115.0 h | 271.7 h | 3,804 |
| 4,000 h | 3,989.04 | 1,534.2 | No (max 135.2 h) | 76.9 h | 29.6× | 153.4 h | 362.6 h (applies to the 4,000 tier before the 2/1/2027 change) | 5,072 |
| 8,000 h | 7,989.04 | 3,072.7 | No (max 135.2 h) | 153.8 h | 59.2× | 307.3 h | 726.3 h | 10,144 |

Reading:
- The 4,000 must be held as a rolling 12 months of public long-form hours. Hours older than 12 months drop off, so "weeks at current pace" is only an upper-bound illustration. At 2.6 h/week the window never fills.
- The banked 10.96 h is MC's lifetime figure. Studio's YPP card is the official number; please screenshot it.

## 4. Daily tracker, Nov 16–29 Shorts test
**Test as briefed:** house and spider topics, 16–18 s, 1-second hooks, 3 Shorts a day.
**Targets:**
- (A) Short median of 1,500+ views.
- (B) Long-form CTR of 4%+. MASTER_ORDERS already sets this as its 72-hour long-form bar ("click-through 4% or more (now 2.5%)").

**Conflicts to settle before the test starts. I haven't acted on any of them:**
1. `skills/channel-brain/MASTER_ORDERS.md` currently says new videos are pets or WMS only, with no new bug videos. This test is house and spider topics.
2. The queue in `data/posted.csv` has 3 YouTube Shorts a day for 11/16–11/20 only.
   - It mixes pet (dog tail wag 11/16), WMS (bison 11/21) and 3D explainers (stink bug, fruit fly, clothes moth).
   - It has no YouTube Shorts 11/22–11/24 or 11/26–11/29; 11/25 has only a teaser.
3. Queued lengths: research/103 lists 17.9–19.9 s, and research/92 lists 17.8 s for the dog tail-wag Short. 17.9 and 17.8 s are inside 16–18 s; everything else listed there is over 18 s.
4. Metricool getScheduledPosts for brand 8135499, 11/15–11/29, returned **0 posts**. This brand's TikTok is "fureverfaces", and the channel's own queue may sit under another brand. I can't confirm what is actually scheduled.

**Scoring rules for the sheet:**
- Score views at 48 h, since a Short earns 85% of its views on day 0 (research 100).
- "Test median" is the running median of all test Shorts aged 48 h or more.
- Engaged share comes from Windsor and runs 2–3 days behind.
- Viewed vs. swiped away comes from Studio screenshots.
- Long-form CTR comes from Studio at 72 h for each long video posted in the window. Queued: 11/18 17:00 Christmas tree, 11/21 08:00 house centipede, 11/25 17:00 night shift (`data/posted.csv`).

| Date | Shorts posted (n) | Titles | Lengths (s) | Hook (1-s) used? | Views at 24 h | Views at 48 h | Day median at 48 h | Running test median (n) | ≥1,500 count | Engaged share (Windsor) | Viewed vs. swiped (Studio) | Avg % viewed | Subs gained | Long-form posted | Long-form CTR at 72 h (Studio) | Long-form 28-day hours | Target A met? | Target B met? | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **BASELINE (before 11/16)** | 76 in MC | all Meatball Shorts 10/15–11/11 | 15–20 s bucket median 1,159 (n=23) | v6 median 1,159 (n=27); NEW punch-in 551 (n=4) | | | | **1,018.5** (n=76, MC); house+spider **1,115** (n=44); newest 12: 932 (board.json); brief: 1,007 | 8 of 76 | 0.427 (n=71); house+spider 0.456 (n=44) | blank (Studio) | 69.6 (n=71) | 63 on 60,436 Shorts views = 1.04 per 1,000 (research 100) | 11 live long videos | **2.50%** channel, 28 days to 11/11 (Studio) | 10.4 h (Windsor, research/115) | No | No | Subscribers 1,010 (MC, 11/15) |
| Mon 11/16 | | | | | | | | | | | | | | | | | | | |
| Tue 11/17 | | | | | | | | | | | | | | | | | | | |
| Wed 11/18 | | | | | | | | | | | | | | | | | | | |
| Thu 11/19 | | | | | | | | | | | | | | | | | | | |
| Fri 11/20 | | | | | | | | | | | | | | | | | | | |
| Sat 11/21 | | | | | | | | | | | | | | | | | | | |
| Sun 11/22 | | | | | | | | | | | | | | | | | | | |
| Mon 11/23 | | | | | | | | | | | | | | | | | | | |
| Tue 11/24 | | | | | | | | | | | | | | | | | | | |
| Wed 11/25 | | | | | | | | | | | | | | | | | | | |
| Thu 11/26 | | | | | | | | | | | | | | | | | | | |
| Fri 11/27 | | | | | | | | | | | | | | | | | | | |
| Sat 11/28 | | | | | | | | | | | | | | | | | | | |
| Sun 11/29 | | | | | | | | | | | | | | | | | | | |

**Decision check at the end (11/30, reads to 12/1):**
- Target A is met if the running median of test Shorts at 48 h is 1,500 or more, with n of at least 30. Report the n.
- Target B is met if a long video posted in the window shows 4%+ CTR at 72 h in Studio.
- Report results as the numbers only, with n.

## 5. Data gaps that need Studio screenshots
1. **Viewed vs. swiped away, per Short.** Studio > Analytics > Content > Shorts. Needed for every test Short and the 11/9–11/13 Shorts; it's the column that is blank in the CSV.
2. **Long-form CTR and impressions, per video.** Studio > Content > each long video > Analytics > Reach. Needed for the 11 live long videos plus house cat (11/13) and spider (11/14).
3. **The YPP card (Studio > Earn):** the official 12-month public watch hours and 90-day qualified Shorts views. Repo and MC only give the 10.96 h MC lifetime and 28-day figures.
4. **Shorts "shown in feed" (impressions) by week.** Tells a falling test pool (suppression) apart from falling stay rate (swipes) for the weeks of 11/2 and 11/9.
5. **Audience: new vs. returning viewers and subscriber geography.** Checks whether the Bart-era and India subscribers (bart-clips/03) dilute the subscriber feed for long videos.
6. **The dog guilty-look Short (xIbnhX10r7k):** visibility and restrictions (3 views at about 48 h, research/117).
7. **AVD and % viewed for the house cat and spider long videos,** once out of their first 72 h.
8. **Per-Short subscribers gained after 11/10.** Windsor and MC don't cover it yet.

**What Metricool did and didn't give:**
- Gave: per-video views, watch minutes, AVD, likes, comments and shares through videos published 11/11, plus daily subscribers.
- Didn't give: swipe, retention, impressions, CTR, per-video subscribers, traffic sources (0 rows), titles of deleted videos, or scheduled posts (0 for this brand).
