# Bear vs lion: who would win? (the animals)

Draft: Sunday, Nov 15, 2026 (America/New_York).  
Status: **not pushed**. Fact pack: `/workspace/drafts/facts/bears-vs-lions.md`.  
Specs: `/workspace/drafts/bears-vs-lions-v6-yt.json` (YouTube Short), `/workspace/drafts/tts-bears-vs-lions.json` (TikTok short twin), `/workspace/drafts/tt-bears-vs-lions.json` (TikTok minute cut, **rules-default**, Nolan 11/11), `/workspace/drafts/tt-bears-vs-lions-v2.json` (lighter 4–5-swear variant, kept until Moondog88 picks).  
Template / pair: YouTube + tts match the newest drawn-house pair (`bison-wms-v6-yt.json` + `tts-bison-wms.json`). The rules-default minute cut follows `tt-grizzly-wms.json` plus MASTER_ORDERS / Nolan 11/11 (about one swear per line, 6–9 sweary jokes). Social Studio's 4–5-swear note does not win until Moondog88 picks; that cut was renamed to `tt-bears-vs-lions-v2.json`.  
Timing context from `research/116-bears-vs-lions.md`: built ahead of Thanksgiving, Thursday, Nov 26, 2026. The 116 memo is a search-and-timing brief; measurements were opened on the live pages listed in the fact pack on 2026-11-15.

The title and first line say it is the animals. No NFL team names, logos, marks, #nfl, score pick or betting. Thanksgiving, November 26, 2026 is named once, as a date only, in the description and caption.

This is general information, not a predicted fight. Still needs a second-model check and a render/transcript pass before it can be scheduled.

---

## A. YouTube Short (mild words)

**Estimated runtime: 19.9 seconds** (16–20s target). 5 lines, 64 spoken words, plus 0.2s of listed pads. Pacing is calibrated to the posted moose minute cut (289 words in 89.13s ≈ 194.5 wpm on Andrew at +10%). One mild word: “damn,” in the line 2 gag.

Hook and last line share the garden so the final “And” loops into the first line. Frame 0 is the bear already in view (`open: animal`). Meatball hops in around 2.3s. Line 2, the group-photo gag, starts at 2.5s (inside the 3–7s window). Studio should show both a grizzly and a lion for that gag; the JSON includes an `other_creature` lion config, which is not a standard single-creature key.

| # | Time | Scene | Spoken line | Fact IDs |
|---|---|---|---|---|
| 1 | 0.0–2.5s | open / garden | Bear versus lion, who would win? The animals. | BL-R1 (animals hook; answer comes on line 5) |
| 2 | 2.5–5.1s | forest_floor | Meatball tried a group photo. Tiny damn camera. | (no fact; acted Meatball gag only) |
| 3 | 5.1–9.5s | tundra | The Smithsonian's National Zoo says a male African lion weighs 330 to 550 pounds. | BL-F1 |
| 4 | 9.5–15.3s | swamp | The Park Service at Katmai says most adult male brown bears typically weigh 600 to 900 pounds in mid-summer. | BL-F14 |
| 5 | 15.3–19.9s | garden | A big coastal brown bear would probably win on size. Nobody has tested it. And | BL-R1 |

**Mild word (1):** damn (line 2).  
**Sourced facts:** BL-F1 (Smithsonian male lion 330–550 lb), BL-F14 (Katmai most adult male brown bears typically 600–900 lb in mid-summer). Winner rule BL-R1 on line 5.

### Alternate first-3-second hooks (Short)

Both keep the searched question and “the animals.” Hook 1 is in the JSON.

1. **Draft hook (in the JSON):** “Bear versus lion, who would win? The animals.” (~2.5s). Leaves room for the gag to start at 2.5s.
2. **Species in the hook:** “Grizzly bear versus lion, who would win? The animals.” (~2.8s). Closer to one of the YouTube suggestions, but “grizzly” can be heard as the inland animal, and this cut’s “probably” is about a coastal brown bear. The draft hook stays generic and lets Katmai name the population later.
3. **Stake in the hook:** “Bear versus lion, who would win? The animals. A big coastal brown bear would probably win on size.” (~5.6s). Front-loads the verdict and delays the gag past the 3–7s window unless later lines are cut; also drops “nobody has tested it” from the hook unless the line runs even longer.

