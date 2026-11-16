# Shorts "view jail" + long-form push plan: Meatball Myths, Sun 11/15/2026

Owner: Social: Packaging & Thumbnails. **Read-only research.** Nothing was changed in YouTube Studio, nothing was posted, and no repo was edited. All times are ET (America/New_York).

**Data used (channel claims come only from these):**
- **Studio export:** "Last 90 days", Aug 17–Nov 14, 2026, 249 videos. Path: `/home/box/Downloads/meatball-myths-analytics-last-90-days/Table data.csv`. Its era split (99 Meatball-era videos: 86 Shorts and 13 long-forms; 150 pre-rebrand) is in `/workspace/packaging/winners-baseline-1115.csv`.
- **Metricool (read-only, blogId 8135499):** YouTube daily views, subscribers gained and lost, and subscriber count from Aug 17 to Nov 12 (Metricool runs about 3 days behind). Also per-video views, watch minutes, likes, comments and shares for 82 videos published Oct 22 onward. Metricool's traffic-source call returned no rows.
- **Team research:** files already in the skills repo (`skills/channel-brain/KNOWLEDGE.md`, `MASTER_ORDERS.md`, `MONETIZATION_PLAN.md`). These are marked "(team research)" wherever they are used.

Platform claims are sourced at the bottom (§ Sources). Each one is tagged [S1], [S2] and so on.

---

## (a) Diagnosis, with numbers

### 1. It's a hard ceiling at about 1,000 views per Short, not a slow decline
- 86 Meatball Shorts (Oct 22 to Nov 15) earned **76,649 views**. Per-Short views by percentile:
  - p10: 110
  - p25: 432
  - **median: 1,007**
  - p75: 1,158
  - p90: 1,362
- **43 of 86 Shorts (50%) landed between 900 and 1,399 views.** Only 6 reached 1,400–1,999, and only **2 passed 2,000**:
  - Daddy Longlegs: 2,445
  - "The Bug You Squish Is Protecting You": 2,316
- 26 Shorts (30%) stayed under 500.
- The median barely moves week to week:

  | Week (publish date) | Median views |
  |---|---:|
  | 10/22–10/25 | 960 |
  | 10/26–11/01 | 993 |
  | 11/02–11/08 | 1,153 |
  | 11/09–11/15 | 921 |

- Team research says a Short gets about 85% of its views on day 0 and about 1% after day 2. So these numbers are effectively final (team research, `KNOWLEDGE.md` 11/13).
- **What it means:** almost every Short gets one test batch of about 1,000 viewers and is never widened. That matches YouTube's description of how ranking works. Shorts are judged on:
  - whether viewers **chose to view or swiped**;
  - average view duration and average % viewed;
  - likes and surveys [S1][S2].

  YouTube widens a Short to more viewers only when it beats competing Shorts for the same viewers [S1].

### 2. % viewed separates the Shorts that clear the floor from the ones that don't, but it doesn't break the ceiling
| Avg % viewed | Shorts | Median views | Median length |
|---|---:|---:|---:|
| < 50% | 14 | **229** | 30 s |
| 50–70% | 31 | 950 | 24 s |
| 70–90% | 21 | 1,148 | 18 s |
| 90–110% | 13 | 1,158 | 20 s |
| > 110% (loops) | 7 | 1,153 | 16 s |

- The rank correlation between % viewed and views is 0.45.
- Below 50% viewed, a Short dies at about 230 views. From 70% up, the median plateaus at about 1,150, even at 110%+ looping.
- So retention gets a Short **into** the 1K test pool but is not what pushes it past. The missing signal is most likely the **viewed-vs-swiped share in the first second**, plus likes, shares and comments.
- **Swiped share is not in the export.** It's in Studio's "Stayed to watch" / "Viewed vs swiped away" card [S2]. Team research from 11/11 measured roughly 60% swiping away in the first second (1,820 engaged of 4,603) and 44% engaged plays across Shorts (`KNOWLEDGE.md`).

