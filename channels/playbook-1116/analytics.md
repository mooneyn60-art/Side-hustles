# Meatball Myths — own-analytics deep dive

Prepared Mon 11/16/2026, ~2:15 PM ET, for Social Studio. Read-only. No posts, schedules, or repo writes. Every figure has a source and an n. Blanks mean no data, not an estimate. Deleted Joe Bartolozzi clips are excluded from rankings and appear only as context.

**Windows and as-of dates (do not mix them):**

| Label | Window | As of | Source |
|---|---|---|---|
| Studio 28d | Oct 18–Nov 14, 2026 | Screenshots captured ~Nov 15, 8:55 PM ET (`/workspace/yt-studio/*.png`; date axis visible) | YouTube Studio Insights, 28-day toggle |
| Studio 90d table | Views **during** Aug 17–Nov 14, 2026 | Totals.csv through 2026-11-14; zip `Content 2026-08-17_2026-11-15 Meatball Myths.zip` | Per-video views, AVD, avg % viewed, impressions, CTR |
| For videos published on/after Oct 18 | Same as last-28-day views | Same export | Used for Shorts and long-form rankings and breakdowns |
| Shorts CSV | Post time, topic, hook, Windsor subs / engaged-share proxy | Views fields ~Nov 14 | `/workspace/research/2026-11-16-shorts-90d.csv` (119 rows) |
| Metricool | Brand 8135499, YouTube `UCw98RQD81t_339LX5EJqcrg`, TZ America/New_York | Pulled Nov 16, ~2:00–2:05 PM ET | Evolution daily (views complete through Nov 13); published-in-range, 82 videos through Nov 12; best-time heatmap |
| Windsor long-form | last_28d | 2026-11-14 | `skills/oh-meatball/data/longform-hours.csv` |
| Board KPIs | now / last 28d | 2026-11-14 07:40 ET | `data/board/board.json` |

Metricool’s TikTok link is **fureverfaces, not @meatballmyths**. No Meatball TikTok analytics are used here.

**Main analysis set — Meatball Shorts published Oct 18–Nov 15 that appear in the Studio 90d table:** n=86 with views, median **1,007.5**, sum 76,649, **8 of 86** reached 1,500. Fair-age subset (posted by Nov 11, ≥~3 days old as of the Nov 14 export): n=70, median **1,034**, same 8 over 1,500. Three Shorts posted Nov 15 (mice 8:00 AM, shark attacks 2:00 PM, spider leftovers 7:00 PM ET) have no Studio row and no view read — they sit after or at the edge of the Nov 14 export. Several Nov 12–14 Shorts lacked IDs in the CSV but are in the Studio table and are included in the n=86 set.

90d / all-Meatball context (labeled as such, not the 28d set): median 1,018.5, n=76 Metricool reads through Nov 11 (`2026-11-16-shorts-ceiling-and-longform-pace.md`).

---

## 1. Channel snapshot, last 28 days (Studio, Oct 18–Nov 14)

