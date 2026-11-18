# QA: House Bugs Ranked (flagship long-form #1), script `channels/scripts/longform-house-bugs-ranked.md`

Research & QA, Wed 11/18/2026, morning ET. One pass. Read first: `channels/team/playbooks/research-qa.md`, `channels/qa/checklist.md` (C1–C12 plus Y/T rows), MASTER_ORDERS (latest read-only copy, `skills/channel-brain/MASTER_ORDERS.md`). Script checked at main `9cdcb7c` (11/17 7:05 PM ET), against the renderer outline `skills/oh-meatball/scripts/longform-house-bugs-ranked-v3.outline.json` (`c1e742c`). Nothing was posted or messaged.

## Verdict: **FIX (text only, no re-render, no re-voice).** Every spoken fact PASSES.

- 116 spoken lines in the .md, plus 1 line that is only in the outline (117 voiced). I checked all 78 fact-tagged lines against our fact and QA files. Three were re-opened live this morning: Mayo, EPA asthma and MDC cellar spiders.
- Result: 78 PASS, 0 CUT, 0 spoken FIX.
- 3 FIXes (rows below):
  - 1 in the YouTube description, which goes out at 5 PM.
  - 2 doc-sync fixes in the .md, where the file lags the outline and render.
- 4 WATCH rows, none blocking.
- The v4 render (`channels/renders/flagship/house-bugs-ranked-v4.mp4`, frames sampled 2:30–3:45) already shows the fixed 3:00 visual: the COUNTY EXTENSION OFFICE desk and the doctor phone. So the render is ahead of the .md.
- **Note on the v5 file:** `channels/renders/flagship/house-bugs-ranked-v5.mp4` has **no video stream**. ffprobe shows a single pcm_s16le audio track lasting 442.8 s. Check that the scheduled upload is the muxed picture+voice file, not this one. [UNCERTAIN] It may simply be the voice stem saved with an .mp4 name.

## FIXes (exact)

| # | Where | Current | Fixed | Source / rule |
|---|---|---|---|---|
| F1 | Description, Sources list | (no MDC Cellar Spiders entry) | Add: `- Missouri Department of Conservation, Cellar Spiders field guide: https://mdc.mo.gov/discover-nature/field-guide/cellar-spiders` | C1. Line 2:18 "usually hangs belly-up" rests on MDC (live 11/18: "They usually hang belly-up."). Penn State HS7 says only "irregular mesh". The 11/17 night check asked for this addition, and it never reached the description. |
| F2 | .md line `3:00` visual + tag | *"Cut: a blurry phone photo; a big red NO; then a sharp photo going to an EXPERT ID box."* tag **[HS62]** | *"Meatball puts the spider in a jar and walks it to a COUNTY EXTENSION OFFICE desk; doctor icon for the bite line."* tag **[UC IPM Spiders]** | Sync to the outline/render (house-bugs-ranked-check.md row 3:00). UC IPM Spiders: "save it for identification … take it to your county UC Cooperative Extension office". UCR (HS62) does not support a photo-ID promise. |
| F3 | .md, after line `3:00` | (missing) | Add: `` `3:02` If a bite causes an unusual or severe reaction, call a doctor. **[UC IPM Spiders]** *Meatball holds up a phone, dials. Card stays.* `` | It is in the outline (and so in the voice) but not in the .md. UC IPM: "If you receive a bite that causes an unusual or severe reaction, contact a physician." C3: the condition is kept. |

## Line-by-line facts (all PASS; source quote location)

