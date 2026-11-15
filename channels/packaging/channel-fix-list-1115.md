# Channel packaging fix list — Sunday, Nov 15, 2026

**Draft only.** Do not edit live YouTube or TikTok. Do not git commit or push. Second-pass check notes are in this file; only the Apply list is ready to use. No new facts were invented. If a fact could not be taken from a fact pack, an episode script, or a locked packaging title, the original wording was kept.

Times are America/New_York (ET, UTC-5).

Studio export: YouTube Studio "Last 90 days," Aug 17–Nov 14, 2026, `/home/box/Downloads/meatball-myths-analytics-last-90-days/Table data.csv` (249 video rows + totals). Public yt-dlp and Metricool still sit under `/workspace/packaging/audit-1115/`. Metricool TikTok (`fureverfaces`) is ignored (Etsy / shop account). TikTok performance numbers will come from Claude later; YouTube is the focus here.

Baseline table: `/workspace/packaging/winners-baseline-1115.csv`.

---

## Summary

| Count | What |
|------:|------|
| **249** | Videos in the Studio 90-day table (plus a totals row not in the baseline CSV) |
| **99** | Meatball Myths videos in that window (86 Shorts, 13 long-forms). Channel-wide totals include 150 pre-rebrand videos (Joe Bartolozzi and earlier shorts) and should not be used for packaging decisions. |
| **77,595** | Meatball views in the export, on **39,268** thumbnail impressions, **3.25%** impression-weighted CTR. Channel-wide CTR is **2.49%** (307,224 views / 131,344 impressions) because pre-rebrand rows are mixed in. |
| **9** | Meatball long-forms **failing** the under-3% CTR trigger (new title + thumbnail the same day). Four long-forms **pass** CTR (the Don't-squish-it bug format, plus 6 Creatures on only 33 impressions). |
| **34** | Videos on the final Apply list that passed the second-pass check: **27 new titles** and **7 title-keep + sourced new thumbnails**. Description/Sources cleanups are attached to those items, not counted twice. |
| **11** | Proposed titles or conversions that failed or were deferred by the second-pass check (see that section). |

Nov 15 posts (How Mice, Shark Attacks) are not in the Studio export. Lightning and the Oct 27 Brown Recluse Short are in neither Studio nor the public uploads list.

---

## What wins (Meatball Myths only)

All figures below are from the Studio export, Meatball-era videos only (`era=meatball` in the baseline CSV). Thumbnail CTR on Shorts mainly measures browse/search/suggested surfaces, not the Shorts feed, so a Short can have low impressions and high views. Long-form CTR is the packaging signal that matters most.

**The format that actually clears the long-form bar**

- "Don't squish it" house-bug long-forms are the only Meatball long-forms with both a CTR above 3% and real impressions:
  - *3 Bugs in Your House You Should Never Kill (And 4 You Must)* — **5.44% CTR**, 1,856 impressions, 214 views, **42.71%** average viewed. This is the long-form to beat.
  - *Don't Kill the Spider in Your Corner. It Eats Bigger Spiders* — **4.63% CTR**, 1,771 impressions, 114 views, **22.33%** average viewed (CTR passes; retention does not).
  - *3 More Bugs…* — **4.37% CTR**, 1,510 impressions, 88 views, **23.68%** average viewed (CTR passes; 100-view bar missed; retention just under 25%).
- Every other long-form with 300+ impressions is under 3% CTR (median long-form CTR at 200+ impressions: **2.26%**; impression-weighted **2.85%**). Quiz, conspiracy, "How Wolves Became Dogs," and the house-cat born-as title are not winning clicks.

**Shorts title patterns (impressions ≥100 unless noted)**

| Pattern | n | Median CTR | Imp-weighted CTR | Median avg % viewed |
|---------|--:|-----------:|-----------------:|--------------------:|
| *Is This Spider Venomous?* series | 5 | 4.29% | **5.20%** | 97.3% |
| *Things Living In Your House* series | 25 | 3.38% | 3.88% | 76.7% |
| *Would Meatball Survive?* (not "I Tried to…") | 3 | 3.21% | 3.69% | 63.1% |
| "I Tried to…" WMS leads | 2 | 2.62% | 2.48% | 53.9% |
| No series tag | 12 | 2.76% | 3.77% | 65.9% |
| *Meatball Investigates* | 3 | 1.09% | **0.81%** | 51.7% |
| Banned-word titles (TRUE or FALSE / Lied / Cartoons / Believe / Myth) | 3 | 1.50% | **1.67%** | 55.5% |
| Clean titles (no banned words), imp ≥200 | 41 | 3.23% | **3.88%** | 70.6% |
| Hidden-creature leads ("This Bird/Spider…", "100 Feet…"), imp ≥200 | 9 | 3.54% | 3.59% | 89.2% |
| Named-creature leads, imp ≥200 | 34 | 2.94% | 3.87% | 68.5% |

Reading that table honestly: banned-word and Investigates titles lose clearly. Spider-identification titles win clearly. Hidden-creature hook tests can still get a healthy Shorts-feed CTR and retention, so renaming them is a **search** fix, not an automatic CTR rescue. Named leads have a slightly higher impression-weighted CTR once low-impression curiosities are set aside. A series tag is not a CTR magic trick by itself; *Things Living In Your House* wins on volume and solid mid-3% CTR.

**Best and worst individual CTRs (enough impressions to trust)**

Best Shorts, impressions ≥100:

- *The Spider on Your Window Is Watching You Back* — **10.54% CTR**, 522 impressions, 1,290 views, 54.81% viewed.
- *False Widow vs Black Widow in Your Kitchen* — **7.18%**, 515 imp, 1,030 views, 67.84%.
- *The Spider in Your Basement Hunts Black Widows* — **6.52%**, 706 imp, 1,124 views, 55.78%.
- *Are Daddy Longlegs the Most Venomous Spiders?* — **5.95%**, **2,118 imp**, 2,445 views, 96.6%. Highest-impression Meatball Short, and a question title. Do not retitle it without a pack; it is already a packaging winner.
- *This Spider Hides in Your Shoes…* (brown recluse) — **6.14%**, 228 imp, but only 48 views (browse is clicking; the Shorts feed is not pushing it).

Worst packaging (low CTR, enough impressions):

- *Is the Bermuda Triangle Real?* — **0.00% CTR**, 244 impressions, 432 views.
- *Do Elephants Drink Through Their Trunks Like a Straw?* — **0.00% CTR**, 168 impressions, 1,216 views (Shorts feed is carrying it; browse is dead).
- *What REALLY Crashed at Roswell?* — **1.09%**, 366 impressions, 27 views.
- *TRUE or FALSE: Goldfish Have a 3-Second Memory?* — **1.50%**, 200 impressions, 1,107 views.
- *Roaches Fit Through 2-Penny Cracks in Your Kitchen Walls* — **1.61%**, **869 impressions**, 969 views. Biggest Shorts browse miss after the long-forms. No sourced alternate title, so this is a thumbnail job.
- *The Bug You Squish Is Protecting You* — **1.69%**, 236 impressions, but **2,316 views** (Shorts-feed hit; browse thumbnail is weak). Naming the house centipede is for search and browse.

**Thumbnail style.** The export has no thumbnail-image labels, so style winners are inferred from the titles that click. High-CTR thumbs sit on named-spider confrontation videos (window spider, false widow vs black widow, cellar spider vs black widows) and on the Don't-squish-it long-forms. That matches the locked recipe: white or plain background, one huge drawn subject, 2–4 hand-lettered words with one red word, one hand-drawn arrow, no Meatball, readable at 168 px. Quiz / Investigates packaging is the loser (0–1.1% CTR).

---

## Long-forms vs the 72-hour bar

MASTER_ORDERS line 144: judged at 72 hours against CTR **4%+**, **100+** views, **35%+** average viewed. **Under 3% CTR → new thumbnail and title the same day.** Good CTR but under 25% viewed → rebuild the first 30 seconds. The parenthetical "now 2.5%" is the channel-wide performance note, not a lowered bar.

Studio figures are through Nov 14, 2026. The house-cat 72-hour read is still Monday, Nov 16, 2026, 5:00 PM ET, and the spider 72-hour read is Tuesday, Nov 17, 2026, 8:00 AM ET. Both already have enough impressions to read CTR.

### Fail the under-3% trigger (new thumbnail; new title only if a sourced one exists)

| Video | Posted | CTR | Imp | Views | Avg % viewed | 72h status | Title action | Thumbnail concept (`_a`, white bg, one huge subject, 2–4 words, one red word, one arrow, no Meatball, check at 168 px) |
|-------|--------|----:|----:|------:|-------------:|------------|--------------|-----|
| Your Life as a House Cat: 8 Ways It Goes Wrong (`viD-nbPdaxk`) | Fri 11/13 5:00 PM | **1.95%** | 1,439 | 42 | 24.17% | Inside the window; already fails same-day <3% | **Keep** the locked born-as post title. `Why It Sucks to Be Born as a House Cat` is in the script but cannot go on the post without Nolan's yes. | `_a` `YOUR LIFE AS A CAT` (already in `thumbnail-concepts.md`), red `LIFE` or `CAT`. One huge house cat, no Meatball. `_b` `RAW DEAL` (2 words; red `RAW`) from the script's RAW DEAL / SWEET DEAL meter. `_c` `LILIES CAN KILL` (3 words; red `LILIES` or `KILL`; "CAN" is the hedge) from fact pack 87 / the FDA lily page already in that pack. |
| Weird Animal Facts You Didn't Know (3 Are Fake. Can You Spot Them?) (`z-Kg8sXCxlU`) | Oct 26 | **1.82%** | **5,262** | 134 | **11.00%** | Past 72h. Also rebuild the first 30 seconds. | **Keep** the current title. No clean sourced alternate without quiz framing. | `_a` `3 ARE FAKE` (3 words; red `FAKE`) — those words are already in the title. One huge odd animal (not a quiz card). |
| Animals Thought Extinct Found Alive (One Was Hiding on a Rock for 80 Years) (`o9Emu9oMgCs`) | Oct 25 | **2.53%** | **3,438** | 126 | **15.85%** | Past 72h. Also rebuild the first 30 seconds. | **Keep** — this is already the episode script title. | `_a` `HIDING 80 YEARS` (3 words; red `HIDING`). One huge insect on a rock, from the script hook. Do not letter a species name that is not on the card's source line. |
| How Wolves Became Dogs (The Funny History of Man's Best Friend) (`Uqj0QL8G0d4`) | Oct 24 | **1.99%** | 1,558 | 163 | **20.42%** | Past 72h. Also rebuild the first 30 seconds. | **Keep** — only title in `history-01.json`. | `_a` `WOLF TO DOG` (3 words; red `DOG`). One huge wolf, arrow toward a smaller dog. Restates the kept title; no new fact. |
| Everything You Know About Animals Is WRONG (`gFhrONKK0rI`) | Oct 22 | **2.93%** | 750 | 43 | 41.80% (retention is fine) | Past 72h | **Keep**. The script's other title, *Animal 'Facts' Everyone Still Believes…*, fails the banned-word rule (`Believe`). | `_a` `GOT IT WRONG` (3 words; red `WRONG`), from the script's "got completely wrong" line. One huge ostrich head, not buried. |
| 12 Animal Myths You've Believed Your Whole Life (Disney Faked One) (`RwbgzQisvYM`) | Oct 23 | **1.25%** | 399 | 6 | **6.58%** | Past 72h. Also rebuild the first 30 seconds if revived. | **Keep** — no sourced title without Myth / Believed / TRUE or FALSE. | `_a` `DISNEY FAKED ONE` (3 words; red `FAKED`) — already in the current title. One huge drawn lemming or film-strip animal, no Meatball. |
| I Ranked Every Creature Living In Your House From Harmless to Deadly (`bqij8Ht6SX4`) | Nov 1 | **1.31%** | 305 | 5 | **9.92%** | Past 72h. Also rebuild the first 30 seconds if revived. | **New title from the script:** `Every Bug in Your House, Ranked From Harmless to Nightmare 🐛` | `_a` `HARMLESS TO NIGHTMARE` (3 words; red `NIGHTMARE`). One huge house centipede or recluse, not a grid of 17 bugs (will fail at 168 px). |
| Why the CIA Says "We Can Neither Confirm Nor Deny" (`4-gvZTWf2wg`) | Nov 5 | **0.67%** | 149 | 3 | 51.32% (retention is fine) | Past 72h | **New title from the script hook / already-posted teaser:** `The CIA Tried to Steal a Soviet Sub With a Giant Claw 🔍` | `_a` `GIANT CLAW` (2 words; red `CLAW`). One huge claw under a ship, white field. |
| Conspiracy Theories That Turned Out To Be TRUE (`2EC5LDtbUbo`) | Oct 27 | **0.87%** | 115 | 5 | 68.89% (retention is fine) | Past 72h | **New title from beat 0 of the script:** `The CIA Tried to Turn a Cat Into a Spy 🐱` | `_a` `SPY CAT` (2 words; red `SPY`). One huge cat, a small mic or wire, no Meatball. |

### Pass the 3% CTR trigger (do not swap the title)

| Video | CTR | Imp | Views | Avg % viewed | Notes |
|-------|----:|----:|------:|-------------:|-------|
| 3 Bugs in Your House You Should Never Kill (And 4 You Must) (`cH3HCZ8GlHk`) | **5.44%** | 1,856 | 214 | **42.71%** | Clears CTR, views, and the 35% viewed bar. Add a `Sources:` block from the script. Keep title and thumb. |
| Don't Kill the Spider in Your Corner. It Eats Bigger Spiders (`KWOM2-mNmww`) | **4.63%** | 1,771 | 114 | **22.33%** | CTR and views pass. Under 25% viewed → rebuild the first 30 seconds. 72-hour read Tue 11/17 8:00 AM ET. Add Sources; shorten the 35-character tag. |
| 3 More Bugs… (`xeAsg5ECpgw`) | **4.37%** | 1,510 | 88 | **23.68%** | CTR passes. Past 72h, missed 100 views, just under 25% viewed. Keep title/thumb; add Sources; first 30 seconds only if you keep promoting it. |
| 6 Creatures Living In Your House Right Now (`Lid8JXhg1Q4`) | **6.06%** | **33** | 3 | 23.36% | CTR passes on a tiny sample. This is a distribution problem, not a title problem. |

---

## Second-pass check

Each proposed new title or caption was re-reviewed against the locked title standard (statement form, searched words in the first 40 characters, hedge, one sourced fact, one emoji, series tag last when one already exists, ≤100 UTF-16 units, no banned words, pet lead, born-as "Your Life as a …" on the post), `postkit.py lint`, and the cited fact pack or episode script. A separate model was not available to call in this box, so this is a fresh checklist review of every proposal, not a rubber stamp of the first draft.

**Passed** (lint 0 FAIL on the title; source exists; standard held). These may go on the Apply list:

- Locked Shorts: cassowary (with live `#1`), Asian lady beetle (Penn State / `lady-beetle-v6-yt.json`), termite ("Wood" from `termite-yt.json`).
- Goldfish → exact script title in `myths-01-short-goldfish.json`.
- Ostrich → exact script title in `myths-01-short-ostrich.json`.
- Bulls → spoken line "Bulls don't hate the color red" from `myths-01-short-bull.json` beat 1 (see Failures for the script's own title).
- Ranked long-form → exact script title in `longform-house-bugs-ranked.json`, plus the required single emoji.
- CIA long-form → hook already in `longform-azorian.json` and on the posted teaser Short.
- Conspiracy long-form → beat 0 of `longform-turned-out-true.json` ("The CIA once tried to turn a cat into a spy").
- All "name the creature, keep the original fact" Shorts titles listed in the Apply list, including *The House Centipede You Squish Is Protecting You* (teaser script beat 2: "The bug you squish most is the one protecting you. The house centipede.").
- House-cat post title kept as locked; thumbnail words taken from the existing concept, the script meter, or fact pack 87.
- Long-form thumb cards whose words are already in the kept title or the cited script hook.

**Failed or deferred** (not on the Apply list):

1. `Bulls Can't Even See Red?! 🐂` — the episode's own script title. **FAIL** (question mark in the core). Revised to `Bulls Don't Hate the Color Red 🐂`.
2. `Why It Sucks to Be Born as a House Cat` as a replacement post title. **FAIL** without Nolan's yes (MASTER_ORDERS born-as + open ask 2).
3. `Animal 'Facts' Everyone Still Believes (That Are Completely Wrong)` as a replacement for *Everything You Know About Animals Is WRONG*. **FAIL** (`Believe` is banned).
4. `Your Dog's Guilty Look May Not Be a Confession: 14 Dogs Tested…` as a priority retitle. **DEFER.** Studio: **9.09% CTR** but only **11 impressions**, 3 views, 99.87% viewed. The title is not the problem; YouTube is barely showing the video. Fix distribution first. A pet-lead reorder remains optional later.
5. Converting *Are Daddy Longlegs the Most Venomous Spiders?* **FAIL** for apply. No pack, and it is the highest-impression Meatball Short at **5.95% CTR**.
6. Converting *Do Elephants Drink Through Their Trunks Like a Straw?* **FAIL** for a new title (no pack). Browse CTR is 0%; only a thumbnail, not a guessed verdict, may be applied later if a pack lands.
7. *Is the Bermuda Triangle Real?*, *What REALLY Crashed at Roswell?*, *Cartoons Lied To You About Porcupines*, *Disney Lied To You About Lemmings*, *Sharks in the RIVER?!*, *You STILL Believe This Camel Myth*, *Can Owls REALLY Spin Their Heads 360°?*, *12 Animal Myths You've Believed…* — **FAIL** for a new title (banned words and/or no sourced statement). Thumbnail-only is allowed where the words are already in the current title (12 Myths).
8. `Lightning Does Strike Twice ⚡ Case #6 Meatball Investigates` — **N/A.** The video is not in Studio or on the public channel.
9. TikTok caption drafts (Portia, cassowary) — **HELD** off the Apply list. YouTube is the focus; TikTok numbers will come from Claude later. Provisional hashtags were only placeholders.
10. Any description that would have invented a `Sources:` citation. Apply list says "copy Sources from the episode script," not a newly written bibliography.
11. Adding a series tag to early standalone Shorts where no series was assigned. **FAIL** (would invent a series).

---

## Apply list (passed only, priority order)

Exact old title → exact new title. Description/tag notes are included only where they were already checked on a full metadata pull. Do not apply anything that failed the second-pass check.

### A. Long-form packaging (CTR under 3%, real or decent impressions first)

1. **Your Life as a House Cat: 8 Ways It Goes Wrong** → **keep title.** New thumbnail: `_a` `YOUR LIFE AS A CAT`. CTR 1.95% on 1,439 impressions, 42 views, 24.17% viewed. 72-hour read Mon 11/16 5:00 PM ET. Description already has Sources and `#meatballmyths`; do not invent a new opening question.
2. **Weird Animal Facts You Didn't Know (3 Are Fake. Can You Spot Them?)** → **keep title.** New thumbnail: `_a` `3 ARE FAKE`. CTR 1.82% on 5,262 impressions. Also rebuild the first 30 seconds (11.00% viewed). Trim tags from 15 to 8–12; drop `#trueorfalse`; add `#meatballmyths`; add Sources from the script.
3. **Animals Thought Extinct Found Alive (One Was Hiding on a Rock for 80 Years)** → **keep title.** New thumbnail: `_a` `HIDING 80 YEARS`. CTR 2.53% on 3,438 impressions. Also rebuild the first 30 seconds (15.85% viewed). Trim 14 tags and the three over-30-character tags; add `#meatballmyths` and Sources.
4. **How Wolves Became Dogs (The Funny History of Man's Best Friend)** → **keep title.** New thumbnail: `_a` `WOLF TO DOG`. CTR 1.99% on 1,558 impressions. Also rebuild the first 30 seconds (20.42% viewed). Add `#meatballmyths` and Sources.
5. **Everything You Know About Animals Is WRONG** → **keep title.** New thumbnail: `_a` `GOT IT WRONG`. CTR 2.93% on 750 impressions. Retention is fine (41.80%). Trim 19 tags; drop `#didyouknow`; add `#meatballmyths` and Sources.
6. **Why the CIA Says "We Can Neither Confirm Nor Deny"** → **The CIA Tried to Steal a Soviet Sub With a Giant Claw 🔍** New thumbnail: `_a` `GIANT CLAW`. CTR 0.67% on 149 impressions. Retention is fine (51.32%). Add `#meatballmyths` and Sources from `longform-azorian.json`.
7. **I Ranked Every Creature Living In Your House From Harmless to Deadly** → **Every Bug in Your House, Ranked From Harmless to Nightmare 🐛** New thumbnail: `_a` `HARMLESS TO NIGHTMARE`. CTR 1.31% on 305 impressions, 9.92% viewed. Trim 13 tags; keep the existing Sources block; hashtags 3 topic + `#meatballmyths`.
8. **Conspiracy Theories That Turned Out To Be TRUE** → **The CIA Tried to Turn a Cat Into a Spy 🐱** New thumbnail: `_a` `SPY CAT`. CTR 0.87% on 115 impressions. Retention is fine (68.89%). Drop the 47-character tag; add `#meatballmyths`; Sources already present.
9. **12 Animal Myths You've Believed Your Whole Life (Disney Faked One)** → **keep title.** New thumbnail only if you revive it: `_a` `DISNEY FAKED ONE`. CTR 1.25% on 399 impressions, 6 views, 6.58% viewed. No sourced replacement title passed the check.

### B. High-impact Shorts (low CTR with impressions, or a 0% browse CTR plus a locked/sourced title)

10. **Several Colonies Eating Your House 🪵 (Things Living In Your House)** → **Termites Can Hollow a Beam While the Wood Still Looks Fine 🪵 (Things Living In Your House)** CTR **0.00%** on 59 impressions, 167 views. Locked title. Also give it a new white-bg thumb: `_a` `WOOD LOOKS FINE` (3 words; red `FINE` or `WOOD`), one huge hollow beam, from `termite-yt.json`.
11. **Roaches Fit Through 2-Penny Cracks in Your Kitchen Walls 🪳 (Things Living In Your House #53)** → **keep title.** New thumbnail: `_a` `2-PENNY CRACKS` (2 words; red `CRACKS`). CTR **1.61%** on **869 impressions**, 969 views. No sourced alternate title.
12. **TRUE or FALSE: Goldfish Have a 3-Second Memory? 🤔 #shorts** → **Your Goldfish Remembers You… It Just Doesn't Care 🐟** CTR 1.50% on 200 impressions, 1,107 views. Exact script title. Remove `#shorts` from the title; put 3 topic tags + `#meatballmyths` + `#shorts` in the description; drop `#trueorfalse` / `#didyouknow`.
13. **This Spider Hunts Other Spiders 🕷️ (Meatball vs Spiders #1)** → **A Portia Spider Hunts Other Spiders 🕷️ (Meatball vs Spiders #1)** CTR 2.50% on 759 impressions, 1,267 views. Same fact; names the creature (`short-portia.mp4`).
### C. Locked search titles (CTR is already fine; still apply the locked standard)

14. **This Bird Hides a 4-Inch Dagger Claw on Each Foot 🦶 (Would Meatball Survive? #1)** → **This Cassowary Has a 4-Inch Dagger on Each Foot 🦶 (Would Meatball Survive? #1)** CTR 5.34% on 206 impressions. Locked. Keep `#1`.
15. **10,000s of Bugs in Your Walls 🐞 (Things Living In Your House #44)** → **Asian Lady Beetles May Cluster in Your Walls for Winter 🐞 (Things Living In Your House #44)** CTR 4.64% on 453 impressions. Locked. Penn State / `lady-beetle-v6-yt.json`.

### D. Name the creature (keep the original fact). Search hygiene; several are already Shorts-feed hits.

16. **The Bug You Squish Is Protecting You 🐛 (Things Living In Your House)** → **The House Centipede You Squish Is Protecting You 🐛 (Things Living In Your House)** 2,316 views; browse CTR 1.69% on 236 impressions. Teaser script beat 2 names the house centipede.
17. **100 Feet a Night to Your Bed 🩸 (Things Living In Your House #41)** → **Bed Bugs Crawl 100 Feet a Night to Your Bed 🩸 (Things Living In Your House #41)** 1,860 views, 3.47% CTR on 202 impressions. Matches the already-posted TikTok title for the same file.
18. **4-Inch Spider Legs on Your Floor 🕷️ (Things Living In Your House)** → **A Giant House Spider: 4-Inch Legs on Your Floor 🕷️ (Things Living In Your House)** 1,281 views, 4.17% CTR on 144 impressions. File: `yt-giant-house-spider-hook`.
19. **150 Babies in Your Bathroom 🐛 (Things Living In Your House #37)** → **House Centipede: 150 Babies in Your Bathroom 🐛 (Things Living In Your House #37)** File: `yt-house-centipede-4-v6`.
20. **1 Fake Bug in Your Basement 🕷️ (Things Living In Your House #42)** → **A Cellar Spider: 1 Fake Bug in Your Basement 🕷️ (Things Living In Your House #42)** Script `cellar-spider-2-v6-yt.json`; original hook kept.
21. **30 Legs in Your Bathroom 🐛 (Things Living In Your House #45)** → **A House Centipede: 30 Legs in Your Bathroom 🐛 (Things Living In Your House #45)** File: `yt-meatball-centipede-explainer`.
22. **The Hairy Spider on Your Floor 🕷️ (Is This Spider Venomous?)** → **A Wolf Spider on Your Floor 🕷️ (Is This Spider Venomous?)** File: `yt-wolf-spider-hook`.
23. **This Caterpillar Turns Itself Into a Fake Snake 🐍** → **A Hawkmoth Caterpillar Turns Itself Into a Fake Snake 🐍** File: `yt-hawkmoth.mp4`. CTR 4.02% on 249 impressions.
24. **This Beetle Survives Being Run Over by a Car 🪲** → **An Ironclad Beetle Survives Being Run Over by a Car 🪲** File: `short-ironclad.mp4`.
25. **This Animal Fakes Its Own Death and Smells Like a Corpse 💀** → **An Opossum Fakes Its Own Death and Smells Like a Corpse 💀** File: `yt-opossum.mp4`.
26. **This Spider Went to Space and Kept Hunting (Is This Spider Venomous? #9)** → **A Jumping Spider Went to Space and Kept Hunting 🕷️ (Is This Spider Venomous? #9)** File: `jumping-spider-space.mp4`. Added the required single emoji only.
27. **This Bird Fakes a Broken Wing to Trick You 🐦** → **A Killdeer Fakes a Broken Wing to Trick You 🐦** File: `short-killdeer.mp4`.
28. **It Lives in Your Walls All Winter 🪲 (Things Living In Your House)** → **A Stink Bug Lives in Your Walls All Winter 🪲 (Things Living In Your House)** File: `yt-stinkbug-loop.mp4`.
29. **8 Legs Live In Your Pillow 😬 (Things Living In Your House #49)** → **Dust Mites: 8 Legs Live In Your Pillow 😬 (Things Living In Your House #49)** File: `yt-dustmites-explainer.mp4`.
30. **This Beetle Gets Swallowed by a Toad and Makes It Throw Up 🪲** → **A Bombardier Beetle Gets Swallowed by a Toad and Makes It Throw Up 🪲** File: `yt-bombardier-beetle.mp4`. CTR 0.79% on 127 impressions.
31. **The Hunchback Cricket in Your Basement 🦗 (Things Living In Your House)** → **A Camel Cricket in Your Basement 🦗 (Things Living In Your House)** File: `yt-camel-cricket-hook`; search name is camel cricket.
32. **This Spider Hides in Your Shoes and Its Venom Can Kill Skin 🕷️ (Is This Spider Venomous?)** → **A Brown Recluse Hides in Your Shoes and Its Venom Can Kill Skin 🕷️ (Is This Spider Venomous?)** File: `yt-brown-recluse-v4.mp4`. CTR already 6.14% on 228 impressions; this is a search-name fix. "Can" stays as the hedge.
33. **Ostriches / bulls banned-word Shorts** (low impressions; still rule breaks with sourced replacements):
    - **TRUE or FALSE: Ostriches Bury Their Heads in the Sand? 🤯 #shorts** → **Ostriches DON'T Bury Their Heads in the Sand 🤯** (`myths-01-short-ostrich.json`)
    - **Do Bulls Really Hate the Color Red? 🐂 TRUE or FALSE** → **Bulls Don't Hate the Color Red 🐂** (spoken line in `myths-01-short-bull.json`)

**Apply-list count: 34 videos.** 27 of them get a new title. 7 keep the title and get a sourced new thumbnail (house cat, Weird Animal Facts, Extinct, Wolves, Everything WRONG, 12 Myths, and *Roaches Fit Through 2-Penny Cracks*). *Is the Bermuda Triangle Real?* (0.00% CTR, 244 impressions) stays off the Apply list until a 2–4 word card line is taken from its own script — do not invent a slogan or a verdict.

### E. Keep doing, but not a title swap

- *3 Bugs* long-form: keep title and thumb (5.44% CTR, 42.71% viewed). Add Sources.
- *Don't Kill the Spider* long-form: keep title and thumb (4.63% CTR). Rebuild the first 30 seconds (22.33% viewed). Add Sources.
- *3 More Bugs:* keep title and thumb (4.37% CTR). Add Sources.
- Guilty-look Short (`xIbnhX10r7k`): **9.09% CTR, 11 impressions, 3 views, 99.87% viewed.** Fix or re-upload so YouTube will show it. Do not retitle first.
- How Mice and Shark (Nov 15) are not in this export; watch them in Studio after they age.
- `posted.csv` title `26` for the stink-bug cut is a CSV quoting bug. Live title is already `26,205 Stink Bugs in One House 🪲 (Things Living In Your House)` (1,035 views, 3.38% CTR). No live change.

---

## What could not be checked

- Studio rows after Nov 14 (How Mice, Shark Attacks) and any Nov 14 traffic after the export was cut.
- Lightning and the Oct 27 Brown Recluse Short (missing from Studio and the public channel).
- Per-video traffic sources (Search vs Browse vs Shorts feed vs Related). CTR here is thumbnail CTR only.
- Pinned-comment wording and live Related-video targets.
- Full descriptions and tags on Shorts that were not in the earlier 17-video pull.
- TikTok `@meatballmyths` performance (pending Claude; `fureverfaces` ignored).
- A second, separate model process (checklist review only, as noted above).

No live edits were made. No git commits or pushes were made.