| Metric | Value | Source | Notes |
|---|---|---|---|
| Channel views | **82.8K** (+14.7K vs prior 28d) | `1_overview.png` | |
| Channel watch time | **195.0 hours** | `1_overview.png` | All content, mostly Shorts; **not** YPP public long-form hours |
| Channel subs (net) | **+75** | `1_overview.png`, `4_audience.png` | |
| Total subscribers | **1,017** | `1_overview.png` | Board.json 11/14 public count was 1,010 (YouTube-rounded) |
| 48-hour views | 7,089 | `1_overview.png` | |
| Shorts views | **81.8K** (+14.6K) | `3_shorts_28d.png` | 81.8K of 82.8K channel views |
| Shorts engaged views | 35.9K | `3_shorts_28d.png` | |
| Shorts likes | 833 | `3_shorts_28d.png` | |
| Shorts subscribers | **+97** | `3_shorts_28d.png` | Higher than channel net +75; different tab / attribution. Do not force them to match. |
| Stayed to watch / swiped away | **46.3% / 53.7%** | `3_shorts_28d.png` | Channel Shorts, last 28d. This is the official viewed-vs-swiped rollup. |
| Shorts traffic | Feed 93.6%; YT search 5.4%; channel pages 0.5%; other 0.3%; hashtags 0.0% | `3_shorts_28d.png` | |
| Long-form (“Videos”) views | **946** | `6_videos_reach.png` | Matches the 13 non-Short videos in the 90d table |
| Long-form impressions | 18.5K | `6_videos_reach.png` | |
| Long-form CTR | **2.8%** | `6_videos_reach.png` | Target is 4%+. Older record: 2.50% for 28d to 11/11 (`KNOWLEDGE.md`) |
| Long-form AVD | **1:30** | `6_videos_reach.png` | 946 × 90s = 23.65 implied hours (see YPP) |
| Long-form traffic | Suggested 58.0%; Browse 35.2%; search 2.8%; direct/unknown 1.6%; channel pages 1.6% | `6_videos_reach.png` | Channel rollup, not per video |
| New / casual / regular viewers | **99.3% / 0.7% / 0.0%** | `4_audience.png` | “Audience by watch behavior,” monthly audience 24.8K |
| “Videos growing your audience” (returners, last 90d) | All listed **Low** | `4_audience.png` | Five titles shown, all Low |

Metricool evolution, Oct 19–Nov 16 pull (n=29 daily rows): views **78,941** on 26 days with a view count (Oct 19–Nov 13); Nov 14–16 have subscribers only. Subscribers gained **99**, lost **29**, net **+70** on 26 days with gain/loss (through Nov 13). Subscriber field: 942 on Oct 19 → 1,010 on Nov 13–16 (YouTube-rounded; Studio shows 1,017). Published-video count in the videos field: 82 on 22 days.

Same-page funnel on `6_videos_reach.png` lists 39.7K thumbnail impressions, 3.2% CTR, 1.2K engaged views, 0:46 AVD, and 16.8 watch hours from impressions. That 39.7K matches the lifetime daily-impressions export summed Oct 18–Nov 14 (**39,787**, n=28 days, `yt-studio/csv1/Totals.csv`) and is **channel-wide**, not the Videos-tab 18.5K. Treat the two impression figures as different scopes.

---

## 2. Shorts — views, retention, and post time

Breakdowns below use the fair-age set unless noted: Meatball Shorts published Oct 18–Nov 11, Studio 90d views, n=70. Medians, not means. Length = Studio duration. Topic and hook = Shorts CSV. The one unlabeled aged row is `26,205 Stink Bugs…` (`-Fths6h79_o`, 1,024 views, house-bug title; the leading hyphen on the ID blocked the topic join).

### By topic

| Topic | n | Median views | ≥1,500 | Median avg % viewed (n) | Median CTR (n) | Subs gained (n with data) |
|---|---:|---:|---:|---:|---:|---|
| House bug | 30 | **1,138.5** | **6** | 79.88 (30) | 3.32% (30) | 31 (27) |
| WMS | 4 | 1,123.5 | 0 | 58.79 (4) | 2.64% (4) | 2 (4) |
| Spider | 12 | 1,104.5 | **2** | 69.80 (12) | 4.23% (12) | 8 (11) |
| Unlabeled (stink bugs; see note) | 1 | 1,024 | 0 | 56.86 (1) | 3.38% (1) | no data |
| Other animals | 17 | 667 | 0 | 62.73 (17) | 2.46% (17) | 17 (17) |
| Case files / mysteries | 6 | **57.5** | 0 | 46.77 (6) | 1.25% (6) | **0 (6)** |

House bug + spider together: n=42, median 1,126.5, **all 8** of the ≥1,500 Shorts. Adding the stink-bugs row does not change the story.