| Lines | Claim (short) | Verdict | Source |
|---|---|---|---|
| 0:24, 0:28 | Fossils 400 million years; "about twice as long ago as the dinosaurs" | PASS | P5-F1, MDC (silverfish-p5-1118.md). "About" is kept. |
| 0:32 | Move rapidly, including sideways; flat bodies, narrow crevices | PASS | P5-F7, Penn State, word for word |
| 0:40, 0:46 | Very weak jaws scrape paper instead of biting; "about paper, not people" | PASS | P5-F8, UC IPM. The hedge is kept, and there's no "never bite". |
| 0:50 | Do not transmit disease | PASS | P5-F2, MDC |
| 0:52, 0:58 | Invade new homes from wild areas, especially as they dry out in summer | PASS | P5-F10, UC IPM. "Can" and "especially" are kept. |
| 1:01, 1:07 | Can't climb slippery tub/sink sides; can't crawl up the drain | PASS | P5-F9, UC IPM |
| 1:10 | Dustlike scales around damaged books | PASS | P5-S4, UC IPM ("scales around or beneath damaged items … delicate, dustlike") |
| 1:18 | Damages paper, books, wallpaper | PASS | P5-F2, MDC damage list |
| 1:30 | Adults about 0.5 mm | PASS | DM1, UKY ef646 |
| 1:34, 1:38 | Primary food is skin flakes in house dust; most numerous in beds, overstuffed sofas and chairs | PASS | DM3, UKY |
| 1:45, 1:53 | Not capable of biting or stinging humans; allergens in mites, cast skins, droppings | PASS | DM8, UKY |
| 1:50 | Every home has dust mites | PASS | EPA, **live 11/18**: "Every home has dust mites." |
| 1:58 | "Wash bedding in hot water once a week, and dry it completely." Dial card AT LEAST 130°F | PASS (HOLD cleared) | EPA, **live 11/18**: "wash bedding in hot water once a week, and dry completely." Mayo, **live 11/18** (opened this run; the 11/17 night check got a 403): "Wash all sheets, blankets, pillowcases and bedcovers in hot water that is at least 130 F (54.4 C) to kill dust mites and remove allergens." |
| 2:03 | Hygrometer needle under 50 (visual only) | PASS (HOLD cleared) | Mayo, **live 11/18**: "Maintain a relative humidity below 50% in your home. … A tool called a hygrometer measures humidity levels." |
| 2:18 | Usually hangs belly-up in an irregular web | PASS (needs F1) | MDC, **live 11/18**: "They usually hang belly-up." Penn State HS7: "an irregular mesh of threads." |
| 2:21 | Jaws of most spiders too small to bite humans | PASS | HS2, UC IPM. "Most" is kept. |
| 2:29, 2:35, 2:39 | Bites only if squeezed, lain on, provoked; might bite when trapped in clothing or bedding; usually no worse than itching or a bee sting | PASS | HS4, UC IPM. Conditions kept. |
| 2:44, 2:49 | Garages, dark quiet protected spots; cellar spider not known to be in any way harmful | PASS | HS7, Penn State |
| 2:54 | Only a few, like black widows and brown recluses, have venom very toxic to humans | PASS | HS5, UKY ef622 |
| 3:00 (+ outline 3:02) | Save it, ask your county extension office; severe reaction, call a doctor | PASS (needs F2, F3 in .md) | UC IPM Spiders (see F2, F3) |
| 3:16 | About sixteen inches a second | PASS | P4-F1, Acosta 2003 (420 mm/s). "About" is kept. |
| 3:20 | Runs up walls to hunt | PASS | P4-F2, UKY ef645 |
| 3:23 | Unlike most centipedes, well-developed faceted eyes | PASS | P4-F4, UARK |
| 3:35, 3:45, 3:59 | Bites uncommon unless handled or pressed against skin; "I never touched it, so probably not"; "Don't grab it" | PASS | MSU (centipede-p4-1117.md). The condition is kept on all three. |
| 3:40 | Fangs so small that piercing human skin is difficult | PASS | UKY ef645 |
| 3:48, 3:54, 4:06, 4:13 | Feeds on bugs in the home, including cockroaches and silverfish | PASS | UKY ef645 |
| 3:56 | Half pouncing, half lassoing | PASS | P4-F3, UARK |
| 4:02 | Most infestations counted in single digits | PASS | P4-S2, MSU |
| 4:16 | Scatter when disturbed (story) | PASS | CR18, UC IPM |
| 4:20 | German: light brown, about 1/2 inch, two dark stripes | PASS | CR8, UKY ef614 |
| 4:25 | Adult Germans hide in a 1/16-inch crack | PASS | CR10, UC IPM. "Adult German" is kept. |
| 4:29, 5:10 | About 30 young per egg case | PASS | CR6, UC IPM (German). "About" is kept. The joke repeats the number and adds nothing (C4). |
| 4:34, 4:39 | Extremely heavy infestations, reported to bite | PASS | CR39, UF/IFAS. "Extremely heavy" and "have been reported" are kept, and 4:39 keeps the condition. |
| 4:43 | Droppings or body parts can trigger asthma | PASS | CR37, EPA |
| 4:46, 4:51 | Often brought in with infested grocery bags; even clean homes | PASS | CR11, UKY |
| 4:53–5:08 | Pesticides alone won't solve it; sanitation and exclusion; baits over sprays; avoid foggers, bombs, aerosol sprays, which can be hazardous; read the label | PASS | CR26, CR27 (UC IPM); CR29 (UKY) |
| 5:16 | Roaches feed on filth; the biter feeds solely on blood | PASS | BB13, UKY: "Unlike cockroaches and flies that feed on filth … the bugs feed solely on blood" |
| 5:37 | About 3/16 inch, reddish-brown, oval, flat | PASS | BB4, UKY. The apple seed is used for colour only. |
| 5:42 | No wider than a toothpick | PASS | BB7, UKY |
| 5:46 | Seams, box springs, bed frames, headboards | PASS | BB8, CDC |
| 5:54 | Bite people and animals at night while they sleep | PASS | BB17, CDC |
| 5:58 | Bite painless, seldom realize | PASS | BB19, UKY |
| 6:02 | Marks may take as long as 14 days in some people | PASS | BB18, CDC. All three hedges are kept. |
| 6:08 | Itching, loss of sleep; serious allergic reactions rare | PASS (WATCH W1) | BB20, CDC: "Bites can cause itching, loss of sleep, and, rarely, allergic reactions." |
| 6:12 | Not known to spread diseases | PASS | BB20 / BB33, CDC |
| 6:19 | Hitchhike on luggage, clothing, furniture | PASS | BB11, UKY |
| 6:24, 6:30 | Dryer on high heat 30 min; washing alone generally won't kill | PASS | BB21, EPA IPM |
| 6:33, 6:38 | Don't heat the home with thermostat, propane heater, fireplace; doesn't work and is dangerous | PASS | BB23, EPA DIY. Kept whole (C3). |
| 6:41 | Never use an outdoor pesticide indoors | PASS | BB29, EPA |
| 6:45 | Removal expensive and inconvenient | PASS | BB33, CDC |
| 6:49, 6:52 | If needed, hire a pro; pros can treat whole houses with heat | PASS | BB30, BB23, EPA. "If needed" is kept. |
| 7:24 | Regularly check mattress seams | PASS | BB33 + BB8, CDC ("regularly looking for signs") |

