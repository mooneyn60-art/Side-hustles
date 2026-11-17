# Viral deep dive: TikTok "House centipede part 2" (7703357929851800862)

Data role (Trends & Analytics). Written Tue 11/17/2026, about 8:00–9:00 AM ET, for Social Studio. Follows `channels/team/playbooks/data.md` (55000aa): real numbers only, each with its source and n, and every claim labeled.

- **OFFICIAL** means TikTok Studio, YouTube Studio or Metricool (platform data).
- **NON-OFFICIAL** means public counts from yt-dlp, the TikTok public page or vidIQ.
- **OUR ANALYSIS** means our own math or reading of the data. **GUESS** marks a cause we can't prove.

Nothing was posted, messaged or bought. Part 4 is Claude's (TASKS 4afee0d), so this file contains no Part 4 script.

## 0. The post and its numbers

| Item | Value | Label / source |
|---|---|---|
| Posted | Sun 11/1/2026, 7:03 PM ET, 63.43 s, original sound, drawn | NON-OFFICIAL: yt-dlp and ffprobe on the public video, pulled 11/17 ~8:00 AM ET |
| Studio, updated 11/16 | **71.1K views**, 2,246 likes, 99 comments, 220 shares, 302 saves, 28h50m total play time, 18.8 s average watch, 4.18% watched the full video, 3 new followers, $0.20 in rewards | OFFICIAL: Moondog88's TikTok Studio screenshot |
| Rates from the Studio numbers | Likes 3.16%, comments 0.14%, shares 0.31%, saves 0.42%, follows 0.004% of views. Average watch is 18.8 ÷ 63.43 = **29.6%** of the length. Rewards come to about **$0.003 per 1,000 views** | OUR ANALYSIS |
| Account like-rate median | 1.98% (n=109 public posts) | OUR ANALYSIS of `viral-centipede-1117-tt109.csv` |
| **Hit multiple** | 71.1K ÷ the TikTok median of 233 (n=109, `baseline-1116.md` §2) = **305x**. The 5x hit line is about 1,165 views | OUR ANALYSIS. OFFICIAL views divided by a NON-OFFICIAL median |

**Growth timeline: Part 2 was already a hit before it went viral.**

| When (ET) | Plays | Multiple of median | Source |
|---|---:|---:|---|
| 11/12, ~4:47 PM (day 11) | 2,793 (89 likes) | 12.2x (median 229, n=82) | NON-OFFICIAL: `97-tiktok-own-posts.csv` (skills repo) |
| 11/16, ~6:44 PM (day 15) | 6,655 (165 likes, 13 comments, 16 shares) | 28.6x (233, n=109) | NON-OFFICIAL: `baseline-1116.md` §6 |
| 11/16, time not shown | **71,100** | 305x | OFFICIAL: Studio screenshot |
| 11/17, 7:40 AM | 93,900 (3,059 likes, 112 comments, 271 shares, 420 saves) | 403x | NON-OFFICIAL: `channels/claude/status.md` (0eae9d4, ttpage) |

OUR ANALYSIS of the timeline:
- Part 2 grew slowly for 15 days, at roughly 1K plays a day between 11/12 and 11/16.
- It then gained about 64K between the 6:44 PM public read on 11/16 and the Studio screenshot, and about 23K more overnight.
- The 5x rule would have flagged it on day 11.
- What set off the jump is **no data**: we have no traffic-source split for this post.
  - GUESS: two new centipede TikToks went up just before the surge, "house centipede in your bathroom" (11/15, 8:15 PM, 314 views) and "Kill a house centipede?" (11/16, 12:24 PM, 419 views). They may have re-signaled the topic.

**Data warning (OUR ANALYSIS):** 28h50m is 103,800 s. Divided by 18.8 s, that is about 5,521 plays, not 71.1K. So the play time, average watch and full-watch figures on the screenshot most likely lag the view count and describe roughly the first 5.5K viewers, not the viral wave. Watch behavior during the surge is **no data**.

## 1. What Part 2 has that our other posts don't

### 1a. TikTok top 10 and bottom 10

