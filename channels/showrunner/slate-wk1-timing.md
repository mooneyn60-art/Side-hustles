# Slate wk1: chapter Shorts, final (timing copy; the slate is not edited)

Built Mon Nov 16, 2026, 7:24 PM ET, with Social Studio's final rulings 1–7 and ruling 8 (UC Davis) applied. Updated about 7:35 PM ET: every fix in /workspace/qa/slate-wk1-shorts-qa.md is applied word for word (the list is below). Source: /workspace/showrunner/slate-wk1.md as saved at 7:19 PM ET (QA pass 3), read-only.

## Final summary

| Short | Hook (words) | Words / s | PASS/FAIL |
|---|---|---|---|
| EP1 S1 | "Your dog ate white chocolate, which has almost no theobromine." (10) | 56 / 17.28 s | PASS |
| EP1 S2 | "How long after chocolate do dog symptoms start?" (8) | 58 / 17.89 s | PASS |
| EP1 S3 | "Your cat probably won't touch chocolate. It can still be dangerous." (11) | 55 / 16.97 s | PASS |
| EP2 S1 | "Your dog may have 100 million or more scent receptors." (10) | 57 / 17.58 s | PASS |
| EP2 S2 | "Your dog jumps on you at the door." (8) | 55 / 16.97 s | PASS |
| EP2 S3 | "You were only gone 2 hours." (6) | 57 / 17.58 s | PASS |
| EP3 S1 | "Your cat kneads you, then drools on you." (8) | 58 / 17.89 s | PASS |
| EP3 S2 | "Kneading your chest? It's "almost like a sign of the bond."" (11) | 54 / 16.66 s | PASS |
| EP3 S3 | "Your cat wakes you at night? Cats are naturally crepuscular." (10) | 52 / 16.04 s | PASS |

Hard checks run on all 9 (every one passes):
- hook ≤11
- 52–58 words
- no banned words
- one prompt
- ends on And
- no spoken credit
- one action-only gag
- comma-form pets
- cards readable (3 w/s)

Method: wc()/sec() verbatim from /workspace/drafts/shorts-push-1116/.build/check.py at 194.5 wpm. Hook = the first spoken line, 11 words max. For EP1 S3, EP3 S2 and EP3 S3 that is the full two-sentence line from the ruling, still ≤11. Cards are read at 3 words/s, and the phone number counts as +3. A card passes if it is on screen at least that long. Spoken-credit scan: says/ASPCA/UC Davis/Cornell/behaviorist/FDA/Merck/AKC/Tufts/Penn/iCatCare/Grigg/Rehn/Keeling/AAHA/AAFP. Gag scan: no numbers, danger, feeling, motive or instruction words. Generator: /workspace/scripts/.build/final.py and gen_final.py.

Src tags: **S** = slate/QA words kept · **R** = text set by a Social Studio ruling 11/16 · **R+S** = slate words re-cut under a ruling · **QA** = QA fix text, word for word (slate-wk1-shorts-qa.md) · **F** = my fill (fact-pack wording, or an action-only Meatball gag).

## Scripts, line by line

### EP1 S1: 56 words / 17.28 s, PASS

| # | Start–end (s) | Words | Src | Role | Spoken line | On-screen source card |
|---|---|---|---|---|---|---|
| 1 | 0.00–3.08 | 10 | R+S | hook | Your dog ate white chocolate, which has almost no theobromine. | ASPCA |
| 2 | 3.08–6.17 | 10 | F | gag | Meatball weighed the bar. His dog, Noodle, took the scale. | — |
| 3 | 6.17–8.02 | 6 | S | body | It's not considered toxic to pets. | UC Davis |
| 4 | 8.02–14.19 | 20 | R | body | But some dogs may be sensitive to the amount of sugar and fat, and any chocolate may lead to pancreatitis. | ASPCA |
| 5 | 14.19–17.28 | 10 | S | prompt | Where do you hide the chocolate from your dog? And | — |

Cards (3 words/s):