### 3. Shorter is better, up to a point
| Length | Shorts | Median views | Median % viewed |
|---|---:|---:|---:|
| ≤ 17 s | 20 | **1,187** | 90% |
| 18–21 s | 21 | 996 | 75% |
| 22–25 s | 20 | 1,055 | 62% |
| 26–34 s | 20 | 763 | 56% |
| ≥ 35 s | 5 | **285** | 48% |

- Median length by phase:

  | Phase | Median length | Median views |
  |---|---:|---:|
  | 10/22–10/28 | 24 s | 993 |
  | 10/29–11/10 | 16 s | **1,148** (best phase; 81.8% median viewed) |
  | 11/11–11/15 | 20 s | 921 (63.6% median viewed) |

- The current rule is 16–20 s with no Short under 15 s (MASTER_ORDERS, Nolan 11/10). The data supports staying at the **short end of that band (16–18 s)**.

### 4. Cadence changed a lot. Volume isn't the cause, but the extra slots went to weak topics.
- Shorts per day by phase:

  | Dates | Shorts | Per day |
  |---|---:|---:|
  | 10/22–10/28 | 34 | 4.9 |
  | 10/29–11/10 | 31 | 2.4 |
  | 11/11–11/14 | 20 | 5.0 |

- On days with 5 or more Shorts, the median was **969** views (n=41). On days with 3 or fewer, it was **1,121** (n=41).
- That gap is confounded by what filled the extra slots:
  - 10/22–10/28: TRUE/FALSE and Investigates Shorts.
  - 11/13–11/14: news Shorts (FAA, Nvidia) and pet tests.
- Team research found no effect from the number of Shorts per day once topic was controlled (about 166 comparisons, research 100). YouTube also says no posting cadence is required and that upload frequency isn't rewarded [S1][S5].
- **Conclusion:** keep the 3-a-day cap (MASTER_ORDERS 11/6). Fill every slot with a proven topic instead of adding volume.

### 5. Topic and series: the house show works, everything else drags the median down
| Series / type | Shorts | Median views | Median % viewed | Median length |
|---|---:|---:|---:|---:|
| Things Living In Your House | 42 | **1,127** | 77% | 20 s |
| Is This Spider Venomous? | 6 | 1,056 | **83%** | 18 s |
| Meatball vs Spiders | 2 | 1,118 | 70% | 23 s |
| Would Meatball Survive? | 6 | 1,021 | 63% | 22 s |
| Untagged animal | 13 | 1,017 | 65% | 23 s |
| TRUE/FALSE, "Lied", "Myth" | 8 | **493** | 58% | 34 s |
| News (FAA, Nvidia) | 4 | **184** | 54% | 35 s |
| Investigates / conspiracy | 5 | **27** | 47% | 23 s |

- Mites (median 1,340, 95.5% viewed), roaches (1,362), centipede/"don't squish" (1,158, 92.8% viewed) and spiders (1,085) lead.
- Dogs are weakest (859, 58% viewed). One dog Short got 3 views.
- Mixing news, conspiracy and pet tests with the house show trains the system on several different audiences [S4 creator analysis].

### 6. The rebrand drop-off and the audience mismatch
- **Daily channel views (Metricool):**

  | Period | Views | Per day |
  |---|---:|---:|
  | Aug 17–31 (last Bartolozzi uploads Aug 17–25) | 200,912 | 13,394 |
  | Sep 1–30 | 22,575 | |
  | Oct 1–18 (no uploads) | 908 | about 50 |
  | Oct 19–Nov 12 (Meatball era) | 75,833 | **about 3,033** |

- **Bartolozzi-era Shorts:**
  - 11 Shorts posted Aug 17–25 earned **165,457** views in the window, which is **54% of all 307,224 channel views**.
  - Their median was **6,360** views and **96%** viewed. The top one had 71,384.
  - The Meatball median is **1,007**, about 6.3 times lower.
