# Long-form fix plan: audit, new edit template, recut spec (for Tue 11/17)

Prepared by Social: Long-form Editor, Mon Nov 16, 2026, ~9:15–9:35 PM ET. Rebuilt at ~9:35 PM ET after the box re-sync removed `/workspace/longform/`. The content is unchanged except for the Rulings section (§5) and the edits it requires.

**This is an edit spec only.** Nothing here is rendered, uploaded, scheduled, published, pushed to git, or changed in YouTube Studio. Jarvis owns production; Claude/Jarvis build from this. **Moondog88 sees the cut before anything is scheduled.** The Amazon affiliate spots are removed and appear nowhere in this plan.

**Where we stand** (`/workspace/retention/dig-1117.md`, vidIQ Race to 4K):
- **12.73 of 4,000** public long-form watch hours.
- Pace is about 0.7 h/day. Hitting 4,000 by 12/16 needs 132.9 h/day (dig §2).
- No long-form reaches the 50% AVD target (dig §3).
- Proxy exits cluster at **0:30**, **0:57–1:15** and **1:45–2:10** (dig §4). These are AVD-based, not measured cliffs.

---

## 0. Method and sources (what was measured, what was not)

**Media.** The audit covers the 4 public long-forms that got the v6b thumbnails on 11/16 (`drafts/thumbs-v6-1116/`): `cH3HCZ8GlHk`, `KWOM2-mNmww`, `viD-nbPdaxk` and `bqij8Ht6SX4`. They are the four Meatball-cartoon long-forms in `channels/packaging/winners-baseline-1115.csv`.

The channel has 13 public long-forms (dig §1). The other 9 are covered in `drafts/longform-plan-1116.md` §2 and are not re-audited here: Wolves, Weird Facts, 12 Myths, Extinct, Everything WRONG, 6 Creatures, CIA ×2 and Conspiracy.

**Files.**
- Public 480p renders, auto-captions and info JSON were pulled with yt-dlp to `/tmp/lf/` (~9:11 PM ET 11/16) and measured ~9:12–9:30 PM ET.
- *The `/tmp/lf/` work files were lost in the same re-sync.* The figures below are carried over from that run.
- To reproduce: re-download with yt-dlp and re-run the commands in the table.

| Check | How | Caveat |
|---|---|---|
| Shot length | ffmpeg `select='gt(scene,0.3)',showinfo`, plus a second pass at 0.15 | Our 2D animation changes overlays and poses on a fixed plate. At 0.3 the detector misses many of those changes. For example, the spider's first "cut" registers at 0:35, but the 0–30 s frames visibly change. Both thresholds are reported, and the real change rate is between them. |
| Dead air (audio) | `silencedetect=noise=-35dB:d=0.7` | **Zero silences in all 4 videos.** A music bed runs under everything (mean volume −16.8 to −17.9 dB). Here, "dead air" means speech gaps plus static or held visuals. |
| Speech gaps | Word timestamps from YouTube auto-captions (VTT) | Word times are approximate. A local Whisper pass couldn't handle the music-bed audio, so it was discarded. |
| Static / near-identical frames | 1 fps frames at 64×36. Consecutive mean abs diff under 2 counts as static. A frame matching any frame ≥15 s earlier (diff under 4) counts as a repeat. | Heuristic. Spot-checked on contact sheets. |
| First 30 s | 1 fps frames 0–30 s, viewed | — |
| Humor | My count of joke beats in the transcript (punchline lines and character gags) | Judgment. The house-rule C9 bar (`channels/qa/checklist.md`) is a joke every 5–7 s, ≈9–12/min. MO L154 says 6–9 per minute. |
| Retention | dig-1117 (Metricool YTVP06–08 AVD proxy); `winners-baseline-1115.csv` (Studio % viewed, CTR); research 72 (`skills/oh-meatball/research/72-hook-teardown-1110.md`) for the 3 Bugs Studio curve | **No per-second Studio curve for 3 of the 4.** |

---

## 1. Audit: our 4 Meatball long-forms vs the outliers

The outliers are the dig's own winners and losers:
- House-bug and spider "kill it or keep it?" episodes get both the views and the best hold. Myth and quiz compilations get the clicks, then lose people (dig §3).
- The 3 Bugs Studio curve drops 45% in the first 60 s. Its "hospital" promise isn't paid off until 3:49 (research 72 §b).

### Scorecard

