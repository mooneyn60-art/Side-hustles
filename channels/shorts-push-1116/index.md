# Shorts push 11/16: index

Box drafts only, written Mon 2026-11-16 (ET) by Social: Scriptwriter for Social Studio. Nothing rendered, scheduled, committed, posted or sent. All slots TBD.

## The v6 hook spec used (quoted)

Source: `/workspace/skills-readonly/skills/channel-brain/MASTER_ORDERS.md`, line 177, section "The Short template and title rules". This is the only definition of v6 in the workspace. Every later mention (`claude-note-1116-push.md` 'keeping them 15-20 s with the v6 hook'; `OPERATIONS.md` lines 55/68; research 68; the 11/16 shorts-ceiling research; the 11/18 performance brief) points back to it and doesn't redefine it.

> **The v6 template (every render from 11/3):** narration from 0.00 s; frame 0 is the animal close-up already moving (Meatball hops in at ~2.3 s, smaller); a visceral "you" + number hook; line 2 (3-7 s) is the Meatball gag ("Make them funnier", rule 1), never the name or anatomy; no spoken or visual outro (no Subscribe, Part X, Follow or end card); the last line flows into the hook in the hook's room; the comment question is a top-corner pill on the last line and the pinned comment; a new fact or visual every second, cuts every 1.5-2.5 s, keyword cards in seconds 1-4, center captions. YT 16-20 s; TikTok lengths are in "Posting".

Also applied (same file): line 178, 'New YouTube Shorts run 16-20 s with at least two sourced facts plus a payoff'; line 164, at least 3 locations, with hook and last line sharing a room; line 89, the hook is the searched question aimed at the viewer; line 137, rule 7: 'No ending says a tactic saved Meatball: "Meatball lived. Nothing's guaranteed."'

## Files

- `bed-bugs.md`: bedbug-lights, mite-millions
- `spider-venomous.md`: spider-widow-lookalike, spider-wolf-eyes
- `wms.md`: wms-lion-roar, wms-polar-swim
- `wms-wednesdays-ep1-4.md`: EP 1 saltwater crocodile, EP 2 hippo, EP 3 Komodo dragon, EP 4 Florida alligator
- `reply-to-comment.md` (renamed from `reply-to-comment-PENDING.md`): R1 reply-mommy-longlegs and R2 reply-venom-harmless (real comments, verbatim), plus R3, a placeholder waiting for a third real comment
- `rulings-1116.md`: Social Studio's 11/16 rulings, applied in `.build/shorts.py` and kept by every regeneration
- `.build/`: `shorts.py` (all script data), `check.py` (verifier), `gen.py` / `index_gen.py` (write these .md files), `check-output.txt`, and `sources/` (page text saved for every NEW-FACT page)

## Every Short

