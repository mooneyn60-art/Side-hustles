# Oh Meatball / Would Meatball Survive? — Deep-research playbook (research)

Prepared by Social: Research & Fact-check · checked Mon Nov 16, 2026, 2:02–2:20 PM ET (UTC-5) · free tools only (WebSearch, WebFetch, curl, yt-dlp public data). Nothing posted, messaged or committed.

**Labels:** `VERIFIED` = read on the linked page this session. `UNVERIFIED` = could not confirm. `ANALYSIS` = my inference from verified data, not a sourced fact. `ESTIMATE` = third-party benchmark, not an official number.

**Access limits hit (stated, not guessed):**
- YouTube rate-limited this box (HTTP 429 / "Sign in to confirm you're not a bot") partway through. **Spoken first lines from transcripts could not be pulled for any video.** Every hook quote below is the real **title** plus the real **description opener** taken from the watch page. Spoken openers are UNVERIFIED.
- Three top-hit watch pages stayed blocked after a retry. For those, the view count is the rounded figure on the channel's Videos/Shorts tab, labelled "tab count".
- TikTok profile pages returned stats for only 4 of the 9 creators. For the rest, the handles I tried (`@zackdfilms`, `@bravewilderness`, `@brave.wilderness`, `@casualgeographic`, `@casual.geographic`, `@deeplook`, `@kqeddeeplook`) were empty, impostors or tiny accounts, so those creators' official TikTok handles are UNVERIFIED. I could not scrape any TikTok video-level hits.

---

## 0. Baseline: our own channels (checked Nov 16, 2026)

| Metric | Value | Source |
|---|---|---|
| YouTube subscribers | 1,010 | yt-dlp read of https://www.youtube.com/channel/UCw98RQD81t_339LX5EJqcrg/shorts |
| YouTube Shorts | 86 public; ~76,876 lifetime views summed from tab counts (median 1,000; best 2,400) | same |
| YouTube long-form | 13 public; ~1,040 lifetime views (median 48; best 219, "3 Bugs in Your House You Should Never Kill (And 4 You Must)"); median length 8:17 | https://www.youtube.com/channel/UCw98RQD81t_339LX5EJqcrg/videos |
| Long-form watch hours, upper bound | ≤123 h (views × full duration; real figure is lower) | ANALYSIS from the above |
| TikTok @meatballmyths | 9,316 followers · 3,231 likes · 109 videos, from the profile page JSON | https://www.tiktok.com/@meatballmyths |

The TikTok numbers come from one scrape of the public profile. Confirm them in TikTok Studio, since likes below followers is unusual (UNVERIFIED).

---

## 1. Top channels in the niche (bug, animal-myth and survival/"what if")

Selection: the largest active English channels I found covering bugs, animal facts and myths, or survival scenarios. Subscriber counts come from yt-dlp channel reads on Nov 16, 2026. Cadence is the last 15 uploads (long + Shorts) in each channel's public RSS feed (`https://www.youtube.com/feeds/videos.xml?channel_id=…`). Lengths come from the channel tab durations. Thumbnail notes come from my viewing of the top hit's `i.ytimg.com/vi/<id>/hqdefault.jpg`. "Why it hit" is ANALYSIS.

