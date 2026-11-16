# Shorts edit checklist v1

## Changelog, 11/15 8:30 PM ET

SPEC CHANGE ONLY. No renders, no pipeline changes, no commits. Matches the "Script and edit rules" in `plan-update-1115.md` (Moondog88's decisions, relayed through Jarvis and Social Studio). Existing grades were not re-run.

- Frame 0 item is now "the threat in close-up" (was: creature mid-action in the hook room). It is still the loop target.
- Hook checks: you + your home + a number or threat, and hook word count under 12; hedges stay where a fact needs one. The claim card stays on at 0.00 s.
- Pace item is now a new picture every 1–2 s, with no gap between picture changes over 2.0 s (replaces 1–3 s, and the 2–4 s long-form note).
- Comment item is now one comment trigger per script, phrased as a debate prompt (replaces one open comment question).
- New check: the Short speaks a long-form promise that points to the matching long-form, and that line has to fit inside the 16–18 s Nov 16–29 budget (length is unchanged). This is a tension to resolve, not a solved policy. A 3–5 word promise inside the loop line is a suggestion only, not a rule.
- New standing-rule checks: sourced facts; safety lines keep their condition; no team logos or betting; titles name the creature or carry the series tag; 3 Shorts a day, at least 3 h apart.
- Grading note added: the existing grades predate these rules; a count of which of the six hooks are 12 words or more, and which have no spoken long-form promise, is listed there from the actual hooks-bank text. Scripts were not re-graded.
- Animation style is noted in `shorts-edit-spec.md` only (illustrated panels plus the code-drawn rig; Jarvis owns it; current renders stay as they are). This checklist does not restyle or re-render anything.

Status: **draft only**, Sunday, Nov 15, 2026, 7:20 PM ET (America/New_York). Written to `/workspace/drafts/` for Social Studio to commit. No repo edit, no render, no schedule, no post, no channel-settings change. Claude re-renders; this file only grades and proposes trims.

Primary due: Monday, Nov 16, 2026, 4:45 PM ET.

Companion files: `shorts-edit-spec.md` (full templates), `plan-update-1115.md` (script and edit rules, 11/15), `shorts-edl-carpet-beetle-window.md`, `shorts-edl-christmas-tree-bugs.md`. Hook source: `/workspace/drafts/shorts-hooks-1s-1115.md` (same text as `channels/scripts/shorts-hooks-1s-1115.md`).

Runtime math used throughout: **194.5 wpm**, the house rate from the posted moose minute cut (289 words in 89.13 s on Andrew at +10%), as used in the hooks bank and current v6 script notes. A word is a token with letters or digits; contractions, hyphenated words, and numerals count as one. Where a script lists a `pad`, it is added after spoken time. **No queued mp4 or TTS file was on this box**, so render duration is not independently measured here. Packaging's bug-shorts lint pass also noted that `--mp4` was not run because the sparse clone excluded episode media.

Proven vs guideline is marked on each checklist item. See `shorts-edit-spec.md` for the fuller templates (16–18 s YouTube, 65–90 s TikTok Creator Rewards, long-form cutdowns). Script and edit rules follow `plan-update-1115.md`.

---

## Checklist (use on every test Short)

### 1. Frame 0 shows the threat in close-up, and it is the loop target

**House order (plan update 11/15). First-second "chose to view" is still the missing signal the packaging plan names, but we do not have stayed-to-watch per Short in the export.**

- [ ] First frame: the threat is in close-up. No logo, no establishing shot, no Meatball, no countdown.
- [ ] Last shot returns to that same close-up of the threat, so the loop joins picture as well as words.
- Pass / Flag: ____

### 2. Hook and on-screen text in the first second

**House order (plan update 11/15) plus the existing first-second card rule.** Best openers state the twist immediately; textbook lines in 0:04–0:06 dropped 15–24% in Studio AI reads. The claim card stays on at 0.00 s. A hook under 12 words can still run past 1.00 s at 194.5 wpm; the card, not a faster read, carries the claim in the first second.

- [ ] Spoken hook is you + your home + a number or threat.
- [ ] Hook word count is under 12 (a word is a token with letters or digits; contractions, hyphenated words, and numerals count as one).
- [ ] Hedges stay where a fact needs one (`about`, `typically`, `can`, `may`, `up to`), in the voice and on the card.
- [ ] A claim card is on at 0.00 s and stays readable through the first second.
- [ ] The card matches the spoken hook in meaning, including those hedges.
- [ ] No spoken study name, year, or sample size in the hook. Sources stay on the tag or in the description.
- Pass / Flag: ____

### 3. Cut pace — a new picture every 1–2 s

**House order (plan update 11/15).** This replaces the old 1–3 s Shorts cadence and the 2–4 s long-form note. It is not a finding from our Shorts table.

- [ ] A new picture every 1–2 s: a new scene, camera move, card, Meatball entrance, or creature action.
- [ ] No gap between picture changes over 2.0 s.
- [ ] Lines longer than 2.0 s (especially the loop line) have mid-line visual changes. A still must not hold past 2.0 s.
- Pass / Flag: ____

### 4. Caption safe zones (YouTube Shorts and TikTok)

**Official organic pixel safe zones do not exist. Do not treat any pixel box as YouTube's or TikTok's organic rule.**

What official pages do say, checked Nov 15, 2026:

- YouTube Help, "Get started creating YouTube Shorts" and "Upload YouTube Shorts": a Short is square or vertical, up to 3 minutes, maximum upload resolution 1080p. Those pages do **not** publish a text or logo safe area, or any margin in pixels. https://support.google.com/youtube/answer/10059070 https://support.google.com/youtube/answer/12779649
- Google Ads Help, "Use square and vertical video to engage mobile customers": for **vertical video ads** (which may appear in-stream, in-feed, and on Shorts), overlays, CTAs, and buttons "may appear in different places depending on the format, campaign type, and screen." The page points to a red safe-area **image** and, in the related "About video ad specs" article, to downloadable transparent PNG templates. The help text does **not** print pixel margins. This is ad guidance, not organic Shorts guidance. https://support.google.com/google-ads/answer/9128498 https://support.google.com/google-ads/answer/13547298
- TikTok publishes downloadable **In-Feed ads** safe-zone overlays. TikTok's own help text (as reported by later write-ups of that template) says the zone depends on the video's size and the caption length, and the page itself does not print a single pixel box. A guessed ads.tiktok.com help URL returned 404 from this box, so this draft does not invent an official URL or official pixel numbers. Third-party measurements of TikTok's official In-Feed overlay, scaled to 1080×1920, are commonly reported as about 240 px clear at the top, 660 px at the bottom, 120 px on each side, with a wider right (LTR) or left (RTL) margin for the button column from about y=840 down. **Those pixels are unofficial measurements, not a TikTok organic-post rule.** Use them only as a conservative starting box, then check the cut in the actual app.

House working placement (pipeline, not official):

- Frame 1080×1920, 9:16.
- Hook/fact cards: queued bug specs use `card.y: 470` (upper-middle). Keep cards clear of the very top UI and of the right-side button column.
- Burned-in captions: `captions: 66`, `caption_y: 1180`, centered, short lines. On a 1080×1920 frame, a 66 px caption whose top is at 1180 extends to about 1246, which is above a 1260 bottom edge in those unofficial TikTok In-Feed measurements — but only if `caption_y` is the top of the block, which the renderer should confirm on a still.
- Do not place the comment pill or a card with `"x": "right"` against the right edge (the queued Christmas-tree "EVER FIND ONE? COMMENT" card at `x: right`, `y: 400` is the pattern to avoid).
- TikTok `search_top.y: 150` in current tts drafts sits inside the unofficial 240 px top reserve. Flag and preview on a phone before a TikTok twin ships.
- After render, watch the cut once in the YouTube Shorts player and once in the TikTok player (or an equivalent overlay), including with the description expanded if the app does that.

- [ ] Hook card and first-second claim are clear of top UI and of the right-side buttons.
- [ ] Captions and the comment pill are centered (or left-of-center), not in the bottom metadata band and not in the button column.
- [ ] Placement was checked on a device preview, not only on the timeline.
- Pass / Flag: ____

### 5. Seamless loop join back to frame 0

**House order. Looping improves % viewed in our table but did not break the ~1K view ceiling (n=7 at >110% viewed, median 1,153).**

- [ ] Last spoken word is "And," and it runs grammatically into line 1.
- [ ] Exactly one comment trigger, phrased as a debate prompt, is spoken before "And," and is the same as the pill and the pinned comment. (This replaces the old "one open comment question" rule.)
- [ ] Last picture is the same close-up of the threat as frame 0. No end card, no Subscribe, no new room.
- [ ] At most ~0.08 s loop pad, and only if the cut is still ≤ 18.0 s.
- Pass / Flag: ____

### 6. Length check — 16–18 s for the Nov 16–29 test

**Proven band:** Shorts ≤17 s had median 1,187 views at 90% viewed (n=20); 35 s+ had median 285 (n=5). Standing lint window remains 15.0–20.05 s; the test uses 16.0–18.0 s. The plan update does not change length.

- [ ] Spoken + listed pads + allowed 0.08 s loop pad land between 16.0 and 18.0 s at 194.5 wpm, then confirmed on the render (or a TTS file) before schedule.
- [ ] The spoken long-form promise fits inside that 16.0–18.0 s budget. This is a tension to resolve, not a solved policy: do not add runtime past 18.0 s to make room, and do not treat a placement as locked. One suggestion, not a rule, is a 3–5 word promise inside the loop line.
- [ ] No extra silence from leftover queued pads.
- Pass / Flag: ____

### 7. Spoken long-form promise

**House order (plan update 11/15).** Every Short speaks a long-form promise that points to the matching long-form. Where that line sits is not locked (see item 6).

- [ ] The voice speaks a long-form promise, and it points to the matching long-form (not a generic "watch more").
- [ ] That line is inside the same 16.0–18.0 s cut as the rest of the Short.
- Pass / Flag: ____

### 8. Standing rules (unchanged, still in force)

**House orders, restated in the plan update.**

- [ ] Every spoken fact is sourced. No invented numbers, study names, or hedges.
- [ ] Every safety line keeps its condition (do not leave a bare instruction or cut the "if / when / under" clause).
- [ ] No team logos or betting appear in the picture, the captions, or the title.
- [ ] The title names the creature or carries the series tag.
- [ ] Cadence: at most 3 Shorts that day, and this slot is at least 3 hours from the others.
- Pass / Flag: ____

---

## Grading: six test scripts in the 1-second hooks bank

**These grades predate the 11/15 8:30 PM ET script and edit rules** (frame-0 close-up of the threat; hook is you + your home + a number or threat, under 12 words; a new picture every 1–2 s; one debate-prompt comment trigger; a spoken long-form promise inside 16–18 s). They were not re-run against those rules. The table and the "what will not edit to spec" list below are left as written.

Counted from the actual spoken text in `/workspace/drafts/shorts-hooks-1s-1115.md`, including the §4 clothes-moth refit. A word is a token with letters or digits; contractions, hyphenated words, and numerals count as one.

**Hooks 12 words or more:** none of the six current hooks-bank scripts.

- `dust-mites` — 7 words: "Female dust mites lay about 50 eggs."
- `carpet-beetle-window` — 7 words: "Varied carpet beetles typically lay 40 eggs."
- `christmas-tree-bugs` — 8 words: "Christmas trees can hide about 100 mantis eggs."
- `pantry-vs-clothes-moth` — 7 words: "Adult clothes moths never eat. Babies do."
- `cluster-flies` — 7 words: "Cluster flies can wake in your walls."
- `booklice-cupboard` — 6 words: "Booklice eat mold in your cupboards."

The pre-refit clothes-moth hook still quoted in the older grade notes below, "The moth in your closet never eats. Its babies eat your sweaters.", is 12 words. The current §4 hook is the 7-word line above.

**No spoken long-form promise:** all six. None of the spoken scripts points to a matching long-form.

Scripts graded: the six full Shorts in `/workspace/drafts/shorts-hooks-1s-1115.md` (dust mites 11/16, carpet beetle 11/17, Christmas-tree bugs 11/18, clothes moth and cluster flies 11/19, booklice 11/20). These are draft rewrites, status "re-render needed, Claude's call after fact-check." Dust mites is expected to ship as queued unless Social Studio changes that; it is still graded here as written in the hooks bank.

Runtimes below are the hooks bank's own spoken-word math at 194.5 wpm (rechecked on this pass). They are not mp4 durations.

Legend: **P** = pass as written, if the EDL/render follows the script's frame and loop notes. **F** = flag — will not edit to spec unless the fix in the list below is applied.

| # | Slot (ET) | Slug | Words | Est. runtime (194.5 wpm) | Frame 0 = loop target | Text in first 1 s | Pace 1–3 s | Safe zones (as scripted) | Loop join | Length 16–18 s |
|---|---|---|---:|---:|---|---|---|---|---|---|
| 1 | Mon 11/16 16:00 | `dust-mites` | 56 | 17.28 s | P | F | F | F | P | P |
| 2 | Tue 11/17 16:00 | `carpet-beetle-window` | 54 | 16.66 s | P | F | F | F | P | P |
| 3 | Wed 11/18 19:00 | `christmas-tree-bugs` | 56 | 17.28 s | P (if last shot stays on the twig) | F | F | F | P (if last shot stays on the twig) | P |
| 4 | Thu 11/19 16:00 | `pantry-vs-clothes-moth` | 55 | 16.97 s | P | F | F | F | P | P |
| 5 | Thu 11/19 19:00 | `cluster-flies` | 56 | 17.28 s | P | F | F | F | P | P |
| 6 | Fri 11/20 16:00 | `booklice-cupboard` | 54 | 16.66 s | P | P (spoken payoff in 1 s) / F (safe zone still to place) | F | F | P | P |

Frame 0 / loop is a **pass on the page** for all six: each script names the hook room and tells the editor to return there. It is still a render risk, especially Christmas-tree bugs, because the queued cut ended in the kitchen.

Safe-zone column is flagged for all six because the hooks bank specifies cards and a corner pill but not a tested placement, and official organic pixels do not exist. Use the working box in item 4, then preview.

### What will not edit to spec, and the fix

1. **Spoken hook does not finish inside 1.00 s (scripts 1–5).** At 194.5 wpm, only the first three words are fully spoken by 1.00 s. Payoffs land later: "50 eggs" ~2.16 s; "typically lay 40 eggs" ~2.16 s; "about 100 mantis eggs" ~2.47 s; clothes-moth hook is 12 words / 3.70 s (the hooks bank itself says "never eats" is about 1.3 s and the full line about 3.7 s; constant-rate math puts "never eats" at 1.85–2.16 s); "wake in your walls" starts around 1 s. **Fix:** keep the written hooks. Put the full claim on the frame-0 card at 0.00 s so the first second carries the payoff visually. Do not speed Andrew past +10% / +3Hz. Booklice is the exception: "Booklice eat mold" is fully spoken by about 0.93 s.

2. **Clothes-moth hook overruns the 1–3 s visual-change window by itself (3.70 s) and overruns a 1-second spoken hook.** **Fix:** at about 1.8–2.2 s, change the picture from the adult moth to the larvae / sweater (the "babies eat your sweaters" half) without leaving the closet, which is the hook room. Keep Packaging's chosen wording.

3. **Several spoken lines run longer than 3 s, so a one-card-per-line edit will fail the pace rule.** Lines over 3 s: dust-mites L3 (3.08 s) and L6 (5.24 s); carpet-beetle L2 (4.32 s) and L5 (5.24 s); Christmas-tree L4 (9.87 s); clothes-moth L1 (3.70 s), L5 (4.01 s), L6 (3.08 s); cluster-flies L2 (3.70 s), L3 (3.39 s), L6 (4.01 s); booklice L2 (3.70 s) and L6 (3.39 s). **Fix:** add mid-line visual changes (camera, Meatball hop, new card, creature action). Do not cut hedges, safety conditions, or the loop question to chase pace. The Christmas-tree last line must be broken into on-twig beats (find case / clip / tuck) and then **return to the foamy case on the swaying twig** for the question and "And." Do not end in the kitchen or stay on an outdoor evergreen.

4. **Corner pill and TikTok search card can hit UI.** **Fix:** center the pill; do not use `x: right`. Keep hook cards around the current `y: 470`. Keep captions at the house `caption_y: 1180` only after a still confirms the block is clear of the bottom metadata. For any TikTok twin, preview `search_top.y: 150` or move it down. No official pixel number to lock.

5. **Queued leftover pads, second gags, and old last lines will push a re-render off-spec if they are copied forward.** Christmas-tree queued pads total 2.4 s (about 19.98 s with the old 57-word script). Pantry queued pads total 1.2 s. Extra gags ("sweater is now a damn vest," "Merry damn Christmas," "Meatball eats for both," "Meatball, every Monday," "Meatball calls it a water feature," "Longer than Meatball's diets") were already cut in the hooks bank for time. **Fix:** build from the hooks bank, not from the queued JSON, except dust mites if it ships as queued (see Trims). New cuts may use a 0.08 s loop pad only.

6. **Fact-check still required before any of these is a test post.** The hooks bank lists the source lines (UKY ENTFACT-646; UC IPM 7436; Missouri / Penn State / Illinois Extension; UKY ENTFACT-609 and UC IPM 7435 / pantry pests; Penn State and CSU cluster flies; Clemson HGIC and Utah State booklice). Flags already in that file stand: varied vs other carpet-beetle egg counts; Missouri "about 100" vs Illinois 200–400; cluster-fly "thousands" is not a wall-population count; "inside earthworms" is not in the pack; booklice "1-millimeter" is a conversion, not Clemson's "about 1/25 inch"; humidity must stay a condition, not a cure. **Fix:** Claude's second-model check, then render, then a transcript check. Nothing here is approved to post.

7. **Dust mites may not use this rewrite.** Social Studio: if the fact-check and re-render are not ready at least 2 hours before the slot, the Short ships as queued and is logged as a non-test post; dust mites will likely ship as queued. The queued cut is a different length and loop (see Trims).

---

## Trims (measured, 11/15 7:30 PM ET)

Source for the six YouTube house Shorts queued 11/16 16:00–11/20 16:00 ET: ffprobe `format.duration` on the Metricool mp4s linked from `data/post-ids.csv` lines 25–30, saved under `/workspace/scratch/queued-renders/`. Times match `/workspace/research/2026-11-16-queued-shorts-lengths.csv` exactly (19.133, 18.233, 19.500, 18.233, 20.000, 19.767 s). Video is 1080×1920 h264 30 fps; audio is AAC 48 kHz mono. The earlier spoken+pad Trims section is kept below and marked superseded. Claude re-renders; do not render from this checklist. Nothing here is approved to post or schedule.

Social Studio rulings for this pass: the claim card is on at 0.00 s; Shorts under 16 s no longer "ship as they are" for these six (all are over 18 s); `dust-mites` keeps the queued file unless a trim is safe; `carpet-beetle-window` and `christmas-tree-bugs` switch to the new-hook EDLs; `pantry-vs-clothes-moth` uses the Scriptwriter refit in `shorts-hooks-1s-1115.md` §4 (the queued 18.233 s file is the old script). Hook, loop back to frame 0, and every safety line with its condition must survive. A trim that would hurt the Short is marked **ship as is, off-spec** with the reason.

### Why spoken+pad math undercounted

There is no separate title-stamp intro and no end card after the voice on these six files. Frame 0 already shows the creature and the first caption (`YOUR BED'S`, `YOUR WINDOW BUG`, `YOUR CHRISTMAS`, `YOUR CLOSET`, `THOUSANDS OF`, `1-MILLIMETER`). The last frame still shows the last spoken word (`BECAUSE`, `AND`, `RIGHT NOW`, `50 PERCENT OR`) plus the comment pill. `ffmpeg silencedetect` at −35 dB found no silent spans because the music bed fills the gaps.

`tools/drawn.py` `plan()` sets each beat to `dur = speech + b.get("pad", 0.08)` after `trim_air` (keeps 0.01 s lead and 0.03 s tail). `LOOP_LAND` (0.6 s) and `recut` only move the camera inside that duration; `ffmpeg -shortest` and loudnorm do not add a measured intro or tail card. The 1.6–4.6 s gap versus 194.5 wpm math is therefore:

- **Actual Andrew TTS**, including period pauses inside a beat (word-count math ignores them). Queued rates are not uniform: `dust-mites-v6-yt.json` is `rate: +0%`; `carpet-beetle-window` is `+8%`; the other four are `+10%`. The 194.5 wpm house rate was taken from the moose minute cut on Andrew at **+10%**.
- **Default `pad` 0.08 s on every beat that omits the key**, not only the last-beat 0.08 that the superseded math counted.
- **Explicit pads** where the JSON sets them: christmas-tree beats 2–5 `pad: 0.5` and beat 6 `pad: 0.4` (2.4 s listed); pantry beats 2–5 `pad: 0.3` (1.2 s listed). Caption holds with no new words match those pads (for example christmas-tree has no caption at 6.00 s and 12.20 s, just before the next scene cut).
- Inter-beat remaining air after `trim_air` ran larger than 0.08 s on the files we could word-align (dust-mites gaps about 0.21–0.42 s).

On the two +10% files that already had large listed pads, spoken+pad math was close: pantry 16.66 + 1.2 + 0.16 default ≈ 18.02 vs measured 18.233 (0.21 s over); christmas 17.58 + 2.4 + 0.16 default ≈ 20.14 vs measured 19.500 (0.64 s under). Do not reuse the 3–4 s gaps from the +0% / +8% / no-explicit-pad files as a pipeline constant on a new render.

Hook cards in the queued JSON use `card.at: "45%"` of beat 1 (visible on the mp4s around 1.5 s, not at 0.00 s). A duration trim of a queued file does not move that card. Re-renders must set the claim card at 0.00 s.

Beat in/out times below are scene cuts (`ffmpeg` `select=gt(scene,0.18)`) confirmed against burned-in captions and, for dust-mites and cluster-flies, against a word-level transcript of the first-pass VO. Timecodes are seconds on the measured render.

### Summary

| Slot (ET) | Slug | Measured (ffprobe) | Cut | New length |
|---|---|---|---|---|
| Mon 11/16 16:00 | `dust-mites` | **19.133 s** | Queued file, drop beat 4 tag `12.54–13.74` | **17.933 s** |
| Mon 11/16 19:00 | `stinkbug-explainer` | unmeasured, no file | — | — |
| Tue 11/17 10:00 | `fungus-gnats` | unmeasured, no file | — | — |
| Tue 11/17 16:00 | `carpet-beetle-window` | **18.233 s** (old hook) | Re-render from the new-hook EDL | **16.74 s** est. (16.66 spoken + 0.08 loop pad) |
| Tue 11/17 19:00 | `earwig-hook` | unmeasured, no file | — | — |
| Wed 11/18 10:00 | `carpenter-ant-hook` | unmeasured, no file | — | — |
| Wed 11/18 19:00 | `christmas-tree-bugs` | **19.500 s** (old hook) | Re-render from the new-hook EDL | **17.36 s** est. (17.28 spoken + 0.08 loop pad) |
| Thu 11/19 10:00 | `housefly-hook` | unmeasured, no file | — | — |
| Thu 11/19 16:00 | `pantry-vs-clothes-moth` | **18.233 s** (old script) | Re-render from the §4 refit | **16.43 s** est. (16.35 spoken + 0.08 loop pad) |
| Thu 11/19 19:00 | `cluster-flies` | **20.000 s** | Queued file, drop both Meatball tags `5.76–7.20` and `11.28–12.46` | **17.38 s** |
| Fri 11/20 10:00 | `fruitfly-explainer` | unmeasured, no file | — | — |
| Fri 11/20 16:00 | `booklice-cupboard` | **19.767 s** | Queued file, drop beat 4 tag + post-pipes pause `12.933–14.967` | **17.733 s** |
| Fri 11/20 19:00 | `clothesmoth-explainer` | unmeasured, no file | — | — |
| Mon 11/16 10:00 | `dog-tail-wag` | unmeasured, no file | — | — |

Time every new mp4 with ffprobe before locking a slot. The three re-render estimates assume 194.5 wpm plus only the overhead listed in each row, with `pad: 0` on earlier beats so `drawn.py`'s default 0.08 does not stack. If those keys are omitted, add 0.08 s × number of beats instead (carpet 5 beats → 17.06 s; christmas depends on beat count, still under 18 s at typical 4–7 beats; pantry 6 beats → 16.83 s). Residual TTS vs word math on the two measured +10% padded files was under 0.7 s. Do not invent a larger constant.

### Per-Short measured trims

Beat ids are 1-based `beats[]` in the queued v6 JSON, with the beat's `m` key.

#### Mon 11/16 16:00 — `dust-mites` (queued; trim is safe)

Measured **19.133 s**. JSON: 6 beats, `rate: +0%`, `pad` omitted on beats 1–5 (default 0.08), beat 6 `pad: 0.08`. Scene cuts at 3.367, 6.533, 9.933, 14.133, 17.467 (plus mid-line recuts at 16.233 and 18.567). VO (word times):

- Beat 1 `hook` 0.000–3.367: "Your bed's female mites lay about 50 eggs." (VO 0.00–3.14)
- Beat 2 `fact` 3.367–6.533: "Meatball hasn't washed his damn sheets since March." (3.46–6.16)
- Beat 3 `xray` 6.533–9.933: "In ideal conditions, eggs are adults in about a month." (6.58–9.68; period pause 7.48–8.18)
- Beat 4 `tiny` 9.933–14.133: "Adults live about one to two months. Longer than Meatball's diets." (10.08–13.74; period pause 11.96–12.54; tag 12.54–13.74)
- Beat 5 `calm` 14.133–17.467: "Keep humidity under 50 percent, and mites struggle." (14.10–17.26) — **safety, keep the condition**
- Beat 6 (loop) 17.467–19.133: "Dry air matters, because" (17.52–18.82, then ~0.31 s hold)

**Cut:** drop the second sentence of beat 4 only. Render in/out **12.54–13.74** (1.20 s). JSON: delete ` Longer than Meatball's diets.` from `beats[4].say` (1-based beat 4, `m: tiny`). New length **17.933 s**. Hook, loop back to frame 0, and the humidity condition all stay. Do not cut beat 5 or beat 6.

Remaining off-spec if this trimmed queued file ships (do not "fix" them with a deeper cut): the claim card is still `card.at: "45%"` of beat 1, not 0.00 s; the last line is still "because" with no "And" and no spoken question. Moving the card to 0.00 s takes a re-render of the same script, not a duration trim.

#### Tue 11/17 16:00 — `carpet-beetle-window` (switch to the new-hook EDL)

Measured **18.233 s** (old hook). JSON: 5 beats, `rate: +8%`, default pads on beats 1–4, beat 5 `pad: 0.08`. Scene cuts at 2.167, 6.900, 12.367, 14.733. Captions: hook still on "EGGS" at 2.10; vest gag "MEATBALL'S" at 10.12, "A DAMN VEST" at 12.20; beat 4 "THEY LEAVE" at 12.36; loop "AND" at 17.90. A vest-gag only trim (10.12–12.367 = 2.247 s) would land at **15.986 s**, under the 16.0 s floor, so do not trim the queued file.

**Cut:** re-render from `/workspace/drafts/shorts-edl-carpet-beetle-window.md` (hooks-bank 54 words, 16.66 s at 194.5 wpm, no queued pads, claim card at 0.00 s, loop back to the sill with the question and "And"). **Assumed overhead:** 0.08 s last-beat / loop pad only, with `pad: 0` on earlier beats. New length **16.74 s** estimated. If every `pad` key is omitted, drawn.py adds 0.08 × 5 = 0.40 s → **17.06 s**. Time the new mp4. Do not reuse this file's 18.233 − 15.12 = 3.11 s gap; the EDL uses +10%, not the queued +8%.

#### Wed 11/18 19:00 — `christmas-tree-bugs` (switch to the new-hook EDL)

Measured **19.500 s** (old hook). JSON: 7 beats, `rate: +10%`, beats 2–5 `pad: 0.5`, beat 6 `pad: 0.4`, beats 1 and 7 default 0.08. Scene cuts at 2.667, 6.067, 8.633, 12.433, 14.667, 17.600. Captions: "SCREAMED" at 5.50, no caption at 6.00 (pad before 6.067); "CRAWL OUT" at 8.20, "WITH NO FOOD" at 8.63; "MERRY DAMN" at 10.92, "CHRISTMAS" at 11.50, no caption at 12.20 (pad before 12.433); "OUTSIDE" at 16.90; "CHECK EACH TWIG" at 17.60; "BECAUSE" at 19.20. Last shot is the kitchen, so the picture does not loop to frame 0. Pad-only surgery on this file would not restage that loop.

**Cut:** re-render from `/workspace/drafts/shorts-edl-christmas-tree-bugs.md` (56 words, 17.28 s at 194.5 wpm, no 2.4 s pads, clip-and-tuck condition kept, cannibalism line out, loop on the twig, card at 0.00 s). **Assumed overhead:** 0.08 s last-beat / loop pad only, with `pad: 0` on earlier beats. New length **17.36 s** estimated. If pad keys are omitted, add 0.08 s × N beats; at 4–7 beats that is 17.60–17.84 s, still under 18.0 s. Time the new mp4. The queued +10% file was 0.64 s *shorter* than spoken + listed pads, so do not add a 3–4 s fudge.

#### Thu 11/19 16:00 — `pantry-vs-clothes-moth` (Scriptwriter refit; queued file is the old script)

Measured **18.233 s** on the old 54-word script (hook "Your closet moths lay 40 to 50 eggs," beats 2–5 `pad: 0.3`). Captions: "TO 50 EGGS" at 2.80; "THE LARVAE DO" at 9.20; "MEATBALL EATS" at 10.00; "FOR BOTH" at 10.72; "PACKAGE OF" at 14.40; "AND" at 18.00. Do not trim this render.

**Cut:** re-render from the §4 refit in `shorts-hooks-1s-1115.md`: 53 words, **16.35 s** spoken, no pads, hook "Adult clothes moths never eat. Babies do.", loop "Check your wool. What's in your closet right now? And", card at 0.00 s. Six spoken lines. **Assumed overhead:** 0.08 s loop pad only, with `pad: 0` explicitly set on beats 1–5 (otherwise drawn.py adds 0.08 × 6 = 0.48 s). New length **16.43 s** estimated (16.83 s if the default pads are left to fire). Time the new mp4. The old +10% file was only 0.21 s over spoken + pads, which is why this estimate is not padded with the old 18.233 s gap.

#### Thu 11/19 19:00 — `cluster-flies` (queued trim)

Measured **20.000 s**. JSON: 6 beats, `rate: +10%`, no explicit pads (default 0.08 each). Scene cuts at 2.933, 7.600, 12.700, 14.233, 17.267 (plus a mid-line recut at 9.300). Captions / first-pass VO:

- Beat 1 `hook` 0.000–2.933: "Thousands of flies can sleep inside your walls." (VO 0.00–2.70; "WALLS" at 2.80)
- Beat 2 `chase` 2.933–7.600: "One warm day wakes them. They crawl out. Meatball needs three alarms." ("THEY CRAWL OUT" at 5.30; tag **5.76–7.20**, "THREE ALARMS" still up at 7.20)
- Beat 3 `scale` 7.600–12.700: "Flies crowd your sunny windows, dazed and sluggish. Meatball, every Monday." ("SLUGGISH" at 11.20; tag **11.28–12.46**, "EVERY MONDAY" at 12.46)
- Beat 4 `fact` 12.700–14.233: "They can't breed in your house." ("THEY CAN'T" at 12.70; "HOUSE" at 14.00) — **safety, keep**
- Beat 5 `tiny` 14.233–17.267: "Their babies grow inside earthworms, outdoors." ("THEIR BABIES" at 14.40; "OUTDOORS" still held at 16.50 and 17.20)
- Beat 6 `punch` 17.267–20.000: "They're just lost, not nesting. Right now," ("NOT NESTING" at 18.50; "RIGHT NOW" at 19.50) — **loop, keep**

**Cut:** drop both Meatball tags only. Render in/out **5.76–7.20** (1.44 s) and **11.28–12.46** (1.18 s). JSON: delete ` Meatball needs three alarms.` from beat 2 `m: chase` and ` Meatball, every Monday.` from beat 3 `m: scale`. Leave the 7.20–7.600 and 12.46–12.700 holds as pads into the next beat. New length **17.38 s**. Hook, "They can't breed in your house," and the "Right now," loop all stay. This trim does not change the "Thousands" hook or the earthworm wording; those are rewrite issues, already drafted at 56 words / 17.28 s spoken in the hooks bank. If Claude is cleared to swap to that script instead, use the same overhead rule as the EDLs (17.28 + 0.08 = 17.36 s estimated, with `pad: 0` on earlier beats) and time the new mp4.

#### Fri 11/20 16:00 — `booklice-cupboard` (queued trim)

Measured **19.767 s**. JSON: 6 beats, `rate: +10%`, default pads on beats 1–5, beat 6 `pad: 0.08`. Scene cuts at 2.933, 4.533, 7.767, 10.567, 12.933, 14.967, 17.167, and loop-land at 19.200. Captions:

- Beat 1 `hook` 0.000–2.933: "1-millimeter bugs are eating mold in your cupboards." ("CUPBOARDS" at 2.80)
- Beat 2 `fact` 2.933–7.767: "And flour, cereal, and dried fruit. Meatball's cereal expired years ago." (recut 4.533, "AND DRIED" at 4.50; "YEARS AGO" at 7.60)
- Beat 3 `tiny` 7.767–10.567: "They like 75 to 90 percent humidity." ("HUMIDITY" at 10.50) — **keep**
- Beat 4 `escalate` 10.567–14.967: "They gather around leaking, sweating pipes. Meatball calls it a water feature." ("SWEATING PIPES" still held at 12.50 and 12.93; tag starts "MEATBALL CALLS" at 13.30, "IT A WATER" at 14.20, "FEATURE" at 14.90)
- Beat 5 `calm` 14.967–17.167: "Dry air can wipe them out within weeks." ("WITHIN WEEKS" at 16.30 and 17.10) — **keep**
- Beat 6 (loop) 17.167–19.767: "Keep humidity under 50 percent, or" ("50 PERCENT OR" at 19.00 and at the last frame) — **safety condition + loop, keep**

**Cut:** drop the second sentence of beat 4 and the post-"pipes." hold that leads into it. Render in/out **12.933–14.967** (2.034 s), from the 12.933 recut (caption still `SWEATING PIPES`) to the beat 5 in-point. JSON: delete ` Meatball calls it a water feature.` from `beats[4].say` (`m: escalate`). New length **17.733 s**. Keep "They gather around leaking, sweating pipes." Keep all three humidity / dry-air lines, with the "under 50 percent" condition attached. Hook and the "or" loop stay.

A gag-only in-point at first "MEATBALL CALLS" caption (13.30–14.967 = 1.667 s) would leave **18.100 s**, still over 18.0 s, so that tighter cut is not enough. The cereal gag on beat 2 is not required if the 12.933–14.967 cut is used.

Remaining off-spec if this trimmed queued file ships: claim card still at 45% of beat 1; last line is still "or" with no "And" and no spoken question. Those are rewrite issues (hooks bank 54 words / 16.66 s spoken). Do not cut the humidity condition to chase them.

#### Unmeasured, no file (8 Shorts)

No Metricool mp4 was pulled for these, and this pass does not guess a runtime from JSON or a 3D header. Leave them as **unmeasured, no file** until a render is timed: `fungus-gnats` (Tue 11/17 10:00); `stinkbug-explainer` (Mon 11/16 19:00); `fruitfly-explainer` (Fri 11/20 10:00); `clothesmoth-explainer` (Fri 11/20 19:00); `earwig-hook` (Tue 11/17 19:00); `carpenter-ant-hook` (Wed 11/18 10:00); `housefly-hook` (Thu 11/19 10:00); `dog-tail-wag` (Mon 11/16 10:00).

---

## Trims (house and spider Shorts queued 11/16–11/20) — superseded, 11/15 spoken+pad math

**Superseded** by **Trims (measured, 11/15 7:30 PM ET)** above. Left in place as the spoken-word audit trail. Do not use these runtimes or the ship-as-is calls for the six measured files.


Trends reported that only 2 queued Shorts fit 16–18 s and that the rest run 18.2–20.0 s. **This draft could not find Trends' measurement table, and no queued mp4 or TTS duration field was on the box**, so the times below are not those 18.2–20.0 figures. They are spoken-word estimates at 194.5 wpm plus any `pad` in the v6 JSON, or the duration written in a 3D explainer source header. If a render is truly 18.2–20.0 s, start with the pad and joke cuts below (they are the only slack that does not touch the hook, the loop join, or a safety condition) and re-time the file. Do not invent new wording. Claude re-renders; do not render from this checklist.

Scope: every YouTube house or spider Short in `skills/oh-meatball/data/posted.csv` dated 11/16–11/20 ET. Pet Short `yt-dog-tail-wag-v6.mp4` (Mon 11/16 10:00) and the Christmas-tree long-form (Wed 11/18 17:00) are out of scope.

### Summary

| Slot (ET) | File / slug | Current runtime (source) | vs 16–18 s | Trim (one line) | New est. |
|---|---|---|---|---|---|
| Mon 11/16 16:00 | `yt-dust-mites-v6.mp4` | 15.12 s spoken + 0.08 s pad = **15.20 s** (hooks bank + `dust-mites-v6-yt.json`) | Under 16.0 floor | **Ship as is, off-spec** (too short to trim; dust mites keeps the queued cut) | 15.20 s |
| Mon 11/16 19:00 | `yt-stinkbug-explainer.mp4` | **~16.3 s** (header in `tools/sim3d/explainer/ep_stinkbug.js`) | In band | **Ship as is** if the render matches the header; no line-level JSON to trim | ~16.3 s |
| Tue 11/17 10:00 | `yt-fungus-gnats-v6.mp4` | 17.28 s spoken + **2.00 s pads** = **19.28 s** (`fungus-gnats-v6-yt.json`) | Over 18.0 | Drop the five 0.4 s pads on beats 2–6 | **17.28 s** |
| Tue 11/17 16:00 | `yt-carpet-beetle-window-v6.mp4` | 15.12 s spoken + 0.08 s pad = **15.20 s** (hooks bank + v6 JSON) | Under 16.0 floor | Preferred: re-render from the new hook script (16.66 s). Queued fallback: **ship as is, off-spec** (too short; trimming would hurt) | 16.66 s if rewritten; 15.20 s if queued |
| Tue 11/17 19:00 | `yt-earwig-hook.mp4` | Hook-test script not in the tree. Older `earwig-yt.json` is 83 words / 25.60 s and ends "Subscribe," which is not a safe proxy | Unknown | **Cannot trim from sources on hand** | — |
| Wed 11/18 10:00 | `yt-carpenter-ant-hook.mp4` | Hook-test script not in the tree. Older `carpenter-ant-yt.json` is 88 words / 27.15 s and ends "Subscribe," which is not a safe proxy | Unknown | **Cannot trim from sources on hand** | — |
| Wed 11/18 19:00 | `yt-christmas-tree-bugs-v6.mp4` | 17.58 s spoken + **2.4 s pads** ≈ **19.98 s** (hooks bank + v6 JSON) | Over 18.0 | Preferred: re-render from the new hook script (17.28 s, no 2.4 s pads). Queued fallback: drop all listed pads (2.4 s) | **17.28 s** rewritten; **17.58 s** queued minus pads |
| Thu 11/19 10:00 | `yt-housefly-hook.mp4` | Hook-test script not in the tree. `ep_housefly.js` is a different 3D cut (~19.6 s), not this file | Unknown | **Cannot trim from sources on hand** | — |
| Thu 11/19 16:00 | `yt-pantry-vs-clothes-moth-v6.mp4` | 16.66 s spoken + **1.2 s pads** = **17.86 s** (hooks bank + v6 JSON) | In band (close) | Preferred: re-render from the new hook script (16.97 s, no 1.2 s pads). If the queued render is over 18 s, drop the four 0.3 s pads first | **16.97 s** rewritten; **16.66 s** queued minus pads |
| Thu 11/19 19:00 | `yt-cluster-flies-v6.mp4` | 15.42 s spoken, **no pad** = **15.42 s** (hooks bank + v6 JSON) | Under 16.0 floor | Preferred: re-render from the new hook script (17.28 s). Queued fallback: **ship as is, off-spec** (too short; no pad to cut) | 17.28 s if rewritten; 15.42 s if queued |
| Fri 11/20 10:00 | `yt-fruitfly-explainer.mp4` | **~15.8 s** (header in `ep_fruitfly.js`) | Under 16.0 floor if the header is exact | **Ship as is, off-spec** if the render is under 16 s; do not invent lines to lengthen it from this checklist | ~15.8 s |
| Fri 11/20 16:00 | `yt-booklice-cupboard-v6.mp4` | 16.04 s spoken + 0.08 s pad = **16.12 s** (hooks bank + v6 JSON) | In band | Preferred: re-render from the new hook script (16.66 s). Queued cut already fits 16–18 s by this math; **no trim** unless the render is over 18 s (then cut the second gag only) | 16.66 s rewritten; 16.12 s queued |
| Fri 11/20 19:00 | `yt-clothesmoth-explainer.mp4` | **~15.8 s** (header in `ep_clothesmoth.js`) | Under 16.0 floor if the header is exact | **Ship as is, off-spec** if the render is under 16 s; do not invent lines to lengthen it from this checklist | ~15.8 s |

If Trends' 18.2–20.0 s figures were taken from renders, several rows that look "under" or "in band" on spoken-word math may still need a pad or joke cut after the file is timed. Time the mp4 (or TTS) before locking a slot.

### Per-Short trim notes

Beat ids below are the v6 `beats[]` index (1-based) and the beat's `m` key, which is the line id in this pipeline.

#### Mon 11/16 16:00 — `dust-mites` (queued; likely ships as queued)

Source: `/workspace/packaging/lint-specs/dust-mites-v6-yt.json` and the hooks bank's queued-cut note. 49 words, 15.12 s spoken, `beats[6].pad: 0.08`, **15.20 s**.

**Ship as is, off-spec.** Trimming would take it further under the 16.0 s test floor. Social Studio already said this slot keeps the queued version if a re-render is not ready. Known off-spec issues to log, not "fix" with a shorter cut: the last line is "Dry air matters, because" (no "And," no spoken question); spoken length is under 16.0 s; the humidity line is an instruction ("Keep humidity under 50 percent, and mites struggle."). If Claude is later cleared to use the hooks-bank rewrite instead, that script is already 17.28 s and does not need a trim.

Do not cut the humidity condition if anyone does touch this file. If a later measured render is somehow over 18 s, the only line that can come out without losing the hook, the loop room, or the humidity condition is the joke tag on beat 4 (`m: unspecified` / line 4): "Longer than Meatball's diets." (4 words, 1.23 s). That would leave 13.97 s spoken + 0.08 s pad = 14.05 s, which is worse for the 16 s floor — another reason to ship as is.

#### Mon 11/16 19:00 — `stinkbug-explainer`

Source: comment at the top of `/workspace/skills-readonly/skills/oh-meatball/tools/sim3d/explainer/ep_stinkbug.js`: "YouTube Short ~16.3 s, 9 lines, loops." No v6 beat list with line ids was in the lint-specs tree. **Ship as is** if the render is in 16–18 s. If a timed render is over 18 s, come back with the TTS/timeline file; this checklist will not guess which of the 9 lines to cut.

#### Tue 11/17 10:00 — `fungus-gnats-v6`

Source: `/workspace/skills-readonly/skills/oh-meatball/scripts/drawn-house/fungus-gnats-v6-yt.json`. 56 words, 17.28 s spoken. Pads: beat 2 `chase` 0.4 s, beat 3 `xray` 0.4 s, beat 4 `scale` 0.4 s, beat 5 `calm` 0.4 s, beat 6 `fact` 0.4 s. Total pads **2.00 s**. Current estimate **19.28 s**.

**Trim:** delete those five pads only. New estimate **17.28 s** (plus at most 0.08 s loop pad = 17.36 s).

Keep, with their conditions: beat 4 `scale`, "Let the soil dry. Larvae hate drying out."; beat 5 `calm`, "Put a potato slice down. Maggots crawl on."; beat 6 `fact`, "Yellow sticky traps can catch the adults." Do not cut beat 1 `hook` ("Your plant soil hides up to 200 eggs.") or beat 7 `punch` ("So water less, because") if that line is still the loop into frame 0. If a timed render is still over 18 s after the pads come out, cut only the joke tag at the end of beat 5: "Worst snack tray ever." (4 words, 1.23 s) → about 16.05 s spoken, still in band. Do not cut the potato-slice instruction in front of it.

#### Tue 11/17 16:00 — `carpet-beetle-window`

Queued source: `carpet-beetle-window-v6-yt.json`. 49 words, 15.12 s spoken, last-beat `pad: 0.08`, **15.20 s**.

**Preferred path (already ordered):** re-render from the hooks-bank script. That cut is 54 words, **16.66 s**, one gag, open question, loop back to the sill. EDL: `shorts-edl-carpet-beetle-window.md`.

**Queued fallback, if the new cut is not fact-checked and rendered at least 2 hours before the slot: ship as is, off-spec** (under the 16.0 s floor). Trimming the queued file would hurt it. Do not cut "Adults gather at windows, drawn to light. And" (beat 5, the loop). Do not cut "Larvae live up to 630 days" or turn "typically / can lay 40" into a claim about every carpet beetle.

#### Tue 11/17 19:00 — `earwig-hook` and Wed 11/18 10:00 — `carpenter-ant-hook` and Thu 11/19 10:00 — `housefly-hook`

These are `hook-test` rows in `posted.csv` (`yt-earwig-hook.mp4`, `yt-carpenter-ant-hook.mp4`, `yt-housefly-hook.mp4`). The hook-test scripts for those files were **not** in the Side-hustles tree, the lint-specs folder, or the skills-readonly drawn-house / sim3d folders. The older drawn-house scripts (`earwig-yt.json`, 83 words / 25.60 s; `carpenter-ant-yt.json`, 88 words / 27.15 s) end on a "Subscribe. Part …" tease, which the test forbids, so they must not be used as a trim sheet. `ep_housefly.js` is a 3D explainer (~19.6 s), a different file from `yt-housefly-hook.mp4`.

MASTER_ORDERS notes hook-test Shorts in the queue at 23.7 s and 26.1 s, and the hooks bank says hook-test slots in this window were not part of the 1-second-hook rewrite. **Cannot give a line-id trim without the hook-test script or a timed render.** Open question for Social Studio: point this editor at those scripts or at the mp4/TTS durations.

#### Wed 11/18 19:00 — `christmas-tree-bugs`

Queued source: `christmas-tree-bugs-v6-yt.json`. 57 words, 17.58 s spoken. Pads: beats 2–5 `0.5` s each, beat 6 `0.4` s, total **2.4 s**, about **19.98 s**. Last beat (`m: punch`) is in the kitchen: "Check each twig first, because."

**Preferred path:** re-render from the hooks-bank script, **17.28 s**, clip-and-tuck condition kept, cannibalism line moved to the description, loop on the twig. EDL: `shorts-edl-christmas-tree-bugs.md`.

**Queued fallback trim, if that rewrite cannot ship:** drop all five listed pads (2.4 s). New estimate **17.58 s**. Keep beat 6 `fact`: "Clip the twig and put it in an evergreen outside." Keep the condition (a foamy case on the twigs) in beat 5 "Look for a foamy case on the twigs." Do not cut beat 1. If the render is still over 18 s after the pads come out, cut only the joke tag "Merry damn Christmas." from beat 4 `xray` (3 words, 0.93 s; leaves the sourced "With no food, they eat each other" in the queued voice — the hooks bank still flags that line for the description if the rewrite is used). Then restage the last shot on the hook-room twig; do not leave it in the kitchen, even though that is a picture change, not a time cut.

#### Thu 11/19 16:00 — `pantry-vs-clothes-moth`

Queued source: `pantry-vs-clothes-moth-v6-yt.json`. 54 words, 16.66 s spoken. Pads: beats 2–5 `0.3` s each, total **1.2 s**, **17.86 s**. Already in band on this math.

**Preferred path:** re-render from the hooks-bank script, **16.97 s**. If the queued render is the one Trends timed at 18.2 s or more, drop the four 0.3 s pads first. New estimate **16.66 s**. If it is still over 18 s, cut only the second gag on beat 3: "Meatball eats for both." (4 words, 1.23 s), leaving "The adults don't eat. The larvae do." New spoken estimate about 15.43 s, which would fall under the 16.0 s floor — only do that if the measured render is still over 18 s after pads are gone, and confirm the timed length. Keep the hook and the last "And."

#### Thu 11/19 19:00 — `cluster-flies`

Queued source: `cluster-flies-v6-yt.json`. 50 words, 15.42 s spoken, no pad, **15.42 s**.

**Preferred path:** re-render from the hooks-bank script, **17.28 s** (does not hook on "Thousands," does not say "inside earthworms"). **Queued fallback: ship as is, off-spec** (under the 16.0 s floor; there is no pad to cut). Do not trim "They can't breed in your house." If a measured render is over 18 s, the only joke tag that can come out is "Meatball, every Monday." on beat 3 (3 words, 0.93 s). Do not "fix" the hook or the earthworm wording in a trim pass; that is a rewrite, already drafted.

#### Fri 11/20 10:00 — `fruitfly-explainer` and Fri 11/20 19:00 — `clothesmoth-explainer`

Source: headers in `ep_fruitfly.js` and `ep_clothesmoth.js`, both "~15.8 s, 8 lines, loops." No beat-id JSON in lint-specs. **Ship as is, off-spec** if the render is under 16.0 s. Do not invent lengthening lines here. If a timed render is over 18 s, come back with the timeline; this checklist will not guess an 8-line cut.

#### Fri 11/20 16:00 — `booklice-cupboard`

Queued source: `booklice-cupboard-v6-yt.json`. 52 words, 16.04 s spoken, last-beat `pad: 0.08`, **16.12 s**. In band on this math.

**Preferred path:** re-render from the hooks-bank script, **16.66 s**, booklice named in the hook, loop stays in the cupboard, humidity kept as a condition. Queued cut needs **no trim** unless a measured render is over 18 s. In that case cut only the second gag on beat 4: "Meatball calls it a water feature." (6 words, 1.85 s). Keep "They gather around leaking, sweating pipes." Keep the humidity condition; do not leave a bare "Keep humidity under 50 percent" as a cure. The queued last line, "Keep humidity under 50 percent, or," is already off the loop rule (no "And," no question); that is a rewrite issue, not a trim.

---

## What Claude needs to do next

- Second-model fact-check on any hooks-bank rewrite that will replace a queued file (carpet beetle and Christmas-tree bugs first; clothes moth, cluster flies, and booklice if they are also to be swapped).
- Re-render. Time the actual file. Do not trust spoken-word math alone if Trends already measured 18.2–20.0 s on a render.
- Transcript check against the approved script, including "And," hedges, and safety conditions.
- Device check of captions, cards, and the comment pill against the real Shorts and TikTok UI.
- Nothing in this folder is approved to post or schedule.

---

## Update, Sun 11/15/2026, 7:23 PM ET: clothes-moth refit (`pantry-vs-clothes-moth`, Thu 11/19 16:00 ET)

Scriptwriter refit §4 of `/workspace/drafts/shorts-hooks-1s-1115.md`. It's 53 words, 16.35 s at 194.5 wpm, with no pads, so it's in the 16–18 s band.

- **Hook:** "Adult clothes moths never eat. Babies do." It's 7 words, about 2.16 s. Flag 2 (the 3.70 s hook) is resolved. The frame-0 card carries the claim at 0.00 s (now the rule): CLOSET MOTH: NEVER EATS / ITS BABIES EAT YOUR SWEATERS.
- **Pace:** Line 2 ("Clothes moth larvae eat your wool sweaters, fur, and silk.") runs past 3 s. Meatball's hop-in at about 2.3 s gives the visual change. Add a second change (for example, a larvae close-up on the sweater) if line 2 runs past about 5.3 s.
- **Gag:** it moved to line 3 (5.2–6.8 s).
- **Loop:** it ends "...What's in your closet right now? And" and loops back to the hook in the same closet.
- **Owed:** Claude's fact check on lines 1, 2 and 5 (UKY ENTFACT-609; UC IPM 7435; UC IPM Pantry Pests), then re-render and transcript check. Nothing is approved to post.
