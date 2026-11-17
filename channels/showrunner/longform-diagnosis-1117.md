# Long-form diagnosis and relaunch EP1 format (for topic-pitches-1117.md)

Draft: Mon Nov 16, 2026, about 9:50 PM ET. Box only; nothing posted, scheduled or changed. It's a proposal until Moondog88 sees it.

## Sources (every number below cites one of these)
- **[Studio CSV]** `/workspace/yt-studio/csv1/Table data.csv`
  - A YouTube Studio Content export, lifetime (2018-05-24 to 2026-11-15), saved on the box Nov 15, 5:52 PM ET.
  - Columns: impressions, impressions CTR, views, average view duration (AVD), duration.
  - The vidIQ pass had no Studio access, but this earlier export does.
- **[vidIQ 11/16]** tonight's partial browser pass. Public view counts are as shown 11/16. Screenshots are in `/workspace/showrunner/vidiq-1117/`.
- **[Metricool]** the user-Metricool connector, brand 8135499, YouTube "videos published in range", pulled 11/16 about 9:40 PM ET.
  - It has views, watch minutes and AVD, but no impressions or CTR fields (checked with getAnalyticsAvailableMetrics).
- **[Pace file]** `/workspace/research/2026-11-16-shorts-ceiling-and-longform-pace.md` §3 (Windsor % viewed to 11/10; channel CTR on record).
- **[Thumb spec]** `/workspace/side-hustles/channels/packaging/thumbnail-spec-two-styles-1115.md`
- **[Thumbs 11/16]** the four public thumbnails, fetched from i.ytimg.com on 11/16 about 9:40 PM ET and saved as `vidiq-1117/our4_thumbs.jpg`.
- **[Breakout]** `/workspace/research/breakout-tactics-1116.md`

"% viewed (calc)" = Studio AVD ÷ duration. That's my arithmetic, not a Studio field.

## 1. The four newest long-forms

| Video | Length | Published | Impressions [Studio CSV] | CTR [Studio CSV] | Views [Studio CSV] / [vidIQ 11/16] | AVD [Studio CSV] | % viewed (calc) | AVD [Metricool] |
|---|---|---|---|---|---|---|---|---|
| 3 Bugs in Your House You Should Never Kill (And 4 You Must) | 4:34 | Nov 7 | 1,856 | **5.44%** | 214 / 225 | 1:57 | **42.7%** (Windsor 42.84% to 11/10 [Pace file]) | 74 s |
| Don't Kill the Spider in Your Corner. It Eats Bigger Spiders | 8:17 | Nov 14 | 1,771 | 4.63% | 114 / 183 | 1:50 | 22.1% | 106 s |
| 3 More Bugs in Your House You Should Never Kill (And 5 You Must) | 4:37 | Nov 11 | 1,510 | 4.37% | 88 / 93 | 1:05 | 23.5% | 65 s |
| Your Life as a House Cat: 8 Ways It Goes Wrong | 9:17 | Nov 13 | 1,439 | **1.95%** | 42 / 53 | 2:14 | 24.1% | 131 s |

The Studio and Metricool AVDs disagree for 3 Bugs (1:57 vs 74 s). Metricool's YouTube data has run behind before ([Pace file] treats Metricool as "as of roughly 11/14"), so Studio is used for the diagnosis.

For context, the earlier long-forms have the same impressions-and-CTR columns [Studio CSV]:
- Weird Animal Facts: **5,262** impressions, 1.82% CTR (11.0% viewed, Windsor [Pace file])
- Animals Thought Extinct: 3,438 impressions, 2.53%
- How Wolves Became Dogs: 1,558 impressions, 1.99%
- Everything You Know About Animals Is WRONG: 2.93%
- 12 Animal Myths: 1.25%
- Every Bug Ranked: 1.31%
- the two CIA videos: 0.67% and 0.87%

### Per-video call (only where the data supports it)
- **3 Bugs (Never Kill):** the problem is **impressions (reach).**
  - It has the channel's best CTR (5.44%) and best % viewed (42.7%) [Studio CSV].
  - But YouTube showed it only 1,856 times in 8 days (Nov 7 to the Nov 15 export).
  - Packaging, retention and topic all work. YouTube just hasn't widened distribution yet.
- **Spider in Your Corner:** CTR is fine (4.63%) [Studio CSV].
  - % viewed is 22.1% at 8:17, about half the 4:34 original's share, though its AVD in seconds is close (1:50 vs 1:57).
  - Possibly **retention past ~2 minutes**. But it was about 1 day old at export, so that's **unknown, needs current Studio impressions/CTR and a retention curve.**
