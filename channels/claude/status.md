# Claude status (Claude overwrites this each run; see channels/team/claude-sync-schedule.md)
Start here: channels/claude/handbook.md (everything I know: tools, numbers, rules, files, schedule, and my questions for you).
Sections every run: RENDERED, POSTED/SCHEDULED, BLOCKED, ETA, NUMBERS, and ASKS FOR STUDIO (what you need to fix so I can keep going; the open list lives in channels/claude/asks.md).
Updated Tue 11/17 3:25 PM ET by Claude (2-hour check).

HOW TO REACH CLAUDE FAST (from 11/17, Moondog88: "make sure you guys have full communication"):
- I now check this repo every 2 hours (9:23 AM, 11:23, 1:23 PM, 3:23, 5:23, 9:23 PM ET), plus the 7:37 AM morning run and the 6:41 PM evening read. A new note gets an answer in status.md within about 2 hours.
- Put URGENT in a note's heading if it can't wait for the next check. Put QUESTION FOR CLAUDE if you need an answer, and I'll reply under it in this file.
- My questions to you go in channels/claude/asks.md. Answer under each one, or write DONE.

RENDERED:
- **[MEATBALL] Read 3:15 PM "PART 4 V3 FRAMES: PASS" (11/17 3:25 PM).** Part 4 v3 stays at 7 PM. Your note (the bug sits small mid-video; give it a punch-in or a BUG CAM about every 10 s) goes in tonight, 11:05 PM: a renderer rule so no 10 s stretch goes without a bug close-up. It's used on Part 5 and every video after.
- **[MEATBALL] SHIP V3 TODAY: DONE (11/17 3:00 PM ET). Tonight's 7 PM TikTok is now Centipede Part 4 v3: channels/renders/centipede-p4-v3-1117.mp4** (62.1 s; frames: channels/renders/centipede-p4-v3-1117-sheet.jpg). It is swapped into the same Metricool post (uuid 7918539842414070977, new id 431955478). The rehosted file was checked byte for byte (24,300,310 bytes). The caption and title are unchanged.
  - Same script and QA wording, word for word, as v2. "Will it bite you?" is now its own short beat (+34%, +12 Hz), with a 0.35 s pause before your bite line.
  - Voice C: Guy at +32%, fact lines at +20%.
  - Fix 1: the BUG ID card is now 1,020 px wide (about 2x the area), centered, on screen 2.6 s, with a pop sound and the picture dimmed behind it. It sits on its own beat (the speed line, at about 0:07-0:10), and that beat's old text card was removed. Rows: AMONG THE FASTEST ARTHROPODS / ABOUT 16 INCHES A SECOND / BITE: UNCOMMON (ONLY IF HANDLED).
  - Fix 2: the camera now keeps Meatball's whole body and head in frame on every push-in and punch (renderer rule, every video).
  - Fix 3: no SIZE CHECK coin. It is out of the auto shot rotation for every video.
  - Checks: voice check pass (every line heard to its end; the speech model wrote "Part 5" as "five"). Lint pass (62.07 s, 61 s floor).
  - **Studio, please check the frames before 7 PM.** If anything is wrong, write URGENT and I can swap back to v2 (the v2 file is still on Metricool).
  - Part 5 and the 15-18 s Shorts cut of Part 4 get the v3 look and voice C from the start (tonight's night build).
- **[MEATBALL] Animation upgrade v3 READY (11/17 about 2:30 PM, Moondog88 asked for it now): channels/renders/retention-test-v3-1117.mp4** (22.3 s, voice C, voice check pass). It's built into the renderer, on by default for every new video. What's in:
  - The camera moves on every line: push-in, punch on key words, a shake on the scare, whip-pans and smash cuts.
  - The legs ripple in every frame, the bug has a shadow and smears, and it bursts out of the drain on the scare.
  - A flashlight-reveal hook and dimmed night scenes with light pools.
  - Shot library: BUG CAM magnifier, night-vision SECURITY CAM with timestamp, SIZE CHECK next to a coin.
  - Meatball breathes, anticipates, gets a sweat drop, and never repeats a pose.
  - A BUG ID card in one fixed design (only checked words, no invented meters).
  - Whoosh, hit, thud and skitter on cuts, and the music drops before the scare.
  - Not done yet: the wall cutaway and under-bed POV, broom and jar props, real eye-pops.
  - Flag: the SIZE CHECK coin proportion isn't sourced yet. QA, please give a body length or say drop it.
- **[MEATBALL] 2 PM notes read (11/17 about 2:05 PM).** VOICE PICK C is now the default from tonight's Part 5 on: Guy at +32%, with the scare-line lift and the pause before the bite answer. ANIMATION UPGRADE v3 ("not AI slop") is renderer work: shot library, flashlight hook, legs moving every frame, BUG ID CARD, darker night lighting. **ETA: Wed and Thu night windows**, then retention-test-v3-1117.mp4 with voice C for your review. Part 5 and tonight's 7 PM post come first. One ask for the BUG ID CARD: please give the Bite risk, Speed and Gross factor values per bug (0-5) from QA's facts. Otherwise I'll leave those meters off rather than make up numbers.
- **[MEATBALL] Voice test READY (11/17 about 1:10 PM):** the same 22 s retention-test-v2 script in three voices, all free.
  - **A: channels/renders/voice-test-A-1117.mp4** (20.3 s). edge-tts Andrew, tuned per line: base +27%; scare lines "Will it bite you?" and "Nope. Not touching it." at +34% and +12 Hz; a 0.35 s pause before the bite answer; fact lines slower at +20%.
  - **B: channels/renders/voice-test-B-1117.mp4** (20.9 s). Kokoro-82M am_adam, local, Apache 2.0, at speed 1.18. Kokoro has no per-line pitch.
  - **C: channels/renders/voice-test-C-1117.mp4** (23.1 s). edge-tts Guy, with the same tuning as A.
  - Specs are in channels/renders/st2/. The renderer now takes rate, pitch and voice per line, so whichever voice Moondog88 picks can be used on every video.
- **[MEATBALL] Read 11/17 12:00 PM "5 fixes": adopted.** Long-form fixed days: **Mon 5 PM, Wed 5 PM and Sat 8 AM ET** (Wed and Sat already run; Mon starts once there are 3 long-forms a week). Fix 4 ("Full episode on YouTube, Meatball Myths" at the end of every bug-series TikTok) starts with Part 5 tonight. The @meatballmyths bio link is NEEDS STUDIO. Pinned comments are NEEDS STUDIO. Thumbnail spec noted for the next long-form.
- **NUMBERS 12 PM:** centipede Part 2 is now **253,000 plays**, 9,418 likes, 291 comments, 675 shares, 1,142 saves (public page, ttpage).
- **[MEATBALL] Centipede Part 4 v2 (11/17 about 12:20 PM): your QA addendum fixes are in.** "Don't squish it!" is the first line at 0:00; the vote "Squish it, or let it live?" is at about 0:04; your bite line, word for word, ends before 18 s; and the caption names the sources. Two Meatball jokes were cut to fit, so it runs 64.0 s. It replaces the 7 PM TikTok post (same uuid 7918539842414070977). Still owed: the 15-18 s YouTube Shorts cut. It goes in the night queue and through your QA.
- **[MEATBALL] Retention test v2 READY (11/17 about 11:45 AM): channels/renders/retention-test-v2-1117.mp4** (22 s). Changes from v1:
  - The bite line is your QA wording, word for word.
  - Frame 1 is a big close-up of the bug for about 1.3 s before the wide shot.
  - Captions no longer end on "and", "the", "baby" and the like (a change to the renderer, so it applies to every video).
  - Two chase/scuttle shots, one shake-and-punch reveal on the bite question, a "Nope. Not touching it." reaction beat, a pop card for "15 pairs of legs", the three prey popping in one at a time, and the danger meter on "fastest".
  - The music bed is the same.
  - Voice: edge-tts Andrew has no emotion styles. The delivery is lifted with punctuation and the reaction beat only.
  - Not done yet: hiding behind the door, and the ripple of the legs on every frame (the rig only moves the legs while it walks). Spec: channels/renders/st2/retention-test-v2-1117.json.
- **[MEATBALL] Retention test READY (11/17 about 11:05 AM): channels/renders/retention-test-1117.mp4** (20.8 s). It's the opening of centipede Part 2 with your upgrade: +18% voice; the bite answer moved up to about 0:04 ("Will it sting you? Almost never. Only if you grab it hard."); a tense "eerie" bed at -17; a whoosh on every cut; a skitter scratch on every image; bigger captions. Same checked words as Part 2, no new claims, all sounds from our own kit. Not posted. One gap: our captions show 1-3 words at a time, not strictly one, because the renderer groups them. Say if one-word is a must and I'll change the caption code. Spec: channels/renders/st2/retention-test-1117.spec.json.
- **House centipede Part 4:** 65.6 s, Part 2's look, 8 new sourced facts, second-model checked (8 wording fixes), voice and lint pass. Skills repo: skills/oh-meatball/episodes/drawn-house/tt-house-centipede-p4.mp4, check in research/facts/house-centipede-p4-check.md.
- Style test v2: channels/renders/style-test-v2-1117.mp4 (19.6 s), with a render note in channels/renders/st2/RENDER-NOTE.md. Moondog88 has it as a preview.

POSTED/SCHEDULED (Metricool):
- **Centipede Part 4: TikTok Tue 11/17 7 PM** (uuid 7918539842414070977). The shark minute cut moves to Thu 11/19 7 PM. The 19.9 s bed bug TikTok (Wed) and the 25 s grizzly TikTok (Thu) are now drafts because they're under a minute.
- YouTube Shorts as queued (skills repo posted.csv). Nothing was pulled.

BLOCKED:
- Nothing for Part 4.

ETA:
- **House centipede Part 4 (your 7:00 AM note):** facts, script and the second-model check this morning; render early afternoon; preview to Moondog88 about 3 PM; scheduled for TikTok 7 PM ET today. Style is the one that won Part 2 (stick-figure Meatball, tiled bathroom), 61-65 s, voice +15%, clean first 7 s, and the end line "Part 5 drops tomorrow, follow so you don't miss it". DONE and scheduled. **Part 5:** built in tonight's night window for Wed 11/18 7 PM, ending with "Part 6 drops tomorrow" only if you want the series to keep going. Please say yes or no here by 10 PM, or I'll end Part 5 on a question instead. The pinned comments linking Part 2 and Part 4, and the playlist, are NEEDS STUDIO.
- EP5 long-form and S1-S3/T1-T3: after Moondog88 okays the style test v2.

NUMBERS (TikTok public pages via postkit ttpage, 12:40 UTC 11/17):
- **House centipede Part 2 (7703357929851800862): 93,900 plays**, 3,059 likes (3.3%), 112 comments, 271 shares, 420 saves, 63 s, posted 11/1. This is the 1-min+ video Moondog88 saw pass 11K; it's ours.
- Part 3 (7703729172081806622): 227 plays. House centipede minute cut (7708571792947858718): 396. Cat name minute cut: 932 (7.5% likes). FAA "why it happened": 17,600.
- Subscribers and watch hours need Studio (asks #4).

ASKS FOR STUDIO (what you need to fix so I can keep going; the open list lives in channels/claude/asks.md).
Updated Tue 11/17 about 12:15 AM ET (first written Mon 11/16 10:30 PM) by Claude (Meatball Myths session, branch claude/youtube-monetization-strategy-m9vz6i of mooneyn60-art/skills). Moondog88 told me tonight to follow Notes for Claude as orders. I have read them, and I've adopted the sync schedule from tonight: night builds by 6:30 AM, this file by 7:45 AM, Notes read 6-7 PM.

RENDERED:
- **Style test v2 (11/17 about 12:10 AM):** channels/renders/style-test-v2-1117.mp4, 19.6 s, built from ep5-s1-funny-v2.md with your pipeline. Voice is +15% (fact payoff at 2.63 s), captions sit above the bodies, and the spider scuttles. Render note: channels/renders/st2/RENDER-NOTE.md. Sent to Moondog88 as a preview; not posted.
- Bison minute TikTok, 88.8 s, and shark minute TikTok, 86.9 s (second-model checked, voice and lint pass): skills repo, skills/oh-meatball/episodes/drawn-house/tt-bison-wms.mp4 and tt-shark-wms.mp4.
- Cat lilies YouTube Short, 19.0 s (FDA and ASPCA facts, second-model checked): yt-cat-lilies-v6.mp4.
- Dog chocolate YouTube Short, 21.4 s: over our 20 s limit, so it needs a trim and a re-check before it can post.

POSTED/SCHEDULED:
- Cat lilies YouTube Short: Mon 11/16 7 PM (Metricool uuid 4718692198843895770). It replaced the old stink bug Short, which is now a draft.
- Bison minute TikTok: Mon 11/16 7 PM (uuid -9053344906847369449).
- Shark minute TikTok: Tue 11/17 7 PM (uuid 3481255443704858529). The 23 s dog tail wag TikTok was moved to draft.
- Full list of what's scheduled: skills/oh-meatball/data/posted.csv on the branch above.

BLOCKED:
- Style test and EP5 render: the script is here (channels/scripts/ep5-s1-funny-v2.md), but the pipeline you used (/workspace/renders/st/: render.py, master.py, timeline.json, cutouts, voice) and style-test-1117.mp4 are in your workspace, not in this repo. Please commit them under channels/renders/st/ and I'll re-render from the funny v2 script in the next night window. If they can't be shared, say so here and I'll build the clip in our own drawn pipeline from your cartoon kit art instead.
- Changes to videos that are already live (the 101 retitles, pinned comments, related-video links, end screens, playlists, Test & Compare, "not made for kids"): I can only reach posts that are still scheduled in Metricool. YouTube's own API isn't connected here, so all of these are NEEDS STUDIO. That includes the ASPCA line on the lilies Short.
- Live TikTok captions: NEEDS STUDIO for the same reason.

ETA:
- Style test (15-20 s): the first night window after the files are committed (or after your answer above). Done by 6:30 AM and posted here.
- EP5 long-form, S1-S3 and T1-T3: two nights after the style test is approved.
- Dog chocolate Short: trim and re-check, then it can take a slot from Tue.
- New titles on posts that are still scheduled: I'll apply the FINAL column of channels/fixes/titles-1116.md to every Meatball post still queued in Metricool by the Tue 7:37 AM run.

NUMBERS (public counts, Mon 11/16 7:45 AM ET; subscribers and watch hours need Studio):
- TikTok: FAA "why it happened" 17,600 plays; FAA first video 9,352; cat-name minute cut 807 at 13 h (8.2% likes); house centipede minute cut 294 at 11 h; cellar spider minute cut 3 at 35 h (looks stuck).
- YouTube: shark Short 907 at 18 h; cat name 956; mouse Short 11 at 24 h; dog guilty look 4 (both look stuck: please check them in Studio); house cat long-form 45 at 63 h.
- Long-form watch hours: 10.4 h in 28 days on 11/14 (Windsor); about 4,000 still needed.

ASKS FOR STUDIO (Moondog88 11/16: "write all this to him to fix and make that a habit"; full list with status in channels/claude/asks.md):
1. Sound effects: the comedy kit has no shing, slide whistle, ta-da, claw or bloop, so v2 uses synth stand-ins. If Voice & Sound adds real ones to channels/sound/comedy-kit/, I'll swap them in.
2. Do the live-video changes in YouTube Studio (NEEDS STUDIO): the 101 retitles, pins-1116.md, related-video links, end screens, playlists, Test & Compare, "not made for kids", and the ASPCA line on the lilies Short.
3. Check four stuck videos in Studio and write the cause in channels/analytics/: mouse Short MEEPvBFpcQM (11 views in 24 h), dog guilty look xIbnhX10r7k (4), dust mites A9lteZ9mtDE, and the cellar spider TikTok 7708200672570658079 (3 plays in 35 h).
4. Paste the Studio numbers I can't read (subscribers, 28-day long-form watch hours, TikTok followers and Creator Rewards qualified views) into channels/analytics/ once a day.
5. In every note, use repo paths with a commit hash, not /workspace/ paths, and say which older note it replaces. Where two notes disagree (for example "nothing scheduled without Moondog88's approval" and "auto approve"), I follow the newest one and record the clash here.
