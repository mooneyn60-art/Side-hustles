# Long-form packaging: polar bear (Sat 12/5) and lion (Sat 12/12)

Draft only. No scheduling, posting, repo edits, or thumbnail file changes. Facts are from the packs cited below; nothing is invented. Times are America/New_York (ET).

---

## Conflict (read this first)

Social Studio called the Sat 12/5 video **"Would Meatball Survive a Polar Bear?"** That is a Would Meatball Survive (WMS) frame.

The orders do **not** support that frame for this video.

- `posted.csv` already schedules Sat 12/5/2026 08:00 ET as **Your Life as a Polar Bear: 8 Things You Have to Get Through**, episode `longform-born-as-polar-bear`, file `born-as-polar-bear.mp4`.
- MASTER_ORDERS, "Long videos" (the 11/13 "do all three" line): one **"born as"** video every Saturday in December — polar bear 12/5 (scheduled), lion 12/12, then dog and wolf by data rank on 12/19 and 12/26.
- MASTER_ORDERS, Watch hours: the post title carries **"Your Life as a …"**; no title may promise only misery; **"Why It Sucks …" is A/B only with Nolan's yes** (open ask 2 is still unanswered in the orders).
- Research 85 addendum (11/12, 148 S6 videos, channels under 100K): **"Your Life as X" median 29,000 views** (29 videos, 5 channels, 59% over 10K) vs **"Why It Sucks to Be (Born as) X" median 4,150** (106 videos, 21 channels, 41% over 10K). **"Anything else": 0 of 13 over 10,000** (median 660). A WMS / "Would Meatball Survive a Polar Bear?" title is in that third family.
- Research 85 on S1: **"Would you survive [animal]" as a long video has no small-channel base.** The 25 videos from 9 channels are mostly games, prehistoric "could it survive," and history. YouTube suggestions for that seed collapse to **attack** phrasing ("can you survive a polar bear attack"), which is a different video than the scheduled born-as life script.