- **Subscribers:**
  - The count was already **942 on Oct 19**, before the first Meatball upload. It reached 1,010 by Nov 13.
  - So about **93% of today's subscribers came from the old reaction/commentary era**.
  - From Oct 19 on: +98 gained, −29 lost.
- **What this means:** the subscriber base is mostly an audience that never chose bug and animal content. Viewer history and channel affinity personalize Shorts recommendations [S1], so that early signal points at the wrong viewers.
- The export can't show what share of Meatball views come from subscribers versus non-subscribers. Studio's Audience tab can.

### 7. Engagement is very low
- Metricool, 82 Meatball-era videos, about 64,008 views:

  | Signal | Total | Per 1,000 views |
  |---|---:|---:|
  | Likes | 661 | 10.3 |
  | **Comments** | **17** | 0.27 |
  | **Shares** | **9** | 0.14 |

- Likes and surveys are the "satisfaction" signals YouTube names [S1][S3]. With almost no comments or shares, a Short has little beyond retention to argue for a wider push.

### 8. Shorts don't feed the long-forms yet
- 13 Meatball long-forms totaled **946 views** in the export.
- Team research (Windsor, 10/22–11/09) found that long-forms got **0 of 655** views from the Shorts feed. Their views came from related videos (313), subscribers (300) and search (23). Shorts send at most 0.49% of their views on to long-form (`KNOWLEDGE.md`, research 94/100).
- The Related-video bridge has only just been locked (`related-video-rule.md`, 11/15). It isn't applied channel-wide yet.

---

## (b) Shorts fixes, ranked by expected impact

1. **One-second hook, built for the swipe.** Highest impact; targets the missing "chose to view" signal [S1][S2].
   - The first frame already shows the creature mid-action, with a 3–5-word on-screen claim that matches the first spoken line. No establishing shot, no logo, no "Meatball here".
   - The best two openers say the twist straight away: "Are Daddy Longlegs the most venomous…?" (96.6% viewed) and "The bug you squish is protecting you" (109.6%).
   - No textbook biology in seconds 0–6. Studio's AI saw 15–24% drops between 0:04 and 0:06 when narration turned textbook (team research 11/11).
   - Owner: Scriptwriter (hooks), Social Studio/Claude (edit).
2. **Topic focus: only the proven shows for the next 2 weeks.** House bugs, house spiders, mites, roaches, bed bugs and centipedes, under *Things Living In Your House* and *Is This Spider Venomous?*.
   - Pause TRUE/FALSE, Investigates/conspiracy, news and dog tests on the main channel. Their medians are 493, 27, 184 and 859.
   - Lean into *Is This Spider Venomous?*. It has the best % viewed (83%) and the best Shorts title CTR in the baseline (5.20% impression-weighted).
3. **Loop endings plus a shorter cut (16–18 s).**
   - Shorts at 17 s or less have a median of 1,187 views at 90% viewed. At 26 s or more, views drop to 763 and below.
   - The last line asks the question and runs straight into the hook. The hook and the last line share a scene (already in MASTER_ORDERS).
   - Never say "subscribe" or signal an ending. Team research found that loses the last 3 seconds.
4. **Engineer comments and shares (the satisfaction signals [S1][S3]).**
   - Each Short gets one open, personal question on screen and in the pinned comment, e.g. "What's the worst bug you've found in your bed?". Yes/no prompts got skipped (MASTER_ORDERS).
   - Add a "send this to the person who squishes every bug" style share line where it fits.
   - Reply to every real comment within the first hour.
   - Target: from 0.27 to 2+ comments per 1,000 views.
5. **Cadence: 3 a day, well spaced, all on-topic.**
   - Keep Nolan's cap (3 a day, at least 3 hours apart).
   - Don't add slots. Swap any off-topic Short in the queue for a house or spider one.
   - Slots don't lift reach; YouTube says frequency isn't rewarded [S1][S5]. Each weak Short is also a wasted test.