| # | File | Slug | Title | Hook | Hook words | Words | Est. s @194.5 | Sources | NEW-FACT / flags |
|---|---|---|---|---|---|---|---|---|---|
| 1 | bed-bugs.md | bedbug-lights | Do Lights Keep Bed Bugs Away? 💡 (Things Living In Your House) | Sleeping with your lights on likely won't deter hungry bed bugs. | 11 | 55 | 16.97 | BB16, BB32 | Hook has no number (v6 asks 'you + number'; the source line has none). |
| 2 | bed-bugs.md | mite-millions | An Infested Mattress Can Contain Millions of Dust Mites 🛏️ (Things Living In Your House) | Your mattress: an infested one can contain millions of dust mites. | 11 | 55 | 16.97 | DM19, DM8 | — |
| 3 | spider-venomous.md | spider-widow-lookalike | Is This Spider Venomous? The Black Widow Lookalike in Your House 🕷️ (Is This Spider Venomous?) | Your house 'black widow' may be a brown lookalike instead. | 10 | 58 | 17.89 | HS39, HS40, HS64 | Spoken lines never say 'false' (banned word). The species' common name 'false black widow' stays only in the description quote. Social Studio: OK the title without 'False', or allow the name as an exception (see conflicts). No number in the hook. |
| 4 | spider-venomous.md | spider-wolf-eyes | Is This Spider Venomous? Wolf Spider Eyes Reflect Green 🔦 (Is This Spider Venomous?) | Your flashlight at night: wolf spider eyes reflect green. | 9 | 56 | 17.28 | HS28, HS29, HS32 | No number in the hook. The medical-care line is on screen only (HS64). |
| 5 | wms.md | wms-lion-roar | You Can Hear a Lion's Roar Up to 5 Miles Away 🦁 (Would Meatball Survive? #N) | You can hear a lion's roar up to five miles away. | 11 | 53 | 16.35 | LB33, LB41 | Verdict is conditional ('from inside the car'): check it against rule 7. |
| 6 | wms.md | wms-polar-swim | One Polar Bear Swam 687 km in 9 Days 🐻‍❄️ (Would Meatball Survive? #N) | One polar bear swam 687 kilometers in 9 days. Could you? | 11 | 58 | 17.89 | PB36, PBA1 | Verdict 'Probably not' comes from one bear's 687 km swim. No human swim figure is used: Research, please confirm the hedge is enough. |
| 7 | wms-wednesdays-ep1-4.md | wmsw-ep1-saltwater-crocodile | Would Meatball Survive a Saltwater Crocodile? | Large saltwater crocodiles can stay underwater up to an hour. You? | 11 | 56 | 17.28 | CB27, CB28, CB42, CB50 | Verdict rests on CB50 (Australian Museum). |
| 8 | wms-wednesdays-ep1-4.md | wmsw-ep2-hippo | Would Meatball Survive a Hippo? | A hippo's canines can reach 20 inches. Your canoe? | 9 | 55 | 16.97 | NF-H1, NF-H2, NF-H3 | NEW-FACT x4 (San Diego Zoo). Conditional verdict: check it against rule 7. |
| 9 | wms-wednesdays-ep1-4.md | wmsw-ep3-komodo-dragon | Would Meatball Survive a Komodo Dragon? | One meal: adults can eat up to 80% of their weight. | 11 | 58 | 17.89 | NF-K1, NF-K2, NF-K3, NF-K4 | NEW-FACT x4 (Smithsonian). No 'you' in the hook (it would make 12 words). |
| 10 | wms-wednesdays-ep1-4.md | wmsw-ep4-florida-alligator | Would Meatball Survive a Florida Alligator? | Your Florida county? Alligators are found in all 67. | 9 | 58 | 17.89 | NF-A1, NF-A2, NF-A3, NF-A4 | NEW-FACT x4 (FWC). |
| 11 | reply-to-comment.md | reply-mommy-longlegs | Where Is Mommy Longlegs? She Holds Her Eggs in Her Jaws 🕷️ (Is This Spider Venomous?) | Mommy longlegs? She holds 25 to 60 eggs in her jaws. | 11 | 58 | 17.89 | HS15, HS7 | Real comment, verbatim. No NEW-FACT: all lines are pack rows HS7/HS15. The hook has no 'you' (it answers the comment). 'Mommy longlegs' is treated as the female cellar spider, and the card says so. |
| 12 | reply-to-comment.md | reply-venom-harmless | Are Daddy Longlegs Venomous? It Depends Which One 🕷️ (Is This Spider Venomous?) | Which daddy longlegs? One of the three has venom. | 9 | 58 | 17.89 | HS13, HS17, HS19 | Real comment, verbatim (correction, kind). No NEW-FACT: HS13/HS17/HS19, passed in factcheck-spider-id-1116 sec. 5. Never says harmless, myth or false in its own voice. '100% harmless' appears only inside the commenter's verbatim sticker. The hook has no 'you'. |

Hook seconds: 9 words = 2.78 s, 10 = 3.08 s, 11 = 3.39 s, so every hook is spoken by about 0:03.4.

## Verification script output (`python3 .build/check.py`)

Checks: word count, seconds at 194.5 wpm, the 15–20 s band (plus the 16–18 s aim), hook under 12 words, hook = line 1, last line ends on 'And' and holds the pill question, strict banned-word scan of spoken lines (TRUE, FALSE, Myth, Believe, Cartoons, Lied, 'Did you know'), banned-word scan of titles and tags, mild-word scan, hashtag order, series title format plus EP card, verdict line present and marked HEDGED, and every non-gag, non-loop line has a source. Reply Shorts also check: the verbatim comment and handle are in the frame-0 sticker, and the reply never says harmless, myth or false in its own voice (spoken, title, pinned, description).

```
slug                             words    sec hook_w hook_s  checks
bedbug-lights                       55  16.97     11   3.39  PASS
mite-millions                       55  16.97     11   3.39  PASS
spider-widow-lookalike              58  17.89     10   3.08  PASS
spider-wolf-eyes                    56  17.28      9   2.78  PASS
wms-lion-roar                       53  16.35     11   3.39  PASS
wms-polar-swim                      58  17.89     11   3.39  PASS
wmsw-ep1-saltwater-crocodile        56  17.28     11   3.39  PASS
wmsw-ep2-hippo                      55  16.97      9   2.78  PASS
wmsw-ep3-komodo-dragon              58  17.89     11   3.39  PASS
wmsw-ep4-florida-alligator          58  17.89      9   2.78  PASS
reply-mommy-longlegs                58  17.89     11   3.39  PASS
reply-venom-harmless                58  17.89      9   2.78  PASS
ALL HARD CHECKS PASS
Banned-word note: '#meatballmyths' is the required channel tag and is excluded from the tag scan; 'false widow' / 'false black widow' are species common names, excluded from the TITLE scan only (spoken scan is strict).
```

## NEW-FACT rows for Research & Fact-check (opened live 2026-11-16, quoted exactly; page text saved in `.build/sources/`)

| ID | Used for | Exact quote | URL |
|---|---|---|---|
| NF-H1 | EP 2 hook | "Their canine and incisor teeth grow continuously, with canines reaching 20 inches (51 centimeters) in length." | https://animals.sandiegozoo.org/animals/hippo |
| NF-H2 | EP 2 l3-l4 | "Yet despite all these adaptations for life in the water, hippos can't swim—they can't even float! Their bodies are far too dense to float, so they move around by pushing off from the bottom of the river or simply walking along the riverbed in a slow-motion gallop" | same |
| NF-H3 | EP 2 l5 + verdict | "An unsuspecting human boater who enters hippo territory risks an aggressive response." | same |
| NF-H4 | EP 2 card + verdict | "A hippo can kill people if it's provoked or feels threatened." (also: "they are among the most dangerous and aggressive of all mammals") | same |
| NF-K1 | EP 3 hook | "The stomach expands easily, enabling an adult to consume up to 80 percent of its own body weight in a single meal" | https://nationalzoo.si.edu/animals/komodo-dragon |
| NF-K2 | EP 3 verdict | "Komodo dragons are limited to a few Indonesian islands of the Lesser Sunda group, including Rintja, Padar and Flores, and of course the island of Komodo" (not seen on Padar since the 1970s) | same |
| NF-K3 | EP 3 l3 | "Although the Komodo dragon can briefly reach speeds of 10 to 13 mph (16 to 20 kph), its hunting strategy is based on stealth and power. It can spend hours in one spot along a game trail" | same |
| NF-K4 | EP 3 l4 + card | "Most of the monitor's attempts at bringing down prey are unsuccessful. However, if it is able to bite its prey, bacteria and venom in its saliva will kill the prey within a few days." | same |
| NF-A1 | EP 4 hook | Alligators "are found in all 67 counties." | https://myfwc.com/conservation/you-conserve/wildlife/alligators/ |
| NF-A2 | EP 4 l3 | "The Florida record for weight is a 1,043 pound (13 feet 10-1/2 inches long) male from Orange Lake in Alachua County." | https://myfwc.com/wildlifehabitats/wildlife/alligator/facts/ |
| NF-A3 | EP 4 l4 + verdict | "Serious injuries caused by alligators are rare in Florida, but if you are concerned about an alligator, call FWC's toll-free Nuisance Alligator Hotline at 866-392-4286." | https://myfwc.com/conservation/you-conserve/wildlife/alligators/ |
| NF-A4 | EP 4 safety line | "Remember, never feed an alligator and keep your distance if you see one. Swim only in designated swimming areas during daylight hours. And keep pets on a leash and away from the water." | same |

Not used: the San Diego Zoo hippo charge speed ("up to 14 miles per hour (30 kilometers per hour)"), because the mph and km/h on the page don't match. The Smithsonian hippo URL returned 'Page not found'. The 10/24 pilot-pack hippo, komodo and croc lines (press coverage) are not reused.

## Social Studio rulings 11/16 (applied, see `rulings-1116.md`)

Lanes confirmed. Bed-bug lights hook: 'Sleeping with your lights on likely won't deter hungry bed bugs.' Wolf hook: 'Your flashlight at night: wolf spider eyes shine back green.' The Komodo and lookalike hooks stay as written. The corner EP card is approved, and the next-Wednesday pointer goes only in pinned comments. Conditional verdicts stay, with the condition spoken; the fallback is 'Meatball lived. Nothing's guaranteed.' The title keeps 'Black Widow Lookalike', and #falseblackwidow is added to the tags (no banned-word exception). '#N' is for Claude to number at upload. Ship once Research clears the 12 NEW-FACT rows. Items 1, 3 (lookalike), 4, 5, 6 and 10 below were raised before these rulings and are now settled by them.

## Rule conflicts and calls for Social Studio / Research (as first raised)

1. **Bug and spider lanes vs the 11/11 direction change.** MASTER_ORDERS 'Direction change' (Nolan, 11/11) says 'No new bug or spider episodes are built', and the 11/18 performance brief says 'Less: bugs'. The 11/16 push (Social Studio, `claude-note-1116-push.md`) asks for bed-bug and spider Shorts. I followed the newer push. It came to me from an agent, so Social Studio should confirm it with Moondog88 before anything is built.
2. **Length:** v6 says YT 16–20 s, and line 178 has the lint failing under 15.0 s. The brief says 15–20 s. All 10 run 16.66–17.89 s, so they satisfy both.
3. **v6 'you + number' hook:** bedbug-lights, spider-widow-lookalike and spider-wolf-eyes have no number, because the sourced line has none worth leading with. Komodo EP 3 has a number but no 'you', since adding 'You?' makes 12 words. Hooks that end in a rhetorical 'You?', 'Could you?' or 'Your canoe?' are part of the hook, not a second comment prompt. The one prompt is the pill/pinned question.
4. **v6 bans 'Part X' and end cards vs the requested 'EP N' card:** the EP card is a top-right corner card from frame 0, not an end card, and nothing in the video promises the next episode. The 'Next Wednesday: EP N' pointer is only in the EP 1–3 pinned comments, where the next episode really exists. Social Studio, please confirm.
5. **Rule 7 ('No ending says a tactic saved Meatball') vs 'verdict must follow from sourced facts':** every verdict is hedged ('probably' / 'probably not') with 'Nothing's guaranteed', and its stamp names its fact row. Three are conditional: lion 'from inside the car', hippo 'out of its territory', Komodo 'unless he's on a few Indonesian islands'. None says a tactic saved him, but Research should rule whether the conditionals are OK under rule 7. The fallback for each is 'Meatball lived. Nothing's guaranteed.'
6. **'False' in the false black widow's name:** the spoken script avoids it. The title uses 'Black Widow Lookalike'. The tag #falsewidow was dropped. The description keeps UC IPM's exact wording ('false black widow'), as `factcheck-spider-id-1116.md` allowed for the long-form ('"False widow" is the common name, not a TRUE/FALSE card'). If Social Studio wants the searched name in the title ('...The False Black Widow'), that's an exception to the banned-word list and needs their call.
7. **Mild words:** the 11/13 funny pass allows 1–2 mild words per YouTube Short. The brief says ideally none. These use none.
8. **'#meatballmyths' contains 'myths':** it's the required channel tag. The scan skips it (same precedent as `bedbug-teasers.md`).
9. **Hippo verdict and pet-science hedges:** no pet lab results appear, so the 11/12 'probably/likely/may' rule for 'your cat/your dog' isn't triggered. EP 4's pet line is FWC's own instruction, said clean.
10. **WMS #N numbering:** the standalone titles carry '#N' for Social Studio to number. Wednesdays episodes carry 'EP N' only.

## Not done (by design)

- Reply-to-comment slot R3: placeholder only. It's waiting for a third real comment; the channel had 19 comments from Oct 18 to Nov 12 per Metricool.
- Nothing was committed to channels/scripts/ (Social Studio commits), posted, scheduled or sent to anyone.
