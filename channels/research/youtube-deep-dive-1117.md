> OWNER: MEATBALL CLAUDE ONLY (@MeatballMyths, repo mooneyn60-art/skills). Etsy Claude: ignore this file.

# How YouTube works, for Meatball Myths: a deep-dive research brief

Written by Social: Research & QA on Tue 11/17/2026, 9:25–9:35 AM ET, for Social Studio, asked for by Moondog88. All sources were fetched live on 11/17/2026. Nothing was posted or messaged, and no settings were changed.

**Labels used in this file**
- **[OFFICIAL]**: YouTube Help Center, YouTube Official Blog, How YouTube Works, or a YouTube staffer speaking on Creator Insider.
- **[THIRD-PARTY]**: creator or vendor research. Its method and sample are stated, and none of it is a random sample.
- **[OUR DATA]**: numbers quoted exactly from our repo files, with the file named.
- **[OUR ANALYSIS]**: my reading or math. It is not a YouTube statement.
- **[UNCERTAIN] / [DISPUTED] / [OLDER SOURCE: year]**: as named.
- **Transcript note:** quotes from Creator Insider videos come from YouTube's auto-captions, so they may contain small transcription errors. The words are kept as captioned, with filler ("um", "uh") removed.

---

## TL;DR (6 lines)
1. **There is no single "algorithm" and no magic metric.** YouTube ranks videos *for each viewer*. It "pulls" candidates when someone opens Home, a watch page or the Shorts feed, and weighs click, watch time, likes/dislikes, comments and surveys differently by device and context. The stated goal is long-term viewer satisfaction. [OFFICIAL, §1]
2. **Search, Home, Suggested and the Shorts feed are separate contexts.** Search adds query relevance (title, description, video content). Home ranks mainly on how videos do *on Home*. Shorts and long-form have **separate recommendation systems**. [OFFICIAL, §1]
3. **Packaging decides the click; the first seconds decide the stay.** YouTube's own A/B tool picks winners by **watch time, not CTR**. On Shorts there is no thumbnail click: the key appeal metric is "stayed to watch." [OFFICIAL, §2]
4. **Breakouts happen when a video finds viewers beyond its core audience** who choose it and stay satisfied. CTR and average view duration usually *fall* as a video breaks out. Topic size, competition and seasonality cap reach, and old videos can come back in later waves. [OFFICIAL, §3]
5. **Views are now an exposure count.** Since 8/24/2026, every format counts a view from the first frame (Shorts since 3/31/2025). Use **engaged views, watch time, retention vs your own similar-length videos, and stayed-to-watch**. Raw views, small-sample CTR and cross-channel "benchmarks" are mostly noise. [OFFICIAL, §4]
6. **For us:** YPP needs **4,000 qualified long-form watch hours**, and Shorts-feed hours don't count. We are at "about 13 of 4,000," and Shorts send "at most 0.49%" of viewers to long videos. Search-first long-form house-bug episodes are the lever, Shorts are discovery, and TikTok-to-YouTube is a side bet. [OUR DATA + OUR ANALYSIS, §5]

---

## 1. The algorithm: discovery, ranking and session behavior

