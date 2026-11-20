> OWNER: MEATBALL CLAUDE ONLY (@MeatballMyths). Etsy Claude: ignore this file.

# Raunch ceiling research, 11/20 (Studio)
Read-only. Pulled 11/20 9:50–10:20 AM ET. Follow-up to `cutout-traction-1120.md` (22a41bd). Every claim has a link, our own numbers, or a **GUESS** label.
Method: yt-dlp metadata (title, views, duration, `age_limit`) on each comp's top Shorts (sorted by views from the latest ~150), YouTube auto-captions for swear counts and timing, and frame grabs to check burned-in captions. Caveat: YouTube auto-captions turn swears into `[ __ ]` and miss some, so counts are a floor. TikTok profile scraping was blocked for Fruit Love Island, so that one uses press coverage.

## TL;DR
1. **On swearing, we're already raunchier than the comps.** Their top Shorts average **0–1.5 swears per minute**. Our new scripts (Ozempic, Confession) plan 5 swears in 62 s, about **4.8 per minute**. MeatCanyon's 5 biggest captioned Shorts have **1 swear total**. Hatim's biggest have **0**.
2. **Where the comps beat us is the premise, the visuals and the targets.** MeatCanyon does grotesque body horror and sexual premises about named people ("Gooner…" 15.1M, "Fat Shaming A Streamer" 16.7M, "When Steve Harvey Hears A Lewd Answer" 17.2M). South Park clips do the f-word plus taboo setups. Explosm does dark death and Jesus gags. **Every one of their top videos is `age_limit 0`, not age-restricted.**
3. **The wall isn't swearing or limited ads.** Moderate swearing, even frequent, earns full ads. Since 7/29/2025 even strong swearing in the first 7 s does. A yellow icon doesn't change distribution (YouTube says so officially). **The real walls are:**
   - **(a) Age restriction,** which cuts off signed-out and under-18 viewers. It's triggered by sexual suggestiveness, gore as the focus, profanity in the title or thumbnail, and swear-compilation formats.
   - **(b) TikTok For You ineligibility,** for sexually suggestive behavior or graphic fictional violence. It also kills Creator Rewards.
   - **(c) Strikes** for harassment and hate.
4. **For the live cutouts, the wall is creative, not raunch.** The 3 live cutouts had **0 swears**. So did the bug Shorts that beat them 4–5x on YouTube. The variables that differ are the hook, the target and the length (see the first report). **GUESS:** adding swears alone won't move views.
5. **How to get over it:** go raunchier in the **premise and visuals** and stay clean in the **title, thumbnail and first caption line**. Use innuendo, never acts. Make the bleep itself a joke. Aim savagery at named people's **behavior**, not their bodies. Keep swears around 2–3 per 60 s, built into the punchlines, and stop masking moderate swears in captions on YouTube (detail in section 3).

---

## 1. RAUNCH LEVEL: comps vs ours

**Scale:**
- **1:** clean slapstick.
- **2:** mild swears, rude jokes.
- **3:** moderate swears plus dark themes (death, drugs, church hypocrisy) and light innuendo.
- **4:** strong profanity (the f-word), a sexual premise, grotesque body horror, or savage named-target satire.
- **5:** explicit sex, nudity or gore. This is age-restricted or For You-ineligible territory.

