# Minute-TikTok verdict: do TikTok cuts over 60 seconds beat shorter ones?

Prepared Sun 2026-11-15, about 14:20 ET, for the Fri 11/20 read. This uses only the data in the repo today.
Sources are in `mooneyn60-art/skills`, branch `claude/youtube-monetization-strategy-m9vz6i`. "OM" means `skills/oh-meatball/`.

## Short answer
**No evidence they beat shorter cuts on plays. Watch time: no data.** In the only per-post dataset with lengths, the 61 s+ posts have a *lower* median than the shorter ones. That data is confounded and ends 11/12, so it can't judge the new minute cuts. The minute cuts posted since 11/13 have no play counts logged in the repo yet.

## Plays by length (posts 10/23–11/12)
Source: `OM/research/data/97-tiktok-own-posts.csv` (82 posts; public page pulled 11/12 about 21:47 UTC; columns `length_s`, `plays`, `like_pct`, `style`). I computed the medians.

| Group | n | Median plays | Mean | Range | Median like % |
|---|---|---|---|---|---|
| All posts 61 s or longer | 66 | 221.5 | 455 | 11 – 5,989 | 2.07 |
| All posts under 61 s | 16 | 326 | 379 | 181 – 872 | 1.93 |
| Drawn 60–90 s cuts | 35 | 249 | 461 | 11 – 3,869 | 2.28 |
| Drawn short search-led cuts (15–25 s) | 6 | 367 | 467 | 265 – 872 | 2.72 |
| Drawn sweary 90 s cut | 1 | 299 | — | — | 5.02 |
| Real photo / quiz (Oct), 61 s or longer | 29 | 196 | 459 | 86 – 5,989 | 1.55 |
| Real photo / quiz (Oct), under 61 s | 7 | 229 | 295 | 181 – 510 | 1.44 |

Reading:
- The longer group holds the two biggest animal posts (5,989 and 3,869), so its mean is higher, but its median is lower.
- The short group has only 16 posts (6 in the drawn style). The short search-led cuts also changed their captions and topics at the same time, so length is not isolated.
- An earlier analysis of 81 posts found "Length: no effect on the median" (`skills/channel-brain/KNOWLEDGE.md`, research 91).

## Minute cuts since the rule (Nolan, 11/12: every TikTok over a minute)
| Cut (slot ET) | Length | Plays | Source |
|---|---|---|---|
| Pantry moth minute cut (Thu 11/12 12:00) | 62 s | 240 at 19.7 h; 260 at the 11/15 read | OM/research/102; OM/data/tiktok-stats.csv (id 7707331348586941709; matched to the pantry moth cut by its 240-play count in research 102, not by title) |
| Cat sugar (Fri 11/13 19:00) | 84.8 s | no data | OM/research/data/tiktok-minute-queue.json (length) |
| Grizzly, sweary (Fri 11/13 20:15) | not in the files read | no data | skills/channel-brain/MASTER_ORDERS.md |
| Cat purr (Fri 11/13 21:30) | 86.7 s | no data | tiktok-minute-queue.json |
| Moose (Sat 11/14 19:00) | 89.1 s | no data | tiktok-minute-queue.json |
| Cat name (Sun 11/15 19:00) | 82.2 s | no data (under a day old) | tiktok-minute-queue.json |

`OM/data/tiktok-stats.csv` has no post newer than about 11/13 16:00 ET apart from the news videos (last read 11/15 18:35 UTC).

**Side note: all seven news TikToks run over a minute (65.7–85.4 s)** and are the account's biggest posts (17,600 / 9,340 / 3,457 / 3,034 / 1,426 plays at 40–51 h; `OM/research/117`, lengths in `OM/research/102`). Topic and search drive that, not length. 95–99.7% of views on two of them came from Search (`OM/research/114`), so it says nothing about length.

## Watch time
- **No data for any post.** The account is Personal: Metricool returns nulls and Windsor needs a Business or Creator account. Only the TikTok app's Studio screen shows average watch time, % watched to the end and traffic source (`OM/research/95-next-topics.md`; `skills/channel-brain/MASTER_ORDERS.md`, open ask 1).
- **Creator Rewards qualified views: no data.** Rewards only pays on videos of 1 minute or more (`skills/channel-brain/KNOWLEDGE.md`). So minute cuts are needed for eligibility whatever the plays verdict turns out to be.

## What would settle it by Fri 11/20
1. **Plays at 48 h** (public page reads with `postkit.py ttpage`, logged to `OM/data/tiktok-stats.csv`) for every animal minute cut posted 11/13–11/18, against the account median (333–341; `OM/research/115`; board.json).
   - Posted so far: cat sugar, grizzly, cat purr, moose, cat name.
   - Queued: bison, shark, dog guilty look 11/16 20:15, dog tail wag 11/17, dog stare 11/19, grizzly 11/19 (`OM/data/posted.csv`).
   - Pass bar: a median above 341 across at least 5 minute cuts. Fewer than 5 means decide nothing.
2. **Comparison group:** the 6 drawn short search-led cuts (median 367, `97-tiktok-own-posts.csv`). No new short TikToks are posting, because the rule pulls them to draft (`OM/data/held.csv`). So the comparison stays historical and confounded by date.
3. **Watch time:** one TikTok Studio screenshot per minute cut (see `monetization-tracker.md` for exactly what it must show). With 3 or more, compare average watch time and % watched to the end against video length.
4. **Rewards:** a Creator Rewards screenshot showing qualified views per minute cut.