## Rules

| Row | Verdict | Note |
|---|---|---|
| Safety conditions (C3) | PASS | Silverfish "about paper"; spiders "squeezed, lain on…"; centipede "unless handled…" (with 3:45 tying back to it); roach "extremely heavy"; heat ban kept whole; "If needed" pro; doctor line conditioned on "unusual or severe reaction". No line says a tactic saved Meatball. |
| Peril template / Help 1311392 (Y2, Y3) | PASS, WATCH W2 | No animal is shown in exaggerated distress or peril. The bug bomb is never shown going off, no bug is killed on screen, and the bed-bug freak-out is Meatball's comedy. The six suspects each end differently (cleared, annoying ×4, gross, get out), driven by their own facts. That is a format inside one video, not the same situation with the same outcome. |
| Rule 7 ending (C2) | PASS / N/A | Not a survival verdict. The ending is "Case closed" plus the roof joke. No invented winner, and the ranking is labelled opinion (description: "The ranking is Meatball's opinion, not a finding"). |
| No swears: first 7 s, title, captions, on-screen text, description (C10, C11) | PASS | Zero swears anywhere in the script, cards, 3 titles, description, pin or thumbnail brief. |
| C1 facts sourced | FIX → F1 | Otherwise PASS. Mayo HOLD cleared live. |
| C4 jokes add no facts | PASS | 1:14, 2:07, 4:06, 5:10, 6:56, 7:13 add nothing new. 2:03 is a joke over a Mayo-sourced visual. |
| C5 logos/betting | PASS | Generic pro, no brands |
| C6 lane | PASS | Bug long-form against MO "Direction change". Moondog88's go is recorded via Social Studio in TASKS (11/17 6:40 PM ET "Moondog88 wants it out THIS week"; 11/17 10:35 PM ET Studio PASS v4; voice pick by Moondog88). |
| C7 title words | PASS | No banned words in any of the 3 titles. "Ranked" is not a competitor clone (`channels/research/faceless-outliers-1117.md`). |
| C8 pet claims | N/A | No cat/dog study claims |
| C9 funny first | WATCH W3 | 4:53–5:08 runs 5 fact lines (about 15 s) with visual gags only, no spoken joke. Studio passed the render, so no block. |
| C12 slurs/sexual | PASS | — |
| Y1 / Y4 / Y5 originality | PASS, WATCH W4 | Not a stitch: new narration and story arc. Original beats in every chapter. |
| Y6 hook/thumb | PASS | Thumb "GET OUT?" keeps the question mark, and the body pays it off (the centipede lands in ANNOYING). |
| Y7 AI persona advice | PASS | Advice is general pest guidance, with sources in the description; the heat line names the EPA there. No posing as a doctor; the doctor line refers out. |
| Y8 / Y9 | PASS | Drawn content, label on per MO. Nothing graphic. |