Including younger 28d Shorts (no age cut, n=86) adds: WMS n=5, median 1,024; pets n=3, median 859 (includes the 3-view dog guilty-look Short); news n=4, median 183.5 (FAA / Jensen, 31–39 s). Those young rows are incomplete and are not used in the aged table.

### By length

| Length | n | Median views | ≥1,500 | Median avg % viewed (n) |
|---|---:|---:|---:|---:|
| 15–18 s | 21 | **1,159** | **5** | **89.08** (21) |
| 19–20 s | 8 | 988.5 | 2 | 74.12 (8) |
| 21–29 s | 29 | 1,033 | 1 | 61.41 (29) |
| <15 s | 1 | 528 | 0 | 126.01 (1) |
| 30 s+ | 11 | **411** | **0** | 47.92 (11) |

15–20 s combined: n=29, median 1,153, 7 of the 8 ≥1,500. 90d context (all Meatball in Metricool, not 28d): 15–20 s median 1,159, n=23; 30 s+ median 397, n=9 (`shorts-ceiling-and-longform-pace.md`).

### By hook (first second)

| Hook | n | Median views | ≥1,500 | Median avg % viewed (n) |
|---|---:|---:|---:|---:|
| Teaser | 1 | 2,316 | 1 | 109.59 (1) |
| v6 close-up + title stamp | 26 | **1,156** | **5** | 82.42 (26) |
| NEW punch-in + 2-line hook text | 3 | 1,085 | 0 | 55.78 (3) |
| Unlabeled (stink bugs) | 1 | 1,024 | 0 | 56.86 (1) |
| Older format (photo / quiz / case / soap) | 33 | 856 | 1 | 60.97 (33) |
| 3D explainer open | 6 | 824.5 | 1 | 75.01 (6) |

