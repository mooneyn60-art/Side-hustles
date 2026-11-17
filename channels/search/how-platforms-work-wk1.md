# How the platforms work: week 1 (YouTube + TikTok)

**For:** Meatball Myths (YouTube @MeatballMyths, `UCw98RQD81t_339LX5EJqcrg`; TikTok @meatballmyths). Pet-POV animation: Meatball is the human stick figure, Noodle the dog, Sauce the cat. Locked title pattern: `[Exact searched question]? Inside Noodle's/Sauce's [Body Part]`.
**Prepared by:** Search agent. **Sources accessed:** Mon Nov 16, 2026 (ET). Every URL below returned HTTP 200 on that date. Read-only: nothing was posted, edited, or committed.

**Labels:** **[OFFICIAL]** = YouTube Help, How YouTube Works, YouTube Official Blog, Creator Insider, TikTok Creator Academy, TikTok Newsroom, TikTok Support, or TikTok Community Guidelines. **[NON-OFFICIAL]** = a strategist, agency, or trade outlet. **[CHANNEL]** = our own public data, pulled today with yt-dlp and the channel's RSS feed. **[ANALYSIS]** = my inference, not a sourced fact.

---

## 0. Where the channel stands today [CHANNEL]

- About 90 Shorts and 13 long-form videos are public (yt-dlp, `/shorts` and `/videos` tabs). The two newest long-form uploads have 184 and 53 views ([KWOM2-mNmww](https://www.youtube.com/watch?v=KWOM2-mNmww), [viD-nbPdaxk](https://www.youtube.com/watch?v=viD-nbPdaxk)).
- All 15 items in the [RSS feed](https://www.youtube.com/feeds/videos.xml?channel_id=UCw98RQD81t_339LX5EJqcrg) are from Nov 13–17. 13 are Shorts, and most of their titles still carry series tags like "(Things Living In Your House #NN)".
- There are 5 public playlists. "Things Living In Your House" has 40 items, and the pet-POV episodes have no playlist of their own.
- Comments are on for the long-form videos, so the channel is probably not set to "made for kids". That setting matters a lot (see §2).
- **What this means [ANALYSIS]:** almost all of our output is Shorts. Shorts-feed watch time does not count toward YPP watch hours ([YPP Help](https://support.google.com/youtube/answer/72851?hl=en)). So the watch-hour question is really: **how do we get more long-form watched, and how do we move Shorts viewers onto it?**

---

## 1. How YouTube recommends long-form vs Shorts

**Separate surfaces**
- [OFFICIAL] YouTube lists its recommendation surfaces as the Homepage ("primarily a personalized surface"), Up Next, the Shorts player/Shorts Feed, destination pages, and channel pages ([How YouTube recommendations work](https://support.google.com/youtube/answer/16089387?hl=en)).
- [OFFICIAL] Analytics reports them as separate traffic sources:
  - **Browse features:** Home, Subscriptions, Watch Later, Trending/Explore.
  - **Suggested videos:** "suggestions that appear next to or after other videos, and from links in video descriptions".
  - **Shorts:** "the Shorts vertical viewing experience".
  - **YouTube search** and **Playlists** are also their own sources ([Understand your video reach](https://support.google.com/youtube/answer/9314355?hl=en)).

**Separate systems**
- [OFFICIAL] "We've built separate recommendation systems optimized for each [format]. While these systems understand cross-format viewing, they primarily focus on serving the unique viewing patterns of each format… we haven't seen evidence of Shorts negatively impacting long-form performance." (YouTube Blog, May 6, 2025: [Shorts truths](https://blog.youtube/creator-and-artist-stories/debunking-common-myths-about-youtube-shorts/))
- [OFFICIAL] Creator Insider, Jul 28, 2022: YouTube "separate[s] Shorts and long form watch history, so when someone discovers a new channel via Shorts, we're not currently using that to inform what longer videos are recommended to them outside of the Shorts experience" ([Shorts and The Algorithm](https://www.youtube.com/watch?v=DY_oxuM8niQ)).
- [NON-OFFICIAL, quoting YouTube] Three weeks later, vidIQ reported that YouTube's Todd Beaupré tweeted: "Recommendations now consider recent long-form videos from channels the viewer watches in Shorts" ([vidIQ, Aug 22, 2022](https://vidiq.com/blog/post/youtube-recommends-long-form-videos-shorts-viewers/)). The 2025 blog's line "understand cross-format viewing" is the current official wording. **YouTube has published no numbers on how strong that cross-over is.**

**Signals and satisfaction**
- [OFFICIAL] The main signals are watch history, search history, subscriptions, likes, dislikes, "Not interested", "Don't recommend channel", and satisfaction surveys, which help the system "understand satisfaction, not just watch time" ([16089387](https://support.google.com/youtube/answer/16089387?hl=en)).
- [OFFICIAL] Different surfaces lean on different signals. For the next video to play, "the video you're currently watching" is the main signal. For the homepage, the system "primarily relies on your watch history" ([16089387](https://support.google.com/youtube/answer/16089387?hl=en)).
- [OFFICIAL] YouTube measures "valued watchtime" through 1–5 star surveys, and only 4–5 star ratings count. A model predicts survey answers for viewers who never take one. When watch time was added in 2012, views immediately dropped 20% ([On YouTube's recommendation system, 2021](https://blog.youtube/inside-youtube/on-youtubes-recommendation-system/)).
- [OFFICIAL] In the Shorts feed, "those views feel… more like Impressions than traditional views". Early views are "very exploratory". There is no 5- or 10-Shorts-a-day threshold that unlocks reach. Deleting and reposting a Short "gets seen as spam" ([Creator Insider, Aug 23, 2023](https://www.youtube.com/watch?v=n3jsYK_-aRU)).
- [OFFICIAL] Studio's Shorts metric is "Stayed to watch": the share of viewers who stayed "past the initial seconds of a Short" ([9314355](https://support.google.com/youtube/answer/9314355?hl=en)).
- [NON-OFFICIAL] Paddy Galloway's team studied 3.3B Shorts views. The algorithm "does… appear to favor longer videos (40 seconds+) that hold viewer duration well", and engagement metrics "don't seem massively important" ([LinkedIn](https://www.linkedin.com/posts/paddy-galloway-459b8913a_we-studied-33-billion-views-to-decode-the-activity-7053697597592498176-PAkf)).

---

## 2. What actually moves Shorts viewers to long-form

| Lever | Officially documented? | What we know |
|---|---|---|
| **Related video link** on a Short | **Yes** | [OFFICIAL] Studio → Content → the Short → Related video. It needs **advanced feature access**. The target must be public or unlisted. "Viewers will see a clickable link below your channel handle" ([Help 14075157](https://support.google.com/youtube/answer/14075157?hl=en); [feature access](https://support.google.com/youtube/answer/9890437?hl=en)). It is the only clickable link in a Short ([Sharing links](https://support.google.com/youtube/answer/13748639?hl=en)). |
| **YouTube's own conversion playbook** | **Yes (Blog, Jul 14, 2026)** | [OFFICIAL] 1) Use Related Videos as "the most effective tool" and match the viewer's intent. 2) Add a verbal and visual call to action "during the final 5 seconds", pointing at the link or flashing the long-form thumbnail. 3) "Reward the click immediately": "The first 5 to 10 seconds of your long video should directly address the topic… promised in the Short." It also warns that some viewers are "Shorts-Only" and "may never naturally click on a 10-minute video" ([YouTube Blog](https://blog.youtube/creator-and-artist-stories/youtube-related-videos-traffic-guide/)). |
| **Conversion rates** | **No official number** | [NON-OFFICIAL] Matt Koval says "only about 0.3% click over" on the educational channels he works with. In the same thread, Kevin Daigle describes a 60M-subscriber channel where a Short with several hundred million views sent about 1,500 long-form clicks that month ([LinkedIn](https://www.linkedin.com/posts/mattkoval_youtube-creatoreconomy-creators-activity-7246568113830264836-WJP2)). Also in that thread, Rene Ritchie of YouTube (a comment, not a policy doc) says it "can work great" with a strong call to action and highlighting the link. [NON-OFFICIAL] Spotter analyzed 5,000+ channels: only 2% got noticeable long-form traffic from the link. Channels with more than 1M monthly long-form views that did saw "an average 10% increase in first 30 days views" ([Spotter, Mar 28, 2024](https://spottercommunity.beehiiv.com/p/related-shorts)). Both are small, self-selected samples. |
| **Pinned comments** | Only partly | [OFFICIAL] "URLs placed in YouTube Shorts comments and Shorts descriptions are non-clickable." Long-form comment and description URLs *are* clickable, but only with advanced features ([13748639](https://support.google.com/youtube/answer/13748639?hl=en)). **So a pinned comment on a Short cannot carry a working link.** On long-form, a pinned comment with a link works, but **YouTube has published no data that it raises views**. Treat it as anecdotal. |
| **End screens** | Long-form only | [OFFICIAL] End screens go in the last 5–20 s of a video that is at least 25 s long. They hold up to 4 elements on 16:9, can show a video, a **playlist**, "best for viewer", or Subscribe, and are reported in Analytics ([Help 6388789](https://support.google.com/youtube/answer/6388789?hl=en)). They appear as their own traffic source ([9314355](https://support.google.com/youtube/answer/9314355?hl=en)). The end-screen Help page does not mention Shorts. YouTube's list of clickable Short elements includes only the Related Video link ([13748639](https://support.google.com/youtube/answer/13748639?hl=en)). **In practice, Shorts get no end screens.** |
| **Playlists** | Yes, as a traffic source | [OFFICIAL] "Playlists" is its own traffic source and includes your own playlists ([9314355](https://support.google.com/youtube/answer/9314355?hl=en)). An end screen can feature a playlist ([6388789](https://support.google.com/youtube/answer/6388789?hl=en)). YouTube publishes no figure on how much watch time playlists add. |
| **"Made for kids" setting** | Yes, and it's a trap | [OFFICIAL] Made-for-kids videos lose end screens, cards, comments, notifications, and "Save to playlist" ([Help 9632097](https://support.google.com/youtube/answer/9632097?hl=en)). "Animated content that appeals to everyone" is listed as a *general audience* example ([MFK FAQ](https://support.google.com/youtube/answer/9684541?hl=en)). **[ANALYSIS]** Set the audience honestly. If our cartoon ever gets set to made for kids, most of the levers in this table switch off. |

**Bottom line:** the Related Video link and YouTube's call-to-action/reward-the-click playbook are the only *officially documented* Shorts-to-long-form tools. Every conversion rate in circulation is anecdotal and low (about 0.3–10%). **YouTube has never published a conversion figure.**

---

## 3. How Browse vs Search traffic is earned

**Search**
- [OFFICIAL] Search ranks on **relevance, engagement, and quality**, weighted differently by type of search.
  - Relevance means "how well the title, tags, description, and video content match your search query".
  - Engagement includes "the watch time of a particular video for a particular query".
  - Quality looks for channels that show "expertise, authoritativeness, and trustworthiness on a given topic".
  - Results are personalized by search and watch history ([How YouTube search works](https://support.google.com/youtube/answer/16090438?hl=en); [How YouTube Works: Search](https://www.youtube.com/howyoutubeworks/product-features/search/)).
- [OFFICIAL] Tags "play a minimal role in your video's discovery" unless a word is commonly misspelled. The title, thumbnail, and description are "more important" ([Help 146402](https://support.google.com/youtube/answer/146402?hl=en)).
- [OFFICIAL] For medical or scientific topics, YouTube works to surface "high-quality and authoritative content from trusted sources" ([Help 9962575](https://support.google.com/youtube/answer/9962575?hl=en)). **[ANALYSIS]** Pet-health questions like chocolate, grapes, or chicken bones probably fall under this. Citing vets or the ASPCA on screen and in the description is the honest way to show quality.

**Browse (Home) and Suggested (Up Next)**
- [OFFICIAL] The homepage "primarily relies on your watch history". Up Next uses "the video you're currently watching as the main signal" ([16089387](https://support.google.com/youtube/answer/16089387?hl=en)). The system "compares your viewing habits with those that are similar" ([2021 blog](https://blog.youtube/inside-youtube/on-youtubes-recommendation-system/)).
- So browse is earned through click → watch time → survey-predicted satisfaction among similar viewers. No keyword match is involved ([2021 blog](https://blog.youtube/inside-youtube/on-youtubes-recommendation-system/)).
- [OFFICIAL] Recommendations "drive a significant amount of the overall viewership on YouTube, even more than channel subscriptions or search" ([2021 blog](https://blog.youtube/inside-youtube/on-youtubes-recommendation-system/)).
- [NON-OFFICIAL] Galloway says a viewer who watches "four or five videos in a row" is "more likely to have your content recommended on their home page" than one who only subscribes ([Business Insider, Oct 2022](https://www.businessinsider.com/youtube-strategist-paddy-galloway-how-to-grow-shorts-mrbeast-preston-2022-10)).
- **[ANALYSIS]** For a channel with 53–184 views per long-form video, search is the dependable on-ramp, because the query does the targeting. Browse comes once enough watch time from similar viewers builds up.

**Claims with no official backing:**
- That a specific CTR or average-view-duration "threshold" triggers browse.
- That posting time matters for Shorts. Netinfluencer reports that Todd Sherman said on Creator Insider that YouTube does not factor in posting time ([Netinfluencer, trade press](https://www.netinfluencer.com/youtube-debunks-common-myths-about-shorts-as-format-gains-traction/)).
- That tags meaningfully boost ranking. The Help page above says the opposite.

---

## 4. How TikTok search and the For You feed treat a new series or account

**For You feed**
- [OFFICIAL] FYF ranking uses user interactions, "video information… captions, sounds, and hashtags", and device/account settings, which get lower weight. "Whether a user finishes watching a longer video from beginning to end" gets greater weight.
- [OFFICIAL] "Neither follower count nor whether the account has had previous high-performing videos are direct factors." New users pick interest categories "like pets" ([Newsroom: How TikTok recommends videos](https://newsroom.tiktok.com/en-us/how-tiktok-recommends-videos-for-you)).
- **[ANALYSIS]** So a new account or series is not penalized for being new, but it doesn't get a boost either. Each video is judged on its own completion and engagement.
- [OFFICIAL] FYF eligibility standards (effective Sep 24, 2026): some content is made FYF-ineligible, but "people may still find it through search or by going to a creator's account". Ineligibility shows up in analytics ([FYF Eligibility Standards](https://www.tiktok.com/community-guidelines/en/fyf-standards)).

**Search**
- [OFFICIAL] "Search is different from the For You feed, as it values relevance over video views and engagement."
- [OFFICIAL] "Use relevant keywords in your video, subtitles, and captions." "Your video titles and covers should clearly showcase your topic." "Irrelevant text stacking will actually negatively affect your video traffic" ([Creator Academy: Driving video traffic: Search, updated Aug 18, 2026](https://www.tiktok.com/creator-academy/article/driving-video-traffic-search)).
- [OFFICIAL] "Use this topic and other relevant keywords in your description and text-on-screen." Don't "overload your content with irrelevant or redundant hashtags." Publish while a topic's search popularity is rising.
- [OFFICIAL] Search Analytics shows search views, search view %, impressions, CTR, and average search ranking ([Creator Academy: why Search Analytics matter](https://www.tiktok.com/creator-academy/en/article/Why-Search-Analytics-Matter)).
- [OFFICIAL] Creator Search Insights surfaces often-searched topics and a **content gap** filter: topics that are searched a lot but covered by few videos. Search value also factors into the Creator Rewards Program ([Newsroom, Mar 13, 2024](https://newsroom.tiktok.com/en-US/creator-search-insights)).
- **Speech:** TikTok's own pages say "in your video" and "subtitles", but **no official page I found says spoken audio is indexed.** That claim comes from third parties, e.g. [TokConnect](https://tokconnect.com/guides/how-tiktok-search-works/) [NON-OFFICIAL]. **[ANALYSIS]** Burned-in subtitles of the spoken question cover both cases.
- [NON-OFFICIAL, trade press] Since 2026, published videos show keywords TikTok added automatically, and **Manage keywords** lets creators block them or suggest others. TikTok reviews the suggestions ([Netinfluencer, Jun 22, 2026](https://www.netinfluencer.com/tiktok-adds-post-publish-keyword-management-tool-for-creator-videos/)). I found no TikTok Help page confirming this.

**Series and playlists**
- [OFFICIAL] TikTok **"Series" is a paywalled product**. It requires 10,000+ followers, an account at least 30 days old, and age 18+ ([TikTok Support: Series](https://www.tiktok.com/support/faq_detail?id=7639210131833756180)). It is not a free way to group episodes, so it's off the table for us now.
- [OFFICIAL] Free **Playlists** let viewers "watch related posts in a sequence". A post can be in only one playlist. They "aren't currently available to everyone" ([TikTok Support: Playlists](https://support.tiktok.com/en/using-tiktok/creating-videos/creator-playlist)).
- [OFFICIAL] Hashtags exist and help the system understand the video ([Newsroom](https://newsroom.tiktok.com/en-us/how-tiktok-recommends-videos-for-you)).
- **No official backing:** the idea that a "#series" tag or "Part 2" naming earns extra distribution. I found nothing official.

---

## 5. Five changes for Meatball Myths, ranked by expected watch-hour impact [ANALYSIS, with sourced reasons]

1. **Make long-form pet-POV episodes that answer searched questions, titled in the locked pattern.**
   - *Why it ranks first:* qualified watch hours come only from public long-form videos ([YPP](https://support.google.com/youtube/answer/72851?hl=en)), and we have just 13 ([§0](#0-where-the-channel-stands-today-channel)).
   - Search matches the title, description, and *video content* to the query, then rewards watch time per query ([16090438](https://support.google.com/youtube/answer/16090438?hl=en)).
   - The 20 questions in `title-pattern-1116.md` are already sorted by evidence. Lead with the exact question in the title, and say it in the first lines of the description and in the first seconds of the video.
   - For toxic-food topics, cite the ASPCA on screen to meet the quality bar for health topics ([9962575](https://support.google.com/youtube/answer/9962575?hl=en)).

2. **Add a topic-matched Related Video link to all ~90 Shorts, with a call to action in the last 5 s.**
   - This is the only clickable link a Short allows ([13748639](https://support.google.com/youtube/answer/13748639?hl=en)). It needs advanced features; check Studio → Settings → Channel → Feature eligibility ([9890437](https://support.google.com/youtube/answer/9890437?hl=en)).
   - Follow YouTube's playbook: match intent, have Noodle or Sauce point at the link, and answer the Short's promise in the first 5–10 s of the long-form ([YouTube Blog](https://blog.youtube/creator-and-artist-stories/youtube-related-videos-traffic-guide/)).
   - *Why it's second:* it costs almost nothing across the whole back catalog, but reported click-through is low (about 0.3%, [Koval](https://www.linkedin.com/posts/mattkoval_youtube-creatoreconomy-creators-activity-7246568113830264836-WJP2)). The gain only counts if #1 gives viewers good long-form to land on. Measure it with the destination video's Shorts traffic source ([9314355](https://support.google.com/youtube/answer/9314355?hl=en)).

3. **Build a binge path on every long-form video: an end screen, a pet-POV playlist, and a pinned comment.**
   - Add an end screen with "best for viewer" plus the playlist in the last 20 s ([6388789](https://support.google.com/youtube/answer/6388789?hl=en)).
   - Create one public "Inside Noodle & Sauce" playlist ordered by the question sequence; it would be a Playlists traffic source ([9314355](https://support.google.com/youtube/answer/9314355?hl=en)).
   - Pin a comment linking the next episode; long-form comment links are clickable ([13748639](https://support.google.com/youtube/answer/13748639?hl=en)). The pinned-comment lift is anecdotal.
   - Up Next is driven by the current video ([16089387](https://support.google.com/youtube/answer/16089387?hl=en)), and multi-video sessions predict Home recommendations ([Galloway/BI](https://www.businessinsider.com/youtube-strategist-paddy-galloway-how-to-grow-shorts-mrbeast-preston-2022-10)). **Keep the audience set to "not made for kids", or all of this switches off** ([9632097](https://support.google.com/youtube/answer/9632097?hl=en)).

4. **Write long-form for satisfaction, not just clicks.**
   - Open on the answer, with no logo intro ([YouTube Blog](https://blog.youtube/creator-and-artist-stories/youtube-related-videos-traffic-guide/)).
   - Make sure the organ tour delivers what the title promises. YouTube weights survey-predicted "valued watchtime", where only 4–5 star ratings count ([2021 blog](https://blog.youtube/inside-youtube/on-youtubes-recommendation-system/)), and satisfaction surveys are a primary signal ([16089387](https://support.google.com/youtube/answer/16089387?hl=en)).
   - *Why it's fourth:* it multiplies watch time per view on every surface, but only once #1 and #2 are bringing views in.

5. **TikTok: put the exact searched question in the caption, the on-screen text, and the subtitles. Pick topics from Creator Search Insights' content-gap tab.**
   - Search "values relevance over video views", and covers and titles should state the topic ([Creator Academy](https://www.tiktok.com/creator-academy/article/driving-video-traffic-search)).
   - Use the topic "in your description and text-on-screen", with no hashtag stuffing ([Creator Academy](https://www.tiktok.com/creator-academy/en/article/Why-Search-Analytics-Matter)). Find gap topics with Creator Search Insights ([Newsroom](https://newsroom.tiktok.com/en-US/creator-search-insights)).
   - Check auto-added keywords with Manage keywords, if it's available ([Netinfluencer](https://www.netinfluencer.com/tiktok-adds-post-publish-keyword-management-tool-for-creator-videos/), unconfirmed by TikTok).
   - *Why it's last:* TikTok watch time adds no YouTube watch hours. Its value is audience-building and testing which questions land before we spend long-form effort on them. Skip Series (paywalled, 10k-follower minimum: [Support](https://www.tiktok.com/support/faq_detail?id=7639210131833756180)). Use Playlists only if the account has them ([Support](https://support.tiktok.com/en/using-tiktok/creating-videos/creator-playlist)).

---

## Sources (all accessed Nov 16, 2026)

**Official: YouTube**
- How YouTube recommendations work: https://support.google.com/youtube/answer/16089387?hl=en
- How YouTube search works: https://support.google.com/youtube/answer/16090438?hl=en
- How YouTube Works, Search: https://www.youtube.com/howyoutubeworks/product-features/search/
- How YouTube works for you: https://support.google.com/youtube/answer/9962575?hl=en
- Understand your video reach (traffic sources): https://support.google.com/youtube/answer/9314355?hl=en
- Add a related video to Shorts: https://support.google.com/youtube/answer/14075157?hl=en
- Sharing links with your audiences: https://support.google.com/youtube/answer/13748639?hl=en
- Feature access: https://support.google.com/youtube/answer/9890437?hl=en
- Add end screens: https://support.google.com/youtube/answer/6388789?hl=en
- Add tags: https://support.google.com/youtube/answer/146402?hl=en
- Watching made-for-kids content: https://support.google.com/youtube/answer/9632097?hl=en
- Made-for-kids FAQ: https://support.google.com/youtube/answer/9684541?hl=en
- YPP eligibility: https://support.google.com/youtube/answer/72851?hl=en
- YouTube Blog, Shorts truths (May 6, 2025): https://blog.youtube/creator-and-artist-stories/debunking-common-myths-about-youtube-shorts/
- YouTube Blog, converting Shorts views (Jul 14, 2026): https://blog.youtube/creator-and-artist-stories/youtube-related-videos-traffic-guide/
- YouTube Blog, On YouTube's recommendation system (Sep 15, 2021): https://blog.youtube/inside-youtube/on-youtubes-recommendation-system/
- Creator Insider, Shorts and The Algorithm (Jul 28, 2022): https://www.youtube.com/watch?v=DY_oxuM8niQ
- Creator Insider, YouTube Shorts Algorithm Explained (Aug 23, 2023): https://www.youtube.com/watch?v=n3jsYK_-aRU

**Official: TikTok**
- Newsroom, How TikTok recommends videos: https://newsroom.tiktok.com/en-us/how-tiktok-recommends-videos-for-you
- Newsroom, Creator Search Insights (Mar 13, 2024): https://newsroom.tiktok.com/en-US/creator-search-insights
- Creator Academy, Driving video traffic: Search: https://www.tiktok.com/creator-academy/article/driving-video-traffic-search
- Creator Academy, why Search Analytics matter: https://www.tiktok.com/creator-academy/en/article/Why-Search-Analytics-Matter
- Community Guidelines, FYF Eligibility Standards: https://www.tiktok.com/community-guidelines/en/fyf-standards
- Support, Series: https://www.tiktok.com/support/faq_detail?id=7639210131833756180
- Support, Playlists: https://support.tiktok.com/en/using-tiktok/creating-videos/creator-playlist

**Non-official (strategists and trade press)**
- Paddy Galloway, 3.3B Shorts views study (LinkedIn): https://www.linkedin.com/posts/paddy-galloway-459b8913a_we-studied-33-billion-views-to-decode-the-activity-7053697597592498176-PAkf
- Business Insider on Paddy Galloway (Oct 18, 2022): https://www.businessinsider.com/youtube-strategist-paddy-galloway-how-to-grow-shorts-mrbeast-preston-2022-10
- vidIQ, long-form recommended to Shorts viewers (Aug 22, 2022): https://vidiq.com/blog/post/youtube-recommends-long-form-videos-shorts-viewers/
- Matt Koval, Related video click-through (LinkedIn): https://www.linkedin.com/posts/mattkoval_youtube-creatoreconomy-creators-activity-7246568113830264836-WJP2
- Spotter, Related Shorts data (Mar 28, 2024): https://spottercommunity.beehiiv.com/p/related-shorts
- Netinfluencer, YouTube debunks Shorts myths: https://www.netinfluencer.com/youtube-debunks-common-myths-about-shorts-as-format-gains-traction/
- Netinfluencer, TikTok Manage Keywords (Jun 22, 2026): https://www.netinfluencer.com/tiktok-adds-post-publish-keyword-management-tool-for-creator-videos/
- TokConnect, How TikTok search works: https://tokconnect.com/guides/how-tiktok-search-works/

**Limits:**
- I didn't cite Film Booth, Think Media, or Creator Science. I found no page from them with a specific, checkable claim on these questions in the time I had.
- Creator Academy pages are rendered by JavaScript. I read them through headless Chrome, and the quotes are from that render.
- YouTube has no Help page that says outright "Shorts have no end screens". That row is inferred from the end-screen and link-clickability pages.
