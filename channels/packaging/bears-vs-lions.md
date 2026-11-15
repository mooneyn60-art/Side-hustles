# Bears vs Lions (animals, not the teams) — packaging draft

**DRAFT PENDING.** MASTER_ORDERS and research 116: nothing is built until Nolan picks. This file is packaging only. No script, render, schedule, post, repo edit, commit, or push.

Suggested window if he picks option B (research 116): TikTok and Short out Wednesday 11/25/2026 evening, America/New_York, or Thursday 11/26/2026 morning, before the 1:00 pm ET kickoff. A long "who would win" video is possible only if the Short shows demand. Option A (Rams vs Cardinals as the animals, 11/15) is already in the past and is not packaged here.

## Conflicts and holds

- MASTER_ORDERS: nothing built until Nolan picks. This draft stays pending.
- Title and first line say it is the animals. No `#nfl` tag. No logos, helmets, uniforms, team colors as marks, players, or league marks. No score pick or betting. The game may be named once as a dated fact (research 116 rules).
- Social Studio audit opened Yellowstone / NPS grizzly speed and weight figures and Smithsonian lion weights on 11/15. **Those numbers are not in `research/116-bears-vs-lions.md`.** This draft does not use them. Facts below come only from research 116 and from `postkit.py kw`.
- The audit itself said lion running speed still needs a source; do not use a number. This draft uses no speed or weight at all.
- Do not invent a winner. Research 116: "Weights, speed and bite force from primary sources; no invented winner."
- TikTok hashtags in this file follow Studio's 3 topic + `#meatballmyths`. MASTER_ORDERS still says five topic hashtags and no brand tag. See `tiktok-caption-template.md`. Do not post the caption until that is resolved.
- Would Meatball Survive? episode number is not assigned (`posted.csv` has bison as `#5` on Sat 11/21 11:00 ET). The title uses the series tag without a number.
- Related-video target depends on when this Short actually runs. See `related-video-rule.md`. This is a WMS Short; if it lands on 11/25 evening or 11/26 morning the newest long-form in the queue is Night Shift v2 (house show), which is off-topic under MASTER_ORDERS "on-topic Shorts" / show-playlist rule.

## YouTube title

`Bear vs Lion Who Would Win: The Animals, Not the Teams 🐻 (Would Meatball Survive?)`

83 UTF-16 units. Searched words (`bear vs lion who would win`) sit in the first 40 characters. The title itself says it is the animals. Lint (`/workspace/packaging/lint-specs/title-bears-vs-lions.json`): pass, 0 fail, 1 hashtag WARN, title 83 of 100.

## YouTube description

Bear vs lion who would win? This is the animals, not the football teams. The Bears play at the Lions on Thanksgiving, Thursday 11/26/2026, at 1:00 pm ET (CBS), per research 116. That pack does not yet have primary-source weights, speed, or bite force, so this draft does not pick a winner and does not give those figures.

#bearvslion #grizzlybear #lion #meatballmyths #shorts

Sources: skills/oh-meatball/research/116-bears-vs-lions.md (skills branch claude/youtube-monetization-strategy-m9vz6i). General information, not safety training.

## Tags (10, each ≤30 characters, from `postkit.py kw`)

Keyword file: `/workspace/packaging/kw/kw-studio-assignments.csv` (run 2026-11-15, America/New_York).

1. bear vs lion who would win
2. grizzly bear vs lion
3. polar bear vs lion
4. brown bear vs lion
5. black bear vs lion
6. grizzly bear vs lion fight
7. grizzly bear versus lion
8. bear versus lion
9. would meatball survive
10. Meatball Myths

Omitted on purpose: `bears vs lions`, `bears vs lions thanksgiving`, highlights, week, tickets, and year tags. Those suggestions are football. No `#nfl` and no NFL tags. `grizzly bear vs lion who would win` is 34 characters and fails the 30-character cap. `polar bear vs lion who would win` and `brown bear vs lion who would win` were shortened to the forms above that still appear in the suggestion list. The video, once built, must actually mention a polar, brown, or black bear before those tags stay; if the script is only grizzly vs African lion, drop the extra species tags in the next draft.

## TikTok caption (Studio shape; pending the hashtag decision)

`postkit.py lint` on `lint-specs/tt-bears-vs-lions-studio.json` (TikTok mode) first FAILed without the survival disclaimer in the caption. The line "General info, not safety training." is now in the body, before the closing question. After that fix: 1 FAIL gone; remaining 1 WARN is the 4-hashtag Studio shape vs lint's five topic tags. That WARN is the same conflict as `tiktok-caption-template.md`, not a new wording problem.

```
bear vs lion who would win?

This is the animals, not the teams. The Bears play at the Lions on Thanksgiving, Thursday 11/26/2026, at 1:00 pm ET. This draft does not pick a winner: research 116 still needs primary-source weights, speed, and bite force. General info, not safety training. Would you rather watch the animals or the game?
#bearvslion #grizzlybear #lion #meatballmyths
```

The last question is a choice, not a yes/no about a winner. If MASTER_ORDERS wins the hashtag fight, drop `#meatballmyths` and add two more topic tags the script actually answers, after the fact pack exists.

## Pinned comment

If they met in the wild, what would you want measured first: weight, speed, or bite? Full list in the Related video 👆

Open question, not yes/no. The Related-video line is for an on-topic Short once a target long-form exists. If this Short stays off-topic to the then-newest long-form, drop the Related-video sentence or retarget per `related-video-rule.md`.

## Facts in the repo (research 116 only)

- Game: Bears at Lions, Thanksgiving Day, Thursday 11/26/2026, 1:00 pm ET, CBS. Source in the pack: web search of the 2026 NFL schedule, 11/14. They do not meet before that.
- The animal search "bear vs lion who would win" has year-round YouTube demand. The team phrase spikes in game week but its results are football.
- YouTube suggestions recorded in the pack: "bears vs lions", "bears vs lions thanksgiving", "bear vs lion who would win", "polar bear vs lion who would win", "grizzly bear vs lion who would win".
- Build the video to win the animal search and use the game as the hook and the timing.

## Facts still needed before a script or a tighter description

These are gaps, not license to fill them from the canvas:

1. Which bear and which lion (grizzly? brown? African lion? the pack does not pick).
2. Primary-source adult weights, with the range and the hedge, for both animals.
3. Primary-source running speed for the bear, and a source for the lion (do not invent a lion speed).
4. Bite force, only if a primary source is opened.
5. A spoken line that no test of this matchup exists, if a source supports saying that; do not add "Nobody has tested it" until it is sourced.
6. Fact pack, script, second-model check, Would Meatball Survive? number, and Nolan's pick of option B (or not).