This file therefore ranks the **orders-backed born-as / "Your Life as a …" frame first**, and gives WMS title and thumbnail options second. A WMS title on the already-built polar script would also fight the video the viewer gets (the viewer lives the bear's life; Meatball is a tourist joke inside that script, not the test subject of a survival question).

A residual date conflict inside MASTER_ORDERS does **not** change the frame: Watch hours still lists "Sat 11/28 the lion if ready" and **dog 12/12**, while the "Long videos" line and this Studio request put **lion on 12/12**. 12/12 is not in `posted.csv`. Packaging below follows lion on 12/12 as born-as, and flags that the Watch hours queue still has to be reconciled.

---

## Frame decision

**The orders support the born-as frame, posted under "Your Life as a …", for both Saturday long-forms.**

| Date | Orders-backed frame (rank first) | Studio WMS frame (rank second) |
|---|---|---|
| Sat 12/5 08:00 ET | Born-as. Already scheduled, scripted, fact-checked (research 98, 99, 101), thumbnail `pb_a` on the post. | Conflicts with the scheduled title, the series rule, research 85's "anything else" and S1 findings, and the existing script. |
| Sat 12/12 (time not in `posted.csv`) | Born-as lion, next animal after polar in the "Long videos" line. Rank 1 S6 animal in research 100. No fact pack or script yet. | Same research-85 problem, and no lion-encounter pack either. Do not reuse research 116 / the bears-vs-lions pack (a fight comparison, not a life or an encounter). |

---

## Sources checked

- MASTER_ORDERS: "Long videos," Watch hours (queue, "Your Life as," no only-misery, Sucks needs Nolan's yes), The YouTube play (72-hour bar).
- `posted.csv`: polar row above; no 11/28, 12/12, 12/19, or 12/26 long-form rows.
- Born-as polar episode materials in the skills repo: `scripts/longform-born-as-polar-bear.json`, `scripts/longform-born-as-polar-bear.outline.json` (three titles and `_titles_note`). The built file is scheduled. **No polar long-form script is in `/workspace/drafts/`.** Scriptwriter has not started a new one there.
- Research 98 (`98-polar-bear-life-factpack.md`, row IDs PB1–PB106), script check 99, on-screen/thumbnail check 101 (including `pb_a` / `pb_b` / `pb_c` wording).
- Research 85 (`85-longform-pets-survive-format.md`) and the 11/12 title-family addendum.
- Research 100 (`data/100-longform-topic-candidates.csv`): lion is overall rank 1 in the S6 shape (demand 58, winnability 0.5, score 0.89; small-channel examples include "why it sucks to be born as a lion." at 686,684 views). Dog is rank 2, wolf rank 3.
- Research 115: the lion fact pack had not been started as of that scoreboard note; it was "the next step of the long-video line."
- Research 116 and `/workspace/drafts/facts/bears-vs-lions.md`: animals-not-teams fight facts. **Not** a "life as a lion" pack. Not used for lion titles or thumbnails here.
- Thumbnail recipe from research 85 addendum (white or plain background; one huge drawn animal; 2–4 hand-lettered words naming one specific curse; one word in red; a hand-drawn arrow; readable at 168 px). No Meatball in the thumbnail (MASTER_ORDERS / house-cat precedent).
- `episodes/thumbs-bornas/` and the `pb_a` / `pb_b` / `pb_c` image files were **not** in this sparse clone, so the images were not inspected this pass. On-image words are taken from research 101.
- `postkit.py kw` run 11/15 (YouTube + web suggestqueries). YouTube search (`--search`) did not run: `yt-dlp` is not installed. Rows: `/workspace/packaging/kw/kw-longform-polar-lion.csv`. Notable suggestions: **"your life as a polar bear"** and **"the life of a polar bear"**; **"polar bear cubs born"**; **"your life as a lion"**, **"your life as a lioness"**, **"life of a male lion"**, **"life of a lion pride"**; WMS seeds suggest **"can you survive a polar bear attack"** and **"how do you survive a lion attack"** — attack videos, not born-as. The phrase **"why it sucks to be born as a [animal]"** returned **no** YouTube suggestions (research 100 already noted the born-as phrase has no YouTube suggest volume).

---

## 72-hour bar (both videos)

From MASTER_ORDERS, The YouTube play, "How each long-form is judged at 72 hours (my thresholds, not Studio's)":

- Watch for **CTR of 4% or more**, **100+ views**, and **35%+ average viewed**, plus minutes a view against the current best (1.21).
- The parenthetical **"now 2.5%"** in that line is a current-performance note, not a lowered bar. The bar to watch remains **4%+**.
- **CTR under 3%:** new thumbnail and title **the same day**.
- Good CTR but **under 25% viewed:** rebuild the first 30 seconds.

For the polar video, 72 hours after the scheduled Sat 12/5/2026 08:00 ET start is **Tue 12/8/2026 08:00 ET**. Challenger thumbs `pb_b` and `pb_c` are already designated for the post-publish A/B (research 101 / MASTER_ORDERS_LOG), not as replacements for `pb_a` on the scheduled post.

If the lion posts on Sat 12/12 at the usual Saturday 08:00 ET slot, 72 hours lands **Tue 12/15/2026 08:00 ET**. That start time is not locked in `posted.csv`.

The house-cat 72-hour read on 12/1 decides what to fix in later born-as videos (first 30 seconds, title, thumbnail), not whether they run.

Studio A/B for long-form: `_a` on the post, `_b` / `_c` as challengers after it posts.

---

## Video 1 — Sat 12/5: polar bear

Scheduled. Script and outline already exist in the skills repo (about 10:30, preview sent 11/13). Facts from research 98; wording already cleared in research 99 and 101. Do not put a WMS title on this file without a new script.

### Frame A (orders-backed, rank first): born-as / "Your Life as a …"

**Top title pick (already on the scheduled post):** Your Life as a Polar Bear: 8 Things You Have to Get Through

That is outline Title 3, the post title named in `_titles_note`, and the `posted.csv` title.

#### Title options

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

#### Thumbnails (born-as / white recipe)

The existing files already cover this brief. They are not new concepts. Research 101 recorded the on-image words and cleared them. Map them to Studio A/B as they already are:

| File | Words (research 101) | Recipe / fact | Role |
|---|---|---|---|
| **`pb_a`** | RAW START (bear with a tear) | 2 hand-lettered words; huge drawn bear; first half of the stated mixed verdict; research 101: "does not promise only misery." | **On the post** (`_a`). Do not replace before publish. |
| **`pb_b`** | 687 KM ONE SWIM | 4 words naming one specific curse. Fact: one collared female made a continuous swim of 687 km over 9 days (**PB36**, Durner 2011, one bear, 2008). Research 101: ok. Keep the 687 as one swim, not a typical distance (**PB35** range is 53.7 to 687.1 km). | **Challenger `_b` after publish.** |
| **`pb_c`** | BORN A POLAR BEAR? | 4 words; question card, same job as house-cat `cat_c` ("BORN A CAT?"). | **Challenger `_c` after publish.** |

All three should stay in the white/plain recipe: one huge drawn polar bear, one word in red, a hand-drawn arrow, readable at 168 px, **no Meatball**. The image files were not on this box, so which word is red and whether the arrow is already drawn were not visually confirmed this pass. If a redraw is needed, keep the words above; do not invent a fourth concept unless `pb_a` misses the 72-hour bar.

Do not use a "SUCKS" thumb (the house-cat `cat_s` "BEING A CAT SUCKS" still waits on Nolan's yes).

### Frame B (Studio WMS, rank second): "Would Meatball Survive a Polar Bear?"

Use only if Nolan and Studio explicitly override the scheduled born-as post. That would need a **new script**, not a title swap on `born-as-polar-bear.mp4`. Search phrasing for this frame is attack-survival, not "your life as."

| # | Title | Units (UTF-16) | Lint | Notes |
|---|---|---|---|---|
| B1 | Would Meatball Survive a Polar Bear? | 36 | **FAIL** (question title; also 0 emoji and no series parenthetical) | Studio's wording. Do not put this on YouTube as written. |
| B2 | Meatball vs a Polar Bear: What the Sources Say 🐻 (Would Meatball Survive?) | 75 | 0 fail, 1 warn (`#shorts`) | Lint-clean statement form with the series tag and one emoji. Still a different video than the scheduled life script, and it sits in research 85's "anything else" family (0 of 13 over 10K). |
| B3 | Polar Bear Attack: What Manitoba Says to Do 🐻 (Would Meatball Survive?) | — | not linted as a pick | Shown only to name the kw-suggested attack frame ("can you survive a polar bear attack"). It would depend on **PB71** (Manitoba encounter advice, with its trigger) and the exact safety line **"General information, not safety training."** It is not the 12/5 video. |

WMS thumbnails would also be a new set (Meatball is still banned from the thumb). They are not drawn here, because the orders-backed video already has `pb_a` / `pb_b` / `pb_c`. If a WMS long-form is commissioned later, it needs its own pack, script, second-model check, and thumbs.

---

## Video 2 — Sat 12/12: lion

Not in `posted.csv`. Orders-backed frame is still born-as ("Long videos" line: lion after polar). Research 100 ranks lion first among S6 animals, with a small December lift (36 vs 30) that the file calls small and flat.

**No lion born-as fact pack, no `longform-born-as-lion` script, and no lion draft in `/workspace/drafts/`.** Titles below stay in the series form and in postkit kw phrasing. They do **not** add a count, a curse, or a "sourced fact" clause, because there is no pack to cite. Thumbnail curse words except the series-style question wait for the pack.

### Frame A (orders-backed, rank first): born-as / "Your Life as a …"

**Top title pick (until a pack and script land):** Your Life as a Lion

If the later pack supports a numbered list the way the polar and house-cat scripts do, a second clause in the same family can be added then (compare A1 on the polar video). Do not invent "8 things" now.

| # | Title | Units | Lint | Use |
|---|---|---|---|---|
| A1 (top) | Your Life as a Lion | 19 | 0 fail, 2 warn | Exact YouTube suggestion. Series form, animal in the first 40, no only-misery promise, no unsourced fact. Short, but it is the post form the orders require. |
| A2 | Your Life as a Lioness | 22 | 0 fail, 2 warn | Exact YouTube suggestion. Use only if the pack is written from the female / pride-hunting side. Do not pick a sex before the pack exists. |
| A3 | Your Life as a Male Lion | 24 | 0 fail, 2 warn | Built from the suggestion **"life of a male lion."** Same caveat as A2. |
| A4 | Why It Sucks to Be Born as a Lion | 33 | 0 fail, 2 warn | Rival S6 wording (research 100 examples: Mr scribbles 686,684 views; JustJNR 139,648). **Sucks needs Nolan's yes.** Also needs a script whose verdict is not only misery. Not the post title. |

**Rationale, one line each:**

- **A1.** Locks the orders-backed family and the exact searched phrase without inventing a hook the pack has not delivered.
- **A2.** Browse variant from kw; hold until the pack says the video is a lioness's life.
- **A3.** Browse variant from kw; hold until the pack says the video is a male's life (coalition, takeover, and so on, only if sourced later).
- **A4.** Strong rival-title data, blocked on Nolan's yes and on a mixed-verdict script.

Kw also suggested "your life as every rank in a lion pride" and "your life as a mountain lion." Do not use the first (it copies another channel's wolf-rank pattern and has no pack). Do not use the second (this slot is the African lion born-as, not a mountain-lion video).

#### Thumbnails (born-as / white recipe) — all new

There are no `lion_a` / `lion_b` / `lion_c` files. These concepts are new. Until a pack names a specific sourced curse, only the series-style question card can be specified without inventing a fact.

| File | Concept | Status |
|---|---|---|
| **`lion_a` (on the post, once built)** | White / plain background. One huge drawn African lion (not a mountain lion, not a team logo). 3–4 hand-lettered words: **BORN A LION?** One word in red (LION or BORN). Hand-drawn arrow. Readable at 168 px. **No Meatball.** Same job as `pb_c` / `cat_c`. A question is not an unsourced curse. | New. Safe to design now. |
| **`lion_b` (challenger after post)** | Same recipe. 2–4 words naming **one specific curse from the lion fact pack**, one word in red, arrow, huge drawn lion, no Meatball. | New, **words not chosen.** Wait for the pack. |
| **`lion_c` (challenger after post)** | Same recipe, a second sourced curse, different from `_b`. | New, **words not chosen.** Wait for the pack. |

Do not borrow curse wording from polar (`RAW START`, `687 KM ONE SWIM`) or from house cat (`LILIES CAN KILL IT`). Do not invent pride, cub-kill, or hunger lines from general knowledge or from the bears-vs-lions pack.

### Frame B (Studio WMS, rank second): "Would Meatball Survive a Lion?"

Same problems as the polar WMS frame, plus there is no lion-encounter pack.

| # | Title | Units (UTF-16) | Lint | Notes |
|---|---|---|---|---|
| B1 | Would Meatball Survive a Lion? | 30 | **FAIL** (question title; 0 emoji; series tag missing) | Studio-style wording. Do not use as written. |
| B2 | Meatball vs a Lion: What the Sources Say 🐻 (Would Meatball Survive?) | 69 | 0 fail, 1 warn (`#shorts`) | Lint-clean statement form. Still "anything else" under research 85, and it has no sources until a pack exists. Do not lean on BL-F* (bear vs lion who-would-win), which is a different question. |
| B3 | Lion Attack: How Do You Survive 🐻 (Would Meatball Survive?) | — | not linted as a pick | Matches the kw-suggested attack frame. Needs an opened agency advice row that does not exist here. |

WMS thumbs would be a third new set. Not specified, because the orders-backed path is born-as and the pack is missing.

---

## What's needed (gaps)

**Polar (12/5):** Packaging and the video are largely already in place. Remaining gaps are operational, not research:

- The `pb_a` / `pb_b` / `pb_c` image files were not visually inspected here (missing from the sparse clone). Confirm red word, arrow, and 168 px readability on the actual art before publish.
- Open ask 2 (the word "Sucks" in a title) is still unanswered. Title A5 stays off the post and off the A/B until Nolan says yes.
- No new polar long-form draft exists in `/workspace/drafts/`; none is required for 12/5 if the scheduled skills-repo build is the one that posts.
- YouTube search samples (`postkit.py kw --search`) did not run (`yt-dlp` missing). Suggestions were enough for title phrasing.

**Lion (12/12):** A full born-as fact pack is missing and is required before a script, a fact-forward title, curse thumbnails `_b`/`_c`, a description with animal claims, or a schedule row. Model it on research 98 / the house-cat pack (research 87), including:

- Species scope (African lion, not mountain lion, not a team).
- Birth and cub facts (size, eyes, litter, hide or den) with hedges.
- Cub and adult survival figures **with population and years**.
- Pride / coalition / takeover or hunting-role claims only from opened papers or agency pages.
- Lean-season or fasting claims only if sourced.
- Lifespan and first independence, with the same hedges as PB22–PB24.
- Human-encounter advice only if an agency page is opened, with its trigger (do not invent a Manitoba-style line).
- An honest-verdict section like PB97–PB106 (no unsourced "best deal" / "worst deal"; no cross-species ranking).
- A strongest-hooks list with IDs.
- Then: script, second-model check, on-screen text check, preview, and a `posted.csv` row if 12/12 is confirmed over the Watch hours "dog 12/12" line.

Do not treat research 116, `/workspace/drafts/facts/bears-vs-lions.md`, or the Bears vs Lions Shorts as a substitute pack.

**WMS long-forms (either animal):** There is no "Would Meatball Survive a [polar bear / lion]" long-form pack, and research 85 gives that shape no small-channel base. Do not start one unless Nolan overrides the born-as queue.

---

## Lint summary

Stubs: `/workspace/packaging/lint-specs/yt-lf-*.json`. Kw file: `/workspace/packaging/kw/kw-longform-polar-lion.csv`.

| Title | Result |
|---|---|
| Polar A1–A5 (born-as, including Sucks) | **0 fail, 2 warn** (0 emoji; long-form hashtags without `#shorts`) |
| Polar B1 (Studio WMS question) | **FAIL** — question title |
| Polar B2 (WMS statement) | **0 fail, 1 warn** (`#shorts`) |
| Lion A1–A4 (born-as, including Sucks) | **0 fail, 2 warn** (same two WARNs) |
| Lion B1 (Studio WMS question) | **FAIL** — question title |
| Lion B2 (WMS statement) | **0 fail, 1 warn** (`#shorts`) |

The two born-as WARNs are kept on purpose. Adding an emoji or a `(Would Meatball Survive?)` tag would fight the series rule. Adding `#shorts` to an 8–12 minute description would be wrong packaging.

Lion descriptions in the stubs state that the pack has not landed and make **no animal claims**. They exist so title lint can run. Do not ship them.

---

## Picks (short)

- **Frame:** born-as / "Your Life as a …" for both dates. Studio's WMS labels conflict; options for that frame are second, and they need new scripts.
- **Polar 12/5 top title:** Your Life as a Polar Bear: 8 Things You Have to Get Through (59, already scheduled, lint 0 fail / 2 accepted warn).
- **Polar thumbs:** existing `pb_a` RAW START on the post; `pb_b` 687 KM ONE SWIM and `pb_c` BORN A POLAR BEAR? as post-publish challengers. Not new.
- **Lion 12/12 top title:** Your Life as a Lion (19, lint 0 fail / 2 accepted warn), until a pack supports a second clause.
- **Lion thumbs:** all new. Only `lion_a` **BORN A LION?** can be specified now; `_b`/`_c` curse words wait for the pack.
- **72-hour bar:** CTR 4%+ (not the "now 2.5%" note), 100+ views, 35%+ average viewed; under 3% CTR means a new thumbnail and title the same day. Polar read: Tue 12/8/2026 08:00 ET.