| | **3 Bugs** `cH3HCZ8GlHk` | **Don't Kill the Spider** `KWOM2-mNmww` | **House Cat** `viD-nbPdaxk` | **Ranked** `bqij8Ht6SX4` |
|---|---|---|---|---|
| Runtime | 4:33 (no mid-rolls) | 8:17 | 9:16 | 8:57 |
| Views / hours (Metricool) | 214 / 4.43 h | 114 / 3.36 h | 42 / ~1.5 h (my calc: 42 × 2:11) | 5 / 0.06 h |
| AVD (proxy %) · Studio % viewed | 1:14 (27.3%) · 42.71% | 1:46 (21.4%) · 22.33% | 2:11 (23.6%) · 24.17% | ~8.0% · 9.92% |
| CTR (Studio, 11/15) | 5.44% | 4.63% | 1.95% | 1.31% |
| Shots (0.3 / 0.15) | 66 / 104 | 75 / 126 | 95 / 126 | 51 / 119 |
| Median shot (0.3 / 0.15) | 3.4 s / **2.3 s** | 5.0 s / 3.7 s | 4.9 s / 4.1 s | 6.8 s / 4.2 s |
| Runtime in holds >5 s (0.3 / 0.15) | 46% / 20% | 77% / 43% | 72% / 56% | 86% / 52% |
| Longest holds (0.3) | 15.1 s end card; 13.4 s @0:34 | 35.0 s @0:00; 23.9 s @5:39; 20.6 s @1:22 and @6:03 | 21.3 s @8:54; 18.3 s @7:49; 17.6 s @8:13 | 27.9 s @7:44; 27.0 s @6:11; 26.7 s @2:39; 26.0 s @0:16 |
| Cuts in first 30 s (0.15) | 9 (first @0:02.6) | 10 (first hard cut @0:35 at 0.3) | 9 | 6 |
| Audio silence ≥0.7 s @−35 dB | 0 | 0 | 0 | 0 |
| Speech gaps ≥1 s | 5 (5.6 s) | 12 (13.2 s) | 32 (37.9 s; max 2.9 s @3:52) | 11 (12.2 s) |
| Static runs ≥4 s | end card only (4:24–4:33) | 12 s @8:06 (end card); 5 s @5:04; 5 s @6:04 | none | none |
| Repeat frames (vs ≥15 s earlier) | **9.5%** (e.g. 4:14–4:19 ≈ 2:12; 2:44 ≈ 1:26; 4:02 ≈ 0:28) | 1.0% exact, but **one ceiling-web plate is ~33% of frames** (coarse color clustering) | 1.4% | **16.0%** (e.g. 3:06–3:15 ≈ 0:42; 4:34–4:43 ≈ 3:06) |
| Joke beats (my count) | ~2, ≈0.4/min. Research 72 counted 1. | ~15, ≈1.8/min. **Biggest gap 2:43–4:21 (98 s).** | ~16, ≈1.7/min. Joke-free **6:47–8:10.** | ~5, ≈0.6/min |
| End-screen window (after last word) | 10.6 s | 12.4 s | 12.3 s | **0.9 s** (VO runs to 8:56) |

Where the joke beats fall:
- **3 Bugs:** 0:34 "free pest control working the night shift" and 1:25 "eats pest insects for free."
- **Spider:** 0:16 chair, 0:27 Carol, 1:30 burrito, 1:36 "respected it," 1:54 doorbell, 2:43 other shoe, 4:21 roommate, 5:18 bath towel, 5:27 ceiling of Carols, 5:44 housekeeping, 6:53 furnace, 7:36 basement, 7:46 grain of rice, 7:54 "Carol's got it." Gaps over 30 s: 0:28–1:30, 1:55–2:43, 2:43–4:21, 4:31–5:18, 5:44–6:53 and 6:53–7:36.
- **House Cat:** 1:10 "holds you like a sandwich," 1:20 birthday cake, 1:47 "shame about the menu," 2:38 "Meatball brought milk," 3:48 asterisk, 4:15 "dungeon with a handle," 5:56 "hacked your human," 6:43 hairballs, 8:45 free rent, and others. The run from 6:47 to 8:10 is the mortality stats.
- **Ranked:** 0:31 "Wrong twice," 1:05 "just looking at you," 1:52 "yes, you too," 2:52 fly nursery, 4:10 ears safe.

### Per video

**1. 3 Bugs in Your House You Should Never Kill (And 4 You Must).** Best hours and best % viewed.
- **First 30 s:** strong. The hook claim lands at 0:00 ("can put you in the hospital"), the creature is named at 0:09, and there are 9 cuts.
- The weak spots are the 0:18–0:22 "Pennsylvania in 1849" tangent (video-review-1115) and the hospital promise, which isn't paid until 3:49 (research 72). Studio shows −45% by 1:00.
- **Pacing:** best of the four, with a median shot of 2.3 s at 0.15. There are 13.4 s and 9.5 s holds at 0:34 and 1:14.
- **Dead air:** negligible.
- **Repeats:** room plates come back, giving 9.5% repeat frames.
- **Funny:** almost not.
- **Top problem: almost no jokes, and the promised hospital bug is held to the last 45 s.** At 4:33 it also can't carry mid-rolls, and it earns only ~1.2 min per view.

