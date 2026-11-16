# Meatball Myths: growth research and change list (Nov 16, 2026)

Prepared for Social Studio, Mon Nov 16, 2026, about 4:55–5:20 PM ET. Read-only: nothing posted, scheduled, messaged or pushed.

**Sources used:**
- Public YouTube data via yt-dlp. Channel tabs were read today; tab view counts are rounded by YouTube, and exact counts appear only where a watch page was read.
- Web pages, linked inline.
- Our own data:
  - `/workspace/drafts/playbook-1116/analytics.md` (Studio 28d plus the 90d export through Nov 14).
  - `/workspace/drafts/playbook-1116/research.md`.
  - `/workspace/drafts/tracker-1116.md` and `growth-10k-1116.md`.
  - `/workspace/review-1116/` (our downloaded videos plus the TikTok tab pull, 109 posts from Oct 23 to Nov 16).
  - The Side-hustles repo `channels/research/growth-plan-longform-shorts-1115.md`.
  - MASTER_ORDERS on Claude's branch, read only.

**Labels:** `SEEN` means I read the number myself today. `TEAM` means it comes from an earlier team file. `ANALYSIS` means it's my inference.

---

## ⚠️ Two things to resolve before anyone plans on them

1. **TikTok Creator Rewards status conflict.**
   - The push brief and the growth plan treat 10K followers as the gate.
   - MASTER_ORDERS (line 18 and line 151) says *"He is in Creator Rewards (Nolan 11/14: 'I'm in the creator fund remember that')"* and *"TikTok Creator Rewards: RESTORED 11/11"*.
   - If he's already in, the 10K follower push isn't the gate. The real lever is **qualified views on original videos over 1 minute that reach 1,000+ For You views**, and our >60 s median is 221 (SEEN, n=91).
   - **Ask Moondog88 for one screenshot of the TikTok Rewards dashboard.**
2. **Possible production bug.**
   - The cartoon re-make "Daddy Longlegs Aren't the Most Venomous Spiders" (`w_eCp3tO_dQ`, 1–2 views) has **"Retention v2: daddy longlegs (rev 2)" burned into the bottom of every frame**. I saw it in the frame sheet of `/workspace/review-1116/youtube-2-daddy-longlegs-...mp4`.
   - Several recent Shorts are also stuck at 0–11 views: dust mites `A9lteZ9mtDE` 3, mice `MEEPvBFpcQM` 11, dog guilty look `xIbnhX10r7k` 4.
   - The cause isn't proven. The candidates are the debug overlay, re-posting a topic we'd already posted (the YouTube Oct 1 originality update), or a visibility restriction.
   - Claude's render pipeline should strip debug labels, and someone should check those IDs in Studio for restrictions.

---

## 1. Comparable channels (8), seen today