6. **Make the series recognizable** so viewers know what they're getting and there's a reason to subscribe [S4]. Use the same opening card style, series tag and voice, and vary the creature and story. Don't use an identical template every time: mass-produced, repetitive content is a YPP monetization risk under the "inauthentic content" policy [S8].
7. **Related video on every Short (the long-form bridge)** [S6][S7].
   - On-topic Shorts link to that week's long-form. All others link to the show's playlist entry point, per `related-video-rule.md`. (A Short can only link one video, not a playlist [S7].)
   - Close the pinned question with "Full list in the Related video 👆".
   - Mainly a long-form lift. Small Shorts effect, so ranked 7th.
8. **Packaging for the shelf and search (lowest Shorts-feed impact).**
   - Shorts thumbnails are rarely seen in the feed [S5 interview]. Titles still matter for search, which is about 5.5% of Shorts views (team research).
   - Put the creature's name in the title. The best search Shorts name a spider (team research).
   - Apply the existing title fix list. Don't spend time on custom Shorts frames.

---

## (c) Long-form push toward watch hours

**Double down on the one long-form format that works: "Don't squish it / house bug".**
- *3 Bugs in Your House You Should Never Kill (And 4 You Must)*: **5.44% CTR**, 1,856 impressions, 42.7% viewed. That's the only long-form clearing every bar.
- The spider (4.63%) and "3 More Bugs" (4.37%) clear CTR but hold only 22–24%.
- Everything else (quizzes, myths, conspiracy, wolves to dogs, extinct, weird facts) is under 3% CTR, and several hold under 16%.
- Next long-forms should be one-creature or one-room house-bug episodes: centipede v2, Night Shift v2, Christmas-tree bugs and similar. Retire the quiz and conspiracy long-forms (no re-uploads).

**Length:** 8–12 minutes (MASTER_ORDERS), and only when retention holds. At 3 Bugs' 42.7% viewed, a 10-minute cut earns about 4.3 min per view, against 1.95 min at 4:34.

**Retention fixes (from `video-review-1115.md`):**
- Main promise by 0:05.
- No rules or "keep score" intros, and no silent countdowns.
- A shot change every 2–4 seconds, using animation, not slideshow stills.
- Say study names and years plainly ("scientists found…") and keep citations on screen and in the description.
- One comment prompt in the middle of the video.
- Re-hook at each list item ("but #3 is the one in your bed").
- Reward the click from a Short in the first 5–10 seconds [S7].

**End screens and playlists:**
- Every long-form ends on a verbal hand-off ("the bug that's even worse is in this one"), then an end screen with **one best-fit video + subscribe** [S9].
- Build playlists:
  - "Things Living In Your House: full episodes" (long-forms only, 3 Bugs first);
  - "Is This Spider Venomous?";
  - "Would Meatball Survive?".
- Use playlists as end-screen targets so autoplay keeps the session going [S9].

**Shorts as funnels:**
- Each long-form gets 2–3 same-creature 16–18 s trailer Shorts. Each one teases one item from the list without giving away the full ranking, and sets Related video to the long-form [S6][S7].
- Also cut 2–3 Shorts straight from the finished long-form with Studio's "Create Short" tool. That sets the source video as Related video automatically (per creator guide [S7]).

**Compilations (MONETIZATION_PLAN Path B):** stitch 15–25 existing house-bug Shorts, all sourced already, into 10–15 minute "every bug in your house" compilations. These add watch hours at low cost. The risk is the inauthentic-content review [S8], so give each one new narration and ranking context; not a raw stitch.

**72-hour bar (unchanged):** under 3% CTR means a new title and thumbnail the same day. Under 25% viewed means rebuild the first 30 seconds. Use Studio's thumbnail A/B test on every new long-form.

---

## (d) Watch-hours math: ESTIMATE, not Studio's Earn-tab figure

