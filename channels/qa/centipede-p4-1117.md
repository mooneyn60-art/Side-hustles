# QA: House centipede Part 4 (TikTok)

## Verdict: PASS (with flags)

**Run:** Tue 11/17/2026, about 8:00–8:05 AM ET (America/New_York), against `channels/team/playbooks/research-qa.md` (55000aa), `channels/qa/checklist.md` C1–C12 / Y1–Y9 / T1–T5, MASTER_ORDERS in mooneyn60-art/skills @ 082e975 (`skills/channel-brain/MASTER_ORDERS.md`), and the Part 4 brief in `TASKS.md` @ 4afee0d.

**Branch taken:** script and render found (not the pre-source path). Nothing was in `channels/scripts/` or `channels/renders/` of this repo. Claude's `channels/claude/status.md` (@ d5abb97, 7:45 AM ET) pointed to the skills repo, branch `claude/youtube-monetization-strategy-m9vz6i`:

- Script: `skills/oh-meatball/scripts/drawn-house/tt-house-centipede-p4.json` (commit 5364af2, "House centipede Part 4: checked, rendered 65.6 s, voice and lint pass")
- Render: `skills/oh-meatball/episodes/drawn-house/tt-house-centipede-p4.mp4` — ffprobe **65.63 s**, 1080×1920, drawn stick-figure Meatball / tiled bathroom (Part 2 look, as the brief ordered)
- Contact sheet: `skills/oh-meatball/episodes/drawn-house/sheets/house-centipede-p4-tt.jpg`
- Claude fact pack / second-model check: `skills/oh-meatball/research/facts/house-centipede-p4.md` and `house-centipede-p4-check.md`

The render was transcribed this run and diffed against the script. Claude's eight wording fixes are in the audio and on the cards. Every source URL was fetched live this morning (all HTTP 200). The Acosta PDF is a scan: quotes below are from the page images (pp. 3–4), not the garbled text layer.

**Counts:** 11 sourced fact beats **PASS**, **0 FIX**, **0 CUT**. Title and caption claims PASS. Overall **PASS with flags** (none is a blocking fact error). Confirm the Metricool AI label and that a new Part 5 will actually post Wed 11/18 7 PM ET before this airs at 7 PM today.

Title: `House Centipede Part 4 🐛`  
Scheduled: TikTok Tue 11/17 7 PM ET (status.md; posted.csv uuid 7918539842414070977; `tiktok_title` "House Centipede Part 4: Guinness Speed, Leg Floss and Back Holes").

---

## Fact lines

