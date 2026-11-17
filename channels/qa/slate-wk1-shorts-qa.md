# QA: slate wk1, 9 chapter Shorts (timing copy)

**Reviewed:** `/workspace/scripts/slate-wk1-timing.md`, mtime **2026-11-16 19:26:35 ET**, 17,098 bytes, 236 lines, sha256 **bb8c0cd7f8f5**. It is byte-identical to side-hustles origin/main `channels/showrunner/slate-wk1-timing.md` @ **fc303e2** (19:27:13 ET, "pending QA").
**Against:** the passed slate, sha256 **34d2bc0ce392** (@ 93b38b5; still current on main), and `checklist.md` (Y1–Y9, C1–C8; T1–T5 are N/A for Shorts).
**Run:** Mon 11/16/2026, about 7:30 PM ET.
- Every fact was opened live this run with `src-slate/chk.py` (HTTP 200 unless noted). The two UC Davis pages return 403 to curl, so I opened them with the fetch tool.
- Word counts were recounted independently with check.py's `wc()` at 194.5 wpm.
- The 4 MASTER_ORDERS items stay out of scope.

## Verdicts

| Short | Words / s (QA recount) | Verdict | Fix |
|---|---|---|---|
| EP1 S1 white chocolate | 56 / 17.28 | **PASS** | staging note only |
| EP1 S2 three clocks | 58 / 17.89 | **PASS** | card label: Merck → "Merck Veterinary Manual" |
| EP1 S3 cats | 55 / 16.97 | **FIX** | S3-1: add the pinned "your pet" ingestion card |
| EP2 S1 scent receptors | 57 / 17.58 | **PASS** | |
| EP2 S2 jump | 56 / 17.28 | **FIX** | (a) line 2 re-cut; line 4 duplicates a drafted Short |
| EP2 S3 2 hours | 57 / 17.58 | **FIX** | (b) full hedge sentence on the card |
| EP3 S1 drool | 58 / 17.89 | **FIX** | line 5 duplicates the drafted `cats-knead-v6-yt` Short |
| EP3 S2 bond | 54 / 16.66 | **PASS** | |
| EP3 S3 night | 52 / 16.04 | **FIX** (label only) | AAHA/AAFP card needs "2021" |

The Scriptwriter's figures are confirmed. All 9 Shorts are 16.04–17.89 s (inside 16–20 s), 52–58 words, with hooks of ≤11 words. Every per-line word count matches. No spoken credits, no banned words, one prompt, ends on "And".

## Match to the passed slate (34d2bc0ce392)
- The facts match the slate's chapter bodies. The hooks differ from the slate in EP1 S1, EP1 S3, EP2 S1, EP2 S2, EP3 S2 and EP3 S3. These come from Social Studio rulings 1–8, which are listed in the timing file (spoken credits moved to cards; "may not be pure joy" cut). They aren't slate edits, and the slate wasn't changed.
  - EP3 S2 now says "It's 'almost like a sign of the bond.'" with an "Emma Grigg, UC Davis" card, not the spoken "A UC Davis behaviorist:" from E3-2. The credit is still on screen while the quote plays, so C1 is fine.
- E2-2's line is word for word in EP2 S3, with no tail-wag line.
- EP3 S3 matches F3-3 word for word, and its AAHA/AAFP condition card is pinned.
- EP1's pinned ASPCA ingestion line (the "your dog" form) is on S1 and S2.

## Fixes (exact wording)

**EP1 S3-1 (C3).** The Short says chocolate "can still be dangerous" for cats but gives no action. ASPCA (live): "if your cat does eat chocolate, it is best to follow the above recommendations as well."
- Add the T5 pinned card, card only, with no spoken change: "ASPCA: if you think your pet ate chocolate, note the amount and contact your vet or animal poison control, (888) 426-4435. A consultation fee may apply."
- It needs 29 words / 9.67 s. Pin it 3.39–16.97 s plus the loop (13.58 s).

**EP2 S2-1 (C1/C8, question a).** Replace line 2 with: **"Anxious dogs may appear extra friendly: approaching, jumping on someone, licking faces."** (12 words). Card: "Tufts Cummings School of Veterinary Medicine, 2023".

