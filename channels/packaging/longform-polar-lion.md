# Long-form packaging: polar bear (Sat 12/5) and lion (target Sat 11/28, fallback Sat 12/12)

Draft only. No scheduling, posting, repo edits, or thumbnail file changes. Facts are from the packs cited below; nothing is invented. Times are America/New_York (ET).

**Resolved 11/15:** born-as every December Saturday per MASTER_ORDERS line 69. The schedule is polar 12/5, lion 12/12, then dog and wolf on 12/19 and 12/26 by data rank. Line 217 allows lion on 11/28 if it's ready by Thu 11/26. Scriptwriter's lion long-form now targets Sat 11/28, with 12/12 as the fallback. Line 217 still applies: 11/28 only if it is ready by Thu 11/26. If the lion takes 11/28, the 12/12 slot needs a different animal.

---

## Sources checked

- MASTER_ORDERS: line 69 ("Long videos"), line 217 (Watch hours queue: lion on 11/28 if ready by Thu 11/26), "Your Life as," no only-misery, Sucks needs Nolan's yes, The YouTube play (72-hour bar).
- `posted.csv`: Sat 12/5/2026 08:00 ET is **Your Life as a Polar Bear: 8 Things You Have to Get Through**, episode `longform-born-as-polar-bear`, file `born-as-polar-bear.mp4`. No 11/28, 12/12, 12/19, or 12/26 long-form rows yet.
- Born-as polar episode materials in the skills repo: `scripts/longform-born-as-polar-bear.json`, `scripts/longform-born-as-polar-bear.outline.json` (three titles and `_titles_note`). The built file is scheduled. **No polar long-form script is in `/workspace/drafts/`.**
- Research 98 (`98-polar-bear-life-factpack.md`, row IDs PB1–PB106), script check 99, on-screen/thumbnail check 101 (including `pb_a` / `pb_b` / `pb_c` wording).
- Research 85 (`85-longform-pets-survive-format.md`) and the 11/12 title-family addendum: **"Your Life as X" median 29,000 views** (29 videos, 5 channels, 59% over 10K) vs **"Why It Sucks to Be (Born as) X" median 4,150** (106 videos, 21 channels, 41% over 10K). **"Anything else": 0 of 13 over 10,000** (median 660).
- Research 100 (`data/100-longform-topic-candidates.csv`): lion is overall rank 1 in the S6 shape (demand 58, winnability 0.5, score 0.89). Dog is rank 2, wolf rank 3.
- Research 116 and `/workspace/drafts/facts/bears-vs-lions.md`: animals-not-teams fight facts. **Not** a "life as a lion" pack. Not used for lion titles or thumbnails here.
- Thumbnail recipe from research 85 addendum (white or plain background; one huge drawn animal; 2–4 hand-lettered words naming one specific curse; one word in red; a hand-drawn arrow; readable at 168 px). No Meatball in the thumbnail (MASTER_ORDERS / house-cat precedent).
- `episodes/thumbs-bornas/` and the `pb_a` / `pb_b` / `pb_c` image files were **not** in this sparse clone, so the images were not inspected this pass. On-image words are taken from research 101. The three files are locked as they are.
- Lion pack and script, delivered 11/15 (not edited here): `/workspace/drafts/facts/lion-bornas.md` (LB1–LB43, disagreements D1–D8) and `/workspace/drafts/longform-lion-bornas.md` (about 9:12; working title **Your Life as a Lion: 8 Things You Have to Get Through**). Teasers: `/workspace/drafts/lion-teasers.md`. Packaged teasers: `/workspace/packaging/lion-teasers.md`.
- Studio 11/15: no cub-killing on thumbnails or hooks.
- `postkit.py kw` also rerun 11/15 for the lion pack and teasers: `/workspace/packaging/kw/kw-lion-bornas-teasers.csv`. Extra suggestions: **"how long do lions sleep"**, **"how do lions catch their prey"**, **"lion hunting"**. The seed "how many lion cubs survive" also suggested "why lion kills cubs", which is not used (Studio barred cub-killing from hooks).
- `postkit.py kw` run 11/15 (YouTube + web suggestqueries). YouTube search (`--search`) did not run: `yt-dlp` is not installed. Rows: `/workspace/packaging/kw/kw-longform-polar-lion.csv`. Notable suggestions: **"your life as a polar bear"** and **"the life of a polar bear"**; **"polar bear cubs born"**; **"your life as a lion"**, **"your life as a lioness"**, **"life of a male lion"**, **"life of a lion pride"**. The phrase **"why it sucks to be born as a [animal]"** returned **no** YouTube suggestions (research 100 already noted the born-as phrase has no YouTube suggest volume).