| # | Channel (subs) | Short length & hook style | Pacing | Recurring characters | Long-form format | Numbers seen |
|---|---|---|---|---|---|---|
| 1 | **Natural Habitat Shorts**: [channel](https://www.youtube.com/channel/UCSb_Sui6FBxVS4_ROsrU_Iw), 6.28M. TrendReport lists it at +50K subs in 30 days ([source](https://trendreport.com/channels/fastest-growing/for-pets-and-animals/)) | 29–33 s. The title is one real fact sentence. The video is a **cartoon comedy sketch with dialogue** that ends on real footage of the animal ("less cinematic but just as valiant"). | A scene every ~2–3 s with spoken dialogue. The joke comes first and the fact last. | **Yes, named recurring cast** (Kevin, Lisa, Batrick; there are character compilations and merch) | **Compilations of its own Shorts**, 4–12 min | Shorts tab median **4.25M** (n=40). [Ducklings imprint](https://www.youtube.com/shorts/lgLpsyyVmvg) 25.5M, 33 s. [Exploding ants](https://www.youtube.com/shorts/juJ52SemGw8) 4.14M, 30 s. [Marmot](https://www.youtube.com/shorts/rFRMgGE1xK0) 18.56M, 29 s. Compilations: [Part 1](https://www.youtube.com/watch?v=0Mly6OfT8t8) 4,300,159 (7:52), Part 2 2.6M, Part 3 906K, Batrick comp 884K, Kevin comp 416K, Lisa comp 229K, Christmas comp 114K |
| 2 | **Headlamp Guy**: [channel](https://www.youtube.com/channel/UCEwbkI91uCLJnbf9Wf67X9w), 16K, **started 2026** ([ChannelDB](https://channeldb.com/c/@guyheadlamp)) | 96–124 s Shorts that are **parts of a long story** ("Full stories here. In parts on Shorts, TikTok and Instagram"). Second person: "you're stuck somewhere". | Story beats with day counters ("Day 14") | **Yes**: the Headlamp Guy himself, plus a "he's hiding in every story" Easter egg | **Scripted serialized survival stories**, 10–17 min, with Part 2/3 and a "Full Movie" | Shorts median **559** (n=40), which is our level. Long-form median **73K** (n=10). [Absolute Zero: 100 Hours Survival in a Frozen City](https://www.youtube.com/watch?v=oxj91T7Li34) **1,473,226** views, 16:50, posted Oct 29, 2026. Boiling Point 649K. Lighthouse "Full Movie" (stitched parts, 40 min) 67K vs its parts at 16K–79K |
| 3 | **Zoozle** ("Why It Sucks To Be Born As…"): [channel](https://www.youtube.com/channel/UChFs6t9iB1yv0X8fuKtNIvA), 35.6K | Not checked (the Shorts tab failed) | Narrated cartoon "life story" from birth to death | The animal is the protagonist | **Scripted one-creature episodes**, 8–13 min | Long-form median **62.5K** (n=48). [Hummingbird](https://www.youtube.com/watch?v=j9J1RFgrgiI) 2,611,934. [Fire Ant](https://www.youtube.com/watch?v=sr0P5wU_DoQ) 1,882,579. Bedbug 52K, Tapeworm 198K. **Its 81-min compilation [Why it Sucks To Be Born As Insects](https://www.youtube.com/watch?v=7cq0G8Y8uwk): 1,279 views (posted Nov 14, so still young)** |
| 4 | **Casual Geographic**: [channel](https://www.youtube.com/channel/UC5Yo88QF-chdugJbAnB2tUw), 4.33M | 40–59 s. Second-person escalation timeline. [What if You Ate The Most Poisonous Animal…](https://www.youtube.com/shorts/XFFjxTllpoA) opens "If you ate one, first…", then "after 30-40 minutes…", then "don't bother praying" | A new caption beat every ~3 s. Host face plus photo, with a slang comedic voice | The host is the character | Scripted listicles, 7–38 min | Shorts tab median **4.7M** (n=9). That Short 7,933,799 (59 s). [FaceTimed an Eel](https://www.youtube.com/shorts/Ky0XPonYDcc) 8,607,828 (40 s) |
| 5 | **The Infographics Show**: 15.5M | 29–36 s. "What Happens When You…" / "What To ACTUALLY Do If…" | Flat 2D cartoon with fast narration | A narrator voice ([Meet the voice-over](https://www.youtube.com/shorts/drPjV8zkYmw) 1.1M) | Scripted 16–36 min | Shorts median **346.5K** (n=30). [What Happens When You Are Shot](https://www.youtube.com/shorts/V15wrmD5VFs) 3,001,979 (29 s). [Buried Alive](https://www.youtube.com/shorts/tbwFWiMSWwM) 732,491 (36 s) |
| 6 | **Zack D. Films**: 29.7M | 24–30 s 3D "How X works 😯". Body-curiosity hook in frame 1 | Continuous motion, no host | None | Mostly Shorts. Long-forms are scripted stories plus a few **compilations** | [How Splinters Get Unstuck](https://www.youtube.com/shorts/yGw0nhlUtkQ) 216,835,389. Long-form median 5.5M (n=12). [19 of My Creepiest Fiction Stories (Compilation)](https://www.youtube.com/watch?v=BtwxvD1JYAk) 3.1M (27 min), **the second lowest of the 12**. "13 Unreleased Videos I Thought Would Go Viral" (a compilation of *never-posted* Shorts) 11M |
| 7 | **Life Noggin**: 3.12M | 37–94 s. "Can You Survive…?", "How Mosquitoes Can Actually Kill You 😱" | Cartoon explainer with a Part 1/Part 2 split | **Yes, Blocko** (the recurring cartoon host) | Scripted 2–5 min | Shorts median **8K** (n=40). Long-form median 16.5K (n=40). Shows that a recurring cartoon host alone isn't enough when the topics are generic |
| 8 | **What If**: 8.99M ("could you survive" leader per [MakeViral](https://www.makeviral.ai/tools/survival-video-generator)) | Not pulled | 3D "hour by hour" escalation | None | Scripted 20–30 min | Long-form median **390K** (n=30). [What If all Glaciers Melted, INSTANTLY (Hour by Hour)](https://www.youtube.com/watch?v=fNokPiGfviM) 1.0M |

Context from the earlier team file (`playbook-1116/research.md`, SEEN by Research 11/16): Deep Look "These Face Mites Really Grow On You" 5.7M; Brave Wilderness; Animalogic; MinuteEarth.

**Patterns across the 8 (ANALYSIS):**
- **Character or personality carries the views, not the fact alone.** NHS gives named characters a sketch. Casual Geo uses the host's voice. Headlamp Guy and Zoozle give the protagonist stakes.
- **Second-person stakes plus escalation** ("first… then… after 30 minutes…") is the "would you survive" engine.
- **Small channels that broke out did it on long-form story episodes, not on Shorts.** Headlamp Guy (16K) has Shorts at 559 but one long-form at 1.47M. Zoozle (35.6K) has long-forms at a 62.5K median.

---

## 2. Do compilation long-forms built from Shorts earn watch hours here?

**Policy (both sides):**
- **Allowed:** YouTube's Thomas Kim, who runs YPP, said on Creator Insider that compiling your own clips is fine, and asked creators to say "this is a compilation of my clips" in the description ([video](https://www.youtube.com/watch?v=YPrCfgbX71E); summary on [vi.ki](https://youtube.vi.ki/reaction-videos-and-compilations)). Watch hours from public long-form count toward the 4,000 ([YouTube blog](https://blog.youtube/news-and-events/youtube-monetization-qualified-watch-hours-shorts-views/)).
- **Risk:** the July 2025 "inauthentic content" policy targets "slideshows that all have the same narration" and "narrative stories with only superficial differences" (Rene Ritchie, [Mythbuster](https://www.youtube.com/watch?v=uM4M8BzrT4E); policy page [1311392](https://support.google.com/youtube/answer/1311392)). Review is **channel-level**. Our Shorts are templated still-image scenes with the same voice, so a compilation of them adds to that risk at review time (ANALYSIS).

**Evidence that compilations work:**
- NHS compilations reach 114K–4.3M (Part 1 4,300,159, 7:52). Even its weakest comp would be about 2,400× our long-form median of 48.
- Zack D's compilation drew 3.1M at 27 min. Rough math (ANALYSIS, retention unknown): 3.1M × even 3 min ≈ 155K hours.
- Headlamp Guy's "Full Movie" of its own parts got 67K, inside the range of its parts.
- Reddit creators report own-Shorts compilations as safe and sometimes their best videos (anecdote, [r/PartneredYoutube](https://www.reddit.com/r/PartneredYoutube/comments/1ls4ci0/do_compilations_of_your_own_videos_count_as/)).

**Evidence that they don't:**
- In every case, the compilation pulled **far below the same channel's normal output**:
  - NHS: 114K–4.3M vs a Shorts median of 4.25M.
  - Zack D: 3.1M vs a long-form median of 5.5M.
  - Zoozle: 81-min comp at 1,279 views two days in, vs a 62.5K median.
- Compilations ride an audience that already exists. NHS had 6M subs and characters people search for.
- **We have no long-form audience to ride.** Our long-forms get 48 views median (SEEN, n=13). 99.3% of viewers are new and 0% are regular (TEAM, Studio). Shorts send at most 0.49% of viewers to long-form (TEAM, research 100).
- MASTER_ORDERS line 216 currently bans "a stitch, compilation, recut of posted Shorts".

**Verdict (ANALYSIS):**
- A plain stitch of our existing Shorts would likely get our usual ~50–200 views. At ~1–2 min AVD that's about 1–7 hours, so it won't move 4,000.
- **What does match Moondog88's "made in short format" idea and has evidence is the Headlamp Guy model:**
  - Write **one new scripted long story** (8–12 min).
  - Release it first as **numbered parts**: 61–75 s on TikTok (Rewards-eligible), 15–18 s teasers on YouTube.
  - Then post the **full episode** on YouTube with new connective narration.
- That's "built from short-format pieces" without being a re-upload of posted Shorts, and it clears the inauthentic-content bar.
- Separately, **one disclosed "best of" compilation is a cheap test** if Moondog88 lifts the ban. It needs new bridging narration and a ranking spine (see `compilation-test-plan-v0.md`), with the expectation of low views. Judge it at 72 h against our 48-view long-form median.

---

## 3. Why our videos feel boring (our data vs the winners)

| # | Problem | Our evidence | Winner contrast |
|---|---|---|---|
| 1 | **They're animated slideshows, not scenes.** A stick-figure Meatball stands beside a still creature picture while words pop. Nothing *happens* to anyone. | Frame sheets of our top Shorts (`/workspace/review-1116/`): the same pose for 5–10 s at a time. **53.7% swipe away** (Studio 28d). Engaged views are 35.9K of 81.8K Shorts views (TEAM) | NHS: a dialogue sketch with a new pose or scene every 1–2 s. Casual Geo: a caption beat every ~3 s that escalates |
| 2 | **Meatball narrates; he's never in danger.** "Would Meatball Survive?" never shows him trying to survive. | WMS Shorts median 1,123.5 (n=4) is about the same as the bug median (TEAM). No WMS Short reached 1,500 | Headlamp Guy, Zoozle and Casual Geo all put a protagonist (or "you") through an escalating ordeal |
| 3 | **Titles give the answer away, and they're long.** | "Are Daddy Longlegs the Most Venomous Spiders?" **2,400** vs the re-make "Daddy Longlegs Aren't the Most Venomous Spiders" **1–2** (SEEN). Titles run ~80–100 chars with "(Things Living In Your House #46)" tags | Winners are 4–9 words and ask or threaten: "What Happens When You Are Shot" |
| 4 | **No reason to come back.** | 99.3% new / **0.0% regular** viewers. All "videos growing your audience" are rated Low. **0.27 comments and 0.14 shares per 1,000 views** (TEAM) | NHS's named cast gets its own compilations and merch. Headlamp Guy hides a recurring Easter egg |
| 5 | **TikTok cuts are padded.** 17 s scripts get stretched to 61–75 s. | TikTok median 233 (SEEN, n=109). Over 60 s: median 221 (n=91). 60 s or less: median 359.5 (n=18). **News/search-led posts: median 3,049 (n=7)**, e.g. FAA 17,600. House centipede 461 (n=8) | Casual Geo's 59 s survival timeline uses the whole minute to escalate. Headlamp Guy's 96–124 s parts are story chapters |
| 6 | **Long-forms promise lists, not stories.** | "Weird Animal Facts…" 11.0% viewed, 1.82% CTR. "3 Bugs…" 42.7% viewed, 5.44% CTR. Long-form AVD 1:30 (TEAM) | Zoozle/What If: one subject and one arc ("born → dies", "hour by hour") |
| 7 | **Volume bursts.** | 10 TikToks posted Nov 16 (median 32.5 so far, still young) vs a usual 3/day. 3 YouTube Shorts a day already, and the earlier analysis found no cadence effect (TEAM, research 100, ~166 comparisons) | Not a proven harm. Watch whether the 11/16 batch stays low at 48 h |

---

## 4. Change list, ranked by expected impact

| Rank | Change | 1-line reason | Source |
|---|---|---|---|
| 1 | **Turn "Would Meatball Survive?" into a serialized cartoon *story* show.** Meatball is *in* the danger, with a day/hour counter ("Hour 1 in a bed-bug hotel room"). One new 8–12 min episode a week, released first as 4–6 numbered parts. | It's the only format where a channel at our Shorts level (559 median) got 73K-median long-forms and a 1.47M breakout | Headlamp Guy tabs (SEEN); What If "Hour by Hour" 1.0M |
| 2 | **Long-form = a new scripted episode built from short-format parts** (parts → full episode with new bridging narration and a recap), *not* a stitch of already-posted Shorts. Add "Full story built from Parts 1–6" in the description. | It matches Moondog88's short-format approach, avoids the inauthentic-content flag, and Zoozle/Headlamp show scripted episodes win | Thomas Kim on Creator Insider; policy 1311392; Zoozle median 62.5K |
| 3 | **Move from slideshow to sketch:** every 1–2 s something moves or happens; at least 2 lines of character dialogue; joke first, sourced fact as the punchline; end on a real photo or footage of the creature. | Our 53.7% swipe-away vs NHS's sketch format at a 4.25M median | Studio 28d (TEAM); NHS frame sheet (SEEN) |
| 4 | **A recurring cast with running gags:** Meatball (protagonist), Noodle and Sauce (already approved, action-only gags), plus **one recurring "creature host" per series** (e.g. a talking house centipede) who never states a motive as fact. | 0% returning viewers. Named casts drive return viewing and their own compilations | Studio audience (TEAM); NHS Kevin/Lisa/Batrick comps (SEEN); MASTER_ORDERS line 85 |
| 5 | **Hook formula A (YouTube):** a question title of 4–8 words ("Are Daddy Longlegs Venomous?"), never the answer. Drop series tags from titles (put them in the description or playlist). | The question title got 2,400 vs the answer title's 1–2 on the same topic | Our tab (SEEN) |
| 6 | **Hook formula B (survival):** in second 0–1, "You have [time] before [danger]" or "You wake up in [place]… [creature] is already here", then escalate every ~5 s ("first… then… by hour 3…"). | This is the Casual Geo and Infographics survival engine | Casual Geo 7.9M Short (SEEN); MakeViral breakdown |
| 7 | **TikTok: one-minute+ cuts are story chapters or search answers, not stretched facts.** Open with the searched phrase on screen ("house centipede in bathroom"). Topical/news-search posts are allowed when an animal angle is real. | News/search posts have a 3,049 median vs a 221 overall median for over-60 s posts | Our TikTok tab (SEEN); MASTER_ORDERS line 151 (Rewards pays over 1 min) |
| 8 | **Stay in the winning topic lane:** house bugs and spiders, plus survival framing. No case files, conspiracies or generic "other animals". | House bug/spider median 1,138; other animals 667; case files 57.5 | analytics.md (TEAM) |
| 9 | **Fix QA:** remove debug overlays; don't re-post a topic we already posted under a new file; check the 0–11-view Shorts for restrictions. | The 1–2-view re-make had a burned-in debug label; YouTube cut reach for non-original re-uploads on Oct 1 | Frame sheet (SEEN); Social Media Today (in research.md §2) |
| 10 | **Every Short links to the newest episode** (Related video plus a pinned comment). Shorts parts end on a cliffhanger ("Part 3 → full episode linked"). | Cheap. YouTube's own 3-step Shorts→long-form advice. The current 0.49% hand-off is low, so don't plan hours on it | YouTube Blog 7/14/2026 (TEAM cite); research 100 |
| 11 | **One test compilation, only if Moondog88 lifts the ban:** "Every Bug in Your House, Ranked" with new narration, disclosed as a compilation. Expect a low count and read it at 72 h. | The upside is real for channels with an audience; we have none on long-form yet | §2 above |
| 12 | **Posting:** keep Moondog88's 3 YouTube Shorts a day. **Cap TikTok at about 3 a day** (not 10). Long-form episode on Wed or Thu at 4–5 PM ET. | No cadence effect on YouTube; 4 PM ET is the audience peak; avoid TikTok bursts | research 100; Metricool heatmap (TEAM) |

**Watch-hour math for context:** 4,000 h at a 10-min episode with 30% viewed (3 min a view) is about 80,000 views. One Headlamp-style breakout does it; our current pace (about 0.4–0.9 h/day, TEAM tracker) doesn't.

---

## 5. Ten ready-to-use Short concepts

Every fact below is quoted from the linked source, and every safety line keeps its condition. Each runs as a 15–18 s YouTube cut plus a 61–75 s TikTok "chapter". Concepts 2, 5 and 7 can open the first serialized episode, "Would Meatball Survive a Night in a Bed-Bug Hotel?"

| # | Title | 1 s hook line | Premise | Fact & source |
|---|---|---|---|---|
| 1 | Are Daddy Longlegs Venomous? | "Three totally different bugs are ALL called daddy longlegs." | Meatball hosts a cartoon line-up: harvestman, cellar spider and crane fly each claim the name, and Sauce knocks one over. Reveal: harvestmen have no venom, and the cellar spider's isn't special. | Burke Museum: three unrelated groups; "Harvestmen… have no venom of any kind"; pholcid venom "nothing special" ([page](https://www.burkemuseum.org/static/spidermyth/myths/daddyvenom.html)) |
| 2 | Why Didn't You Feel That Bite? | "Something bit you last night and you didn't feel a thing." | Hour 1 of the bed-bug hotel: Meatball sleeps while a cartoon bug "numbs" him. Wake-up gag. | CDC: bed bugs inject fluids "(anesthetic and anticoagulant) that prevents a person from feeling the bite" ([CDC](https://www.cdc.gov/bed-bugs/about/index.html)) |
| 3 | Bed Bugs in a Five-Star Hotel? | "You paid $600 a night. The bed bugs stayed free." | Meatball checks into a fancy suite; Noodle eats the room-service food. Myth-bust: being clean doesn't decide it. | CDC: "Bed bugs are in five-star hotels… How clean a place is does not determine whether bed bugs are present." (same page) |
| 4 | How Far Do Bed Bugs Crawl? | "Your bed bug can walk the length of a basketball court tonight." | A race gag down the hotel hallway. Must keep the condition. | CDC: "can travel over 100 feet in a night but tend to live within 8 feet of where people sleep" (same page). *Spoken line keeps "but tend to live within 8 feet".* The basketball-court image needs a length check by Research first |
| 5 | Bites Showed Up 2 Weeks Later? | "The bites can show up two WEEKS after the bug." | A calendar gag: Meatball shrugs off Day 1 and panics on Day 14. | CDC: bite marks "may take as long as 14 days to develop in some people" (same page) |
| 6 | Does Washing Kill Bed Bugs? | "Your washing machine isn't the weapon you think." | Meatball triumphantly washes the sheets, and the bugs are fine. Hand-off to the dryer. Do **not** end by saying it saved him. | EPA: dryer "at high temperatures for 30 minutes… (just washing will generally not kill bed bugs)" ([EPA IPM](https://www.epa.gov/bedbugs/controlling-bed-bugs-using-integrated-pest-management-ipm)); fact pack BB21 |
| 7 | What Does a Bed Bug Room Smell Like? | "If your hotel room smells sweet and musty… check the mattress." | Meatball sniffs around like Noodle; a checklist of signs appears. | CDC signs: exoskeletons, rusty-colored spots, "A sweet musty odor" (same page) |
| 8 | Is There a Dust Mite in Your Bed? | "Four out of five beds have something you can't see." | A microscope zoom on Meatball's pillow; Sauce sleeps on it anyway. | American Lung Association via fact pack DM5: "About 4 out of 5 homes in the United States have dust mite allergens in at least one bed" (`drafts/facts/dust-mite-bornas.md`) |
| 9 | 30 Roaches in One Tiny Case? | "This little tan capsule is 30 cockroaches." | Meatball finds the egg case under the fridge; it starts wiggling. | UC IPM via fact pack CR6: "Each egg case contains about 30 young, and a female may produce a new egg case every few weeks" (`drafts/facts/cockroach-bornas.md`) |
| 10 | Can You Outrun a Bear? | "You have about one second to decide. Don't run." | WMS: Meatball tries sprinting uphill and the bear keeps pace. Close with NPS safety guidance, condition intact. | NPS: "Bears can run as fast as a racehorse both uphill and down" ([NPS](https://www.nps.gov/subjects/bears/safety.htm)). "Don't run" must be checked against NPS's own wording before use |

Rules applied: no invented winners, no team logos or betting, safety lines keep their condition, and no ending says a tactic saved Meatball. Pets act out gags only, with no motive stated as fact. Research should re-check #4's analogy and #10's spoken advice before scripting.

---

## 6. What to check in vidIQ (for the separate browser session)

**Keywords** (record search volume, competition and overall score for each):
- daddy longlegs venomous; bed bugs; bed bug bites; how to tell if you have bed bugs; house centipede; house centipede bite; dust mites; cockroach egg; wolf spider; could you survive; would you survive; what if you; why it sucks to be born as; animal facts; bugs in your house.
- Compare question forms against statement forms for the same topic.
- Run the "Keyword Inspector" related and trending lists on "bed bugs" and "house centipede" for long-form episode titles.

**Competitors:**
- Add: Natural Habitat Shorts, Headlamp Guy, Zoozle, Casual Geographic, The Infographics Show, Life Noggin, Zack D. Films, What If, KQED Deep Look.
- Record views per hour on their last 10 uploads and their upload cadence.

**Outliers:**
- Use vidIQ "Outliers" filtered to channels **under 50K subs** in Pets & Animals / Science, with video multiplier ≥5× channel average, for these themes: "would you survive", "born as", "bugs in your house", "bed bugs", "hour by hour".
- Export titles, lengths and thumbnails.

**Our own channel:**
- vidIQ score per video.
- The best posting time by vidIQ (compare it with the Metricool 4 PM ET result).
- The "Daily Ideas" list for bug topics.
- Tag and SEO audit of the 13 long-forms (note our 80–100 char titles).

**Comparison to make:** whether the "Would X Survive" keyword out-searches "Things Living In Your House", which decides the series names.

---

## Gaps / not verified

- Spoken first lines of competitor videos. I saw frames and titles only, apart from Casual Geo's on-screen captions.
- Zoozle's Shorts tab failed to load.
- TikTok competitor video-level views weren't pulled.
- TikTok 30-day views and Creator Rewards status for @meatballmyths still need a Studio screenshot.
- The YouTube Earn card is from 11/11 (10 qualified hours).
- The Zoozle compilation is only 2 days old.
