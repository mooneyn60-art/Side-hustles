# QA verdict: showrunner slate, week 1 (EP 1 chocolate, EP 2 dogs lick, EP 3 cats knead, 15 chapters)

**Slate version reviewed (pass 4, final):** `/workspace/showrunner/slate-wk1.md`, mtime **2026-11-16 19:19:48 ET**, 44,599 bytes, 422 lines, sha256 **34d2bc0ce392**. It is byte-identical to side-hustles origin/main @ **93b38b5** ("Slate wk1 QA pass 3 applied; retire dog-nose teaser", 19:20:21 ET).
**Revision:** pass 4 (final), Mon 11/16/2026 about 7:21 PM ET. It supersedes pass 3 (slate @ b5a2c27, sha256 90fd3520f23e), pass 2 (@ 062d62f, a3014f5ac5d7) and pass 1 (@ 8a7ad35, 99c085d3064a). The "Pass 4" section below is the current verdict. The later sections are history.
**Checklist:** `channels/qa/checklist.md`. Citations: YouTube YPP [1311392](https://support.google.com/youtube/answer/1311392), Shorts [12504220](https://support.google.com/youtube/answer/12504220), TikTok [US Terms](https://www.tiktok.com/legal/page/global/creator-rewards-program-us/en), [EEA Terms](https://www.tiktok.com/legal/page/global/tiktok-creator-rewards-program-eea/en), [CG Integrity and Authenticity](https://www.tiktok.com/community-guidelines/en/integrity-authenticity).
**Claude's rules:** MO = `skills/channel-brain/MASTER_ORDERS.md` in mooneyn60-art/skills, branch `claude/youtube-monetization-strategy-m9vz6i`. I re-pulled it at about 7:05 PM ET: the newest commit on the branch is still 082e975 and the file has not changed. Links are permalinks at that commit.
**Diffed against these planned or posted cuts:**
- side-hustles `channels/scripts/`: `chocolate-v6-yt.json`, `dogs-lick-v6-yt.json`, `tt-dogs-lick.json`, `cats-knead-v6-yt.json`, `tt-cats-knead.json` (drafts with proposed slots, per `channels/packaging/december-chocolate.md`, `why-dogs-lick.md` and `why-cats-knead.md`)
- skills repo `skills/oh-meatball/scripts/drawn-house/dog-chocolate-v6-yt.json`: Claude's rendered Short "#72", commit 63fff05, not yet in `posted.csv`
- the posted tail-wag Short (#67, 11/16 10:00 ET, per `posted.csv`)
**Run:** Mon 11/16/2026 (ET), script and slate stage. Every source page was opened live by QA this session (quotes below). The Animator concept boards were viewed too: `channels/animation/organs-concept-v1.jpg`, `noodle-sauce-concept-v2.jpg`, and the house ref `/workspace/animation/refs/character_ref.png`.



## Pass 4 (final verdict)

**Out of scope:** the 4 MASTER_ORDERS items (long-form shape, 3/week slots, title lead, new designs/style lock) stay out of scope; Social Studio is taking them to Moondog88.

| Ep | Final verdict | Note |
|---|---|---|
| EP 1 chocolate (3 Shorts / 5 TikToks) | **PASS** | |
| EP 2 dogs (3 / 3) | **PASS** | E2-1 is resolved by retiring `dog-nose`, on the condition in the WATCH list. |
| EP 3 cats (3 / 1) | **PASS** | |

**Diff b5a2c27 → 93b38b5 (slate): 12 hunks, all accounted for.**
- **EP 1:** only 3 lines changed. L70 adds the T5-only "your pet" rule. L94 adds the pass 3 verdict and WATCH note. L149 changes the T5 0:58–1:07 line to "ASPCA: if you think your pet ate chocolate, note the amount and contact your vet or animal poison control, (888) 426-4435. A consultation fee may apply." That is identical to the pass 3 line except "pet" for "dog", and the word count is unchanged. No other EP 1 script, fact, hook or timing line changed.
- **E2-1:** applied. `dog-nose` was added to the no-reuse list (L34), and S1 is kept per Social Studio's ruling. The `dog-teasers.md` §3 heading on main now reads "RETIRED 11/16".
- **E2-2:** applied word for word (L196). UNV-2 was removed from S3, the "cannot distinguish" hedge and "never knows" stay, and there is no tail-wag line. T3 keeps UNV-2 (TikTok only) and has a ≥61 s lint note.
- **E3-1:** applied word for word (L256–259). A "SENIOR CATS" label runs 0:42–1:04, the senior-cats framing is at 0:46–0:57, and the action line is the last spoken line (0:57–1:04). "May represent" is kept, with no dementia wording.
- **E3-2:** applied word for word (L240).
- **UNV-6b:** the third-quote card ends with "…" (L256).
- **Facts table:** the UNV-6b/7b status was updated. The pass 3 fix log was appended. EP 2 T2 has a phrasing note.

**New-issue check on the edits:**
- **Hedges:** all kept.
- **Duplicates:** nothing new.
  - E2-2's line isn't in any draft and isn't #67's topic.
  - E3-2's "almost like a sign of the bond" is in the TikTok minute script `cats-knead.md` / `tt-cats-knead`. It is not in the drafted YouTube Short `cats-knead-v6-yt` (kittenhood line only), and S2 already used CK-F7 in its body (accepted in pass 3).
- **Timing:**
  - EP 3 T1 0:46–0:57 is 38 spoken words with "A-A-H-A A-A-F-P" spelled out. That's about 11.7 s at 194.5 wpm against an 11 s window, so T1 runs about 69 s. It still clears 61 s and stays within 65–75 s.
  - EP 2 S3 is 19-word hook + 19-word E2-2 line + hedge, about 17–18 s. That's within the 16–20 s lint band but at the top of the 16–18 s target.
  - All 9 TikToks are still ≥61 s on paper.

**WATCH (no fix needed for PASS):**
1. `channels/scripts/dog-teasers.md` L106 and L114 still list `dog-nose` in both slot plans (Thu 12/10 16:00 and Fri 12/18 16:00; "not booked"). Strike those rows so the retired Short can't be scheduled next to EP 2 S1. **E2-1's PASS depends on `dog-nose` not shipping.**
2. The pass 3 fix log says the GitHub repo wasn't edited, but commit 93b38b5 on side-hustles main does change `channels/scripts/dog-teasers.md` (the heading line only, matching the proposed text). The record is wrong, but the content is right.
3. The timing lint must confirm EP 3 T1 (let 0:46–0:57 run to about 0:58), EP 2 S3 (≤20 s), EP 1 T3 and EP 2 T3 (≥61 s) before render.
4. Carried from pass 3: EP 1 T1/T2 vs the `tts-chocolate` / `tts-dog-chocolate` posting condition, EP 2 T2 phrasing, and Sauce "walks off" in EP 1 and EP 3.

---

## Pass 3 (history; superseded by Pass 4)

**Out of scope:** the 4 MASTER_ORDERS items (long-form shape, 3/week slots, title lead, new designs/style lock) are out of scope for this pass; Social Studio is taking them to Moondog88.

| Ep | Verdict | Open items |
|---|---|---|
| EP 1 chocolate (3 Shorts / 5 TikToks) | **PASS** | WATCH only (see below) |
| EP 2 dogs (3 / 3) | **FIX** | E2-1, E2-2 |
| EP 3 cats (3 / 1) | **FIX** | E3-1, E3-2 |

### Pass 2 fixes, checked against the fix log and the lines themselves
- **Resolved:** F1-1 (ch 1–2 Shorts dropped; S1–S3 = ch 3–5), F1-2 (ASPCA ingestion line word for word at 0:35, the payoff, S1 pinned card, S2 loop card and every EP 1 TikTok close; rule written in), F1-3 (white-chocolate wording; "safe" lines gone), F1-4 (staging binding; ch 4 reframed to "Three sources, three clocks"), F1-5, F2-1 (lick and lip-lick chapters dropped), F2-2 (pucker/sandwich gone; keys planted at the lock and the jump, paid off at 7:30), W-C4, W-Y2 (QA midpoint line; Sauce's action differs in EP 2), F3-1 (option b), F3-2, F3-3, F3-4, the UNV-2 credit, Y5 (porthole once per long-form; each cut names its own first shot), T2 for EP 1 T5 and EP 3 T1 (rewritten to about 69 s and 68 s of new sourced beats, no loops).
- **New issues introduced by the fixes:** E3-1 (the new UNV-7b beat). E2-1, E2-2 and E3-2 were in the slate before and were missed by passes 1–2. They surfaced on a wider diff against the side-hustles drafts this pass.

### Remaining fixes (replacement wording)
- **E2-1 (Y1/Y4): EP 2 S1 duplicates a drafted Short.** `channels/scripts/dog-teasers.md` §3 "dog-nose" (commit 20e89f9) is a 16 s YouTube Short with the same facts (DB32 5–6M / up to 100M / Bloodhounds 300M + DB33 40×) and almost the same hook ("Dogs have up to 100 million scent receptors."). Ship only one: either **drop EP 2 S1** (EP 2 becomes 2 Shorts / 3 TikToks) or **add `dog-nose` to the no-reuse list and don't ship it**. EP 2 T1 (TikTok) is fine either way.
- **E2-2 (Y1): EP 2 S3 re-runs the posted tail-wag Short.** S3's body adds UNV-2 (right-side wag bias), which is the topic of posted #67 (11/16 10:00 ET). Replace it with the rest of the same Rehn & Keeling abstract (SLU page, HTTP 200 this pass): **"The dogs also showed more physical activity and more attentive behavior when the owner returned, already after 2 hours."** The authors' "cannot distinguish" hedge stays, and "never knows" stays. Don't use the abstract's tail-wagging line either (same #67 topic). T3 (TikTok) can keep UNV-2 because #67 is YouTube only.
- **E3-1 (C1/C3/C8): EP 3 T1, 0:46–1:04, the UNV-7b beat (Research quote verified exact, see below).** The quote comes from the senior-cats section of a vet-practice guideline. Spoken alone after the general night lines, it reads as if any cat that wakes you at night may have a disease, and the cut ends on a disease list instead of the action. Scope it and end on the action:
  - 0:46–0:57: "For senior cats, the AAHA/AAFP guidelines say: 'Vocalization, especially nighttime waking, is a common concern and may represent sensory changes (declining hearing and vision), cognitive dysfunction syndrome, pain, hyperthyroidism, or hypertension.'"
  - 0:57–1:04: "Senior cats exhibiting new or unusual behavior should be evaluated for medical conditions." (Said clean and pinned. This is the last spoken line before the quick pick.)
  - A "SENIOR CATS" label stays on screen for 0:42–1:04. No dementia wording, no "your cat may have…". About the same length, so it still clears 61 s.
- **E3-2 (C1): EP 3 S2 hook attributes words Grigg didn't say.** "…probably isn't random, says a UC Davis behaviorist" puts "isn't random" in her mouth. Replace with: **"Kneading your chest? A UC Davis behaviorist: 'almost like a sign of the bond.'"** The body stays as is (CK-F7 + CK-F2, no "loves").

### WATCH (no change needed to pass)
- **EP 1 T1/T2 vs drafted/posted chocolate (Y1/T3): no duplicate.** Nothing about chocolate is in `posted.csv` (side-hustles or skills). The drafted cuts are `chocolate-v6-yt` and #72 `dog-chocolate-v6-yt` (YouTube Shorts) plus `tts-chocolate.json` and Claude's `tts-dog-chocolate.json` (TikTok twins of about 22–25 s). They share CH-F3 (227 vs 57 mg/oz) with T1 and CH-F4 (9/18 mg/lb) with T2. T1 adds F1, F7 and F9 plus the safety line; T2 adds F2, the Merck mg/kg and UC Davis oz/lb units, and F6. Both are new scripts, and the YouTube Shorts aren't on TikTok, so T3 passes. One condition: MO L201–202 keeps sub-minute cuts YouTube-only. If either short TikTok twin is posted to TikTok anyway, don't run T1/T2 in the same week.
- **EP 1 T5:** this is a cat TikTok, but it closes on the dog wording ("if you think your dog ate chocolate"). Optional: say "your pet" in T5 only. It's the APCC page's own wording ("If you think that your pet may have ingested a potentially poisonous substance").
- **EP 2 T2** repeats DL-F4 (the Tufts jump line) and DL-F1, both in the `tt-dogs-lick` / `tt-native-pov` drafts. It passes T3 on new UNV-1/UNV-4 and new gags. Don't reuse the drafts' exact phrasing.
- **TikTok length (T1/T2):** all 9 TikToks clear 61 s on their windows plus added beats: EP 1 T1 80 s, T2 73 s, T3 about 60 s + F7/F13/F10, T4 75 s, T5 about 69 s; EP 2 T1 105 s, T2 70 s, T3 60 s + UNV-4 and the keys; EP 3 T1 about 68 s. EP 1 T3 and EP 2 T3 depend on the added lines. The Scriptwriter's timing lint must show ≥61 s (65–75 s target) before render.
- EP 1 and EP 3 both end Sauce's beat with her "walking off" (W-Y2 asked for a different action each episode). Minor.

### UNV-6b / UNV-7b, opened live this pass
| ID | Source (HTTP) | Verbatim on page | Slate use |
|---|---|---|---|
| UNV-6b | iCatCare "What is a cat?", https://icatcare.org/articles/what-is-a-cat (200; "Updated 26th Sep 2025", first published 15 Aug 2025) | "To be a successful hunter, your cat's natural rhythms will fit the time when their main prey of small creatures are active and vulnerable - usually at dawn and dusk." / "They can be especially active at dawn and dusk and during the spring/summer" / "Some can adapt to a lifestyle not necessarily active at dawn and dusk, but to the activity patterns and availability of food when owners are home, and to a wide range of 'companions'…" | **PASS.** Exact, and the hedges "usually", "can be especially" and "Some can adapt" are all kept. The third quote cuts mid-sentence, so end it with "…" on the card. C8: about cats in general; no "your cat will". Toy-mouse cards only. |
| UNV-7b | AAHA/AAFP 2021 Feline Life Stage Guidelines, section "Behavior and Environmental Needs: Senior Cats", https://www.aaha.org/resources/2021-aaha-aafp-feline-life-stage-guidelines/behavior-and-environmental-needs-senior-cats/ (200; published Feb 18, 2021) | "Vocalization, especially nighttime waking, is a common concern and may represent sensory changes (declining hearing and vision), cognitive dysfunction syndrome, pain, hyperthyroidism, or hypertension." It sits in the same paragraph block as "Senior cats exhibiting new or unusual behavior should be evaluated for medical conditions." | **Quote exact, and "may represent" kept. FIX for framing (E3-1).** This is a clinical guideline for vet teams about senior cats. It is not a description of one condition, and it is about *vocalization* at night, not play. The slate line doesn't say "senior" in the quote, so it can be heard as covering all cats. |

---

# Pass 2 record (history)

## Changes since pass 1 (slate 8a7ad35 to 062d62f)

The slate diff has two parts: line 10 ("Meatball (stick figure)" became "Cartoon-ball Meatball (the live look, pfp-final-c)") and a new 13-line "Staging notes from the Animator" section. No script line, fact, hook, title, chapter or question changed.

| Item | Pass 1 | Pass 2 | Why |
|---|---|---|---|
| F1-4 (EP 1 peril staging, Y3) | FIX | **RESOLVED** (chapter 4 hook reframe now optional) | The staging notes say: "Show the symptoms as icon cards on a clipboard. Noodle stays calm or offscreen. No sick-dog acting, and no gag near the 'can lead to death' line." Also: "The organs never swell or bleed." That is the rule pass 1 asked for. The chapter 4 hook ("Your dog ate chocolate an hour ago and looks fine") is unchanged. It's no longer a Y3 block once the staging holds and F1-2 fixes its card. |
| Y9 (all episodes) | PASS if F1-4 | **PASS** | No sick-dog acting, no swelling or bleeding organs, and lick and drool become "one stylized blue drop, no slobber". |
| C4 / C1 (EP 2 Nose, 40×) | PASS | **PASS, strengthened** | "Show '40×' as two brain-size cards, never as smelling power" matches DB33 (AKC: "the smelling section of a dog brain is 40 times larger"). |
| C3 (all) | as before | **Unchanged** | "Safety lines stay pinned on screen and said clean" helps. But F1-2 is about *which* card EP 1 pins, so it still applies. |
| Y8 / T5 (AI disclosure) | PASS | **PASS, re-checked** | The new organ and Noodle/Sauce boards are flat, non-realistic cartoons. YouTube doesn't require disclosure for non-realistic content ([14328491](https://support.google.com/youtube/answer/14328491)). TikTok's label rule covers "realistic-looking scenes or people" ([CG](https://www.tiktok.com/community-guidelines/en/integrity-authenticity)). The house rule still keeps the AI label on both platforms ([MO L151](https://github.com/mooneyn60-art/skills/blob/082e9752fa806dbd358f07c7f8f73f3eda55600e/skills/channel-brain/MASTER_ORDERS.md#L151), [L205](https://github.com/mooneyn60-art/skills/blob/082e9752fa806dbd358f07c7f8f73f3eda55600e/skills/channel-brain/MASTER_ORDERS.md#L205)). |
| Y5 / Y1 (shared production assets) | — | **WATCH, new** | There is one reusable fur push-in plus porthole iris, and one shared limb rig with swappable organ bodies. A recurring transition or rig is allowed when "the bulk of your content is different" ([1311392](https://support.google.com/youtube/answer/1311392)). Don't let the push-in plus porthole become the opening beat of every chapter cut too; vary the first shot per cut. |
| Meatball look ("cartoon-ball" vs MO's "stick-figure Meatball", [MO L161](https://github.com/mooneyn60-art/skills/blob/082e9752fa806dbd358f07c7f8f73f3eda55600e/skills/channel-brain/MASTER_ORDERS.md#L161)) | — | **No conflict (note)** | The house ref `character_ref.png` shows a meatball body with stick limbs. That's the same character MO calls "stick-figure Meatball" and the Animator calls "cartoon-ball". Not a style change. |
| New assets (organ characters, Noodle/Sauce v2) | in "Approval" | **Still HOLD** | The STYLE LOCK allows "new animals built with the same anatomy kit" and "no new render pipelines" ([MO L161–164](https://github.com/mooneyn60-art/skills/blob/082e9752fa806dbd358f07c7f8f73f3eda55600e/skills/channel-brain/MASTER_ORDERS.md#L161)). The organs and the v2 pets are new designs marked "pending Moondog88". That's not an originality issue; it's an approval item. |
| F1-1, F1-2, F1-3, F1-5, F2-1, F2-2, F3-1 to F3-4, W-C4, W-Y2 | FIX / WATCH | **Still apply, unchanged** | Every offending line is still in the slate word for word (re-checked with grep against a3014f5ac5d7). |
| Croc Short (side note) | QA line | **Either line accepted** | See the note at the end. |

## Overall

| Episode | Verdict | Blocking fixes |
|---|---|---|
| EP 1, What Happens If a Dog Eats Chocolate? (9:00) | **FIX** | F1-1: two chapter Shorts duplicate the drafted chocolate Shorts. F1-2: the safety card on the ingestion cuts can be heard as "wait for signs". F1-3: the white-chocolate wording. F1-5: the comment question is lifted. (F1-4, the no-distress staging, is resolved by the Animator notes.) |
| EP 2, Why Do Dogs Lick You? (8:30) | **FIX** | F2-1: chapters 3 and 4 (Short and TikTok) duplicate the drafted dogs-lick Short and TikTok. F2-2: the pucker and sandwich gag is lifted from the dogs-lick Short. |
| EP 3, Why Do Cats Knead? (8:45) | **FIX** | F3-1: the chapter 1 Short and the chapter 1–4 TikToks duplicate the drafted cats-knead Short and TikTok. F3-2: the cold-open hedge was dropped. F3-3: the 3 AM hook needs its condition. F3-4: the comment question is lifted. |

None of the three is stitched or recut from Shorts (Y4 passes). The new Animator staging clears Y3 and Y9. No winners are invented (C2 passes). No logos or betting (C5 passes). TikTok length rules pass (T1). Every "UNV" row that Research marked sourced checks out on the live page (C1; see the evidence table). The FIXes are duplication against our own drafted cuts, one safety-card choice, and three wording hedges.

**Approval (not a script fix):** the topic is an allowed lane. Pets are one of the two lanes in [MO L137](https://github.com/mooneyn60-art/skills/blob/082e9752fa806dbd358f07c7f8f73f3eda55600e/skills/channel-brain/MASTER_ORDERS.md#L137) and [L170](https://github.com/mooneyn60-art/skills/blob/082e9752fa806dbd358f07c7f8f73f3eda55600e/skills/channel-brain/MASTER_ORDERS.md#L170), so Social Studio's swap of the chocolate chapter for the bedbug sample clears C6. But three things in the slate are not yet in MO, so they need Moondog88's go recorded where Claude reads it ([MO L61](https://github.com/mooneyn60-art/skills/blob/082e9752fa806dbd358f07c7f8f73f3eda55600e/skills/channel-brain/MASTER_ORDERS.md#L61)):
- the long-form shape, where MO says "Why It Sucks to Be Born as a [animal]" ([L221](https://github.com/mooneyn60-art/skills/blob/082e9752fa806dbd358f07c7f8f73f3eda55600e/skills/channel-brain/MASTER_ORDERS.md#L221));
- 3 long-forms a week, against MO's 2 ([L209–212](https://github.com/mooneyn60-art/skills/blob/082e9752fa806dbd358f07c7f8f73f3eda55600e/skills/channel-brain/MASTER_ORDERS.md#L209));
- titles that don't lead with "Your dog" or "Your cat" ([L170](https://github.com/mooneyn60-art/skills/blob/082e9752fa806dbd358f07c7f8f73f3eda55600e/skills/channel-brain/MASTER_ORDERS.md#L170)).

The slate's own status line says the same.

---

## Per-check table

| ID | EP 1 chocolate | EP 2 dogs lick | EP 3 cats knead |
|---|---|---|---|
| **Y4** No stitched or recut Shorts as long-form ([1311392 Reused](https://support.google.com/youtube/answer/1311392); [MO L212–216](https://github.com/mooneyn60-art/skills/blob/082e9752fa806dbd358f07c7f8f73f3eda55600e/skills/channel-brain/MASTER_ORDERS.md#L212)) | PASS. Newly scripted, with organ characters and a new arc. Condition: no shot, audio or render from `chocolate-v6-yt` or `dog-chocolate-v6-yt` goes into the episode. | PASS. Same condition for `dogs-lick-v6-yt` and `tt-dogs-lick`, and for the posted tail-wag Short #67, which covers the 6:30–7:30 lean. | PASS. Same condition for `cats-knead-v6-yt` and `tt-cats-knead`. |
| **Y5** New narration and visuals ([1311392 Reused](https://support.google.com/youtube/answer/1311392)) | PASS. New organ scenes (pellets, Stomach-to-Pancreas card, clipboard), clocks, Sauce sidebar and two-ruler gag. WATCH: the shared push-in, porthole and rig must not be the bulk of any cut. | PASS. Nose map, jump, tail and timing are new material. | **WATCH.** About 0:35–7:00 re-tells the 7 facts already in the 89 s `tt-cats-knead` cut. The new value is the organ scenes plus 7:00–7:45 (UNV-6, UNV-7). See F3-1. |
| **Y1** Not templated or duplicated ([1311392 Generic/Repetitive](https://support.google.com/youtube/answer/1311392); rulings 11/16 #6; [MO L229](https://github.com/mooneyn60-art/skills/blob/082e9752fa806dbd358f07c7f8f73f3eda55600e/skills/channel-brain/MASTER_ORDERS.md#L229)) | **FIX F1-1.** | **FIX F2-1.** | **FIX F3-1.** |
| **Y1, saturation** | **WATCH.** 5 Shorts per episode × 3 episodes is 15 Shorts a week, plus the existing queue at 3 a day ([MO L130](https://github.com/mooneyn60-art/skills/blob/082e9752fa806dbd358f07c7f8f73f3eda55600e/skills/channel-brain/MASTER_ORDERS.md#L130)). MO's own rule is "two or three 16-20 s Shorts on the same creature (different facts, at least a day apart)" ([MO L229](https://github.com/mooneyn60-art/skills/blob/082e9752fa806dbd358f07c7f8f73f3eda55600e/skills/channel-brain/MASTER_ORDERS.md#L229)). Dropping the duplicate Shorts (F1-1, F2-1, F3-1) brings each episode to exactly 3. | same | same |
| **Y2** Same situation, same outcome ([1311392](https://support.google.com/youtube/answer/1311392)) | **WATCH.** All 3 episodes share one skeleton: a "you" plus clock cold open, a "four X" promise, a "most get it wrong" midpoint and a "Sauce walks off / Noodle ends up with it" payoff. The counts are required by [MO L231](https://github.com/mooneyn60-art/skills/blob/082e9752fa806dbd358f07c7f8f73f3eda55600e/skills/channel-brain/MASTER_ORDERS.md#L231), and the pet gags by the bible, so keep both. Vary the midpoint wording and the Sauce beat (see W-Y2). | **WATCH.** "this is where most of us get it wrong" is near EP 1's "the part almost everyone gets wrong". | **WATCH.** "Sauce … walks off" is the third time in three episodes. |
| **Y3** Animals in peril or distress ([1311392 Unsatisfying/Off-putting](https://support.google.com/youtube/answer/1311392); [2802008](https://support.google.com/youtube/answer/2802008); July 2026 date press-reported) | **PASS** (pass 1 was FIX F1-4, now resolved). Animator staging: symptoms are "icon cards on a clipboard. Noodle stays calm or offscreen. No sick-dog acting"; "The organs never swell or bleed." **WATCH:** it's still the declared peril episode, with 10 cuts beside Claude's dog-chocolate Short and the cat-lilies Short. Keep the staging rule on every chapter cut and render, and re-check at render stage. | PASS. Lick is "one stylized blue drop, no slobber". No distress. | PASS. Drool is one stylized blue drop. |
| **Y6** Not misleading | **FIX F1-3** (white chocolate). | PASS. | **FIX F3-2, F3-3.** |
| **Y7** AI persona advice ([1311392 AI Personas](https://support.google.com/youtube/answer/1311392)) | PASS with a condition. Pet health is a sensitive topic. Advice is always attributed (FDA, ASPCA, UC Davis), and "Your vet does the math, not Meatball." The narrator and organs never present as a vet. Keep it that way. | PASS. | PASS. |
| **Y8 / T5** AI disclosure and label ([14328491](https://support.google.com/youtube/answer/14328491); [CG AIGC](https://www.tiktok.com/community-guidelines/en/integrity-authenticity)) | PASS, re-checked on the new boards. Flat non-realistic cartoons (Meatball ball, organs, Noodle/Sauce v2). YouTube disclosure isn't required. TikTok's label rule is for realistic content. House rule: label ON on both ([MO L151](https://github.com/mooneyn60-art/skills/blob/082e9752fa806dbd358f07c7f8f73f3eda55600e/skills/channel-brain/MASTER_ORDERS.md#L151), [L205](https://github.com/mooneyn60-art/skills/blob/082e9752fa806dbd358f07c7f8f73f3eda55600e/skills/channel-brain/MASTER_ORDERS.md#L205)). | PASS | PASS |
| **Y9** Advertiser-friendly | PASS. Nothing graphic: clipboard icon cards, "no gag near the 'can lead to death' line", and organs that never swell or bleed. YouTube cuts: mild words only. | PASS | PASS |
| **C1** Facts sourced, live | PASS. CH-F1 to F14 all matched live. F1-3 is wording, not a source error. | PASS. DB32/33, DL-F1 to F8, UNV-1 to UNV-4 matched live. | PASS on the sources. **FIX F3-2 and F3-3**: hedges were dropped in two spoken lines. |
| **C2** No invented winners or verdicts ([MO L66](https://github.com/mooneyn60-art/skills/blob/082e9752fa806dbd358f07c7f8f73f3eda55600e/skills/channel-brain/MASTER_ORDERS.md#L66), [L139 r7](https://github.com/mooneyn60-art/skills/blob/082e9752fa806dbd358f07c7f8f73f3eda55600e/skills/channel-brain/MASTER_ORDERS.md#L139)) | PASS. "Show both; don't pick a side." "Meatball called. The rest is the vet's call." Nothing says a tactic saved Noodle. | PASS. The tail is "a lean, not a rule". "Never say dogs 'know'." | PASS. |
| **C3** Safety conditions kept ([MO L139 r3](https://github.com/mooneyn60-art/skills/blob/082e9752fa806dbd358f07c7f8f73f3eda55600e/skills/channel-brain/MASTER_ORDERS.md#L139), [L222](https://github.com/mooneyn60-art/skills/blob/082e9752fa806dbd358f07c7f8f73f3eda55600e/skills/channel-brain/MASTER_ORDERS.md#L222)) | **FIX F1-2.** | PASS. AKC: "calmly remove your attention … four paws on the floor", with no knee, shove or grabbing paws. Tufts keeps "frequent". | PASS. "Never punished." No trim tip (UNV-5 cut, and iCatCare says "isn't advisable"). The AAHA/AAFP "new or unusual" wording is kept. |
| **C4 / C8** Jokes add no claim, pet claims hedged ([MO L118](https://github.com/mooneyn60-art/skills/blob/082e9752fa806dbd358f07c7f8f73f3eda55600e/skills/channel-brain/MASTER_ORDERS.md#L118), [L139 r1–2](https://github.com/mooneyn60-art/skills/blob/082e9752fa806dbd358f07c7f8f73f3eda55600e/skills/channel-brain/MASTER_ORDERS.md#L139)) | PASS. The new staging adds "no gag near the 'can lead to death' line". The rulers stay a units gag with no conversion. | **WATCH W-C4** (unchanged). The new "40×" staging is fine. "they're all aimed at your shoes" (cold open) puts a behavior claim inside a fact line. The sandwich payoff right after "lip-smacking can also mean a snack is expected" implies a motive. | PASS. The iCatCare reading gets "probably" on "your cat". |
| **C5** Logos and betting | PASS | PASS | PASS |
| **C6** Lane ([MO L137](https://github.com/mooneyn60-art/skills/blob/082e9752fa806dbd358f07c7f8f73f3eda55600e/skills/channel-brain/MASTER_ORDERS.md#L137), [L170](https://github.com/mooneyn60-art/skills/blob/082e9752fa806dbd358f07c7f8f73f3eda55600e/skills/channel-brain/MASTER_ORDERS.md#L170)) | PASS on topic (pets), **HOLD** on format, slots and title (see Approval). | same | same |
| **C7** Banned words, Short length | PASS. No banned words. Shorts 16–18 s. | PASS | PASS |
| **T1** ≥1 min ([US Terms §2](https://www.tiktok.com/legal/page/global/creator-rewards-program-us/en); [MO L201](https://github.com/mooneyn60-art/skills/blob/082e9752fa806dbd358f07c7f8f73f3eda55600e/skills/channel-brain/MASTER_ORDERS.md#L201)) | PASS. TikToks are 65–75 s. | PASS | PASS |
| **T2** The minute is new content, no padding or loops ([EEA Terms](https://www.tiktok.com/legal/page/global/tiktok-creator-rewards-program-eea/en)) | **WATCH.** The chapter 5 source window is only 7:55–8:25 (30 s), so a 65 s TikTok needs about 35 s of newly written beats (the listed CH-F1, F7, F10). Never slow, loop or hold frames. | WATCH. Chapters 4 and 5 have 60 s windows. | **WATCH.** The chapter 5 window is 45 s. |
| **T3** Original, not reposted ([CG Integrity](https://www.tiktok.com/community-guidelines/en/integrity-authenticity): "unoriginal or reused material without anything new") | PASS. | **FIX F2-1** (the TikTok half). | **FIX F3-1** (the TikTok half). |
| **T4** No engagement bait | PASS. One question per cut. | PASS | PASS |

---

## Fixes

### EP 1, chocolate

**F1-1 (Y1, blocks): two chapter Shorts duplicate drafted Shorts.**
- Chapter 1 Short: "Your dog ate one ounce of 70 to 85 percent dark chocolate. That's about 227 milligrams of theobromine." Body: milk 57.
  - It duplicates `chocolate-v6-yt.json` line 4: "Dark chocolate, 70 to 85 percent cacao, has about 227 milligrams an ounce, it says; milk chocolate, about 57."
  - It also duplicates Claude's `dog-chocolate-v6-yt.json` line 1: "Dark chocolate can have about four times the theobromine of milk."
- Chapter 2 Short: "Your dog's line? The FDA says theobromine can cause mild signs as low as 9 milligrams per pound of body weight." Body: severe around 18.
  - It duplicates `chocolate-v6-yt.json` line 3, and Claude's Short #72's title and line 3 ("FDA says mild signs can start at nine milligrams…").
- **Action:** drop the chapter 1 and 2 Shorts. Keep the chapter 3, 4 and 5 Shorts (3 Shorts, per [MO L229](https://github.com/mooneyn60-art/skills/blob/082e9752fa806dbd358f07c7f8f73f3eda55600e/skills/channel-brain/MASTER_ORDERS.md#L229)). Keep the chapter 1 and 2 **TikToks**: they carry new units and sources and no TikTok twin exists.
- **Alternative:** Social Studio retires `chocolate-v6-yt` (12/01 slot) and asks Claude to hold #72, and the chapter Shorts replace them. Pick one; don't ship both.

**F1-2 (C3, blocks): the safety card on ingestion cuts is the wrong one.**
- Offending: chapter 4 Short: "Your dog ate chocolate an hour ago and looks fine. The FDA says signs can take a few hours." It uses CH-F6 as the loop card. Chapter 2, 4 and 5 TikToks also close on "CH-F6 clean".
- CH-F6 (FDA) is conditional: "If your pet is sick or has a veterinary emergency, call your veterinarian." After "looks fine", that reads as "wait until he's sick".
- The source that matches the scenario is CH-F10 (ASPCA, live): "if you suspect your pet has eaten any of the following foods, please note the amount ingested and contact your veterinarian or poison control at (888) 426-4435." The APCC page adds: "A consultation fee may apply."
- **Replacement loop card (chapter 4 Short) and closing safety line (every EP 1 TikTok):** "ASPCA: if you think your dog ate chocolate, note the amount and contact your vet or animal poison control, (888) 426-4435. A consultation fee may apply." It is said clean. CH-F6 may follow it, not replace it.
- **Rule for EP 1:** every cut that opens on "your dog ate…" carries CH-F10.

**F1-3 (Y6/C1, blocks): the white-chocolate wording overstates the sources.**
- Offending:
  - 5:00 beat: "No page we opened calls any amount safe."
  - Chapter 3 Short hook: "You think white chocolate is the safe one for your dog. Nobody we read calls it safe."
- UC Davis (opened live) says white chocolate amounts "are negligible, so it is not considered toxic to pets." A viewer hears "nobody calls it safe" as contradicting that.
- **Replacement, chapter 3 Short hook (10 words):** "Your dog ate white chocolate. The ASPCA says almost no theobromine."
- **Replacement, chapter 3 body:** "UC Davis says it's not considered toxic. The ASPCA says some dogs may react to the sugar and fat, and any chocolate may lead to pancreatitis."
- **Replacement, 5:00 beat line:** "UC Davis: not considered toxic. ASPCA: some dogs may still react to the sugar and fat. Not toxic isn't a free pass." The last sentence is the show's framing, said by Meatball, not credited.

**F1-4 (Y3): RESOLVED in pass 2.** The Animator staging (slate @ 062d62f, "EP 1 signs (6:00–7:15)" and "EP 1 chemistry") now says what pass 1 asked for. Keep it binding on every EP 1 chapter cut and on the render check.
- Optional, no longer blocking: reframe the chapter 4 Short hook as a question, "How long after chocolate do dog symptoms start? Three sources, three clocks." (11 words). The F1-2 card fix is still required.
- The chapter 3 hook in F1-3 can stay as written.

**F1-5 (Y1, blocks): the comment question is lifted.**
- Offending (8:45 beat): "What's the worst thing your dog ever stole off the counter?" It is word for word the closing question of Claude's dog-chocolate Short #72 ("What's the worst thing your dog stole off the counter?").
- **Replacement:** "Where do you hide the chocolate from your dog?"

### EP 2, dogs lick

**F2-1 (Y1/T3, blocks): chapters 3 and 4 re-run the drafted dogs-lick Short and TikTok.**
- Chapter 3 Short hook: "You call it a kiss. Penn Vet says your dog's lick is a greeting." It duplicates `dogs-lick-v6-yt.json` ("Why do dogs lick you? Penn Vet says it is not a kiss." / "Licking a person or another dog is a greeting behavior…").
- Chapter 4 Short hook: "…That's a different signal." It duplicates that Short's last line: "Lip licking is a different signal, Penn Vet says."
- The chapter 3 and 4 TikToks (DL-F1, F2, F3, F4, F6, F7, F8) are the same fact set, in the same order, as the 73 s `tt-dogs-lick.json`.
- **Action:** pick one of these.
  - (a) Retire `dogs-lick-v6-yt`, `tts-dogs-lick` and `tt-dogs-lick`. The EP 2 chapters replace them.
  - (b) Drop the chapter 3 and 4 Short and TikTok. Then EP 2 ships the chapter 1, 2 and 5 Shorts (3 per [MO L229](https://github.com/mooneyn60-art/skills/blob/082e9752fa806dbd358f07c7f8f73f3eda55600e/skills/channel-brain/MASTER_ORDERS.md#L229)) and the chapter 1, 2 and 5 TikToks.
- Never post both versions of the same TikTok fact set: same account, "reused material without anything new".

**F2-2 (Y1, blocks): a gag is lifted from the drafted Short.**
- Offending: 3:30–4:15 "Meatball leans in for a kiss" plus 5:30–6:30 "Noodle ends up with Meatball's sandwich". It reuses `dogs-lick-v6-yt.json` line 2: "Meatball puckered up. His dog, Noodle, got the damn sandwich."
- **Replacement payoff:** "Noodle ends up with Meatball's **house keys**". This pays off the key-in-the-lock cold open, and it is an action with no motive.
- The pucker can stay as a setup only if the drafted Short is retired (F2-1 option a).

**W-C4 (watch):**
- Cold open, "…and they're all aimed at your shoes" becomes: "Behind that door is a nose with up to 100 million or more scent receptors, depending on the breed. Meatball's shoes are about to be read."
- Keep the snack line and the payoff at least one beat apart, so the payoff isn't heard as Noodle's motive.

### EP 3, cats knead

**F3-1 (Y1/Y5/T3, blocks): chapters 1–4 re-run the drafted cats-knead Short and TikTok.**
- Chapter 1 Short (CK-F1 + CK-F6) is the same pair as `cats-knead-v6-yt.json`: "Kittens tread with alternate front paws…" plus "Emma Grigg at UC Davis says it is most likely carried over from their days as kittens."
- The chapter 1–4 TikToks (CK-F1 to F7) re-split the 89 s `tt-cats-knead.json`. That file already has every one of those facts plus the fluffy-cushion and never-punish lines.
- **Action:** as in F2-1, pick one.
  - (a) Retire `cats-knead-v6-yt`, `tts-cats-knead` and `tt-cats-knead`.
  - (b) Drop the chapter 1 Short, ship the chapter 2, 3 and 5 Shorts, and ship TikToks only for chapter 5 plus one combined "kneading" TikTok that `tt-cats-knead` doesn't already cover. There isn't enough unused kneading material for 4 new minutes.
- Long-form: the episode is fine as its own video, but it re-covers the TikTok's facts. Its added value has to come from new picture and the organ scenes, with no gag lifted from the TikTok (oven mitts, "Meatball kneaded the pillow himself", "Sauce already had the fluffy cushion").
- The 7:45 payoff (Sauce kneads Meatball, Noodle sleeps in the fancy bed) is new: keep it.

**F3-2 (C1/Y6, blocks): the cold-open hedge was dropped.**
- Offending: "…its paws are running a move it learned as a kitten."
- The source (Grigg, UC Davis, live) says "most likely carried over from their days as kittens". "Learned" is a new claim and drops the hedge.
- **Replacement:** "…and its paws are running a move that most likely started when it was a kitten."

**F3-3 (C1/Y6, blocks): the 3 AM hook needs its condition.**
- Offending: chapter 5 Short hook "It's 3 AM and your cat is wide awake. Cornell says cats are naturally more active at dawn and dusk." 3 AM is neither dawn nor dusk, so the pairing implies an explanation the source doesn't give.
- Cornell (live) continues: "Depending upon the cat, this may mean that your kitty might wake you up to play in the middle of the night."
- **Replacement hook (11 words):** "Your cat wakes you at night? Cornell: cats are naturally crepuscular."
- **Body:** "More active at dawn and dusk. Depending on the cat, that may mean waking you in the night." Keep UNV-7's condition: "Senior cats exhibiting new or unusual behavior should be evaluated for medical conditions."
- Apply the same condition to the 7:00–7:45 "Why 3 AM?" beat.

**F3-4 (Y1, blocks): the comment question is lifted.**
- Offending: "Where does your cat knead: you, a blanket, or never?" It is near-identical to `tt-cats-knead.json`'s close: "Does your cat knead you, a blanket, or both?"
- **Replacement:** "What time does your cat start kneading you?" This fits the 2:56 AM frame.

### Series (watch, no block)

**W-Y2: vary the shared skeleton.**
- EP 2 midpoint becomes: "Then comes the lick. Meatball is about to get this one very wrong."
- EP 2 7:30–8:00 Sauce beat ("doesn't come to the door … walks off. No cat claim") is the third "Sauce walks off" in three episodes and carries no fact. Cut it (EP 2 runs about 8:00), or give Sauce a different action, for example Sauce takes Meatball's spot on the couch.

---

## C1 evidence: live source re-read by QA (Mon 11/16/2026, about 7:05–7:20 PM ET)

| Rows | Page (HTTP) | Quote matched |
|---|---|---|
| CH-F1–F6 | FDA, https://www.fda.gov/animal-veterinary/animal-health-literacy/leave-chocolate-out-rovers-celebrations (200; "Content current as of: 04/29/2024") | "two compounds that are toxic to dogs, theobromine and caffeine"; "the theobromine that's the main culprit"; table "Milk chocolate 57 … Dark chocolate with 70-85% cacao 227 … Unsweetened baking chocolate 364"; "as low as 9 mg per pound … around 18 mg per pound"; "within a few hours"; "can lead to death in some cases"; "some dogs may also develop … pancreatitis"; "If your veterinarian is unavailable, call your local emergency animal hospital or an animal poison control center." |
| CH-F7, F8 | ASPCA, https://www.aspca.org/news/what-do-if-your-pet-gets-chocolate (200) | "it will take less dark chocolate to pose a problem"; "White chocolate has almost no theobromine, but some dogs may be sensitive to the amount of sugar and fat…"; "Cats are sensitive to theobromine just like dogs"; "less likely to consume larger quantities". |
| CH-F9, F10 | ASPCA people-foods, https://www.aspca.org/pet-care/aspca-poison-control/people-foods-avoid-feeding-your-pets (200); APCC, https://www.aspca.org/pet-care/animal-poison-control (200) | "abnormal heart rhythm"; "baking chocolate and cocoa powder have the highest concentrations"; "note the amount ingested and contact your veterinarian or poison control at (888) 426-4435"; "A consultation fee may apply." |
| CH-F11, F12 | Merck, https://www.merckvetmanual.com/toxicology/food-hazards/chocolate-toxicosis-in-animals (200; "Last updated: Feb 2026") | mg/kg thresholds; "usually occur within 6-12 hours after ingestion". |
| CH-F13, F14 | UC Davis SVM, https://healthtopics.vetmed.ucdavis.edu/health-topics/chocolate-poisoning-dogs (curl 403; opened with the fetch tool) | "not considered toxic to pets"; "can begin 2-24 hours after ingestion"; "showing signs of anxiety, agitation or vomiting, consult a veterinarian immediately". |
| DB32, DB33 | AKC, https://www.akc.org/expert-advice/training/why-does-my-dog-sniff-everything/ (200) | "Humans have only 5-6 million scent receptors … Depending on the breed, dogs have up 100 million or more … Bloodhounds have 300 million!"; "the smelling section of a dog brain is 40 times larger than ours". |
| DL-F1–F3 | Penn Vet PDF, https://www.vet.upenn.edu/wp-content/uploads/2024/12/dogbodylanguagebasics-pdf.pdf (200) | "not a 'kiss'. This is a greeting behavior, but if dog licks someone repeatedly, he may be anxious about that dog or person"; "Dog licks his lips: anxiety about a situation or interaction"; "Dogs do not kiss either, and they may be frightened by kissing." |
| DL-F4, UNV-4 | Tufts, https://vet.tufts.edu/news-events/news/anxiety-dogs (200) | "Anxious dogs may also appear extra friendly and continually approach, jump on someone, and lick their face, or just be needier"; "Dogs exhibiting frequent anxious behavior should see their veterinarian as soon as possible." |
| DL-F6 | AAHA 2015, https://www.aaha.org/resources/2015-aaha-canine-and-feline-behavior-management-guidelines/common-signs-of-anxietydistress/ (200) | "Lip licking Nose licking" in the list of common signs. |
| DL-F7/F8 | Texas A&M, https://stories.tamu.edu/news/2025/03/13/understanding-your-dogs-body-language-a-guide-to-canine-communication/ (200) | "Licking lips - often accompanied with yawning"; "lip smacking can also indicate a self-soothing method for stress or anticipation of a snack". |
| UNV-1 | AKC, https://www.akc.org/expert-advice/training/stop-dog-jumping/ (200; "Updated: Sep 14, 2026") | "When your dog jumps, calmly remove your attention … four paws on the floor"; "avoid putting your knee up". |
| UNV-2 | Leonetti et al. 2024, Biology Letters, PMC10792393, Europe PMC full text (200) | "Dogs exhibit a right-side wagging bias … (e.g. when shown their owner or a familiar person)"; "Tail wagging is frequently associated with both positive and negative arousal". |
| UNV-3 | Rehn & Keeling 2011, https://research.slu.se/en/publications/the-effect-of-time-left-alone-at-home-on-dog-welfare/ (200) | "Twelve privately owned dogs"; "more intense greeting behaviour … already after 2 h of separation". |
| CK-F1–F5, UNV-5 cut | iCatCare, https://icatcare.org/articles/why-do-cats (200; updated 26 Sep 2025); https://icatcare.org/articles/trimming-your-cats-claws (200) | "treading with alternate front paws … to stimulate the flow of milk"; "associate your relationship with that of their mother"; "Some cats … dribble"; "a few will retain it into adulthood … fluffy cushion or blanket"; "cats should never be punished"; "Routine trimming of a cat's claws isn't advisable". |
| CK-F6/F7 | UC Davis, https://www.ucdavis.edu/magazine/6-common-cat-behaviors-explained (curl 403; opened with the fetch tool; 19 Apr 2021) | "most likely carried over from their days as kittens"; "it's a self-soothing behavior. With humans, it's almost like a sign of the bond". |
| UNV-6 | Cornell FHC PDF, https://www.vet.cornell.edu/sites/default/files/What%20to%20expect%20when%20adopting%20a%20feline%20friends%20-%20Accessible.pdf (200) | "naturally crepuscular, meaning that they are more active during dawn and dusk. Depending upon the cat, this may mean that your kitty might wake you up to play in the middle of the night." |
| UNV-7 | AAHA/AAFP 2021, https://www.aaha.org/resources/2021-aaha-aafp-feline-life-stage-guidelines/behavior-and-environmental-needs-senior-cats/ (200) | "Senior cats exhibiting new or unusual behavior should be evaluated for medical conditions." |
| UNV-6b (pass 3) | iCatCare "What is a cat?", https://icatcare.org/articles/what-is-a-cat (200) | See "UNV-6b / UNV-7b" in Pass 3: exact, hedges kept, PASS. |
| UNV-7b (pass 3) | AAHA/AAFP 2021, same page (200) | Exact; FIX for framing (E3-1). |

**UNV status:** UNV-1, 2, 3, 4, 6 and 7 are now sourced, and the slate's wording matches the live pages. UNV-5 is correctly cut. Not verified by QA:
- The Quaranta et al. 2007 primary paper (Research couldn't open it either). UNV-2 rests on the 2024 review, so credit the review on screen, not "a 2007 study".
- The Tufts article date (4 May 2023). The page text matched, but I didn't confirm the date.

---

## Note: croc Short verdict (`shorts-push-1116-wmsw-ep1-saltwater-crocodile.md`, Fix 1)

Research (`channels/research/sourcing-slate-wk1-1116.md`, section B) proposed a different line from QA's: **"Verdict: seized in the water? Little chance of escaping without serious injury, if at all. Nothing's guaranteed."** QA accepts either line.
- Research's line quotes the Australian Museum source (CB50) more closely and is fine to ship.
- QA's line, "Verdict: grabbed in the water? Probably seriously hurt. Nothing's guaranteed.", is shorter. Timing: Research's line is 16 words against 8 now, so the Short becomes 64 words / about 19.7 s at 194.5 wpm. That's inside the 16–20 s lint band but over the 52–58-word aim. QA's line gives 58 words / 17.9 s. If Research's line is used, re-run the timing lint and keep it under 20.05 s.
- With either line, keep the Queensland attack figures out of the verdict stamp (Research's point). If they're used at all, they go in the description with their own page credit.
