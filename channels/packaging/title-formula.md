# Title formula (locked draft)

Status: draft only. No repo edit, commit, push, post, or publish. Any wording change still needs a second-model check before it is applied.

Sources: Social Studio canvas "Meatball Channels — Deep Dive & Creative Audit" (canvas `4774d0bc-99bc-40d9-bc8b-c27f5ad06153`, store `store-959fd15d-66ea-464e-a6af-8ac8f2415014` — use the URL in the brief); `skills/channel-brain/MASTER_ORDERS.md` 11/12 Posting standard and the born-as rule; `KNOWLEDGE.md` lady-beetle lesson; `postkit.py lint` on the stubs in `/workspace/packaging/lint-specs/`. Notebook context: `mooneyn60-art/Side-hustles` `main` `TASKS.md` "Notes for Claude" is about the Etsy shop (FurEver Faces rename and ads), not Meatball title rules. The 11/15 Social Studio log in that file points at `channels/packaging/bug-shorts-1114-1120.md` and the empty Shorts dates 11/22–11/24 and 11/26–12/4.

Character counts below are YouTube UTF-16 units (one emoji = 2).

## Locked formula (audit reconciled with the 11/12 standard)

1. Statement form. No `?` in the core title. A trailing parenthetical such as `(Would Meatball Survive?)` is allowed (lint strips that last parenthetical before the question check).
2. Put the searched words in the first 40 characters. Name the creature or the typed query there. Do not hide it behind "This Bird" or a vague "Bugs in Your Walls" (the lady-beetle flop in KNOWLEDGE: the title named no creature).
3. Keep the hedge (`May`, `Can`, `Likely`, `About`, `If`, `Typically`).
4. Add one specific sourced fact. Do not invent a number or a winner to fill this slot.
5. One emoji.
6. Series tag last, with the episode number when the episode has one: `(Things Living In Your House #N)` or `(Would Meatball Survive? #N)`. If the number is not assigned yet, use the series name alone.
7. 100 UTF-16 units at most.
8. Banned in the title: `TRUE or FALSE`, `Myth`, `Believe`, `Cartoons`, `Lied`, `Did you know`.
9. Clean wording. No swears. `Sucks` stays out of the posted title unless Nolan says yes (MASTER_ORDERS open ask 2).
10. For Things Living In Your House pet videos, prefer `Your cat` / `Your dog` in the lead when the searched words still fit in the first 40 characters. If they do not fit, the searched words win (clause 2).
11. Born-as long-forms: the post carries `Your Life as a …`. A `Why It Sucks to Be Born as a …` title is an A/B challenger only, and only with Nolan's yes.

The audit's upgrade-3 sentence is the same spine as the 11/12 standard: "Titles lead with the searched words in the first 40 characters, keep the hedge, add one specific sourced fact, one emoji, and the series tag last." The lock above adds the lint rules, the banned list, the pet-lead preference, the series `#N`, and the born-as post title, which the audit's one-sentence formula did not spell out.

## Conflicts with MASTER_ORDERS (and how they were resolved here)

| Item | Audit | MASTER_ORDERS / repo | What this draft locks |
|---|---|---|---|
| Cassowary title | `This Bird Has a 4-Inch Dagger on Each Foot` — "Cassowary" is not in the first 40 characters | Searched words in the first 40; name the creature | Locked title names Cassowary in the first 40. Audit wording is kept as a rejected lead. |
| Lady beetle title | `Lady Beetles May Cluster…` (drops "Asian") | Search suggestions include `asian lady beetles in house`; Penn State source in `lady-beetle-v6-yt.json` is Multicolored Asian Lady Beetle | Locked title keeps `Asian Lady Beetles`. |
| Termite title | `…While the Paint Still Looks Fine` | `termite-yt.json` spoken line is "The wood looks fine outside. But it's thin, and a screwdriver pokes right through." No "paint" in that script | Locked title uses `Wood`, not `Paint`. |
| Pet lead | Formula example: `Why Dogs Lick You: It May Start as a Food Ask` | 11/12: `Your cat` / `Your dog` leading on pet house videos | Preference stated in clause 10. The lick example is not one of the five rewrites; if it is titled later, try to keep "Your dog" and the searched words in the first 40. |
| Series `#N` | Audit examples often omit the number | Live queue and lint expect the series tag; assigned episodes in `posted.csv` use `#N` | Include `#N` when assigned. |
| House-cat long-form title | Keep `Your Life as a House Cat: 8 Ways It Goes Wrong` on the post | Same born-as rule. Lint wants one emoji and the series tag | Keep the posted title. Do not "fix" it to add an emoji or series tag. Lint warnings are expected. |
| `Sucks` challenger | A/B only with Nolan's yes | Open ask 2; mild-word titles stay until he says yes | Challenger is recorded, not locked as the post title, and was not linted as the posted title. |
| YouTube hashtags (descriptions) | Not the subject of this file | Written 11/12: 3 topic + `#meatballmyths` + `#shorts`. `postkit.py lint` still warns that "the standard is four: two topic, `#meatballmyths`, `#shorts`" | Drafts follow the written order (5 hashtags). Lint is a WARN, not a FAIL. |
| TikTok hashtags | 3 topic + `#meatballmyths` | Five topic hashtags, no brand tag | Not locked here. See `tiktok-caption-template.md`. |