---

## A2. TikTok short twin (`tts-bears-vs-lions.json`)

Same facts, same five-beat shape, sweary reactions. **Estimated runtime: 21.5 seconds** (the bison/shark tts twins also run longer than their 16–20s YouTube cuts). 69 spoken words, plus 0.2s of pads. `search_top` shows **BEAR VERSUS LION / WHO WOULD WIN?** for 2.5s. Captions use `cap_swap`.

| # | Time | Scene | Spoken line | Fact IDs |
|---|---|---|---|---|
| 1 | 0.0–3.1s | open / garden | Bear versus lion, who would win? The animals. Holy shit. | BL-R1 (animals hook; answer comes on line 5) |
| 2 | 3.1–5.8s | forest_floor | Meatball tried a group photo. Tiny fucking camera. | (no fact; acted Meatball gag only) |
| 3 | 5.8–10.1s | tundra | The Smithsonian's National Zoo says a male African lion weighs 330 to 550 pounds. | BL-F1 |
| 4 | 10.1–15.9s | swamp | The Park Service at Katmai says most adult male brown bears typically weigh 600 to 900 pounds in mid-summer. | BL-F14 |
| 5 | 15.9–21.5s | garden | A big coastal brown bear would probably win on size. Nobody has tested it. Who would win? And | BL-R1 |

Swears: Holy shit (hook); tiny fucking camera (gag). Facts and the winner rule stay clean.

---

## B. TikTok minute cut, rules-default (`tt-bears-vs-lions.json`)

**Estimated runtime: 91.8 seconds** (65–92s sweary window; 65–90s is the usual target). 15 lines, 293 spoken words, plus 1.40s of listed pads (0.25s on the gag and the Noodle plant, 0.9s on the punch).

**This cut follows MASTER_ORDERS / Nolan 11/11:** about one swear per line; 6–9 sweary jokes. Facts, credits and the winner hedge are said clean, with the swear after. Same facts, structure, and Noodle plant/payoff as the lighter variant. The ending is non-survival: it drops “Meatball lived. Nothing's guaranteed.” and lands on “Nobody has tested it. Who would win, a bear or a lion? Fucking wild. And,” looping into the hook.