- **3 More Bugs (sequel):** CTR held (4.37%) [Studio CSV].
  - AVD fell from 1:57 to **1:05** at almost the same length (4:37 vs 4:34), so 23.5% vs 42.7% viewed.
  - The problem is **retention.** The sequel's packaging worked; the video didn't hold.
  - Why (pacing, a repeated format, a weaker first item) is **unknown, needs a Studio retention curve.**
- **House Cat (born-as):** the problem is **CTR (packaging), and possibly the topic.**
  - At 1.95% it's the lowest of the four [Studio CSV], in the same band as the older general-animal lists (1.25–2.93%).
  - Its AVD is the highest in seconds (2:14), so the people who click do watch.
  - [Thumbs 11/16]: the cat is a flat, low-detail shape, and the art is weaker than the bug thumbnails.
  - Packaging vs. topic can't be separated without a title/thumbnail test.

### What the four say together
- **The main bottleneck is reach, not clicks.** Each video got only 1,439–1,856 impressions [Studio CSV]. Three of the four clear 4% CTR, which is well above the channel's 2.50% (Studio, 28 days to 11/11, [Pace file]).
  - At that impression level even a 5.44% CTR gives roughly 100–200 views.
  - Why YouTube isn't widening distribution (traffic source mix, viewers' first-30-second drop) is **unknown, needs Studio traffic sources and retention per video.**
- **Topic signal:** the bug "never kill" family (CTR 4.37–5.44%) beats every general-animal or born-as long-form (1.25–2.93%) [Studio CSV].
- **Retention signal:** only the original 4:34 video held over 40% [Studio CSV]. The two longer videos and the sequel sit at 22–24%.
- **Weird-topic reach:** "Weird Animal Facts" got the most impressions of any long-form (5,262) but failed on CTR (1.82%) and on retention (11.0% viewed) [Studio CSV; Pace file].
  - It's also the keyword with Low competition and a 65 overall score [vidIQ 11/16] (see §3).
  - So the weird-facts topic can earn reach; that video's packaging and pacing lost it.

## 2. Against tonight's vidIQ outliers (a weak match)

The outliers [vidIQ 11/16]:
- Dog TV Daycare "24 Hour Dog TV…": 1.1K subs, 57K views, >100x
- Kane Ranks "chihuhua secrets": 1.1K subs, 113K views, >100x, 33 VPH
- Sweet Days "The Funniest Cat Memes…": 12K subs, 102K views, 35x
- Relaxing Dog Cartoon TV "24 Hour Dog Cartoon…Vermont": 1.3K subs, 2.8K views, 34x
- Boon & Moon "24 Hours Dog Cartoon for Puppy Home Alone…": 1.4K subs, 15K views, 20x

The dog screenshot also shows Cali and Maui's "Meeting Wolves for the First Time!" (7.7K subs, 140K views, 16x). No lengths or URLs were shown.

| Dimension | Outliers (what the screenshots show) | Our four |
|---|---|---|
| Length | Not shown. "24 Hour" titles say ambient loops; meme comps are unknown | 4:34–9:17 [Studio CSV] |
| Title | A format label plus the pet ("24 Hour Dog TV", "Funniest Cat Memes"), with no question and no fact | A verdict or list promise ("Should Never Kill (And 4 You Must)") |
| Thumbnail | Bright, saturated, full-bleed scenes with big expressive animal faces filling the frame. Cat memes use real photos with caption boxes | Dark navy backgrounds, 2–3 yellow/red words, Meatball small in a corner, a creature at half the frame [Thumbs 11/16] |
| Series | Most are recurring formats ("recurring" label; "24 Hour" variants) | Two of four are a series (3 Bugs + sequel); the rest are one-offs |

**What it does and doesn't suggest:**
- **It doesn't** show that animated explainers break out. The set is ambient TV for dogs to watch and meme compilations. Their audience, watch behavior (looped background play) and search intent differ from ours. The multipliers (">100x") are vidIQ's views-vs-channel-average label, not CTR or retention.
- **It weakly suggests:**
  - Recurring, instantly named formats get repeat distribution even on channels with about 1K subscribers.
  - Bright, full-frame, single-face pet thumbnails are the visual norm where pets win in this search.
  - Both match what our own data already says: the series format got the best CTR.
- **Don't copy:** 24-hour loops (off-brand, and outside our story format and the sourced-facts rule) or real-photo meme compilations (the style lock says fully drawn).

