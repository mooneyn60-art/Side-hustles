> OWNER: MEATBALL CLAUDE ONLY (@MeatballMyths). Etsy Claude: ignore this file.

# Cutout traction research, 11/20 (Studio)
Read-only research. Pulled 11/20 9:34-9:50 AM ET. Every claim below has a link or our own numbers. Anything that isn't proven is labeled **GUESS**.
Tools used: yt-dlp on public YouTube and TikTok pages (public counts lag Studio and the TikTok app), curl, web search, and frame grabs of the first 4 s of comp videos.

## TL;DR
1. **TikTok is not the main problem. YouTube is.** At matched ages (15-23 h), TikTok cutouts got 0.27-0.9x the same-day bug cuts (Rick 309 vs bug 263-429). On YouTube they got 0.03-0.3x (7/46/48 vs 152/272).
2. On YouTube the cutouts are **62-63 s**. The bug Shorts are **16-20 s**. The breakout comps' top Shorts are mostly **10-35 s** (Hatim's 12-20 s, Mischief Time 11-21 s, Cas van de Pol 10-12 s). On TikTok, 61 s+ is fine: Fruit Love Island episodes run 69-144 s and get tens of millions of views, and TimonsDreams' median is 83 s.
3. **Every cutout opens with a "MEATBALL MYTHS / TITLE" banner over a static wide shot plus a setup line from the narrator.** The comps open on the target or the action in frame 1: MeatCanyon shows a caricature plus a headline naming the target, and Hatim's opens on slapstick in the first second.
4. **Our topics are generic types** (a Karen, an uncle, a cookout). The breakouts name a target people already know or search for: Trump, Zelensky, Mbappé, xQc, Taylor Swift, "White Women Ordering Pumpkin Spice Coffee". Hatim's posted the Trump-Putin-Xi China summit the same day and got 100K views in 1 day.
5. **Series and recurring characters drive the biggest animated growth of 2026.** Fruit Love Island gained 2.3M followers in 4 days with numbered episodes. TimonsDreams' top video is a "Part 2". Mashed has standing series. The Chit Show grew by adding recurring characters.

---

## 1. OUR DATA

### 1a. Matched-age table (public counts, 11/20 ~9:35 AM ET)
Ages are computed from yt-dlp upload timestamps. Times are ET.

| Platform | Video | Type | Posted (ET) | Age (h) | Length | Views | Likes | Comments | Shares |
|---|---|---|---|---|---|---|---|---|---|
| YT | Uncle Rick DNA Test (If70iDk7Qes) | cutout | 11/19 10:13 | 23.3 | 62 s | **7** | 1 | 1 | - |
| YT | HOA Karen (kZf7dx_hKbQ) | cutout | 11/19 14:31 | 19.0 | 62 s | **46** | 5 | 1 | - |
| YT | Cookout at the End of the World (n6dDV0UVT8c) | cutout | 11/19 17:31 | 16.0 | 63 s | **48** | 1 | 1 | - |
| YT | Dust Mites Can't Bite (c09ijR9_3dM) | bug | 11/19 16:04 | 17.5 | 20 s | 272 | 2 | 1 | - |
| YT | House Spiders Bite Only If Squeezed (ikLjIJbEHdU) | bug | 11/19 19:03 | 14.5 | 17 s | 152 | 2 | 1 | - |
| YT | House Centipede Bites Uncommon (nLrVbcLedsY) | bug | 11/18 20:31 | 37.1 | 16 s | 981 | 8 | 1 | - |
| YT | Silverfish Weak Jaws (bmN1eg2wQiw) | bug | 11/18 14:06 | 43.5 | 19 s | 936 | 9 | 1 | - |
| TT | Rick (7709900991461592350) | cutout | 11/19 10:13 | 23.4 | 62 s | **309** | 9 | 0 | 2 |
| TT | HOA Karen (7709961092184739086) | cutout | 11/19 14:06 | 19.5 | 62 s | **92** | 3 | 0 | 0 |
| TT | Cookout (7710022435617262878) | cutout | 11/19 18:04 | 15.5 | 62 s | **185** | 3 | 0 | 0 |
| TT | Silverfish age (7709929081294376223) | bug | 11/19 12:02 | 21.5 | 61 s | 429 | 27 | 0 | 0 |
| TT | Do house spiders bite (7709991289202248990) | bug | 11/19 16:04 | 17.5 | 62 s | 263 | 3 | 0 | 0 |