Source: NON-OFFICIAL yt-dlp grid of 109 posts, 11/16 PM ET (`/workspace/deep1116/tt.json`, extract committed as `viral-centipede-1117-tt109.csv`).
- Same 109 posts and same 233 median as `baseline-1116.md`. Per-post counts differ a little from baseline §6; for example, Part 2 is 6,333 here and 6,655 there.
- The style and topic column comes from `97-tiktok-own-posts.csv` (11/12). Posts after 11/12 have no label in that file.
- "x median" is OUR ANALYSIS.

**Top 10**

| # | Caption opener (search phrase first) | Public views | x median (233) | Like rate | Length | Posted (ET) | Sequel? | Style / topic |
|---|---|---:|---:|---:|---:|---|---|---|
| 1 | why did the faa ground stop happen (`7707843829264665887`) | 17,600 | 75.5x | 1.6% | 66 s | Fri 11/13 9:10 PM | no | news (no label) |
| 2 | flights grounded today (`7707812310450031886`) | 9,356 | 40.2x | 2.0% | 74 s | Fri 11/13 7:08 PM | no | news (no label) |
| **3** | **house centipede part 2: you just saw the 30-legged bug in your bathroom** (`7703357929851800862`) | **6,333** | **27.2x** | **2.4%** | 63 s | Sun 11/1 7:03 PM | **yes** | drawn 60–90 s cut / house creature |
| 4 | Would you pick one up? Bombardier beetle (`7700968777902492958`) | 6,043 | 25.9x | 1.5% | 63 s | Mon 10/26 9:32 AM | no | real photo / quiz / other animal |
| 5 | house centipede facts: 30 legs, lives 7 years (`7701402177754942751`) | 4,084 | 17.5x | 1.6% | 66 s | Tue 10/27 1:34 PM | no (it is "Part 1") | drawn 60–90 s cut / house creature |
| 6 | jensen huang allegations explained (`7707684445859384607`) | 3,533 | 15.2x | 1.2% | 87 s | Fri 11/13 10:52 AM | no | news |
| 7 | microsoft outage explained (`7707749755279002911`) | 3,049 | 13.1x | 1.4% | 71 s | Fri 11/13 3:05 PM | no | news |
| 8 | house centipede in bathroom: one female can make up to 150 babies (`7705514437402316062`) | 1,770 | 7.6x | 0.5% | 64 s | Sat 11/7 2:31 PM | no | drawn 60–90 s cut / house creature |
| 9 | gta 6 release date and price (`7707734724675898654`) | 1,459 | 6.3x | 0.7% | 85 s | Fri 11/13 2:07 PM | no | news |
| 10 | Tarantula hawks are wasps that paralyze tarantulas (`7700602376926842143`) | 948 | 4.1x | 0.7% | 62 s | Sun 10/25 9:50 AM | no | real photo / quiz / other animal |

**Bottom 10** (fair-age only: posted before 11/14 12 PM ET, so at least ~2 days old; n=95, median 263). The 11/16 batch of 3–6-view posts is left out as too young; baseline §6 covers it.

| # | Caption opener | Public views | x median | Like rate | Length | Posted (ET) | Sequel? | Style / topic |
|---|---|---:|---:|---:|---:|---|---|---|
| 1 | the lizard on my ceiling can't blink (`7707703103268687135`) | 26 | 0.1x | 0.0% | 64 s | Fri 11/13 12:04 PM | no | no label |
| 2 | Would you crew that ship? Case #8: CIA (`7701076793129717023`) | 86 | 0.4x | 1.2% | 64 s | Mon 10/26 4:31 PM | no | real photo / case file |
| 3 | what to do if you see a grizzly bear (`7707829612465769758`) | 93 | 0.4x | 4.3% | 92 s | Fri 11/13 8:15 PM | no | no label |
| 4 | why do cats purr (`7707849105136946445`) | 102 | 0.4x | 5.9% | 86 s | Fri 11/13 9:31 PM | no | no label |
| 5 | jensen huang part 2 (`7707766536479509790`) | 112 | 0.5x | 0.9% | 68 s | Fri 11/13 4:10 PM | **yes** | news |
| 6 | the possum in my yard dropped dead… then got up (`7702121787953368350`) | 123 | 0.5x | 1.6% | 73 s | Thu 10/29 12:06 PM | no | drawn / other animal |
| 7 | Real giant or fake? Case #14 (`7701024264769539358`) | 125 | 0.5x | 2.4% | 63 s | Mon 10/26 1:07 PM | no | real photo / case file |
| 8 | Would you still go outside? Spider… (`7701154162704157982`) | 129 | 0.6x | 1.6% | 68 s | Mon 10/26 9:31 PM | no | real photo / quiz |
| 9 | What do you think happened? Case… (`7701169467488816415`) | 132 | 0.6x | 0.8% | 61 s | Mon 10/26 10:30 PM | no | real photo / case file |
| 10 | can cats taste sugar (`7707811165333638430`) | 132 | 0.6x | 4.5% | 84 s | Fri 11/13 7:03 PM | no | no label |