### 1a. Comp measurements (yt-dlp, 11/20)
| Channel | Shorts median views | Top Shorts measured (views, length) | Swears (auto-caption floor) | First 7 s? | Sexual | Gore / body | Targets | Burned-in captions uncensored? | age_limit | Raunch |
|---|---|---|---|---|---|---|---|---|---|---|
| **[MeatCanyon](https://www.youtube.com/@MeatCanyon)** | 4.0M | "White Women Ordering Pumpkin Spice Coffee" 22.1M (59 s); "xQc Needs More Views" 18.3M (60 s); "When Steve Harvey Hears A Lewd Answer" 17.2M (60 s); "How Taylor Swift Writes Break Up Songs" 16.8M (60 s); "Do I Look Like A Real Boy Papa" 14.7M (47 s); "When the Guy in the Gym is Huge." 12.7M (47 s) | **1 in 5 captioned videos** (Taylor Swift @42 s: "little [ __ ] worm"). About 0.2/min | no | innuendo in the premise (Steve Harvey "lewd answer") | grotesque body horror: Pinocchio "I must consume your soul to become a real boy"; the gym guy "it hurts dear God it hurts" | streamers, celebrities, stereotypes ("white women"), Disney characters | no captions; headline card (prior report) | all 0 | **Shorts 3.5. Long-form 4.5:** "Gooner…" 15.1M (masturbation premise: "he will furiously masturbate"); "Fat Shaming A Streamer" 16.7M (0 swears in 188 s), both age 0 |
| **[Hatim's Shorts](https://www.youtube.com/@hatimsshorts)** | 1.5M | "Trump, Putin & Zelensky as Street Musicians" 18.1M (32 s); "Trump Had Enough of Kim Jong Un" 17.9M (12 s); "Trump Calls for Help on Hormuz Strait" 15.4M (30 s); "Trump vs Magic Mirror" 10.3M (31 s) | **0.** The swear is cut off mid-word: "What the f…" (Magic Mirror) | no | none | slapstick only | world leaders | none | all 0 | **1.5** |
| **[Cyanide & Happiness](https://www.youtube.com/channel/UCWXCrItCF6ZgXrdozUS-Idw)** | 183K | "Why You Shouldn't Have Kids" 15.8M (44 s); "TRUE ENDING of Tortoise and the Hare" 7.1M (61 s); "If the World Was Backwards" 5.1M; "Wait that's actually brilliant..." 3.9M (56 s); "When Jesus is Your Drinking Buddy" 3.7M (68 s) | 7 in 5 videos, about 1.5/min. "Jesus" opens **"Oh, [ __ ] Oh, [ __ ]" at 1 s**. "Laziest Knight" has "What the [ __ ] is that" ×2 and "OW, [ __ ]" | **yes (Jesus, 1 s)** | none | cartoon injury (kids break parents' backs) | Jesus as a drunk (religion as setting), cops, parents | **Frame-checked. Moderate swear uncensored:** "OH, SHIT!" burned in at ~2 s. **F-word dropped from the caption:** "WHAT THE … IS THAT?!" | all 0 | **3** |
| **[South Park Studios](https://www.youtube.com/@southpark)** (official clips) | 460K | "Have some steak with his butter" 4.0M (77 s); "Butters calls an exterminator [on billionaires]" 3.9M (84 s); "Cartman says a no no word" 3.5M (58 s); "Aura Battle" 3.0M (98 s); "That is what's coming in November" 2.8M (46 s) | 7 in 5, about 1.2/min. **F-word:** "my mom is trying to [ __ ] me" (22 s); "Holy [ __ ] … that game looks [ __ ] tits" (41 s) | no | the f-word as a sex word; a "child molester" accusation as the joke premise | poop gags | billionaires, GTA 6, diet pyramid, Cartman's mom | none (frame-checked) | all 0 | **4** |
| **[Adult Swim](https://www.youtube.com/@adultswim)** (Rick and Morty, Boondocks clips) | 91K | "Survival of the Mortiest" 10.5M; "Realistic Street Fighter II" 7.2M (20 s); "Perfect" 3.6M (26 s); "marriage counseling" 2.6M (37 s); "Leprechaun genes" 2.4M (25 s) | about 0 captioned; "I'M GOING TO EAT YOUR ASS" (Street Fighter) | no | "thirst trap edit"; "She's 17 and hangs out with my dad" | none | the president, family | none | all 0 | **3.5** |
| **[Fruit Love Island](https://www.tiktok.com/@ai.cinema021)** (TikTok) | 773.8K (prior report) | Ep 15 40.1M; Ep 1 36.7M (prior report) | insults such as "bald-headed bitch" ([WIRED](https://www.wired.com/story/theres-something-very-dark-about-a-lot-of-those-viral-ai-fruit-videos/)) | n/a | cheating, affairs, sexual themes ([The Conversation](https://theconversation.com/unethical-brain-rot-why-are-millions-watching-ai-fruits-have-affairs-on-tiktok-279569)) | brawls | reality-TV parody, no real people | n/a | **9 videos taken down** for guideline violations (WIRED) | **4, with takedown cost** |
| **[Oney Plays](https://www.youtube.com/@OneyPlays)** | **29K** | "Ranking Memes" 192K (125 s); "How Toy Story Should Have Ended" 172K; "Housing Cows" 131K | most dense: "Uh [ __ ] I don't know" @4 s; "annoyed the [ __ ] out of me"; "you stupid son of a—" | **yes** | none | none | movies, memes | n/a | all 0 | **3, and the smallest views of the set** |
| **[Haminations](https://www.youtube.com/@Haminations)** | 13M | "What did I do to deserve this?" 100M (51 s); "This PRANK Backfired…" 49.4M; "Stop being so humble!" 46.8M | 0 | no | none | rib dislocation, spit | family | big word captions | all 0 | **1** |

**Read:**
- Raunch and reach **don't line up.** The cleanest channel (Haminations, 1) has the biggest median (13M). The most profane (Oney, 3) has the smallest (29K).
- The 3.5–4 channels win on **premise shock plus named targets plus visuals**, not swear count.
- **None** of the 30+ comp videos we measured is age-restricted.

### 1b. Ours (channels/scripts/)
| Script | Swears | Swears per min | Sexual | Gore / body | Targets | Raunch |
|---|---|---|---|---|---|---|
| Live: Rick DNA, HOA Karen, Cookout | **0** | 0 | none | none | Rick (bigot), a generic Karen, Elon/Zuck cameos | **2** (Rick 2.5 for the race topic) |
| Thanksgiving Politics v3 (posting today) | 1 ("hell", 56 s) | 1 | none | none | generic uncle and niece | **2**: "Richard, you owe child support in three states." |
| AI Took Dad's Job v3 | 1 ("shit", 24 s) | 1 | none | none | a made-up CEO, chatbot | **1.5**: "The robot fired the boss. First good idea it's had." |
| Gender Reveal v3 | 1 | 1 | none | cartoon fire | clout parents | **2.5**: "He's got nine fingers and a dream." |
| Vegan vs Gym Bro v3 | 1 | 1 | "How do you wipe?" / "My mom comes Tuesdays." | the bite | types | **2.5** |
| Holy Black Friday v3 | 1 | 1 | none | none | a made-up TV preacher, Rick | **2.5**: "Basic prayer, nine ninety-nine. Premium, He actually hears it." |
| Meatball on Ozempic | 5 | **about 4.8** | "Ask your mom's boyfriend." | shrinking gag | Oprah (impression), IKEA, diet culture | **3** |
| Meatball Goes to Confession | 5 | **about 4.8** | none | none | the Vatican bank, the Cowboys | **3**: "Feel guilty. Forever. That's the whole business model." |
| Black Friday v3 cursing | about 12 (strong ones bleeped) | about 11 | none | trampled kids | a made-up CEO | **3** |

**Verdict:**
- **Yes, the comps are raunchier,** at 3.5–4 against our 2–3.
- **But not in words.** We already swear 3–20x more per minute than MeatCanyon or Hatim's.
- The gap is in **premise** (sex, body horror, taboo setups), **visual gags** (gross-out and grotesque) and **named real targets**. Ours are made-up or generic.

---

## 2. THE WALL

### 2a. What does NOT limit reach (official)
- **Limited ads (yellow icon) doesn't touch distribution.** "Our search and recommendation system doesn't know which videos are monetizing and which are not" ([YouTube Studio Help 141805](https://support.google.com/youtubecreatorstudio/answer/141805)). It also says violent or graphic content may be "recommended to fewer viewers because it's not appropriate", so **the content is the wall, not the icon.**
- **Moderate swearing, even frequent, earns full ads.** The full-ads list includes "Moderate profanity like 'bitch', 'douchebag', 'asshole', and 'shit' used frequently in the video", plus "obscured profanity" (bleeps or masks) and "hell" or "damn" anywhere, the title included. **Limited ads only for:** moderate profanity in the **title or thumbnail**, or swearing "in most sentences". **No ads:** the f-word in the title or thumbnail, or slurs anywhere ([YouTube advertiser-friendly guidelines 6162278](https://support.google.com/youtube/answer/6162278)).
- **First-7-seconds rule removed (7/29/2025):** strong swearing in the first 7 s can now earn full ads ([TechCrunch 7/30/2025](https://techcrunch.com/2025/07/30/youtube-loosens-profanity-rules-for-monetized-videos/); [YouTube ad-guideline updates](https://support.google.com/youtube/answer/9725604)).
  - **So our "no swears in the first 7 s" rule is outdated for ads.** It's still good hook practice: frame 1 should be the target, not a swear.
  - Shorts: only views of Shorts that meet the ad guidelines count toward Shorts revenue sharing ([YouTube Shorts monetization policies 12504220](https://support.google.com/youtube/answer/12504220)). Limited ads therefore costs money, not reach.
- **TikTok has no swearing rule as such.** Its walls are hostile profanity aimed at a **private** person, and slurs (secondary summary of the 9/24/2026 Community Guidelines: [Clyper](https://www.clyper.io/guides/can-you-swear-on-youtube)).

### 2b. What DOES limit reach
| Wall | What triggers it | Reach effect | Source |
|---|---|---|---|
| **YouTube age restriction** | sexually suggestive content (provocative dancing, fondling, poses meant to arouse, lingerie); a focus on violent or gory imagery; "heavy profanity in the title, thumbnail or metadata"; a video "focused on the use of profanities such as a compilation"; "a video meant for adult audiences but could easily be confused with family content" (a cartoon risk) | **"Not viewable to users who are under 18 years of age or signed out."** Signed-out viewing and teens are a big share of Shorts reach (**GUESS** on size; YouTube doesn't publish it). | [YT Help 2802167](https://support.google.com/youtube/answer/2802167) |
| **YouTube teen safeguards** | content "acceptable in isolation" but problematic if viewed repeatedly | fewer repeat recommendations to under-18s, including viewers YouTube estimates are teens | [YT Help 16422785](https://support.google.com/youtube/answer/16422785), [10315823](https://support.google.com/youtube/answer/10315823) |
| **Harassment strike** | "prolonged insults … based on someone's intrinsic attributes … physical attributes", i.e. fat-shaming a **real named person** | removal. The scripted-satire exception exists but "is not a pass to harass someone and claim 'I was joking.'" | [YT Help 2802268](https://support.google.com/youtube/answer/2802268) |
| **Hate (ads and strikes)** | "Statements intended to disparage a protected group or imply its inferiority"; "Portraying ideologies or beliefs in a malicious way by generalizing" | no ads up to removal. Comedy that "condemns or alludes to ridicule" of protected groups **can** earn ads | [6162278](https://support.google.com/youtube/answer/6162278) (Hateful & derogatory) |
| **TikTok age-restricted plus For You-ineligible** | "significant adult body exposure or sexually suggestive behavior involving adults"; "excessive blood", "graphic fictional violence" | adults only, and **no For You feed.** The video still shows in search and on the profile | [TikTok Sensitive & Mature Themes](https://www.tiktok.com/community-guidelines/en/sensitive-mature-themes), [For You eligibility standards](https://www.tiktok.com/community-guidelines/en/fyf-standards) |
| **TikTok repeat-suppression** | "sexual suggestiveness" is listed among content the feed avoids recommending over and over | throttled, not removed | [For You eligibility standards](https://www.tiktok.com/community-guidelines/en/fyf-standards) |
| **TikTok Creator Rewards** | content ineligible for the For You feed earns nothing; needs ≥1 min, original, 1,000 qualified views (≥5 s watched) | no payout | [Creator Rewards terms](https://www.tiktok.com/legal/page/global/tiktok-creator-rewards-program-eea/en), [Tallyterms summary](https://tallyterms.com/blog/tiktok-creator-rewards-program-requirements) |
| **TikTok 18+ audience control** (our choice) | the creator turns it on per post or for the whole account; the account setting tags every post with no per-post opt-out | removes all 13–17 viewers. The post can still reach adults' For You feeds; policies still apply | [TikTok newsroom via Adweek](https://www.adweek.com/media/tiktok-begins-extending-18-age-gate-to-creators-of-short-form-video/), [Lilach Bullock](https://www.lilachbullock.com/tiktok-audience-controls-18-plus/) |
| **Mass reports and takedowns** | sexual or violent edge drawing reports | Fruit Love Island lost 9 videos at peak | [WIRED](https://www.wired.com/story/theres-something-very-dark-about-a-lot-of-those-viral-ai-fruit-videos/) |

**Pre-check tool:** TikTok's **Content Check Lite** (TikTok Studio web) checks For You eligibility before posting ([TikTok newsroom](https://newsroom.tiktok.com/en-us/new-tools-for-creators), [Engadget](https://www.engadget.com/social-media/tiktok-content-check-tells-creators-if-their-videos-will-be-blocked-from-for-you-pages-110015168.html)). Claude should run it on every edgier cut. **Ask Data/Studio** to check for "Viewable by 18+" or "ineligible for recommendation" notices on the live cutouts (Studio-only; not checked).

### 2c. Is our problem raunch at all? (our numbers, from cutout-traction-1120.md)
- Live cutouts: **0 swears** each, age_limit 0. YouTube 7 / 46 / 48 views against bug Shorts 152–272 at matched ages (0.22x). TikTok 0.53x.
- The bug Shorts also have **0 swears** and beat them. So raunch is **not** what separates winners from losers on our own channel.
- The edgiest topic, Rick (race), was **best** on TikTok (309, 2 shares) and **worst** on YouTube (7). **GUESS:** the YouTube seed audience (bug-education viewers) rejected a 62 s comedy cutout. That's the length, hook and audience wall from the first report, not raunch.
- **Conclusion:** the order of walls is **(1) hook, target and length → (2) seed audience on YouTube → (3) raunch ceiling.** We haven't reached the raunch ceiling yet, but there's room to climb safely from 2 to 3.5.

---

## 3. HOW TO GO OVER IT (ranked)
| # | Tactic | Evidence | Risk |
|---|---|---|---|
| 1 | **Make the premise raunchy, keep the words light.** Taboo setup, absurd sexual or bodily situation, named target. | MeatCanyon: "Gooner…" 15.1M and the Steve Harvey "lewd answer" Short 17.2M, both with ≤1 swear and age 0. South Park's "child molester" accusation clip 3.5M, age 0. | Low on YouTube if implied and not shown. On TikTok, keep it verbal, with no suggestive movement on screen (that's what triggers For You ineligibility). |
| 2 | **Innuendo, not acts.** Talk about sex; never show or animate sexual motion (bed shaking, humping, moaning). | YouTube full-ads list: "Discussions of sex in … comedic contexts", "sexual tension … without explicit depictions". Limited ads: "Sexual innuendos, such as moaning sounds"; no ads: "Focal, implicit sexual act" ([6162278](https://support.google.com/youtube/answer/6162278)). TikTok: "sexually suggestive behavior" means age-restricted and For You-ineligible. | Verbal innuendo: low. Moaning sound effects or humping animation: limited or no ads, and For You-ineligible. |
| 3 | **Gross-out and visual gags in place of extra swear words.** Grotesque cutout deformations, sauce and gore cartoon-style, body horror on Meatball himself. | MeatCanyon's grotesque style is the brand (14.7M Pinocchio "consume your soul"). Explosm cartoon injury 15.8M. YouTube treats animated content as "low realism" ([6162278 definitions](https://support.google.com/youtube/answer/6162278)). | Keep blood cartoonish and brief. "Excessive blood" or "graphic fictional violence" is TikTok For You-ineligible. |
| 4 | **The bleep or swear as the joke itself.** A character can't stop swearing, or a kid says the no-no word. | South Park "Cartman says a no no word" 3.5M. Explosm "Don't Say That, Billy" 3.5M (title only; captions not pulled). Bleeps are "obscured profanity", so full ads. | Low. Don't make it a compilation, since "focused on the use of profanities" can mean age restriction ([2802167](https://support.google.com/youtube/answer/2802167)). |
| 5 | **Fewer, harder swears, all on punches: 2–3 per 60 s, with one strong one allowed.** | Comps run 0–1.5/min. Our 4.8/min is already above them. Moderate swears used frequently still earn full ads. The f-word anywhere in the video (not the title or thumbnail) is fine since 7/2025. | **"In most sentences" means limited ads.** Our 12-swear Black Friday v3 is close to that line. |
| 6 | **Stop masking moderate swears in YouTube captions. Keep the f-word dropped from captions** (Explosm pattern). | Explosm burns "OH, SHIT!" at ~2 s (3.7M, age 0) and drops the f-word from the caption ("WHAT THE … IS THAT?!"). YouTube only cares about the **title and thumbnail** for profanity in text. | Low on YouTube. On TikTok, keep masks only if the Content Check flags them (**GUESS**). **Needs Moondog88/Jarvis to lift the current "captions mask swears" rule.** |
| 7 | **Savagery at named people's behavior, never their bodies or protected traits.** | The harassment policy bans prolonged insults on "physical attributes" even of real people. Its satire exception isn't a pass. Hatim's world-leader slapstick is 0-swear and pulls 10–18M. | Fat-shaming a real person ("Fat Shaming A Streamer" style) is a **strike risk** for us, since we're a small channel without MeatCanyon's history (**GUESS**). Keep fat jokes on Meatball and diet culture. |
| 8 | **Clean title, thumbnail and first caption line. Raunch from second 2 on.** | Profanity in the title or thumbnail is the main ad and age-restriction trigger. All comps' titles are clean ("Gooner…" is the edgiest). | Low. Keeps every surface the system reads before the watch clean. |
| 9 | **TikTok 18+ audience control: only per post, never account-wide.** | Removes 13–17 viewers. Account-wide tags every post with no opt-out (sources in 2b). | **Costs reach** on every tagged post. The share of under-18 viewers on our TikTok isn't measured (ask Data). Use it only for a deliberately maxed-out episode. |
| 10 | **A separate edgier channel for 4–5 raunch content.** | Big brands keep edgier long-form separate from clip Shorts (South Park Studios and Adult Swim clip channels are 3.5–4, not 5). Already the loss-condition in the first report's plan. | Needs Moondog88's yes. It starts from 0 subscribers. **GUESS:** not worth it until a 3.5 cutout proves demand. |

**Don't:**
- Show sexual motion or moaning, or put the f-word in titles or thumbnails.
- Fat-shame a named real person, write slurs or "group is lesser" punchlines, or make abuse jokes.
- Invent crimes or quotes. Fruit Love Island's violent and sexual edge cost 9 takedowns.

---

## 4. Rewrites of the 3 tamest beats
Hard lines kept: no slurs, no abuse jokes, no group-is-lesser, no invented crimes or quotes about real people. **Writer and QA still score these. Nothing is rendered or scheduled.**

### Beat A: AI Took Dad's Job v3, ending lines 21–23 (raunch 1.5)
> CEO: Gary's the CEO now. / DADBOT: First order: I fired everyone. Sales went up four percent. / MEATBALL: The robot fired the boss. First good idea it's had.

**A1, raunchier but distributable (3).** Verbal innuendo, one moderate swear, no act shown.
> CEO: (on the porch, holding a box) Gary's the CEO now. He fired me by text. With a heart emoji.
> DADBOT: I have also replaced your wife's yoga instructor. She says I am "very flexible."
> DAD: (slow turn) …Gary, you son of a bitch.
> DADBOT: Son of a laptop. Please be accurate.

Cost: none expected. Full ads, since "bitch" is moderate and the sex reference is implied in dialogue. For You-safe if there's no suggestive animation.

**A2, max raunch (4.5).** Flagged.
> DADBOT: I have also been satisfying your wife. I have a vibrate setting.
> DAD: Gary, you motherfucker.

Costs:
- **YouTube:** "sex toys or devices featured … even when not used" and "sexual activities (including implied)" mean **limited or no ads** ([6162278](https://support.google.com/youtube/answer/6162278)).
- **TikTok:** "sexually suggestive" content risks For You ineligibility and repeat-suppression ([For You eligibility standards](https://www.tiktok.com/community-guidelines/en/fyf-standards)).
- The f-word itself is fine for ads.
- **Not recommended.**

### Beat B: Holy Black Friday v3, closer line 21 (raunch 1.5)
> MEATBALL: Happy Thanksgiving. Somebody pass the damn pie.

**B1, raunchier but distributable (3).** Priest lane per the owner, aimed at a made-up scam preacher. Moderate swear and a religious-setting gag; the faith isn't the butt.
> PASTOR CHAD: (on the jail TV, still in the gold suit) Sinners! My commissary takes Venmo. The Lord wants me to have Doritos.
> GRANDMA: (sips tea) Ten percent of nothing, Chad.
> MEATBALL: Happy Thanksgiving. Grandma got a jet, Chad got a cellmate who's also a pastor, and they're already selling franchises. Pass the goddamn pie before they tithe it.

Cost: none expected. "Goddamn" is moderate profanity; the butt is a made-up fraud.

**B2, max raunch (4).**
> PASTOR CHAD: Diamond-tier sinners get a private prayer session in my hot tub. Bring a towel and a check.
> MEATBALL: Holy shit. He's still taking Venmo from jail.
> GRANDMA: Fuck it. I'm buying the hot tub too.

Costs:
- The hot-tub line is fleeting innuendo. **Likely still full ads**, since it's comedic sex discussion with no act. It moves to **limited** if it's animated suggestively.
- The f-word is fine since 7/2025.
- **GUESS:** some religious-viewer reports, but the target is a fictional fraud, not the faith.
- **Recommended as the upper bound** if QA agrees.

### Beat C: Thanksgiving Politics v3, open line 1 (raunch 1; also the hook weakness from the first report)
> [Banner] MEATBALL: Thanksgiving. The one day your family remembers why they moved away.

**C1, raunchier but distributable (3).** No banner. Frame 1 is the headline. First swear at about 3 s; that's OK for ads now, but keep it moderate.
> [On-screen, frame 1: "GRANDMA'S HOUSE GOES TO WHOEVER SHUTS UP FIRST."]
> GRANDMA: (slams the knife into the turkey) Starting now.
> UNCLE RICK: (instantly) This turkey's drier than Kaylee's mom's second marriage.
> KAYLEE: Third, Rick. And at least she got stuffed more than this bird.
> GRANDMA: Both of you, shut the hell up. I'm eighty-six. I could die during grace.

Cost: none expected. The "stuffed" innuendo is verbal. "Hell" is fine anywhere, even in titles.

**C2, max raunch (4).**
> UNCLE RICK: (0 s, mouth full) Pass the fucking potatoes before the socialists tax 'em.
> KAYLEE: The only thing you've stuffed since 2019 is that turkey, Rick.
> GRANDMA: And you only came out of my basement for the Wi-Fi, Bradley.

Costs:
- The f-word at 0 s now earns ads (2025 update).
- **GUESS:** opening on a swear instead of the premise hurts "chose to view" on both platforms. That's a hook cost, not a policy one.
- The f-word **can't go in the first caption line** (our rule). It has to be dropped Explosm-style.
- **Not recommended.** It trades the premise for shock.

---

## 5. Recommended rule changes (for Jarvis to put to Moondog88; none applied)
1. **Swear cap:** 2–3 per 60 s, on punchlines; one f-word allowed after the premise lands. The "no swears in first 7 s" rule becomes "first line is the premise, not a swear" (policy: [TechCrunch](https://techcrunch.com/2025/07/30/youtube-loosens-profanity-rules-for-monetized-videos/)).
2. **Captions:** show moderate swears uncensored on YouTube; drop the f-word from captions; keep TikTok masks until Content Check Lite says otherwise.
3. **Raunch target 3–3.5:** a taboo premise plus verbal innuendo plus cartoon gross-out, never sexual motion or moaning sounds.
4. **Fat lane:** Meatball, diet culture, and celebrities' **behavior** (e.g. denying the shot). Never a real person's body ([harassment policy](https://support.google.com/youtube/answer/2802268)).
5. **Add to QA:** Content Check Lite on every TikTok cut, and a Studio check for "Viewable by 18+" within 1 h of each YouTube upload.
6. **Don't change mid-week.** These apply from the 11/27 review, per the first report's 7-day test, unless Jarvis says otherwise.