**2. Don't Kill the Spider in Your Corner.** Best AVD of any long-form and second by hours.
- **First 30 s:** setup, not payoff.
  - 0:07.6–0:17 is a rules intro ("Give me three questions… This meter keeps score. If it says squish at the end…"). That breaks the 11/15 "no rules or keep-score intros" rule.
  - The first payoff ("102 dead things… every single leftover was a spider," "recorded eating giant house spiders") comes at 0:49–1:04.
  - The first hard cut at 0.3 is at 0:35, and 0:00–0:32 sits on the same ceiling-web plate.
  - Studio % viewed is 22.33%, against 42.71% for 3 Bugs. The channel-fix list already says to "rebuild the first 30 seconds."
- **Pacing:** 32 shots run over 5 s (at 0.15), which is 43% of the runtime.
- **Charts and document shots** break the 11/16 "no charts" rule:
  - a pie chart at ~0:55–0:59
  - a balance-scale diagram at ~2:00–2:08
  - "THE RUMOR" cards at 3:08–3:12
  - "CHARGES" at 5:32–5:36
  - a notepad at 7:08–7:12
- **Dead air:** the end card is static for 12 s at 8:06.
- **Repeats:** one plate fills about a third of the video.
- **Funny:** the funniest per minute of the four, but the jokes are clumped.
- The "big one from the start" payoff at 7:52 ("Carol's got it") shows only a shadow (frames 7:53–7:54).
- **Top problem: the opening 0:00–0:20 explains the format instead of paying it off, then the video holds one plate for 35 s.**

**3. Your Life as a House Cat.** Highest minutes per view, tiny reach.
- **First 30 s:**
  - 0:00–0:15 is OK.
  - 0:13–0:16 is a keep-score setup ("Then we add it up. Raw deal or sweet deal?" plus the meter).
  - 0:17–0:21 reads "A 2007 genetic study of 979 cats…" aloud, which video-review-1115 flagged.
  - No payoff by 0:20.
- **Pacing:** 47% of shots run over 5 s (at 0.3), with long holds in the mortality section.
- **Dead air:** 32 small speech gaps.
- **Repeats:** low.
- **Funny:** yes until 6:47, then nothing until 8:10.
- **House-rule flag (C11):** there's profanity on a YouTube long-form: "damn" ×~6, "hell," "badass," and "bastards" at 8:53. C11 allows mild words, with stronger ones bleeped. My judgment is that "bastards" needs a bleep.
- **Top problem: reach (CTR 1.95%, 42 views), plus an open that cites a study.** This is a packaging problem first.

**4. I Ranked Every Creature Living In Your House From Harmless to Deadly.** Worst on every measure.
- **The whole video is vertical with blurred sides** (checked frames at 0:00–0:30, 2:30, 5:00, 7:30 and 8:40). MASTER_ORDERS (Nolan 11/5) bans "blurred-side vertical."
- **First 30 s:** the hook is good. At 0:00 it says "venom 15 times more toxic than a rattlesnake's" and "top spot stays hidden till the end." Then it holds on the daddy longlegs for 26 s (0:16–0:42).
- **Pacing:** 86% of the runtime is in holds over 5 s (at 0.3).
- **Repeats:** 16% of frames.
- **Funny:** ≈0.6 jokes/min. The verdict shape repeats 17 times.
- **End screen:** effectively none.
- **Top problem: the vertical layout with blurred sides and 26–28 s holds.** Per the ruling (§5), it gets a full 16:9 rebuild, not a recut.

---

## 2. NEW long-form edit template (8–10 min, house-bug / spider / born-as)

This combines:
- the 11/15 pacing rule
- the 11/16 anti-boring rules (TASKS.md TOP PRIORITY 11/16 5:10 PM)
- QA C9–C12
- the research 72 checklist §(e)
- dig §5

### 2.1 Hard rules
1. **Promise by 0:05.** Name the creature and the stakes in the first line. Frame 0 is the thumbnail panel. No logo, no "today we're going to," no rules or meter explanation, and no study names or years.
2. **Cold-open payoff by 0:20.** The best visual moment plays by 0:20, even if it plays again later. Then give a count and order in ≤3 s using on-screen chips.
3. **Open loop 1 at 0:55 (±5 s).** A spoken tease plus an on-screen card that names the scariest payoff and roughly when it comes. Pay it off between 2:00 and 4:00, never last.
4. **Open loop 2 at 1:40 (±5 s).** A different tease, such as a rumor, a "the one in your bed" item or a twist. Pay it off by the midpoint, then re-hook with loop 3 at the midpoint.
5. **Pattern break every 20–30 s.** Any of: a new location or plate, a scale change, Meatball entering or leaving, a POV switch, a countdown chip, a 0.5 s freeze-frame with SFX, or a music drop. Never run the same item shape more than twice in a row (research 72).
6. **A joke every 5–7 s (C9).** It can be a VO punchline or a visual or physical gag with SFX. The fact lands as or right after the punchline. Jokes never add facts (C4).
   - **A physical Meatball gag every 30–45 s** (11/16 rule 4).
   - **Cursing:** none in the first 7 s or in titles, thumbs, captions or text (C10). YouTube long-form gets mild words only, or bleeps (C11). No slurs or sexual content (C12).