## The five title rewrites

### 1. Cassowary (Would Meatball Survive?)

- Current / old titles in the repo: `Meatball Walked Into a Rainforest Holding a Sandwich` (`cassowary-v3-yt.json`); `Cassowary: Corner It and It Kicks With a Dagger Claw. Would Meatball Survive? 🦶` (`cassowary-wms-yt.json`, question in the core would fail statement-form lint).
- Audit rewrite: `This Bird Has a 4-Inch Dagger on Each Foot 🦶 (Would Meatball Survive?)` — 71 units. Lint of this wording: pass, 0 fail, 1 hashtag WARN (`lint-specs/title-cassowary-audit-raw.json`). Rejected as the lock because "Cassowary" is not in the first 40 characters.
- **Locked title:** `This Cassowary Has a 4-Inch Dagger on Each Foot 🦶 (Would Meatball Survive?)` — 76 units.
- Sourced fact: both cassowary scripts say each foot hides a four inch dagger claw. No new number was added. Episode `#N` is not assigned in these specs; series tag has no number.
- Lint (`lint-specs/title-cassowary.json`): pass, 0 fail, 1 hashtag WARN. Title 76 of 100.
- Audit last-line rewrite ("Survive? Yes, unless he is holding food… Meatball lived. Nothing's guaranteed.") is a script change, not a title. It is not applied here (draft-only packaging; the spoken ending was not second-model checked in this pass).

### 2. Lady beetle (Things Living In Your House #44)

- Current `posted.csv` / `lady-beetle-v6-yt.json` title: `10,000s of Bugs in Your Walls 🐞 (Things Living In Your House #44)` — names no creature.
- Audit rewrite: `Lady Beetles May Cluster in Your Walls for Winter 🐞 (Things Living In Your House).`
- **Locked title:** `Asian Lady Beetles May Cluster in Your Walls for Winter 🐞 (Things Living In Your House #44)` — 92 units. `#44` kept from the live episode. "May Cluster" hedges Penn State's "tens of thousands can congregate in attics, ceilings and wall voids."
- Lint (`lint-specs/title-lady-beetle.json`): pass, 0 fail, 1 hashtag WARN. Title 92 of 100.

### 3. Termite hook-test

- Current `posted.csv` title (slot 2026-11-11 19:00): `Several Colonies Eating Your House 🪵 (Things Living In Your House)`.
- Audit rewrite: `Termites Can Hollow a Beam While the Paint Still Looks Fine 🪵 (Things Living In Your House)` — 92 units.
- **Locked title:** `Termites Can Hollow a Beam While the Wood Still Looks Fine 🪵 (Things Living In Your House)` — 91 units. "Can" is the hedge. "Wood" is the word in `termite-yt.json`. No episode number is on the scheduled hook-test title, so none was added.
- Lint (`lint-specs/title-termite.json`): pass, 0 fail, 1 hashtag WARN. Title 91 of 100.

### 4. House-cat long-form (already posted Fri 11/13 17:00 ET)

- **Locked post title (unchanged):** `Your Life as a House Cat: 8 Ways It Goes Wrong` — 46 units. This is the title in `posted.csv` for `born-as-house-cat.mp4`.
- Audit / MASTER_ORDERS A/B challenger, only with Nolan's yes: `Why It Sucks to Be Born as a House Cat` — 38 units. Thumbnail challenger `YOUR LIFE AS A CAT` lives in `thumbnail-concepts.md`, not here.
- Lint of the kept post title (`lint-specs/title-house-cat.json`): pass, 0 fail, 3 WARN (0 emoji; title lacks the series tag `Things Living In Your House`; 5 hashtags). Those two title warnings are accepted. Do not add an emoji or a series tag against the born-as post rule.

### 5. TRUE or FALSE (rule, not a single-title rewrite)

The audit did not replace one current title here. It restated the banned-word rule: never use `TRUE or FALSE`, `Myth`, `Believe`, `Cartoons`, `Lied`, or `Did you know` in a title. Ask the searched question as a statement of fact, and keep the hedge in the body.

No new title was invented to demonstrate the rule. Lint was not run on a made-up title.

## Lint summary

All locked titles that were linted passed with 0 fails. Every stub that includes a YouTube description used the written 11/12 hashtag set (3 topic + `#meatballmyths` + `#shorts`) and drew the same 1 WARN from `postkit.py lint`. The house-cat post title has two extra, accepted WARNs. Second-model check is still required before any of these replace a live or scheduled title.

Keyword suggestions used while reconciling leads are in `/workspace/packaging/kw/kw-studio-assignments.csv` (run 2026-11-15, America/New_York, `postkit.py kw`).