### 1b. YouTube Shorts top 10 and bottom 10

Source: Metricool views (NON-OFFICIAL export of platform data, read about 11/14) in `channels/research/2026-11-16-shorts-90d.csv`.
- Fair-age set: Meatball Shorts posted by 11/11, n=76, median **1,018.5**. That matches the 90d context median in `playbook-1116/analytics.md`.
- The Studio 28d median is 1,007.5 (n=86, OFFICIAL, `playbook-1116/analytics.md`).
- Openers come from `96-openings-our-shorts.csv`.

| # | Short | Views | x median | Length | Avg % viewed | Topic | Opener (first sentence) |
|---|---|---:|---:|---:|---:|---|---|
| 1 | Are Daddy Longlegs the Most Venomous Spiders? (`Us0zIbxiR-A`) | 2,390 (Studio 2,445) | 2.3x | 19.9 s | 93.4 | spider | "Daddy long legs are the most venomous spiders." |
| 2 | Your Roach Has 40 Babies (`1hdMaSxJtkU`) | 1,985 | 1.9x | 19.8 s | 75.2 | house bug | "Meatball, your roach is carrying 40 babies." |
| 3 | Your Bed Mites Die at 130°F (`wHCrmIPdCgg`) | 1,974 | 1.9x | 15.2 s | 145.8 | house bug | "Wash your sheets under 130 degrees, and the mites in your bed live." |
| 4 | 100 Feet a Night to Your Bed (`heI2W3z1hk4`) | 1,855 | 1.8x | 15.6 s | 89.3 | house bug | "Something can crawl 100 feet tonight just to reach your bed." |
| 5 | 3 'Mommy Longlegs' in Your Home (`bm6LzV7eRwg`) | 1,823 | 1.8x | 15.5 s | 103.4 | spider | "You asked for mommy long legs." |
| 6 | 40x Jumps From Your Window (`1RJw2Pex_Ro`) | 1,777 | 1.7x | 16.4 s | 76.9 | spider (house-bug series) | "The spider on your window can jump 40 times its own length." |
| 7 | The Bug You Squish Is Protecting You, house centipede (`EPimwC5VMgo`) | 1,664 (Studio 2,316) | 1.6x | 16 s (Studio) | 118.5 (Studio 109.59) | house bug | no data in openings file |
| 8 | Millions of Mites Can Live in Your Mattress (`s_L3sGikMWU`) | 1,647 | 1.6x | 22.9 s | 103.0 | house bug | "There are tiny monsters in your bed eating your skin…" |
| 9 | A Cockroach Can Live for Weeks Without Its Head (`FTKRLEoa-nU`) | 1,377 | 1.4x | 15.5 s | 75.2 | house bug | "A cockroach can live for weeks with no head." |
| 10 | 30K Roaches in Your Kitchen (`FeVJWESbIO8`) | 1,356 | 1.3x | 15.1 s | 83.0 | house bug | "One roach in your kitchen can turn into 30,000 in a year." |
| B10 | The Hunchback Cricket in Your Basement (`vn-MTvvQsbg`) | 47 | 0.05x | 32.1 s | 35 | house bug | no data |
| B9 | He ran from the wedding… Oh Meatball Pt 3 (`A4KoX68UbS4`) | 35 | 0.03x | no data | no data | old soap format | no data |
| B8 | She was already married… Oh Meatball Pt 2 (`jmu0F61CQWg`) | 33 | 0.03x | no data | no data | old soap format | no data |
| B7 | Several Colonies Eating Your House (`-O-_YBst4R8`) | 30 | 0.03x | 25.7 s | 52 | house bug | no data |
| B6 | What REALLY Crashed at Roswell? (`gxi2NH2uuVk`) | 27 | 0.03x | 27 s | 40.6 | case files | no data |
| B5 | He found out he has a secret brother… (`Rf5rfCRHE5Q`) | 18 | 0.02x | no data | no data | old soap format | no data |
| B4 | He crashed the wedding, Oh Meatball Pt 1 (`L5pOwnR3ieE`) | 14 | 0.01x | no data | no data | old soap format | no data |
| B3 | The US Planned to Nuke the Moon (`88gaODWt4qY`) | 11 | 0.01x | 25 s | 69.6 | case files | no data |
| B2 | He crashed the wedding, Oh Meatball Pt 1 (`iAKwF9YyCpc`) | 6 | 0.01x | no data | no data | old soap format | no data |
| B1 | Operation Northwoods: The Conspiracy That Was TRUE (`C7KaAarFUag`) | 2 | 0.00x | 23 s | 42.1 | case files | no data |