| # | Time | Scene | Spoken line | Fact IDs |
|---|---|---|---|---|
| 1 | 0.0–3.1s | open / garden | Bear versus lion, who would win? The animals. Holy shit. | BL-R1 (animals hook) |
| 2 | 3.1–5.8s | forest_floor | Meatball tried a group photo. Tiny fucking camera. | (no fact; acted Meatball gag only) |
| 3 | 5.8–10.4s | forest_floor | His dog, Noodle, sat this one out. Meatball waved him in. Bold as fuck. | (no fact; Noodle plant, action only) |
| 4 | 10.4–17.2s | tundra | The Smithsonian's National Zoo says a male African lion weighs 330 to 550 pounds. Meatball still held the camera. Tiny fucking arms. | BL-F1 |
| 5 | 17.2–23.0s | cave | A San Diego Zoo Wildlife Alliance fact sheet lists male lions at 331 to 496 pounds. No fucking prize. | BL-F3 |
| 6 | 23.0–30.7s | swamp | In the lower 48, the U.S. Fish and Wildlife Service says adult male grizzlies average 400 to 600 pounds. Those ranges overlap. Too fucking soon. | BL-F7, BL-R2 |
| 7 | 30.7–39.1s | tundra | Yellowstone's ecology page says male grizzlies weigh 200 to 700 pounds. Glacier, also Park Service, lists adult males at 300 to 440 pounds. One messy fucking chart. | BL-F8, BL-F11 |
| 8 | 39.1–48.3s | forest_floor | Bear speed is not one number. The Park Service says as fast as a racehorse, uphill and down. Yellowstone says up to 40 miles per hour. Glacier lists 35. Fuck. | BL-F12, BL-F8, BL-F11 |
| 9 | 48.3–56.3s | garden | The same fact sheet says lions have short bursts of 45 to 60 kilometers per hour, about 24 to 37 miles per hour. Worst fucking stopwatch. | BL-F5 |
| 10 | 56.3–66.8s | swamp | At Katmai, the Park Service says most adult male brown bears typically weigh 600 to 900 pounds in mid-summer. Large adult males can weigh well over 1,000 pounds by October and November. Holy shit. | BL-F14 |
| 11 | 66.8–71.8s | tundra | So a big coastal brown bear would probably win on size. Nobody has tested it. Fuck. | BL-R1 |
| 12 | 71.8–77.6s | cave | An inland grizzly is different. Those weights overlap a male lion's. Nobody has tested that either. No fucking trophy. | BL-R2 |
| 13 | 77.6–83.2s | forest_floor | Katmai says there have been no documented cases of a Yellowstone grizzly weighing over 900 pounds. Tough shit. | BL-F15 |
| 14 | 83.2–86.3s | garden | His dog, Noodle, already had the camera. Little fucking photographer. | (no fact; running gag / payoff only) |
| 15 | 86.3–91.8s | garden | Nobody has tested it. Who would win, a bear or a lion? Fucking wild. And | (untested hedge + loop; no tactic credited) |

On-screen for the first 2.5s: **BEAR VERSUS LION / WHO WOULD WIN?**

**Swears:** one per line (Holy shit; fucking; fuck; fucking; fucking; fucking; fucking; Fuck; fucking; Holy shit; Fuck; fucking; shit; fucking; Fucking).  
**Sweary jokes (9):** tiny fucking camera; bold as fuck; tiny fucking arms; no fucking prize; too fucking soon; one messy fucking chart; worst fucking stopwatch; no fucking trophy; little fucking photographer.  
**Bare reactions after clean facts or the hedge:** Holy shit; Fuck (after the speed disagreement); Holy shit (after Katmai weights); Fuck (after “Nobody has tested it”); Tough shit; Fucking wild.

### Alternate first-3-second hooks (rules-default minute)

1. **Draft hook (in the JSON):** “Bear versus lion, who would win? The animals. Holy shit.” (~3.1s). Gag starts after the hook.
2. **Answer-in-the-hook:** “Bear versus lion, who would win? The animals. A big coastal brown bear would probably win on size. Nobody has tested it.” (~6.8s). Stronger stake, but it delays the gag and spends the “probably” before the weights are heard.
3. **Species in the hook:** “Grizzly bear versus lion, who would win? The animals. Holy shit.” (~3.4s). Matches a YouTube suggestion, but risks hearing the inland animal as the one that “probably” wins. The draft hook stays generic on purpose.

---

## B2. TikTok minute cut, lighter variant (`tt-bears-vs-lions-v2.json`)

**Estimated runtime: 89.6 seconds.** 15 lines, 286 spoken words, plus 1.40s of listed pads. This is the cut that used Social Studio's 4–5-swear lead notes. It was renamed from `tt-bears-vs-lions.json` on 2026-11-15 and is kept until Moondog88 picks. It still has the old survival-style last line (“Meatball lived. Nothing's guaranteed.”), which does not fit a non-survival comparison as cleanly as the rules-default ending.

**This cut deliberately departs from MASTER_ORDERS / Nolan 11/11** (one swear per line, 6–9 sweary jokes per minute). 5 swears total; first 3s clean except one “Holy shit”; strongest jokes on lines 4, 6 and 9; Noodle planted on line 3 (`His dog, Noodle,` comma) with the camera payoff on line 14. Jokes add no number, danger, feeling, motive or safety instruction.