| # | Spoken / card | Verdict | Live quote and note |
|---|---|---|---|
| 1 | "You just saw a bug Guinness listed among the fastest arthropods." Card: GUINNESS BOOK, 1973 / AMONG THE FASTEST ARTHROPODS | **PASS** | Acosta 2003, p. 4: "They have been clocked at 420 mm/sec with a 33 mm stride, which was impressive enough to be listed as among the fastest arthropods in the 1973 Guinness Book of World Records." Voice says "listed among," not "made the record." Year is on the card at the same beat, not in the voice. FLAG 1. |
| 2 | "Clocked at about sixteen inches a second. Close to one mile an hour." Card: ABOUT 16 INCHES A SECOND / CLOSE TO 1 MPH | **PASS** | Same Acosta sentence (420 mm/s = 16.54 in/s = 0.94 mph). MSU Extension, Bug's Eye View No. 29 (2015): "They are also able to run much faster than most other ground-dwelling arthropods, reaching speeds approaching one MPH." "About" and "close to" keep the hedges. Card keeps "ABOUT." |
| 3 | "It darts, sometimes stops dead, and can freeze for a while." Card: RUN. STOP. FREEZE. / THEN IT'S GONE | **PASS** | University of Arkansas Arthropod Museum: "The house centipede is often seen darting across floors at high speed, occasionally stopping suddenly and remaining motionless for some time before racing off once more." "Sometimes" holds "occasionally"; "for a while" holds "for some time." |
| 4 | "It catches its food by half pouncing, half lassoing." Card: HALF POUNCE / HALF LASSO | **PASS** | Arkansas: "They capture prey by half pouncing and half lassoing them." "Food" for "prey." The same Arkansas paragraph has the "several prey at once" fact already used in the 11/15 cut; this line uses only pounce/lasso. |
| 5 | "It can run up your walls to hunt." Card: UP YOUR WALLS / TO HUNT | **PASS** | University of Kentucky Entomology ef645: "To aid in hunting, house centipedes can run very quickly across floors and up walls." Voice and card say walls, not ceilings. No opened source says ceilings. |
| 6 | "Unlike most centipedes, it has well-developed, faceted eyes." Card: FACETED EYES / RARE FOR A CENTIPEDE | **PASS** | Arkansas: "Unlike most other centipedes, house centipedes and their close relatives have well-developed, faceted eyes." Acosta p. 3: "The well-developed compound eyes of scutigerids are unique among Chilopoda." "Rare for a centipede" matches "unlike most" / "unique among Chilopoda." "Big" was correctly removed. |
| 7 | "On a strict schedule, it pulls each leg through its mouthparts. Like floss." Card uses LEG FLOSS / ON A STRICT SCHEDULE | **PASS** | Acosta p. 3, citing Le Moli and Parmigiani 1976 and Verhoeff 1938b: "House centipedes meticulously groom themselves on a strict schedule (Le Moli and Parmigiani 1976). The antennae and legs are gripped by the forcipules and passed through the cleaning setae on the first maxillae (Verhoeff 1938b)." P. 4: grooming runs "legs 1 through 15 of the same side," so "each leg" holds. First maxillae are mouthparts; "through its mouth" would be wrong. "Like floss" is a simile, not a claim. These rest on one 2003 NKU review of older papers (see FLAG 4). |
| 8 | "It even tries to clean legs it doesn't have anymore." Card: CLEANS MISSING LEGS / IT STILL TRIES | **PASS** | Acosta p. 4: "Grooming behavior appears to be genetically hard-wired because house centipedes will still attempt to clean legs that have been amputated." "Tries" / "IT STILL TRIES" keep "attempt." |
| 9 | "It breathes through holes down the middle of its back." Card: BREATHES THROUGH / HOLES IN ITS BACK | **PASS** | Acosta p. 3: "The seven tergites each bear a median dorsal spiracle for gas exchange, unlike the lateral paired spiracles of other myriapods." Tergites = back plates; dorsal = on the back; median = down the middle; spiracle = breathing opening. Voice keeps "down the middle"; the card is a fair short form. |
| 10 | "Moms lay eggs one at a time, in soil." Card: EGGS IN SOIL / ONE AT A TIME | **PASS** | Acosta p. 3, citing Lewis 1981, read on the page image (the verb is "lay," not lost): "Females lay relatively few eggs (average four eggs per day; Lewis 1981), singly in soil. Laying and hatching occurs from late spring through early summer." Arkansas: "Eggs are laid in spring and early summer." "One at a time" = "singly." "Moms" is casual for "females." The four-eggs-per-day figure and season are not used, and must not be. |
| 11 | "A male that just molted is especially vulnerable to being eaten by a female." Card: JUST MOLTED? / FEMALES MAY EAT HIM | **PASS** | Acosta p. 4: "Newly molted male house centipedes are especially susceptible to predation by females." "Vulnerable" matches "susceptible"; "MAY" keeps the hedge. Not "likely" and not "always." |

Jokes (trophy bought online; walk to the fridge; "Meatball froze too. Still frozen."; lasso / own foot; "checked his walls. Hell, no!"; "eyes need coffee"; "Meatball skips the legs he has"; "breathes through his mouth"; Noodle digging; "Meatball cancelled his date"): **PASS** under C4. None adds a number, danger, animal motive, or safety instruction. "Cancelled his date" is Meatball's date, not a mating claim about the centipede.

Close: "So, does the speedy roommate stay, or get squished?" is a question, not advice. End line is the Studio-ordered Part 5 CTA. No ending says a tactic saved Meatball (Rule 7 / C3).

### Caption, sentence by sentence

`tiktok_caption`: "house centipede part 4 🐛 the 1973 Guinness Book of World Records listed it among the fastest arthropods. It has been clocked at about 16 inches a second, close to one mile an hour. It can stop dead and freeze, catches its food by half pouncing, half lassoing, and has well-developed, faceted eyes, which most centipedes do not. On a strict schedule it pulls each leg through its mouthparts, and it even tries to clean legs it no longer has. It breathes through holes down the middle of its back. Meatball tried a lasso once and caught his own foot. Missed Part 2? It is on our page: the 30-legged bug that hunts the roaches in your house. Creepiest one: 🦵 leg floss or 🕳️ back holes? #housecentipede #bugsinhouse #thingslivinginyourhouse #centipede #meatballmyths"

All sourced sentences **PASS** (same quotes as above). "30-legged" is 15 pairs (Arkansas, UKY, MSU); it is a pointer back to Part 2, not a new main fact. "Hunts the roaches" is supported by UKY ef645: house centipedes "feed on a variety of arthropods within the home, including (but not limited to) cockroaches, crickets, pillbugs/sowbugs, and silverfish." One genuine question. No #fyp, no swears, no brand/betting tags.