---

## 72-hour bar (both videos)

From MASTER_ORDERS, The YouTube play, "How each long-form is judged at 72 hours (my thresholds, not Studio's)":

- Watch for **CTR of 4% or more**, **100+ views**, and **35%+ average viewed**, plus minutes a view against the current best (1.21).
- The parenthetical **"now 2.5%"** in that line is a current-performance note, not a lowered bar. The bar to watch remains **4%+**.
- **CTR under 3%:** new thumbnail and title **the same day**.
- Good CTR but **under 25% viewed:** rebuild the first 30 seconds.

For the polar video, 72 hours after the scheduled Sat 12/5/2026 08:00 ET start is **Tue 12/8/2026 08:00 ET**. Locked challenger thumbs `pb_b` and `pb_c` go into the post-publish A/B; they are not replacements for `pb_a` on the scheduled post.

If the lion posts on Sat 11/28/2026 at the usual Saturday 08:00 ET slot, 72 hours lands **Tue 12/1/2026 08:00 ET** (the same morning as the house-cat 72-hour read). If it stays on the Sat 12/12 fallback at 08:00 ET, 72 hours lands **Tue 12/15/2026 08:00 ET**. Neither start time is locked in `posted.csv`.

The house-cat 72-hour read on 12/1 decides what to fix in later born-as videos (first 30 seconds, title, thumbnail), not whether they run.

Studio A/B for long-form: `_a` on the post, `_b` / `_c` as challengers after it posts.

---

## Video 1 — Sat 12/5: polar bear

Scheduled. Script and outline already exist in the skills repo (about 10:30, preview sent 11/13). Facts from research 98; wording already cleared in research 99 and 101.

**Top title pick (already on the scheduled post):** Your Life as a Polar Bear: 8 Things You Have to Get Through

That is outline Title 3, the post title named in `_titles_note`, and the `posted.csv` title.

### Title options

Character counts are UTF-16 units, the way postkit and YouTube count them (no emoji in the born-as titles, so this matches ordinary character count). All five are statement form, under 100, "Polar Bear" inside the first 40 characters, no banned words, and none promises only misery (the scheduled script's verdict is mixed; pack 98, PB97–PB106, says the verdict is the script's opinion on cited facts, not a finding that the life is a good or bad deal).

| # | Title | Units | Lint | Use |
|---|---|---|---|---|
| A1 (top / post) | Your Life as a Polar Bear: 8 Things You Have to Get Through | 59 | 0 fail, 2 warn | Put on the post. Matches the proven "Your Life as X" family (research 85: median 29,000). Exact YouTube suggestion **"your life as a polar bear."** The "8 things" are the existing script's list, not a new number. |
| A2 | Why Being Born a Polar Bear Is a Terrible Deal (Until You Grow Up) | 66 | 0 fail, 2 warn | Outline Title 2, the milder twin of the Sucks title. Hedge is in the parenthetical, so it does not promise only misery. A/B only; not the post title. |
| A3 | Your Life as a Polar Bear: Cubs Are Born at About 0.6 kg | 56 | 0 fail, 2 warn | Same family as A1, with a specific sourced curse in the title. Search phrasing from **"polar bear cubs born"** / **"the life of a baby polar bear."** Fact: cubs are born at about 0.6 kg with eyes closed and leave the den at 10 to 12 kg (**PB5, PB6, PB13**). Challenger only; do not swap the scheduled post title without a reason. |
| A4 | Your Life as a Polar Bear: A Mother's Fast Can Top 8 Months | 59 | 0 fail, 2 warn | Extra Your Life-family challenger. Fact: the den fast "can exceed 8 months" (**PB12**, USGS 2024). Keep "can" / "top"; do not say a fixed eight months (**PB11** is a ceiling and rests on a paper the pack did not open). |
| A5 | Why It Sucks to Be Born as a Polar Bear (For the First Few Years) | 65 | 0 fail, 2 warn | Outline Title 1. **"Sucks" needs Nolan's yes** before it is used anywhere. The parenthetical is there because the verdict is mixed. Leave it out of the A/B if he has not said yes (outline fallback: run Titles 2 and 3 with a third from the Your Life family, e.g. A3). |