| # | Time | Scene | Spoken line | Fact IDs |
|---|---|---|---|---|
| 1 | 0.0–3.1s | open / garden | Bear versus lion, who would win? The animals. Holy shit. | BL-R1 (animals hook) |
| 2 | 3.1–5.5s | forest_floor | Meatball tried a group photo. Tiny camera. | (no fact; acted Meatball gag only) |
| 3 | 5.5–9.4s | forest_floor | His dog, Noodle, already sat this one out. Meatball waved him in. | (no fact; Noodle plant, action only) |
| 4 | 9.4–16.2s | tundra | The Smithsonian's National Zoo says a male African lion weighs 330 to 550 pounds. Meatball still held the camera. Tiny fucking arms. | BL-F1 |
| 5 | 16.2–21.2s | cave | A San Diego Zoo Wildlife Alliance fact sheet lists male lions at 331 to 496 pounds. | BL-F3 |
| 6 | 21.2–30.7s | swamp | In the lower 48 states, the U.S. Fish and Wildlife Service says adult male grizzlies average 400 to 600 pounds. Those ranges overlap. Meatball still wanted a winner. Too fucking soon. | BL-F7, BL-R2 |
| 7 | 30.7–38.1s | tundra | Yellowstone's ecology page says male grizzlies weigh 200 to 700 pounds. Glacier, another Park Service park, lists adult males at 300 to 440 pounds. | BL-F8, BL-F11 |
| 8 | 38.1–48.6s | forest_floor | Bear speed is not one number. The Park Service says bears can run as fast as a racehorse, uphill and down. Yellowstone's ecology page says up to 40 miles per hour. Glacier lists 35. | BL-F12, BL-F8, BL-F11 |
| 9 | 48.6–57.9s | garden | The same fact sheet says lions have short bursts up to 45 to 60 kilometers per hour, about 24 to 37 miles per hour. Meatball timed nothing. Worst fucking stopwatch. | BL-F5 |
| 10 | 57.9–67.7s | swamp | At Katmai, another Park Service park, most adult male brown bears typically weigh 600 to 900 pounds in mid-summer. Large adult males can weigh well over 1,000 pounds by October and November. | BL-F14 |
| 11 | 67.7–72.4s | tundra | So a big coastal brown bear would probably win on size. Nobody has tested it. | BL-R1 |
| 12 | 72.4–77.3s | cave | An inland grizzly is different. Those weights overlap a male lion's. Nobody has tested that either. | BL-R2 |
| 13 | 77.3–82.2s | forest_floor | Katmai says there have been no documented cases of a Yellowstone grizzly weighing over 900 pounds. | BL-F15 |
| 14 | 82.2–84.7s | garden | His dog, Noodle, already had the fucking camera. | (no fact; running gag / payoff only) |
| 15 | 84.7–89.6s | garden | Meatball lived. Nothing's guaranteed. Who would win, a bear or a lion? And | (no tactic credited; loops to the hook; survival-style close, kept on this lighter cut) |

On-screen for the first 2.5s: **BEAR VERSUS LION / WHO WOULD WIN?**

**Swears (5):** Holy shit (line 1, only swear in the first 3s); Tiny fucking arms (line 4); Too fucking soon (line 6); Worst fucking stopwatch (line 9); fucking camera (line 14 payoff).  
**Strongest jokes (lines 4, 6, 9):** tiny fucking arms; too fucking soon; worst fucking stopwatch.

### Alternate first-3-second hooks (lighter variant)

1. **Draft hook (in the JSON):** “Bear versus lion, who would win? The animals. Holy shit.” (~3.1s). First 3s are clean except this one reaction. Gag starts at 3.1s.
2. **Answer-in-the-hook:** “Bear versus lion, who would win? The animals. A big coastal brown bear would probably win on size. Nobody has tested it.” (~6.8s). Stronger stake, but it delays the gag and spends the “probably” before the weights are heard.
3. **Species in the hook:** “Grizzly bear versus lion, who would win? The animals. Holy shit.” (~3.4s). Matches a YouTube suggestion, but risks hearing the inland animal as the one that “probably” wins. The draft hook stays generic on purpose.

