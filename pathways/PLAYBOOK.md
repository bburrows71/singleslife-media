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
- FLOOD ran 2026-10-05 to 2026-10-18 (2 slots/day).
- Flood start: 2026-10-05 (flood runs through 2026-10-18)
- DAILY from 2026-10-20 (owner, 2026-10-19: "Keep doing daily posts but I want them different. I keep seeing the same posts reposted").
  The weekly/Friday mode is cancelled. Every run schedules TOMORROW: exactly ONE post per day. Mondays also do the weekly report.

## Daily format: one piece per network per day (no reposting the same thing in several formats)
- Alternate by day of month: EVEN dates = REEL day, ODD dates = CAROUSEL day.
  - REEL day: one video post -> instagram REEL with showReelOnFeed TRUE + facebook REEL + youtube Short. No image post, no story, no pin.
  - CAROUSEL day: one image post -> instagram + facebook carousel (firstCommentText "Read more: <article URL>");
    a separate youtube-only Short of the same slides (YouTube is a different audience); a Pinterest pin of the cover (board below). No IG Reel, no story.
- Time: REEL days 18:00 (best Reel so far went out at 6 PM); CAROUSEL days best hour 9-13 (fallback 10:00). Metricool best-time data is still all 0.
- No Stories, no evening slot. If a network rejects a format (e.g. facebook REEL), drop that network for that piece and note it here.

## Variety rules (hard)
- Every post is built from ONE specific section of ONE article in pathways/sources/ (or a newly fetched Journal post, saved there first).
  Name the article + section in log.json "source".
- Never reuse a hook, quote or idea that appears in pathways/log.json in the last 30 days, or in ../log.json in the last 7 days.
- The same article at most twice in any 7 days, and never the same section twice in 30 days. Rotate articles; never the same article two days running.
- Stock brand lines (tagline "Less clutter. Fewer cycles. More you.", "Simple isn't easy. It's just lighter.", "Change is possible...", the four entry-point sentences,
  the course chapter list) were used to death in the flood: do NOT use them as hooks; at most one stock line per week, as a sign-off only.
- Course mentions at most 2/week, never on consecutive days, always second to the idea. Pattern-post CTA can be the free pattern quiz (pathways2goodlife.com/pattern-quiz.html).
- Each run first tries WebFetch on pathways2goodlife.com to find new Journal posts and saves notes for any new one under pathways/sources/.
  If fetch is blocked, use pathways/sources/ (7 articles as of 2026-10-19; plenty for 30+ distinct posts).

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
- 2026-10-12 (for Oct 13): fetch blocked again. Main built from pathways/sources/the-wisdom-of-speaking-less.md (leave room to learn);
  evening = Bill's "Change is possible" quote recorded above. NEW Journal post seen only in the owner's own Metricool drafts
  for Oct 13 (not read by Claude): "The Groove My Mind Wore Into the Floor" (pathways2goodlife.com/the-groove-my-mind-wore-into-the-floor.html).
  Save its text under pathways/sources/ so runs can use it.
- 2026-10-13 (for Oct 14): fetch blocked again (groove article too). Main from pathways/sources/the-wisdom-of-speaking-less.md (discipline of quiet);
  evening = Bill's "be honest about the inner struggles" quote. Unused angles left in that source: "enter the room ready to receive" and
  "speak when words add clarity, encouragement, truth, or warning" (both close to Oct 13 ideas; free from Oct 20). Source text is running out.
- 2026-10-14 (for Oct 15): fetch blocked again (groove article too). Main = "I keep pushing good people away" entry point + three pattern
  names + soft Freedom Paradox mention (course post 1 of this week); evening = owning less / habits that refill the closet. Both from text recorded here.
- 2026-10-15 (for Oct 16): fetch blocked again (groove article too). Main = tagline carousel "Less clutter. Fewer cycles. More you." (three work areas);
  evening = Bill's "keep your daily life simple enough that you have room to do that work" quote. Recorded text is now nearly used up within 7 days.
- 2026-10-16 (for Oct 17): fetch blocked again (home + groove article). Main = "I repeat the same mistakes" entry point + Freedom Paradox chapter list
  (course post 2 of week Oct 12-18); evening = steady solo life "one income, one household, one set of shoulders". Unused recorded text left for Oct 18:
  "My life feels cluttered and loud" (close to Oct 15-16 clutter ideas) and "I'm starting over on my own" (Singles Life used starting over Oct 10; free from Oct 17).
- 2026-10-17 (for Oct 18, last flood day): fetch blocked again (groove article; sites absent from web search). Main = "Do you test the people who love you?"
  (best Oct 6 performer, >7 days) + Bill's "be true to yourself and your feelings"; evening = "I'm starting over on my own" + closing line.
  Every recorded idea has now been used within the last 14 days. Weekly mode starts; first batch Fri Oct 23 needs NEW source text in pathways/sources/.
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
- 2026-10-12 (week Oct 5-11): Instagram 2 -> 9 followers. Off-grid IG Reels carry reach ("Talking without listening is a loop."
  138 views / 132 reached); feed carousels reach 1-7 each. Best feed post: "Do you test the people who love you?" (6 interactions).
  Course-first post weakest. Facebook 0 followers / 0 views. YouTube 103 views Oct 5-8. Pattern / self-recognition hooks win.
  Owner's own drafts may sit in the planner (e.g. Oct 13 10:00): schedule around them, never on top. Report: reports/2026-10-12.md
- 2026-10-19 (week Oct 12-18): Instagram 13 -> 78 followers (+47, mostly Oct 17-18). Reels still carry reach: "I'm starting over on my own."
  (Oct 18 pm) 106 views / 102 reached; other Reels 3-12 views. Best feed: "Be honest about the inner struggles..." (Oct 14) 18 views / 5 interactions.
  First-person entry-point sentences + Bill's honesty quotes win; course-chapter-list hooks are weakest. Facebook 0 followers, ~0 views.
  YouTube 190 views Oct 12-16, 0 subs. New owner Journal post seen in IG: pathways2goodlife.com/right-or-close.html ("Do I want to be right
  here, or do I want to be close?"), not yet readable by unattended runs. Report: reports/2026-10-19.md