| Card | Text | Words | Needs | On–off (s) | On screen | Result |
|---|---|---|---|---|---|---|
| source card | ASPCA | 1 | 0.33 s | 0.00–3.08 | 3.08 s | PASS |
| source card | UC Davis | 2 | 0.67 s | 6.17–8.02 | 1.85 s | PASS |
| source card | ASPCA | 1 | 0.33 s | 8.02–14.19 | 6.17 s | PASS |
| ASPCA ingestion line (pinned) | ASPCA: if you think your dog ate chocolate, note the amount and contact your vet or animal poison control, (888) 426-4435. A consultation fee may apply. | 29 (incl. +3 phone) | 9.67 s | 2.30–17.28 + loop | 14.98 s | PASS |

Facts: CH-F7 (ASPCA, "almost no theobromine", "may be sensitive to the amount of sugar and fat", "may lead to … pancreatitis"); CH-F13 (UC Davis, "not considered toxic to pets"). Never "safe".

### EP1 S2: 58 words / 17.89 s, PASS

| # | Start–end (s) | Words | Src | Role | Spoken line | On-screen source card |
|---|---|---|---|---|---|---|
| 1 | 0.00–2.47 | 8 | S | hook | How long after chocolate do dog symptoms start? | — |
| 2 | 2.47–3.70 | 4 | S | body | Three sources, three clocks. | — |
| 3 | 3.70–6.79 | 10 | F | gag | Meatball set the clocks. His dog, Noodle, took a clock. | — |
| 4 | 6.79–8.95 | 7 | F | body | Signs can appear within a few hours. | "within a few hours" (FDA) |
| 5 | 8.95–12.34 | 11 | F | body | Clinical signs usually occur within 6 to 12 hours after ingestion. | "usually occur within 6–12 hours after ingestion" (Merck Veterinary Manual) |
| 6 | 12.34–14.81 | 8 | F | body | Signs can begin 2 to 24 hours after. | Clinical signs of chocolate poisoning in dogs can begin 2-24 hours after ingestion. (UC Davis) |
| 7 | 14.81–17.89 | 10 | S | prompt | Where do you hide the chocolate from your dog? And | — |

Cards (3 words/s):

| Card | Text | Words | Needs | On–off (s) | On screen | Result |
|---|---|---|---|---|---|---|
| source card | "within a few hours" (FDA) | 5 | 1.67 s | 6.79–17.89 + loop | 11.11 s | PASS |
| source card | "usually occur within 6–12 hours after ingestion" (Merck Veterinary Manual) | 11 | 3.67 s | 8.95–17.89 + loop | 8.95 s | PASS |
| source card | Clinical signs of chocolate poisoning in dogs can begin 2-24 hours after ingestion. (UC Davis) | 15 | 5.00 s | 12.34–17.89 + loop | 5.55 s | PASS |
| ASPCA ingestion line (pinned) | ASPCA: if you think your dog ate chocolate, note the amount and contact your vet or animal poison control, (888) 426-4435. A consultation fee may apply. | 29 (incl. +3 phone) | 9.67 s | 2.30–17.89 + loop | 15.59 s | PASS |

Facts: CH-F5 (FDA "can appear within a few hours"); CH-F12 (Merck "usually"); UC Davis "can begin 2-24 hours after ingestion", https://healthtopics.vetmed.ucdavis.edu/health-topics/chocolate-poisoning-dogs. Three separate clocks, no merged range. The clock cards stay up through the loop.

### EP1 S3: 55 words / 16.97 s, PASS

| # | Start–end (s) | Words | Src | Role | Spoken line | On-screen source card |
|---|---|---|---|---|---|---|
| 1 | 0.00–3.39 | 11 | R | hook | Your cat probably won't touch chocolate. It can still be dangerous. | ASPCA |
| 2 | 3.39–6.79 | 11 | F | gag | Meatball called his cat, Sauce, over. She walked the other way. | — |
| 3 | 6.79–8.64 | 6 | F | body | Fortunately, cats lack sweet taste buds. | ASPCA |
| 4 | 8.64–11.11 | 8 | F | body | Cats are sensitive to theobromine just like dogs. | ASPCA |
| 5 | 11.11–13.88 | 9 | F | body | In dogs, it's the main culprit in chocolate toxicity. | FDA |
| 6 | 13.88–16.97 | 10 | S | prompt | Where do you hide the chocolate from your dog? And | — |

Cards (3 words/s):