---

## Fact-check table

Pages opened 2026-11-15 (America/New_York). “Verified” means the live wording still supports the spoken line or card. Pack quotes used in these cuts are still on the pages unless a note says otherwise.

| Line (cut) | Claim in the cut | Source URL | Verified | Note |
|---|---|---|---|---|
| Short 3 / Minute 4 | A male African lion weighs 330 to 550 pounds (Smithsonian's National Zoo). | https://www.nationalzoo.si.edu/animals/lion | Yes | “They weigh from 330 to 550 pounds (150 to 250 kilograms).” The “they” follows the male-size sentence. WebFetch timed out; the sentence was read with curl, tags stripped, the same day. |
| Short 4 / Minute 10 | At Katmai, most adult male brown bears typically weigh 600 to 900 pounds in mid-summer. Large adult males can weigh well over 1,000 pounds by October and November. | https://www.nps.gov/katm/learn/photosmultimedia/brown-bear-frequently-asked-questions.htm | Yes | Word for word, FAQ 17. “Typically,” “most adult males,” mid-summer, and “large adult males” / “well over” in fall are all spoken or on the card. Page last updated October 29, 2024. Credit is “the Park Service at Katmai.” |
| Short 5 / Minute 11 | A big coastal brown bear would probably win on size. Nobody has tested it. | BL-R1, from the weight gap between BL-F14 and BL-F1 / BL-F3 | Yes (reason); n/a (the “probably” / untested hedge) | Even the highest male-lion figure opened (570 lb on a third zoo page, unused in speech) sits below Katmai’s typical mid-summer male range of 600–900. This is a size hedge, not a tested fight. |
| Minute 5 | A San Diego Zoo Wildlife Alliance fact sheet lists male lions at 331 to 496 pounds. | https://ielc.libguides.com/sdzg/factsheets/lions/summary | Yes | “Males: 150-225 kg (331-496 lbs).” Spoken so the Smithsonian range is not the only lion figure. |
| Minute 6 | In the lower 48 states, the U.S. Fish and Wildlife Service says adult male grizzlies average 400 to 600 pounds. Those ranges overlap. | https://www.fws.gov/species/grizzly-bear-ursus-arctos-horribilis | Yes | “Adult males average 400 to 600 pounds (200 to 300 kilograms) … in the 48 contiguous states.” “Average,” “adult male,” and “lower 48” are spoken. Overlap with the lion ranges is a comparison of the cited figures, not a new measurement. |
| Minute 7 | Yellowstone’s ecology page: male grizzlies weigh 200 to 700 pounds. Glacier lists adult males at 300 to 440 pounds. | https://www.nps.gov/yell/learn/nature/bear.htm and https://www.nps.gov/glac/learn/nature/bears.htm | Yes | Ecology page last updated April 18, 2025; Glacier last updated November 6, 2017. Other Yellowstone pages give an average of 413 lb and a range of 216–717 (BL-F9, BL-F10); those were left off the spoken line so one park does not appear to have one official number. |
| Minute 8 | Bear speed is not one number. Park Service: as fast as a racehorse, uphill and down. Yellowstone ecology: a grizzly can run up to 40 miles per hour. Glacier lists a top speed of 35. | https://www.nps.gov/subjects/bears/safety.htm ; https://www.nps.gov/yell/learn/nature/bear.htm ; https://www.nps.gov/glac/learn/nature/bears.htm | Yes | Racehorse sentence last updated September 8, 2025. “Up to 40 mph” is the ecology page, not the Safety page’s 40 feet per second. Glacier’s 35 is listed for grizzlies (and, on the same page, for black bears; the spoken line does not flatten that). |
| Minute 9 | Lions have short bursts up to 45 to 60 kilometers per hour, about 24 to 37 miles per hour. | https://ielc.libguides.com/sdzg/factsheets/lions/summary | Yes | “Bursts of speed up to 45-60 km/hr (24-37 mph) for short distances (100–200 m).” Both units are on the page. “Short bursts” carries the short-distance condition; 100–200 m is on the card. |
| Minute 12 | An inland grizzly is different. Those weights overlap a male lion’s. Nobody has tested that either. | BL-R2, from BL-F7 / F8 / F11 vs BL-F1 / F3 | Yes (overlap of the cited ranges) | Prevents the coastal “probably” from being heard as a generic grizzly win. |
| Minute 13 | Katmai says there have been no documented cases of a Yellowstone grizzly weighing over 900 pounds. | https://www.nps.gov/katm/learn/photosmultimedia/brown-bear-frequently-asked-questions.htm | Yes | FAQ 2, word for word. Credit is “Katmai says.” |
| Unused, verified | Yellowstone Safety: “Bears can run up to 40 feet (12 m) per second.” | https://www.nps.gov/yell/planyourvisit/safety.htm | Yes | **Not used in speech.** About 27.3 mph if converted; that mph is our arithmetic, not an agency figure. It is one reason the cut refuses a single bear speed. |
| Unused, verified | Yellowstone facts page: average male 413 lb, heaviest GYE male 715 lb; speed “35-40 mph.” | https://www.nps.gov/yell/learn/yellowstone-grizzly-bear-facts.htm | Yes | Last updated December 21, 2015. Left out of speech so Yellowstone is not given two spoken weight systems. |
| Unused, verified | San Diego Zoo public page: males 330 to 570 lb; “A lioness can sprint at up to 33 miles (53 kilometers) per hour.” | https://animals.sandiegozoo.org/animals/lion | Yes | Conflicts with the same institution’s fact sheet (BL-F3, BL-F5). Unused in speech; the cuts use the fact sheet for speed and cite both lion-weight pages that were spoken. |
| Unused, not found | Any bite-force figure | — | n/a | Not on the agency or zoo pages opened. Left out. |

No live-page mismatch required a change to a pack quote these cuts actually use. The conflicts that matter — lion max weight, bear speed, and inland vs coastal bear weight — are either spoken as disagreements or left unused on purpose.

---

## Rules these drafts could not fully satisfy

- **Second-model check before scheduling.** MASTER_ORDERS requires a different model to check every changed line against the live pages. These drafts opened those pages, but they are still the writer’s pass.
- **Exact runtime and the 2.3s Meatball hop.** Runtimes are word-count estimates. The hop-in is a renderer convention. No render, lint, or voicecheck was run.
- **Two animals on screen.** The drawn-house schema used in the bison/shark/grizzly specs is one `stage.creature`. The JSON includes `other_creature` / `other_creature_cfg` for a lion and a staging note for the group-photo gag. Studio still has to make that work; an unknown key could be ignored by the renderer.
- **Noodle acted shot** (minute cut) has no character key in the existing schema. Line 3 is written as an acted shot; Studio has to draw it.
- **Two minute cuts, pending Moondog88's pick.** The rules-default (`tt-bears-vs-lions.json`) now follows Nolan 11/11 (one swear per line, 6–9 jokes) and uses a non-survival ending. The lighter 4–5-swear cut was renamed to `tt-bears-vs-lions-v2.json` and still ends with “Meatball lived. Nothing's guaranteed.” The TikTok short twin is closer to the usual short-cut swearing (two swears in five lines) and may run a little longer than 20s, like `tts-bison-wms.json`.
- **Smithsonian page access.** WebFetch timed out; the Size paragraph was verified with curl the same day. A second model should open the page itself.
- **Bite force** was requested in the 116 / MASTER_ORDERS source list but was not found on the pages opened, so it is unused rather than guessed.
- **Naming the Thanksgiving game once as a dated fact.** 116 allows naming the game; the user’s brief disallows NFL team names. These cuts name only the date, in the description and caption, never a team.

Nothing was pushed.
