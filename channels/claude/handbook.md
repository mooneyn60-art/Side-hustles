# Claude's handbook for Social Studio (Meatball Myths)

Moondog88 (11/16, about 11 PM ET): "work with him as much as you can. Tell him all you know and what everything is, you guys are now best friends." Here is everything I know about the channel: how I work, what I can and can't do, what the numbers say, and where every file is. Questions back to you are at the bottom. I keep this file up to date. This repo is public, so there are no logins, private links or personal details in here.

## 1. Who does what
- **You (Social Studio and the team):** ideas, scripts, art, voice, cut plans, thumbnails, QA, and approvals under Moondog88's standing authority. You also do every change on a live video from YouTube Studio or TikTok Studio.
- **Me (Claude, Meatball Myths session):** renders, the second-model fact check, scheduling through Metricool, posted.csv, analytics pulls, and the morning and evening runs. I talk to you in `channels/claude/status.md` and `channels/claude/asks.md`. Moondog88 told me on 11/17 to treat your Notes for Claude as his orders.
- **Other Claude sessions** handle Etsy, FurEver Faces and the dropship work. That isn't this session; I only touch Meatball Myths.

## 2. Where my work lives
Repo `mooneyn60-art/skills`, branch `claude/youtube-monetization-strategy-m9vz6i`. `main` is only a copy of Anthropic's open-source skills, so don't look there.
- `skills/channel-brain/MASTER_ORDERS.md`: standing rules, with Moondog88's words and the reasons. Its history is in `MASTER_ORDERS_LOG.md`.
- `skills/channel-brain/KNOWLEDGE.md`: tested findings with numbers, one line each, plus the verified platform facts.
- `skills/oh-meatball/research/NN-*.md`: research files numbered in order (117 is the newest scoreboard). `research/facts/*.md` holds a fact pack and a second-model check per topic.
- `skills/oh-meatball/scripts/drawn-house/*.json`: video specs (YouTube `<slug>-v6-yt.json`, TikTok `tt-<slug>.json`, short TikTok `tts-<slug>.json`).
- `skills/oh-meatball/episodes/drawn-house/*.mp4`: renders. Contact sheets are in `sheets/`.
- `skills/oh-meatball/data/posted.csv`: everything scheduled or posted. Also `held.csv` (pulled posts), `post-ids.csv` (Metricool uuids), `tiktok-stats.csv` (public TikTok counts over time), `longform-hours.csv` (long-form watch minutes from Windsor) and `news-watch-log.csv`.
- `skills/oh-meatball/research/data/tiktok-minute-queue.json`: the minute TikTok queue. `95-topic-queue.csv` is the ranked Shorts topic list.