Lint WARNs on every born-as title, and they are accepted: **0 emoji** (same as the scheduled house-cat post title, which also has no emoji and no series parenthetical) and **hashtags do not end `#meatballmyths #shorts`**. The hashtag WARN is from the lint default for Shorts. These are 8–12 minute long-forms, so the draft descriptions use three topic tags plus `#meatballmyths` and **do not** add `#shorts`.

**Rationale, one line each:**

- **A1.** Browse-ready series form, already scheduled, research-85's stronger title family, and it names a hard start without only-misery.
- **A2.** Ready-made A/B from the outline if Studio wants a "deal" hook without the word Sucks.
- **A3.** Keeps "Your Life as a Polar Bear" in the first 40 and puts one pack hook (birth size) where browse can see it.
- **A4.** Same structure, using the mother's-fast hook already cleared for cards and the description (**PB12**).
- **A5.** Closest to the rival S6 wording that still dominates search examples, but it is blocked until Nolan says yes.

### Thumbnails — locked

**`pb_a`, `pb_b`, and `pb_c` are locked as they are.** No new concepts and no redraw. Research 101 recorded the on-image words and cleared them. Studio A/B mapping stays as already built:

| File | Words (research 101) | Recipe / fact | Role |
|---|---|---|---|
| **`pb_a`** | RAW START (bear with a tear) | 2 hand-lettered words; huge drawn bear; first half of the stated mixed verdict; research 101: "does not promise only misery." | **On the post** (`_a`). Locked. |
| **`pb_b`** | 687 KM ONE SWIM | 4 words naming one specific curse. Fact: one collared female made a continuous swim of 687 km over 9 days (**PB36**, Durner 2011, one bear, 2008). Research 101: ok. Keep the 687 as one swim, not a typical distance (**PB35** range is 53.7 to 687.1 km). | **Challenger `_b` after publish.** Locked. |
| **`pb_c`** | BORN A POLAR BEAR? | 4 words; question card, same job as house-cat `cat_c` ("BORN A CAT?"). | **Challenger `_c` after publish.** Locked. |

White/plain recipe, one huge drawn polar bear, one word in red, a hand-drawn arrow, readable at 168 px, **no Meatball**. The image files were not on this box, so which word is red and whether the arrow is already drawn were not visually confirmed this pass. That does not change the lock.

