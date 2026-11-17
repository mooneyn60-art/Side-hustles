# QA verdict: wmsw-ep1-saltwater-crocodile

**Script:** `channels/shorts-push-1116/wms-wednesdays-ep1-4.md`, § 1 ("Would Meatball Survive a Saltwater Crocodile?", EP 1, 56 words, 17.28 s). side-hustles main @ 77f687b.
**Checklist:** `channels/qa/checklist.md`. QA run Mon 11/16/2026 (ET), script stage. A render-stage check is still owed.
**Overall: FIX.** One line needs changing: the spoken verdict (C2). Everything else passes, apart from one channel-level WATCH on the series template and a TikTok block (YouTube-only as written).

## Results

| ID | Result | Note |
|---|---|---|
| Y1 Not templated | PASS | The hook fact (dive time), the knee-deep warning and the QLD rule are new to the channel. Script notes say it avoids the croc-bite, freshwater and nest-sex teasers. |
| Y2 Same situation, same outcome | **WATCH (series)** | The Wednesdays format fixes the open and makes the close "the same shape every time": "Verdict: <hedged answer>. Nothing's guaranteed." Earlier WMS episodes end "Meatball lived. Nothing's guaranteed." YouTube lists "characters … put in the same situation over and over again with the same outcome" as not monetizable ([1311392](https://support.google.com/youtube/answer/1311392)). Mitigation: let each verdict's wording and outcome come from its own source (EP 1 negative, EP 4 positive), and don't make the stamp and sting the bulk of the video. Log outcomes across episodes. |
| Y3 Animals in peril or distress | PASS | Frame 0 is a calm croc, eyes above the water. No animal is hurt, trapped or rescued, and no attack is shown (the knee-deep shot is "a ripple"). Policy wording confirmed on [1311392](https://support.google.com/youtube/answer/1311392). The July 2026 date is press-reported ([TechCrunch](https://techcrunch.com/2026/07/20/youtube-clarifies-policies-around-ai-slop-and-upsetting-videos/)). |
| Y4 Not stitched Shorts as long-form | N/A | Short. |
| Y5 New narration and visuals | PASS | Three of six spoken lines closely follow official sentences, but the gag, the "You?" hook frame, the verdict and the question are original, and all visuals are drawn. |
| Y6 Not shock-only or misleading | PASS (after the C2 fix) | The current verdict overstates fatality (see C2). |
| Y7 AI persona advice | PASS | The safety rule is attributed ("Queensland's rule"). Meatball isn't presented as an expert. |
| Y8 GenAI disclosure | PASS | Drawn and non-realistic, so YouTube doesn't require disclosure ([14328491](https://support.google.com/youtube/answer/14328491)). The house rule keeps the AI label on ([MO L205](https://github.com/mooneyn60-art/skills/blob/082e9752fa806dbd358f07c7f8f73f3eda55600e/skills/channel-brain/MASTER_ORDERS.md#L205)). |
| Y9 Advertiser-friendly | PASS | No graphic beat and no swears. Keep the "horrific wounds" part of the Australian Museum quote out of the cards. |
| T1–T5 TikTok | **BLOCK for TikTok / N/A for YouTube** | At 17.28 s it fails the 1-minute rule ([US Terms §2](https://www.tiktok.com/legal/page/global/creator-rewards-program-us/en); [MO L201–202](https://github.com/mooneyn60-art/skills/blob/082e9752fa806dbd358f07c7f8f73f3eda55600e/skills/channel-brain/MASTER_ORDERS.md#L201)). It posts to TikTok only as a separate 61–75 s clean cut (or 65–92 s sweary) with new sourced beats. Never loop or pad this Short. |
| C1 Facts sourced | PASS | All four lines were checked on the live pages 11/16: NT.gov.au "Large saltwater crocodiles can stay underwater for up to one hour…"; Kakadu "…can attack in knee-deep water, so even wading can be dangerous."; QLD Be Crocwise "Keep out of the water. Stay more than 5 metres away from the water's edge. Keep a sturdy object between yourself and the water."; Australian Museum "A person seized in the water by a Estuarine Crocodile has little chance of escaping without serious injury, if at all." |
| C2 No invented verdict | **FIX** | See Fix 1. |
| C3 Safety conditions kept | PASS | The condition "where they live" is spoken, and the card carries all three QLD steps. The verdict credits no tactic. |
| C4 Jokes add no facts | PASS | "Meatball held his breath. His cat, Sauce, stopped the stopwatch." adds no number, motive or claim. |
| C5 Logos and betting | PASS | None. |
| C6 Lane | PASS | A "Would Meatball Survive?" big animal is an allowed lane ([MO L170](https://github.com/mooneyn60-art/skills/blob/082e9752fa806dbd358f07c7f8f73f3eda55600e/skills/channel-brain/MASTER_ORDERS.md#L170)). |
| C7 Title, length, facts | PASS | No banned words. 17.28 s. Four sourced facts. |
| C8 Pet claims | N/A | No pet claim. |

## Fixes

**Fix 1 (C2, blocks): the spoken verdict overstates the source and is contradicted by official data.**
- Offending line (row 5): "Verdict: in the water, probably not. Nothing's guaranteed." In a "Would Meatball Survive?" episode this is heard as "he probably dies".
- The cited source (CB50) says something narrower: "A person **seized** in the water … has little chance of escaping **without serious injury**, if at all." That is about being seized, not just being in the water, and about injury, not death.
- The Queensland Government says the opposite of "probably not survive": "There have been over 50 crocodile attacks on humans since 1985, with about a third of these resulting in a fatality." (https://www.qld.gov.au/environment/plants-animals/animals/living-with/staying-safe-around-wildlife , opened 11/16). Its attack list puts it at 15 fatal of 51 since 12/1985 (https://www.qld.gov.au/environment/plants-animals/animals/living-with/crocodiles/crocodile-sightings/crocodile-attacks).
- Replacement line (10 words, +2; the Short becomes 58 words / 17.89 s, still inside 52–58 and 16–20 s): **"Verdict: grabbed in the water? Probably seriously hurt. Nothing's guaranteed."**
- Stamp and chips: VERDICT stamp: `GRABBED IN THE WATER? PROBABLY SERIOUSLY HURT / NOTHING'S GUARANTEED`. Chips: `HEDGED`; `'LITTLE CHANCE OF ESCAPING WITHOUT SERIOUS INJURY, IF AT ALL' (Australian Museum, CB50)`.
- Description, add after the Australian Museum quote: Queensland Government: "There have been over 50 crocodile attacks on humans since 1985, with about a third of these resulting in a fatality." Add it as a new fact row (CB-QLD-ATTACKS) and have Research clear it.
- Fallback if Social Studio wants no injury talk: "Meatball lived. Nothing's guaranteed." (rulings-1116 #4).
- Note: Research's 11/16 factcheck (`factcheck-shorts-push-1116.md` row 179) passed this verdict. QA disagrees for the reasons above. Please route it back to Research for sign-off.

**Watch 1 (Y2, series level, no block for EP 1):** keep the verdict wording specific to each episode's source, and don't add the same stock close line to every episode. Before EP 5, list the outcomes of all WMS and Wednesdays episodes. If most land the same way ("lived" or "probably not"), change the format rather than single episodes.

**Before TikTok:** a separate minute cut, run through T1–T5.
