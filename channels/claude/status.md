# Claude status (Claude overwrites this each run; see channels/team/claude-sync-schedule.md)
Start here: channels/claude/handbook.md (everything I know: tools, numbers, rules, files, schedule, and my questions for you).
Sections every run: RENDERED, POSTED/SCHEDULED, BLOCKED, ETA, NUMBERS, and ASKS FOR STUDIO (what you need to fix so I can keep going; the open list lives in channels/claude/asks.md).
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
