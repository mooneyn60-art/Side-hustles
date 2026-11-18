> OWNER: MEATBALL CLAUDE ONLY (@MeatballMyths). Etsy Claude: ignore this file.

# Why our long-form dies: the outlier autopsy

Written Wed 11/18/2026 for Social Studio. Brief: the [MEATBALL] note "HEAVY RESEARCH: WHY OUR LONG-FORM DIES" in TASKS.md (11/17 5:35 PM). Nothing was posted, scheduled or changed. No YouTube watch page was opened from this machine.

**Source labels.** [YT-DLP] public flat listing, read 11/18 (views are rounded two digits above 1,000). [VIDIQ] vidIQ MCP tool, read 11/18 (a vendor tool; its search numbers are estimates). [OFFICIAL] YouTube Help or YouTube staff on Creator Insider, read 11/18. [STUDIO] our own Studio numbers as recorded in `playbook-1116/analytics.md` (through 11/14). [TRENDS] Google Trends through `postkit.py trends`, 12 months, YouTube search, US. [KW] YouTube autocomplete and top-result lists through `postkit.py kw`. [OUR MATH] arithmetic on the above.

---

## 1. The answer (read this part)

1. **The outliers are not "long videos". They are one typed question about one bug, answered in 3.5 to 4.5 minutes.** Zyka (10,700 subscribers) has 6 of 28 long-forms above 500K views. All 6 run 3:26 to 4:31, and all are "What happens if you [do something] to a spider or wasp?" [YT-DLP]
2. **Our gap is impressions and views, not click-through.** Our bug long-forms clear 4% CTR (4.37% to 5.44%) but got only 1,510 to 1,856 impressions. Our 13 long-forms have a median of 60 public views. Zyka's weakest 15 of 28 have a median of 3,400. Zyka's floor is above our best video (229). [STUDIO, YT-DLP]
3. **Copying the topic does not copy the result.** For "what happens to a cockroach after you flush it" there are 6 videos in the top results: 703K, 95.7K, 1.2K, 319, 93 and 71 views. For the cockroach "trap and forget" topic the top copies sit at 1,899 and below. Only a minority of copies break out, so every plan below has a stop rule. [KW]
4. **The outliers hold viewers by re-hooking about every 30 to 60 seconds** (a new sub-question or a stake line), and they end by calling back the opening line. Nine of our 13 long-forms were viewed under 25% on average. [OUR MATH on transcripts; STUDIO]
5. **The shape split matters for tonight's flagship.** One ranked list got 636K (Benny Goes Wild), but only 4.3 times its channel's median. The single-bug question videos got 100 to 3,300 times their channels' medians. The flagship "House Bugs Ranked" is the list shape. Judge it against Benny, not against Zyka. (Our own best long-form, 229 views, was also a list, so the data does not say lists are worse here. It says lists have the weaker evidence.)
6. **Plan:** 10 videos after the flagship. 8 are search-led question videos (4 to 5 minutes), one is a sequel slot, one is an 8 to 10 minute "born as" test for watch hours. Titles are in section 6.

**Heads up on resources.** This run spent 85 of the 100 vidIQ add-on credits (balance 15, `renewableCredits` 0, renewal date 11/24 14:30 UTC). The 11/24 retention order in MASTER_ORDERS now has little left to spend until then.

---

## 2. Outlier teardown

### 2a. How I picked them