- **Baselines.** YouTube bug-Short median is 716 (from the brief). On TikTok, the last 30 bug cuts have a median of **314.5** views and all 119 bug cuts have a median of **299** (yt-dlp, @meatballmyths). The account has **9,619** TikTok followers (public profile) and 1,020 YouTube subscribers (brief).
- **YouTube ratio,** cutout median vs same-day bug average at matched age: 46 vs 212 = **0.22x**.
- **TikTok ratio:** 185 vs 346 = **0.53x**. Rick (309) roughly matched a same-day bug cut (263).
- **TikTok like rate:** Rick 2.9%, HOA 3.3%, Cookout 1.6%. Bug cuts: silverfish 6.3%, spiders 1.1%. Rick is the only cutout with shares (2).
- **Earlier reads** (claude/status.md, 11/19 6:45 PM): HOA had 5 TikTok plays at 4.6 h while the spiders bug cut had 231 at 2.7 h. The cutouts' first push is far smaller.
- **YouTube metadata:** cutouts are in the category **Comedy**, bug Shorts in **Education**. None of the cutouts are age-restricted (age_limit 0). TikTok labels cutouts "Comics & Cartoon, Anime" and bug cuts "Humanities" (status.md).
- **Not measured** (Studio or app only): "chose to view vs swiped away", average % viewed, traffic source, any FYF-ineligible notice. **Ask Studio/Data for these first.** They will tell us whether the problem is the hook (swipe-away) or the seed audience (too few impressions).

### 1b. Script and open audit (channels/scripts/cutout-*.md, plus frame grabs of the live posts)

| Ep | First 2 s, as posted | Topic and target | Joke density | Notes |
|---|---|---|---|---|
| Cookout (ep1) | "THE COOKOUT AT THE END OF THE WORLD" banner over a static backyard; Meatball: "The news says it's the end of the world…" (YT auto-captions) | generic cookout; Elon and Zuck appear as cameos only | ~10 beats in 75 s (1 per ~7 s) | Exposition opener. The named targets come too late and too briefly. |
| HOA Karen (ep4) | "MEATBALL MYTHS / HOA KAREN" banner over a static wide shot of the lemonade stand; caption "EVERY NEIGHBORHOOD" | generic Karen | ~25 lines in 62 s (1 per ~2.5 s) | Dense. But "Karen" is a 2020 meme and there's no news peg. The green-hat kid reads like a South Park lookalike (**GUESS: IP or "unoriginal" risk**). |
| Rick DNA (ep8) | Meatball: "Uncle Rick took a DNA test. Rick has opinions about DNA." (setup, no conflict yet) | race/heritage; Rick is the butt | ~20 lines in 62 s | Best on TikTok (309, 2 shares). Worst on YouTube (7). **GUESS:** race plus a 62 s length plus the YouTube seed audience (bug-education viewers) gave a poor first-test signal. |
| Thanksgiving Politics v3, Black Friday v8/v9, Holy BF v4, Confession, Ozempic, ep5/ep6/ep7 | All open with "[Banner: MEATBALL MYTHS / TITLE]" and a Meatball setup line | Confession and Ozempic are the first scripts with named targets (Cowboys, Vatican bank, Oprah, IKEA) | 4-5 swears planned, first at 12-16 s | The named targets are side bits. None is the premise. |

**Verdict.** Joke density is not the main problem: most cutouts land a line every 2.5-3.5 s. The problems are:
- **(a) The open.** Branding plus exposition instead of conflict in frame 1.
- **(b) No recognizable or searchable target as the premise.**
- **(c) 62 s on YouTube**, against our own 16-20 s bug Shorts and comp hits of 10-35 s.
- **(d) Titles with no search intent**, e.g. "| Animated Comedy". The bug Shorts' question titles carry the search.

---

## 2. COMPS (public counts pulled 11/20 via yt-dlp and TikTok public pages)
"Median" is the median views of the latest ~60 Shorts on YouTube, or the latest 30-40 posts on TikTok.