---

## Originality vs Parts 1–3 (and other posted centipede cuts)

Compared the Part 4 script and render to:

- Part 1 TikTok (`house-centipede-tt.json` / `tt-house-centipede.mp4`, posted 10/27 as "A 30-Legged Hunter Lives in Your House 🐛 (Part 1)")
- Part 2 TikTok, the viral cut (`house-centipede-2-v2-tt.json` / `tt-house-centipede-2-v2.mp4`, posted 11/1 as "Never Squish the 30-Legged Bug in Your House 🐛 (Part 2)")
- Part 3 TikTok (`house-centipede-3-tt.json` / `tt-house-centipede-3.mp4`, posted 11/2 as "Turn On Your Bathroom Light at 3 A.M. 🐛 (Part 3)")

The eight Part 4 facts are **new** as punchlines. Parts 1–3 used: 15 pairs / 30 legs; feelers that look like legs; "fast runner" or "one of the fastest things in your house" with no number; venom fangs and "almost never" stings if grabbed; the prey list; night hunting; hides in basements, cellars and bathrooms; hatches with four pairs and adds legs at each molt; about three years to grow up, up to seven years; the female's back legs; dry out the damp; harmless / don't bother spraying. Part 4's speed *number* and 1973 Guinness listing, dart-stop-freeze, pounce/lasso, walls-to-hunt, faceted eyes, scheduled grooming / missing-leg floss, back spiracles, eggs laid singly in soil, and newly molted males are not in Parts 1–3.

Also checked two later already-posted cuts, because the playbook requires a check against earlier posts, not only Parts 1–3:

- 11/7 TikTok `tt-house-centipede-4-v6.mp4`, title "House Centipede: 150 Babies From One in Your Bathroom 🐛" (not titled "Part 4"): 150 young, autotomy, drains, cardboard, Mediterranean / PA 1849, outdoor summer hunting along walls, bite rare. No overlap with this Part 4's main facts. "Hunt outside, right along your walls" is a different claim from "run up your walls to hunt."
- 11/15 TikTok `tt-house-centipede-5.mp4`, title "House Centipede: The Leg It Drops and Where It Hides": drop/regrow a leg, body size, catch several at once, hide spots, lots of them may mean lots of other bugs, bite like a bee sting. No overlap with this Part 4's main facts. **Naming clash:** that file is already called "centipede-5" but was not titled "Part 5." See FLAG 2.

Shared series format, not a fact repeat: the "stay or squish?" close also ends Part 2 and the 11/15 cut. Y1 allows a shared outro when the bulk differs. Logged as WATCH (FLAG 3), not a FIX.

---

## Checklist

