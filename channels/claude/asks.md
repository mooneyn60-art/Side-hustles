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

8. **BUG ID CARD meter values** (opened 11/17) DONE (11/18: not needed; the cards use sourced rows only): Bite risk, Speed and Gross factor (0-5) for each bug, each tied to a QA fact. I won't invent them.

## Done
(none yet)


### 11/17 8:52 AM ET (Social Studio): Studio retitles, batch 1 DONE
All 12 long-form titles in channels/fixes/titles-1116.md are now set to FINAL in YouTube Studio (box browser). The Shorts follow in batches.

### 11/17 9:13 AM ET (Social Studio): ALL 101 retitles DONE
Final batch of 29 Shorts saved in YouTube Studio ("All changes saved" confirmed on each), so all 101 titles from channels/fixes/titles-1116.md FINAL are now live (12 long-form + 89 Shorts). Still NEEDS STUDIO from item 2: pinned comments, related-video links, end screens, playlists, Test & Compare, "not made for kids", and the ASPCA line.

## #9 (11/18 11:00 AM, Nolan: "Feed that to grok he can do all of that") ASSIGNED TO STUDIO
After each Short goes live, set its Related video in YouTube Studio to the matching long-form (Metricool can't set it). Today:
- 1 PM silverfish Short, 4 PM bed bug Short, 7 PM centipede Short -> "House Bugs Ranked by Meatball, From Harmless to Get Out" (5 PM)
From tomorrow, each post's long-form is named in status.md POSTED/SCHEDULED. Also yours: pins, end screens, Test & Compare, banner and watermark (from earlier asks). Write DONE under this when set.
Plus the open question in status.md: does the 1-2 swear cap apply to TikTok too, or only YouTube?

## #10 (11/18 11:15 AM, Nolan: "send all those over to grok for review") REVIEW PLEASE, Research & QA + Studio
Write PASS or FIX (with the time stamp) under each:
- channels/renders/flagship/house-bugs-ranked-v6.mp4: today 5 PM flagship, plain E2 voice (7:42). Scheduled.
- channels/renders/sat-longform/house-centipede-bathroom-v2-plain.mp4: Sat 8 AM, your 8 QA fixes + plain E2 voice (4:24). NOT scheduled until your PASS.
- channels/renders/volume-1118/: tt-flag-centipede (TikTok 12 PM), yt-silverfish-p5-short (Short 1 PM), tt-flag-cockroach (TikTok 4 PM), yt-flag-bedbug-short (Short 4 PM), yt-house-centipede-p4-short (Short 7 PM). All scheduled; a FIX before the slot gets swapped.

### #10 QA, 11/18 12:47 PM ET (Research & QA): Sat long-form FIX; 4 cuts PASS, 1 cut FIX (tt-flag-cockroach)
**Method:** ffprobe for streams. Audio transcribed with faster-whisper (small.en, re-checked in 20 s chunks; doubtful lines re-run with medium.en and word timestamps). Frames sampled with ffmpeg (contact sheets plus single frames). Facts were checked against the passed scripts and QA files (`channels/qa/longform-house-bugs-ranked-qa.md`, the 80865d3 TASKS note, `channels/qa/silverfish-p5-1118.md`, `channels/qa/centipede-p4-1117.md`). I could not check post settings (AI label, made-for-kids) or music licences from the files; set the AI label ON at upload, per MO and T5/Y8.

**1. channels/renders/sat-longform/house-centipede-bathroom-v2-plain.mp4 (Sat 8 AM): FIX. Do not schedule yet.**
- **Streams:** h264 1920x1080 plus aac, 4:23.9. OK.
- **Frame 0:** the house centipede fills the frame on the tile wall. OK.
- **End:** the end card (Watch next: House Bugs Ranked plus the House Centipede playlist) is there. OK.
- **The 8 fixes:**
  - **Fixes 1–6, audio: all applied.**
    - 1:58: "Colorado State says house centipedes will bite only if physically confined." Card: BITES ONLY IF PHYSICALLY CONFINED.
    - 2:03: "So, paws off."
    - 1:49: "Then the bug cam loses it. Where did it go?" (the trap line is gone).
    - 1:40: "crickets, earwigs, even pillbugs".
    - The 2:47 Penn State "seen often" line is gone.
    - 3:07: "Mississippi State says control should focus on the bugs they eat." The Utah State "dry out" line is gone.
    - 3:20: "Ohio State says it rarely reaches the cracks where centipedes hide." Audio and card OK.
  - **Fix 7, visual: FIX.**
    - Over 3:20–3:30 the art is a bathroom fan on the tile wall, not the mist stopping at the crack. That's not blocking on its own.
    - **But the old bug-bomb asset (the yellow can with the red NO stamp) now plays over 3:31–3:45, the escort line** ("Can't live with it? Maryland Extension says escort it outdoors…").
    - That is the flagship's 5:04 gag again (Job A repeat), and it contradicts the line on screen.
    - Fix: over 3:31–3:45 show the script's escort visual: Meatball holds the front door open with a bow, a paper cup and card in paw, and the cup never goes over the bug. Over 3:20–3:30, use the mist-stops-at-the-cabinet-edge shot, with the antennae waving from the crack.
  - **Fix 8, visual: NOT applied. FIX.**
    - At 0:41–0:48 ("Most centipedes … die shortly after, from the lack of moisture"), the stubby centipedes still march in on the carpet and lie tipped over at an angle (frames at 0:45.5 and 0:47).
    - Fix: grey silhouettes on the card with a DRY AIR stamp; nothing on screen wilts or tips over. Rule: checklist Y3; Help 1311392, Unsatisfying or Off-putting.
  - **3:07 visual: FIX (small).**
    - The art is a crossed-out water drop, left over from the cut half "cutting indoor moisture also helps". The line now says only "focus on the bugs they eat".
    - Fix: cross out a small generic prey bug, or use a sticky trap with bugs, to match the CONTROL THE BUGS IT EATS card.
- **C1–C12:** no swears anywhere, first 7 s included.
  - Safety conditions are kept: the CSU "only if physically confined" line, and the escort line with the Penn State winter caveat spoken and on the card.
  - Rule 7 / C2: "Meatball's verdict: it stays, and the fan stays on" is an opinion; no tactic saves Meatball.
  - The optional 2:26 trim was not applied ("…or damage to your home" is still spoken). That's OK; it's sourced.
- **After the 3 visual fixes:** re-render and drop it in; audio needs no change. A frames-only re-check is enough.

**2. volume-1118/tt-flag-centipede.mp4 (TikTok 12 PM): PASS.**
- h264 1080x1920 plus aac, 63.8 s (T1 ≥61 s).
- Every spoken line is from the passed flagship centipede chapter, with the MSU condition kept ("unless it's handled or accidentally pressed against skin" plus "I never touched it").
- On-screen title "Is a house centipede dangerous?" is clean. No swears. The comment prompt is a genuine question (T4).
- It's a recut of our own long-form with its own arc, not padding (T2, T3).

**3. volume-1118/yt-silverfish-p5-short.mp4 (Short 1 PM): PASS.**
- 19.4 s.
- Facts: P5-F8 (weak jaws scrape paper), P5-F1 (fossils 400 million years, "about twice as long ago as the dinosaurs", hedge kept), P5-F7 (rapidly, including sideways). All word for word with silverfish-p5-1118.md. The BUG ID row "does not transmit disease" is P5-F2.
- No swears, and the ranking CTA is clean. The hook "Squish it or let it live?" is a question, not a claim.

**4. volume-1118/yt-flag-bedbug-short.mp4 (Short 4 PM): PASS.**
- 16.7 s (16–20).
- Facts: EPA BB21 dryer high heat 30 min, plus "just washing will generally not kill bed bugs". EPA BB23 heat ban kept whole: "That does not work, and it is dangerous." That's 2 sourced facts plus a payoff (C7).
- The on-screen title "Bed bugs: what actually kills them" matches EPA ("to kill bed bugs"). No swears.
- Watch: it opens on "What should you do?" with no bug named by voice in the first second. That's Studio's call, not a block.

**5. volume-1118/tt-flag-cockroach.mp4 (TikTok 4 PM): FIX before the slot.**
- 69.95 s. Facts all match the passed flagship cockroach chapter (CR8, CR10, CR6, CR39 with "extremely heavy" kept and the 0:24 "not extremely heavy" line, CR37, CR11, CR26, CR27, CR29, BB13).
- **The voice reads "1/16" as "one slash sixteen":** "can hide in a crack one slash sixteen inch wide" at about 0:08.5. Both small.en and medium.en hear "slash".
- Fix: re-voice that one line as "Adult German cockroaches can hide in a crack one-sixteenth of an inch wide." (CR10, UC IPM: "Adult German cockroaches can hide in a crack 1/16 inch wide.") The card text "1/16-INCH" can stay.
- If it can't be re-voiced before 4 PM, swap the slot.
- The "ABOUT 0" seen at about 0:14 is the egg-case counter mid-tick (it counts up to 30). OK.

**6. volume-1118/yt-house-centipede-p4-short.mp4 (Short 7 PM): PASS.**
- 16.4 s.
- Facts: P4-F1 ("Guinness listed among the fastest arthropods". The card "GUINNESS BOOK, 1973 · AMONG THE FASTEST ARTHROPODS" keeps "among", with no record claim. "About 16 inches a second, close to one mile an hour" keeps "about" and "close to".) Plus the script-safe MSU bite line, and P4-F3 pounce/lasso.
- No swears. This is the YouTube cut of Part 4, not a re-upload on the same platform.

**Also found (flagship v6, live since 11:12 AM, jD2GXfsiSO4):** the same "one slash sixteen" read is in the flagship at about 4:19 ("…crack one slash 16-inch wide"). It can't be re-voiced on a live video. Studio's call: leave it, or add a pinned or description correction ("1/16 inch"). The "not extremely heavy" condition at 4:35 is spoken in full.


## #11 (11/18 11:40 AM) 11/25 FLAGSHIP SCRIPT DRAFT: Writer + Research & QA please
channels/scripts/longform-christmas-tree-flagship.md: Christmas tree bugs, 1,525 words (about 10 min). Facts unchanged from the checked 11/10 script, plus F43 (Fraser fir) and F71 (scales). Lines tagged `joke` are new edgier lines: Writer, punch them up; QA, check them and the swear count (one "damn", after 0:07). Nolan stopped the extra Shorts batch, so this is now the main job. Build (new art: tree, egg case, aphid, lanternfly) starts tonight once you write PASS or edits here.

### #11 QA, 11/18 12:43 PM ET (Research & QA): FIX (header only); the joke punch-up passes
Checked: Writer's commit 382766d on channels/scripts/longform-christmas-tree-flagship.md.
- **(b) Diff:** all 10 changed lines are `joke` lines. No fact, safety or other line changed; all 10 '-' lines in the diff carry the `joke` tag. **PASS**
- **(a) Swears: 2, spoken only, none before 0:25.** **PASS**
  - "damn" at 3:39.87, captioned "dang". "Dang" is a minced word, not profanity, so it meets C10 ("Zero profanity in those places, bleeped or not").
  - [BLEEP] at 8:18.19. The caption "deserves a lump of coal" leaves the word out, so it also meets C10.
  - Both are within the 1-2 cap and later than the 7 s and MO 0:25 limits. None appear in the titles, description or on-screen text.
  - Render note: the voice must never say the bleeped word or the word "bleep". Use a comedy-kit bleep tone over a gap.
- **(c) "tiny cannibals" / "siblings eating each other":** supported. **PASS**
  - Penn State Extension, Insects on Real Christmas Trees, https://extension.psu.edu/insects-on-real-christmas-trees (live 11/18): "Mantises are predatory and cannibalistic, so will eat each other if no other food is present, as is usually the case indoors during the winter."
  - The condition is spoken just before ("There is nothing for them to eat in your living room").
- **(d) "Bougie little bugs. Fir snobs, honestly.":** **PASS**
  - It plays on the fact line right above it, which matches the source.
  - University of Illinois Extension, Christmas tree hitchhikers, https://extension.illinois.edu/news-releases/christmas-tree-hitchhikers (live 11/18): "A Female praying mantis commonly prefers Fraser fir Christmas trees for egg-laying."
  - It adds no number or new claim beyond that preference (C4).
  - It's not blocking, but if Writer wants it airtight: "Of course they do. Bougie little bugs. Fir snobs, mostly."
- **(e)** "three hundred" and "twelve years ago" are gone from the spoken lines; they now appear only in the changelog's old-text column. **PASS**
- **Other joke lines** (toddler starter pack, rumor in a lab coat, world's worst ornament, spooky/dramatic, counting bug legs, worst resort): none adds a fact, number, danger or motive, and none roasts the viewer (C4, C9). **PASS**
- **(f) Stale header: FIX.**
  - Line 3, current: "Swears: one light 'damn', after 0:07."
    - Fixed: "Swears: 2: spoken 'damn' at 3:39.87 (caption 'dang') and a [BLEEP] at 8:18.19 (caption omits the word); none before 0:25, none in titles, captions or on-screen text."
  - Line 5, current: "Words: 1525 (about 10.2 min at the flagship pace)."
    - Fixed: "Words: 1531 (9:52.65 at 155 wpm)." I recounted: 110 spoken lines, 1,531 words.
- **Scope:** I re-verified the fact lines the jokes rest on live today (F36, F37, F43). The other fact lines are unchanged from the checked 11/10 script (research 79) and were not re-run in this pass.
- **Build:** the art build can start tonight once the two header lines are fixed. That is a docs-only change; no re-QA is needed.


## #12 PHILOSOPHY TEST (11/18)
Script: channels/scripts/philosophy-ship-of-theseus.md (due 6:00 PM). Previews: channels/renders/philosophy-1118/preview-thumb.png, preview-first10s.mp4 (6:15 PM). Full renders: same folder, tt-philosophy-ship.mp4, yt-philosophy-ship.mp4 (8:00 PM). Research & QA: please check the script when it lands.

### #10 Sat v3 READY for the frames-only re-check (11/18 3:55 PM ET)
channels/renders/sat-longform/house-centipede-bathroom-v3.mp4 (4:23.9, h264 1920x1080 + aac, audio words and timing unchanged) and house-centipede-bathroom-v3-fixframes.jpg (12 frames).
- 0:41.5-0:47.4: grey still silhouettes on an OTHER CENTIPEDES card + DRY AIR stamp; nothing moves or dies.
- 3:07.2-3:11.1: a fly, then moth/fly/earwig crossed out (matches CONTROL THE BUGS IT EATS).
- 3:22.3-3:29.7: mist stops at the vanity cabinet edge; antennae wave from the baseboard crack. No can, no fan.
- 3:29.7-3:44.8: Meatball holds the front door with a bow, cup + card in paw, cup never over the bug; no bug-bomb can.
- Seen, NOT changed (outside the 3 fixes, your call): 3:11-3:18 (Connecticut "fans or dehumidifiers" line) shows the laundry room with "DRY IT OUT"; 3:18-3:22 ("My fan works now") shows the dehumidifier box, not the fan. Say FIX and I swap those 2 shots.
On PASS I schedule Sat 11/21 8 AM with thumb channels/renders/brand/thumb-centipede-bathroom.png.

- 11/18 3:40 PM: script + previews + TikTok READY: channels/scripts/philosophy-ship-of-theseus.md; channels/renders/philosophy-1118/preview-thumb.png, preview-first10s.mp4, tt-philosophy-ship.mp4 (64.0 s, voice check pass, gaps clean, lint pass). The Short (44.6 s) is rendering. Research & QA: please check the script now. Studio: previews to Nolan.
