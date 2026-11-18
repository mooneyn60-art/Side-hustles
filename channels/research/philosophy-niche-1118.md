# Philosophy niche research (written 2026-11-18, due Fri 11/20 noon)

Spec: TASKS.md "[MEATBALL] 11/18 2:50 PM ET" item 2. Every claim has a source and a date, or is labeled GUESS.

## 1. Answer first

**Verdict: HYBRID. Do not pivot. Keep the bug and pet lane as the base. Add one philosophy Short a week as a test lane, framed as a life question, not as a classic puzzle. Judge it after 3 Shorts.**

Why, in short:
1. **Search demand favors life-advice philosophy, not classic puzzles.** On YouTube search (Google Trends, US, 12 months to 2026-11-18), "ship of theseus" is about 4.5% of "stoicism" and "trolley problem" about 27%. "Plato's cave" is about 3.5%. (Section 3.)
2. **The big animated and faceless channels win with self-help framing.** Their top videos are "Carl Jung and the Most Important Rule of Life", "You're Trying Too Hard | Taoist Philosophy", "Why Democracy Rewards Idiots". None of the top three in any sampled channel is a classic thought experiment. (Section 4.)
3. **Pay is better, but unproven for us.** One study of 300 channels puts Education & Science at a $10.22 median RPM against $2.30 for all niches. Pets & Animals is not in that study. We are not in the Partner Program yet, so we have no RPM of our own. (Section 5.)
4. **Policy risk is real but manageable.** YouTube's page bars "templated" mass-produced content and allows "a unique character and narrative you invented". Meatball fits the allowed side if each video has its own angle and sources. A fixed philosophy template posted many times a day would not. (Section 7.)
5. **The gap is a funny, honest dog.** In the 11 channels I measured, I found none with a recurring comic animal narrator. That is a GUESS about the whole niche, not a count. (Section 6.)

What this changes in the queue (the work gate): the 3+3 volume stays. One of the six weekly slots goes to a philosophy Short, picked from the table in Section 3 and not from the Ship of Theseus. Rule in Section 9.

## 2. Method and limits

- **Search suggestions:** `postkit.py kw` on 20 seeds, 2026-11-18 (YouTube autocomplete).
- **Relative demand:** `postkit.py trends compare`, YouTube search, US, 12 months, run in 5 batches that each include "stoicism". Google Trends scales each batch to its own biggest term. I rescaled every term to **stoicism = 100 inside its own batch**. Batches are not exactly comparable, and the means move between batches. Treat the index as a rank, not a count.
- **Volumes:** vidIQ `keyword_research` (questions mode, seed "philosophy"), 2026-11-18. vidIQ credits are now 10 spent, balance 0 until 2026-11-24. The estimate field is vidIQ's model, not YouTube's.
- **Channels:** yt-dlp flat listing of each channel's Videos tab (newest first), 2026-11-18. Up to 40 videos. Subscribers are YouTube's public rounded count. View counts are rounded by YouTube and are lifetime views of videos of different ages, so the median is not age-adjusted. vidIQ `channel_search` (faceless, thought experiments) gave 3 small channels' numbers and its own earnings estimates.
- **RPM:** AIR Media-Tech's page, opened 2026-11-18. **Policy:** support.google.com pages, opened 2026-11-18.
- Not opened as pages: Fluxnote, Kineclip, FluxNote TikTok guide (search summaries only, labeled below).

## 3. Search demand: the top 20 philosophy questions

Google Trends, YouTube search, US, 12 months to 2026-11-18. Index: stoicism = 100 inside the same batch. "Last 4 wk" is the last 4 weeks mean over the 12-month mean, in the same batch (an up or down sign only).

| # | Question or term | Index vs stoicism | Trend | Noise warning |
|---|---|---|---|---|
| 1 | stoicism | 100 | flat | none |
| 2 | meaning of life | 32 | down (19.8 vs 23.2) | songs and a Monty Python film share the term |
| 3 | trolley problem | 27 | down (8.0 vs 14.5) | TV show and game searches (autocomplete: "show", "smosh", "try guys") |
| 4 | simulation theory | 16 | flat | a Muse album shares the term |
| 5 | nihilism | 15.8 | flat | band names in autocomplete |
| 6 | absurdism | 12 | up (10.8 vs 8.7) | piano and song names in autocomplete |
| 7 | descartes | 11 | flat | none |
| 8 | existentialism | 11 | flat | "existentialism on prom night" is a song |
| 9 | chinese room | 11 | down | game and decor searches |
| 10 | ship of theseus | 4.5 | up (4.8 vs 2.4); peak week 2026-10-11 | a TV show (WandaVision) is the top related search, not the paradox |
| 11 | determinism | 4.5 | flat | none |
| 12 | utilitarianism | 3.7 | flat | none |
| 13 | plato's cave | 3.5 | flat | none |
| 14 | experience machine | 1.3 | flat | none |
| 15 | pascal's wager | 0.6 | flat | a game is the top autocomplete |
| 16 | brain in a vat | 0 (too small to read) | n/a | game and podcast in autocomplete |
| 17 | zeno's paradox | 0 (too small to read) | n/a | none |
| 18 | free will | 120 | down | NOT USABLE. "free willy" movie dominates the term (autocomplete) |
| 19 | who am i | 529 | up | NOT USABLE. Songs ("casting crowns", "snoop dogg") dominate |
| 20 | consciousness | 187 | down | NOT USABLE. Broad term: meditation, psychology, physics |