| Card | Text | Words | Needs | On–off (s) | On screen | Result |
|---|---|---|---|---|---|---|
| source card | ASPCA | 1 | 0.33 s | 0.00–3.39 | 3.39 s | PASS |
| source card | ASPCA | 1 | 0.33 s | 6.79–8.64 | 1.85 s | PASS |
| source card | ASPCA | 1 | 0.33 s | 8.64–11.11 | 2.47 s | PASS |
| source card | FDA | 1 | 0.33 s | 11.11–13.88 | 2.78 s | PASS |
| ASPCA ingestion card, "your pet" form (pinned; card only, QA S3-1) | ASPCA: if you think your pet ate chocolate, note the amount and contact your vet or animal poison control, (888) 426-4435. A consultation fee may apply. | 29 (incl. +3 phone) | 9.67 s | 3.39–16.97 + loop | 13.57 s | PASS |

Facts: CH-F8 (ASPCA, "can be dangerous", "lack sweet taste buds", "sensitive to theobromine just like dogs"; "if your cat does eat chocolate, it is best to follow the above recommendations as well", which is why QA added the "your pet" card); CH-F1 (FDA, "the main culprit in chocolate toxicity in dogs").

### EP2 S1: 57 words / 17.58 s, PASS

| # | Start–end (s) | Words | Src | Role | Spoken line | On-screen source card |
|---|---|---|---|---|---|---|
| 1 | 0.00–3.08 | 10 | F | hook | Your dog may have 100 million or more scent receptors. | AKC |
| 2 | 3.08–4.32 | 4 | F | body | Depending on the breed. | AKC |
| 3 | 4.32–6.17 | 6 | F | body | You have 5 or 6 million. | AKC |
| 4 | 6.17–9.56 | 11 | F | gag | Meatball hid his shoes. His dog, Noodle, brought a shoe back. | — |
| 5 | 9.56–13.57 | 13 | F | body | The smelling section of a dog brain is 40 times larger than ours. | AKC |
| 6 | 13.57–17.58 | 13 | S | prompt | What does your dog do in the first 10 seconds you're home? And | — |

Cards (3 words/s):

| Card | Text | Words | Needs | On–off (s) | On screen | Result |
|---|---|---|---|---|---|---|
| source card | AKC | 1 | 0.33 s | 0.00–3.08 | 3.08 s | PASS |
| source card | AKC | 1 | 0.33 s | 3.08–4.32 | 1.23 s | PASS |
| source card | AKC | 1 | 0.33 s | 4.32–6.17 | 1.85 s | PASS |
| source card | AKC | 1 | 0.33 s | 9.56–13.57 | 4.01 s | PASS |

Facts: DB32 (AKC, "Depending on the breed, dogs have up 100 million or more"; humans "5–6 million"); DB33 (AKC, brain section "40 times larger", shown as brain size, not smelling power). The slate's two sentences are tightened into one hook; the human figure moves to line 3.

### EP2 S2: 55 words / 16.97 s, PASS

| # | Start–end (s) | Words | Src | Role | Spoken line | On-screen source card |
|---|---|---|---|---|---|---|
| 1 | 0.00–2.47 | 8 | S | hook | Your dog jumps on you at the door. | — |
| 2 | 2.47–6.17 | 12 | QA | body | Anxious dogs may appear extra friendly: approaching, jumping on someone, licking faces. | Tufts Cummings School of Veterinary Medicine, 2023 |
| 3 | 6.17–8.95 | 9 | F | gag | Meatball dropped his keys. His dog, Noodle, has them. | — |
| 4 | 8.95–12.96 | 13 | QA | body | Dogs exhibiting frequent anxious behavior should see their veterinarian as soon as possible. | Tufts Cummings School of Veterinary Medicine, 2023 |
| 5 | 12.96–16.97 | 13 | S | prompt | What does your dog do in the first 10 seconds you're home? And | — |

Cards (3 words/s):

| Card | Text | Words | Needs | On–off (s) | On screen | Result |
|---|---|---|---|---|---|---|
| source card | Tufts Cummings School of Veterinary Medicine, 2023 | 7 | 2.33 s | 2.47–6.17 | 3.70 s | PASS |
| source card | Tufts Cummings School of Veterinary Medicine, 2023 | 7 | 2.33 s | 8.95–12.96 | 4.01 s | PASS |

