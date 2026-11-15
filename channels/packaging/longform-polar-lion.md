# Long-form packaging: polar bear (Sat 12/5) and lion (Sat 12/12)

Draft only. No scheduling, posting, repo edits, or thumbnail file changes. Facts are from the packs cited below; nothing is invented. Times are America/New_York (ET).

**Resolved 11/15:** born-as every December Saturday per MASTER_ORDERS line 69. The schedule is polar 12/5, lion 12/12, then dog and wolf on 12/19 and 12/26 by data rank. Line 217 allows lion on 11/28 if it's ready by Thu 11/26.

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
- `postkit.py kw` run 11/15 (YouTube + web suggestqueries). YouTube search (`--search`) did not run: `yt-dlp` is not installed. Rows: `/workspace/packaging/kw/kw-longform-polar-lion.csv`. Notable suggestions: **"your life as a polar bear"** and **"the life of a polar bear"**; **"polar bear cubs born"**; **"your life as a lion"**, **"your life as a lioness"**, **"life of a male lion"**, **"life of a lion pride"**. The phrase **"why it sucks to be born as a [animal]"** returned **no** YouTube suggestions (research 100 already noted the born-as phrase has no YouTube suggest volume).

---

## 72-hour bar (both videos)

From MASTER_ORDERS, The YouTube play, "How each long-form is judged at 72 hours (my thresholds, not Studio's)":

- Watch for **CTR of 4% or more**, **100+ views**, and **35%+ average viewed**, plus minutes a view against the current best (1.21).
- The parenthetical **"now 2.5%"** in that line is a current-performance note, not a lowered bar. The bar to watch remains **4%+**.
- **CTR under 3%:** new thumbnail and title **the same day**.
- Good CTR but **under 25% viewed:** rebuild the first 30 seconds.

For the polar video, 72 hours after the scheduled Sat 12/5/2026 08:00 ET start is **Tue 12/8/2026 08:00 ET**. Locked challenger thumbs `pb_b` and `pb_c` go into the post-publish A/B; they are not replacements for `pb_a` on the scheduled post.

If the lion posts on Sat 12/12 at the usual Saturday 08:00 ET slot, 72 hours lands **Tue 12/15/2026 08:00 ET**. That start time is not locked in `posted.csv`. If it instead posts Sat 11/28 under line 217, 72 hours lands **Tue 12/1/2026 08:00 ET**.

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

## Video 2 — Sat 12/12: lion (waiting on Scriptwriter)

This section is waiting on Scriptwriter's lion born-as fact pack and script, which are in progress. Not in `posted.csv`. Default date is Sat 12/12 per line 69; line 217 allows Sat 11/28 if the pack and script are ready by Thu 11/26. Research 100 ranks lion first among S6 animals, with a small December lift (36 vs 30) that the file calls small and flat.

Do not add a count, a curse, or a sourced-fact clause until that pack lands. Do not treat research 116 or the bears-vs-lions pack as a substitute.

**Placeholder title (until the pack and script land):** Your Life as a Lion

If the pack supports a numbered list the way the polar and house-cat scripts do, a second clause in the same family can be added then. Do not invent "8 things" now.

| # | Title | Units | Lint | Use |
|---|---|---|---|---|
| A1 (placeholder) | Your Life as a Lion | 19 | 0 fail, 2 warn | Exact YouTube suggestion. Series form, animal in the first 40, no only-misery promise, no unsourced fact. Hold as the placeholder post title until Scriptwriter's pack and script land. |

Parked until the pack can support or rule them out: **Your Life as a Lioness** (22), **Your Life as a Male Lion** (24), and **Why It Sucks to Be Born as a Lion** (33; Sucks needs Nolan's yes). Kw also suggested "your life as every rank in a lion pride" and "your life as a mountain lion." Do not use the first (it copies another channel's wolf-rank pattern). Do not use the second (this slot is the African lion born-as, not a mountain-lion video).

### Thumbnails — `lion_a` only, for now

There are no `lion_a` / `lion_b` / `lion_c` files yet. `lion_b` and `lion_c` curse words wait for Scriptwriter's pack.

| File | Concept | Status |
|---|---|---|
| **`lion_a` (on the post, once built)** | White / plain background. One huge drawn African lion (not a mountain lion, not a team logo). 3–4 hand-lettered words: **BORN A LION?** One word in red (LION or BORN). Hand-drawn arrow. Readable at 168 px. **No Meatball.** Same job as `pb_c` / `cat_c`. A question is not an unsourced curse. | Keep. Safe to design now. |
| **`lion_b` / `lion_c`** | Same recipe, each naming one specific curse from the lion fact pack. | Waiting on Scriptwriter's pack. |

Do not borrow curse wording from polar (`RAW START`, `687 KM ONE SWIM`) or from house cat (`LILIES CAN KILL IT`).

---

## What's needed (gaps)

**Polar (12/5):** Title A1 and thumbs `pb_a` / `pb_b` / `pb_c` are locked. Open ask 2 (the word "Sucks" in a title) is still unanswered, so title A5 stays off the post and off the A/B until Nolan says yes. No new polar long-form draft is in `/workspace/drafts/`; none is required for 12/5 if the scheduled skills-repo build is the one that posts. YouTube search samples (`postkit.py kw --search`) did not run (`yt-dlp` missing); suggestions were enough for title phrasing.

**Lion (12/12, or 11/28 if ready by Thu 11/26):** Waiting on Scriptwriter's lion born-as fact pack and script, now in progress. Until those land, do not write a fact-forward title, `lion_b` / `lion_c` curse words, a description with animal claims, or a `posted.csv` row. The placeholder title **Your Life as a Lion** and the `lion_a` **BORN A LION?** concept stay. After the pack: second-model check, on-screen text check, preview, and a schedule row.

---

## Lint summary

Stubs: `/workspace/packaging/lint-specs/yt-lf-*.json`. Kw file: `/workspace/packaging/kw/kw-longform-polar-lion.csv`.

| Title | Result |
|---|---|
| Polar A1–A5 (born-as, including Sucks) | **0 fail, 2 warn** (0 emoji; long-form hashtags without `#shorts`) |
| Lion A1 (placeholder: Your Life as a Lion) | **0 fail, 2 warn** (same two WARNs) |

The two born-as WARNs are kept on purpose. Adding an emoji would fight the house-cat / born-as post-title precedent. Adding `#shorts` to an 8–12 minute description would be wrong packaging.

Lion descriptions in the stubs state that the pack has not landed and make **no animal claims**. They exist so title lint can run. Do not ship them.

---

## Picks (short)

- **Frame:** resolved 11/15 — born-as every December Saturday per line 69 (polar 12/5, lion 12/12, dog and wolf 12/19 and 12/26 by data rank). Line 217 allows lion on 11/28 if ready by Thu 11/26.
- **Polar 12/5 top title:** Your Life as a Polar Bear: 8 Things You Have to Get Through (59, already scheduled, lint 0 fail / 2 accepted warn).
- **Polar thumbs:** locked as they are — `pb_a` RAW START on the post; `pb_b` 687 KM ONE SWIM and `pb_c` BORN A POLAR BEAR? as post-publish challengers.
- **Lion:** waiting on Scriptwriter's born-as fact pack and script (in progress). Placeholder title: Your Life as a Lion (19, lint 0 fail / 2 accepted warn). Keep `lion_a` **BORN A LION?**; `_b`/`_c` wait for the pack.
- **72-hour bar:** CTR 4%+ (not the "now 2.5%" note), 100+ views, 35%+ average viewed; under 3% CTR means a new thumbnail and title the same day. Polar read: Tue 12/8/2026 08:00 ET.