Do not use a "SUCKS" thumb (the house-cat `cat_s` "BEING A CAT SUCKS" still waits on Nolan's yes).

---

## Video 2 — Lion born-as long-form (target Sat 11/28, fallback Sat 12/12)

Scriptwriter delivered the pack (`/workspace/drafts/facts/lion-bornas.md`, LB1–LB43, D1–D8) and the script (`/workspace/drafts/longform-lion-bornas.md`, about 9:12). Not in `posted.csv`. Sources were not edited.

**Target date:** Sat 11/28/2026, usual Saturday hour 08:00 ET, **only if it is ready by Thu 11/26** (MASTER_ORDERS line 217). Ready here means the second-model check, a lion shot set (the script notes there is not one yet), the build, the on-screen text check, and the preview. **Fallback:** Sat 12/12. If the lion takes 11/28, the 12/12 slot needs a different animal. Line 69 still lists lion on 12/12 as the December Saturday; 11/28 is the early option from line 217.

**Top title pick:** Your Life as a Lion: 8 Things You Have to Get Through

That is Scriptwriter's working title. It matches the polar post form, the "Your Life as X" family (research 85, median 29,000), and the script's eight chapters. It names a hard start without promising only misery. The script's verdict is an opinion: a brutal start, a short reign if you're a male, and a pretty sweet deal if you're a female who gets through it.

### Title options

Character counts are UTF-16 units. All four are statement form, under 100, "Lion" inside the first 40 characters, no banned words. None promises only misery. A title built only on cub deaths (for example "Up to 80% of Cubs Don't Reach Two" with no other clause) was considered and rejected for that rule, even though LB9 is used on a challenger thumbnail and in the description.

| # | Title | Units | Lint | Use |
|---|---|---|---|---|
| A1 (top / post) | Your Life as a Lion: 8 Things You Have to Get Through | 53 | 0 fail, 2 warn | Put on the post. Exact series form plus the script's eight things. YouTube suggestion **"your life as a lion."** |
| A2 | Your Life as a Lion: About 15% of Hunts Work in Etosha | 54 | 0 fail, 2 warn | Same family, with one place-specific hunt figure (**LB19**, Stander 1992; keep Etosha, keep "about"). Challenger only. |
| A3 | Your Life as a Lion: Up to 21 Hours of Rest a Day | 49 | 0 fail, 2 warn | Same family, using the rest hook (**LB42**). "Up to" and "rest" stay; do not say "sleep 21 hours." Shows the life is not only hardship. Challenger only. |
| A4 | Why It Sucks to Be Born as a Lion (If You Get Through the Start) | 64 | 0 fail, 2 warn | Rival S6 wording (research 100). **"Sucks" needs Nolan's yes.** The parenthetical keeps it from promising only misery. Not the post title. |

Lint WARNs are the usual born-as pair and are accepted: **0 emoji**, and **hashtags do not end `#meatballmyths #shorts`**. Draft descriptions use three topic tags plus `#meatballmyths` and do not add `#shorts`.

**Rationale, one line each:**

- **A1.** Locks the orders-backed family, matches the polar post title, and covers all eight chapters without a misery-only promise.
- **A2.** Puts Scriptwriter's strongest hunt number in the first browse line, hedged and tied to Etosha so it does not become a species-wide failure rate.
- **A3.** Answers a typed search ("how long do lions sleep") with the pack's correction (rest, not all sleep) and balances the hard-start chapters.
- **A4.** Strong rival-title data, blocked on Nolan's yes, and hedged so a Sucks title still has a way through.

Do not use "your life as a mountain lion" or "your life as every rank in a lion pride." Do not use a lioness-only or male-only post title: the script covers both.

### Thumbnails — `lion_a` / `lion_b` / `lion_c`

White / plain background. One huge drawn African lion (not a mountain lion, not a team logo). 2–4 hand-lettered words, one word in red, a hand-drawn arrow, readable at 168 px. **No Meatball.** Studio A/B: `_a` on the post, `_b` / `_c` as challengers after it posts.

Numbers that D rows dispute stay off the art: speed (**LB18**), roar distance (**D3**, **LB33**), lifespan (**D2**, **LB40**). Do not put a single tenure, pride-size, or count figure on a thumb either (**D4**, **D6**, **D5**). **No cub-killing on thumbnails or hooks** (Studio, 11/15): no "new males," "cubs that can't run," or Serengeti "1 in 4" wording or pictures.

| File | Words | Fact | Role |
|---|---|---|---|
| **`lion_a` (on the post)** | **BORN A LION?** | 3–4 words. Question card, same job as `pb_c` / `cat_c`. One word in red (LION or BORN). Not a misery-only promise and not a disputed number. Kept from the earlier placeholder. | **On the post.** |
| **`lion_b` (challenger)** | **UP TO 80%** | 3 words. Cub survival, Smithsonian: up to 80 percent of cubs die within their first two years (**LB9**). "Up to" is required; do not write "80% of cubs die." Do not merge with the SDZWA year-one average (**LB10**, **D1**). If a second line still reads at 168 px, add **IN 2 YEARS** as the span; if not, leave the span in the title and description. Arrow to a cub. No takeover or cub-killing image. | **Challenger `_b` after publish.** |
| **`lion_c` (challenger)** | **15% IN ETOSHA** | 3 words. Hunting success in Etosha, about 15% (**LB19**, Stander 1992, not 1972). Keep the place name so it is not read as every hunt everywhere. One word in red (15% or ETOSHA). Arrow to a missed hunt or to a lone hunter versus a group. Do not write "lions fail 75%." | **Challenger `_c` after publish.** |

These concepts are new; there are no `lion_*` image files yet.

### Description (draft)

```
What is your life as a lion? Females usually give birth to one to four cubs after about three and a half months (LB1), and a cub weighs about 3 pounds at birth (LB2). The Smithsonian National Zoo says up to 80 percent of lion cubs die within their first two years (LB9). A San Diego Zoo Wildlife Alliance fact sheet says that on average, 60 percent die within the first year, higher in some places such as the Serengeti and Kruger, and that after one year mortality falls below 20 percent (LB10). Those are two different spans; do not merge them (D1).

Hunting success depends on place: 38 percent in a Kalahari study, 23 percent in the Serengeti, and 15 percent in Etosha (LB19; the Etosha figure is Stander 1992, not 1972). Lions hunting alone are less successful than those hunting in a group (LB19). Females may lose up to 20 percent of kills to spotted hyenas when the pride's males are absent (LB23). Lions rest up to 21 hours in 24, which is lying around and resting, not all sleep (LB42). The Smithsonian calls lions the world's most social felines (LB34), and San Diego Zoo says they are at the top of the food chain (LB43). The IUCN Red List lists the lion as Vulnerable, with 23,000 mature individuals and a decreasing trend, in its 2023 assessment (LB37).

The eight things in the script, in order: 1. The hiding place, 2. The odds, 3. The takeover, 4. Hunting school, 5. The neighbours, 6. Kicked out, 7. Taking a pride, 8. Time, and people. Then "What you got" and the verdict. The verdict is the script's opinion: a brutal start, a short reign if you're a male, and a pretty sweet deal if you're a female who gets through it.

#lion #lionpride #wildlife #meatballmyths

Sources: /workspace/drafts/facts/lion-bornas.md (LB1, LB2, LB9, LB10, LB19, LB23, LB34, LB37, LB42, LB43; D1). Script: /workspace/drafts/longform-lion-bornas.md.
```

The description names chapter 3 ("The takeover") but does not hook on cub-killing, per the Studio rule. The Tanzania (LB39) and Kruger (LB41) lines stay in the script, said clean; they are not used as the packaging hook.

### Tags (11, from postkit kw, each 30 characters or fewer)

```
your life as a lion
life of a lion
life of a lion pride
life of a lioness
life of a male lion
life of a lion cub
lion cubs
how long do lions sleep
lion hunting
how do lions catch their prey
Meatball Myths
```

### Pinned comment

```
Which of the eight gets you first? Tell me your number.
```

That is the script's closing question (`s11.l7`).

### 72-hour bar

Same thresholds as above: CTR of 4% or more (the "now 2.5%" note is not a lowered bar), 100+ views, 35%+ average viewed, and minutes a view against the best (1.21). CTR under 3% means a new thumbnail and title the same day. Good CTR but under 25% viewed means rebuild the first 30 seconds.

- If it posts Sat 11/28/2026 08:00 ET, the read is **Tue 12/1/2026 08:00 ET**.
- If it stays on the fallback Sat 12/12/2026 08:00 ET, the read is **Tue 12/15/2026 08:00 ET**.

### Teaser Shorts

Three on-topic trailers are packaged separately in `/workspace/packaging/lion-teasers.md` (cub odds, resting up to 21 hours, hunting odds). Related video points at this long-form. Slot conflicts with `open-dates-1121-1204.md` and with already-queued TikTok 19:00 rows are flagged in that file.

---

## What's needed (gaps)

**Polar (12/5):** Title A1 and thumbs `pb_a` / `pb_b` / `pb_c` are locked. Open ask 2 (the word "Sucks" in a title) is still unanswered, so polar title A5 stays off the post and off the A/B until Nolan says yes. No new polar long-form draft is in `/workspace/drafts/`; none is required for 12/5 if the scheduled skills-repo build is the one that posts.

**Lion (target 11/28, fallback 12/12):** Pack and script have landed; packaging is in this file. Still required before an 11/28 post, and they must be done by Thu 11/26: second-model fact check, a lion shot set (the script says none exists yet), TTS respellings (crèche, Etosha, and others), the build, the on-screen text check, a preview, and a `posted.csv` row. The house-cat end-screen video should be confirmed live before build; the script's fallback is the polar video only if this one posts on 12/12. Lion A4 still needs Nolan's yes. YouTube search samples (`postkit.py kw --search`) did not run (`yt-dlp` missing); suggestions were enough for title phrasing.

**Teasers:** See `/workspace/packaging/lion-teasers.md`. The source Short 1 still has one spoken takeover/cub-killing line (LB12). Studio barred cub-killing from hooks; packaging leaves that line out of the title, description, cover, and pin, and flags Scriptwriter's already-offered swap to the crèche line (LB6). Do not edit the source.

---

## Lint summary

Stubs: `/workspace/packaging/lint-specs/yt-lf-*.json`, `/workspace/packaging/lint-specs/yt-lion-teaser-*.json`, `/workspace/packaging/lint-specs/tt-lion-teaser-*.json`. Kw files: `/workspace/packaging/kw/kw-longform-polar-lion.csv` and `/workspace/packaging/kw/kw-lion-bornas-teasers.csv`.

| Title | Result |
|---|---|
| Polar A1–A5 (born-as, including Sucks) | **0 fail, 2 warn** (0 emoji; long-form hashtags without `#shorts`) |
| Lion A1–A4 (born-as, including Sucks) | **0 fail, 2 warn** (same two WARNs) |
| Teaser Shorts, YouTube (3) | **0 fail, 1 warn** each (5 hashtags vs lint's four; drafts follow written MASTER_ORDERS: 3 topic + `#meatballmyths` + `#shorts`) |
| Teaser Shorts, TikTok (3) | **0 fail, 0 warn** |

The two born-as WARNs are kept on purpose. Adding an emoji would fight the house-cat / born-as post-title precedent. Adding `#shorts` to an 8–12 minute description would be wrong packaging.

---

## Picks (short)

- **Frame:** resolved 11/15 — born-as every December Saturday per line 69 (polar 12/5, lion 12/12, dog and wolf 12/19 and 12/26 by data rank). Line 217 allows lion on 11/28 if ready by Thu 11/26. Scriptwriter now targets 11/28, with 12/12 as the fallback. If 11/28 is used, 12/12 needs a different animal.
- **Polar 12/5 top title:** Your Life as a Polar Bear: 8 Things You Have to Get Through (59, already scheduled, lint 0 fail / 2 accepted warn).
- **Polar thumbs:** locked as they are — `pb_a` RAW START on the post; `pb_b` 687 KM ONE SWIM and `pb_c` BORN A POLAR BEAR? as post-publish challengers.
- **Lion top title:** Your Life as a Lion: 8 Things You Have to Get Through (53, lint 0 fail / 2 accepted warn).
- **Lion thumbs:** `lion_a` **BORN A LION?** on the post; `lion_b` **UP TO 80%** (LB9, cub survival, keep "up to," no cub-killing image); `lion_c` **15% IN ETOSHA** (LB19, Stander 1992). Speed, roar distance, and lifespan stay off the art.
- **72-hour bar:** CTR 4%+ (not the "now 2.5%" note), 100+ views, 35%+ average viewed; under 3% CTR means a new thumbnail and title the same day. Polar read: Tue 12/8/2026 08:00 ET. Lion read: Tue 12/1/2026 08:00 ET if it posts 11/28 08:00; Tue 12/15/2026 08:00 ET on the 12/12 fallback.