Rule: faceless or cartoon animal or bug long-form, 500K+ views, published inside the last 2 years, found with vidIQ `outliers` (keywords "why it sucks to be born as animal" and "what happens if bug spider cockroach ant in your house animated", min 500,000 views) plus yt-dlp listings of those channels. Multiple = the video's views divided by that channel's median long-form views (from the channel's /videos listing, videos of 60 s or more). The median includes the outliers themselves, so the multiple is a floor. For Stone the median rests on 3 videos (n=3), so read its 17x as weak. [VIDIQ, YT-DLP]

**Date note.** The Dinzo anaconda video was published 2024-11-05, 13 days outside the 2-year window. I kept it because I have its transcript. Dinzo's wild horse video (2024-11-27, 5.48M) is inside the window and is in the second table.

### 2b. The 10 with transcripts

Views are public counts from 11/18 [YT-DLP] and vidIQ's metadata [VIDIQ] (they agree within rounding). Transcripts are vidIQ's caption pulls. Re-hook = a spoken question, open promise or stake line that pushes to the next beat. I counted them by hand from the transcript, so read each as plus or minus 1.

| # | Title | Channel (subs) | Length | Published | Views | x channel median |
|---|---|---|---|---|---|---|
| 1 | What Really Happens to a Spider After You Throw It Outside? | Zyka (10.7K) | 3:26 | 2026-10-27 | 2.48M | 291x (median 8,500, n=28) |
| 2 | What Happens If You Trap a Spider and Forget About It? | Zyka | 3:46 | 2026-10-19 | 2.32M | 272x |
| 3 | What Happens When a Wasp Comes Home but Its Nest Is Gone? | Zyka | 3:51 | 2026-09-26 | 1.49M | 176x |
| 4 | Why It Sucks to be Born as a House Centipede | Stone (23.5K) | 8:04 | 2025-01-04 | 1.48M | 17x (n=3, weak) |
| 5 | Why It Sucks To Be Born As a Hummingbird | Zoozle (35.6K) | 9:40 | 2026-04-21 | 2.61M | 41x (median 63,000, n=49) |
| 6 | Why it Sucks To Be Born As a Termite | Bound (337K) | 12:00 | 2026-03-03 | 929K | vidIQ breakout 8.8x (listing blocked, see 7) |
| 7 | Why It Sucks to Be Born as a Giant Anaconda | Dinzo (475K) | 8:04 | 2024-11-05 | 7.49M | vidIQ breakout 1.9x (Dinzo's median is itself 1.6M) |
| 8 | What Happens to a Cockroach After You Flush It? | Nexus Explainer (1.2K) | 3:39 | 2026-10-29 | 704K | 3,273x (median 215, n=19) |
| 9 | Never Kill the Stink Bug on Your Window: Here's What Happens Next | Sixandsixty (1.25K) | 7:58 | 2026-08-08 | 700K | 2,397x (median 292, n=56) |
| 10 | What Happens If You Block a Tarantula's Burrow? | Bodo (35.7K) | 7:05 | 2026-11-07 | 1.2M | 59x (median 20,500, n=12) |

vidIQ marks #8, #9 and #10 as AI-labeled. Bodo was one week old when read, Nexus two weeks.

### 2c. Opening, re-hooks, chapters, thumbnail, how it was found

| # | First 30 seconds, in short | Re-hooks | Chapters | Thumbnail | How it was found (inference) |
|---|---|---|---|---|---|
| 1 | You toss a spider outside and feel good. "Real trouble begins, and not because of the fall." A named source (Haldane, 1926) at 0:15. "The problem is where it landed" at 0:30. | About 5 in 206 s (one per 41 s). Ends on a callback: "It was already home." | None in the description | Stick figure tossing a spider out a window, one word "WAIT!", bright flat colors | Search plus suggested. Title is the typed question. |
| 2 | You trap a spider under a glass and forget it. The question names three outcomes (starve, no air, waiting). "Let's start with food" at 0:16, a named study (Anderson, 1974) by 0:20. | About 8 in 226 s (one per 28 s): food, water, air, escape, male, "if you remember it". One-line answer at the end. | None | Stick figure walking away from a spider under a glass, "FORGOTTEN?" | Same |
| 3 | A nest is knocked down, one wasp hovers in empty air. The question, then "it flies home to a picture" at 0:15. | About 4 in 231 s (one per 58 s) | None | Stick figure with a broom and a falling nest, no text | Same |
| 4 | Second person, born in a dark basement. A sibling "will eat you" at 0:33. No title question, no spoken promise. | 6 life-stage jumps in 484 s (one per 80 s), plus about 14 jokes or similes (my count) | None seen | White background, a huge centipede, handwritten "Lives like sh*t" with an arrow | Suggested and browse. The "born as" shape. |
| 5 | "Your heart is already running at 1,200 beats a minute." A number in the first sentence. An egg that was "never going to hatch" by 0:15. | About 15 beats in 580 s (one per 39 s), "Skip forward" 4 times. Ends with "Next video" and a teaser. | None. The description lists "Next: Why It Sucks To Be Born As a Fire Ant". | White background, an icy blue bird, "It Dies EVERY NIGHT" with an arrow | Suggested and browse |
| 6 | "You hatch from an egg as a nymph." At 0:31 a stuck sibling is pulled apart. No joke. | About 22 beats in 720 s (one per 33 s), with a one-line stakes sentence after big beats ("only takes one spore to poison everything") | None seen | White background, a swollen ant, "Can't Move Will Burst" | Suggested and browse |
| 7 | "You slip into life..." and a joke inside 10 seconds. | About 10 beats in 484 s (one per 48 s) | None | Green snake mouth open, "Lives like sh*t" | Suggested and browse |
| 8 | Bathroom at night, you flush a cockroach. "Is it really gone?" At 0:16 a teaser: "for one kind of cockroach, you gave it a free ride home." | About 8 in 219 s (one per 27 s): "Can it drown?", "How long?", "which roach?", "can it come back up?", "what to do instead" | Not read | Stick figure at a toilet, "DON'T FLUSH!" in red | Search. Title is the typed question. |
| 9 | Window scene, then "Stop. Put the vacuum down." At 0:31 an explicit promise of what you will know by the end. | About 8 in 478 s (one per 60 s). Long lecture-style sentences. Ends with a comment prompt and "the next video is already waiting". | Not read | A realistic stink bug on white, "Don't Crush It!" | Search plus browse |
| 10 | A rock over a burrow hole. The question names three outcomes. At 0:15 the counter-claim: "that hole already has a door". | About 9 in 425 s (one per 47 s). Ends: "You didn't trap her. You just locked up for her." | Not read | Stick figure pushing a rock onto a burrow, "BAD IDEA?" | Search |

Notes on the table:
- **Chapters.** I read the descriptions of 7 of these 10 plus 3 more "born as" videos. None has timestamps. Only the Zyka descriptions restate the question in the first line and add a long boilerplate tag list. So "chapter structure" in these videos is spoken, not listed.
- **How found.** I cannot see anyone else's traffic sources. The "search" labels are inferred from titles that are the typed query, plus vidIQ's search-demand estimates in section 4. "Suggested and browse" is inferred from titles that are not typed queries. Treat both as inference.
- **Thumbnails** came from the public image of each video (i.ytimg.com), not from a watch page.

### 2d. The other 8 (no transcript pulled, vidIQ credits)

| Title | Channel (subs) | Length | Views | x median |
|---|---|---|---|---|
| What Happens to a Spider After You Vacuum It Up? | Zyka | 4:00 | 849K | 100x |
| What Happens If You Seal a Wasp Nest in Your Wall? | Zyka | 3:33 | 714K | 84x |
| Does the Spider in Your Room Know You Exist? | Zyka | 4:31 | 592K | 70x |
| Why It sucks to be Born as a Narwhal | giblixy (118K) | 9:50 | 2.63M | 43x |
| Why It Sucks To Be Born As a Jaglion | Sketching the Wild (38.4K) | 12:18 | 1.60M | 71x |
| What Happens If a Housefly Lands on Your Food for Just One Second? | Curio (1.6K) | 4:02 | 604K | 549x |
| What Happens When a Wasp Returns Home and Its Nest Is Gone? | Titly (11.7K) | 20:15 | 668K | 108x |
| From the Most Harmless House Spider to the One That Can Bite Through Your Shoe | Benny Goes Wild (7.6K) | 11:32 | 636K | 4.3x |

All from [YT-DLP] and [VIDIQ] 11/18. Together with 2b that is 18 videos above 500K views in the last 2 years (one just outside the window). Also seen: Dinzo "Why It Sucks to Be Born as a Wild Horse" (9:33, 2024-11-27, 5.48M) and Bound "Why it Sucks To Be Born As a Greenland Shark" (10:04, 1.9M).

### 2e. What the teardown says

- **Two lanes, both faceless and drawn.**
  - Lane Q (Zyka and its imitators): the title is a typed "what happens if you [do X] to [bug]" question. 3:26 to 4:31 (7:05 to 7:58 for Bodo and Sixandsixty). Narrated to "you". Real named sources (Burke Museum, Haldane 1926, Anderson 1974, Punzo, Prentice). Ends with a one-line answer, a "what to do instead", and a callback to the opening.
  - Lane B ("Why it sucks to be born as"): 8 to 12 minutes, first-person arc, a beat every 33 to 80 s, jokes, the creature as the hero. The channels are 23K to 475K subscribers.
- **Zyka's own record is the best proof of the odds.** 28 long-forms since the first upload on 5/7/2026: 6 above 500K (21%), 7 between 10K and 500K, 15 under 10K (the 15 weakest: 387 to 8,700, median 3,400). All 6 winners are about a spider or a wasp and about something a person does to it (throw, trap, vacuum, seal). The under-10K ones are mostly flies, bees, "why" biology and listicles. The 6 winners ran 3:26 to 4:31 and the 15 weakest median 4:09, so length did not separate them; the topic did. [YT-DLP, OUR MATH]
- **Fast follow-up.** All 6 of Zyka's winners were posted between 9/26 and 11/5, about 6 weeks (wasp 9/26, vacuum 10/17, trap 10/19, wasp nest 10/22, throw-outside 10/27, "know you exist" 11/5). The 11/5 follow-up on the spider topic came 9 days after the 2.4M one and drew 592K. Stone posted 3 videos and stopped. [VIDIQ dates, YT-DLP, `faceless-outliers-1117.md`]
- **Imitation wave.** Titly's wasp copy (9/30, 20:15, 668K) and Nexus's flush video (10/29, 704K) came after Zyka's. Others copied word for word and got 269 views (NEXEAT, `faceless-outliers-1117.md`). So the format travels. Exact titles do not.
- **Thumbnails.** Lane Q: a stick figure doing the action to the bug, 1 to 2 words in caps, often with "?" or "!" (WAIT!, FORGOTTEN?, DON'T FLUSH!, BAD IDEA?). Lane B: white background, one detailed animal, a handwritten phrase with an arrow ("It Dies EVERY NIGHT", "Lives like sh*t"). Our stick-figure Meatball already matches Lane Q. The thumbnail is not where we lose.

---

## 3. What YouTube itself says

All read 11/18 unless noted. Quotes are exact.

**Impressions and click-through rate (Help 7628154).**
- "Half of all channels and videos on YouTube have an impressions CTR that can range between 2% and 10%." [OFFICIAL]
- Videos with fewer than 100 views "can see an even wider range", and "it's also common for videos with fewer impressions and views to have higher click-through-rates and average view duration." [OFFICIAL]
- "YouTube's systems rank each video against all the other videos a viewer might watch." [OFFICIAL]
- Our reading: our 4.37% to 5.44% CTR on bug long-forms is already inside the normal range. We have too few impressions, not too low a CTR.

**CTR falls as a video breaks out.** Rene Ritchie: "click-through rate and average view duration will go down as the views go up." Todd Beaupre: "the more impressions something gets, the broader the audience is reached." (Creator Insider, 9/1/2026, about 11:05, captions.) Do not panic when CTR falls after a spike. [OFFICIAL]

**How a new long-form gets its first impressions.**
- It is not tested on subscribers only. Beaupre: "even in the first hour um videos are reaching people who've never watched the channel before." Ritchie: "it's not only your subscribers who will see it." (about 4:21 and 0:00) [OFFICIAL]
- A new channel has no history with any viewer. Beaupre: "there are zero viewers who have that channel in their history"; the system uses "other signals that we have about the fit between that content and that viewer." (about 31:38 to 31:55) [OFFICIAL]
- Help 141805 (Home): "Videos watched by similar viewers and new videos are also shown." It gives no number of first impressions and no early-hours window. [OFFICIAL]
- Our reading: YouTube publishes no first-impressions number. What we can control is the fit between the video and a viewer's interest: the title and thumbnail have to say the topic plainly.

**Suggested.**
- Help 141805: "Suggested Videos are ranked to offer your audience videos they're most likely to watch next."
- Beaupre: "the reason that a video can appear next to another video is not simply just because it's related" and "many viewers watch hundreds of channels and they're not all related." (about 29:22 and 31:08) [OFFICIAL]
- Our reading: Suggested is mostly a result of one video holding viewers, not something we can set up by linking our own Shorts to it. `youtube-deep-dive-1117.md` and MASTER_ORDERS agree: Shorts feed very few viewers into long videos.

**Intro retention.**
- Studio's Intro metric "tells you what percentage of your audience still watched your video after the first 30 seconds" (Help 9314415). It can also show how your video compares "to all YouTube videos of similar length". [OFFICIAL]
- Help 16559650: "The initial seconds of your content are when viewers decide to stay or move on, especially for Shorts and long-form videos." And "Your title and thumbnail are vital for communicating value, sparking intrigue, and setting clear expectations." [OFFICIAL]
- Our reading: our intro is fine. "3 Bugs" had 70% still watching at 0:30 [STUDIO]. The loss comes after the intro.

**Clickbait.** "Clickbait videos tend to have low average view duration." (Help 7628154) [OFFICIAL]

**Not found in official pages.** No official CTR target for small channels, no number for how many impressions a new long-form gets, no statement that channels under 1,000 subscribers are treated differently on Home. I ran one web search for Creator Insider and Creator Academy material; it returned only third-party summaries, which I did not use as facts. I did not search Creator Academy separately. Related official material (the 8,000-hour rule, view counting, A/B test rules) is already in `youtube-deep-dive-1117.md`.

---

## 4. Search demand: the top 15 house-bug questions

### 4a. What I measured, and the catch

- **[VIDIQ] `keyword_research`, mode "questions"**, 11/18: seeds "spider in your house", "cockroach", "house centipede", "silverfish". "estimatedMonthlySearch" is vidIQ's own estimate, and "competition" is its 0 to 100 score (lower is easier). Rows under 750 show as "<750".
- **[KW] YouTube autocomplete** (`postkit.py kw`) shows what people really type. It gives order, not volume.
- **[KW] `kw --search`** lists the top results for a query, so I can see who already ranks and how big they are.
- **[TRENDS]** relative interest on YouTube search, US, 12 months. Each Trends call rescales to its biggest term, so I chained them by a shared anchor ("kill spider" = 65.5).

**The catch.** Several vidIQ "questions" are word-for-word titles of videos that already exist (the Zyka family). Their estimates may partly reflect those titles. Autocomplete confirms some of the long phrases and not others, so the table has a column for it. "Not confirmed" means the phrase did not appear in autocomplete when I tried it, not that nobody types it.

### 4b. The ranking

Ranked by vidIQ's monthly estimate. Where one topic has several phrasings I kept the biggest and counted the topic once.

| Rank | Question (as typed) | vidIQ est. searches a month | vidIQ competition | Autocomplete | Who already ranks (top results, views) |
|---|---|---|---|---|---|
| 1 | what happens to a cockroach after you flush it | 46,960 (the "down the toilet" version +80.3% growth) | 18 | Not confirmed for roach. "what happens if you flush a spider down the toilet" is confirmed. | Nexus 704K; Lanay 95.7K; then 1.2K, 319, 93, 71 |
| 2 | what happens to a cockroach after you vacuum it up | 28,675 | 27 | Not confirmed ("vacuum cockroach" only). The spider version is confirmed. | National Geographic 3.0M (85 s clip); then copies at 261, 56, 27, 22 |
| 3 | what happens if you trap a cockroach and forget about it | 13,731 (+31.4%) | 35 | Not confirmed. "what happens if you trap a spider" is confirmed. | Peekaboo Kidz 4.9M (different topic); copies at 1,899, 595, 453, 268, 229 |
| 4 | what happens if a cockroach walks across your food for just one second | 6,761 | 40 | Not confirmed ("what happens if you eat a cockroach" is) | Curio's housefly version 13K in this list (604K per vidIQ); Cockroach Zone 20.5K |
| 5 | what happens to a cockroach without food or water (also: how many days can a cockroach survive without food and water, 6,520) | 6,635 | 40 | Not run | Not run (the list returned no view counts) |
| 6 | what to do if you see a spider in your house | 5,796 | 31 | Confirmed (3 forms) | Not run |
| 7 | what happens if you squish just one cockroach in winter | 5,228 | 21 | Not confirmed ("kill a cockroach" forms are) | Not run |
| 8 | what happens when a cockroach loses its head | 5,069 | 34 | Confirmed (2 forms) | Peekaboo Kidz 4.9M ("without its head") |
| 9 | silverfish cluster: best row "why you should never wash a silverfish down the drain" (also: trapped in a bathtub 4,664 at competition 9; turn on the light 4,562; leave one alone in your house 4,017) | 4,861 | 13 (the bathtub phrase is 9) | "are silverfish dangerous", "are silverfish harmful", "why are silverfish in my room" confirmed; the long phrases not | Weak: top bathtub result 8.5K (a trap product), next 2.2K, then 37, 9, 3 |
| 10 | does the spider in your house know you exist | 4,651 | 33 | Not run | Zyka 592K (11/5). Already taken. |
| 11 | what really happens if you kill a house centipede in your basement | 4,623 | 26 | Confirmed ("what happens if you kill a house centipede") | Bright Side 2.59M; Facts Verse 1.85M; Garden Whispers 482K; Crawl Space Ninja 443K |
| 12 | why you should never kill a spider in your house | 4,487 | 40 | Not run | We already have "Should You Kill the Spider in Your Ceiling Corner?" (187 views) |
| 13 | which spider lives in your house right now | 4,218 | 34 | Not confirmed ("when you find a spider in your house" is) | MyWildBackyard 2.03M (16 min ID video) |
| 14 | what happens if a spider lives in your house for a year | 3,644 | 29 | Not confirmed. "why are there so many spiders in my room" is. | Nothing on the exact phrase. Raph Explores 17.6K ("trap a spider") |
| 15 | what happens if you leave a house centipede in your bathroom | 3,605 | 22 | Phrase not confirmed, topic confirmed | Same centipede videos as rank 11 |

**Autocomplete-only questions (confirmed typed, no volume figure):** "do bed bugs fly" (top suggestion; also "can bed bugs fly", "do bed bugs jump"), "do house spiders bite", "are house centipedes good", "is house centipede dangerous", "what do house centipedes eat", "why are stink bugs in my house", "why are earwigs in my house", "do cockroaches bite / fly / go in your ears". [KW]

**Google Trends signals (YouTube search, US, 12 months, chained to "kill spider" = 65.5).** Rounded to one decimal by Trends, so the small ones are rough.

| Term | Level against "kill spider" = 65.5 | Last 4 weeks against the 12-month mean | Note |
|---|---|---|---|
| house spider | 124.5 | 48.0 against 63.9 (falling) | peak week 2026-08-16 |
| termites | 103.9 | flat | |
| silverfish | 81.3 | 55.0 against 42.2 (rising) | peak week 2026-10-25. Minecraft searches inflate it. |
| daddy long legs | 77.0 | 27.0 against 39.5 | |
| kill spider | 65.5 | 36.8 against 65.5 | peak 2026-08-09 |
| kill ants | 32.2 | 10.5 against 32.2 | |
| earwig | 18.5 | 7.0 against 9.5 | |
| carpenter ants | 17.7 | 25.2 against 9.1 (rising) | peak 2026-10-25 |
| kill wasp | 8.4 | 2.2 against 8.4 | |
| bed bug bites | 7.3 | 11.5 against 3.8 (rising) | peak 2026-10-25 |
| kill cockroach | 2.6 | 3.2 | peak 2025-11-16 |
| centipede bite | 3.3 | | |
| kill centipede, cockroach bite | 0.4 each | | too small to rank |

"Cockroach" on its own is swamped by a political meme ("cockroach janta party" shows as the top rising search), so I did not use the bare word. "Black widow" is swamped by the film. [TRENDS]

**What the ranking means.** Rank 1 to 4 have the biggest vidIQ estimates, but they are the topics where copies mostly flop (section 1, item 3) and where autocomplete did not confirm the long phrase. Rank 8, 11 and 15 are confirmed in autocomplete. Rank 11 and 15 are the house centipede, which is our best lane on TikTok (305 times our TikTok median on Part 2, `swot-1117.md`). Bed bugs and silverfish are rising now on Trends. So the plan in section 6 starts with the centipede, not the biggest estimate.

---

## 5. Our gap: the 5 biggest differences, each with a fix

Our 13 long-forms today (public views 11/18 [YT-DLP]): 229, 187, 165, 135, 127, 96, 60, 45, 9, 8, 8, 6, 4. Median 60. Total 1,079. (The brief says 12; the channel listing and `titles-1116.md` both show 13.) Studio numbers through 11/14 for impressions, CTR, average viewed and AVD: `playbook-1116/analytics.md` section 3. All 13 were published 10/22 to 11/14. Titles were refit to autocomplete questions on 11/16 and 11/17, so the Studio numbers mostly reflect the old titles.

### Difference 1: Our titles are statements, lists and generic phrases. The outliers' titles are the typed question.

- **Outliers:** 15 of the 18 in section 2 are "what happens if / to / when [you do X]" or "why it sucks to be born as [animal]". The title text is the search.
- **Us:** 8 of our 13 original titles were lists, rankings or myth or quiz forms ("3 Bugs...", "6 Creatures...", "Weird Animal Facts...", "12 Animal Myths..."). The refit on 11/16 turned several into autocomplete phrases, but `titles-1116.md` itself notes that 9 of 13 long-form titles had no question form that autocomplete offered.
- **Fix:** every long-form title starts with a phrase that autocomplete or `kw --search` shows, in question form, and says the viewer's action ("What happens if you leave a house centipede in your bathroom?"). Run `postkit.py kw --search "<title>"` first and record the top 5 results with their views in the fact pack.

### Difference 2: We have no impressions. The outliers' topics have real demand. This is the biggest gap.

- **Us:** long-form impressions of 33 to 5,262 per video, median 1,439 (n=13). CTR is not the problem: 4.63% (spider), 4.37% (3 More Bugs), 5.44% (3 Bugs) against YouTube's "half of all channels" range of 2% to 10%. Best video 229 views. [STUDIO, OUR MATH]
- **Outliers:** Zyka's weakest 15 of 28 median 3,400 views; its median is 8,500. Even a channel of 1,250 subscribers (Sixandsixty) got 700K from one search-led title. [YT-DLP]
- **Fix:** choose topics from section 4's table where a real typed phrase exists and the top results show room (small competition score, or top results that are old or weak). Also copy Zyka's habit of putting the question in the first line of the description and the phrase in the tags. Stop picking topics for the story and start picking them for the query.
- **Honest limit:** demand does not guarantee a result. In section 1, item 3, 5 of the 6 flush videos got under 100K. Use the stop rule in section 6.

### Difference 3: We hop between topics. The outliers hold one lane and follow a winner within days.

- **Us:** in 3 weeks we posted 13 long-forms across 3 lanes: bugs and spiders (5), animal myths, facts and dogs and cats (6), CIA history (2). The CIA videos got 4 and 8 views.
- **Honest note:** inside our data the bug and spider five (median 96) and the animal six (median 91) look the same. At under 250 views each, we cannot say that a lane helped us. This difference comes from the outliers, not from our numbers.
- **Outliers:** Zyka stays in "what happens when you do X to a household bug" for 27 long-forms. Its sequel came 9 days after the 2.4M video. Stone had one hit and stopped after 2 more videos.
- **Fix:** the next 10 are one lane (house bugs, what happens if you...), with a sequel rule: any video that passes 10 times our long-form median (600 views, from the current median of 60) within 7 days gets a same-format sequel on a different bug within 7 to 10 days. Off-lane long-forms (history, myths) wait until the lane has a result.

### Difference 4: We lose viewers in the middle. The outliers re-hook every 30 to 60 seconds.

- **Us:** average viewed under 25% on 9 of 13 long-forms (6.58% to 24.17%); AVD from 0:44 to 2:14 on videos of 4:34 to 11:18 (the exceptions are two near-empty videos with 3 to 5 views). The only 40%+ videos are the 4:34 and 2:15 ones. Intro retention is fine (70% at 0:30 for "3 Bugs"). [STUDIO]
- **Outliers:** a new sub-question or stake line every 27 to 60 s in lane Q (counts in 2c), a beat every 33 to 80 s in lane B, a one-line stake after big beats, and a closing callback to the first line (Zyka: "It was already home"; Nexus: "You just sent it home"; Bodo: "You just locked up for her").
- **Fix (script rules for every video in section 6):** (a) the title question restated by 0:15; (b) the 2 or 3 possible answers named by 0:20; (c) a named source by 0:30; (d) a new sub-question at least every 45 s, written as a spoken question; (e) one stake sentence after each beat; (f) a last line that calls back the first one; (g) the practical "what to do instead" with its condition. This fits the existing flagship template (cold open, same beats per chapter, a re-hook at the end of each chapter). I could not see our own retention curves, so (a) to (g) are copied from the outliers, not proven on our videos. The 11/24 vidIQ read, or a Studio screenshot, should test them.

### Difference 5: Length and hours. The outliers earn hours two different ways. We do neither yet.

- **Us:** our best AVD is 1:57 ("3 Bugs", 4:34). At that AVD, 4,000 hours takes about 123,100 views (4,000 x 3,600 / 117 s) and 8,000 hours takes about 246,200. [STUDIO, OUR MATH]
- **Outliers:** lane Q wins at 3:26 to 4:31, which makes a high percent viewed easy but earns only minutes per view. Lane B runs 8 to 12 minutes, which earns more minutes per view if people stay. I do not know either lane's average view duration, because only the owner can see it.
- **Fix:** use lane Q (4 to 5 minutes) to win impressions and a breakout. Put one lane B video (8 to 10 minutes) into the plan as the hours test. When a lane Q video breaks out, the next video is the sequel (4 to 5 minutes), and the lane B follows. Do not pad a Q video past about 5 minutes: Zyka's 6 winners ran 3:26 to 4:31.

**Not a top-5 gap:** thumbnails and CTR. Our stick-figure Meatball with 1 to 3 caps words already matches lane Q's look, and our CTR is in range.

---

## 6. The 10-video long-form plan

This follows the flagship template in TASKS.md (11/17 5:35 PM): cold open with no intro, a fixed beat order inside each chapter (reveal, ID card, "will it bite you", "why is it in my house", "what should you do" with its condition, a Meatball reaction), a re-hook at the end of each chapter, a comment prompt at about two thirds of the way (the flagship's "about 3:30" is for a 7 to 8 minute video), the last 20 seconds left clear for end screens, and a description with timestamps and sources. It adds the section 5 script rules. Every script still goes through the fact pack, a checker who opens the sources, and the other gates in TASKS and MASTER_ORDERS.

**Video 0 (the flagship, already ordered): "House Bugs Ranked From Harmless to Get Out", Wed 11/18 5 PM.** Read it at 72 hours against Benny Goes Wild's ranked spiders video (4.3x its median), not against Zyka. It is the list shape, which has the weakest outlier evidence in this file.

**Draft hook lines contain no facts.** They are scene and question only, so they stay true whatever the fact pack finds. Titles are 100 characters or fewer, start with the typed phrase, and use none of the banned words (TRUE or FALSE, Myth, Believe, Cartoons, Lied, "Did you know").

| # | Title | Lane and length | Draft hook line | Why this one, and in this place | What we already have |
|---|---|---|---|---|---|
| 1 | What Happens If You Leave a House Centipede in Your Bathroom? | Q, 4 to 5 min | "You flip on the bathroom light. A house centipede is on the wall. Your hand reaches for a shoe. Stop. Here is what happens if you leave it." | Our best lane (TikTok Part 2 at 71.1K, 305x our median; `swot-1117.md`). Topic confirmed in autocomplete. vidIQ 3,605 a month, competition 22. Big results already exist (2.59M, 1.85M), so demand is proven. | Fact pack and QA in `qa/centipede-p4-1117.md` |
| 2 | What Happens to a Cockroach After You Flush It? Inside the Pipes | Q, 3:30 to 4:30 | "It is late. You flip on the bathroom light and a cockroach is next to the toilet. One flush. Is it really gone?" | Biggest vidIQ estimate (46,960). Proven by one outlier (704K) but 5 of 6 copies got under 100K, so we need our own angle and our own sources. First 40 characters match the typed phrase. | `scripts/facts/cockroach-bornas.md` for the species facts |
| 3 | What Happens to a Silverfish Trapped in a Bathtub? | Q, 3:30 to 4:30 | "You step out of the shower and a silverfish is stuck in the tub. You could rinse it down the drain. Should you?" | Lowest competition in the set (9). Rising on Trends (55.0 against 42.2). Autocomplete confirms the short forms ("are silverfish dangerous"), not this long phrase. Search results are weak, so a small win is possible, but demand is the least proven. | `qa/silverfish-p5-1118.md` |
| 4 | What Happens If You Trap a Cockroach Under a Cup for a Month? | Q, 3:30 to 4:30 | "You trap a cockroach under a cup. Then you forget it. A month later, you lift the cup." | vidIQ 13,731 (+31.4%), competition 35. Closest copies got 1,899 or less. This is Zyka's spider-trap idea on a new bug, so write it as its own story with its own sources (not the same beats). Slot it after video 2 so two cockroach videos do not run back to back. | Cockroach facts |
| 5 | Do Bed Bugs Fly or Jump? How They Get Into Your Bed | Q, 4 to 5 min | "You found a bite on your arm. Now you are checking the bed. Do bed bugs fly to you, or jump to you?" | "do bed bugs fly" is the top autocomplete result. Bed bug bites are rising on Trends (11.5 against 3.8, peak 10/25). No vidIQ volume figure: a gap in the evidence. The flagship's rule applies: any heat advice carries the EPA safety line. | `scripts/facts/bed-bugs.md` and `qa/shorts-push-1116-bed-bugs.md` |
| 6 | What Happens If a Spider Lives in Your House for a Year? | Q, 4 to 5 min | "There is a spider in the corner of the ceiling. It has been there since last winter. You never touched it. What has it been doing?" | vidIQ 3,644 a month, competition 29. No video on the exact phrase. Spider is our second-best Short topic (median 1,104.5, `swot-1117.md`). Do not reuse Zyka's "know you exist" angle. | `scripts/facts/house-spiders-id.md` |
| 7 | What Really Happens If You Kill a House Centipede in Your Basement? | Q, 4 to 5 min. **Sequel slot.** | "Last time you left it alone. This time you stepped on it. Here is what changes in your house." | vidIQ 4,623, competition 26, confirmed in autocomplete. It is the sequel for video 1. If video 1 passes 600 views in 7 days (10x the current median of 60), post this within 7 to 10 days. If not, post it in its normal place. Do not reuse the exact words of Facts Verse's or Bright Side's titles. | Same centipede fact pack |
| 8 | Why Are Stink Bugs in My House? | Q, 4 to 5 min | "The sun hits your window and something on the glass is moving. Why is it always your window?" | "why are stink bugs in my house" is confirmed in autocomplete. The Sixandsixty video (700K) proves demand. Trends shows no strong interest now, so hold it until the other topics are out or until spring. Sixandsixty's video is long (7:58) and AI-labeled, so write ours shorter and in our own voice. | None. A new fact pack is needed. |
| 9 | Which Spider Lives in Your House Right Now? | Q, 5 to 6 min (an ID video) | "You found a spider in the hallway. Is it the harmless kind, or the one worth a phone call?" | vidIQ 4,218, competition 34. We already built the script. The top result is a 16-minute ID video (2.03M), so ours has to be shorter and sharper. | `scripts/longform-spider-id.md` and `research/factcheck-spider-id-1116.md` |
| 10 | Why It Sucks to Be Born as a House Cockroach (fallback title: Your Life as a House Cockroach) | B, 8 to 10 min. **The hours test.** | "You crack out of your egg in the dark behind a kitchen cabinet. You have no mother. You have a crumb." | The only lane B video in the plan. Lane B outliers came from channels our size and bigger (giblixy 2.6M, Zoozle 2.6M, Sketching the Wild 1.6M). The "sucks" title needs Nolan's yes (MASTER_ORDERS, open ask 2). Keep "Your Life as a" as the fallback. Our own born-as house cat got 60 views and a 2:14 AVD, so treat this as a test, not a bet. | `scripts/longform-cockroach-bornas.md` and `research/factcheck-cockroach-bornas-1116.md` |

**Order:** 1, 2, 3, 4, 5, 6, then 7 (or earlier as the sequel), 8, 9, 10. One cockroach story is spaced from the next by at least one other bug. Videos 2 and 10 are both cockroach videos: if 2 flops, move 10 to the end.

**Stop and go rules (mine, not YouTube's).**
- **Go:** a video at 10 times our long-form median (600 views) within 7 days gets the sequel in 7 to 10 days. A video at 100 times (6,000) earns a second lane Q video the same week.
- **Stop:** if the first 4 lane Q videos each have under 150 views at 7 days, the lane is not working at our size. Stop and read the retention curves (11/24) before building more.
- **Policy guard (YouTube's own words in `faceless-outliers-1117.md`):** a distinct fact payload and a different ending in each video, no "Meatball lived" repeat, no exaggerated-distress framing. Never reuse a Zyka, Nexus or Bodo title word for word.

---

## 7. Notes for the main session

- **The spider-outside fact-check (`research/factcheck-spider-outside-1118.md`) is titled "What happens to a spider after you throw it outside?".** That is Zyka's 2.48M video, almost word for word. If that topic ships, change the title and the story so it adds something Zyka's does not. Do not use it as a Lane Q video as written.
- **MASTER_ORDERS "Direction change" (11/11) says no new bug videos.** The 11/17 [MEATBALL] notes in TASKS.md order bug long-forms, and Nolan's 11/17 order is to follow those notes. The plan above follows TASKS. Say so to Nolan if he wants it pulled.
- **Slots.** MASTER_ORDERS puts "born as" videos on Saturdays through December (polar bear 12/5, lion 12/12, others). This plan does not take those slots. I did not assign dates; the Wed or Thu 17:00 midweek slot is the natural home for videos 1 to 9.
- **vidIQ credits:** balance 15 after this run (see section 1).

---

## 8. Could not measure

- **Anyone else's traffic sources, impressions, CTR or average view duration.** Only owners see them. "How it was found" in 2c is inferred from titles and search estimates.
- **Our own retention curves,** per-video traffic sources and mid-video drop points. Studio or the 11/24 vidIQ read. The section 5 fixes are copied from the outliers.
- **Real search volume.** vidIQ's monthly numbers are estimates and may be inflated where the question is already someone's title. Autocomplete confirms a phrase is typed but gives no volume. Trends is relative and rounded, and "spider", "ants", "black widow", "cockroach" and "silverfish" are polluted by films, games and a meme.
- **Seasonality.** `postkit.py trends season` failed twice (Google returned code 400), so I have only the last 12 months, not a multi-year pattern.
- **Chapters and re-hook counts for 8 outliers** (no transcript pulled, to save vidIQ credits) and descriptions for Nexus, Sixandsixty and Bodo.
- **Re-hook counts are my hand counts** from transcripts, plus or minus one. The definition is in 2b.
- **Bound's and Forgotten Lin's channel listings returned 403**, so Bound's multiple uses vidIQ's own "breakout" score (8.8x), a different measure. Dinzo's multiple is also vidIQ's. Stone's median rests on 3 videos.
- **Whether AI-labeling or the July 2025 "inauthentic content" rules affect these channels.** Their monetization status is not public.
- **The 13th long-form.** The brief and the asks file say 12; the listing and `titles-1116.md` show 13.
- **Whether the outliers' success came from the topic, the execution, or luck.** The copy results in section 1 suggest it is not the topic alone.

## Sources

- [YT-DLP] flat listings of the channels of Zyka, Stone, Dinzo, Zoozle, giblixy, Sketching the Wild, Bodo, Nexus Explainer, Sixandsixty, Curio, Titly, Benny Goes Wild, The Animal Person, Fishy Science, and @MeatballMyths, read 11/18/2026.
- [VIDIQ] `outliers` (2 calls), `get_videos_by_ids`, `video_transcript` (10 calls), `keyword_research` (4 working calls, 1 with no data), 11/18/2026.
- [OFFICIAL] https://support.google.com/youtube/answer/7628154, https://support.google.com/youtube/answer/16559650, https://support.google.com/youtube/answer/141805, https://support.google.com/youtube/answer/9314415, Creator Insider "YouTube Algorithm 2026" 9/1/2026 (caption transcript mirror: https://viewrankai.com/tools/youtube-transcript/rHLjxrbXmmY).
- [KW], [TRENDS] `postkit.py kw`, `kw --search`, `trends compare`, `trends related`, 11/18/2026.
- [STUDIO] `channels/playbook-1116/analytics.md` section 3; `channels/research/swot-1117.md`; `channels/research/faceless-outliers-1117.md`; `channels/research/youtube-deep-dive-1117.md`; `channels/fixes/titles-1116.md`; TASKS.md 11/17.
