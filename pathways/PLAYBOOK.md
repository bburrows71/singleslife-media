# Pathways to Good Life — social playbook

Second brand, managed the same way as Singles Life (see ../PLAYBOOK.md for the shared mechanics:
image post + video post + story per slot, first-comment links, captions, best-time scheduling, weekly report).
Everything here overrides the Singles Life playbook for this brand.

## Metricool
- Brand "pathways2goodlife.com", blogId **7226677**, timezone America/Chicago.
- SAFETY GATE: as of 2026-10-03 this brand is connected to the SAME social accounts as Singles Life
  (blogId 7158515). The owner chose SEPARATE accounts. Before scheduling anything, call getBrandSettings and
  compare each network ID in networksData of 7226677 against 7158515. Only post to networks whose ID is
  DIFFERENT. If none differ, schedule nothing and report: "Waiting for separate Pathways accounts in Metricool."
- Threads is currently "singleslife71" (the Singles Life Instagram's Threads) and Pinterest is "billburrows07"
  (personal). Neither counts as a Pathways account. A network is usable ONLY if its ID differs from Singles
  Life's, its handle does not contain "singles", AND it is listed under "Approved networks" below.
- Approved networks (owner confirmed 2026-10-04, connected their own new Pathways accounts):
  facebook (Page ID 1362549460276464), instagram (pathways2goodlife), youtube (channel UC-LJG2Uxg0ajy5zkYkv6FOA).
  pinterest (07lgwy9fzmk7psp4johf4vrf6nn4uq, owner confirmed 2026-10-04; pin only once the board below exists).
  Not approved: tiktok and threads (not connected on this brand).
- Pinterest needs a board: use the board named "Pathways to Good Life"; if missing, skip Pinterest
  (2026-10-04, 2026-10-06 and 2026-10-08: board not found, Metricool could not resolve it; owner asked to create it). Pin = cover slide as a separate pinterest-only post,
  pinTitle = hook, pinLink https://pathways2goodlife.com/.
- 2026-10-10: board NAME still unresolvable, but the owner's own Pathways pin draft uses boardId 1107674539542383834;
  Claude used that ID for the Oct 11 pin (accepted). Use it unless the owner says otherwise.

## Cadence
- FLOOD: 14 days of daily posting, 2 slots/day (main + evening), starting the first day this brand actually
  posts. Record that date here as `Flood start:` the first time posts are scheduled.
- WEEKLY afterwards: every Friday, fill the next 7 days with 1 main slot per day.
- Flood start: 2026-10-05 (flood runs through 2026-10-18)

## Brand
- Pathways to Good Life (pathways2goodlife.com). Coach: Bill Burrows. Tagline: "Less clutter. Fewer cycles. More you."
  Closing line: "Simple isn't easy. It's just lighter."
- "Plainspoken coaching for people rebuilding on their own terms: breaking old relationship patterns,
  owning less, and running a steady life on one set of shoulders."
- Voice: warmer and more personal than Singles Life; first person from Bill is fine when quoting him.
  Coaching, not therapy: never diagnose, never promise outcomes. No invented stats, studies, testimonials.
- Four entry points: "I keep pushing good people away" / "I repeat the same mistakes" /
  "My life feels cluttered and loud" / "I'm starting over on my own".
- Three work areas: Relationship patterns (come-here go-away cycle, misdirected anger, testing the people who
  love you); Owning less (letting go of things and the habits that refill the closet); A steady solo life
  (one income, one household, one person keeping it all running).
- Bill: "Change is possible for anyone. Is it easy? No. But it can be done." … "be true to yourself and your
  feelings, be honest about the inner struggles most of us learn to hide, and keep your daily life simple
  enough that you have room to do that work."

## Sources (only these)
- pathways2goodlife.com (home sections, journal at /#journal: check for new posts and add them here).
- The Freedom Paradox ($129, one payment): 8 chapters, 10 lessons, 90-day follow-up. Chapters: The Invisible
  Wall (free preview), The Roots of Withdrawal, The Retaliation Trap, Redefining Freedom vs. Connection,
  The Integration Blueprint, bonus content. Includes Emergency Toolkit, self-assessment quiz, partner guide,
  private student community. Link: pathways2goodlife.com (course section) or
  bill-s-site-680c.thinkific.com/products/courses/the-freedom-paradox
- Singles Life articles (the site is built from them) on relationship patterns, habits, cycles, letting go and
  starting over: misdirected-destruction, root-of-misdirected-destruction, pattern-quiz, root-cause-reflection,
  breaking-the-cycles, life-harvest, habits, letting-go-of-things, after-divorce (singles-life.app/<name>.html).
  Re-angle them for coaching; link to pathways2goodlife.com, not singles-life.app.
- Don't post the same idea on both brands within 7 days: check ../log.json too.
- 2026-10-09 run: live WebFetch of pathways2goodlife.com and singles-life.app is blocked in unattended runs (permission
  prompt unanswered). Every idea in the text recorded here was used by one of the brands within 7 days, so Oct 9
  was skipped. Fix: allow those domains for the scheduled task, or save article text under pathways/sources/.
- 2026-10-09 (for Oct 10): same block again (WebFetch permission withdrawn; sites not in web search). Oct 10 main +
  evening skipped. Ideas used Oct 5 (intro, simple-isn't-easy) free up again from Oct 12.
- 2026-10-10 (for Oct 11): fetch blocked again; both slots built from pathways/sources/the-wisdom-of-speaking-less.md
  (main: listen first / nature listens first; evening: the speaking-without-listening loop). The owner's own
  draft quote card for that article ("We learn very little when we listen very little") sits in Metricool as a draft.
- Course posts: at most 3 per week on this brand (it's the main offer), never two days in a row.

## Look
- Render with `python3 pathways/render.py SPEC OUTDIR` (themes ink / paper / sage; Young Serif headlines,
  Figtree body, marigold path mark). Video: `python3 make_video.py pathways/posts/X 4 1D2B3A`.
- Posts live in pathways/posts/<DATE or DATE-pm>/, log in pathways/log.json.

## Captions
- Hook, 3-6 short lines, soft CTA to pathways2goodlife.com "(link in bio)", 5 hashtags
  (e.g. #lifecoaching #breakingcycles #simpleliving #attachmentstyles #startingover — vary them).

## What's working
- 2026-10-05: No data yet (first Pathways posts go live Oct 5). Video posts = YouTube Short only (IG trial reels
  fail the follower requirement on the sister account). Pinterest board still missing. Report: reports/2026-10-05.md