| # | Channel | Followers | Median views | Top videos (views, length) | Topic | First-2-second hook | On-screen text | Cadence |
|---|---|---|---|---|---|---|---|---|
| 1 | **Hatim's Shorts** [YT](https://www.youtube.com/@hatimsshorts) / [TT](https://www.tiktok.com/@hatimsshorts) | YT 729K, TT 747K | YT 635.5K, TT 866.6K | "Donald Trump Had Enough of Kim Jong Un 😂" 17.9M (12 s, 10/4/26); "Trump Just Keeps Trolling Zelensky" 12.6M (20 s); TT "After the peace negotiations…" 31M (16 s) | world leaders in slapstick, news-reactive ("Trump, Putin and Xi Jinping meet in China!" posted 11/19, 100.6K in 1 day) | frame-checked: slapstick action in second 1 (water splash), no dialogue | none; small logo; title carries "Name + verb 😂" | ~0.8/day on TT; ~10 uploads/mo ([ReachRanking](https://reachranking.com/youtube/UCpaAinUuCAEA0IELy2v6QMQ): +3.1% subs in 30 d) |
| 2 | **Mischief Time** [YT](https://www.youtube.com/channel/UC0Badcq36RBDHN-e3N1Papg) | YT 9.89M | 510K | "Mbappé Was NOT Ready for Yamal's Next Move!" 13.6M (15 s, 11/1/26); "Mbappé Can't Stop Laughing at Haaland" 5.5M (21 s) | parody pranks with famous footballers | frame-checked: the stars already mid-scene in frame 1 | none; "#parody" in the title | 2+/day (2 posts on 11/20). Hit #13 worldwide in a World Cup week with 583M weekly views ([Parasocial/Tubefilter](https://www.parasocialmagazine.com/entertainment/ai-channel-mischief-time-cracks-youtubes-global-top-15/)) |
| 3 | **MeatCanyon** [YT](https://www.youtube.com/@MeatCanyon) | YT 9.19M | 3.45M | "White Women Ordering Pumpkin Spice Coffee" 22.1M (59 s); "xQc Needs More Views" 18.3M (60 s); "Clavicular Is Nutmaxxing" 4.56M (56 s, 5/29/26) | named influencers and celebrities plus stereotype bits, grotesque caricature | frame-checked: grotesque caricature plus a big headline naming the target at 0 s; line 1 states the absurd premise ("We have my doctor here to prove…") | headline title card in frames 0-1 s | about weekly |
| 4 | **정서불안 김햄찌 (Kim Hamchi)** [YT](https://www.youtube.com/channel/UCU5Bngb-griCg_96ZXpXOgg) | YT 726K | 1.1M | "인생사 새옹지마" 12.8M (94 s); "미라클 모닝" 3.0M (39 s) | AI hamster office worker, relatable work rage ([Somako](https://somako.co.kr/%ec%a0%95%ec%84%9c%eb%b6%88%ec%95%88-%ea%b9%80%ed%96%84%ec%b0%8c%ea%b0%80-%eb%b3%b4%ec%97%ac%ec%a4%80-%ec%b4%88%ea%b3%a0%ec%86%8d-%ec%84%b1%ec%9e%a5-%eb%a7%88%ec%bc%80%ed%84%b0%ea%b0%80-%ec%a3%bc/)): 100K subs in month 1, average Short ~30 s | frame-checked: fixed headline bar at top, character in the situation at 0 s | permanent top headline plus bottom captions | every 1-2 days |
| 5 | **Fruit Love Island (@ai.cinema021)** [TT](https://www.tiktok.com/@ai.cinema021) | TT 2.0M | 773.8K | Ep 15 40.1M (129 s); Ep 1 36.7M (69 s); Ep 21 19.8M (144 s) | serialized reality-TV parody with original characters | not frame-checked | "EPISODE N" title | 2.3M followers in 4 days; 7 episodes in week 1 ([case study](https://fruitloveisland.ai/blog/how-fruit-love-island-went-viral/)) |
| 6 | **TimonsDreams** [YT](https://www.youtube.com/@TimonsDreams) / [TT](https://www.tiktok.com/@timonsdream) | TT 779.4K, YT 154K | TT 422.4K (median length 83 s), YT 72.5K | TT "Part 2: Unc Vegeta taking the boys…" 1.8M (95 s); YT "Sasuke takes Naruto to the new barber…" 366K (71 s) | anime parody characters in everyday Black/LA life situations | not frame-checked | caption-style title | ~weekly; 111 videos in 2 years ([Resident](https://resident.com/art-and-culture/2026/03/13/how-timonsdreams-built-a-million-strong-audience-by-blending-anime-culture-with-real-life)) |
| 7 | **Haminations** [YT](https://www.youtube.com/@Haminations) | YT 9.12M | 13M | "What did I do to deserve this?" 100M (51 s); "He Went For The THROAT..." 14.8M (36 s, 7/25/26) | family storytime, crude stick-figure animation | frame-checked: characters in motion; story starts word 1 ("A while back, my nephews…") | big word-by-word center captions | ~monthly now |
| 8 | **Cas van de Pol** [YT](https://www.youtube.com/@cas) | YT 8.84M | 619K | "BIRDS! 🥪 \| TF2" 7.7M (10 s); "Lava Chicken \| Minecraft Movie" 567K (39 s, 11/15/26) | game and movie meme parody, trend-reactive | not frame-checked | minimal | several a week |
| 9 | **Mashed** [YT](https://www.youtube.com/@Mashed) | YT 5.56M | 172.5K | "Amy Finally Meets Her Sonic 🥺" 5.1M (41 s); "Peach's Backrooms Monster Is HORRIBLE" 3.06M (65 s) | gaming-character parody series | not frame-checked | emoji titles | daily. Added 100K subs in 3/2025 with recurring series ([Drop Media](https://www.dropmedia.co.uk/spud-gun-takes-over-mashed-from-channel-4-and-plots-global-expansion/)) |
| 10 | **Cyanide & Happiness (Explosm)** [YT](https://www.youtube.com/channel/UCWXCrItCF6ZgXrdozUS-Idw) / [TT](https://www.tiktok.com/@explosm) | YT 12.9M, TT 1.2M | YT 157K, **TT only 8.3K** | YT "Wait that's actually brilliant..." 3.9M (56 s); TT top 212K (21 s) | dark adult gag cartoons | frame-checked: title card "THE LAZIEST KNIGHT" plus dialogue from word 1 | logo bar plus word captions | daily on YT, ~0.3/day on TT |
| 11 | **brewstew** [YT](https://www.youtube.com/@brewstew) | YT 3.79M | 229K | "Dad Life" 2.73M (15 s); "Things 90s Teachers Yelled" 96.7K (107 s, 11/17/26) | relatable dad and 90s nostalgia | not frame-checked | hashtags in the title | weekly |
| 12 | **Wallace** [YT](https://www.youtube.com/@WallaceAnimation) | YT 228K | 418K (long-form) | "Your Life as Every Viltrumite Rank" 2.9M | brutally honest fandom satire; 2M views in 28 days on 19 videos ([LinkedIn](https://www.linkedin.com/posts/usmannow_wallace-animation-is-redefining-storytelling-activity-7407419988157911040-dw1F)) | not frame-checked | - | weekly |

**Cautionary comps.** These show both the demand and the risk:
- **The AI world-leader slapstick cluster** (Make AI Great Again, Global Presidents) passed 2.2B views in 2025, and 8 of the 10 most-viewed Trump videos on YouTube in 2025 came from it ([Forbes 9/17/25](https://www.forbes.com/sites/emilybaker-white/2025/09/17/bizarre-ai-generated-anti-trump-videos-are-getting-billions-of-views-on-youtube/)). YouTube said the videos don't break policy because they are labeled AI fiction. It did remove one account for ban evasion.
- **Explosive Media's AI Lego Trump videos** got millions of views. YouTube terminated the channel for spam, deceptive practices and scams ([RFI/AFP 4/16/26](https://www.rfi.fr/en/international-news/20260415-youtube-suspends-pro-iran-channel-posting-lego-style-clips-mocking-trump)).
- Both are realistic or propaganda-adjacent. **Do not copy the photoreal-politician look.** Our cartoon cutouts are the safe version of the same demand.

**What the breakouts share** (each point backed by the table above):
1. **A known name or premise in frame 1.** Trump, Mbappé, xQc, Naruto/Vegeta, Sonic, "white women + pumpkin spice". Nobody opens with a channel banner.
2. **Action or conflict in seconds 0-1, then dialogue from word 1.** There is no "this is the show" setup line.
3. **Length.** YouTube hits are mostly 10-60 s, and the newest breakouts (Hatim's, Mischief Time, Cas) run 10-21 s. On TikTok, longer episodes win when they are **serialized** (Fruit Love Island 69-144 s, TimonsDreams 83 s median).
4. **Recurring cast and series naming.** "Ep N", "Part 2", the same duo every time.
5. **Volume plus news reaction.** Hatim's and Mischief Time post daily and react within a day.
6. **Even big animated brands can flop on TikTok** without a TikTok-native hook (Explosm: 1.2M followers, 8.3K median). So the format is the problem, not the cartoon category.

---

## 3. TOPICS: what's live this week (sources) and 15 ranked ideas
**This week's verified news pegs:**
- Thanksgiving dinner cost is up ~6% to $58.63 for 10 people, and the turkey is up 10% ([AFBF](https://www.fb.org/news-release/cost-of-thanksgiving-dinner-increases-remains-below-2022-record-high), [Axios 11/20](https://www.axios.com/2026/11/20/thanksgiving-meal-cost-increases-2026)).
- Trump posthumously pardoned Pete Rose on 11/19 for his 1990 tax conviction ([AP](https://apnews.com/article/pete-rose-pardon-trump-baseball-14f398d4c657ccf55cb8a77cc7e60915), [NPR](https://www.npr.org/2026/11/20/nx-s1-6047757/trump-issues-posthumous-pardon-for-baseball-player-pete-rose)).
- Trump, Xi and Putin held a summit in Shenzhen ([World Watch 11/20](https://worldwatch.media/en/digest/2026-11-20)).
- Robert Pattinson was cast as the next James Bond on 11/16 ([BBC](https://www.bbc.com/news/articles/cwx2ev0pxmvjo)).
- "Melania: The Series" premiered on Prime Video on 11/20 ([AP](https://apnews.com/article/melania-trump-streaming-series-life-02e5c9ec1a482ea68094c2268a42856a)).
- At the Anthropic IPO, Ashton Kutcher's former fund holds a ~$7B stake, but he left it in July ([Fortune](https://fortune.com/2026/11/19/anthropic-ipo-sound-ventures-ashton-kutcher-7-billion-stake/)).
- The Apple iCloud/App Store outage on 11/17 was caused by an internal update ([TechCrunch](https://techcrunch.com/2026/11/17/apple-services-including-icloud-app-store-and-apple-music-hit-by-outage/)).
- Google Trends US daily RSS on 11/20 shows thanksgiving, turkey, melania trump, elizabeth debicki/Bond and guy oseary/Anthropic ([RSS](https://trends.google.com/trending/rss?geo=US)).
- **Calendar:** Thanksgiving is Thu 11/26 and Black Friday is 11/27. **GUESS:** the White House turkey pardon will fall on ~Tue 11/24, as in past years, and Spotify Wrapped will drop in early December, as in past years.
- TikTok Creative Center was not reachable without login, so it was not checked.

**Rules for all 15 ideas:**
- Obvious exaggeration only.
- No invented crimes, and no fake quotes presented as real.
- No abuse jokes and no slurs.
- The butt is the powerful person or the bigot, never a group.

**The 15 ideas, ranked by timeliness × name recognition × fit:**

| Rank | Title | Named target | One-line hook (frame 1 on-screen text in CAPS) |
|---|---|---|---|
| 1 | **The $58 Thanksgiving** | grocery CEOs / inflation; Rick blames everyone | "THANKSGIVING COSTS 6% MORE." Grandma holds up one green bean: "That's the whole side dish. We're splitting it ten ways." |
| 2 | **Turkey Pardon** (post within 24 h of the real ceremony) | Trump, as a cartoon president | "HE PARDONED A DEAD GUY LAST WEEK." Turkey: "Sir, can I get the Pete Rose deal?" |
| 3 | **Pete Rose Gets Pardoned in Heaven** (48 h window: post by Sat) | Trump / Pete Rose (real 1990 tax case, factual) | "TRUMP PARDONED A MAN WHO'S BEEN DEAD 2 YEARS." St. Peter: "Pardoned? He's still betting on the clouds." (**GUESS:** a betting gag is fine because MLB banned him for betting, a public fact) |
| 4 | **Trump, Xi & Putin Split the Dinner Bill** | Trump, Xi, Putin (cartoon) | "THREE WORLD LEADERS. ONE CHECK." All three refuse to pay; Meatball the waiter adds a tariff. (Proven demand: Hatim's got 100K in 1 day on the same summit) |
| 5 | **Uncle Rick Ep. 2: Rick Reviews Thanksgiving** (series) | Rick (returning) | "UNCLE RICK IS BACK. HE BROUGHT A FLAG CAKE." Builds the recurring-character habit. |
| 6 | **Black Friday Doorbuster** (v9 already in QA; a follow-up on 11/27) | Jeff Bezos / Walmart, as cartoons | "60% OFF (AFTER THEY RAISED IT 40%)." Already in our joke bank. |
| 7 | **Robert Pattinson Is Bond** | Pattinson's brooding persona (obvious parody) | "THE NEW JAMES BOND IS SAD." Bond refuses the martini: "I just want to be alone… in a tux." |
| 8 | **Meatball Goes to Confession** (script exists) | Vatican bank, Dallas Cowboys | Cold open in the booth: "Father, I ate a whole ham." Priest: "I bet on the Cowboys. Who's worse?" |
| 9 | **Thanksgiving on Ozempic** (rework of the Ozempic script) | Oprah, diet culture | "GRANDMA FOUND OUT EVERYONE'S ON OZEMPIC." Meatball's plate is untouched and he shrinks every beat. |
| 10 | **Grandma's Docuseries** | "Melania: The Series" / Prime Video | "MELANIA GOT A DOCUSERIES. SO DID GRANDMA." Ten episodes about a casserole. |
| 11 | **Ashton Missed the $7 Billion** | Ashton Kutcher (factual: he left the fund in July) | "HE LEFT 4 MONTHS BEFORE THE $7 BILLION." Meatball sells his lemonade stand one day before Karen buys it for a million. |
| 12 | **The Day iCloud Died** | Apple | "APPLE WENT DOWN. RICK HAD TO TALK TO HIS FAMILY." |
| 13 | **AI Took Dad's Job** (ep5 v4, retargeted at the AI IPO) | the trillion-dollar AI companies | "THE AI COMPANY IS WORTH $1.5 TRILLION. DAD IS WORTH ONE SANDWICH." |
| 14 | **HOA Karen vs Christmas Lights** (series: Karen Ep. 2) | Karen (returning) | "KAREN MEASURED YOUR CHRISTMAS LIGHTS." |
| 15 | **Spotify Wrapped Roast** (early Dec, date is a GUESS) | Spotify | "RICK'S #1 ARTIST IS THE NATIONAL ANTHEM." |

---

## 4. FORMAT

**Hook (0-2 s)**
- Cut the "MEATBALL MYTHS / TITLE" banner from the open and move it to the end card. Every frame-checked comp opens on the target or the action (MeatCanyon, Hatim's, Mischief Time, Haminations, Kim Hamchi).
- In frame 1, show **one caps headline naming the target and the absurd premise**. MeatCanyon uses a headline title card at 0 s, and Kim Hamchi keeps a permanent top headline bar.
- Put the first joke or conflict by 2 s.
- YouTube's Shorts lead says a view is an "intentional act of watching," and Studio shows viewed vs swiped away ([SEJ/Todd Sherman](https://www.searchenginejournal.com/youtube-explains-how-shorts-algorithm-works/494953/)).

**Length**
- **YouTube:** make a **20-35 s cut** of each cutout. The proof is in our own data: bug Shorts at 16-20 s get 5-20x the cutouts at 62 s. The comps' hits are 10-35 s.
- YouTube itself says story matters more than length ([SEJ](https://www.searchenginejournal.com/youtube-explains-how-shorts-algorithm-works/494953/)). **GUESS:** our 62 s cutouts lose viewers in the middle, so a shorter cut would help.
- **TikTok:** keep 61 s+. Creator Rewards needs videos of at least 1 minute ([TikTok Creator Academy](https://www.tiktok.com/creator-academy/en/article/creator-rewards-program)), and serialized 69-144 s episodes win there (Fruit Love Island, TimonsDreams).

**Pacing**
- Our line density (~1 line every 2.5-3.5 s) is fine.
- Remove the setup narration ("Every neighborhood has one…").
- Make sure the camera or characters move in second 1. Our HOA open is a static wide shot (frame grab).

**On-screen text**
- Keep one persistent top headline that names the target, plus word captions. Haminations and Explosm use big word-by-word center captions.
- Our masked or blurred-swear captions are fine. Keep caption text clean, per the standing rule.

**Series naming**
- Name episodes like "Uncle Rick Ep. 2" or "Karen Ep. 2", and build a recurring cast of Rick, Karen, Grandma and Pastor Chad.
- Evidence: Fruit Love Island's numbered episodes, TimonsDreams' "Part 2" top post, Mashed's series ([Drop Media](https://www.dropmedia.co.uk/spud-guns-mashed-named-best-comedy-channel-at-tellycast-digital-video-awards-2025/)), and The Chit Show growing by adding recurring characters ([TheWrap](https://www.thewrap.com/the-chit-show-tiktok-will-forte-bob-odenkirk-youtube-jay-renshaw-interview/)).
- Our own bug lane already uses "Things Living In Your House #58".

**Titles**
- Use "Named target + verb" plus one emoji, which is the pattern for Hatim's, Mischief Time and MeatCanyon.
- Drop "| Animated Comedy", which has no search intent.

**Look**
- **GUESS:** the cutouts reuse the bug-lane Meatball and the same flat vector look, so viewers and the system see the "same channel, different promise".
- **GUESS:** the green-hat kid is too close to South Park's Kyle. Redesign him so the characters read as original ([TikTok IP and unoriginal-content rules](https://www.tiktok.com/community-guidelines/en/integrity-authenticity)).

**Same account vs new account**
- YouTube's official pivot guidance: pivot gradually and mix old and new content; it "can take time (months, not weeks)". If you want to experiment "without impacting your existing core audience, consider creating a second channel" ([YT Help 16541080](https://support.google.com/youtube/answer/16541080)).
- Rene Ritchie (YouTube Creator Liaison) says discovery follows viewer interest, so existing subscribers may not follow a very different topic ([video](https://www.youtube.com/watch?v=JSYNPjcDakA), via search summary).
- YouTube says viewers aren't a fixed pool; early Short views are "exploratory" as it looks for an audience ([SEJ](https://www.searchenginejournal.com/youtube-explains-how-shorts-algorithm-works/494953/)).
- Our data fits a seed-audience mismatch on YouTube, where the bug audience is Education. TikTok shows a smaller gap because TikTok re-labeled the cutouts "Comics & Cartoon".
- **Recommendation:** stay on the same account for this 7-day test, as the owner wants. If YouTube cutouts are still under 25% of the bug median after 14 days, propose a second YouTube channel for the cutouts. **That needs Moondog88's yes, via Jarvis.**

---

## 5. PLATFORM RULES (official)

**YouTube AI disclosure** ([YT Help 14328491](https://support.google.com/youtube/answer/14328491))
- Disclosure is required only for **realistic** content.
- Creators "don't need to disclose non-realistic content made with AI". Its own example: an "AI-generated or altered animation of a missile in a fully animated video".
- "Disclosing AI content alone won't limit a video's audience or impact its eligibility to earn money."
- Our YT synthetic = NO setting is correct for cartoon cutouts.

**YouTube monetization, inauthentic content** ([YT Help 1311392](https://support.google.com/youtube/answer/1311392))
- As of 7/15/2025, "repetitious" content was renamed "inauthentic" and now explicitly covers "mass-produced, generic, repetitive" content.
- Reviewers look at the channel's main theme, most-viewed videos, newest videos and metadata.
- **GUESS (risk):** high-volume templated Shorts across two unrelated lanes muddy the "main theme". Keep each cutout clearly unique.

**YouTube ad-friendly profanity** ([YT Help 6162278](https://support.google.com/youtube/answer/6162278))
- Moderate profanity ("shit", "asshole", "bitch") "used frequently in the video" can earn full ads.
- Profanity "at the start or throughout the majority of the video", or "in most sentences", gets limited ads.
- Strong profanity (f*ck) in a title or thumbnail gets no ads.
- Slurs get no ads.
- Bleeped or obscured profanity is treated more leniently.
- **So:** 4-5 swears per video on punchlines, none in the open, is within the rules.

**YouTube harassment and satire**
- Insults are allowed in scripted satire and comedy ([YT Help 2802268](https://support.google.com/youtube/answer/2802268)), as Studio cited 11/20.
- YouTube left the AI world-leader satire channels up because they were labeled fiction ([Forbes](https://www.forbes.com/sites/emilybaker-white/2025/09/17/bizarre-ai-generated-anti-trump-videos-are-getting-billions-of-views-on-youtube/)).
- It terminated Explosive Media under its spam, deceptive practices and scams policies, not its satire rules ([RFI/AFP](https://www.rfi.fr/en/international-news/20260415-youtube-suspends-pro-iran-channel-posting-lego-style-clips-mocking-trump)).

**TikTok AI labels** ([Integrity & Authenticity](https://www.tiktok.com/community-guidelines/en/integrity-authenticity))
- Labels are **required only for AI content "that shows realistic-looking scenes or people."**
- TikTok says the AI-generated setting doesn't affect distribution ([TikTok Support AIGC](https://support.tiktok.com/en/using-tiktok/creating-videos/ai-generated-content), per the search summary; the page itself would not load via curl).
- **However:** since 11/24/2025, TikTok has been testing a "Manage topics" **AIGC slider** that lets viewers "choose how much AIGC they want to see" ([TikTok Newsroom](https://newsroom.tiktok.com/more-ways-to-spot-shape-and-understand-ai-generated-content?lang=en)).
- **GUESS:** with our label ON, viewers who turned AIGC down won't see these videos. This affects bug cuts and cutouts equally, so it doesn't explain the gap.
- Our label is ON under the owner's standing rule. **The rule is the owner's call.** Flag it to Jarvis; don't change it.

**TikTok For You feed eligibility** ([FYF standards, eff. 9/24/2026](https://www.tiktok.com/community-guidelines/en/fyf-standards), [Safety & Civility](https://www.tiktok.com/community-guidelines/en/safety-civility), [Integrity](https://www.tiktok.com/community-guidelines/en/integrity-authenticity))
- "Lower-severity degrading behavior may be ineligible for the FYF."
- Public figures get "more critical commentary" latitude than private people.
- Content is ineligible if it is "unoriginal or reused material without anything new".
- Unverified claims about crises or civic events are ineligible.
- TikTok avoids repeatedly recommending "extreme fitness or dieting" content, which matters for the Ozempic and gym jokes: keep them as cartoon gags, not diet advice.
- "If a video isn't getting many views, it also doesn't necessarily mean it broke a rule." Check analytics for an "ineligible for recommendation" flag.
- **So:** punch at public figures and powerful institutions, not at private "types" with degrading insults. This supports the named-target direction.

**TikTok monetization:** Creator Rewards needs 1 min+, original, high-quality content ([Creator Academy](https://www.tiktok.com/creator-academy/en/article/creator-rewards-program)). That's why we stay at 61 s+ on TikTok.

---

## 6. PLAN

### Top 5 changes, ranked by expected impact
1. **YouTube: a separate 20-35 s cut of every cutout. TikTok stays 61 s+.**
   - Evidence: our bug Shorts at 16-20 s get 5-20x the 62 s cutouts at matched age. Comp YT hits are 10-35 s (Hatim's, Mischief Time, Cas, brewstew). TikTok's 1-minute rule applies only to TikTok.
   - Cost: one extra Claude export per episode. That is a render, so it needs a Jarvis yes under the usage limits.
2. **Cold open on the target: no banner, a caps headline naming the target and premise in frame 1, conflict by 2 s, and the banner moved to the end card.**
   - Evidence: every frame-checked comp; our opens are all banner plus setup.
   - Measure it with Studio's "viewed vs swiped away" metric.
3. **Make the named target the premise, and react to news within 24-48 h.** Use topics 1-4 now: the Thanksgiving price, the turkey pardon, Pete Rose, the Shenzhen summit.
   - Evidence: Hatim's got 100K in a day on the summit; MeatCanyon's top videos are named targets; Mischief Time rode the World Cup to 583M views in a week.
   - Cartoon only, never photoreal (YouTube's disclosure rules and the Explosive Media takedown).
4. **Series and a recurring cast with numbered titles** ("Uncle Rick Ep. 2", "Karen Ep. 2"), plus a "follow for Ep. 3" end card.
   - Evidence: Fruit Love Island, TimonsDreams "Part 2", Mashed, The Chit Show. Rick is our only cutout with shares.
5. **Search-intent titles and first lines** ("Trump Pardons a Turkey… Again 🦃"), not "| Animated Comedy", plus a character redesign so the cast reads as original rather than as South Park lookalikes.
   - Evidence: the packaging rules in 2cd4154 (YT Help 12340300 and 12948449: titles and first lines share keywords) and the TikTok unoriginal/IP rule. The redesign is a **GUESS** on impact.

Not in the top 5: the extra swearing (4-5 per video). It is allowed (YT Help 6162278), but there's no evidence it drives reach. Treat it as a creative choice. **GUESS:** it is neutral for reach.

### 7-day test (Fri 11/20 - Thu 11/26)
- Bug Shorts keep their normal schedule alongside, each at least 1 h from a cutout on the same platform.
- One new cutout a day, within the 2-specialist-passes-a-day limit.
- Every cutout gets a TikTok 61-66 s version and, from Sun on, a YouTube 20-35 s cold-open cut. That needs Jarvis's yes for the extra exports.

| Day | Cutout (TT / YT) | Test variable |
|---|---|---|
| Fri 11/20 | ep3 Thanksgiving Politics (3 PM TT / 4 PM YT); Black Friday v9 (7 / 8 PM) after PASS | baseline: current format, 62 s on both platforms |
| Sat 11/21 | ep7 Vegan vs Gym Bro after PASS; **Pete Rose in Heaven (#3)** if Claude can turn it around in 48 h, else skip | baseline vs first news-reactive |
| Sun 11/22 | **The $58 Thanksgiving (#1)**: cold-open headline; YT 30 s cut | change 1 + 2 |
| Mon 11/23 | **Trump/Xi/Putin Dinner Bill (#4)** | named political target |
| Tue 11/24 | **Turkey Pardon (#2)**, posted within 24 h of the real ceremony (date is a GUESS) | 24 h news reaction |
| Wed 11/25 | **Thanksgiving on Ozempic (#9)** or **Meatball Goes to Confession (#8)** | named celebrity/institution side-target |
| Thu 11/26 | **Uncle Rick Ep. 2 (#5)** on Thanksgiving Day | series/recurring-character test |

**Measure at 24 h, then again at 72 h:**
- **YouTube:** views, "viewed vs swiped away" %, average % viewed, subscribers gained, traffic source (Shorts feed share).
- **TikTok:** views, average watch time, % watched in full, shares, follows, For You share, and whether it shows "ineligible for recommendation".

**What counts as a win:**
- A cutout reaches **≥ 50% of the same-day bug median on YouTube at 24 h** (≥ ~350 against the 716 median) and **≥ 100% of it on TikTok** (≥ 315).
- At least **one cutout beats 2x the bug median** on either platform.
- YouTube "viewed vs swiped" for the 30 s cuts is at or above the 62 s cutouts. **GUESS:** expect +10 points.

**What counts as a loss:** all 7 YouTube cutouts stay under 25% of the bug median (under ~180).
- Then escalate to Jarvis: propose a second YouTube channel for the cutouts (needs Moondog88's yes) and keep TikTok on the same account, since its gap is small.

**Do not change mid-week.** Read the numbers on Fri 11/27 and decide then.
