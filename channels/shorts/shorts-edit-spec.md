## Social Studio rulings, 11/15 8:30 PM ET (now policy)
1. **Long-form promise placement:** a spoken 3-5 word promise goes inside the loop line, before the closing "And", so the Short stays within 16.0-18.0 s.
2. **Promise target:** each Short points to the long-form that its Related video link already uses, as listed in `/workspace/packaging/studio-related-links.csv` (match on `short_id`, use `related_longform_title`). The promise names that video's creature or topic, for example "full corner-spider video linked." Once a bug long-form posts, its Shorts switch their promise and Related link to it.
3. **Scope:** the six queued test Shorts (11/16-11/20) ship as re-trimmed, without re-cutting the hook or the promise, because renders are frozen until Jarvis's animation spec. The new rules apply only to scripts that haven't been rendered yet.

# Short-form edit spec (YouTube Shorts + TikTok)

## Changelog, 11/15 8:30 PM ET

SPEC CHANGE ONLY. No renders, no pipeline changes, no commits. Matches the "Script and edit rules" in `plan-update-1115.md` (Moondog88's decisions, relayed through Jarvis and Social Studio).

- Frame 0 now must show the threat in close-up (was: the creature mid-action in the hook room).
- Hook rule is now you + your home + a number or threat, under 12 words; hedges stay where a fact needs one (was: about 6–8 words, search keyword plus payoff). The claim card stays on at 0.00 s.
- Visual pace is now a new picture every 1–2 s, with no gap over 2.0 s (replaces the 1–3 s Shorts rule and the 2–4 s long-form note).
- Comment rule is now one comment trigger per script, phrased as a debate prompt (replaces one open comment question).
- Every Short must speak a long-form promise that points to the matching long-form. The promise has to fit inside the 16–18 s Nov 16–29 length budget, which this update does not change. Placement is now policy (ruling 1 below): a 3–5 word promise inside the loop line.
- Existing rules restated: sourced facts; safety lines keep their condition; no team logos or betting; titles name the creature or carry the series tag; Shorts stay at 3 a day, at least 3 h apart.
- House animation style: moving to illustrated panels for hooks and payoffs plus the code-drawn rig for action. Jarvis owns that spec. Current renders stay as they are until Jarvis hands it over.

Status: **draft only**, Sunday, Nov 15, 2026, 8:30 PM ET, America/New_York. Written to `/workspace/drafts/` for Social Studio to commit. No repo edit, no render, no schedule, no post, no channel-settings change.

Owner: Shorts Editor. This is the house edit spec for Oh Meatball / Would Meatball Survive? short-form. The pass/fail checklist and the 11/16–11/20 grading and trims live in `shorts-edit-checklist-v1.md`. Edit decision lists for the two hook rewrites are `shorts-edl-carpet-beetle-window.md` and `shorts-edl-christmas-tree-bugs.md`.

Proven vs guideline is marked on every rule. "Proven" means it is backed by a number or an already-locked house order cited below. "Guideline" means a working method that has not been isolated in our data. The 11/15 8:30 PM ET script and edit rules above are house orders from Moondog88.

## Sources this spec is based on

- Channel plan update: `/workspace/drafts/plan-update-1115.md` (Moondog88's decisions, relayed by Jarvis, 8:26 PM ET). Script and edit rules below follow that file.
- Packaging plan: `/workspace/packaging/shorts-viewjail-and-longform-plan-1115.md` (also `channels/packaging/shorts-viewjail-and-longform-plan-1115.md` in the repo). Studio export, Last 90 days, Aug 17–Nov 14, 2026, 86 Meatball Shorts.
- Scriptwriter 1-second hook bank: `/workspace/drafts/shorts-hooks-1s-1115.md` (same text as `channels/scripts/shorts-hooks-1s-1115.md`).
- Meatball bible: `/workspace/drafts/meatball-bible.md`.
- House pipeline shape: existing v6 Short JSON (`captions`, `caption_y`, `cut_whoosh`, `music`, `loop`, `beats`). Queued bug specs in `/workspace/packaging/lint-specs/` and `/workspace/skills-readonly/skills/oh-meatball/scripts/drawn-house/`.
- MASTER_ORDERS (skills-readonly copy): YouTube Shorts 16–20 s standing rule, no Short under 15 s, 3/day at least 3 hours apart, voice `en-US-AndrewMultilingualNeural` at +10% / +3Hz.
- Related-video rule: `/workspace/packaging/related-video-rule.md`.
- Official platform pages cited in the checklist (safe zones, Shorts format, YPP inauthentic-content policy).

## Locked pipeline values (already in the v6 JSON)

These are how the current renderer is set, not a claim that the numbers were A/B tested:

- Voice: `en-US-AndrewMultilingualNeural`, `rate` +10%, `pitch` +3Hz.
- Spoken-runtime math: **194.5 wpm**, calibrated in house scripts to the posted moose minute cut (289 words in 89.13 s on Andrew at +10%). A word is a token with letters or digits; contractions, hyphenated words, and numerals count as one (`shorts-hooks-1s-1115.md`).
- YouTube house bed: `music: mystery`, `music_db: -13`. TikTok short twins in the current drafts use `music: detective`, same level.
- Burned-in captions: `captions: 66` (px, on a 1080×1920 frame), `caption_y: 1180`. Hook/fact cards in the queued bug specs sit at `card.y: 470`. TikTok search cards use `search_top.y: 150` for about 2.5 s (`tts-cats-knead.json` and the meatball bible).
- `cut_whoosh: true` on beat cuts. Some last beats also fire `tink` / `pop` SFX. Do not invent new cue names.
- `loop: true`. Last spoken word is **And**, in the hook's room, so the picture and the sentence both return to frame 0.
- Meatball hops in at about 2.3 s. Line 2 is the acted gag, aimed at the 3–7 s window. The joke adds no number, danger, feeling, motive, or safety instruction.

## House animation style (Jarvis)

The house animation style is moving to illustrated panels for hooks and payoffs plus the code-drawn rig for action. Jarvis owns that spec and the pipeline for it. Current renders stay as they are until Jarvis hands it over. This file does not change renderer settings, and it is not a request to restyle queued or already-rendered files.

---

## 1. 0–1 s hook rules

**Proven (channel data + platform signals, packaging plan §a–b):** Shorts are judged on whether viewers chose to view or swiped, then on average view duration, average % viewed, likes and surveys ([S1][S2] in the packaging plan). Team research from 11/11 measured roughly 60% swiping away in the first second. Studio's AI saw 15–24% drops between 0:04 and 0:06 when narration turned textbook. The two best openers in the plan say the twist immediately.

**House rules (plan update 11/15 8:30 PM ET):**

1. Frame 0 shows the threat in close-up. No establishing shot, no logo, no "Meatball here," no countdown, no rules intro. Meatball is not in the frame yet.
2. Voice and the payoff card start at 0.00 s. Keep the claim card at 0.00 s. The on-screen claim matches the spoken hook in meaning, word for word.
3. The hook is you + your home + a number or threat, and it is under 12 words. Hedges stay where a fact needs one (`about`, `typically`, `can`, `may`, `up to`), in the voice and on the card.
4. No spoken study name, year, or sample size in the hook. The full searched question lives in the title, the first description sentence, and (on TikTok) `search_top`. Titles name the creature or carry the series tag.

**Guideline, and a known tension:** Packaging asked for the hook to "land in the first second." At 194.5 wpm, a hook just under 12 words can take about 3.4 s, so the spoken payoff often finishes after 1.00 s. The fix is editorial, not a faster read: the **card must state the full claim inside the first second**, while the voice starts that same line at 0.00 s. Do not speed the voice past the locked Andrew settings.

---

## 2. Visual change every 1–2 s

**House order (plan update 11/15).** This replaces the old 1–3 s Shorts cadence and the 2–4 s long-form note. Our data shows length and % viewed moving together, but it does not isolate cut frequency.

How to hit it:

- A visual change is a new scene, a camera move or scale change, a new card, Meatball entering, or a new action on the creature. A cut whoosh may land with the cut; do not add whooshes that are not in the pipeline.
- No gap between picture changes over 2.0 s. If a spoken line runs longer than 2.0 s (the loop line often does), place mid-line visual changes so no still holds more than 2.0 s.
- Do not change the fact, the hedge, the safety condition, or the room of the loop just to add a cut.

---

## 3. On-screen caption style

**Pipeline (locked in JSON), not a proven retention lever:**

- Burned-in word captions, size 66, at `caption_y` 1180, with yellow key words (`cap_key`) as in current v6 cuts. Center the caption block; do not run a line into the right-side buttons.
- Frame-0 claim card: two short lines that together match the spoken hook (example from the hooks bank: `VARIED CARPET BEETLES` / `TYPICALLY LAY 40 EGGS`). Card on at 0.00 s. Card `y` in queued bug specs is 470. Keep hedges on the card.
- Source tags go on the card or in the description, not in the voice.
- Exactly one comment trigger per script, phrased as a debate prompt: spoken in the loop line before the final "And," also the corner pill and the pinned comment. This replaces the old "one open comment question" rule. Packaging also allows closing the pin with "Full list in the Related video 👆" when a Related video is set.
- No spoken or visual outro (no Subscribe, Follow, or end card). Team research found that a spoken ending loses the last 3 seconds.
- YouTube: at most one mild word per test Short, never in the hook, only in the Meatball line if at all. TikTok short twins may be sweary; facts, credits, hedges, and safety stay clean. Caption-style / hashtag conflicts between Studio and MASTER_ORDERS are already flagged in `tiktok-caption-template.md` and are not resolved here.
- Safe-zone placement is in the checklist. Do not guess official pixel numbers. The house `search_top.y: 150` sits higher than TikTok's published In-Feed ad top reserve; test it on a phone before a TikTok twin ships (guideline).

---

## 4. Loop-ending technique

**Partly proven, partly house order.** Shorts that loop (>110% viewed, n=7) still plateaued at about 1,153 median views, so looping alone does not break the ~1K ceiling. It does help % viewed, and MASTER_ORDERS plus the Nov 16–29 test require it.

1. The last spoken beat still ends on the debate-prompt comment trigger and **And**, and "And" must run grammatically into line 1.
2. The last picture is the same close-up of the threat as frame 0, so the join is visual as well as verbal. A 0.08 s loop pad is the only extra silence the hooks bank allows, and only if the cut stays at or under 18.0 s.
3. Never end in a different room (the queued Christmas-tree cut ending in the kitchen is the example not to repeat).
4. Never say "subscribe" or otherwise signal an ending.

Every Short also speaks a long-form promise that points to the matching long-form. That spoken promise has to fit inside the 16.0–18.0 s budget. **Policy (Social Studio, 11/15 8:30 PM ET):** a 3–5 word promise inside the loop line, before "And," naming the creature or topic of the Short's Related-link long-form (from `/workspace/packaging/studio-related-links.csv`), so the hook, the safety condition, the debate prompt, and the loop join still fit.

---

## 5. YouTube Short template — 16–18 s (Nov 16–29 test)

**Proven length band (packaging plan, 86 Meatball Shorts):**

| Length | Shorts | Median views | Median % viewed |
|---|---:|---:|---:|
| ≤ 17 s | 20 | **1,187** | 90% |
| 18–21 s | 21 | 996 | 75% |
| ≥ 35 s | 5 | **285** | 48% |

The standing MASTER_ORDERS rule is 16–20 s, no Short under 15 s (`postkit.py lint` fails under 15.0 s or over 20.05 s). The test uses the **short end of that band: 16.0–18.0 s**. The plan update does not change length. Target in the hooks bank: 52–58 words → 16.04–17.89 s at 194.5 wpm, **before** the spoken long-form promise. The promise has to fit inside 16.0–18.0 s; placement is set by the 11/15 8:30 PM ruling (3–5 words in the loop line).

Template:

| Beat | Target time | What happens |
|---|---|---|
| 0. Hook | 0.00 s, card on; spoken hook under 12 words | Threat in close-up, claim card at 0.00 s, voice starts. Hook is you + your home + a number or threat. No Meatball. |
| 1. Gag | Meatball in ~2.3 s; line 2 in the 3–7 s window | One Meatball gag only. A new picture at least every 1–2 s; no gap over 2.0 s. |
| 2. Facts | After the gag, through ~12–14 s | At least two sourced facts. Hedges stay. Safety lines keep their condition. A new picture every 1–2 s. |
| 3. Loop | Last 3–6 s, ending at 16.0–18.0 s | Debate-prompt comment trigger, "And," picture back on the frame-0 close-up. The spoken long-form promise also has to live in this 16–18 s budget (3–5 words inside the loop line, per the 11/15 ruling). |

Cadence (house order, restated in the plan update): max 3 Shorts a day, at least 3 hours apart, house or spider topics only during the test. On a midweek long-form day the queue holds two Shorts, not three, so the long-form keeps its slot.

Dust mites (Mon 11/16 16:00 ET) keeps its queued cut unless Social Studio changes that. Carpet-beetle-window (Tue 11/17 16:00) and christmas-tree-bugs (Wed 11/18 19:00) should use the new 1-second hooks if Claude can fact-check and re-render at least 2 hours before the slot; otherwise the queued cut ships and is logged as a non-test post.

---

## 6. Standing rules (unchanged, still in force)

These were already house rules and are restated in the plan update:

- Sourced facts only. Do not invent numbers, study names, or hedges.
- Safety lines keep their condition. Do not leave a bare instruction or cut the "if / when / under" clause to save time.
- No team logos or betting.
- Titles name the creature or carry the series tag.
- Shorts stay at 3 a day, at least 3 hours apart.

---

## 7. TikTok Creator Rewards template — 65–90 s

**House order, not a length test we have run on this channel.** MASTER_ORDERS and the bible: sweary TikTok minute cuts run 65–92 s (this template uses the 65–90 s brief). Only videos over 1 minute pay in TikTok Creator Rewards (channel brief). No Duets, no Stitches. These are **original cuts**, not a stretched Short and not a recut of the YouTube file with the same edit.

Template (guideline structure, facts must still come from a checked pack):

| Beat | Target | What happens |
|---|---|---|
| 0. Hook | 0.00–2.5 s | Search phrase on screen (`search_top`). Threat in close-up. Claim card at 0.00 s. Hook is you + your home + a number or threat, under 12 words. |
| 1. Gag | ~3–7 s | Meatball gag with a prop or a card. Joke adds no fact. |
| 2. Facts | through ~60–80 s | Same sourced facts as the topic pack, with hedges and conditions, enough extra context to justify the minute length. About one swear a line on TikTok, after the clean fact, not inside it. A new picture every 1–2 s; no gap over 2.0 s. |
| 3. Loop | last line ends 65–90 s | Debate-prompt comment trigger, "And," return to the frame-0 close-up. Speak a long-form promise that points to the matching long-form. No Follow end card. |

Do not ship a TikTok under 60 s and call it a Creator Rewards cut. The 16–18 s YouTube Short and the minute cut are different files.

---

## 8. Long-form-to-Shorts cutdown template

**House plan, not yet measured as a traffic source.** Meatball long-forms got 0 of 655 views from the Shorts feed in the Windsor window through 11/09; views came from related videos, subscribers, and search. The Related-video bridge is newly locked and is not yet applied channel-wide. Bug and spider long-forms are now approved in the plan update; news, CIA, and pets are paused.

For each finished long-form, cut **2–3 Shorts**:

1. **Prefer Studio "Create Short"** from the finished long-form when the picture and sound can stand as a 16–18 s loop. That sets the source video as Related video automatically (packaging plan, citing the YouTube related-video guide).
2. If a clean loop cannot be cut from the master, render a same-creature 16–18 s trailer from the script, then set Related video to the long-form by hand (one video per Short, not a playlist).
3. Each Short teases **one** item or fact from the episode and does not give away a full ranking.
4. Frame 0 is the threat in close-up; hook is you + your home + a number or threat, under 12 words; claim card at 0.00 s; a new picture every 1–2 s (no gap over 2.0 s); one debate-prompt comment trigger; a spoken long-form promise that points to that long-form; loop back to frame 0; same caption style as the YouTube Short template. The promise is 3–5 words inside the loop line and names the Related-link long-form's creature or topic.
5. Reward the click in the long-form's first 5–10 seconds (YouTube's related-video guidance, cited in the packaging plan).
6. Pin the same debate prompt, and close with "Full list in the Related video 👆" when the link is set.
7. Do not use cub-killing or other excluded content in a lion cutdown. A lion cutdown EDL was optional and is not in this draft folder.

These Shorts still count toward the 3-a-day cap and must stay on-topic during the Nov 16–29 test.

---

## What this spec is not

- Not approval to post, schedule, or change Studio settings.
- Not a second-model fact-check, a render, or a transcript check. Those stay with Claude.
- Not a request to edit `TASKS.md` or to commit this file.
- Not a change to the renderer or to current renders. The illustrated-panel style is Jarvis's spec, still unhanded.