Sources: `postkit.py trends compare` batches 2026-11-18 (stoicism anchor means 53.8, 71.7, 15.5, 37.9, 84.2 in the five batches). Autocomplete: `postkit.py kw`, 2026-11-18. Rows 18 to 20 are listed because the brief asked for 20; they should not be used to size demand.

Google web search (not YouTube), same date, stoicism = 100 inside its batch: "meaning of life" about 423, "nihilism" about 90, "trolley problem" about 23, "ship of theseus" about 16. So on web search "meaning of life" is the big question. On YouTube, stoicism is.

vidIQ volume estimates for philosophy question searches, 2026-11-18 (vidIQ's own model; use as order of size only):
- "what is philosophy": about 11,658 searches a month (competition 56).
- "who am i philosophy": about 9,394 a month, demand growth +94.8%.
- "why do i feel empty inside philosophy": about 5,625 a month.
- "why love never lasts forever philosophy": about 5,120 a month.
- "how smart people communicate with fools, schopenhauer's philosophy": about 21,837 a month, demand growth -44.5% (a title-style phrase, not a true question).
- Most other rows read "<750".
- Pattern: the volume sits in "life feelings plus philosophy" phrases, not in puzzle names. This matches Section 4.

**TikTok demand: NOT MEASURED.** TikTok shows hashtag counts only inside the app, and its public pages gave me nothing (`ttpage` takes video links only, and a direct hashtag page returned no counts). Only a marketing blog's claim (search summary, page not opened, no method): "#philosophy" over 10 billion views, "#stoicism" about 1.5 billion, "#shipoftheseus" no figure. GUESS-level. What would settle it: Nolan's TikTok Creator Search Insights screenshot, or vidIQ's TikTok tools after credits return 2026-11-24.

## 4. Competitors: the 10 animated or faceless philosophy channels

Sample: last up to 40 videos on each Videos tab, yt-dlp flat listing, 2026-11-18. Median is not age-adjusted. "Median % of subs" = median views divided by subscribers. Max over median is a breakout size.

| # | Channel | Style | Subs | Median views | Max views | Max / median | Median % of subs |
|---|---|---|---|---|---|---|---|
| 1 | exurb1a | animated, narrated, a person's voice | 2.99M | 2,150,000 | 9,400,000 | 4.4 | 71.9% |
| 2 | Pursuit of Wonder | animated, faceless | 3.52M | 329,500 | 2,700,000 | 8.2 | 9.4% |
| 3 | Einzelgänger | faceless | 2.39M | 114,500 | 302,000 | 2.6 | 4.8% |
| 4 | Academy of Ideas | animated, faceless | 2.03M | 83,500 | 809,000 | 9.7 | 4.1% |
| 5 | The School of Life | animated | 9.81M | 81,500 | 328,000 | 4.0 | 0.8% |
| 6 | Sprouts | animated (mixed topics) | 1.95M | 35,000 | 1,000,000 | 28.6 | 1.8% |
| 7 | Philosophy Coded | faceless | 179K | 11,000 | 2,000,000 | 181.8 | 6.2% |
| 8 | Wireless Philosophy | animated lectures | 373K | 4,050 | 118,000 | 29.1 | 1.1% |
| 9 | PhilosophyInsights | faceless | 450K | 2,900 | 317,000 | 109.3 | 0.6% |
| 10 | Tired Thinker | faceless, sleep-length | 61.6K | 1,700 | 9,000 | 5.3 | 2.8% |

Also measured, not philosophy-only: TED-Ed, 23M subs, median 419,000, max 4,700,000.

What the table says:
- **Small faceless channels live on a few breakouts.** Philosophy Coded has 179K subs and a median of 11,000, with one video at 2,000,000 (182 times its median). PhilosophyInsights has 450K subs and a median of 2,900. Typical videos there reach a small slice of the subs.
- **Top videos are life framing.** Philosophy Coded: "Why Democracy Rewards Idiots: Plato Saw It Coming 2,400 Years Ago" (2.0M). Academy of Ideas: "Carl Jung and The Most Important Rule of Life" (809K). Einzelgänger: "You're Trying Too Hard | Taoist Philosophy" (302K). Pursuit of Wonder: "The Existential Elk Theory" (1.4M), a darker essay. Sprouts' top video (1.0M) is about the menstrual cycle, not philosophy.
- **A small channel's own median is the right yardstick.** Our channel's YouTube Shorts median is about 1,100 views (MASTER_ORDERS, research 93, as of 2026-11-14). A philosophy Short that reaches 2,200 is 2 times our median.
- vidIQ `channel_search`, 2026-11-18, own earnings estimates (an estimate, not measured): Philosophy Coded about $4,197 a month, Tired Thinker about $419 a month, Philosophy Overdose about $1,447 a month. Philosophy Overdose is a lecture reupload channel and is not in the table.
- Other faceless "thought experiment" channels vidIQ found are mostly Shorts or Roblox-style: e.g. Postabar (111K subs, 38 Shorts, 78M views), TWO THINGS (18.9K subs, 121 Shorts), Zakyssal Shorts (31.7K subs, 16 videos, 24.8M views). Format is "what if" and not classic philosophy. I did not run their medians.
- Not measured: whether any of these use AI voices (I only know vidIQ's "faceless" flag).

## 5. RPM: education and philosophy against animals

- **Education & Science median RPM $10.22; middle half $2.31 to $19.50.** Source: AIR Media-Tech, "YouTube RPM by niche 2026", last updated 2026-07-01. Method: 300 real YouTube Studio dashboards, 3,595 channel-months, May 2025 to May 2026, medians. Quote: "Education & Science pays the most, at a $10.22 median RPM." https://air.io/en/air-data-findings/which-youtube-niche-makes-the-most-money-in-2026-ranked-by-real-rpm-and-cpm
- **All-niche median RPM about $2.30 per 1,000 views.** Same study. Quote: "the median RPM came out to about $2.30 per 1,000 views". https://air.io/en/air-data-findings/how-much-does-youtube-really-pay-in-2026-real-rpm-data-from-300-channels
- **Pets & Animals: not in that study.** The study ranks 13 niches and none is Pets & Animals. I could not find a measured, opened source for animals. Search summaries (Fluxnote about $4 to $8, Kineclip about $4 to $9) came from pages I did not open and are marked GUESS. One source I opened (OutlierKit, published 2026-08-19) lists only CPM, no pets row, and says it links no outside source for its figures.
- **Philosophy is not its own row.** "Education & Science" is the closest. A philosophy channel could land anywhere in the $2.31 to $19.50 range.
- **Our RPM: none.** The channel has 1,000 subs but under 4,000 long-form hours (MASTER_ORDERS "Where we are", 2026-11-12), so it is not paid yet. Shorts RPM is lower than long-form RPM (GUESS, no source opened).
- **Reading:** education pays more per view in the only measured source. But a higher RPM on near-zero views is still near zero. The 4,000 hours matter first.

## 6. The gap a cartoon dog narrator could own

Measured fact first, then GUESS.

- The faceless and animated philosophy channels I sampled lean serious (Section 4). Even the lighter ones (School of Life, Sprouts) use a calm human voice.
- GUESS: nobody in this sample runs a recurring comic animal character who argues a side. Meatball's 11/18 "It's NOT the same ship" take (3:05 PM note) is that gap in one line: a funny, confident dog with a hard side, kind to people and rude to ideas.
- GUESS: the "kind roast" format (Studio's rule: roast the idea, never people) gives comment fights without insults.
- GUESS, to test: philosophy told as "what Meatball's dog life teaches about X" (stoicism for a dog who loses his ball) beats a plain puzzle explainer, because the winners in Section 4 are life-advice framed.
- Our own proof point: our pet and house videos already use this voice (MASTER_ORDERS, "Make them funnier").
- Source accuracy: every philosophy claim still needs a university or Stanford Encyclopedia source (TASKS.md rule). The cell-turnover hook needs a peer-reviewed or university source or it gets cut.

## 7. Risk: YouTube's inauthentic and repetitive content policy

Official text, opened 2026-11-18: "YouTube channel monetization policies - YouTube Help", https://support.google.com/youtube/answer/1311392 (the page shows a most recent update of July 15, 2025).

- **Renamed:** "to better clarify this includes content that is repetitive or mass-produced." (the policy changed from "repetitious content" to "inauthentic content").
- **Core rule:** "Not be mass-produced, generic, repetitive, or manipulative."
- **Not allowed to monetize:** "Similar or repetitive content with low educational value, commentary, narratives, or minimal variation across videos" and "AI-generated content made with generic or unoriginal templates giving the impression of mass production".
- **Allowed:** "Same intro and outro for your videos, but the bulk of your content is different"; "each video has a distinct storyline, focus, or concept"; "using AI to visualize a unique character and narrative you invented".
- **AI label:** YouTube's disclosure page (https://support.google.com/youtube/answer/14328491, opened 2026-11-18, no date on page): creators "don't need to disclose non-realistic content that's made with AI". A cartoon dog is non-realistic. Using AI for a script or outline is listed as minor. This fits the standing YouTube rule that synthetic stays off (MASTER_ORDERS, 11/18).
- **Enforcement evidence (secondary, discounted):** AIR Media-Tech's 2026 timeline (https://air.io/en/monetization/youtube-monetization-policy-changes-2026-a-complete-dated-timeline) says a January 2026 sweep "removed 16 channels under the inauthentic content policy" (its FAQ), about 35 million subs and 4.7 billion lifetime views (the article's estimate, not YouTube's). A blog claim of 18,000 channels in one month conflicts with this and I did not use it. I found no primary YouTube announcement of numbers.
- **Risk rating (my reading, GUESS on the odds): medium-low if each philosophy video has its own angle, its own sources, and Meatball's own commentary. High if we post several near-identical videos a day.** The risk is not special to philosophy. Our bug videos face the same page. The risk goes up with a philosophy series run on one fixed template.
- Mitigations that match the allowed list: distinct concept per video, named sources on screen, Meatball's own take, no slideshow or scrolling text, no near-duplicate scripts.
- Not measured: whether any of the 10 channels above lost monetization (not visible from outside).

## 8. Options (for Studio and Nolan)

| Option | What it is | Evidence for | Evidence against |
|---|---|---|---|
| A. Pivot | Move most output to philosophy | Higher measured RPM for education; big winners exist | Our median is about 1,100 Shorts views and the small channels' medians are 1,700 to 11,000 with a few breakouts; classic puzzles have low demand; one test video has no result yet |
| B. Hybrid (recommended) | Bugs and pets stay. One philosophy Short a week, life-question framed | Cheap, same pipeline, fits the policy page, uses our funny-dog gap | Takes one slot of six |
| C. Stay | No philosophy | Zero risk to a tested lane | Skips the only RPM lead we have; bug median is "stuck" per Nolan 11/12 |

## 9. Rule and next steps (ends in a queue change)

1. **Queue:** one weekly philosophy Short, slot picked by Studio. Topics from the demand table, in this order: stoicism angles ("what a dog knows about stoicism"), meaning of life, simulation theory, nihilism or absurdism. Skip Plato's cave, brain in a vat, Pascal's wager and Zeno for now (index under 4).
2. **Gate:** after 3 philosophy Shorts, compare each against our same-age Shorts median (about 1,100). Two of three at 2 times or better: keep weekly and consider a second a week. Fewer: drop it and say so.
3. **Format guard:** each Short carries a source and its own claim; no templated copy; Meatball argues one side; no insults at viewers (Studio's 3:05 PM rule).
4. **Long-form:** no philosophy long-form until a Short passes 2 times. (Sleep-length philosophy, like Tired Thinker's 3-hour videos, is a possible watch-hour route, but that style does not fit a cartoon dog. GUESS.)

## 10. Could not measure

- TikTok demand and hashtag counts (no public access; vidIQ credits at 0 until 2026-11-24).
- True search counts. Trends are relative; vidIQ volumes are estimates. Terms with other meanings (free will, who am i, consciousness, trolley problem, meaning of life) are noisy.
- Age-adjusted medians for competitors. Subs and views are rounded.
- Whether competitor channels use AI voices, or are monetized.
- Pets & Animals RPM from a measured source. Philosophy as its own RPM row. Our own RPM.
- The result of the 11/18 Ship of Theseus test.
- Shorts-only medians for animated philosophy channels (only the Videos tab was sampled).
- Policy odds. No primary YouTube enforcement count.

## 11. Sources and dates (all opened 2026-11-18 unless noted)

- Google Trends via `postkit.py trends compare` and `related`, YouTube and web search, US, 12 months.
- YouTube autocomplete via `postkit.py kw` (20 seeds).
- vidIQ `keyword_research` (questions, seed "philosophy") and `channel_search` (faceless, thought experiments).
- yt-dlp flat listings of channel Videos tabs (the 11 channels above).
- AIR Media-Tech RPM study (updated 2026-07-01) and policy timeline.
- YouTube Help: https://support.google.com/youtube/answer/1311392 and https://support.google.com/youtube/answer/14328491
- OutlierKit RPM benchmarks (published 2026-08-19; CPM only, no outside source).
- MASTER_ORDERS (our Shorts median, our hours).