Facts: "may not be pure joy" is cut (ruling 7). Line 2 is QA S2-1, word for word: DL-F4 (Tufts, May 4, 2023) with the whole cluster kept, "also" dropped and "may" kept. Line 4 is QA S2-2, word for word: UNV-4 (Tufts), the slate's safety condition. It replaces the Penn Vet "repeatedly" line, which duplicated the drafted dogs-lick-v6-yt Short.

### EP2 S3: 57 words / 17.58 s, PASS

| # | Start–end (s) | Words | Src | Role | Spoken line | On-screen source card |
|---|---|---|---|---|---|---|
| 1 | 0.00–1.85 | 6 | S | hook | You were only gone 2 hours. | — |
| 2 | 1.85–5.86 | 13 | S | body | One study of 12 dogs found more intense greetings after just 2 hours. | Rehn & Keeling 2011 |
| 3 | 5.86–7.71 | 6 | F | gag | His dog, Noodle, took Meatball's timer. | — |
| 4 | 7.71–13.57 | 19 | S | body | The dogs also showed more physical activity and more attentive behavior when the owner returned, already after 2 hours. | Rehn & Keeling 2011 |
| 5 | 13.57–17.58 | 13 | S | prompt | What does your dog do in the first 10 seconds you're home? And | — |

Cards (3 words/s):

| Card | Text | Words | Needs | On–off (s) | On screen | Result |
|---|---|---|---|---|---|---|
| source card | Rehn & Keeling 2011 | 3 | 1.00 s | 1.85–5.86 | 4.01 s | PASS |
| source card | Rehn & Keeling 2011 | 3 | 1.00 s | 7.71–13.57 | 5.86 s | PASS |
| "cannot distinguish" hedge card, full sentence (pinned from 1.85 s through the loop, QA S3-1) | Rehn & Keeling 2011: 'this study cannot distinguish between whether dogs were aware of the length of time they were alone (but did not signal it) or whether they were unaware until reminded of it by the return of their owner.' | 40 | 13.33 s | 1.85–17.58 + loop | 15.73 s | PASS |