**EP2 S2-2 (Y1).** Line 4, "If a dog licks someone repeatedly, he may be anxious about that dog or person.", is nearly the same sentence as line 3 of the drafted YouTube Short `dogs-lick-v6-yt` ("…if a dog licks someone repeatedly, he may be anxious about that person"). That draft is not retired. Replace line 4 with Tufts UNV-4 (live): **"Dogs exhibiting frequent anxious behavior should see their veterinarian as soon as possible."** (13 words). Card: "Tufts Cummings School of Veterinary Medicine, 2023".
- This also gives the Short the slate's safety condition.
- With S2-1, the Short is 8 + 12 + 9 + 13 + 13 = **55 words / 16.97 s**.

**EP2 S3-1 (C8, question b).** Hedge card text: **"Rehn & Keeling 2011: 'this study cannot distinguish between whether dogs were aware of the length of time they were alone (but did not signal it) or whether they were unaware until reminded of it by the return of their owner.'"**
- 40 words, so it needs 13.33 s at 3 words/s.
- Extend the pin from 1.85–13.57 s to 1.85–17.58 s plus the loop (15.73 s). No spoken change.

**EP3 S1-1 (Y1).** Line 5, "Kittens tread with alternate front paws to stimulate the flow of milk.", is the core line of the drafted YouTube Short `cats-knead-v6-yt` ("Kittens tread with alternate front paws on the mother's abdomen to stimulate the flow of milk"). That is the duplication F3-1 removed. Replace it with CK-F4 (iCatCare, live: "Cats grow out of this behaviour when it ceases to be necessary, but a few will retain it into adulthood"): **"Cats grow out of it, but a few keep kneading as adults."** (12 words; still 58 / 17.89 s). Card: iCatCare.

**EP3 S3-1 (label).** The condition card's credit should be "(AAHA/AAFP 2021 Feline Life Stage Guidelines)". If that's too long, use "(AAHA/AAFP, 2021)".

**EP1 S2 (label).** "(Merck)" → **"(Merck Veterinary Manual)"**. On its own, "Merck" reads as the drug company.

## (a) EP2 S2, the Tufts DL-F4 line
Live text: Tufts Cummings School, "Anxiety in Dogs", May 4, 2023, by Stephanie Borns-Weil (board-certified animal behaviorist). Section "Warning Signs":
> "An anxious dog may pant, pace, tremble, drool, withdraw from its owner, or hide. Alternatively, they may appear irritable or aggressive… Their body carriage may be low and their manner hesitant or avoidant. **Anxious dogs may also appear extra friendly and continually approach, jump on someone, and lick their face, or just be needier with the owner.**"

Verdict: the line keeps "may" and is conditioned on "anxious dogs", so it doesn't state a feeling as fact. MO L139 rules 1–2 are met for the sentence on its own. **The cut is not acceptable as written:**
1. "also" now dangles, because its antecedent (the other warning signs) is gone.
2. Keeping only "jump on someone", straight after the hook "Your dog jumps on you at the door.", reverses Tufts' direction. Tufts says an anxious dog *may* show this cluster; the Short suggests that jumping alone may mean anxiety.

Use the S2-1 replacement, which keeps the whole cluster, drops "also" and keeps "may". The Penn Vet "repeatedly" line no longer carries the condition, because S2-2 replaces it. The Tufts vet line now does that job.

## (b) EP2 S3, the first clause of the hedge
SLU abstract (live; Rehn & Keeling, *Appl. Anim. Behav. Sci.* 129(2–4):129–135, 2011; "Twelve privately owned dogs"):
> "Although this study cannot distinguish between whether dogs were aware of the length of time they were alone (but did not signal it) or whether they were unaware until reminded of it by the return of their owner, it does confirm that dogs are affected by the duration of time at home alone."

**Yes, the first clause alone changes the meaning.** The authors' hedge is a two-way alternative. The second option is that the dogs only "remembered" at the owner's return, and that is the explanation that counters "your dog knows how long you were gone". Without it, the card reads as a vague doubt about awareness, and the main alternative is gone. Use the card text in S3-1. Leaving off the final "it does confirm…" clause is fine: it's a positive claim that the spoken lines already carry.