**Where the channel stands:**
- **Long-form hours in the 90-day export:** Meatball long-forms ≈ **24.6 h**, computed as views × duration × avg % viewed. Pre-rebrand long-forms add about 0.1 h.
- Metricool's watch minutes for the same long-forms come to ≈ **11.0 h** through 11/12.
- Nolan's Studio paste on 11/11 showed **10.6 long-form hours in 28 days** (team research).
- **Working estimate: about 10–25 qualified long-form hours** in the last 12 months that are visible to us. Hours earned before Aug 17 aren't in the export. Studio → Earn shows the exact count.
- **Shorts-feed watch time does not count** toward the 4,000 [S10]. The roughly 1,258 h of Shorts watch time in the export (estimate) doesn't help.

**Pace and the deadline:**
- At about 10.6 h per 28 days (≈0.38 h/day), 4,000 h would take decades. A breakout is required.
- **Deadline problem (verified):** from **Feb 1, 2027**, new YPP applicants need **8,000 hours** in 365 days or **20M Shorts views** in 90 days, plus 1,000 subscribers [S11][S12]. Today's bar is 4,000 h or 10M Shorts views plus 1,000 subscribers [S10].
- Reaching 4,000 by **Jan 31, 2027 (77 days)** would need about **52 long-form hours a day**. At the best current rate (3 Bugs, about 1.95 min per view), that's about **1,600 long-form views a day**, roughly 40 times today's pace. It isn't realistic without a viral long-form; say so plainly.
- **How many views 4,000 hours takes:** about 123K long-form views at 1.95 min per view, about 69K at 3.5 min per view (a 10-minute video at 35% viewed), or about 56K at 4.3 min per view (10 minutes at 3 Bugs' 42.7%).
- **Nearer target:** the fan-funding/Shopping tier is unchanged at **500 subscribers + 3,000 hours in 12 months, or 3M Shorts views in 90 days** [S11]. It doesn't include ads. The channel already has the subscribers.
- **Shorts path:** 10M qualified Shorts views in 90 days ≈ 111K a day. Today is about 3,033 total views a day. Since Aug 24, 2026, "views" count from the first frame, and qualified views are the engaged ones [S3]. Team research put engaged views at about 44%, so the real gap is about 80 times.

**Honest framing for Moondog88:** long-form is the right main path because hours compound and the 8,000-hour bar applies from February anyway. The 2-week goal is to prove one format that holds 40%+ at 8–12 minutes, then scale it.

---

## (e) Who does what

| Team member | Owns | First deliverable |
|---|---|---|
| **Scriptwriter** | Hooks and scripts. First-second Shorts openers (creature mid-action + claim), loop endings, 16–18 s cuts, one open question per Short. Long-form cold opens (promise by 0:05), re-hooks per list item, removing countdowns, rules and study-reading. | Hook bank of 20 house and spider openers. Rewritten opens for the next 2 long-forms. |
| **Trends & Analytics** | Topic ranking (house bugs and spiders first; seasonal winter-indoor bugs), TikTok per-video data from Claude (`channels/packaging/tiktok-per-video-90d.csv`), and the daily scoreboard. **Pull the Studio-only metrics we can't see:** stayed-to-watch per Short, subscriber vs non-subscriber views, Shorts-to-long-form traffic, retention curves. | Weekly topic list. Stayed-to-watch table for the last 30 Shorts. |
| **Packaging (me)** | Long-form titles and thumbnails (white background, one huge drawn subject, 2–4 words, one red word), A/B tests, Short titles (creature name, series tag), pinned questions, Related-video map, playlists and end-screen spec, descriptions. Any live Studio change needs Moondog88's okay. | Related-video map for every queued Short. Playlist and end-screen spec. Thumbnails for the next 2 long-forms. |
| **Social Studio + Claude** | Production, editing and cadence. 3 on-topic Shorts a day. 2 house-bug long-forms a week at 8–12 min. Compilation builds. Scheduling. Posting needs Moondog88's okay. | Swap off-topic Shorts in the queue for house/spider ones. Ship the first 8–12 min house-bug long-form. |

---

## (f) 2-week test plan (Mon 11/16 to Sun 11/29)

**Baseline (Meatball era):**
- Shorts: median 1,007 views; 2 of 86 over 2,000; median 67.9% viewed (last week); 0.27 comments per 1,000 views.
- Long-form: 946 views total; about 10.6 h per 28 days; CTR 3.25% across the Meatball era (impression-weighted).

**Week 1 (11/16–11/22): hook + topic + length**
- All 21 Shorts are house-bug or spider topics, 16–18 s, first-frame hook, loop ending, open-question pin, Related video set.
- Split test: about 10 Shorts with the "twist claim" opener (Daddy Longlegs style) and about 11 with the "you, right now" opener (bug in your bed or wall). Same topics on both sides.
- Long-forms: Christmas tree (Wed 11/18 17:00) and centipede v2 (Sat 11/21 08:00) ship with the cold-open rules, an end screen and a playlist.

**Week 2 (11/23–11/29): scale the winner + funnel**
- Every Short uses the winning opener from week 1.
- 2–3 same-creature trailers per long-form, each pointing at it through Related video.
- First 10–15 minute house-bug compilation, with new narration.

**Success metrics, judged at 48 hours for Shorts and 72 hours for long-form:**

| Metric | Baseline | Week-2 target |
|---|---:|---:|
| Median views per Short | 1,007 | **≥ 1,500** |
| Shorts over 2,000 views | 2 of 86 (2%) | **≥ 4 of 21 per week (≥ 20%)** |
| Shorts under 500 views | 30% | **≤ 10%** |
| Median % viewed | 67.9% (wk of 11/9) | **≥ 85%** |
| Stayed to watch (Studio) | about 40–44% engaged (team research) | **+10 points over our own median** (no official benchmark exists [S2][S4]) |
| Comments per 1,000 views | 0.27 | **≥ 2** |
| Long-form views from Shorts / Related video | 0 of 655 | **> 0, and growing week over week** |
| Long-form CTR (72 h) | 3.25% wtd | **≥ 4%** |
| Long-form avg % viewed (72 h) | 3 Bugs 42.7%, others ≤ 24% | **≥ 35%** |
| Long-form watch hours / 28 days | about 10.6 | **≥ 40** |

**Decision rules:**
- If week-1 opener A beats B by 25%+ in median views, adopt A.
- If house-only Shorts don't lift the median above 1,200, the cause is audience mismatch, not the hook. Ask Trends & Analytics for the subscriber vs non-subscriber split. Then put the "survival" and "creature" series on an equal footing, with no pets, news or conspiracy.
- Any long-form under 3% CTR at 72 h gets new packaging the same day.

---

## Data gaps (needed from Studio; not in the export or Metricool)
- **Viewed vs swiped away / Stayed to watch** per Short: Studio → Content → Shorts → "How viewers engaged" [S2]. This is the most important missing number.
- **Shorts-feed impressions** per Short. The export's "thumbnail impressions" and CTR measure browse and search shelves, not the feed.
- **Traffic sources** per video (Shorts feed, related video, search). Metricool's traffic-source call returned nothing; the team's Windsor numbers run to 11/09 only.
- **Subscriber vs non-subscriber and returning-viewer** split. This is needed to confirm the Bartolozzi audience mismatch.
- **Retention curves** (second-by-second) for Shorts and long-forms.
- **Exact 12-month qualified watch hours:** Studio → Earn. The export starts Aug 17.
- **Daily views after 11/12:** Metricool lags about 3 days.
- **Views vs engaged views:** since Aug 24, 2026, "views" count from the first frame [S3], so per-Short view counts aren't the YPP-qualified number.

---

## Sources (platform claims)
- [S1] YouTube Help, Shorts search & discovery tips: ranking signals (chose to view vs swiped, AVD, avg % viewed, likes, surveys), personalization, no minimum cadence, competition. https://support.google.com/youtube/answer/11914225?co=YOUTUBE._YTVideoType%3Dshorts&hl=en
- [S2] YouTube Help, Shorts content-tab analytics ("how many chose to view" = viewed vs swiped away): https://support.google.com/youtube/answer/12942217?hl=en&co=YOUTUBE._YTVideoType%3Dshorts. Also YouTube Help, recommendation signals (appeal, engagement, satisfaction): https://support.google.com/youtube/answer/16559650?hl=en
- [S3] YouTube Blog, "What are 'Engaged' Views": from Aug 24, 2026, views count from the first frame, and engaged views are the old definition used for YPP: https://blog.youtube/inside-youtube/engaged-views-youtube-explained/
- [S4] Creator analyses (not official) of the test-audience plateau and its fixes:
  - vidIQ, "How Does the YouTube Shorts Algorithm Work in 2026" (explore/exploit seed audience; Todd Sherman via Creator Insider): https://vidiq.com/blog/post/youtube-shorts-algorithm/
  - "Shorts stuck at a few hundred views": https://www.autoaishorts.com/blog/shorts-stuck-at-200-views
  - "Why your Shorts get stuck at 1,000 views": https://theartificialwarrior1.substack.com/p/why-your-youtube-shorts-get-stuck
  - "Stayed to watch vs swiped away" (no official threshold; use your own median): https://prepublish.ai/blog/viewed-vs-swiped-away-youtube-shorts
- [S5] Creator Insider, "YouTube Shorts Algorithm — Explained!" (Todd Sherman: viewed vs swiped, length "to tell your story", Shorts thumbnails rarely seen): https://www.youtube.com/watch?v=n3jsYK_-aRU. Also Benzinga, Shorts lead on posting volume not affecting performance: https://www.benzinga.com/news/23/08/34020532/youtube-shorts-chief-debunks-popular-myths-no-posting-10-videos-a-day-doesnt-affect-your-performance
- [S6] YouTube Help, add a related video to your Shorts: https://support.google.com/youtube/answer/14075157?hl=en
- [S7] YouTube Blog, converting Shorts views into long-form growth (Related video, CTA, reward the click in the first 5–10 s): https://blog.youtube/creator-and-artist-stories/youtube-related-videos-traffic-guide/. Also Clyper's guide (one video per Short, no playlists; Studio "Create Short" auto-links the source): https://www.clyper.io/guides/how-to-link-a-youtube-short-to-a-video
- [S8] YouTube channel monetization policies ("inauthentic content", renamed July 15, 2025): https://support.google.com/youtube/answer/1311392. Also The Verge: https://www.theverge.com/news/703772/youtube-monetization-policy-update-ai-spam
- [S9] YouTube Help, video reach and content performance (end screens, playlists, retention): https://support.google.com/youtube/answer/9314355 and https://support.google.com/youtube/answer/12220281
- [S10] YouTube Help, YPP overview & eligibility (1,000 subs + 4,000 qualified public long-form hours in 12 months, or 10M qualified Shorts views in 90 days; Shorts-feed watch hours don't count; private, unlisted and deleted videos don't count): https://support.google.com/youtube/answer/72851?hl=en
- [S11] YouTube Help, changes to YPP (from Feb 1, 2027: 8,000 h or 20M Shorts views for new applicants; 500-sub tier unchanged at 3,000 h or 3M): https://support.google.com/youtube/answer/12843009
- [S12] YouTube Blog, YPP 2027 updates: https://blog.youtube/news-and-events/youtube-partner-program-updates-2027-new-opportunities-earn/. Also The Verge: https://www.theverge.com/streaming/977474/youtube-partner-program-new-requirements
- Shorts length up to 3 minutes since Oct 15, 2024 (context only; our data favors 16–18 s): https://support.google.com/youtube/answer/15424877?hl=en