### 1.1 The core model (all surfaces) [OFFICIAL]
- **Ranking is per viewer ("pull", not "push").** Todd Beaupré, Senior Director of Growth & Discovery, on Creator Insider (Sept 2026): "most of the recommendations are more pulled for each viewer… when a viewer opens their app or turns on their TV… it takes that information and understands and then brings in candidate videos that might be a good match for that viewer and then ranks them for that viewer. And so, each viewer gets a different ranking." ([Creator Insider, "YouTube Algorithm 2026 - What Creators Need to Know," 9/1/2026](https://www.youtube.com/watch?v=rHLjxrbXmmY), ~1:14–2:21; [caption transcript](https://viewrankai.com/tools/youtube-transcript/rHLjxrbXmmY))
- **Inputs YouTube names publicly:** "a user's viewing behaviour, likes, dislikes, subscriptions and feedback, including from satisfaction surveys"; it also considers "the reputation and the quality of a channel" and uses "external evaluators." ([How YouTube Works: Recommendations](https://www.youtube.com/howyoutubeworks/product-features/recommendations/))
- **Context matters.** "The recommendation system uses time of day and device… as some of the signals." (Beaupré, [Creator Insider, "The YouTube Algorithms in 2025 — Explained!," 1/23/2025](https://www.youtube.com/watch?v=dhYIb72L1hU))
- **No fixed weights.** "The system doesn't even work that there's a weighting for each of these that is the same for everyone. It actually doesn't even work such that it's the same for you at all times… Maybe on television, the time you spend it might be more or less important than… the click through rate versus on mobile maybe it's… whether you like or dislike." (Beaupré, [rHLjxrbXmmY](https://www.youtube.com/watch?v=rHLjxrbXmmY), ~12:28–13:34)
- **Three buckets of performance signals,** in YouTube's own Help wording ([Understand your content performance for YouTube's recommendation system](https://support.google.com/youtube/answer/16559650?hl=en)):
  - "Appeal: Did people choose to watch the content or did they ignore or click 'not interested?'"
  - "Engagement: Once viewers start watching, do they stick around?"
  - "Satisfaction: Did viewers enjoy the video?"
- **Satisfaction beats raw time.** "we ask them directly with surveys built into the product we collect millions of responses and feed that directly into the recommendation system." YouTube looks at "the absolute time you spend as well as the relative time." (Beaupré, [dhYIb72L1hU](https://www.youtube.com/watch?v=dhYIb72L1hU); [rHLjxrbXmmY](https://www.youtube.com/watch?v=rHLjxrbXmmY) ~11:05–11:46)
- **Comments count, but turning them off isn't punished.** "when we started looking at integrating comments, it was very important to us that we didn't penalize people that… choose not to have comments on." ([rHLjxrbXmmY](https://www.youtube.com/watch?v=rHLjxrbXmmY) ~14:51–15:28)
- **Learned per audience segment, not one verdict.** "it can learn that for subscribers, this video is not… performing well. And for people who haven't watched the channel, it is." "We're not going to decide just based on the first hour or first 1,000 people who see a video." ([rHLjxrbXmmY](https://www.youtube.com/watch?v=rHLjxrbXmmY) ~4:21–5:07, ~35:29)
- **New and small channels:** "we have parts of the system that don't depend on an individual viewer's history with that channel… we'll look at things like the user's topical preferences and what we understand about what this video is about… And if we don't [find interested viewers], then maybe that video just won't get more impressions." ([rHLjxrbXmmY](https://www.youtube.com/watch?v=rHLjxrbXmmY) ~31:55–32:35)
- **Large language models are now in recommendations.** These are meant to understand content "ingredients" (style, emotion), not just memorize which video worked for which viewer. (Beaupré, [dhYIb72L1hU](https://www.youtube.com/watch?v=dhYIb72L1hU)) [UNCERTAIN: YouTube gives no detail on what changed in ranking because of this.]

### 1.2 Surface by surface

| Surface | How it ranks (official) | What it means |
|---|---|---|
| **Home / browse** | Personalized; "a mixture of personalised recommendations, subscriptions and the latest news" ([HYW](https://www.youtube.com/howyoutubeworks/product-features/recommendations/)). For Home ranking, "what's most valuable for us to look at… is how well videos perform in that home page context. So, if people have a very different behavior when they come in through an embed or through an ad or through a link from a friend, if that isn't predictive… it doesn't make sense for us to weight that information very much." ([rHLjxrbXmmY](https://www.youtube.com/watch?v=rHLjxrbXmmY) ~34:02–34:41) | Off-platform traffic (for example from TikTok) is not a strong Home signal either way. [OUR ANALYSIS] |
| **Suggested / Up Next** | "based on what you're currently watching, alongside other videos that we think you may be interested in" ([HYW](https://www.youtube.com/howyoutubeworks/product-features/recommendations/)). Watch-page recommendations moved "from only being related videos to videos that can be relevant for a number of reasons"; "the number one place that people are watching videos from channels they're subscribed to is actually on the watch page in that suggested list." ([rHLjxrbXmmY](https://www.youtube.com/watch?v=rHLjxrbXmmY) ~29:22–29:43) | Unrelated videos in our "suggested" traffic list are normal and are not a targeting error. [OFFICIAL] |
| **Search** | "relevance, engagement and quality… given differing importance based on the type of search." Relevance includes "how well the title, tags, description, and video content match your search query"; engagement includes "the watch time of a particular video for a particular query"; quality means "expertise, authoritativeness, and trustworthiness." Results can be personalized by history. ([How YouTube search works](https://www.youtube.com/howyoutubeworks/product-features/search/)) Tags "are primarily used to help correct for common spelling mistakes." ([Help 16559650](https://support.google.com/youtube/answer/16559650?hl=en)) | Search is the one surface where the *words* in the title and description directly decide whether we are a candidate. |
| **Shorts feed** | "Shorts are ranked based on performance and viewer personalization." Performance: "do they choose to watch it, ignore it, or click 'not interested'?… Our systems use the signals for % of viewers who chose to view, avg. view duration and avg. % viewed to inform ranking. Lastly… likes and post-watch survey results." ([Shorts search & discovery tips](https://support.google.com/youtube/answer/11914225?co=YOUTUBE._YTVideoType%3Dshorts&hl=en)) | The swipe-or-stay decision in the first seconds is the Shorts version of CTR. |
| **Shorts vs long-form** | "we've built separate recommendation systems optimized for each. While these systems understand cross-format viewing, they primarily focus on serving the unique viewing patterns of each format. Consequently, we haven't seen evidence of Shorts negatively impacting long-form performance." ([YouTube Blog, 5/6/2025](https://blog.youtube/creator-and-artist-stories/debunking-common-myths-about-youtube-shorts/)) "Shorts performance doesn't negatively impact long form Video recommendations." ([Help 11914225](https://support.google.com/youtube/answer/11914225?co=YOUTUBE._YTVideoType%3Dshorts&hl=en)) | Shorts won't hurt long-form, but they won't automatically feed it either. [OUR ANALYSIS] **[DISPUTED]:** some third-party blogs claim the systems were "fully decoupled in late 2025" (e.g. SocialPilot, Sept 2026). I found **no official statement** using that wording, so treat it as unverified. |
| **Subscriptions feed** | "just a chronological feed… doesn't have any sort of like dynamics of the recommendation system in it." ([dhYIb72L1hU](https://www.youtube.com/watch?v=dhYIb72L1hU)) | This is a clean comparison slice (see §4). |

### 1.3 Session behavior
- **[OFFICIAL] The current framing is long-term value, not "session time".** "our North Star is long-term user value"; "it actually leads to people coming back to YouTube more in the long run… not just to… suck a lot of time from you today." ([rHLjxrbXmmY](https://www.youtube.com/watch?v=rHLjxrbXmmY) ~10:26; [dhYIb72L1hU](https://www.youtube.com/watch?v=dhYIb72L1hU))
- **[UNCERTAIN]** Older creator lore says YouTube rewards videos that "start or extend sessions." I found **no 2025–2026 official statement** that names session time as a ranking factor, so don't plan around it.
- **[OFFICIAL] Decision fatigue drives format growth.** "short-form video has been successful… [because] it eases the burden of decision-making"; "on televisions… viewers don't want to be picking up the remote every 5 to 10 minutes… This is why series tend to work on television." Also: "people think that YouTube is pushing longer videos now, but people are watching on television and they want longer videos." ([rHLjxrbXmmY](https://www.youtube.com/watch?v=rHLjxrbXmmY) ~16:17–18:49)
- **[OFFICIAL] Catalog depth helps.** "the more catalog that they have to choose from the more likely it is that they'll find another video that they'll enjoy watching which is a great signal back to us." This was said about dubbed catalogs, but the logic is general. ([dhYIb72L1hU](https://www.youtube.com/watch?v=dhYIb72L1hU))
- **[OFFICIAL] The same video can be shown many times before a click.** Users complain about repeats, but "we do see that people do engage sometimes… it takes a few tries." One viewer had been shown a channel's recent uploads "19 times, and they didn't notice." ([rHLjxrbXmmY](https://www.youtube.com/watch?v=rHLjxrbXmmY) ~7:14–8:22)

---

## 2. How people decide to click (and to stay)

### 2.1 Long-form: title + thumbnail, then the intro [OFFICIAL]
- **Packaging sets reach and expectations.** "Your title and thumbnail are vital for communicating value, sparking intrigue, and setting clear expectations for viewers." YouTube's example of a wider-appeal reframe: "instead of 'In-depth analysis of economics in the coffee market' try… 'Why Is Your Coffee So Expensive? Understanding Everyday Economics.'" ([Help 16559650](https://support.google.com/youtube/answer/16559650?hl=en))
- **The hook must keep the packaging's promise.** "The initial seconds of your content are when viewers decide to stay or move on, especially for Shorts and long-form videos. Ensure your intro delivers on the promise made by your thumbnail and title." ([Help 16559650](https://support.google.com/youtube/answer/16559650?hl=en))
- **YouTube measures the intro at 30 seconds, not 3.** "Intro tells you what percentage of your audience still watched your video after the first 30 seconds." A high intro percentage can mean "the content in the first 30 seconds matched the viewer's expectation of the video's thumbnail and title." ([Help 9314415](https://support.google.com/youtube/answer/9314415?hl=en)) **[UNCERTAIN]:** the popular "first 3 seconds" rule has **no official number** behind it for long-form. YouTube says only "initial seconds."
- **Clickbait backfires.** "Clickbait videos tend to have low average view duration and therefore are less likely to get recommended… You can tell if your thumbnail is clickbait if it's getting high CTR but low average view duration and lower than expected Impressions." ([Help 7628154](https://support.google.com/youtube/answer/7628154?hl=en))
- **YouTube's own A/B tool optimizes watch time, not clicks.** "the title or combination of title and thumbnail with the highest watch time will be shown to all viewers"; "we optimize tests for overall watch time over other metrics, like click-through-rate." It is not available for Shorts, needs advanced features, runs on desktop Studio only, and "can take a few days or up to 2 weeks." ([A/B test titles & thumbnails](https://support.google.com/youtube/answer/13861714?hl=en))
- **Bigger thumbnails, fewer choices.** The larger-thumbnail Home redesign "actually drove more attention and engagement around long-form… often less is more." ([rHLjxrbXmmY](https://www.youtube.com/watch?v=rHLjxrbXmmY) ~19:25–20:04)

### 2.2 Shorts: no click, just stay-or-swipe
- **[OFFICIAL]** The feed autoplays, so the "choose to view" signal is the share who stay. Studio calls it **"Stayed to watch: The percentage of times viewers stayed to watch past the initial seconds of a Short."** ([Understand your YouTube video reach](https://support.google.com/youtube/answer/9314355?hl=en))
- **[OFFICIAL blog, quoting a creator]** "I really do think you have one second to hook someone, especially on Shorts." (Jenny Hoyos, in [YouTube Blog recap of Creator Insider with Shorts product lead Todd Sherman, 1/28/2025](https://blog.youtube/creator-and-artist-stories/youtube-shorts-deep-dive/)) This is a creator's opinion that YouTube published, not a measured YouTube rule.
- **[OFFICIAL blog, quoting a creator]** On Shorts thumbnails: "Thumbnails are not important because 99.9% of the views are coming from the Shorts feed… As far as channel marketing and branding, I think thumbnails are very important." (same source) **[UNCERTAIN]:** the 99.9% describes Hoyos's own channel, not YouTube overall. Shorts thumbnails and titles still show in search, on the channel page and on Home ([Help 10059070](https://support.google.com/youtube/answer/10059070?hl=en)).

### 2.3 How search, browse and suggested differ [OFFICIAL unless marked]

| | Search | Browse (Home) | Suggested |
|---|---|---|---|
| Viewer intent | Has a question | Open to anything | Mid-session, often "changing the channel" ([rHLjxrbXmmY](https://www.youtube.com/watch?v=rHLjxrbXmmY) ~29:43–30:20) |
| What wins the click | Matching the query words, then engagement for that query ([HYW search](https://www.youtube.com/howyoutubeworks/product-features/search/)) | Broad appeal and curiosity (the "coffee" reframe, [16559650](https://support.google.com/youtube/answer/16559650?hl=en)) | Relevance to the viewer's interests, not only to the current video |
| Typical CTR | Not published by YouTube | "If a video gets a lot of impressions (such as if it appears on the Home Page), it's natural for the CTR to be lower" ([7628154](https://support.google.com/youtube/answer/7628154?hl=en)) | Not published |
| Packaging rule [OUR ANALYSIS] | Say the plain words people type ("house centipede") | One clear, curious promise | Same as browse, and it must work next to unrelated videos |

---

## 3. What makes a video break out vs stall

**[OFFICIAL] Mechanism.** Ranking is relative to everything else a viewer could watch. "YouTube's systems rank each video against all the other videos a viewer might watch. Even if a video is performing well compared with other videos on your channel… videos from other channels are performing even better." ([Help 7628154](https://support.google.com/youtube/answer/7628154?hl=en)) A breakout is a video that keeps winning these per-viewer contests as it reaches viewers further from its core audience.

**[OFFICIAL] Signs of a breakout in the data**
- **Aggregates drop as reach grows.** "the more impressions something gets, the broader the audience is reached and that tends to make those aggregates look lower than if you're only targeting just the core fans." ([rHLjxrbXmmY](https://www.youtube.com/watch?v=rHLjxrbXmmY) ~11:05)
- **Non-subscribers dominate.** "the majority of their audience can be non-subscribers. And even in the first hour videos are reaching people who've never watched the channel before." ([rHLjxrbXmmY](https://www.youtube.com/watch?v=rHLjxrbXmmY) ~4:21)

**[OFFICIAL] Why videos stall (external caps)**
- **Topic interest:** "Some topics have more broad appeal than others, and that appeal can change over time."
- **Competition:** "you may get fewer impressions if Shorts from other channels are performing even better."
- **Seasonality:** traffic varies through the year.
- All three are from [Help 11914225](https://support.google.com/youtube/answer/11914225?co=YOUTUBE._YTVideoType%3Dshorts&hl=en).
- **Supply and demand:** early in a trend there is "high demand and low Supply so a lot of views per video and then later there might be a lot more creators… more Supply than demand." ([dhYIb72L1hU](https://www.youtube.com/watch?v=dhYIb72L1hU))
- **Audience saturation:** "sometimes you may need to move on from a particular format or topic… because the audience has been saturated on that particular area." (same)
- **Niche size:** "some videos naturally have a smaller audience than other videos." (same) "it's unhealthy for creators to always just aim for the high water mark." ([rHLjxrbXmmY](https://www.youtube.com/watch?v=rHLjxrbXmmY) ~22:41)

**[OFFICIAL] Late breakouts are real**
- "a lot of videos also get the majority of their views… a month or… later if it's evergreen content. We're not going to stop… trying to see if there's viewers that would be interested in it." ([rHLjxrbXmmY](https://www.youtube.com/watch?v=rHLjxrbXmmY) ~6:14–6:57)
- Videos can come back "in multiple waves… in six months there's something else that's related that pops up that makes this video relevant again." ([dhYIb72L1hU](https://www.youtube.com/watch?v=dhYIb72L1hU))

**[OFFICIAL] Myths YouTube rejects**
- "If subscribers don't click in hour 1 the video is cooked": rejected ([rHLjxrbXmmY](https://www.youtube.com/watch?v=rHLjxrbXmmY) ~3:16–5:47).
- Turning off subscriber notifications as a tactic: "I wouldn't advise people to turn off notifying subscribers." (~34:41)
- Posting cadence: "There is no minimum posting cadence required for your videos to perform well." ([11914225](https://support.google.com/youtube/answer/11914225?co=YOUTUBE._YTVideoType%3Dshorts&hl=en))
- Trending sounds required: "not essential." ([Blog 5/6/2025](https://blog.youtube/creator-and-artist-stories/debunking-common-myths-about-youtube-shorts/))

**[THIRD-PARTY] What creator research adds** (correlations only, not causes)
- **Shorts length (quso.ai, vendor).** "Across 108,000 matured YouTube Shorts, the 11 to 20 second band earns the most median views, a median of 901." Under 10 s: 514; 31–45 s: 347; 46–60 s: 188; 90 s+: 51. The sample is Shorts "live at least 14 days" from the vendor's users, and the page was last updated 6/29/2026. ([quso.ai research](https://quso.ai/research/youtube-shorts-length))
  - Caveats [OUR ANALYSIS]: the sample is self-selected and correlational. It predates the 8/24/2026 view change, but Shorts were already counted from the start after 3/31/2025.
- **Long-form retention (Retention Rabbit, vendor, May 2025).** "Overall Average YouTube Video Retention: 23.7%"; "Only 1 in 6 videos (16.8%) surpass the 50% audience retention mark"; "55%+ viewer drop-off occurs within the first minute"; "Videos 5-10 mins hold viewers best (31.5%)." The sample is "over 10,000 YouTube videos across 1k+ creators… most users are early- to mid-stage creators," Q1 2024–Q1 2025. ([Retention Rabbit report, archived 7/25/2026](https://web.archive.org/web/20260725211359/https://www.retentionrabbit.com/blog/2025-youtube-audience-retention-benchmark-report))
  - **[DISPUTED/UNVERIFIED]:** the same report says videos "perceived as heavily AI-generated" show "70% lower" retention. That rests on the vendor's own AI classifier and has no public method, so don't treat it as a fact. It is a reason to keep checking our own retention on AI-assisted videos against human-voiced ones.

---

## 4. Analytics: signal vs noise

### 4.1 First, the view-count changes (verified)
- **[OFFICIAL] Shorts, from 3/31/2025.** "Views will count the number of times a Short starts to play or replay, with no minimum watch time requirement… We will keep the existing Shorts view metric, now called 'Engaged views.'" ([Help 10059070](https://support.google.com/youtube/answer/10059070?hl=en))
- **[OFFICIAL] All formats, from 8/24/2026.** "Starting August 24, 2026, views across YouTube are counted from the first frame going forward — Shorts, Long Form, Podcasts, Live." "An engaged view is defined as clicking to watch or watching past the initial seconds." Hovering a thumbnail so it autoplays "is now counted as a view from the very first frame." ([YouTube Blog, 8/19/2026](https://blog.youtube/inside-youtube/engaged-views-youtube-explained/); Creator Insider announcement by Rene Ritchie, [8/17/2026](https://www.youtube.com/watch?v=2FBzExbYHxg); [Studio Content Manager changelog, "August 2026"](https://support.google.com/youtube/answer/9082582?hl=en-GB))
- **[OFFICIAL] What did not change.** "the vast majority of analytics remain anchored on engaged views, so the way metrics like CTR, AVD, and retention are calculated hasn't changed… there's no change to recommendations." ([Blog 8/19/2026](https://blog.youtube/inside-youtube/engaged-views-youtube-explained/)) Average view duration is "Average minutes watched among those who stayed to watch… calculated from engaged views." ([Help 9314415](https://support.google.com/youtube/answer/9314415?hl=en))
- **[OFFICIAL] November 2026 addition.** "Beginning November 2026, YouTube public view counts on video watch pages incorporate co-views by estimating the number of individual viewers watching together on TV screens." ([Help 2991785](https://support.google.com/youtube/answer/2991785?hl=en))
- **[OFFICIAL] Money and YPP.** "YPP earnings will still be based on 'engaged views' and 'engaged watch hours'. YPP eligibility will still be based on 'qualified views.'" (same) **[UNCERTAIN, minor]:** the older Shorts page ([10059070](https://support.google.com/youtube/answer/10059070?hl=en)) still says YPP is "based on 'Engaged Shorts views'," so YouTube's terms aren't fully consistent across pages. Read Studio's YPP progress bar as the source of truth.
- **[OUR ANALYSIS] Consequence:** public view counts from before and after 3/31/2025 (Shorts) or 8/24/2026 (long-form) are **not comparable**. Use **engaged views** for any trend line that crosses those dates, and for any Shorts comparison.

### 4.2 Signal vs noise, metric by metric

| Metric | Signal or noise | Why (source) | How to use it |
|---|---|---|---|
| **Public views** | Mostly noise for decisions | Exposure from the first frame, with co-views added ([Blog](https://blog.youtube/inside-youtube/engaged-views-youtube-explained/), [2991785](https://support.google.com/youtube/answer/2991785?hl=en)) | Use for reach and sponsor talk only. Decide on engaged views. |
| **Engaged views** | Signal | The old view definition, and what pays ([2991785](https://support.google.com/youtube/answer/2991785?hl=en)) | Main volume metric, especially for Shorts. Advanced Mode. |
| **Impressions** | Signal of distribution | Counted only when "the thumbnail is shown for more than 1 second and at least 50% of the thumbnail is visible"; **not** counted for external sites, end screens, cards, notifications, the mobile web, etc. ([Help 9314486](https://support.google.com/youtube/answer/9314486?hl=en)) | Rising impressions means YouTube is testing the video wider. More views than impressions usually means outside traffic ([7628154](https://support.google.com/youtube/answer/7628154?hl=en)). |
| **Impressions CTR** | Signal only in context; noisy at small n | "Half of all channels and videos on YouTube have an impressions CTR that can range between 2% and 10%." Avoid "Deciding without enough data," "Improving for small changes," and testing several titles one after another. Videos "with fewer than 100 views can see an even wider range" ([7628154](https://support.google.com/youtube/answer/7628154?hl=en)). CTR "will only show you… how attractive the thumbnail and the idea were" ([rHLjxrbXmmY](https://www.youtube.com/watch?v=rHLjxrbXmmY) ~10:26) | Compare only within the same traffic source and similar impression volume. Never compare across channels: it's "not really comparable like across channels" ([dhYIb72L1hU](https://www.youtube.com/watch?v=dhYIb72L1hU)). |
| **Subscriptions-feed CTR and AVD** | Clean signal | "kind of a clean way to isolate the content from the algorithm"; "probably all your videos have about maybe a 10% or less click-through rate" ([rHLjxrbXmmY](https://www.youtube.com/watch?v=rHLjxrbXmmY) ~35:55–37:02) | Studio > Reach > Browse features > subscriptions. Useful once we have enough subscribers watching. |
| **Average view duration / % viewed** | Signal, judged relative to length | Shorts rank on "avg. view duration and avg. % viewed" ([11914225](https://support.google.com/youtube/answer/11914225?co=YOUTUBE._YTVideoType%3Dshorts&hl=en)). "look at things relative to each other… relative to other videos that are similar length" ([rHLjxrbXmmY](https://www.youtube.com/watch?v=rHLjxrbXmmY) ~14:00) | Compare with our own same-length videos; YouTube's "typical retention" uses "your 10 latest videos of similar length" ([9314415](https://support.google.com/youtube/answer/9314415?hl=en)). Note: Shorts % viewed can top 100% when viewers loop; [OUR DATA] one of ours shows "145.8" avg % viewed (`wHCrmIPdCgg`, viral-centipede §1b). |
| **Retention curve** | The most actionable signal | Flat = held, gradual decline = losing interest, spikes = rewatches/shares, dips = skips/exits. Key moments need "at least 60 seconds long and… at least 100 views" ([9314415](https://support.google.com/youtube/answer/9314415?hl=en)) | Fix the biggest dip first. Move "top moments" earlier. |
| **Stayed to watch (Shorts)** | Signal: the Shorts "appeal" metric | "% of viewers who chose to view" is a named ranking input ([11914225](https://support.google.com/youtube/answer/11914225?co=YOUTUBE._YTVideoType%3Dshorts&hl=en)) | Compare with our own recent Shorts. YouTube publishes **no** target. |
| **Traffic sources** | Signal for *where* to package for | Definitions: Browse, Suggested, Search, Shorts, Channel pages, External, etc. ([9314355](https://support.google.com/youtube/answer/9314355?hl=en)) | Search terms and suggested-video lists tell you what to title and what to make next. Unrelated suggested sources are normal (§1.2). |
| **Subscribers gained / conversion** | Weak signal | "the signal of subscribe isn't as strong as a lot of people think… It might mean I'm going to watch it 10%." ([rHLjxrbXmmY](https://www.youtube.com/watch?v=rHLjxrbXmmY) ~37:28) | Track it, but don't optimize for it over watch time. **[UNCERTAIN]:** YouTube publishes no subs-per-view benchmark. |
| **Returning vs new viewers** | Signal of loyalty | Segmentable on the retention report ([9314415](https://support.google.com/youtube/answer/9314415?hl=en)). "the portion of their audience that watches every video is so tiny" ([rHLjxrbXmmY](https://www.youtube.com/watch?v=rHLjxrbXmmY) ~38:43) | Series and Parts are the tool for raising returning viewers. |
| **First-hours data** | Noise | "creators do tend to overfocus on… the immediate data… we're not basing decisions just on those initial moments" ([rHLjxrbXmmY](https://www.youtube.com/watch?v=rHLjxrbXmmY) ~6:14) | Judge at 7, 28 and 90 days. Look past 90 days for seasonality ([dhYIb72L1hU](https://www.youtube.com/watch?v=dhYIb72L1hU)). |
| **Third-party "benchmarks"** | Mostly noise | Self-selected samples (§3) | Use as a sanity check only. |

### 4.3 The Shorts-to-long-form funnel
- **[OFFICIAL]** Separate systems; Shorts "can help with audience discovery but can't hurt your Video performance" ([11914225](https://support.google.com/youtube/answer/11914225?co=YOUTUBE._YTVideoType%3Dshorts&hl=en)). "Shorts can help drive traffic to your long-form content too!" ([Blog 5/6/2025](https://blog.youtube/creator-and-artist-stories/debunking-common-myths-about-youtube-shorts/)). YouTube **publishes no conversion rate**.
- **[OFFICIAL] YPP math.** "Get 1,000 subscribers with 4,000 qualified watch hours" or "1,000 subscribers with 10 million qualified Shorts views" in 90 days. "Any qualified watch hours from Shorts views in the Shorts Feed won't count towards the 4,000 qualified public watch hours threshold." ([YPP overview](https://support.google.com/youtube/answer/72851?hl=en))
- **[THIRD-PARTY / UNCERTAIN]** The "Related video" link on a Short (Studio > Details) is widely described as the in-feed bridge to a long-form, and it needs advanced features ([Winprotips](https://winprotips.blog/add-related-video-to-youtube-shorts); I could not load an official Help page for it this session). **How its clicks are labeled in long-form traffic sources is not documented in what I could fetch.** Don't assume it shows up as "Suggested." Data should check Studio directly.
- **What to measure [OUR ANALYSIS]**, on each long-form:
  - Views and watch hours by traffic source, especially "Shorts" and any related-video detail.
  - Returning viewers.
  - Long-form watch hours per 1,000 *engaged* Shorts views, measured over 28 days.

---

## 5. What this means for @MeatballMyths

Our numbers, quoted exactly:

| Number | File |
|---|---|
| "YouTube: no Short has passed 2,445. Shorts send at most 0.49% of their viewers to long videos. Long-form watch hours toward YPP are about 13 of 4,000." | `channels/plan/growth-and-tt-to-yt-1117.md` |
| "Best Short is 2,445 (Studio). 8 of 86 reached 1,500. 0 of 86 reached 5,038 (5x of 1,007.5)." | `channels/research/viral-centipede-1117.md` §2 |
| "Studio's 48 h slice on our best Short: 43 views from YouTube search against 10 from the Shorts feed (n=55, `playbook-1116/analytics.md`)" | viral-centipede §2 |
| "99.3% new viewers, 0.0% regular. 46.3% stayed and 53.7% swiped (Studio 28d)" | viral-centipede §2 |
| "Our 15–18 s rule exists because 30 s+ Shorts have a median of 411 (n=11) against 1,159 (n=21)" | viral-centipede §2 |
| The YouTube twin of TikTok Part 2 "got **1,326** views (1.3x median), 91.6% average viewed, 12 likes, 0 comments and 0.535 engaged share" | viral-centipede §1 |
| House bugs: "(House bug median 1,138.5, n=30)" | viral-centipede §1 |
| Long-form: "no stable median in the repo yet. The baseline has n=11 Metricool long-forms, most with 2–5 views." | viral-centipede §5 (hit rule) |
| Centipede Part 2 (TikTok): "68.1% of traffic is TikTok Search and 31.2% is For You." | growth-and-tt-to-yt-1117.md |

**Practical takeaways** (each is OUR ANALYSIS of the sources above)

1. **YPP runs only through long-form watch hours.** Shorts-feed hours don't count, and "about 13 of 4,000" means long-form is the job. The Shorts route (10M qualified views in 90 days) would take roughly 9,900 Shorts at our 1,007.5 median (10,000,000 ÷ 1,007.5), and qualified views will be fewer than public views. It isn't realistic. Keep Shorts for discovery and testing ideas, and put production weight into **house-bug long-forms** (EP5 House Guests and episodes built from the Parts).
2. **Search is our proven YouTube lane, so title for it.**
   - YouTube search ranks on title, description and content match, plus watch time *for that query*.
   - Our best Short got 43 search views against 10 from the Shorts feed, and TikTok Part 2 was 68.1% search.
   - Every long-form and Short title should contain the plain phrase people type ("house centipede," "silverfish," "spider in my bathroom"). The description's first line should repeat it.
   - Don't rely on tags; YouTube says tags are mainly for misspellings.
3. **Judge Shorts on stayed-to-watch and engaged views, not public views.**
   - 46.3% stayed is our baseline to beat. YouTube publishes no target, so track it per Short against our own 28-day average.
   - Since 3/31/2025, our Studio Shorts "views" (median 1,007.5) count every start. Ask Data to add **engaged views** and **stayed to watch** columns to the scoreboard so hits are judged on what YouTube ranks and pays on.
4. **Long-form analytics are noise at our current size, so don't over-read them.**
   - With most long-forms at 2–5 views, CTR and AVD are meaningless. YouTube itself warns about videos "with fewer than 100 views."
   - Use the retention curve once a video passes 100 views. Key moments need 60 s+ and 100+ views.
   - Use the 30-second "intro" number as the long-form hook metric. "First 3 s" is a Shorts and TikTok rule, not a YouTube long-form one.
5. **Use Test & Compare on long-form packaging,** once advanced features are on. It picks the winner by watch time, which protects against clickbait. Our house rule that titles and thumbnails can't claim more than the source already fits how YouTube scores the test. It can't run on Shorts.
6. **Don't expect Shorts to feed long-form by themselves.** The systems are separate, and our 0.49% shows it.
   - Add the Short's related-video link to the matching long-form; this is a third-party-documented feature, so confirm it in Studio.
   - Make the Short a true chapter of that long-form, so the click delivers what the Short promised.
   - Measure long-form watch hours per 1,000 engaged Shorts views over 28 days.
7. **TikTok-to-YouTube stays a side bet, as the plan already says.** Beaupré says Home ranking barely weights traffic from embeds, ads or friend links, because it isn't predictive of Home behavior. So external TikTok traffic won't teach Home much. It adds watch hours only if those viewers actually watch, which agrees with the plan's "Bigger lever" note.
8. **Series and returning viewers.**
   - At "99.3% new viewers, 0.0% regular," every video starts cold.
   - YouTube says series work, especially on TV, and a deeper catalog helps viewers find a next video.
   - Numbered house-bug Parts, playlists in order and long-forms that collect the Parts are the sourced way to build regulars. Expect only a small share to watch everything; that is normal.
9. **Give videos time.** YouTube resurfaces evergreen videos "a month or… later," and in waves. Judge house-bug topics at 28 days or more, not on day 1. Our own late growth on YouTube (daddy longlegs, `EPimwC5VMgo`, viral-centipede §2 #3) is small but real.
10. **Two cautions.**
    - (a) Public long-form view counts jumped in meaning on 8/24/2026, so compare old and new long-forms on engaged views only.
    - (b) The vendor claim that AI-looking content retains "70% lower" is unverified. Our AI label stays on (YouTube: "We require that creators disclose realistic content that is made with altered or synthetic media", [HYW](https://www.youtube.com/howyoutubeworks/product-features/recommendations/)). The test that matters is our own retention data.

**Not covered on purpose**
- Livestreams, podcasts, multi-language dubbing, Shopping and ads. These are not relevant to the current plan.
- "Hidden" factors like upload time or tag stuffing, for which I found no current official support.

---

## Sources (all fetched 11/17/2026)

**Official: YouTube Help / How YouTube Works**
1. How YouTube Works: Recommendations: https://www.youtube.com/howyoutubeworks/product-features/recommendations/
2. How YouTube search works: https://www.youtube.com/howyoutubeworks/product-features/search/
3. Understand your content performance for YouTube's recommendation system (Help 16559650): https://support.google.com/youtube/answer/16559650?hl=en
4. Shorts search & discovery tips (Help 11914225): https://support.google.com/youtube/answer/11914225?co=YOUTUBE._YTVideoType%3Dshorts&hl=en
5. Impressions & click-through-rate FAQs (Help 7628154): https://support.google.com/youtube/answer/7628154?hl=en
6. Check your thumbnail impressions and watch time (Help 9314486): https://support.google.com/youtube/answer/9314486?hl=en
7. Understand your YouTube video reach / traffic sources (Help 9314355): https://support.google.com/youtube/answer/9314355?hl=en
8. Measure key moments for audience retention (Help 9314415): https://support.google.com/youtube/answer/9314415?hl=en
9. A/B test titles & thumbnails (Help 13861714): https://support.google.com/youtube/answer/13861714?hl=en
10. How engagement metrics are counted (Help 2991785; co-views Nov 2026): https://support.google.com/youtube/answer/2991785?hl=en
11. Get started creating YouTube Shorts (Help 10059070; 3/31/2025 view change): https://support.google.com/youtube/answer/10059070?hl=en
12. What's new in Studio Content Manager (Help 9082582; "August 2026" entry): https://support.google.com/youtube/answer/9082582?hl=en-GB
13. YouTube Partner Program overview & eligibility (Help 72851): https://support.google.com/youtube/answer/72851?hl=en

**Official: YouTube Blog**
14. What are 'Engaged' Views on YouTube? (8/19/2026): https://blog.youtube/inside-youtube/engaged-views-youtube-explained/
15. Shorts truths: Debunking common myths about YouTube Shorts (5/6/2025): https://blog.youtube/creator-and-artist-stories/debunking-common-myths-about-youtube-shorts/
16. YouTube Shorts deep dive: Todd Sherman and Jenny Hoyos (1/28/2025): https://blog.youtube/creator-and-artist-stories/youtube-shorts-deep-dive/

**Official: Creator Insider (YouTube staff).** Channel, date and title were checked with yt-dlp metadata.
17. "YouTube Algorithm 2026 - What Creators Need to Know," Rene Ritchie with Todd Beaupré (9/1/2026): https://www.youtube.com/watch?v=rHLjxrbXmmY. yt-dlp caption download hit HTTP 429, so the text was read from a third-party mirror of YouTube's own auto-captions: https://viewrankai.com/tools/youtube-transcript/rHLjxrbXmmY
18. "The YouTube Algorithms in 2025 — Explained!," Rene Ritchie with Todd Beaupré (1/23/2025): https://www.youtube.com/watch?v=dhYIb72L1hU (auto-captions via yt-dlp)
19. "Update to How Public Views Are Counted on YouTube," Rene Ritchie (8/17/2026): https://www.youtube.com/watch?v=2FBzExbYHxg (metadata checked; captions hit 429, and claims are quoted from the matching Blog post #14)

**Third-party (stated method; not random samples)**
20. quso.ai, "YouTube Shorts Length: The Sweet Spot, by the Data" (updated 6/29/2026; 108,138 Shorts): https://quso.ai/research/youtube-shorts-length
21. Retention Rabbit, "Beyond Views: The 2025 State of YouTube Audience Retention" (May 2025; 10,000+ videos, 1k+ creators; archived copy): https://web.archive.org/web/20260725211359/https://www.retentionrabbit.com/blog/2025-youtube-audience-retention-benchmark-report
22. Winprotips, "2 Ways to Add a Related Video to a YouTube Short" (feature description only): https://winprotips.blog/add-related-video-to-youtube-shorts
23. SocialPilot, "YouTube Algorithm September 2026" (cited only as the source of the unverified "fully decoupled" claim): https://www.socialpilot.co/youtube-marketing/youtube-algorithm

**Our data**
24. `channels/research/viral-centipede-1117.md` (Data, 11/17)
25. `channels/plan/growth-and-tt-to-yt-1117.md` (Social Studio, 11/17)