## (d) Source-card labels
| Label as written | Verdict | Use |
|---|---|---|
| ASPCA (EP1 S1, S3; ingestion card) | Approve | ASPCA |
| UC Davis (EP1 S1, S2 clock) | Approve (UC Davis School of Veterinary Medicine, Animal Health Topics, Nov 2, 2020) | UC Davis |
| "within a few hours" (FDA) | Approve | FDA |
| (Merck) | **Fix** | Merck Veterinary Manual |
| AKC (EP2 S1) | Approve | AKC |
| Tufts (Cummings School) | Approve; tidy | Tufts Cummings School of Veterinary Medicine, 2023 |
| Penn Vet | Approve, though line 4 is replaced by S2-2 | — |
| Rehn & Keeling 2011 | Approve. The year is correct: 2011 issue (©2010 Elsevier) | Rehn & Keeling 2011 |
| iCatCare | Approve | iCatCare |
| Emma Grigg, UC Davis | Approve (UC Davis Magazine, Apr 19, 2021) | Emma Grigg, UC Davis |
| Cornell Feline Health Center | Approve (the PDF is headed "Cornell Feline Health Center") | Cornell Feline Health Center |
| (AAHA/AAFP) | **Fix** | AAHA/AAFP, 2021 |
| 2007 / review | **N/A.** No Short carries the tail-wag claim (UNV-2 was removed from EP2 S3 by E2-2), and no "2007" appears anywhere in the file. The "credit the 2024 *Biology Letters* review" rule applies only to EP2 T3 and the long-form. | — |

## Facts opened live this run
| Fact | Source | Result |
|---|---|---|
| CH-F7, CH-F8 | ASPCA chocolate article | "almost no theobromine… may be sensitive to the amount of sugar and fat… may lead to… pancreatitis"; "Cats are sensitive to theobromine just like dogs… can be dangerous… Fortunately, cats lack sweet taste buds… tend to not be readily drawn" ✔ |
| CH-F13, UC Davis clock | UC Davis healthtopics (fetch tool) | "negligible, so it is not considered toxic to pets"; "can begin 2-24 hours after ingestion" ✔ |
| CH-F1, CH-F5 | FDA | "the main culprit in chocolate toxicity in dogs"; "can appear within a few hours" ✔ |
| CH-F12 | Merck | "usually occur within 6-12 hours after ingestion" ✔ |
| DB32, DB33 | AKC | "Humans have only 5-6 million… Depending on the breed, dogs have up 100 million or more"; "the smelling section of a dog brain is 40 times larger than ours" ✔ |
| DL-F4, UNV-4 | Tufts | as quoted in (a); "Dogs exhibiting frequent anxious behavior should see their veterinarian as soon as possible." ✔ |
| DL-F1 | Penn Vet PDF | "if dog licks someone repeatedly, he may be anxious about that dog or person" ✔ |
| UNV-3, E2-2 | SLU | "Twelve privately owned dogs"; "more intense greeting… higher frequency of physical activity and attentive behaviour… already after 2 h" ✔ |
| CK-F1, F2, F3, F4 | iCatCare "Why do cats…?" | all ✔. F2 drops "when they were a kitten"; that's OK. |
| CK-F7 | UC Davis Magazine (fetch tool) | "With humans, it's almost like a sign of the bond" ✔ |
| UNV-6 | Cornell PDF | "naturally crepuscular… more active during dawn and dusk. Depending upon the cat…" ✔ |
| UNV-7 | AAHA/AAFP 2021 | ✔ (pass 3) |

## Duplicates and staging
- **Duplicates:** `dog-nose` is retired, and both of its slots are struck on main (f8fdb43). The only Short-to-Short duplicates found are EP2 S2 line 4 and EP3 S1 line 5, fixed above. EP2 S1 still shares DB32 with the on-hold `longform-dog-bornas` (a long-form, so WATCH only). Nothing posted (`posted.csv`) overlaps; #67 is not touched.
- **Staging:** the timing copy has no visual notes, so the slate's named first shots and the Animator rules still govern. No script line conflicts with them.
  - EP1 S1 gag: show Noodle with the scale only, never with or eating the bar.
  - EP3 S1: the drool is one stylized blue drop.
  - No sick-dog acting; Meatball is the cartoon ball.
  - Gags are action-only on Meatball and the pets (Sauce is "she", which matches canon).
