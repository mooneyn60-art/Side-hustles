# Shorts edit checklist v1

Status: **draft only**, Sunday, Nov 15, 2026, 7:20 PM ET (America/New_York). Written to `/workspace/drafts/` for Social Studio to commit. No repo edit, no render, no schedule, no post, no channel-settings change. Claude re-renders; this file only grades and proposes trims.

Primary due: Monday, Nov 16, 2026, 4:45 PM ET.

Companion files: `shorts-edit-spec.md` (full templates), `shorts-edl-carpet-beetle-window.md`, `shorts-edl-christmas-tree-bugs.md`. Hook source: `/workspace/drafts/shorts-hooks-1s-1115.md` (same text as `channels/scripts/shorts-hooks-1s-1115.md`).

Runtime math used throughout: **194.5 wpm**, the house rate from the posted moose minute cut (289 words in 89.13 s on Andrew at +10%), as used in the hooks bank and current v6 script notes. A word is a token with letters or digits; contractions, hyphenated words, and numerals count as one. Where a script lists a `pad`, it is added after spoken time. **No queued mp4 or TTS file was on this box**, so render duration is not independently measured here. Packaging's bug-shorts lint pass also noted that `--mp4` was not run because the sparse clone excluded episode media.

Proven vs guideline is marked on each checklist item. See `shorts-edit-spec.md` for the fuller templates (16–18 s YouTube, 65–90 s TikTok Creator Rewards, long-form cutdowns).

---

## Checklist (use on every test Short)

### 1. Frame 0 is the hook visual, and it is the loop target

**Proven as a house order; first-second "chose to view" is the missing signal the packaging plan names, but we do not have stayed-to-watch per Short in the export.**

- [ ] First frame: the creature is already mid-action in the hook room. No logo, no establishing shot, no Meatball, no countdown.
- [ ] Last shot returns to that same room and the same mid-action creature, so the loop joins picture as well as words.
- Pass / Flag: ____

### 2. On-screen text in the first second

**Partly proven (best openers state the twist immediately; textbook lines in 0:04–0:06 dropped 15–24% in Studio AI reads). The 3–5-word card vs 6–8-word hedged hook is a resolved house compromise in the hooks bank, not a tested card length.**

- [ ] A claim card is on at 0.00 s and stays readable through the first second.
- [ ] The card matches the spoken hook in meaning, including hedges (`about`, `typically`, `can`, `may`, `up to`).
- [ ] No spoken study name, year, or sample size in the hook. Sources stay on the tag or in the description.
- Pass / Flag: ____

### 3. Cut pace — a visual change every 1–3 s

**Guideline.** Long-form review asked for a change every 2–4 s. This tighter Shorts cadence is a working rule, not a finding from our Shorts table.

- [ ] Every 1–3 s: a new scene, camera move, card, Meatball entrance, or creature action.
- [ ] Lines longer than 3 s (especially the loop line) have mid-line visual changes. A still must not hold past 3 s.
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
- [ ] The open question is spoken before "And," and is the same as the pill and the pinned comment.
- [ ] Last picture is the hook room, mid-action, matching frame 0. No end card, no Subscribe, no new room.
- [ ] At most ~0.08 s loop pad, and only if the cut is still ≤ 18.0 s.
- Pass / Flag: ____

### 6. Length check — 16–18 s for the Nov 16–29 test

**Proven band:** Shorts ≤17 s had median 1,187 views at 90% viewed (n=20); 35 s+ had median 285 (n=5). Standing lint window remains 15.0–20.05 s; the test uses 16.0–18.0 s.

- [ ] Spoken + listed pads + allowed 0.08 s loop pad land between 16.0 and 18.0 s at 194.5 wpm, then confirmed on the render (or a TTS file) before schedule.
- [ ] No extra silence from leftover queued pads.
- Pass / Flag: ____

---

## Grading: six test scripts in the 1-second hooks bank

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

## Trims (house and spider Shorts queued 11/16–11/20)

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