## WATCH (no block)

- **W1, 6:08:** "Serious allergic reactions are rare" is true under CDC but narrower than CDC's "rarely, allergic reactions". If any line is ever re-voiced, use: "Bites can cause itching, loss of sleep and, rarely, allergic reactions." (CDC, https://www.cdc.gov/bed-bugs/about/index.html)
- **W2, series level:** "NEW CASE EVERY WEDNESDAY" promises a repeatable frame. Case #2 must not reuse the same arc (2 AM bite → six rooms → bed bug wins → roof). Vary the mystery, the culprit and the close, per Help 1311392 "same situation … same outcome".
- **W3:** add one spoken Meatball gag in the 4:53–5:08 stretch in future cuts.
- **W4, fact reuse:** the silverfish chapter re-uses the P5 Short's headline fact (400 million years / twice the dinosaurs, the P5 Shorts cut Thu 7 PM). The centipede chapter re-uses P4's 16 in/s. That is allowed in a new long-form with new narration, but don't make these the thumbnail or title hook.

## Sources opened live this run (11/18/2026, morning ET)

- Mayo Clinic, Dust mite allergy, diagnosis and treatment (by Mayo Clinic Staff, Sept. 12, 2025): https://www.mayoclinic.org/diseases-conditions/dust-mites/diagnosis-treatment/drc-20352178
- EPA, Asthma Triggers: Gain Control (HTTP 200): https://www.epa.gov/asthma/asthma-triggers-gain-control
- MDC, Cellar Spiders (HTTP 200): https://mdc.mo.gov/discover-nature/field-guide/cellar-spiders
- All other quotes are from our files: `channels/qa/silverfish-p5-1118.md`, `channels/qa/centipede-p4-1117.md`, `channels/scripts/facts/{dust-mite-bornas,house-spiders-id,cockroach-bornas,bed-bugs}.md`, skills `oh-meatball/research/facts/{house-centipede-p4,house-bugs-ranked-check}.md` (read-only).
