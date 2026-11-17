# Meatball Myths: baseline retention audit (Nov 16, 2026)

Prepared for Social Studio, Mon Nov 16, 2026, about 6:43–6:56 PM ET. **Read-only: nothing was posted, scheduled, committed, or changed.**

**Accounts:** YouTube [@MeatballMyths](https://www.youtube.com/@MeatballMyths) (`UCw98RQD81t_339LX5EJqcrg`). TikTok [@meatballmyths](https://www.tiktok.com/@meatballmyths).

**Window:** last 30 days, Oct 17–Nov 16, 2026, America/New_York.

**How to read numbers:** every figure cites a source. Metricool AVD is average view duration, not a per-second retention curve. Recommendations that go beyond a measured number are marked **hypothesis**.

---

## Sources and limits

| Source | What it covers | Fetched |
|---|---|---|
| Metricool brand `8135499`, timezone America/New_York. Called `getAnalyticsAvailableMetrics` first, then `getAnalyticsDataByMetrics` | YouTube evolution (`YTEV01–06`, `YTEV10–19`) and per-video published-in-range (`YTVP01/02/04–09/11/12/17`). Last published video in the extract: Nov 12. Last day with view counts: Nov 13. Subscriber snapshot continues through Nov 16. | ~6:43 PM ET, Nov 16, 2026 |
| yt-dlp, public YouTube Videos and Shorts tabs | Duration, exact public view count, publish time (UTC → ET) | ~6:50–6:52 PM ET, Nov 16, 2026 |
| [Social Blade, `UCw98RQD81t_339LX5EJqcrg`](https://socialblade.com/youtube/channel/UCw98RQD81t_339LX5EJqcrg) | Lifetime channel views, daily views Nov 2–16 | ~6:52 PM ET, Nov 16, 2026 |
| yt-dlp + TikTok profile HTML + Social Blade TikTok user page | Public TikTok post views, likes, comments, shares, duration, publish time; profile follower / like counts | ~6:44 PM ET (posts) and ~6:53–6:54 PM ET (profile), Nov 16, 2026 |
| `channels/research/deep-growth-research-1116.md` | Goals, YPP deadline, TikTok Rewards 1,000-view rule | Same day, earlier |

**Unavailable in this pull (stated so we do not invent them):**
- Per-second retention curves, audience-retention graphs, and YouTube "viewed vs swiped." Metricool has no such fields for YouTube.
- YouTube traffic sources: `YTTS01/YTTS02` returned no rows.
- Metricool TikTok: `getAnalyticsDataByMetrics` for TikTok evolution returned one all-zero row dated 2026-11-16; the posts connector (`TKPO*`, including average time watched and full-video watched rate) returned no rows. **Same empty result as last time.** Brand settings list `tiktokData: "fureverfaces"` on this brand, while `youtubeData` is the Meatball Myths channel ID. Public TikTok is used instead. There is no TikTok AVD or % watched in this audit.
- Trailing 12-month YouTube Partner Program qualified watch hours (Studio Earn tab is not in Metricool or on any public page).
- Note: Metricool `YTEV02` period views (78,996, Oct 17–Nov 13) exceed Social Blade lifetime views (78,693, Nov 16). The sources disagree; treat channel-level view totals as approximate.

Shorts vs long-form are classified by the public tabs, not by title. Publish times below are yt-dlp timestamps converted to ET. Metricool `YTVP02` values are 5 hours ahead of those times and are treated as UTC.

---

## 1. Goals this audit is for

From `channels/research/deep-growth-research-1116.md`, citing [YouTube Help](https://support.google.com/youtube/answer/12843009?hl=en-12) and the [YouTube Blog YPP 2027 update](https://blog.youtube/news-and-events/youtube-partner-program-updates-2027-new-opportunities-earn/):

- YouTube: apply to YPP under today's **4,000** public long-form watch-hour bar before **Jan 31, 2027**. From **Feb 1, 2027**, new applicants need **8,000** hours. The 1,000-subscriber bar is already met (see below). Shorts-feed watch time does not count toward hours.
- TikTok Creator Rewards: a post starts earning only after **1,000 For You feed views**, with qualified-view length rules (5+ seconds on FYP; 30+ seconds on Search) in the countries TikTok lists. Public view counts are **total** views, not FYP vs Search. This audit cannot confirm qualified views.

---

## 2. Channel snapshot

**YouTube**

| Metric | Value | Source |
|---|---|---|
| Subscribers | 942 (Oct 19) → **1,010** (Nov 13–16) | Metricool `YTEV01` |
| Followers gained / lost in the request window | +99 / −29 | Metricool `YTEV05` / `YTEV06` sums |
| Channel views in period, Oct 17–Nov 13 | **78,996** | Metricool `YTEV02` sum (28 days with views; Nov 14–16 are null) |
| Lifetime channel views | **78,693** | Social Blade, Nov 16 |
| Social Blade views after Metricool's last view day | Nov 14: +2,858 (73,377 lifetime); Nov 15: +1,950 (75,327); Nov 16: +3,366 (78,693) | Social Blade daily table |
| Videos published in Metricool range | **84** (71 Shorts still on the Shorts tab + 11 long-forms + 2 "Oh Meatball" story posts no longer on the Shorts tab) | Metricool published-in-range, classified against public tabs |
| Views on those 84 videos | **64,057** | Metricool `YTVP06` sum |
| Public catalog now | 13 long-forms + 88 Shorts; 1,010 subscribers | yt-dlp tabs, ~6:50–6:52 PM ET |
| Ad revenue in Metricool | 0 | Metricool `YTEV03` |

**TikTok (public only)**

| Metric | Value | Source |
|---|---|---|
| Followers / likes / following / public videos | **9,316** / 3,258 / 11 / 109 | TikTok profile HTML (`followerCount`, `heartCount`, `followingCount`, `videoCount`), matched on Social Blade TikTok, ~6:53–6:54 PM ET |
| Posts in the public grid | **109**, dated Oct 23–Nov 16 | yt-dlp, ~6:44 PM ET |
| Total public views on those 109 | **81,786** | same |
| Median public views | **233** (≤60 s: 359.5, n=18; >60 s: 221, n=91) | same |
| Posts at 1,000+ **total** views | **9 of 109** | same |

---

## 3. The drop-off pattern

**Team benchmark, now checked:** Social Studio's brief said the median Shorts drop is about 7 seconds. In this Metricool extract, median Shorts **average view duration is 7 seconds** (`YTVP08`, 71 Shorts published Oct 17–Nov 12). That is a confirmed median AVD, not a verified per-second cliff. Most of those Shorts are 15–30 s long (median length **22 s**, yt-dlp duration), so a 7 s AVD is roughly one-third of the typical video.

| Shorts length (yt-dlp) | n | Median views (`YTVP06`) | Median AVD (`YTVP08`) | Median AVD ÷ length |
|---|---:|---:|---:|---:|
| ≤15 s | 10 | 1,177 | 6.5 s | 45.0% |
| 16–20 s | 20 | 1,139 | 7.0 s | 43.8% |
| 21–30 s | 32 | 1,022.5 | 6.0 s | 26.0% |
| 31–60 s | 8 | 404.5 | 8.0 s | 21.6% |

AVD alone does not make a hit: one Short held **15 s AVD on a 17 s** video (88.2% proxy retention) and still only got 48 Metricool views (see brown recluse, below). Distribution still dies on some well-watched videos.

**Series medians, Metricool Shorts views** (plus the 2 Oh Meatball posts for that row):

| Series (grouped by title) | n | Median views | Median AVD | Best in group |
|---|---:|---:|---:|---:|
| Things Living In Your House | 34 | 1,155 | 7.0 s | 1,985 |
| Would Meatball Survive? | 4 | 1,126.5 | 5.5 s | 1,256 |
| Meatball vs Spiders | 2 | 1,119 | 6.0 s | 1,270 |
| Is This Spider Venomous? | 5 | 1,055 | 8.0 s | 1,823 |
| Other / one-off | 12 | 1,027.5 | 6.5 s | 2,390 |
| True/False | 8 | 493.5 | 7.0 s | 1,108 |
| Case files / conspiracy | 6 | 57.5 | 4.5 s | 432 |
| Oh Meatball (Pts 3–4) | 2 | 24.5 | 8.0 s | 31 |

House-bug and spider lanes clear the ~1,000-view Shorts test batch. Conspiracy/case-file Shorts and the Oh Meatball story posts do not. True/False is the soft middle.

**Long-form pattern:** of 11 long-forms in the Metricool window, only one has enough views for a stable AVD: "3 Bugs in Your House You Should Never Kill (And 4 You Must)" at **74 s AVD** on a **273 s** video (27.1% proxy retention, 208 Metricool views). The other long-forms with 100+ Metricool views sit at 29–63 s AVD on 7–10 min videos (about 6–13% proxy retention). AVDs on videos with 2–5 views are too thin to use.

---

## 4. Five best and five worst YouTube Shorts

Metricool window only (published Oct 17–Nov 12), ranked by Metricool views. Public views and length are from yt-dlp later the same evening. Hook lines, where present, are from `channels/research/2026-11-16-shorts-90d.csv` (column `first_sentence`).

**Best 5 (Metricool views)**

| # | Title (current public title if different) | Metricool views / likes / AVD | Length | AVD÷len | Public views | Posted (ET) | What differs |
|---|---|---|---:|---:|---:|---|---|
| 1 | Are Daddy Longlegs the Most Venomous Spiders? (`Us0zIbxiR-A`) | 2,390 / 16 / 9 s | 20 s | 45.0% | 2,474 | Oct 24, 3:02 PM | One-off spider myth. Opening line in the 90d file: "Daddy long legs are the most venomous spiders." Highest Short in the window; still under 2,500. |
| 2 | Your Roach Has 40 Babies (`1hdMaSxJtkU`) | 1,985 / 16 / 8 s | 20 s | 40.0% | 1,991 | Nov 4, 7:03 PM | House-bug series. Opening: "Meatball, your roach is carrying 40 babies." |
| 3 | Your Bed Mites Die at 130°F (`wHCrmIPdCgg`) | 1,974 / 19 / **11 s** | **15 s** | **73.3%** | 1,955 | Nov 7, 2:03 PM | Shortest of the top 5, highest AVD and likes. Opening: "Wash your sheets under 130 degrees, and the mites in your bed live." |
| 4 | Bed Bugs Crawl 100 Feet a Night to Your Bed (`heI2W3z1hk4`; Metricool title omitted "Bed Bugs Crawl") | 1,855 / 13 / 7 s | 16 s | 43.8% | 1,862 | Nov 8, 8:03 AM | House-bug, posted early morning. Opening: "Something can crawl 100 feet tonight just to reach your bed." |
| 5 | 3 'Mommy Longlegs' in Your Home (`bm6LzV7eRwg`) | 1,823 / 3 / 8 s | 16 s | 50.0% | 1,918 | Nov 9, 4:03 PM | Spider-venomous series. Opening: "You asked for mommy long legs." Low likes for its views. |

**Also notable, not in the Metricool-views top 5:** "The House Centipede You Squish Is Protecting You" (`EPimwC5VMgo`) was 1,664 Metricool views (AVD 10 s, 15 s long, 66.7% proxy) and had grown to **2,302** public views by 6:52 PM ET — now second on the public Shorts tab. After the Metricool publish cutoff, "House Centipede vs Spider in Your Basement" (`L6xt-kze48M`, Nov 14, 11:04 AM ET, 19 s) has **2,149** public views and no AVD in Metricool yet.

**Worst 5 that had time to finish a test** (weeks old, public views still low; newer Shorts still accumulating are listed after)

| # | Title | Metricool views / likes / AVD | Length | AVD÷len | Public views | Posted (ET) | What differs |
|---|---|---|---:|---:|---:|---|---|
| 1 | Operation Northwoods: The Conspiracy That Was TRUE (`C7KaAarFUag`) | 2 / 0 / 5 s | 22 s | 22.7% | 1 | Oct 26, 4:31 PM | Case-file Short, not a house bug. 90d csv tags the hook as "older format (real photo / quiz / case / soap)." |
| 2 | The US Planned to Nuke the Moon (`88gaODWt4qY`) | 11 / 0 / 7 s | 24 s | 29.2% | 10 | Oct 26, 10:07 AM | Same case-file lane and hook tag. |
| 3 | What REALLY Crashed at Roswell? (`gxi2NH2uuVk`) | 27 / 0 / **4 s** | 27 s | 14.8% | 27 | Oct 26, 2:02 PM | Same lane. Lowest AVD in this worst-five. |
| 4 | 8 Weeks of Mites in Your Skin (`66YDY0wDiaU`) | 58 / 3 / 6 s | 15 s | 40.0% | 68 | Nov 4 (Metricool `YTVP02` 15:08:54, treat as 10:08 AM ET) | House-bug topic, short length, still missed the ~1,000-view batch. Exception, not the series rule. |
| 5 | The CIA Tried to Steal a Soviet Sub (`taxvYvHCK5k`) | 88 / 2 / 6 s | 31 s | 19.4% | 89 | Around midnight Nov 8–9 ET (yt-dlp) | Case-file Short, on the long side of the Shorts range. A long-form with a related CIA title also stalled (see §5). |

**High-retention miss:** "A Brown Recluse Hides in Your Shoes and Its Venom Can Kill Skin" (`YrPzxjXZJCY`), Nov 3, 12:03 PM ET: Metricool **48 views**, AVD **15 s** / 17 s (88.2%). Opening in the 90d file: "The spider in your shoe has venom that can kill skin." Watch time was fine; the feed did not extend it.

**Since Metricool's last published Short (public views only, no AVD):** strong — House Centipede vs Spider, 2,149. Weak and already stale enough to flag — "14 Dogs Tested: Your Dog's Guilty Look…" (`xIbnhX10r7k`, Nov 13, 1:03 PM, 20 s, **4** views); "How Mice Get in Your House Through a 1/4-Inch Gap" (`MEEPvBFpcQM`, Nov 15, 8:03 AM, 20 s, **11** views). Two Nov 16 Shorts (bathroom-wall bug, 12 views at 1:00 PM; "Daddy Longlegs Aren't the Most Venomous Spiders," 2 views at 4:00 PM) are too new to rank.

Posting hour, by itself, is not a clean lever: mid-morning through late afternoon medians on Metricool Shorts cluster around 1,000–1,200 views (yt-dlp ET hours). Sample sizes per hour are small.

---

## 5. YouTube long-form

11 videos in the Metricool window (Videos tab). **698 Metricool views** and **657.4 watch-minutes (10.96 hours)** total (`YTVP06`, `YTVP07`). Public titles are used where they have changed.

| Title (public) | Dur. | Metricool views / AVD / watch-min | Public views | Posted (ET) |
|---|---:|---|---:|---|
| 3 Bugs in Your House You Should Never Kill (And 4 You Must) (`cH3HCZ8GlHk`) | 4:33 | **208 / 74 s / 259.5** | 224 | Nov 7, 8:04 AM |
| How Wolves Became Dogs (`Uqj0QL8G0d4`) | 8:21 | 163 / 29 s / 81.0 | 165 | Oct 24, 9:31 AM |
| Weird Animal Facts You Didn't Know (`z-Kg8sXCxlU`) | 10:17 | 136 / 63 s / 143.8 | 135 | Oct 26, 1:01 PM |
| Animals Thought Extinct Found Alive (`o9Emu9oMgCs`) | 7:04 | 126 / 56 s / 119.2 | 127 | Oct 25, 1:04 PM |
| Everything You Know About Animals Is WRONG (`gFhrONKK0rI`) | 2:15 | 43 / 33 s / 24.2 | 45 | Oct 22, 9:32 AM |
| Every Bug in Your House, Ranked… (`bqij8Ht6SX4`; Metricool: "I Ranked Every Creature…") | 8:57 | 5 / 42 s* / 3.6 | 8 | Nov 1, 5:03 PM |
| The CIA Tried to Turn a Cat Into a Spy (`2EC5LDtbUbo`; Metricool: "Conspiracy Theories That Turned Out To Be TRUE") | 5:39 | 5 / 93 s* / 7.8 | 8 | Oct 27, 1:02 PM |
| 12 Animal Myths You've Believed Your Whole Life (`RwbgzQisvYM`) | 11:18 | 5 / 32 s* / 2.7 | 9 | Oct 23, 10:10 AM |
| The CIA Tried to Steal a Soviet Sub (`4-gvZTWf2wg`; Metricool: "Why the CIA Says…") | 8:38 | 3 / 178 s* / 8.9 | 4 | Nov 5, 5:04 PM |
| 3 More Bugs in Your House You Should Never Kill (`xeAsg5ECpgw`) | 4:36 | 2 / 157 s* / 5.2 | **93** | Nov 11, 5:04 PM |
| 6 Creatures Living In Your House Right Now (`Lid8JXhg1Q4`) | 6:33 | 2 / 43 s* / 1.4 | 6 | Oct 29, 4:04 PM |

\*AVD on 2–5 Metricool views is not a reliable retention signal.

**After the Metricool cutoff (public views only):**
- "Your Life as a House Cat: 8 Ways It Goes Wrong" (`viD-nbPdaxk`), Nov 13, 5:04 PM ET, 9:16, **53** views.
- "Don't Kill the Spider in Your Corner. It Eats Bigger Spiders" (`KWOM2-mNmww`), Nov 14, 8:03 AM ET, 8:17, **181** views — already near the previous best long-form's public count, in about two days, on a house-spider promise.

What differs: the only long-form with a real audience in Metricool is a house-bug "should you kill it?" list, not CIA/conspiracy and not a generic myth compilation. "3 More Bugs…" has since grown from 2 Metricool views to 93 public, which is encouraging but still small, and we have no updated AVD.

---

## 6. Five best and five worst TikTok posts

Public profile only. Metricool TikTok was empty. Ranked by public view count as of ~6:44 PM ET, Nov 16. Duration, likes, and ET time from the same yt-dlp dump.

**Best 5**

| # | Post | Views / likes / comments / shares | Len. | Posted (ET) | What differs |
|---|---|---|---:|---|---|
| 1 | why did the faa ground stop happen (`7707843829264665887`) | **17,600** / 289 / 5 / 6 | 66 s | Nov 13, 9:10 PM | Breaking search/news, timestamped "as of Fri Nov 13, 9 pm ET." |
| 2 | flights grounded today (`7707812310450031886`) | 9,356 / 185 / 3 / 15 | 74 s | Nov 13, 7:08 PM | Same FAA story, earlier that evening. Most shares in the 109. |
| 3 | house centipede part 2 (`7703357929851800862`) | 6,655 / 165 / 13 / 16 | 63 s | Nov 1, 7:03 PM | Best animal post. Sequel ("you just saw the 30-legged bug…"). |
| 4 | Would you pick one up? 👍/👎/🧤 Bombardier beetle (`7700968777902492958`) | 6,043 / 90 / 0 / 3 | 63 s | Oct 26, 8:32 AM | Direct yes/no prompt. Best of the ≤-noon posts. |
| 5 | house centipede facts (`7701402177754942751`) | 4,088 / 67 / 2 / 2 | 66 s | Oct 27, 12:34 PM | Same centipede run as #3. |

Next over the 1,000-view line: Jensen Huang allegations, 3,534 (Nov 13, 10:52 AM); Microsoft outage, 3,049 (Nov 13, 3:05 PM); house centipede "150 babies," 1,773 (Nov 7, 2:31 PM); GTA 6 release date and price, 1,460 (Nov 13, 2:07 PM). Five of the nine 1,000+ posts are Nov 13 news explainers, not animal posts.

**Worst 5**

| # | Post | Views / likes | Len. | Posted (ET) | What differs |
|---|---|---|---:|---|---|
| 1–3 | is daddy longlegs venom deadly?; worst spider in your house?; are dust mites in my bed? | **3** / 0–1 each | 64, 71, 61 s | Nov 16, **12:25, 12:28, 12:30 PM** | Same 11-minute batch as #5. Topics overlap winning YouTube Shorts, but these were dumped back-to-back. |
| 4 | cellar spider in the corner of your ceiling (`7708200672570658079`) | 4 / 0 | 88 s | Nov 14, 8:15 PM | Long for this account; 88 s, 4 views, two days old. |
| 5 | mites on your face? (`7708823992773201182`) | 6 / 0 | 61 s | Nov 16, 12:34 PM | Same batch (a sixth post, "what is eating my books?", 12:36 PM, has 22 views). |

Same-day contrast: "Kill a house centipede?" at **12:24:32 PM** ET, one minute before that batch, has **423** views. Batching, not the topic, is the obvious difference.

---

## 7. Threshold tracker

**TikTok 1,000-view gate (public totals, not For You vs Search), 9 of 109 posts, ~6:44 PM ET Nov 16:**

| Post | Total views | Over 1,000 total? | Rewards caveat |
|---|---:|---|---|
| why did the faa ground stop happen | 17,600 | Yes | May be Search-heavy. Search qualified views need 30+ s (research file). We cannot see FYP vs Search here. |
| flights grounded today | 9,356 | Yes | Same caveat. |
| house centipede part 2 | 6,655 | Yes | Animal sequel; still unknown FYP share. |
| Would you pick one up? (bombardier beetle) | 6,043 | Yes | same |
| house centipede facts | 4,088 | Yes | same |
| jensen huang allegations explained | 3,534 | Yes | News explainer; same FYP/Search gap. |
| microsoft outage explained | 3,049 | Yes | same |
| house centipede in bathroom: 150 babies | 1,773 | Yes | Animal; same gap. |
| gta 6 release date and price | 1,460 | Yes | News explainer; same gap. |
| Next below the line: Tarantula hawks… | 948 | No | — |
| Other 99 posts | 3–890 | No | At most, these have not met a *total*-view proxy of the 1,000-view gate. |

The research file states the account is already in Creator Rewards; this audit did not re-open the Rewards dashboard. The lever is still how many posts clear 1,000 **For You** views, which public totals can only approximate.

**YouTube watch hours**

| Figure | Value | What it is |
|---|---|---|
| Long-form watch time on the 11 Metricool-window long-forms | **657.4 minutes = 10.96 hours** | Metricool `YTVP07`, views through Nov 13. This is *period* watch time on those 11 videos, not trailing 12-month YPP hours. |
| Shorts watch time on the 71 Metricool-window Shorts | 8,438.4 minutes = 140.6 hours | Metricool `YTVP07`. Does not count toward YPP hours. |
| 12-month qualified hours | **Not visible** in Metricool or public pages | `growth-plan-longform-shorts-1115.md` earlier called Studio Earn "not visible (est. 10–25)." That estimate was not re-read from Studio today and is not used as a fact here. |
| Pace | ~11 long-form hours in ~30 days | At this rate, 4,000 hours is not reachable by Jan 31, 2027 without a long-form hit. The research file's deadline and 8,000-hour change on Feb 1, 2027 still stand. |
| Subscribers | 1,010 | The 1,000-sub YPP requirement is already met. Hours are the gap. |

---

## 8. Gaps to close next time

- Connect Metricool TikTok to `@meatballmyths` (it currently appears pointed at "fureverfaces") and re-pull `TKPO13–15` (full-video watched rate, total/average time watched) plus For You vs Search (`TKPO16`, `TKPO21`).
- Screenshot or export YouTube Studio: audience-retention graphs, viewed-vs-swiped, and the Earn-tab trailing 12-month qualified hours.
- Screenshot TikTok Rewards: qualified views and RPM, especially on the FAA/news posts.
- Metricool YouTube views lag 3 days (null after Nov 13 in this pull). Re-run after it catches up so the Nov 13–16 Shorts and the two new long-forms have AVD.

---

## 9. Five edit rules (exact seconds)

Rules 1–2 are tied to measured Metricool/yt-dlp numbers. Rules 3–5 are **hypotheses** built from those numbers plus title/opening lines. They are not from per-second retention curves.

1. **Land the first payoff before 0:07.** Median Shorts AVD is 7 s. If the myth, the "don't squish it," or the number has not landed by then, the average viewer is already gone. The strongest AVD in the top 5 (bed mites, 11 s on a 15 s video) names the mite and the 130°F rule in the opening line.

2. **Finish Shorts at 0:15–0:20, not 0:30+.** 16–20 s Shorts had a 1,139 median views and 43.8% AVD/length; 31–60 s Shorts had a 404.5 median and 21.6%. A 7 s average watch on a 35 s video is a much weaker completion signal than the same 7 s on a 16 s video.

3. **Hypothesis: first scene change and on-screen stake by 0:03.** We did not measure a 2-second swipe curve. What we do have: winning openings in the 90d file put the creature and the consequence in the first sentence, and the worst-performing lane is case-file/conspiracy (median 57.5 views, median AVD 4.5 s), not "bugs in your house." Do not wait until mid-video to say what is in the room.

4. **Hypothesis: show the creature clearly in the first frame (0:00–0:01), and stop shipping case-file / CIA / Roswell Shorts in the current form.** Those six conspiracy Shorts never left the dead batch. The brown recluse Short *did* hold viewers (15 s AVD on 17 s) and still stalled at 48 views — fix packaging and first-frame clarity on spider IDs, and do not read a high AVD as distribution.

5. **Hypothesis, long-form: give a reason to stay before 1:00, and a second hook before 1:14.** The only long-form with a usable AVD peaks at 74 s on a 4:33 house-bug episode. CIA long-forms are at 3–8 public views. The new Nov 14 spider episode ("Don't Kill the Spider in Your Corner," 8:17, 181 public views in ~2 days) is the one to copy in topic and promise, not the myth-compilation or conspiracy titles. We still need Studio retention graphs before tightening this further.

**TikTok, from public counts only (no AVD):** do not batch-publish (the Nov 16 12:25–12:36 PM ET dump is 3–6 views; the centipede post one minute earlier is 423). Animal sequels and a direct "would you pick it up?" prompt are the organic pattern that has cleared 1,000 total views. News explainers can spike much higher, but see the Rewards caveat in §7.