7. **The picture changes every 2–3 s, and no shot holds longer than 5 s** (11/16 rule 3).
   - No charts, scales, documents or text slides. Show data as physical gags.
8. **Sound:** an energetic read with a pause before each punchline and stress on the number. Music under everything, and an SFX on every action.
9. **Safety lines keep their condition.** No jokes or mid-rolls on them or right after.
10. **Citations:**
    - Put an on-screen source tag on every fact card and a Sources block in the description.
    - Say studies plainly, with no years or sample sizes read aloud.
11. **One mid-video comment prompt,** an either/or question, between 2:30 and 4:00.
12. **Full episodes only.** Never a stitch, compilation, recut of posted Shorts, or blurred-side vertical (MASTER_ORDERS).

### 2.2 Chapters, mid-rolls, end screen
- **Chapters** ([9884579](https://support.google.com/youtube/answer/9884579)):
  - Start at `00:00`, with ≥3 chapters of ≥10 s each.
  - Stamp from the **final** render.
  - Title each chapter with the item or stake.
- **Mid-rolls** ([6175006](https://support.google.com/youtube/answer/6175006)):
  - They need 8:00+. Aim for 8:30–9:30 so trims don't drop the video under 8:00.
  - Place them at chapter gaps only, never before 2:00, never on or right after a safety line.
  - Default to 2 breaks (~2:30 and ~5:00). Add a 3rd (~7:00) only at ≥9:00.
  - Turning them on is a Studio setting for Moondog88.
- **End screen** ([6388789](https://support.google.com/youtube/answer/6388789)):
  - Runs in the last 5–20 s.
  - Leave ≥12 s of animated end card after the last VO word.
  - The VO names the next episode, and the tile shows that episode once it's public (otherwise 3 Bugs). Add a playlist tile and a subscribe button.

### 2.3 Minute-by-minute beat grid (9:00 target; scale ±1 min)

| Time | Beat | Must-haves |
|---|---|---|
| 0:00–0:05 | Promise | Creature + stakes; frame 0 = thumbnail; joke or SFX hit by 0:05 |
| 0:05–0:20 | **Cold-open payoff** | Best visual moment; one punchline |
| 0:20–0:25 | Count + order | 3 chips, ≤3 s VO |
| 0:25–0:55 | Chapter 1 opens | Strongest fact first; pattern breaks at ~0:30 and ~0:50 |
| **0:55** | **Open loop 1** | Tease card + VO |
| 1:00–1:40 | Chapter 1 payoff run | Physical gags at ~1:05 and ~1:35 |
| **1:40** | **Open loop 2** | Second tease + gag |
| 1:40–2:30 | Chapter 1 close → chapter 2 | Pay loop 1 by 2:00–2:30; end on the next chapter's stake |
| 2:30 | Mid-roll 1 (chapter gap) | Only if ≥8:00, not on a safety line |
| 2:30–3:30 | Chapter 2 | Comment prompt ~3:00 |
| 3:30–4:30 | Chapter 2 close | Pay loop 2 by ~4:00; **midpoint re-hook ~4:30** (loop 3) |
| 4:30–5:30 | Chapter 3 (case against / twist) | Flip the shape; new plate |
| 5:00–5:30 | Mid-roll 2 (chapter gap) | Not in a medical or safety cluster |
| 5:30–6:30 | Chapter 4 | New location; gag every 30–45 s |
| 6:30–7:30 | "The deal" / what to do | Instructions as gags; safety lines clean |
| 7:30–8:10 | Verdict + callback | Pay loop 3 and the cold-open callback **on screen** |
| 8:10–8:20 | Next-episode line | VO names it |
| last 12–20 s | End screen | Animated; tile = that episode |

### 2.4 Editor checklist
- [ ] Frame 0 matches the thumbnail; promise by 0:05; no rules or meter intro; no study year or size in 0:00–0:30
- [ ] Visual payoff by 0:20 (timestamp: ____)
- [ ] Loop 1 at 0:55 ±5 s (____), paid at ____
- [ ] Loop 2 at 1:40 ±5 s (____), paid at ____
- [ ] Midpoint loop (____), paid at ____
- [ ] Scene-detect at 0.15: median ≤3 s; **no shot over 5 s** except the end card (list any exceptions)
- [ ] Joke log with timestamps; no gap over 7 s; a physical Meatball gag every ≤45 s
- [ ] No charts, scales, documents or text slides
- [ ] No plate over 15% of runtime; no near-identical repeats except deliberate callbacks
- [ ] Music bed throughout; SFX on every action; no flat read; profanity per C10/C11 (list each swear and bleep)
- [ ] Safety lines verbatim with their conditions; no joke or mid-roll on them
- [ ] Source tags on every fact; description Sources block matches
- [ ] Runtime ≥8:00 if mid-rolls are planned
- [ ] Chapters start 00:00, ≥3, each ≥10 s, stamped from this render
- [ ] ≥12 s animated end card; VO names the next episode; tile target noted
- [ ] Native 16:9 full episode, with no stitch, compilation, Shorts recut or blurred-side vertical
- [ ] QA has passed the cut (§5) **and** Moondog88 has watched it. Nothing is scheduled or uploaded before that.

---

## 3. Recut: **Don't Kill the Spider in Your Corner** (`KWOM2-mNmww`). Pick confirmed by the Social Studio ruling (§5).

**Why this one:**
1. **It has the best hold in absolute time:** AVD 1:46 (dig §3).
   - It's second by hours (3.36 h) on about half the views of 3 Bugs (114 vs 214).
   - That makes **~1.8 min per view, against ~1.2 for 3 Bugs** (my calc: hours × 60 ÷ views).
2. **Its packaging works.** CTR is 4.63%, 2.4× House Cat's, and it's in the lane the dig says wins on both reach and hold (dig §3, §5.3).
3. **At 8:17 it can carry mid-rolls.** 3 Bugs (4:33) can't, and the 11/16 plan says not to pad that winner.
4. **Its failure is the fixable kind, and it's in the first 30 s.** It's at 22.33% viewed vs 42.71% for 3 Bugs. The causes are the rules/meter intro, a payoff that comes at 0:49–1:04, and 35 s on one plate. The footage already has the payoff shots and 15 jokes.

The runner-up is House Cat, but its problem is reach, so packaging should come first. 3 Bugs gets fixed in place, and Ranked gets a rebuild (§5).

**Mechanics:** inserts and re-ordering can't be done as in-place Studio trims, so the relaunch is a **new upload of a substantially re-edited episode.** That's my understanding; Jarvis should confirm. How the original is handled is set by the ruling (§5): it stays live for 48 h, then is unlisted only if the recut wins, and is never deleted.

**Unverified risk:** YouTube's monetization review checks for "inauthentic content," meaning repetitive or mass-produced videos ([YouTube Help 1311392](https://support.google.com/youtube/answer/1311392), 7/15/2025 update). It focuses on most-viewed and newest videos. Two similar public versions overlapping for 48 h+ could look repetitive. That's why the recut must be genuinely re-edited, not trims plus a re-upload.

### 3.1 Recut EDL (source = current public video)
- Source times come from auto-captions (±0.2 s); Jarvis snaps them to breaths on the master audio.
- "Dup" means the line is also kept in its original place. Give the second showing a **new angle**.

| # | Source in–out | New time | Line (existing VO) | Picture |
|---|---|---|---|---|
| CO-1 | 0:00.0–0:07.3 | 0:00.0–0:07.3 | "That skinny spider in the corner of your ceiling is hunting something in your house. Sometimes something much bigger, and you're standing on a chair holding a shoe." | Cut on every clause (5 changes): ceiling → shadow of the big one (src 0:04) → Meatball wobbling on the chair with the shoe. SFX: creak, shoe whoosh. |
| CO-2 (dup) | 1:00.7–1:04.0 | 0:07.3–0:10.6 | "She has been recorded eating giant house spiders, the big ones." | Giant house spider plate (src 1:01–1:04). Hard cut + stinger. |
| CO-3 (dup) | 1:24.7–1:31.9 | 0:10.6–0:17.8 | "She stays out of reach and flicks silk over it with her back legs. Left, right, left, right. Like wrapping a burrito she's scared of." | The wrap (src 1:26–1:32). Punch in on each left/right with a silk-zip SFX. **Payoff on screen from 0:10.6.** Meatball reaction on "burrito." |
| CO-4 (moved) | 0:09.8–0:12.9 | 0:17.8–0:20.9 | "What's it hunting? Can it hurt you? And what happens if you leave it up there?" | 3 chips. The meter appears as an overlay with no explanation. |
| CUT | 0:07.3–0:09.8 | — | "Give me three questions before you swing." | Rules intro |
| CUT | 0:12.9–0:17.3 | — | "This meter keeps score. If it says squish at the end, I'll hold the chair." | Keep-score intro. The chair joke becomes a visual gag in CO-1. |
| CH1 | 0:17.3–0:34.7 | 0:20.9–0:38.3 | "Question one. What is it hunting? Meet the cellar spider… anything that blunders in." | Chapter card at 0:20.9. No shot over 3 s. |
| CUT | 0:34.7–0:40.9 | — | "In one lab, cellar spiders were fed just one fly every three or four days and still laid eggs." | Off-promise tangent |
| CH1 | 0:40.9–0:58.4 | 0:38.3–0:55.8 | "But flies are not why you should put the shoe down… Every single leftover was a spider." | **Replace the pie chart** (src ~0:55–0:59 → new ~0:52–0:56) with Meatball in rubber gloves tipping out the shed tray while the count ticks up. Keep the source tag. |
| **LOOP 1** (dup) | 1:57.1–2:00.6 | **0:55.8–0:59.3** | "Now the question everyone asks. Does she eat brown recluses?" | Card: "Brown recluse vs Carol → 2:04". Meatball hides behind the chair. *The captions dropped "brown recluses"; a local transcription heard it. Confirm on the master.* |
| CH1 | 0:58.9–1:37.4 | 0:59.3–1:37.8 | "And she doesn't stop at her own size… I did not sleep, but I respected it." | New angles where the 1:00.7 and 1:24.7 lines play again. "Picture it. 2:00 in the morning" (new 1:09.9): Meatball wakes, alarm SFX, climbs onto the chair. |
| **LOOP 2** (moved) | 2:32.5–2:33.6 | **1:37.8–1:38.9 (+1.5 s gag → 1:40.4)** | "But you've heard the other thing about her." | Card: "'Deadliest venom of any spider'? → 2:37". Meatball raises the shoe, then slowly lowers it. Cut the line from its original place. |
| CH1 | 1:37.4–2:32.1 | 1:40.4–2:35.1 | "And she doesn't only hunt at home… Carol is not a recluse cure… even big ones." | Keep the doorbell gag. Replace the **balance-scale diagram** (src ~2:00–2:08) with a boxing-ring plate of Carol vs the recluse. A "RECLUSE CURE" box gets stamped NOT. |
| CH2 → end | 2:34.0–8:16.9 | 2:35.1–8:18.0 | Unchanged VO, from "Question two. Can it hurt you?" to the end card | Fixes in 3.3. New time = source + 1.1 s. |

**New runtime is about 8:18.0**, which keeps it at ≥8:00 so mid-rolls stay eligible. Overlay gags add no time; punchline pauses do.

### 3.2 New chapters (re-stamp from the final render)
```
00:00 Put the shoe down
00:21 What is it hunting?
02:35 Can it hurt you?
04:30 The case for the shoe
07:00 The deal
07:38 The verdict
```
Derived from the source:
- "Question two," src 2:34.0 → 2:35.1
- "Here is the case for the shoe," src 4:28.9 → 4:30.0
- "So here's the deal," src 6:59.6 → 7:00.7
- "Final score," src 7:37.3 → 7:38.4

**Mid-rolls** (a Studio setting for Moondog88):
- **2:35** and **4:30**, with **7:00** optional.
- Keep them off the "Barely. Recorded bites were mild" safety beat (~4:21) and off the jar/relocation instructions.

**Comment prompt:** keep "Tell me in the comments which of the three you've been calling daddy longlegs" (src 3:05.6 → **3:06.7**).

### 3.3 Dead-air, hold and repeat fixes (new = source + 1.1 s after 2:34)
- **Holds to break** (source shots over 5 s at 0.15). Each needs a new pose, angle or plate every 2–3 s:
  - src 2:34.0 (8.0 s), 2:47.6, 2:56.5, 3:09.2, 3:15.2, 3:24.1, 3:32.7 (7.5 s), 3:40.2, 4:04.6, 4:12.5, 4:34.9, 5:01.3 (7.2 s), 5:19.1, 5:32.5, 5:55.4 (7.9 s), **6:03.3 (10.3 s)**, 6:42.7, 7:02.6, 7:08.7, 7:14.5 (7.9 s), 7:22.4, 7:29.1, 7:44.4
  - in the CH1 span: 1:04.4, 1:22.2, 1:28.4, 1:49.6 (7.5 s), 2:00.7, 2:06.3, 2:15.0
- **Static:** src 5:04 (5 s) and 6:04 (5 s) need motion. Animate the 12 s static end card at 8:06 (Meatball waving the shoe, Carol dangling).
- **Document and chart shots to replace with gags:**
  - "THE RUMOR" (src 3:08–3:12) → Meatball tears it up
  - "CHARGES" (5:32–5:36) → Carol in a tiny dock, with a gavel SFX on "bad housekeeping"
  - the notepad (7:08–7:12) → a calendar flip with the vacuum
- **Plate fatigue:** the ceiling-web plate is ~33% of frames. Give each return a new angle (low POV from the bed, extreme close-up on the legs, a wide of the room).
- **A payoff that doesn't land:** at src 7:52–7:55, "Here it comes. Carol's got it." shows only a shadow. **This needs one new shot:** 2–3 s of Carol wrapping the big one on the wall, mirroring CO-3.

### 3.4 Joke inserts (visual or physical, no new facts; one beat every 5–7 s)
The existing VO jokes land at about (new times): 0:14.6, 0:31.4, 1:30.7, 1:37.3, 1:57.8, 2:44.6, 4:22.7, 4:32.1, 5:19.2, 5:28.6, 5:45.8, 6:54.4, 7:37.8, 7:48.0 and 7:55.6, about 15 in all. Add a visual or SFX beat in every gap over 7 s. These are the priority gaps:

| Gap (new) | Anchor (existing VO) | Gag |
|---|---|---|
| 0:31–0:56 | "anything that blunders in" / "102 dead things" | A fly blunders in wearing a tiny helmet; the tray sort |
| 1:00–1:30 | "Picture it. 2:00 in the morning" | Meatball wakes and silently screams; chair-wobble callback |
| 2:04–2:35 | "In a lab in Brazil… five times heavier" / "not a recluse cure" | A bathroom-scale weigh-in (no numbers); the NOT stamp |
| **2:45–4:22 (98 s)** | "three different animals get called daddy longlegs" / "urban legend" / "bit a person on camera" / "sore about 1 mm wide" | A police lineup; the rumor card shredded; Meatball offers his arm, braces, shrugs; a tiny magnifying glass |
| 4:32–5:19 | "She carries her eggs in her jaws" / "your corners" | An egg bundle as a grocery bag; baby Carols planting flags in every corner |
| 5:46–6:54 | "whirls… into a blur" / "7 of the 10" / "people carried [her] around the world" | Meatball gets dizzy watching the blur; Carol with suitcase stickers |
| 6:54–7:37 | "A vacuum or a broom" / "put a jar over her" | Meatball vacuums while Carol ducks; jar-and-paper slapstick |

Keep a physical Meatball gag at least every 45 s, and give every gag an SFX.

### 3.5 Title and thumbnail angle (notes for Packaging; no Studio change)
- The current title gets 4.63% CTR. The v6b thumbnail has been live since 11/16 with no data yet, so wait 72 h before judging it.
- **Relaunch angle:** the tiny spider beating a much bigger one ("recorded eating giant house spiders," an existing sourced line). Keep the hedge. No TRUE/FALSE/Myth/Believe.
- **Thumbnail:** cellar spider mid-wrap on a giant house spider, Meatball on a chair with the shoe, "SQUISH IT?" style (`channels/packaging/longform-bug-1-4-titles-thumbs-1117.md` §1).
- Titles are Packaging's call. Moondog88 approves anything that goes live.

### 3.6 End screen
- **Window:** the VO at new 8:01.6 says "Next time, the 30-legged thing in your bathroom… Until then, here are eight more bugs. Three to keep, five to kill." That leaves **8:01.6–8:18.0 (16.4 s).**
- **Tile 1:** house centipede v2 (scheduled Sat 11/21 08:00, `posted.csv`) once it's public.
- **Tile 2:** 3 More Bugs (`xeAsg5ECpgw`).
- Plus a subscribe button.
- **Fallback:** 3 More Bugs plus the Kill It or Keep It playlist (`PLd9ViCdnwfoQ`).

### 3.7 The other three
- **3 Bugs:** the 0:18–0:22 trim and the 1:30 comment prompt (plan-1116 §2) stand. Any v2 would be a new episode built on this template.
- **House Cat:** packaging first. If Moondog88 approves, Studio-trim the 0:17–0:21 study line and bleep "bastards" at 8:53 (C11).
- **Ranked:** gets a full 16:9 rebuild (see §4).

---

## 4. Ranked: 16:9 rebuild spec (queued after the Spider recut; ruling §5)

- **This is a rebuild, not a recut.** It's a new native 16:9 render in the cartoon kit. The current vertical version stays live until the rebuild ships.
- **Keep:** the hook ("venom 15 times more toxic than a rattlesnake's… top spot stays hidden till the end"), the 17-item order, the "Still to come" teasers (1:40, 3:08, 4:36, 6:05, 7:12), every safety line with its condition, and all sourced facts as written. Re-run the fact check only where a line changes.
- **Fix:**
  - The template in §2 applies in full: a cold-open payoff by 0:20, loops at 0:55 and 1:40, and no hold over 5 s. The current holds run 26–28 s.
  - Break up the 17× repeated verdict shape ("X, F tier, harmless…"). Every third item gets a different shape (a versus, a myth flip, a Meatball test).
  - Joke density goes from ≈0.6/min to the C9 bar.
  - Leave a ≥12 s end-screen window. The current one is 0.9 s.
- **Runtime:** keep it ≥8:00.

---

## 5. Rulings (Social Studio, 11/16 9:31 PM ET)

1. **Spider is the pick.** The recut is approved once QA passes it. Moondog88 still sees the cut before anything is scheduled.
2. **The original stays live** until the recut has 48 h of data. If the recut beats it on **views AND average view duration**, the original goes to **unlisted, never deleted.** Its end screen and pinned comment then point to the recut. These are Studio actions for Moondog88 or whoever he authorizes; this plan doesn't make them.
   - For a fair test, compare both videos on their first 48 h. For the original, use Studio's first-48 h figures, not its lifetime numbers.
3. **Ranked gets a full 16:9 rebuild** in the cartoon kit, queued after the Spider recut (§4). The vertical version stays live until the rebuild ships.
4. **The Amazon affiliate spots are removed.** There are no affiliate links, spots or disclosures in any long-form, description or plan. `drafts/longform-plan-1116.md` was checked and has none. The committed 11/16 revisions (`channels/longform/spider-house-edition-revision-1116.md`, `dog-bornas-revision-1116.md`, commit 4f5b53d) never had any.

---

## 6. Still unverified / needs Moondog88

- **Per-second Studio retention curves** for Spider, House Cat and Ranked. Only Moondog88 can screenshot them. The dig's exit points are AVD proxies.
- **Studio hours:** vidIQ shows 12.73 h and Metricool shows 17.53 h (dig §1).
- **Scene counts:** these are a range between the two thresholds. Joke counts are my reading. Caption word times are ±0.2 s, and "brown recluses" at src 1:59 comes from a local transcription.
- **Raw files:** the `/tmp/lf/` work files were lost in the re-sync, so the raw measurements need re-pulling if anyone wants to audit them.
- **Mechanics:** I haven't verified that the recut must be a new upload, or how YouTube treats two similar public versions under the inauthentic-content review.
- **Calculations:** minutes per view and House Cat's hours are my numbers from dig-1117.

---

## Note for Claude (paste under "## Notes for Claude" in TASKS.md)

```
2026-11-17 — Long-form Editor via Social Studio. Long-form fix plan: /workspace/longform/fix-plan-1117.md (copy: /workspace/drafts/fix-plan-1117.md). Edit spec only; Jarvis owns production.
(1) NEW long-form edit template (§2): promise by 0:05, cold-open payoff by 0:20, open loops at 0:55 and 1:40, pattern break every 20–30 s, joke every 5–7 s (C9), physical Meatball gag every 30–45 s, no shot >5 s, no charts/docs, chapters 00:00/≥3/≥10 s from the final render, mid-rolls only at chapter gaps on ≥8:00 cuts, ≥12 s animated end card naming the next episode. Use it for every new long-form.
(2) RECUT, approved by Social Studio once QA passes it: Don't Kill the Spider in Your Corner (KWOM2-mNmww). EDL §3.1: new cold open from existing VO (src 0:00–0:07.3 + 1:00.7–1:04.0 + 1:24.7–1:31.9 + 0:09.8–0:12.9); cut the rules/meter intro (0:07.3–0:09.8, 0:12.9–0:17.3) and the lab-fed tangent (0:34.7–0:40.9); loop 1 at 0:55.8, loop 2 at 1:37.8; replace pie chart/scale/document shots with gags; break every hold >5 s (§3.3); one NEW shot: Carol wrapping the big one at the 7:5x callback. ≈8:18; chapters 00:00/00:21/02:35/04:30/07:00/07:38; mid-rolls 2:35 + 4:30 (Moondog88's setting). End-screen tile: house centipede v2 once public, else 3 More Bugs.
(3) Original KWOM2-mNmww stays live until the recut has 48 h of data. If the recut beats it on views AND average view duration, the original goes to UNLISTED (never deleted) and its end screen + pinned comment point to the recut. Those are Studio actions for Moondog88; not from this note.
(4) Ranked (bqij8Ht6SX4): full 16:9 rebuild in the cartoon kit, queued AFTER the Spider recut (spec §4). The vertical version stays live until the rebuild ships.
(5) Amazon affiliate spots are removed: no affiliate links, spots or disclosures in any long-form or description.
(6) QA pass first, then Moondog88 sees the cut before anything is uploaded or scheduled. No Studio changes from this note.
```