The teaser row is a single video (House Centipede, #2). Do not treat n=1 as a winning format. NEW punch-in n=3 includes late 11/11 posts. Hook type overlaps with topic and era.

### By post time (ET)

Observed medians by hour bucket are **flat** in the mid-day / evening slots (n=70):

| Hour (ET) | n | Median views | ≥1,500 |
|---|---:|---:|---:|
| 12–15 | 22 | 1,054.5 | 2 |
| 19–23 | 12 | 1,044.5 | 2 |
| 16–18 | 18 | 1,038 | 3 |
| 00–05 | 1 | 1,024 | 0 |
| 06–11 | 17 | 938 | 1 |

By weekday (confounded by topic; Saturday n=6 is small and includes two of the top five): Sat 1,362 (n=6); Sun 1,153 (n=11); Tue 1,091.5 (n=12); Wed 993 (n=12); Fri 981.5 (n=8); Mon 968 (n=13); Thu 621 (n=8).

**Metricool best-time heatmap** (audience-online values, Oct 19–Nov 16, America/New_York; not the same as “what we posted then”): **4 PM ET is the top hour every day**. Highest cells: Wed 4 PM (12,033) and Thu 4 PM (11,979). Weekends at 4 PM are about half (Sat 5,880, Sun 5,648). This says when viewers are on YouTube, not that Thursday posts in this set performed well.

### 11/11 later posts (swipe, not a clean topic fail)

Four Meatball Shorts timestamped Nov 11 in the joined ET data, plus the Nov 10 7:02 PM House Centipede that Studio dates Nov 11 UTC. Later Nov 11 slots:

| ET time | ID | Title | Views | % viewed | Length | Engaged-share proxy |
|---|---|---|---:|---:|---:|---:|
| 10:07 | ExqLbAxnFPc | Hairy Spider on Your Floor | 1,085 | 55.78 | 33 s | 0.43 |
| 12:31 | IvskPD8cY8I | Roaches Fit Through 2-Penny Cracks | 969 | 78.01 | 18 s | 0.38 |
| 14:31 | sPrA70BWGtg | Boxelder Bugs Can Fly Up to 2 Miles | 888 | 76.66 | 18 s | 0.39 |
| 16:01 | vn-MTvvQsbg | Hunchback Cricket in Your Basement | 123 | 44.73 | 33 s | 0.36 |

Proxies are Windsor engaged share in the Shorts CSV (Studio viewed-vs-swiped is still blank per Short except the Daddy Longlegs example). 0.36–0.39 on the last three sits well below a typical ~0.43–0.46 house-bug/spider share in the earlier 90d work and is consistent with swipe-away, especially on the 33 s cricket (123 views).

---

## 3. Long-forms — last 28 days

All 13 Videos-tab titles were published inside this window, so the Studio 90d table is effectively last-28-day / lifetime-to-Nov-14. n=13. Channel Videos tab: 946 views, 2.8% CTR, 1:30 AVD (`6_videos_reach.png`). “3 Bugs…” intro: **70% still watching at 0:30**, above typical intros (same screenshot).

| ID | Title | Published | Dur. | Views | Avg % viewed | AVD | Impr. | CTR | Windsor 11/14 min (views, % if any) |
|---|---|---|---:|---:|---:|---|---:|---:|---|
| cH3HCZ8GlHk | 3 Bugs in Your House You Should Never Kill (And 4 You Must) | Nov 7 | 4:34 | **214** | **42.71** | 1:57 | 1,856 | **5.44%** | 257 (208, 43.6%) |
| Uqj0QL8G0d4 | How Wolves Became Dogs | Oct 24 | 8:21 | **163** | 20.42 | 1:42 | 1,558 | 1.99% | 75 (139, 24.6%) |
| z-Kg8sXCxlU | Weird Animal Facts You Didn't Know (3 Are Fake…) | Oct 26 | 10:17 | 134 | **11.00** | 1:07 | **5,262** | 1.82% | 141 (134, 11.0%) |
| o9Emu9oMgCs | Animals Thought Extinct Found Alive | Oct 25 | 7:04 | 126 | 15.85 | 1:07 | 3,438 | 2.53% | 111 (119, 15.8%) |
| KWOM2-mNmww | Don't Kill the Spider in Your Corner… | Nov 14 | 8:17 | 114 | 22.33 | 1:50 | 1,771 | **4.63%** | no data (too new for Windsor 11/14) |
| xeAsg5ECpgw | 3 More Bugs… (And 5 You Must) | Nov 11 | 4:37 | 88 | 23.68 | 1:05 | 1,510 | **4.37%** | 5 (2, 56.7%) — Windsor lag |
| gFhrONKK0rI | Everything You Know About Animals Is WRONG | Oct 22 | 2:15 | 43 | 41.80 | 0:56 | 750 | 2.93% | 22 (37, 45.0%) |
| viD-nbPdaxk | Your Life as a House Cat: 8 Ways It Goes Wrong | Nov 13 | 9:17 | 42 | 24.17 | 2:14 | 1,439 | 1.95% | no data |
| RwbgzQisvYM | 12 Animal Myths You've Believed… | Oct 23 | 11:18 | 6 | 6.58 | 0:44 | 399 | 1.25% | no data |
| 2EC5LDtbUbo | Conspiracy Theories That Turned Out To Be TRUE | Oct 27 | 5:40 | 5 | 68.89 | 3:54 | 115 | 0.87% | 5 (1, 99.8%) |
| bqij8Ht6SX4 | I Ranked Every Creature Living In Your House… | Nov 1 | 8:58 | 5 | 9.92 | 0:53 | 305 | 1.31% | no data |
| Lid8JXhg1Q4 | 6 Creatures Living In Your House Right Now | Oct 29 | 6:33 | 3 | 23.36 | 1:31 | 33 | 6.06% | no data |
| 4-gvZTWf2wg | Why the CIA Says "We Can Neither Confirm Nor Deny" | Nov 5 | 8:38 | 3 | 51.32 | 4:25 | 149 | 0.67% | 8 (2, 51.3%) |

**By views:** (1) 3 Bugs, 214; (2) Wolves, 163.

**By avg % viewed, among videos with ≥40 views:** (1) 3 Bugs, 42.71% (n=214 views); (2) Everything You Know, 41.80% (n=43; 2:15 quiz). High percentages on 3–5 views (Conspiracy 68.89%, CIA 51.32%) are left out of that ranking — n is too small.

**CTR ≥4% (the test target):** 3 Bugs 5.44%, Don't Kill the Spider 4.63% (posted Nov 14, still young), 3 More Bugs 4.37%. `6 Creatures` is 6.06% but on 33 impressions and 3 views — ignore as a target hit.

Pattern: the “bugs/spiders you should never kill” packaging has the views, the retention, and the CTR. High-impression quiz/myth long-forms do not (Weird Animal Facts: 5,262 impressions, 1.82% CTR, 11% viewed, 134 views; 12 Animal Myths: 6 views, 6.58% viewed).

---

## 4. Top 5 and bottom 5 videos (Meatball Shorts, last 28d, by Studio views)

Bartolozzi-era clips are out of this list. Bottom 5 uses the fair-age set (posted by Nov 11) so brand-new posts are not dinged for age. IDs and numbers are from the Studio 90d table and match the Top Shorts 28d card on `3_shorts_28d.png` (2.4K / 2.3K / 1.9K / 1.9K / 1.9K, rounded).

### Top 5

| # | ID | Title | Views | % viewed | Length | Topic / hook | Posted ET | CTR (impr.) | Why (from the numbers) |
|---|---|---|---:|---:|---:|---|---|---|---|
| 1 | Us0zIbxiR-A | Are Daddy Longlegs the Most Venomous Spiders? | 2,445 | 96.60 | 20 s | Spider / older question title | Sat 10/24, 4:02 PM | **5.95%** (2,118) | Only top Short with real thumbnail volume. 53.7% stayed vs swiped (`3b_short_single_example.png`), vs channel 46.3% stayed. A 48-hour traffic slice on that same page was YouTube search 43, Shorts feed 10, other 2 (equals the 55 48-hour views — not lifetime traffic). Searchable question title. Since published: 6.8 watch hours, **+1 sub**, 17 likes. |
| 2 | EPimwC5VMgo | The Bug You Squish Is Protecting You (House Centipede) | 2,316 | **109.59** | 16 s | House bug / teaser (n=1) | Tue 11/10, 7:02 PM | 1.69% (236) | Feed-native: almost no thumbnail impressions, heavy replay. Highest Windsor subs in the 28d CSV (**+7**). |
| 3 | 1hdMaSxJtkU | Your Roach Has 40 Babies | 1,988 | 75.12 | 20 s | House bug / 3D explainer | Wed 11/4, 7:03 PM | 2.34% (214) | House-bug + ~20 s, low impressions / feed path. +1 sub. |
| 4 | wHCrmIPdCgg | Your Bed Mites Die at 130°F | 1,975 | **145.76** | 16 s | House bug / v6 | Sat 11/7, 2:03 PM | 2.36% (127) | Highest replay in the top 5. 15–18 s + v6 + house bug. 0 subs in the CSV. |
| 5 | bm6LzV7eRwg | 3 'Mommy Longlegs' in Your Home | 1,922 | 97.27 | 16 s | Spider / v6 | Mon 11/9, 4:03 PM | 3.26% (215) | Same 16 s / v6 / spider-in-the-house pattern. 0 subs in the CSV. |

#6–8 also cleared 1,500, all house bug, 16–17 s, v6: `heI2W3z1hk4` 1,860 (89.21%, +3 subs); `1RJw2Pex_Ro` 1,779 (76.96%, +2); `s_L3sGikMWU` 1,647 (103.02%, 23 s, 0 subs).

### Bottom 5 (posted by Nov 11)

| # | ID | Title | Views | % viewed | Length | Topic / hook | Posted ET | CTR (impr.) | Why (from the numbers) |
|---|---|---|---:|---:|---:|---|---|---|---|
| 1 | C7KaAarFUag | Operation Northwoods: The Conspiracy That Was TRUE | 1 | 42.09 | 23 s | Case file / older | Mon 10/26, 5:31 PM | 1.75% (57) | Case-file topic, low hold, low CTR, 0 subs. |
| 2 | 88gaODWt4qY | The US Planned to Nuke the Moon | 10 | 69.61 | 25 s | Case file / older | Mon 10/26, 11:07 AM | 1.60% (125) | Same topic bucket (median 57.5, n=6, 0 subs). |
| 3 | gxi2NH2uuVk | What REALLY Crashed at Roswell? | 27 | 40.61 | 27 s | Case file / older | Mon 10/26, 3:02 PM | 1.09% (366) | Impressions arrived; people did not stay (40.61%) or click (1.09%). |
| 4 | YrPzxjXZJCY | This Spider Hides in Your Shoes… Venom Can Kill Skin | 48 | **141.06** | 17 s | Spider / v6 | Tue 11/3, 12:03 PM | **6.14%** (228) | Hold and CTR are excellent. Distribution did not follow. No data on a restriction; flag for Studio visibility. 0 subs. |
| 5 | 66YDY0wDiaU | 8 Weeks of Mites in Your Skin | 65 | 87.99 | 16 s | House bug / v6 | Wed 11/4, 10:08 AM | 2.57% (545) | On-format (16 s, v6, house bug) with **more** impressions than any top-5 feed Short except Daddy Longlegs, but it did not take off. 0 subs. |

Not in the bottom 5 because of the age rule, but flagged: **dog guilty-look** `xIbnhX10r7k`, posted Fri 11/13 1:00 PM ET, **3 views**, 99.87% viewed, 9.09% CTR on **11 impressions**. Needs a Studio visibility / restriction check (already on the gap list). News explainers from 11/13 (FAA, Jensen) are 90–470 views at 31–39 s — short history, long runtime, not ranked here.

---

## 5. What moves subscribers

**Channel:** net **+75** in 28d (Studio); total **1,017**. Shorts tab **+97**. Metricool: +99 / −29, net +70 through Nov 13 (n=26 days). The three figures agree on direction and rough size; they are not the same report.

**Per-video subs are incomplete.** Metricool has no per-video subscriber metric. Windsor `subs_gained` in the Shorts CSV covers **66 of 89** Meatball Shorts posted in the window, total **63** subs on **61,676** views = **1.02 per 1,000 views**. Nothing after ~Nov 10 in that field. Studio example: Daddy Longlegs, #1 Short, is only **+1** since published (`3b_short_single_example.png`).

Windsor per-topic (same 66, views are the CSV’s ~Nov 14 reads, not the Studio column):

| Topic | n | Subs | Views | Subs / 1,000 views |
|---|---:|---:|---:|---:|
| House bug | 28 | 36 | 32,270 | 1.12 |
| Other animals | 17 | 17 | 12,266 | 1.39 |
| Spider | 11 | 8 | 12,453 | 0.64 |
| WMS | 4 | 2 | 3,956 | 0.51 |
| Case files / mysteries | 6 | **0** | 731 | 0.00 |

Other-animals convert slightly better **per view** but do not get the views (median 667). House bugs deliver both volume and most of the raw subs. The single biggest Windsor row is House Centipede at **+7**. Case files added none.

**Returning audience is effectively zero.** 99.3% new / 0.0% regular (`4_audience.png`). Every title on “videos growing your audience” (new viewers who returned, last 90d) is marked Low. The channel is still a first-impression machine, not a subscriber feed.

No per-long-form subscriber data.

---

## 6. YPP progress

Official Studio > Earn card (12-month public long-form hours and 90-day qualified Shorts views): **no data**. Not in the screenshot set.

| Threshold | What we can read | Pace |
|---|---|---|
| **1,000 subscribers** | **Met.** 1,017 (Studio, ~Nov 15); 1,010 public/Metricool on 11/14–16 | Net +75 in 28d (Studio) |
| **4,000 public long-form hours** in a rolling 12 months (8,000 for new applicants after 1/31/2027) | Official count: no data. Nearest figures, **do not treat as the Earn card:** Windsor last-28d **10.4 h** (624 min, n=8 videos, 11/14); previously computed Metricool lifetime watch minutes **10.96 h** (n=11 live long videos, all published 10/22–11/11, ceiling doc 11/15); Studio 90d table views × AVD = **24.5 h** (n=13, through Nov 14); Videos-tab 946 × 1:30 = **23.65 h**. Channel-wide watch time **195.0 h** in 28d is almost all Shorts and **does not count** toward this threshold. | From Windsor 10.4 h / 4 wk = **2.6 h/week** → a steady year holds ~135 h. From the higher Studio-derived 24.5 h / 4 wk = **6.1 h/week** → a steady year holds ~317 h. Either way, **4,000 is not reachable at current pace** (holding 4,000 needs 76.9 h/week; arithmetic only, not a forecast). Deleted Bart-era hours do not count (YouTube Help). |
| **10M Shorts views in 90 days** (alternative path) | Official qualified count: no data. Computable 90d-table views (Aug 17–Nov 14): all Shorts **242,916** (n=236 rows with a view); of that, Bart-titled **166,036** (n=38, mostly August, deleted, likely ineligible); Meatball Shorts published in the last 28d **76,649** (n=86). Studio Shorts **81.8K** is last-28-day views on all Shorts, including residual older ones. | Even the larger 242,916 figure is **~2.4% of 10M**. 81.8K in 28d does not scale to 10M in 90d. |

**Bartolozzi context (not in rankings):** 24 deleted Certified Bart clips, Metricool median 3,717.5; the 90d Studio table still shows 166,036 views on 38 Bart-titled Shorts in Aug 17–Nov 14. Earlier research: 709 of 883 subs gained 6/17–10/12 came from India (`bart-clips/research/03`). Deleted videos do not count for YPP. Subscriber-country for the current 1,017 is still a Studio gap.

---

## 7. Data gaps

Now filled, from the Nov 15 Studio screenshots and the 90d Content export (through Nov 14):

- Channel Shorts viewed vs swiped (46.3% / 53.7%).
- Per-video CTR and impressions for everything in that export, including the 13 long-forms.
- New vs returning viewers (99.3% / 0.0% regular).
- Long-form AVD and % viewed for the Nov 13 house-cat and Nov 14 spider videos.
- Channel Videos traffic mix (suggested 58.0%, browse 35.2%).

**Still needed (screenshot or official export):**

1. **Studio > Earn card** — official 12-month public long-form hours and 90-day qualified Shorts views. Required to close the Windsor 10.4 h vs Studio-derived 24.5 h gap.
2. **Per-Short viewed vs swiped** for the 11/11 set and for every test Short through 11/29. Channel rollup only, plus one Daddy Longlegs example, is not enough.
3. **Per-Short subscribers gained after ~Nov 10**, and per-long-form subs. Windsor stops; Metricool has no such field.
4. **Subscriber country** — to test whether the Bart-era India subs still dominate the 1,017.
5. **Shorts shown-in-feed (impressions) by week** — to separate a smaller test pool from a worse stay rate.
6. **Visibility / restrictions on** `xIbnhX10r7k` (dog guilty-look, 3 views, 11 impressions) and on `YrPzxjXZJCY` (48 views despite 141% viewed and 6.14% CTR).
7. **Notifications-off long-form test** — 11/18 and 11/25 not yet posted as of this writing. Need first-72-hour views, AVD, and browse/suggested share vs other recent long-forms, for the 11/30 verdict.
8. **@meatballmyths TikTok Studio** (or a Metricool reconnect). This brand is linked to fureverfaces. Board.json 11/14 public follower count is 9,323; that is not analytics.

---

## 8. The 5 changes the data most supports

Current approved test through 11/29: Shorts on bugs, spiders and WMS only; pets paused; target Short median 1,500+; Shorts ≤18 s; two long-forms on 11/18 and 11/25 with notifications off. The numbers below support holding that test, with these sharpenings.

1. **Keep Shorts at 15–18 s, and treat 30 s+ as a failed bucket.** In the last-28d fair-age set, 15–18 s has median **1,159 views** (n=21) and **5 of the 8** Shorts that reached 1,500, plus the highest median % viewed (89.08). 30 s+ has median **411** (n=11) and **zero** over 1,500. This is the same direction as the 90d Metricool read (15–20 s median 1,159, n=23; 30 s+ median 397, n=9). The 11/11 hunchback cricket (33 s, 123 views, 44.73% viewed, engaged share 0.36) is the in-period example of going long and getting swiped.

2. **Stay on house-bug and spider Shorts (WMS as the third approved topic); do not bring back case files, and do not add news or other-animals volume.** House bug median **1,138.5** (n=30, 6 of 8 ≥1,500); spider **1,104.5** (n=12, the other 2); together they account for every Short over 1,500. WMS median 1,123.5 (n=4, small, none over 1,500) — keep measuring through 11/29, do not expand the claim. Case files median **57.5** (n=6), **0 subs**. Other animals median **667** (n=17), 0 over 1,500 — slightly better subs per 1,000 views (1.39 vs house bug 1.12) but no distribution. News explainers in this window: median 183.5 (n=4, young, 31–39 s). Pets are already paused (n=3, median 859, including a 3-view stall).

3. **Default the hook to v6 close-up + title stamp, and write searchable question titles when the topic allows.** v6 median **1,156** (n=26), **5 of 8** over 1,500. Older-format hooks median 856 (n=33). #1 Short, Daddy Longlegs, is a question title with **2,445** views, 96.6% viewed, **5.95% CTR**, 2,118 impressions, and a 48-hour slice that was mostly YouTube search — unlike the other toppers, which are feed-native (127–236 impressions). Do not generalize “teaser” or “NEW punch-in” from n=1 and n=3.

4. **Package long-forms like “3 Bugs in Your House You Should Never Kill,” not like the high-impression quiz/myth videos.** 3 Bugs: **214** views, **42.71%** viewed, AVD 1:57, **5.44% CTR** (already over the 4% target), 70% still watching at 0:30. Two sequels also cleared 4% CTR (Don't Kill the Spider 4.63%, 3 More Bugs 4.37%) even with less age and fewer views. Weird Animal Facts is the counterexample: **5,262** impressions, **1.82% CTR**, **11%** viewed, 134 views. 12 Animal Myths: 6 views, 6.58% viewed, 1.25% CTR. Use the 11/18 and 11/25 notifications-off posts to test this packaging, and read CTR / AVD / browse-vs-suggested at 72 hours.

5. **Do not add volume to chase YPP, and do not stack many Shorts on one day.** Subs are already over 1,000 (1,017). The hours path, even using the **higher** Studio-derived 24.5 h in 28d (~6.1 h/week), only holds ~317 h in a rolling year — far from 4,000 (76.9 h/week to hold). The Shorts-views path is not close either (81.8K Shorts views in 28d; 76,649 Meatball Shorts views in the 90d table for this period’s posts). Meanwhile the audience is **99.3% new / 0% regular**, and even a 2,445-view Short added **one** subscriber. The 11/11 later slots were swiped (engaged share 0.36–0.39). Hold the approved cadence and topics through 11/29; post around **4 PM ET** when Metricool says the audience is on YouTube (Wed/Thu strongest; weekends about half), but treat time as secondary to length, topic, and hook. Reconnect @meatballmyths in Metricool or send TikTok Studio screenshots before any TikTok plan uses numbers.