| Row | Result | Note |
|---|---|---|
| Y1 | PASS (WATCH) | New facts, new gags, new payoff. Shared "you just saw" sequel hook and stay/squish close are series format. WATCH: FLAG 3. |
| Y2 | PASS | Close is a question plus a Part 5 CTA, not a stock "Meatball lived" ending. |
| Y3 | PASS | Drawn, calm animal; no distress, rescue, or gore. |
| Y4 | N/A | Not long-form. |
| Y5 | PASS | Original Meatball commentary on every fact beat; all visuals drawn for this cut. |
| Y6 | PASS | Hook (Guinness listing / speed) is paid off in the body; title does not overclaim. |
| Y7 | PASS | Meatball does not pose as an expert. Advice is not given. |
| Y8 | PASS (upload step) | Fully drawn, non-realistic. House rule still keeps the AI label on. See T5. |
| Y9 | PASS | No gore. Mild words only, all after 7 s. |
| T1 | **PASS** | Rendered length **65.63 s** (house rule ≥61 s; clean/sweary boundary, but only mild words). |
| T2 | PASS | Reaches 61 s with new sourced beats and gags. `loop` is false; no freeze-frame padding. |
| T3 | PASS | All in-house drawn animation and narration. No Duet/Stitch/Photo Mode. |
| T4 | PASS (Studio override) | Caption has one genuine question. No follow-for-follow or "comment X to…". Spoken/on-screen "Follow so you don't miss it" is the 11/17 7:00 AM ET Studio end-line order in TASKS.md. |
| T5 | **WATCH — confirm before post** | House rule: AIGC label ON. Could not open the Metricool scheduled post (uuid 7918539842414070977) from this box. Status.md does not record the label. Confirm it is on before 7 PM ET. |
| C1 | **PASS** (11/11 fact beats) | Live quotes above. No invented citations. |
| C2 | PASS | No invented winner. "Stay or squish?" is a question. |
| C3 | PASS | No stripped safety absolute. No "never bite." No ending says a tactic saved Meatball. |
| C4 | PASS | Jokes land on Meatball (or Noodle, the show dog). |
| C5 | PASS | No logos, teams, or betting. |
| C6 | **PASS** | Bug episode explicitly approved by Moondog88 in TASKS.md, 11/17 7:00 AM ET ("BUILD NOW"). TikTok Part series allowed by Social Studio override @ 4d63a90. House Guests / bug override f370db4 also on the books. |
| C7 | PASS | Title avoids TRUE/FALSE, Myth, Believe, Cartoons, Lied, "Did you know." This is a 65 s TikTok, not a 16–20 s Short, so the Short fact-count rule does not apply; it has eight sourced facts. |
| C8 | PASS | No unhedged "your pet" study claim. |
| C9 | PASS | Comedy leads; a joke on almost every fact beat, well inside 5–7 s. |
| C10 | **PASS** | First 7 s (0.00–7.00): hook + trophy + start of the speed line. No profanity. Title, caption, and cards are clean. Burned-in captions never show "damn" or "hell" (at the "Hell, no!" beat the caption is "NO!"). |
| C11 | PASS | Mild words after 7 s: "damn" ~21.8 s, "Hell, no!" ~25.8 s (ASR heard "Heh, no" / caption "NO!"; script is "Hell, no!"), "Damn" ~40.9 s. Fits mild-words-OK on a 65.6 s cut. No slurs, nothing sexual. |
| C12 | PASS | None. |
| Creature in frame 1 | PASS | House centipede is on the tiled bathroom wall at 0.00 s, with the caption "YOU JUST SAW." |
| Cartoon / style | PASS against the brief | Stick-figure Meatball, tiled bathroom, Part 2 look. Brief said do not switch to the new cartoon kit for this cut. |
| Voice | PASS (spec) | Script is `en-US-AndrewMultilingualNeural`, rate +15%, pitch +3 Hz, as ordered. |
| Rule 7 | PASS | Ending is the stay/squish question and the Part 5 CTA. |

Render/script diffs (not fact FIXes): ASR consistently heard the last line as "Follow us so you don't miss it," while the script and the on-screen card say "Follow so you don't miss it." Cards and captions match the checked script, including the eight wording fixes.

---

## Flags (not blocking; act before 7 PM ET)

1. **1973 is on the card, not in the voice.** The hook is still accurate ("listed among the fastest arthropods"). Optional polish: say "in 1973" aloud so a muted-off viewer hears the edition.
2. **Part 5 CTA is only true if a new Part 5 posts Wed 11/18 7 PM ET.** Status.md says it will be built tonight for that slot, and asks Studio whether the series continues to Part 6. An older file, `tt-house-centipede-5.mp4`, already posted 11/15 under the title "House Centipede: The Leg It Drops and Where It Hides" (not "Part 5"). Do not let the new Part 5 collide with that title, and do not air this CTA if Wednesday's post slips.
3. **Stay-or-squish close** also ends Part 2 and the 11/15 cut. Shared series format; bulk of this video is new. WATCH, not a rewrite.
4. **Grooming, back spiracles, and newly molted males** rest on one authoritative source: Acosta 2003, a Northern Kentucky University review in the *Journal of the Kentucky Academy of Science*, hosted on NKU's site, citing older papers (Verhoeff 1938, Le Moli and Parmigiani 1976, Lewis 1981) that were not opened this run. Speed, eyes, pounce/lasso, walls, and egg timing have a second university or extension page.
5. **T5 AI label** must be confirmed on the scheduled TikTok before post.

---

## Sources opened live this run (all HTTP 200, 11/17/2026 morning ET)

- Acosta, C. A. (2003), "The House Centipede (*Scutigera coleoptrata*; Chilopoda): Controversy and Contradiction," *J. Ky. Acad. Sci.* 64(1):1–5. PDF on the author's NKU page: https://websites.nku.edu/~acostac/AcostaJKAS2000.PDF (the filename says 2000; the scan is Volume 64, Spring 2003). Quotes from page images 3–4.
- Mississippi State University Extension, Bug's Eye View, House Centipede, No. 29 (2015): https://www.accessibility.extension.msstate.edu/newsletters/bugs-eye-view/2015/house-centipede-no-29
- University of Arkansas Arthropod Museum, House centipede: https://arthropod.uark.edu/house-centipede/
- University of Kentucky Entomology, fact sheet ef645, "Centipedes and Millipedes in and Around the Home" (Gordon, Larson, DeVries): https://entomology.mgcafe.uky.edu/ef645
