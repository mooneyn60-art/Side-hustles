# Monetization tracker: Meatball Myths (update weekly)

Started Sun 2026-11-15. Sources are in `mooneyn60-art/skills`, branch `claude/youtube-monetization-strategy-m9vz6i`, unless marked. "OM" means `skills/oh-meatball/`, "CB" means `skills/channel-brain/`.

**Targets:**
- **YouTube YPP (ads):** 1,000 subs plus either 4,000 public long-form watch hours in 12 months or 10M valid public Shorts views in 90 days.
- **New YPP applicants from 2027-02-01:** 8,000 hours or 20M Shorts views.
- **YouTube lower tier (fan funding and Shopping, no ads):** 500 subs plus 3,000 hours or 3M Shorts views.
- **TikTok Creator Rewards:** pays on original videos of 1 minute or more that reach 1,000 qualified For You views.
- Source for all of the above: `CB/KNOWLEDGE.md`, "Verified platform facts".

| Metric | Value | As of | Source | Target |
|---|---|---|---|---|
| YouTube subscribers | 1,010 (public count, rounded by YouTube) | 2026-11-14 | OM/data/board/board.json (kpis `yt_subs`) | 1,000 ✔ |
| Long-form public watch hours, 12 months | **no data** | — | (proxy only: 10.4 h in the last 28 days, Windsor, 11/14, `OM/data/board/notes.json` and `OM/data/longform-hours.csv`; Studio 28-day figure 10.6 h on 11/11, `CB/KNOWLEDGE.md`) | 4,000 (8,000 for applications from 2/1/2027) |
| Valid public Shorts views, 90 days | **no data** | — | (proxy only: 65,778 Shorts views in the last 28 days, Studio paste 11/11, `CB/KNOWLEDGE.md`) | 10M (20M from 2/1/2027) |
| TikTok followers | 9,323 | 2026-11-14 | OM/data/board/board.json (kpis `tt_followers`, public profile) | 10,000 was the Rewards join rule; already joined (`CB/MASTER_ORDERS.md`) |
| TikTok qualified For You views | **no data** | — | (related: For You share was 4.1% and 0.0% on two news TikToks, Nolan's Studio screenshots 11/13, `OM/research/114`) | 1,000 per eligible video |
| TikTok Creator Rewards earnings | **no data** | — | (open ask in `OM/data/board/notes.json`) | — |

## Screenshots needed to fill the gaps
1. **YouTube Studio → Earn (monetization) tab.** The YPP eligibility card must show, with today's date visible:
   - Subscribers (exact count)
   - **Public watch hours (last 365 days)**
   - **Valid public Shorts views (last 90 days)**
   - Which tier the channel is eligible for, if any
2. **YouTube Studio → Analytics → Overview, "Last 365 days".** Must show views and watch time (hours) for the period.
   - Optional, as a cross-check on hour 1 above: the Content tab split into Videos against Shorts. Only long-form hours count toward the 4,000.
3. **TikTok app → Profile → TikTok Studio → Creator Rewards Program dashboard.** Must show:
   - Estimated rewards for the period, with the date range
   - **Qualified views** for the period
   - The per-video list with qualified views and rewards for each eligible video. At minimum, the big airline video ("Why the Ground Stop Happened") and the newest animal minute cuts (cat sugar, cat purr, moose, cat name).
   - This also answers whether search views pay (open ask in `OM/data/board/notes.json`).
4. **TikTok app → TikTok Studio → Analytics → Overview (last 28 days).** Must show:
   - Video views
   - Followers (net and total)
   - Traffic source split (For You, Search, Following, Profile, other) for the period
5. **TikTok app → TikTok Studio → Analytics → Content → tap one video (one screenshot per minute cut; at least 3 for Friday's verdict).** Must show:
   - Video length
   - **Average watch time**
   - **Watched full video %**
   - **Traffic sources** (For You against Search)
   - This is the existing open ask 1 in `CB/MASTER_ORDERS.md`.

## Weekly update steps
- Copy the four Earn and Analytics numbers in with the screenshot date.
- Keep the public counts from `OM/data/board/board.json` (refreshed by the daily scoreboard run).
- Write "no data" wherever a screenshot is missing.