### 1.1 Brave Wilderness (Coyote Peterson): bugs, stings, bites
- Channel: https://www.youtube.com/@BraveWilderness · 21.8M subs · TikTok handle UNVERIFIED
- **Format:** host-led field and studio "challenge" episodes (STUNG / BITTEN by X), plus a few Shorts.
- **Length:** top hits run 8:02 to 19:15. Recent uploads run about 12–18 min.
- **Cadence:** 15 uploads from Aug 25 to Nov 14, 2026 ≈ **1.3/week**.
- **Thumbnail:** macro of the creature on a bright sky-blue background, held in forceps right next to skin, with the channel badge. No text on the top hit.
- **Hook pattern:** ALL-CAPS verb + creature + "!" (STUNG / BITTEN / "Will They BITE?!"). Recent titles: "STUNG by a Tiger Bee!", "BITTEN by a Vampire Bat!", "DOUBLE STING! Cow Killer vs. Tarantula Hawk".
- **Top 3 (views as shown on the watch page, Nov 16, 2026):**
  1. [STUNG by a COW KILLER!](https://www.youtube.com/watch?v=EF-oSVCCqzU): 86,650,435 views, Sep 20, 2016. Description opener: "On this episode of Breaking Trail, Coyote is stung by an infamous COW KILLER…the Velvet Ant!"
  2. [BLOODWORMS - Will They BITE?!](https://www.youtube.com/watch?v=o7aM5gU8mFY): 80,876,670 views, Jul 19, 2017. Description opener: "Watch Bloodworms Part 2!"
  3. [EXTREME Cactus Attack!](https://www.youtube.com/watch?v=dJzTse9Dsaw): 79,814,014 views, Oct 14, 2016. Description opener: "Please SUBSCRIBE - http://bit.ly/BWchannel"
- **Why it hit (ANALYSIS):** one concrete promise of pain to a real person, a scary folk name ("cow killer") and a question the viewer has to stay to answer. **Safety:** this is the format we must NOT imitate. Self-stings are unsafe to copy, so we keep our "would Meatball survive" framing hypothetical and sourced.

### 1.2 Casual Geographic: animal myths and "weird animal" lists, comedic host
- https://www.youtube.com/channel/UC5Yo88QF-chdugJbAnB2tUw · 4.33M subs · TikTok UNVERIFIED
- **Format:** host-on-camera listicles over stock footage and diagrams. Slang-heavy comedy.
- **Length:** top hits run 7:35 to 15:37. Recent uploads run about 15–38 min.
- **Cadence:** 15 uploads from Mar 27 to Nov 13, 2026 ≈ **0.5/week**. Infrequent but big.
- **Thumbnail:** split image with the host's face reacting next to a bizarre animal photo or anatomical diagram. No text.
- **Hook pattern:** pop-slang superlative + "animals that…" ("Animals that Got the Middle Finger from Evolution", "Animal Diseases that Belong in a Horror Movie"), or a conspiratorial angle ("…Zoos Don't Want You To Know").
- **Top 3 (watch page, Nov 16):**
  1. [Animals that Got the Middle Finger from Evolution](https://www.youtube.com/watch?v=s5p6vGuWqeQ): 17,310,581 views, Aug 23, 2021
  2. [Why I'd Throat a Cactus Before I Go In The Ocean](https://www.youtube.com/watch?v=KpxYhv0NPDM): 13,243,904 views, May 5, 2021. Description opener: "Subscribe, turn on ALL post notifications and make sure to drink water and hug your mother."
  3. [Animal Secrets Zoos Don't Want You To Know](https://www.youtube.com/watch?v=nvika2cFiq0): 12,352,178 views, Jun 1, 2021
- **Best Shorts (tab count):** "You could've FaceTimed an Eel...." 8.6M; "What if You Ate The Most Poisonous Animal in the World?" 7.9M ([channel Shorts tab](https://www.youtube.com/channel/UC5Yo88QF-chdugJbAnB2tUw/shorts)).
- **Why it hit (ANALYSIS):** a personality-driven voice plus "nature is cursed" lists. The "what if you ate…" Short is the closest format to "Would Meatball Survive?".

### 1.3 Ze Frank, "True Facts": comedic narrated animal facts
- https://www.youtube.com/@ZeFrank · 4.28M subs · TikTok UNVERIFIED
- **Format:** deadpan comedic voiceover on licensed nature footage ("True Facts: …").
- **Length:** 2–4 min classics. Recent episodes run 7–16 min.
- **Cadence:** 15 uploads from May 26 to Oct 21, 2026 ≈ **0.7/week** (mixed with short clips).
- **Thumbnail:** clean single-subject photo. The top hit is a staged teddy-bear "surgery" tableau.
- **Hook pattern:** "True Facts About The [Animal]" / "True Facts: [weird behaviour]".
- **Top 3 (watch page, Nov 16):**
  1. [Teddy Has An Operation](https://www.youtube.com/watch?v=AdYaTa_lOf4): 44,162,004 views, Apr 26, 2013 (non-animal sketch)
  2. [Sad Cat Diary](https://www.youtube.com/watch?v=PKffm2uI4dk): 32,937,562 views, May 9, 2013. Description opener: "The diary of sad cats everywhere :("
  3. [True Facts About The Angler Fish](https://www.youtube.com/watch?v=Z-BbpaNXbxg): 23,964,422 views, Dec 27, 2012
- **Best Shorts (tab):** "Pigeons DON'T bob their heads" 1.3M ([Shorts tab](https://www.youtube.com/@ZeFrank/shorts)).
- **Why it hit (ANALYSIS):** a voice and comedy layer on top of real biology. A myth-bust Short ("Pigeons DON'T bob…") is a direct analogue for us.

### 1.4 Animalogic: animal explainers
- https://www.youtube.com/@Animalogic · 2.15M subs · TikTok **@animalogic: 694,300 followers, 7.7M likes, 1,110 videos** (profile JSON, Nov 16)
- **Format:** narrated documentary explainers plus heavy Shorts output.
- **Length:** top hits run 7:04 to 11:41. Recent uploads run 14–27 min.
- **Cadence:** 15 uploads from Oct 13 to Nov 16, 2026 ≈ **3.1/week**.
- **Thumbnail:** one bold animal image with 1–2 huge white words ("OCTOPUS ESCAPE").
- **Hook pattern:** "[Animal]: The [superlative role]" ("Sand Cat: The King of the Desert"; "Coconut Crab: A 3-Foot Land Crab That Eats Birds").
- **Top 3 (watch page, Nov 16):**
  1. [Octopuses are the World's Greatest Escape Artists (Ft. PhilosophyTube)](https://www.youtube.com/watch?v=wSn7CJ0cNZ4): 13,559,219 views, May 20, 2016
  2. [Sand Cat: The King of the Desert](https://www.youtube.com/watch?v=y8kTYCex8RU): 12,625,906 views, Mar 6, 2020. Description opener: "Sand Cats may not look the part, but they are built to handle the extremes of one of the harshest environments on Earth."
  3. [Fishing Cat: The Cat That Hunts Underwater](https://www.youtube.com/watch?v=cso87inf29Q): 10,748,336 views, Mar 20, 2020. Description opener: "Life in the mangroves of South Asia is difficult, but there's one creature in this swamp that's defying the odds, and our expectations at the same time."
- **Best Short (tab):** "What To Do If You Find a Snapping Turtle on the Road" 3.8M, a practical safety how-to.
- **Why it hit (ANALYSIS):** survival-in-extremes framing ("built to handle the extremes"), and its top Short is useful safety advice.

### 1.5 AntsCanada: bugs, ant-keeping storytelling
- https://www.youtube.com/@AntsCanada · 7.06M subs · TikTok **@antscanada: 1.7M followers, 17.6M likes, 1,100 videos**
- **Format:** first-person serialized "colony saga" with seasons/episodes (e.g. "S8: E5").
- **Length:** top hits run 15:01 to 29:08. Recent uploads run 21–56 min.
- **Cadence:** 15 uploads from Apr 26 to Oct 11, 2026 ≈ **0.6/week**. A recent upload is titled "Why I Have to Stop" (content not checked).
- **Thumbnail:** extreme macro of a swarm with a big red arrow and the logo.
- **Hook pattern:** first person + threat or experiment ("My Fire Ants Are Planning an Escape", "I Gave My Fire Ants A Chicken Head", "7 ANT COLONIES in 1 ARENA: ANT WAR or JOIN FORCES?").
- **Top 3 (watch page, Nov 16):**
  1. [My Fire Ants Are Planning an Escape](https://www.youtube.com/watch?v=lrnDOovsmfg): 48,025,377 views, Sep 11, 2016. Description opener: "My fire ants are planning a great escape!"
  2. [I Gave My Fire Ants A Chicken Head](https://www.youtube.com/watch?v=pFpkfbqepP4): 18,258,132 views, Dec 29, 2018
  3. [7 ANT COLONIES in 1 ARENA: ANT WAR or JOIN FORCES?](https://www.youtube.com/watch?v=RydlJtjgovg): 15,327,390 views, Oct 16, 2021. Description opener: "I took seven ant colonies and placed them into a single arena."
- **Why it hit (ANALYSIS):** insects given personalities and stakes, an unanswered "what happens next" question, and recurring characters. **House rule:** "ANT WAR" style vs-framing must not name invented winners.

### 1.6 Zack D. Films: 3D-animated "how it works / what happens if" Shorts
- https://www.youtube.com/@zackdfilms · 29.7M subs · TikTok handle UNVERIFIED (`@zackdfilms` returned a 24-follower account)
- **Format:** 20–40 s 3D-render explainers. Almost entirely Shorts (4,190 on the tab vs 12 long-form).
- **Length:** 24–30 s on the checked hits.
- **Cadence:** 15 uploads from Nov 13 to Nov 16, 2026 ≈ **5/day**.
- **Thumbnail/first frame:** a realistic 3D close-up of the body or object (stitched wound).
- **Hook pattern:** "How [X] Works 😯" / "The Reason [X] Looks Weird 😮" / "Could [X] …? 🤔". Titles end in a reaction emoji.
- **Top 3 (Nov 16):**
  1. [How Stitches Work 😯](https://www.youtube.com/shorts/ttuKeS5k4Uo): **tab count 255M** (watch page blocked)
  2. [How Splinters Get Unstuck 😲](https://www.youtube.com/shorts/yGw0nhlUtkQ): 216,833,898 views, Mar 5, 2024, 30 s
  3. [The Reason The McFlurry Spoon Looks Weird 😮](https://www.youtube.com/shorts/rRAmNz6G3Tk): 167,162,783 views, Dec 19, 2022, 24 s
- **Why it hit (ANALYSIS):** body-horror curiosity resolved in under 30 s, a loop-friendly ending and very high volume. Its top hits are not animal content; it's included as the benchmark for the "what happens if" Short format.

### 1.7 The Infographics Show: survival / "what if" scenarios
- https://www.youtube.com/@TheInfographicsShow · 15.5M subs · TikTok **@theinfographicsshow: 1.7M followers, 32.4M likes, 1,323 videos**. Bio lists a business email (`tiktok@darkmatterdesign.com`), showing the norm of a public sponsor contact.
- **Format:** flat 2D animation with narration, plus "What If / Who Would Win / How to survive" Shorts.
- **Length:** top hits run 7:04 to 17:57. Recent uploads run 16–36 min.
- **Cadence:** 15 uploads from Nov 8 to Nov 15, 2026 ≈ **2/day**.
- **Thumbnail:** bright cartoon scene with a yellow/red text banner ("WHAT HAPPENS: WHEN YOU DIE?").
- **Hook pattern:** "What Happens When…", "What If You…", "X vs Y - Who Would Win?"
- **Top 3 (Nov 16):**
  1. [What Happens When You Die?](https://www.youtube.com/watch?v=vLaErMfgJ8Q): 27,409,743 views, Feb 21, 2018. The description opens with a sponsor read: "Start your free trial today at Squarespace.com…"
  2. [Russian Sleep Experiment - EXPLAINED](https://www.youtube.com/watch?v=8eq2vGEEbB4): **tab count 22M** (blocked)
  3. [How SEAL Team Took Down Osama bin Laden (Minute by Minute)](https://www.youtube.com/watch?v=knjliFs3gR8): 20,736,365 views, Aug 10, 2022
- **Animal-relevant Short (tab):** "Dumb Ways To Die" 8.9M.
- **Why it hit (ANALYSIS):** second-person stakes ("you") plus a minute-by-minute escalation. That is close to our "Would Meatball Survive?" spine. The top-hit description also shows a sponsor read in the first description line.

### 1.8 Deep Look (KQED / PBS): bug macro science
- https://www.youtube.com/@KQEDDeepLook · 2.4M subs · TikTok UNVERIFIED
- **Format:** ultra-macro cinematography with calm narration. Classic episodes are 3–5 min. Now heavy on Shorts.
- **Length:** top hits run 3:18 to 4:36. Recent long-forms run 5–20 min.
- **Cadence:** 15 uploads from Sep 30 to Nov 16, 2026 ≈ **2.2/week** (mostly Shorts).
- **Thumbnail:** a single photographic macro (mosquito proboscis in skin) with only a small logo.
- **Hook pattern:** "How [bug] [does gross/amazing thing to you]" ("How Mosquitoes Use Six Needles to Suck Your Blood").
- **Top 3 (Nov 16):**
  1. [How Mosquitoes Use Six Needles to Suck Your Blood | Deep Look](https://www.youtube.com/watch?v=rD8SmacBUcU): 24,587,913 views, Jun 7, 2016
  2. [The Ladybug Love-In: A Valentine's Special | Deep Look](https://www.youtube.com/watch?v=c-Z6xRexbIU): 21,006,383 views, Feb 9, 2016. Description opener: "Ladybugs spend most of their lives alone, gorging themselves on aphids."
  3. [How Lice Turn Your Hair Into Their Jungle Gym | Deep Look](https://www.youtube.com/watch?v=Yb26BBvAAWU): **tab count 17M** (blocked)
- **Best Shorts (tab):** "The Undying Hydra" 14M; "These Face Mites Really Grow On You" 5.7M. That second one is on the same topic as our dust-mite and face-mite scripts.
- **Why it hit (ANALYSIS):** "on YOUR body" bug content (mosquito, lice, face mites) plus visuals nobody else has. This is our closest topic match.

### 1.9 MinuteEarth: animal "why" explainers
- https://www.youtube.com/@MinuteEarth · 3.34M subs · TikTok **@minuteearth: 1.2M followers, 26.7M likes, 614 videos**
- **Format:** hand-drawn-style animation with a fast narrated "why" answer.
- **Length:** 2:25–2:39 on the top hits. Recent uploads run 3–8 min.
- **Cadence:** 15 uploads from Oct 2 to Nov 16, 2026 ≈ **2.3/week**.
- **Thumbnail:** cartoon animal plus 4–5 words of large text, with one word in red ("WHY IT SUCKS TO BE A MALE HYENA").
- **Hook pattern:** "Why [Animal fact framed as problem]?"
- **Top 3 (Nov 16):**
  1. [The World's Largest Nuclear Weapon (ft. Stephen Fry) #shorts](https://www.youtube.com/shorts/nGutkWaXDUs): **tab count 23M**, Jul 22, 2021 (non-animal). Description opener: "How devastating is the world's largest nuclear weapon? Stephen Fry explains."
  2. [Why It Sucks to Be a Male Hyena](https://www.youtube.com/watch?v=PBCNWmU5apE): 19,145,683 views, Jul 19, 2017. Description opener: "Thanks to spotted hyenas' unusual social structure, males experience a tough life of solitude, harassment, and deprivation."
  3. [Why Do Animals Eat Their Babies?](https://www.youtube.com/watch?v=8xVgAULDwNE): 17,327,380 views, Oct 20, 2016. Description opener: "Sometimes, it makes sense for critters across the animal kingdom to chow down on their own young."
- **Why it hit (ANALYSIS):** a dark "why" question answered by real science in about 2.5 min, the same structure as our myth-bust Shorts.

### 1.10 Cross-channel patterns (ANALYSIS from the verified data above)
1. **Second-person or personal stakes win:** "Suck *Your* Blood", "*Your* Hair", "*I'd* Throat a Cactus", "What Happens When *You* Die". This backs our "Your kitchen / Your bed / Would Meatball survive" framing.
2. **One creature, one visceral verb:** STUNG, BITE, Escape, Suck, Eat Their Babies.
3. **On-body bugs** (mosquito, lice, face mites, splinters) beat abstract bugs. Our bed-bug, dust-mite and roach series sit right in that lane.
4. **Thumbnails:** either an ultra-macro photo with no text (Brave, Deep Look, AntsCanada) or 1–5 huge words with one red word (Animalogic, MinuteEarth, Infographics).
5. **Cadence splits:** Shorts-first channels post daily or more (Zack D 5/day, Infographics 2/day). Personality long-form channels post weekly or less (Casual Geographic 0.5/wk, Ze Frank 0.7/wk).

---

## 2. 2026 algorithm signals

| # | Signal | Platform | Label | Source |
|---|---|---|---|---|
| 1 | Since **Aug 24, 2026**, public views count "from the first frame" across all formats. The old definition is now "engaged views" ("clicking to watch or watching past the initial seconds"), which still determines Shorts revenue sharing. | YouTube | **OFFICIAL** | https://blog.youtube/inside-youtube/engaged-views-youtube-explained/ ; Creator Insider video https://www.youtube.com/watch?v=2FBzExbYHxg |
| 2 | **Oct 1, 2026** Shorts update: recommendations "further prioritize original content and reduce the reach of content re-uploaded from other creators without adding anything of your own." Aggregator channels "will likely see less distribution within the Shorts feed." | YouTube | **REPORTED** (quotes YouTube's announcement) | https://www.socialmediatoday.com/news/youtube-updates-shorts-algorithm-to-put-more-focus-on-original-content/831976/ |
| 3 | Same update: remixes must add value, "not just VO descriptions of what's happening on screen, minor technical edits, or template-based bulk changes" (Rene Ritchie, Creator Insider). Channels that shift to original content get reach "re-evaluated". | YouTube | **REPORTED** | https://www.searchenginejournal.com/youtube-original-shorts-reposted-clips-reach/591774/ |
| 4 | Shorts goal is viewer satisfaction. "Viewed vs swiped away" is the in-Studio metric; "grabbing people in the first few seconds tends to be important"; length should be whatever "you need to tell your story". | YouTube | **OFFICIAL** (YouTube's own video; undated in my read, so it may predate 2026) | https://www.youtube.com/watch?v=n3jsYK_-aRU |
| 5 | Non-original Shorts (reuploads, unedited clips, compilations) produce **ineligible** views for revenue. | YouTube | **OFFICIAL** | https://support.google.com/youtube/answer/12504220?hl=en |
| 6 | For You ranks on user interactions (likes, shares, follows, comments), video info (captions, sounds, hashtags) and lower-weighted device settings. "Whether a user finishes watching a longer video from beginning to end" is a strong signal. "Neither follower count nor whether the account has had previous high-performing videos are direct factors." No duplicates or spam, and "videos that have just been uploaded or are under review… may be ineligible." | TikTok | **OFFICIAL** (Newsroom post; flysub reports it dates to Jun 18, 2020 and is unchanged) | https://newsroom.tiktok.com/en-us/how-tiktok-recommends-videos-for-you |
| 7 | "For You feed Eligibility Standards" were added to the Community Guidelines (released Aug 25, 2026, effective Sep 24, 2026). FYF-ineligible content includes unoriginal, shocking/graphic, mature, and dangerous activities or challenges. | TikTok | **REPORTED** (I did not open the guidelines page itself) | https://www.flysub.io/blog/tiktok-algorithm-2026-what-tiktok-says-officially |
| 8 | Creator Rewards "Additional Reward" favours "specialized content that demonstrates your expertise in a niche". Clickbait, low-quality slideshows and split screens are ineligible. | TikTok | **OFFICIAL** | https://www.tiktok.com/creator-academy/en/article/creator-rewards-program |
| 9 | Mar 10, 2026: TikTok is testing an AI-generated-content slider in "Manage topics", so viewers can dial AIGC down. | TikTok | **OFFICIAL** | https://newsroom.tiktok.com/tiktok-ssa-shares-more-ways-to-spot-shape-and-understand-ai-generated-content?lang=en-ZA |
| 10 | "No confirmed ranking changes Aug–Sep 2026." Completion and watch time come first, then saves and shares, then likes. US FYF runs on an "Oracle-retrained, US-only model from April". | TikTok | **REPORTED / UNVERIFIED** (secondary blog, no primary link checked) | https://www.socialpilot.co/blog/tiktok-algorithm |

**Implication (ANALYSIS):** the safety and graphic-content FYF rules (7) matter for stings, bites and bed-bug imagery. Keep gore out of the first frame and keep the house rule that safety lines say their condition aloud. Original voice plus sourced facts lines up with both platforms' originality pushes (2, 3, 5, 8).

---

## 3. Monetization

### 3.1 YouTube Partner Program: verified on YouTube Help, Nov 16, 2026
| Tier | Threshold (current) | Source URL |
|---|---|---|
| Expanded YPP (fan funding + Shopping) | 500 subs + 3 valid public uploads in last 90 days + **3,000** qualified watch hours/12 mo **or** **3M** qualified Shorts views/90 days. Available in the US (and other listed countries). | https://support.google.com/youtube/answer/13429240?hl=en |
| Full YPP (ad revenue + Premium) | 1,000 subs + **4,000** qualified watch hours/12 mo **or** 1,000 subs + **10M** qualified Shorts views/90 days. Shorts-feed watch hours don't count toward the 4,000. | https://support.google.com/youtube/answer/72851?hl=en |
| Shorts revenue share | Creators keep **45%** of their allocated Creator Pool revenue. 1 music track halves the pool allocation. | https://support.google.com/youtube/answer/12504220?hl=en |
| ⚠️ **Change on Feb 1, 2027** | New-creator ad/Premium entry rises to 1,000 subs + **8,000** watch hours/365 days **or** **20M** Shorts views/90 days. Earning from the Shorts Creator Pool will need **10M** qualified Shorts views over the trailing 90 days each month. **No change** to the 500-sub fan-funding / Shopping / Creator Partnerships tier (3,000 h or 3M Shorts views). | https://support.google.com/youtube/answer/12843009?hl=en |
| YouTube Shopping affiliate | Must be in YPP and meet "the subscriber threshold for YPP". US eligible. Not available to Made for Kids channels. | https://support.google.com/youtube/answer/13376398 ; 500-sub expansion: https://blog.youtube/creator-and-artist-stories/youtube-shopping-expansion-500-subscribers/ |

The review "typically [takes] about 1 month" (72851). Facelessfuel reports the 500-sub Shopping expansion was announced Mar 25, 2026 (REPORTED: https://facelessfuel.com/youtube-shopping-affiliate-program-requirements/).

### 3.2 TikTok Creator Rewards Program: TikTok's own pages
- **Eligibility:** 18+; **≥10,000 authentic followers**; **≥100,000 authentic video views in the last 30 days**; personal (not Business) account in good standing; a payment account in your own name. Source: https://www.tiktok.com/legal/page/global/creator-rewards-program-mx/en (terms) and https://newsroom.tiktok.com/en-us/introducing-the-new-creator-rewards-program/
- **Eligible videos:** original, **over 1 minute**, **≥1,000 For You feed views**, not a Duet/Stitch/Photo Mode, not ads or sponsored content, 1080p+ recommended. Source: https://www.tiktok.com/creator-academy/en/article/creator-rewards-program
- **Qualified views** are unique FYF views over 5 s, and the video must be uploaded after joining. Source: https://support.tiktok.com/es/business-and-creator/creator-rewards-program/creator-rewards-program (Spanish-language support page; I could not open the English version in the time available)
- **Regions:** "United States, United Kingdom, Germany, Japan, South Korea, France, Mexico, and Brazil" (Creator Academy, same URL as above).
- **Payout rate per 1,000 views:** TikTok doesn't publish one. Its terms say rewards are based on "total legitimate video views and other signals" and may be capped. **Any RPM figure is UNVERIFIED.**

### 3.3 Affiliate: Amazon Associates (US), verified Nov 16, 2026
- **Commission rates** (Fixed Standard Commission table, https://affiliate-program.amazon.com/help/node/topic/GRXPHT8U84RAYDXZ):
  - Physical Books **4.5%**: insect and spider field guides, if listed as books.
  - **3.00%**: Pets Products, Outdoors, Tools, Home, Home Improvement, Lawn & Garden, Toys.
  - Health & Personal Care **1%**.
  - All Other Categories **4%**.
- **Product mapping is UNVERIFIED.** Which category Amazon assigns to a specific UV flashlight, loupe, bug vacuum or pest trap must be checked per item. My guess: loupes and UV lights fall under Tools or Home Improvement (3%) and pest traps under Lawn & Garden (3%), but these are not confirmed.
- **Approval:** at least **3 qualified sales within the first 180 days** (personal orders don't count), or the application can be withdrawn. Social pages need "a substantive number of organic followers… (in most cases, at least 500)". YouTube and TikTok are accepted. Sources: https://affiliate-program.amazon.com/help/node/topic/G8TW5AE9XL2VX9VM ; https://affiliate-program.amazon.com/help/node/topic/G7MJTPEP9NC3YKMG
- **Cookie:** an order counts if placed within 24 h of the click (or added to cart in that session and ordered within 89 days). Purchases referred through paid or boosted ads are disqualified (Apr 14, 2026 update). Sources: https://affiliate-program.amazon.com/help/operating/policies ; https://affiliate-program.amazon.com/help/operating/compare
- **Disclosure:** YouTube requires paid-promotion disclosure under its branded-content policies (13376398). TikTok Creator Rewards excludes sponsored videos from rewards.
- **Safety and house rules:** never link indoor-use pesticides, foggers or anything an imitation could misuse. Gear links should be ID tools (loupe, field guide, UV light for scorpion spotting with its condition stated aloud), not treatments.

### 3.4 Sponsors (all figures are ESTIMATES from third parties)
| Benchmark | Figure | Source |
|---|---|---|
| ThoughtLeaders, sold integrations Aug 2024–Aug 2026 | Science & education median **$25 per 1,000 projected views** (middle half $17–36). Channels projected **under 50K views: median $37/1K**, median price **$800**. They warn that post-Aug-24 first-frame views make CPMs look cheaper (their median moved from $29.94 to $17.05 on the new count). | https://thoughtleaders.ai/blog/2026-10-20-youtube-sponsorship-cpm-by-category/ |
| Sponsorbloom | Under 10K subs: about 2K typical views, **$35–$67 per integration**, and only **6%** have a paid sponsor. Education & science CPM $20–35. "A Short usually prices at around a third of an integration." | https://sponsorbloom.com/guides/youtube-sponsorship-rates/ |
| ytcalculators | 1K–10K subs at under 500 views/video: $20–70 for a 60 s integration. | https://ytcalculators.com/blog/youtube-sponsorship-rates-small-channels/ |
| Influencer Advisory (creator *asks*, not deals) | Education median asked CPM $70 (n=12). | https://influenceradvisory.com/blog/youtube-cpm-by-niche/ |

**Outreach norms (sourced where possible):**
- Price by median recent views, not subscribers. Price = views ÷ 1,000 × CPM (Sponsorbloom, ThoughtLeaders).
- A 60–90 s integration is the standard unit, and a dedicated video costs about 2× (Sponsorbloom).
- List a business email in the bio. The Infographics Show's TikTok bio does this (observed).
- Disclose per platform rules.
- Unsourced norms (pitch decks, follow-up timing) are UNVERIFIED and left out.

---

## 4. Fastest realistic path to first dollars (math shown; inputs cited above)

| Route | Gap from today | First-dollar math | Verdict |
|---|---|---|---|
| **A. TikTok Creator Rewards** | Followers: 10,000 − 9,316 = **684 to go** (§0, §3.2). Also needs ≥100K views in the last 30 days (current 30-day views UNVERIFIED; check TikTok Studio). | Payout per 1K qualified views is **not published, so revenue is UNVERIFIED**. What we can count: each video must be over 60 s and reach 1,000+ FYF views to earn anything. | **Closest unlock.** The 684-follower gap is the only verified, measurable gap. |
| **B. Amazon Associates** | YT 1,010 subs and TT 9,316 followers clear the "≥500 organic followers" guidance. Needs 3 sales in 180 days. | Commission = price × rate. Example: a field guide at P dollars earns 0.045·P. A pet or outdoor item earns 0.03·P. **Product prices are not checked here, so dollar totals are left open.** To clear approval, 3 sales are needed. At an assumed (UNVERIFIED) 1% click-to-purchase rate, that means about 300 Amazon clicks. | **Fastest literal "first dollar"**, but tiny amounts. The link has to live in the description or bio, since Shorts and TikTok links are less visible (ANALYSIS). |
| **C. YouTube expanded YPP (fan funding + Shopping)** | 500 subs ✅. Uploads ✅. Shorts: 3,000,000 needed vs **~76,876 lifetime** (§0). Long-form: 3,000 h needed vs **≤123 h lifetime upper bound**. | At the current Shorts median of 1,000 views, 3M views in 90 days means about **3,000 Shorts in 90 days**, which isn't realistic. It takes 100 Shorts × 30K views, or 10 videos × 300K views. | **Not near-term.** |
| **D. YouTube full YPP ad share** | Today: 4,000 h or 10M Shorts views/90 d. **From Feb 1, 2027: 8,000 h or 20M** (§3.1). | Long-form 4,000 h ÷ 8.3 min median length ≈ 29,000 full watches. At the current median of 48 views per long-form video, that is out of reach before Jan 31, 2027. | **Not reachable before the Feb 1, 2027 bar doubles.** Plan for the new 8,000 h / 20M numbers. |
| **E. Sponsors** | Long-form median is 48 views. Shorts median is 1,000. | At ThoughtLeaders' under-50K median of $37/1K: 1,000 views → **$37 per integration (ESTIMATE)**. Sponsorbloom's "a Short ≈ ⅓ of an integration" puts a Short at about $12. Only 6% of under-10K channels have a paid sponsor (Sponsorbloom). | Possible but low-value. A niche-gear brand (loupe or UV-light maker) is the likeliest fit (ANALYSIS). |

**Top recommendation (ANALYSIS):**
- **First, push TikTok to 10K followers and 100K views per 30 days, then join Creator Rewards.** Use 61–90 s original myth-bust or "Would Meatball Survive?" cuts with second-person on-body bug hooks (the Deep Look / Zack D pattern), with gore kept out of the first frame.
- **At the same time, apply for Amazon Associates** with ID-gear links (field guides 4.5%, loupes and UV lights about 3%) to land the 3 qualifying sales.
- On YouTube, aim for the **500-sub tier's 3M Shorts views in 90 days**, which is unchanged after Feb 1, 2027, rather than the ad-share tier, which roughly doubles.

---

## Gaps / UNVERIFIED (summary)
1. Spoken first lines and transcripts: blocked by YouTube 429 / bot check. Hooks are titles plus real description openers.
2. Three top-hit counts are rounded channel-tab counts (Zack D "How Stitches Work", Infographics "Russian Sleep Experiment", Deep Look "Lice"; MinuteEarth's top Short also uses the tab count and is labelled in §1.9).
3. TikTok: official handles for Zack D, Brave Wilderness, Casual Geographic, Deep Look and Ze Frank weren't confirmed, and no TikTok video-level top hits were scraped.
4. TikTok Creator Rewards payout rate: not published by TikTok.
5. Amazon category mapping for specific loupes, UV lights and traps, and their prices: not checked.
6. @meatballmyths 30-day views and YouTube real watch hours: Studio-only data that I can't see.
7. TikTok FYF Eligibility Standards page: reported via flysub, not opened directly.

Raw data: `/workspace/drafts/playbook-1116/raw/`, `top_meta.json`, `retry_meta.json`, `rss.json`, `thumbs_montage.jpg`.