Facts: UNV-3 (Rehn & Keeling 2011, 12 privately owned dogs, "already after 2 h"); QA E2-2 line word for word. No tail-wag line (#67). Never "knows".

### EP3 S1: 58 words / 17.89 s, PASS

| # | Start–end (s) | Words | Src | Role | Spoken line | On-screen source card |
|---|---|---|---|---|---|---|
| 1 | 0.00–2.47 | 8 | S | hook | Your cat kneads you, then drools on you. | — |
| 2 | 2.47–4.01 | 5 | S | body | Some cats really do that. | iCatCare |
| 3 | 4.01–7.71 | 12 | F | gag | Meatball laid out a towel. His cat, Sauce, kneaded his pajamas instead. | — |
| 4 | 7.71–11.41 | 12 | F | body | Some cats dribble as they anticipate the milk-feed that kneading usually predicted. | iCatCare |
| 5 | 11.41–15.12 | 12 | QA | body | Cats grow out of it, but a few keep kneading as adults. | iCatCare |
| 6 | 15.12–17.89 | 9 | S | prompt | What time does your cat start kneading you? And | — |

Cards (3 words/s):

| Card | Text | Words | Needs | On–off (s) | On screen | Result |
|---|---|---|---|---|---|---|
| source card | iCatCare | 1 | 0.33 s | 2.47–4.01 | 1.54 s | PASS |
| source card | iCatCare | 1 | 0.33 s | 7.71–11.41 | 3.70 s | PASS |
| source card | iCatCare | 1 | 0.33 s | 11.41–15.12 | 3.70 s | PASS |

Facts: CK-F3, then CK-F4 (iCatCare: "Cats grow out of this behaviour when it ceases to be necessary, but a few will retain it into adulthood"), in QA S3-1's wording. The old CK-F1 line duplicated the drafted cats-knead-v6-yt Short. The slate's first sentence is already a full hook (8 words); "Some cats really do that." follows it word for word.

### EP3 S2: 54 words / 16.66 s, PASS

| # | Start–end (s) | Words | Src | Role | Spoken line | On-screen source card |
|---|---|---|---|---|---|---|
| 1 | 0.00–3.39 | 11 | R | hook | Kneading your chest? It's "almost like a sign of the bond." | Emma Grigg, UC Davis |
| 2 | 3.39–7.10 | 12 | F | gag | Meatball patted the cat bed. His cat, Sauce, sat on the floor. | — |
| 3 | 7.10–13.88 | 22 | F | body | If your cat is kneading on your lap or chest this shows that they associate your relationship with that of their mother. | iCatCare |
| 4 | 13.88–16.66 | 9 | S | prompt | What time does your cat start kneading you? And | — |

Cards (3 words/s):

| Card | Text | Words | Needs | On–off (s) | On screen | Result |
|---|---|---|---|---|---|---|
| source card | Emma Grigg, UC Davis | 4 | 1.33 s | 0.00–3.39 | 3.39 s | PASS |
| source card | iCatCare | 1 | 0.33 s | 7.10–13.88 | 6.79 s | PASS |

Facts: CK-F7 (Grigg, "almost like a sign of the bond"), CK-F2 (iCatCare, exact, "this shows that they associate"). No "loves".

### EP3 S3: 52 words / 16.04 s, PASS

| # | Start–end (s) | Words | Src | Role | Spoken line | On-screen source card |
|---|---|---|---|---|---|---|
| 1 | 0.00–3.08 | 10 | R | hook | Your cat wakes you at night? Cats are naturally crepuscular. | Cornell Feline Health Center |
| 2 | 3.08–7.71 | 15 | F | gag | Meatball turned off the bedside lamp. His cat, Sauce, switched the lamp right back on. | — |
| 3 | 7.71–13.26 | 18 | S | body | More active at dawn and dusk. Depending on the cat, that may mean waking you in the night. | Cornell Feline Health Center |
| 4 | 13.26–16.04 | 9 | S | prompt | What time does your cat start kneading you? And | — |

Cards (3 words/s):

| Card | Text | Words | Needs | On–off (s) | On screen | Result |
|---|---|---|---|---|---|---|
| source card | Cornell Feline Health Center | 4 | 1.33 s | 0.00–3.08 | 3.08 s | PASS |
| source card | Cornell Feline Health Center | 4 | 1.33 s | 7.71–13.26 | 5.55 s | PASS |
| AAHA/AAFP condition card (pinned; card only, ruling 5) | Senior cats exhibiting new or unusual behavior should be evaluated for medical conditions. (AAHA/AAFP 2021 Feline Life Stage Guidelines) | 20 | 6.67 s | 7.71–16.04 + loop | 8.33 s | PASS |

Facts: UNV-6 (Cornell, "naturally crepuscular", "more active", "depending upon the cat … may"); QA body word for word; UNV-7 condition on the card only.

## Rulings applied 11/16

1. Hook = the first spoken line, ≤11 words, and strong alone. EP2 S1 is re-cut to "Your dog may have 100 million or more scent receptors." (it keeps "may"). EP1 S2, EP2 S2, EP2 S3 and EP3 S1 now open on the slate's own first sentence; their second sentences are kept as body lines or replaced under rulings. EP3 S2 uses the ruling's hook. The PASS* concept is dropped.
2. EP1 S3 hook: "Your cat probably won't touch chocolate. It can still be dangerous." (ASPCA card).
3. EP1 S2 ASPCA card is pinned from 2.3 s through the loop (15.59 s on screen vs 9.67 s needed).
4. EP2 S3 "cannot distinguish" hedge card is pinned from the study line through the QA line, 1.85–13.57 s: 11.72 s vs 6.33 s needed.
5. EP3 S3 is card only: 52 words / 16.04 s. The AAHA/AAFP card is up 7.71 s through the loop (8.33 s vs 5.00 s needed).
6. No spoken credits anywhere. Removed: "The ASPCA says" ×2, "UC Davis says", "A vet behaviorist says", "A UC Davis behaviorist:", "Cornell:". Each credit is now an on-screen source card. QA's quoted words are kept. EP3 S2 hook: Kneading your chest? It's "almost like a sign of the bond." (Emma Grigg, UC Davis card). EP3 S3 hook: "Your cat wakes you at night? Cats are naturally crepuscular." (Cornell card).
7. EP1 S1 uses ASPCA's exact "may be sensitive to the amount of sugar and fat". EP2 S2: "may not be pure joy" is cut. The Tufts DL-F4 replacement was then re-cut by QA S2-1 (see the QA fixes below).
8. UC Davis 2–24 h is SOURCED: https://healthtopics.vetmed.ucdavis.edu/health-topics/chocolate-poisoning-dogs . EP1 S2 speaks "Signs can begin 2 to 24 hours after." Its own clock card carries the exact sentence, separate from the FDA and Merck clocks.

## QA fixes applied 11/16 (/workspace/qa/slate-wk1-shorts-qa.md, all word for word)

- EP1 S3-1: added the pinned "your pet" ingestion card, card only, with no spoken change: "ASPCA: if you think your pet ate chocolate, note the amount and contact your vet or animal poison control, (888) 426-4435. A consultation fee may apply." 29 words (incl. +3 phone) need 9.67 s. Pinned 3.39–16.97 s + loop = 13.57 s (QA said 13.58 s; the 0.01 s gap is rounding). PASS.
- EP2 S2-1: line 2 is now "Anxious dogs may appear extra friendly: approaching, jumping on someone, licking faces." (12 words). Card: "Tufts Cummings School of Veterinary Medicine, 2023" (7 words, needs 2.33 s, on 3.70 s). PASS.
- EP2 S2-2: line 4 is now "Dogs exhibiting frequent anxious behavior should see their veterinarian as soon as possible." (13 words). Card: "Tufts Cummings School of Veterinary Medicine, 2023" (needs 2.33 s, on 4.01 s). PASS. The Penn Vet card is removed with the old line. The Short is now 55 words / 16.97 s, matching QA's figure.
- EP2 S3-1: the hedge card now carries the full sentence: "Rehn & Keeling 2011: 'this study cannot distinguish between whether dogs were aware of the length of time they were alone (but did not signal it) or whether they were unaware until reminded of it by the return of their owner.'" 40 words need 13.33 s. Pinned 1.85–17.58 s + loop = 15.73 s. PASS. No spoken change.
- EP3 S1-1: line 5 is now "Cats grow out of it, but a few keep kneading as adults." (12 words; iCatCare card; CK-F4). Still 58 words / 17.89 s.
- EP3 S3-1 (label): the condition card credit uses QA's preferred long form, "(AAHA/AAFP 2021 Feline Life Stage Guidelines)". The card is 20 words by the counter, needs 6.67 s at 3 words/s, and is up 8.33 s, so it passes.
- EP1 S2 (label): "(Merck)" → "(Merck Veterinary Manual)". The Merck clock card is now 11 words, needs 3.67 s, and is on 8.95 s. PASS.
- Label table (d): the other labels are approved as written (ASPCA, UC Davis, FDA, AKC, Rehn & Keeling 2011, iCatCare, Emma Grigg, UC Davis, Cornell Feline Health Center). "Tufts (Cummings School)" is tidied to "Tufts Cummings School of Veterinary Medicine, 2023". Penn Vet is gone with the old line 4.
- Staging (see below): EP1 S1 shows Noodle with the scale only. The other QA staging notes are copied in.

## Staging (QA, for the Animator)

- EP1 S1 gag: show Noodle with the scale only, never with or eating the bar. (The spoken line "Meatball weighed the bar. His dog, Noodle, took the scale." stays. The bar is only on Meatball's side of the frame, and Noodle never touches it.)
- EP3 S1: the drool is one stylized blue drop.
- No sick-dog acting; Meatball is the cartoon ball.
- Gags are action-only on Meatball and the pets. Sauce is "she", which matches canon.
- The slate's named first shots and the Animator rules still govern visuals.

## Still open (minor)

- EP1 S2 and EP3 S1 sit at 58 words, the top of the band, so any added word fails them.
- No QA fix was left unapplied. Nothing pushed a Short outside 52–58, so no gag or filler was trimmed.
- WATCH (QA): EP2 S1 shares DB32 with the on-hold long-form longform-dog-bornas. No change asked for.