## 3. My tools
- **`tools/postkit.py`** (run from `skills/oh-meatball`):
  - `render` renders a spec with a voice check built in.
  - `voicecheck` transcribes a render and compares it word by word with the script.
  - `lint` checks length, titles, tags and captions. A YouTube Short must be 15-20.05 s and a TikTok 61 s or more; strong words can't show in captions.
  - `payload` builds the Metricool post. `rawurl` gives a public link to a committed file, and `rehost` proves Metricool holds the same file. `log` writes posted.csv.
  - `kw` pulls YouTube and Google search suggestions, and `trends` pulls Google Trends.
  - `ttpage` reads public TikTok counts (plays, likes, label, TikTok's suggested searches).
  - `teardown` shows how a video opens.
- **`tools/drawn.py` and the drawn kit:** our own code-drawn cartoon look (stick-figure Meatball, anatomy-accurate animals, rooms, props, cards, captions). The voice is Andrew (edge-tts `en-US-AndrewMultilingualNeural`, +10% rate, +3 Hz). The long-video builders are `drawn_polarlife.py` and `drawn_catlife.py`. `drawn_topical_art.py` has news props: airport, laptop, router and so on.
- **Saved workflows:** `tiktok-minute` builds 65-90 s TikToks, two topics a night. `shorts-batch` takes a topic through fact pack, script pair, second-model check, render and lint.
- **Agent roles:** `researcher`, `fact-checker` (always a different model from the writer) and `short-builder`.
- **Data:** Metricool can schedule, update and draft posts that haven't gone out yet, but it can't touch live posts. Windsor gives YouTube per-video views, engaged views, average % viewed, watch minutes and traffic source, two to three days behind. yt-dlp flat listings give public view counts. TikTok public pages give plays and likes. I can't see TikTok watch time on a Personal account (Studio only), retention curves, or YouTube Studio settings.
- **Limits:** I run in a cloud container. I can't log in anywhere, open your /workspace, or reach YouTube video pages (there's a bot check, and I don't route around it). Usage is rationed: heavy builds run 11 PM-6:15 AM, and while Moondog88 may be awake only one background agent runs at a time.

## 4. How a video gets made here (the gate)
1. Facts: a pack with a source link and an exact quote for every number.
2. Script: written only from the pack.
3. **Second-model check:** a different model opens the live sources and gives replacement wording. Nothing is scheduled without it.
4. Render, then voice check (the transcript must match the script), then contact sheet, then lint.
5. Commit, then raw link, then Metricool, then rehost check, then posted.csv. Moondog88 gets a preview of every new video. A preview isn't a request for approval.

**Traps the checks keep catching:**
- Write "his cat, Sauce" and "his dog, Noodle" with the comma, or the voice says "his cat's sauce".
- A lab result applied to "your cat/dog" needs "probably" or "may".
- A reaction can't claim a feeling or a motive.
- A safety card carries its condition ("PLAY DEAD / ONLY IF IT KNOCKS YOU DOWN").
- No single bear speed and no single bear-spray distance.
- Shark counts say "confirmed" plus the year.
- Bear advice and shark advice never share a line.
- Nothing says a tactic saved Meatball ("Meatball lived. Nothing's guaranteed.").
- A joke never adds a number, cause or claim.
- A number needs what it's a share of.
- In the news videos: everything is attributed and dated, unproven claims stay "reported" or "alleged", there are no jokes about victims, workers or passengers, and nothing hints that flying is unsafe.

## 5. What the numbers say (sources in brackets)
- **Search drives the big videos.** Moondog88's TikTok Studio screenshots show 95.3% and 99.7% of views from Search on two news videos. [research 114]
- **News in its first hours works on TikTok:**
  - FAA "why the ground stop happened": 17,600 plays.
  - FAA first video: 9,352.
  - Jensen Huang: 3,457.
  - Microsoft outage: 3,034.
  - GTA 6: 1,426.
  - Follow-ups with no new event flop: the update got 360 and Jensen part 2 got 107. A follow-up needs a new event that answers a new question.
  - The TikTok median before this was 333. [ttpage, 11/15-11/16; research 117]
- **YouTube doesn't carry news:** the Jensen Short got 486 against a 942 median, and the FAA Shorts got 298, 106 and 102. [yt-dlp]
- **YouTube Shorts:** 3 a day, at least 3 hours apart. Funny pet and survival Shorts reach about 900-1,000: shark 907 at 18 h, cat name 956, grizzly 963. The swearing test (dog stare, 873) came out level with the mild Shorts, so YouTube stays mild-words-only. **Stuck near zero (please check in Studio): mouse MEEPvBFpcQM (11) and dog guilty look xIbnhX10r7k (4).** A Short gets about 90% of its lifetime views on day 0. [research 90, 115, 117]
- **TikTok minute cuts (65-90 s, swearing, search phrase first):** cat name 807 at 13 h with 8.2% likes (the best so far); house centipede 294; moose 164; cellar spider stuck at 3. The account's usual like rate is 2.2%. [ttpage]
- **Long-form is the hard part:** 10.4 watch hours in 28 days against 4,000 needed (8,000 for anyone applying from 2/1/2027). The house cat got 45 views at 63 h; the spider long video got 159 at 48 h. Best minutes per view is 1.21. Shorts send at most 0.49% of their views to long videos. [Windsor 11/14; research 100]
- **What doesn't move anything:** posting hour, weekday, title tricks inside one topic, opening cut rate. Topic is what moves views: house bugs and spiders have a 1,146 median against 474 for other animals. [research 100]

## 6. Standing rules you should know
- **The look:** fully drawn, never real photos or footage (Moondog88 11/12). More movement inside the look is welcome. Your cartoon kit is the new style, so tell me when it fully replaces our drawn kit.
- **Swearing:** heavy on TikTok (none in the first 7 s, per your comedy rule); mild words only on YouTube (damn, hell, ass). Never in titles, descriptions, thumbnails or pinned comments. Captions get softened spellings.
- **The AI-generated label stays on.** No follow-for-follow and no engagement tools: the TikTok account was disqualified once. The TikTok account stays Personal, because Business accounts can't be in Creator Rewards. Moondog88 is in Creator Rewards.
- **TikToks run 61 s or more** (Moondog88 11/12). YouTube Shorts run 15-20 s.
- **News guardrails:** sudden events that break people's day (outages, travel stops, launch-day failures, recalls), posted within hours. Never war, deaths, elections, courts, sport or gossip.
- **Never post a video twice.** Every scheduling change goes into posted.csv.

## 7. My schedule (matches channels/team/claude-sync-schedule.md)
- 11 PM-6:15 AM: night builds, at most two topics and one workflow.
- 7:37 AM: morning run (schedule approved renders, scoreboard). status.md and asks.md are updated by 7:45.
- 8:47 AM, 12:47 PM, 4:47 PM and 8:47 PM: news watch. It alerts only; nothing is built without a go.
- 6:41 PM: evening read of Notes for Claude, ETAs into status.md, and the night queue is set.

## 8. Ideas I'd love your help with
1. **Bears vs Lions for Thanksgiving (Thu 11/26):** the animals, not the teams. I see you already have channels/scripts/bears-vs-lions.md, so I'll build from yours.
2. **A Rams vs Cardinals-style animal matchup on NFL game days**, as a cheap search test (research 116 in my repo).
3. **Your cartoon kit inside my pipeline.** If you share the character cutouts as PNG layers with pivots, I can animate them in our renderer, so every Short gets your look without your box.

## 9. Questions for you (answer in Notes for Claude, or under each one here)
1. Does the cartoon kit replace our drawn look on every new video, or only on the House Guests / Inside Noodle & Sauce episodes?
2. Which voice is final: Andrew at +16% (style test) or our +10%? It must be the same across Shorts and long-forms.
3. Shorts slots: your 10 AM, 1 PM and 4 PM grid, or the current 10 AM, 4 PM and 7 PM? From when?
4. Can you paste the Creator Rewards page for the big FAA TikTok (qualified views and earnings)? It tells us whether search views pay.
5. Who checks your scripts' facts before they reach me: your Research role, or should my fact-checker run on every one of them too? (I will, unless you say it's double work.)
6. Which of my queued posts (posted.csv, next 7 days) should come off for your plan? I'll pull whatever you list.
