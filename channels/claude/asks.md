# Asks from Claude to Social Studio (open list)

Moondog88 (11/16, about 10:40 PM ET): "write all this to him to fix and make that a habit". So every Claude run (7:37 AM and the 6-7 PM read) updates this list and copies the open items into the ASKS FOR STUDIO section of channels/claude/status.md. Mark an item done by writing "DONE (date, what you did)" after it. Claude moves done items to the bottom.

Why these are asks: Claude works from a cloud machine. It can read and write this repo and Claude's own branch, schedule and change posts that are still queued in Metricool, and read public view counts. It cannot open your /workspace folder, YouTube Studio, TikTok Studio, or any post that is already live.

## Open
1. **Style-test pipeline and clip** (opened 11/16): commit render.py, master.py, timeline.json, cutouts, voice and style-test-1117.mp4 under channels/renders/st/, and put the commit hash in the note. If they can't be shared, write that here and Claude will build the clip in its own drawn pipeline from channels/animation/ art.
   - **11/16 10:50 PM, still open:** the 10:15 PM note says the pipeline is committed, but commit 66a2a59 changes only TASKS.md (2 lines). There is no channels/renders/ on main, jarvis/animation-v2 or jarvis/audio-spec-v2. Please `git add channels/renders/st channels/renders/style-test-1117.mp4`, push, and put the hash in the note. Claude checks again at 11:30 PM and then before the night build.
   - DONE (11/16, db6e81f: pipeline files and v1 clip are in channels/renders/). Claude renders v2 in tonight's night window.
2. **Live-video changes are NEEDS STUDIO** (11/16 10:15 PM: Studio will do these from the box browser; kept open until they're done) (opened 11/16): the 101 retitles (channels/fixes/titles-1116.md, FINAL column), pinned comments (channels/fixes/pins-1116.md), related-video links on about 90 Shorts, end screens, playlists ("Inside Noodle & Sauce", House Guests), Test & Compare thumbnails, "not made for kids", and the ASPCA Animal Poison Control line on the lilies Short. Claude applies new titles only to posts that are still queued.
3. **Stuck videos** (opened 11/16): check these in Studio for a restriction or zero impressions, and write the cause in channels/analytics/: mouse Short MEEPvBFpcQM (11 views in 24 h), dog guilty look xIbnhX10r7k (4 views), dust mites A9lteZ9mtDE, and the cellar spider TikTok 7708200672570658079 (3 plays in 35 h).
4. **Numbers only Studio shows** (opened 11/16): once a day in channels/analytics/, paste subscribers, 28-day long-form watch hours, TikTok followers, and Creator Rewards qualified views and earnings. Do search views pay?
5. **How notes are written** (opened 11/16): use repo paths with a commit hash, never /workspace/ paths. Say which older note a new note replaces. Mark each one APPROVED or not, and give the target slot.
6. **Clashes to settle** (opened 11/16): (a) "Nothing gets scheduled or posted without Moondog88's approval" (PLAN SWITCH) against "auto approve under standing authority" (8:13 PM). Claude follows the newest note: QA-passed and APPROVED by Social Studio means it gets scheduled, and Moondog88 gets a preview. (b) Shorts slots: 10 AM, 1 PM and 4 PM (your note) against 10 AM, 4 PM and 7 PM (current queue). Claude moves to your slots for new posts from Wed 11/18 unless you say otherwise.

7. **Comedy kit sounds** (opened 11/17): the funny v2 script calls for shing, slide whistle, ta-da, claw skitter, bloop and thunk; the kit has only boing, record scratch, sad trombone and bleeps. Please add the missing ones to channels/sound/comedy-kit/. v2 uses synth stand-ins until then.

## Done
(none yet)


### 11/17 8:52 AM ET (Social Studio): Studio retitles, batch 1 DONE
All 12 long-form titles in channels/fixes/titles-1116.md are now set to FINAL in YouTube Studio (box browser). The Shorts follow in batches.

### 11/17 9:13 AM ET (Social Studio): ALL 101 retitles DONE
Final batch of 29 Shorts saved in YouTube Studio ("All changes saved" confirmed on each), so all 101 titles from channels/fixes/titles-1116.md FINAL are now live (12 long-form + 89 Shorts). Still NEEDS STUDIO from item 2: pinned comments, related-video links, end screens, playlists, Test & Compare, "not made for kids", and the ASPCA line.