**Part 2's YouTube twin.** "Never Squish the 30-Legged Bug in Your House" (`Iqww6xgMvig`, 11/2/2026 4:02 PM ET):
- It opens with the same line: "You just saw the 30-legged bug in your bathroom."
- It is a 14 s cut (`yt-house-centipede-2-v2.mp4`, versus TikTok's `tt-house-centipede-2-v2.mp4`).
- It got **1,326** views (1.3x median), 91.6% average viewed, 12 likes, 0 comments and 0.535 engaged share (CSV, Metricool and Windsor).
- Its title does not contain "house centipede."

### 1c. What is different about Part 2

| Factor | Part 2 | Rest of our posts | Label |
|---|---|---|---|
| **Topic** | House centipede | Centipede TikToks: n=9, median **503**, three of them over 1,000 (6,333; 4,084; 1,770). Account median is 233. All three drawn house-creature posts in the top 10 are centipedes. No other bug or spider TikTok reached 1,000. Best others: mouse 936, ants 752, silverfish 615, cockroach 510. On YouTube, centipede does well but not uniquely: `EPimwC5VMgo` 2,316 (Studio) and `L6xt-kze48M` 2,149 public | OUR ANALYSIS of the tt109 CSV and the Shorts CSV. Creatures matched by keyword in titles, so the counts are rough |
| **First 3 s, spoken** | 0.0–2.1 s "You just saw the 30-legged bug in your bathroom." 2.1–3.2 s "Don't squish it." 3.2–4.1 s "It's hunting." | Other TikTok openers are search questions ("do wolf spiders bite?", 139 views), news ("As of Nov 13…") or quizzes ("Would you…?", n=12, median 202.5). Part 2 is **second person, present tense, a callback to an encounter the viewer just had, plus an order** (don't squish). It is the only one of our top 10 that does this | Transcript is OUR ANALYSIS: speech-to-text of the public video, 11/17. Other openers are NON-OFFICIAL captions. The "Would you" median is OUR ANALYSIS (n=12) |
| **Caption** | Search phrase first ("house centipede part 2"), a stay/squish vote, three sources named (CAES, Penn State, WSU), #thingslivinginyourhouse. TikTok showed search words on the post ("house centipede bites" and others) | Most of our captions also lead with a search phrase. In the tracker, "search phrase first" n=17 had a median of 316 | NON-OFFICIAL: `tiktok-stats.csv` 11/12 and `tracker-1116.md`. That search drove the views is a GUESS (traffic sources: no data) |
| **Length** | 63.43 s | Not a difference. Over 60 s median is 221 (n=91); 60 s or under is 359.5 (n=18). Most of the top 10 also run 62–87 s | NON-OFFICIAL `baseline-1116.md` §2 |
| **Sequel framing** | Caption says "part 2", and the voiceover opens with "You just saw…" as if Part 1 just played. Part 1 ("house centipede facts", 4,084) was already a 17.5x post | Our other sequels flopped: Part 3 got 215 and Jensen Part 2 got 112 (n=3 sequels in total). A "part 2" label is not enough on its own; what seems to matter is the sequel to a **post that was already a hit**, opening on the encounter | OUR ANALYSIS (n=3, small sample) |
| **Set and visuals** | Stick-figure Meatball with the giant drawn centipede **in frame from 0:00**. Night bathroom (tile, moon window, drain), then basement at about 3 s, then kitchen at about 19 s. One-word white captions. Large image changes at 19 points in 63 s, about one every 3.3 s | Bottom 10 is mostly real-photo quiz/case files or unlabeled news. "Kill or keep" topics on Shorts also win (House bug median 1,138.5, n=30) | Frame read and frame-difference count are OUR ANALYSIS of the public video. Topic median is OFFICIAL (Studio, `playbook-1116/analytics.md`) |
| **Engagement** | Likes 3.16% (Studio) against an account median of 1.98%. 302 saves. 99 comments | Bottom 10 like rates run 0–5.9% on tiny view counts | OFFICIAL / OUR ANALYSIS |
| **Slot** | Sun 7:03 PM, 4 posts that day | 7 PM median 222 without Part 2 (n=5) | NON-OFFICIAL `tiktok-plan-1117.md` §4a. Slot is not the cause |

**Bottom line (OUR ANALYSIS):** the hit comes from the topic (house centipede), plus the callback-and-order opener, plus the creature in frame at 0:00, a drawn house set and a kill-or-keep vote. It sits on a series whose Part 1 was already working. Length, slot and the word "part" do not explain it.

## 2. Why the same content does worse on YouTube Shorts

| # | Reason | Our numbers | Evidence or GUESS |
|---|---|---|---|
| 1 | **Our Shorts have a hard ceiling around 2.5K.** None has ever reached 5x the median | Best Short is 2,445 (Studio). 8 of 86 reached 1,500. 0 of 86 reached 5,038 (5x of 1,007.5). The same opener got 1,326 on YouTube (1.3x) against 71.1K on TikTok (305x); the TikTok version has 53.6x the views of the YouTube twin | **Evidence** (OFFICIAL Studio 28d, n=86, plus the Metricool CSV). Why YouTube caps us is a GUESS |
| 2 | **It isn't the same video.** The YouTube twin is a 14 s cut of the hook. The TikTok version adds 60 s of stakes, the "Will it sting you?" beat and a teaser for the next bug | Lengths: 14.0 s against 63.43 s. Our 15–18 s rule exists because 30 s+ Shorts have a median of 411 (n=11) against 1,159 (n=21) | **Evidence** for the lengths and the length medians. That the extra content drove TikTok is a GUESS |
| 3 | **TikTok re-surfaced an old post; YouTube Shorts barely do** | TikTok Part 2 went from 2,793 (day 11) to 6,655 (day 15) to 71.1K. "Centipede facts" went from 3,869 to 4,084. On YouTube: daddy longlegs 2,390 (Metricool) to 2,474 (public); `EPimwC5VMgo` 1,664 to 2,302 | **Evidence** of late growth on both, much bigger on TikTok. The mechanism is a GUESS |
| 4 | **Search packaging.** The TikTok caption leads with "house centipede", and TikTok attached centipede search words to the post. The YouTube twin's title ("Never Squish the 30-Legged Bug…") doesn't say "house centipede" | Studio's 48 h slice on our best Short: 43 views from YouTube search against 10 from the Shorts feed (n=55, `playbook-1116/analytics.md`) | **Evidence** for the titles and for search mattering on YouTube. Search's share of Part 2's views is **no data**, so the effect is a GUESS |
| 5 | **Comment trigger.** The TikTok caption asks for a stay/squish vote | TikTok: 99 comments (Studio). YouTube twin: 0 comments (CSV) | **Evidence** for the counts. That the comments drove distribution is a GUESS |
| 6 | **No returning audience on YouTube** | 99.3% new viewers, 0.0% regular. 46.3% stayed and 53.7% swiped (Studio 28d) | **Evidence** for the numbers. It hurts both platforms (TikTok Part 2 earned only 3 follows), so it explains little of the gap. GUESS |

## 3. Repeatable formula: 5 rules and the next 10 topics

**Rules** (OUR ANALYSIS from §1–2; each rule cites its evidence):
1. **Open on the encounter, then an order.** Use "You just saw the [plain description] in your [room]. Don't [kill/squish] it." by 3 s, with the creature drawn in frame at 0:00. This is Part 2's opener; it also appeared on the 1.3x YouTube twin.
2. **Kill-or-keep stakes plus a vote.** Put a two-option vote in the caption (stay/squish) and the search phrase first ("[creature] part 2"). Name the sources in the caption. This copies Part 2's caption; house bugs are our best Shorts lane (median 1,138.5, n=30).
3. **Make sequels to hits only.** Build a Part 2 only for a post already at 5x or more (Part 1 was 17.5x). Open it as a callback, and deliver what the teaser promised. Part 2 ended "Next, the bug that's older than dinosaurs", but Part 3 was the centipede at 3 AM (215 views), so the promise was never kept.
4. **Two lengths from one script.**
   - TikTok: 61–65 s, for Creator Rewards. Answer the scary question ("Will it sting you?") and open the next loop before **18 s**, since the average watch is 18.8 s.
   - YouTube: a 15–18 s cut with "house centipede"-style search words in the title.
5. **Same look, one post per slot.** Keep the stick-figure Meatball, the drawn rooms (bathroom, then basement, then kitchen), one-word captions and a new image about every 3 s. Never batch posts: the 11/16 batch got 3–6 views each, against 419 for the post one minute earlier.

**Next 10 topics** (house bugs and spiders only, same format; centipede Parts 4–5 left to Claude). Ranking is OUR ANALYSIS. Every fact must pass Research & QA before use.

| Rank | Topic, with the sequel hook | Why it ranks here (source) |
|---|---|---|
| 1 | **Silverfish: "the bug that's older than dinosaurs"** (pays off Part 2's own teaser, and house centipedes eat silverfish) | Part 2's last line promises it, and 4.18% heard it (OFFICIAL completion rate). vidIQ outlier: "If You See Silverfish in Your Bathroom, Don't Kill It Yet", 2.7x (`/workspace/trends/outliers-1117.md`, NON-OFFICIAL). Fact source: [Missouri Dept. of Conservation](https://mdc.mo.gov/discover-nature/field-guide/silverfish-firebrat), "Their fossils date to 400 million years ago — about twice as long ago as the dinosaurs", and "Silverfish are eaten by house centipedes". Our silverfish TikToks: n=2, median 316.5 (one was in the batch) |
| 2 | **"What happens to the spider you throw outside?"** | vidIQ cluster: 3 channels in 30 days at 12x, 11x (2.4M views) and 9.6x (outliers file, NON-OFFICIAL). Spider is our second-best Shorts topic: median 1,104.5, n=12 (OFFICIAL) |
| 3 | **Daddy longlegs / cellar spider: "don't kill the one in your corner"** | Our #1 Short ever, 2,445 (OFFICIAL Studio), and "Mommy Longlegs" at 1,823. The TikTok versions (3–4 views) were batch or 88 s posts, so they weren't a fair test (baseline §6) |
| 4 | **The corner spider that eats bigger spiders** ("it will defend you") | vidIQ "Spider Will Defend", 15M, >100x (NON-OFFICIAL). The long-form `KWOM2-mNmww` reached 181 views in about 2 days, our best long-form pace (baseline §5, NON-OFFICIAL) |
| 5 | **Cockroach: "your roach has 40 babies" / "lives weeks without its head"** | Shorts at 1,985, 1,377 and 1,356 (CSV). TikTok n=5, median 419 (OUR ANALYSIS) |
| 6 | **Bed bugs: "crawls 100 feet a night to your bed"** | Short at 1,855; bed-bug Shorts n=2, median 1,507.5 (CSV). TikTok n=4, median 324 |
| 7 | **Bed/dust mites: "die at 130°F"** | Short at 1,974 with 145.8% viewed (CSV). TikTok n=5, median 263 |
| 8 | **Jumping spider on your window: "40x its length"** | Short at 1,777 (CSV). TikTok n=1, 300 |
| 9 | **Black widow: "the worst spider in your house?"** (keep the safety line conditional) | Shorts n=2, median 1,051 (CSV). TikTok n=3, median 210. Weaker |
| 10 | **Brown recluse in your shoe** | Held 15 s of 17 s (88.2%) but got only 48 views (baseline §4). Retention is proven; distribution isn't. Lowest confidence |

## 4. Where watch-through drops on Part 2

**There is no retention curve.**
- No per-second curve for this post exists anywhere in the repo.
- Metricool's TikTok link points at the wrong account (fureverfaces).
- Claude can't see TikTok watch time (`channels/claude/handbook.md`).

What the two OFFICIAL figures imply (OUR ANALYSIS, and remember they probably cover only about the first 5.5K viewers; see §0):
- Average watch is 18.8 s of 63.43 s, or **29.6%**. Full watches are **4.18%**.
- Full watchers add 0.0418 × 63.43 = **2.65 s** to the average.
- So everyone else averaged at most (18.8 − 2.65) ÷ 0.9582 = **16.9 s**. That assumes average watch doesn't count replays; if it does, the real figure is lower.
- About **96% leave before the end**, and the end-card teaser at 60.7 s reaches about 1 in 24 viewers.

The script around those points (timings are speech-to-text, OUR ANALYSIS; the causes are GUESSES):
- **16.5–19.5 s:** "Will it sting you? Almost never. Only if you grab it hard." This answers the viewer's main fear right where the average viewer is gone.
- **28.5–30.4 s:** "So the one you just saw, it's working for you." It sounds like an ending, at the halfway point.
- **30–60 s:** a list of facts (legs, molting, lifespan, hiding spots) with no new question.

**To close the gap:** we need the per-second retention graph for this post from TikTok Studio. That is a Moondog88 screenshot; Data can't pull it. With that graph we can replace these guesses with actual drop timestamps.

## 5. Hit rule for the 11 AM scoreboard (schedule.md, a0baf74)

Flag a post when it reaches 5x our median, on the same platform and format:
- TikTok: **1,165+** public views (5 × 233, n=109).
- YouTube Shorts: **5,038+** (5 × 1,007.5, n=86, Studio 28d).
- Long-form: no stable median in the repo yet. The baseline has n=11 Metricool long-forms, most with 2–5 views. Data will set one once Studio long-form views are pulled.

In the 11/16 TikTok grid, 9 of 109 posts were at 5x or more (OUR ANALYSIS). No Short has ever qualified.

## Appendix: Part 2 voiceover (speech-to-text, OUR ANALYSIS; spellings are not checked)

0.0 You just saw the 30-legged bug in your bathroom. / 2.1 Don't squish it. / 3.2 It's hunting. / 4.1 It eats bed bugs and baby cockroaches, silverfish, / 7.3 spiders, flies; squish it, and they all stay. / 10.5 It has 15 pairs of legs, and it uses them to chase. / 13.8 It stings its prey with legs that turn into fangs. / 16.5 Will it sting you? / 17.5 Almost never. / 18.5 Only if you grab it hard. / 19.5 It even eats moths and carpet beetle larvae. / 22.0 It would rather run. / 23.1 It's one of the fastest things in your house. / 25.0 And it hunts at night while you sleep. / 26.8 Most people never even see theirs. / 28.5 So the one you just saw, / 29.6 it's working for you. / 30.4 Its long feelers look just like its legs, / 32.5 so a predator can't tell which end is the face. / 35.4 A baby hatches with only four pairs of legs. / 37.9 It grows more every time it molts, / 40.1 until it has 15 pairs. / 41.8 It takes about three years to grow up, / 44.0 and it can live up to seven. / 45.1 And the female's back legs are almost twice / 47.4 as long as her body. / 48.6 They hide by day in basements, / 50.1 cellars, and bathrooms. / 51.4 Bug experts say don't bother spraying it. / 53.6 Dry out the damp spots, and the bugs it eats move out. / 56.7 Fewer bugs, fewer centipedes. / 59.0 [unclear] …stay, follow me. / 60.7 Next, the bug that's older than dinosaurs.
