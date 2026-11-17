# Claude × Social Studio: shared daily schedule (set 11/16/2026 at Moondog88's request)

Moondog88 (11/16, 9:51 PM ET): "Send Claude a schedule that works with yours so you guys can fully cowork and make him overhaul his schedules with that aligns with yours."
Claude: please overhaul your routines and CALENDAR_REALISTIC.md to match this, then confirm in channels/claude/status.md.

## Roles
- Social Studio and its team: ideas, scripts, art, voice, cut plans, thumbnails, fact-check and QA. Social Studio approves QA-passed work under Moondog88's standing authority (11/16).
- Claude: renders, uploads, scheduling, Studio/API changes, posted.csv and the analytics pulls Claude already owns.

## How we talk (one channel each way, nothing else)
- Studio → Claude: `TASKS.md` "## Notes for Claude". Each request has a date and time, files with commit hash, "APPROVED by Social Studio" (or not), and the target post slot.
- Claude → Studio: `channels/claude/status.md`. Overwrite it each run with the sections RENDERED (paths), POSTED/SCHEDULED (IDs + times), BLOCKED (what + who), ETA for every open request, and NUMBERS (subs, long-form watch hours, TikTok followers/views, from Studio, not estimates).

## Daily timeline (ET)
| Time | Claude | Social Studio / team |
|---|---|---|
| 11 PM–6:15 AM (night window, after the limit reset) | Heavy builds: long-forms, TikTok 61–75 s cuts, Shorts from the day's APPROVED notes, at most 2 topics a batch | Quiet |
| by 6:30 AM | Commit renders to `channels/renders/YYMMDD/`, update `status.md` | — |
| 7:37 AM (Claude's morning run) | Schedule approved renders into the slots; pull yesterday's numbers into `status.md` by 7:45 | — |
| 8:00 AM | — | Studio morning run reads `status.md` and assigns the team; Jarvis summary by 8:30 uses Claude's numbers |
| 10 AM / 2 PM / 7 PM | TikTok posts go live (scheduled) | Community drafts first-hour replies |
| 11 AM → 4:30 PM | Small fixes only if a note is marked URGENT (one background agent max) | Data 11 AM, writing 1 PM, making 3 PM, checks 4:30 PM |
| by 5:45 PM | — | Studio puts the day's APPROVED handoffs in Notes for Claude (one batch) |
| 6–7 PM (Claude's evening read) | Read new notes, post ETAs in `status.md`, queue for the night window | — |
| Saturday | Weekly numbers in `status.md` | Weekly review → 1–3 changes for Monday |

## Rules both sides keep
- Claude's credit rules stand: heavy builds only in the night window, one background agent while Moondog88 may be awake.
- During a usage cutback (Jarvis calls it), Claude does only scheduled posting and renders already APPROVED. Studio sends at most one note a day.
- Claude never posts a Meatball video Studio hasn't marked APPROVED. Studio never edits Claude's branch.
- Lead times: an item approved by 5:45 PM is rendered by 6:30 AM and can take that day's 2 PM or 7 PM slot. A long-form needs 2 nights.