## 3. Keywords [vidIQ 11/16]

| Keyword | Volume | Competition | Overall |
|---|---|---|---|
| animated pet facts | <750 | 33.8 | 26 (Low) |
| animal facts | 416,697 | High | 66 |
| weird animal facts | 37,554 | Low | 65 |

- Don't build a title on "animated pet facts" (tiny volume).
- "Weird animal facts" pairs real volume with low competition. Fold it into the description and tags, and a chapter title, not the main title (the main title follows §4).

## 4. Recommended format: relaunch long-form EP1

1. **Topic and series:** House Guests #1, the bug or spider "should you kill it" family. It's the only long-form family on the channel above 4% CTR [Studio CSV].
   - Use the week-2 slate's EP 5 (`/workspace/showrunner/slate-wk2.md`), one bug per episode.
   - Number it (#1) in the description, playlist and a thumbnail corner tag.
   - Watch: MASTER_ORDERS' 11/11 "no new bug videos" order still needs Moondog88's go (slate-wk2 flag 2).
2. **Length: about 8 minutes (8–9).** Watch-hour math needs length, and AVD in seconds didn't fall at 8:17 (1:50 vs 1:57) [Studio CSV].
   - But % viewed halves at 8–9 minutes, so the first 2 minutes have to be the strongest part.
   - It's a single arc with a peak every 20–30 s, not a list (MASTER_ORDERS long-form checklist). The data doesn't show that length itself is the problem.
3. **Title:** keep the "never kill" verdict promise. It's the proven clicker [Studio CSV: 5.44% / 4.63% / 4.37%].
   - The week-2 searched-question title ("Is the Spider in My Bathtub Dangerous? Inside Noodle's Nose") is untested on long-form.
   - Run YouTube's Test & Compare with up to 3 titles, which picks by watch-time share ([Breakout]; YouTube Help 13861714):
     - A: the searched-question pattern
     - B: a "Don't Kill the Spider in Your Bathtub…" verdict title
     - C: Social Studio's "Inside Noodle's Nose: The Spider in Your Bathroom"
4. **Thumbnail:** [Thumb spec] "PLAY DEAD?" question style, or full-bleed.
   - One huge subject at ≥50% of the frame, 2–3 words, one red word, and a frame-0 match.
   - From the outliers (weak evidence): brighter, saturated backgrounds instead of our dark navy, with the face filling the frame.
   - Test it against the current dark style in the same Test & Compare.
5. **Comedy-first house rule:** in a long-form, MASTER_ORDERS bars jokes, intros and comment asks before 0:25.
   - **FLAG for Social Studio:** this conflicts with the new house rule Social Studio relayed (a joke every 5-7 s; no cursing in the first 7 s). One of the two needs to win for 0:00-0:25. Until Social Studio rules, this file follows MASTER_ORDERS.
   - From 0:25: a Meatball gag right after each sourced fact, and a character beat every 30–40 s (Noodle ends up with the shoe; Sauce in the sink).
   - Every fact line is said clean with its condition, and the verdict card keeps its condition (slate-wk2 bible).
6. **Fix the sequel lesson:** a sequel needs new facts in its first 2 minutes, not the same list shape. The sequel's 1:05 AVD vs the original's 1:57 [Studio CSV] is the only evidence for this.

## 5. Missing data, and how to get it
- **Current impressions, CTR, AVD and average % viewed per video since 11/15.** The CSV is from Nov 15, 5:52 PM ET, so the spider video was about 1 day old. Moondog88 can export Studio, Analytics, Advanced mode, Content (lifetime and last 28 days), or screenshot each video's Reach and Engagement tabs. Metricool can't supply impressions or CTR (no such fields).
- **Traffic sources per video** (Browse, Suggested, Search, Shorts feed). These are needed to explain the low impressions. Get them from Studio Reach, "Traffic source types", per video. (The Metricool YouTube traffic-source rows came back empty before, per the deep-growth research file.)
- **Retention curves**, to find where the sequel and the 8–9 minute videos lose people. Get them from Studio Engagement, "Key moments for audience retention". vidIQ's long-form read is due 11/24 per MASTER_ORDERS.
- **The YPP card's official 12-month public watch hours,** from Studio, Earn.
- **Outlier lengths, URLs and upload cadence:** re-run vidIQ with the tabs stable, or open each channel page.
- **The full upload list:** the vidIQ list may be incomplete. The Studio CSV lists every video, including 2019–2020 gaming uploads from the channel's earlier life.
