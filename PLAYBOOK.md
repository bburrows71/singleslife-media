# Singles Life — daily social playbook

This repo holds the images for Singles Life's daily Facebook + Instagram posts, scheduled through Metricool
(brand "Singles-Life", blogId 7158515, timezone America/Chicago). Images must stay public: Metricool and
Instagram fetch them from `https://raw.githubusercontent.com/bburrows71/singleslife-media/main/...`.

## Brand
- Singles Life (singles-life.app): a practical toolkit for people living on their own: bill reminders,
  safety check-ins, home maintenance reminders. Tagline: "Single life, made simple."
- Audience: adults running a household alone, including people newly single or post-divorce.
- Voice: honest, plainspoken, reassuring, a little dry. Not cutesy, not preachy, no "self-care queen" talk.
  Talk like a capable friend. Short sentences. No invented statistics, studies, quotes or app features.
  Only mention app features listed above.

## Content sources (use these, not generic tips)
Every post is built from the owner's own material, quoting or closely paraphrasing it. Never invent facts.
- singles-life.app articles: budgeting.html, after-divorce.html, habits.html, live-alone-safely.html,
  living-alone-checklist.html, letting-go-of-things.html, misdirected-destruction.html,
  root-of-misdirected-destruction.html, pattern-quiz.html, root-cause-reflection.html,
  breaking-the-cycles.html, life-harvest.html (blog index: singles-life.app/blog.html — check for new ones).
- The Freedom Paradox course (Thinkific, $129): bill-s-site-680c.thinkific.com/products/courses/the-freedom-paradox
  Modules: The Invisible Wall; The Roots of Withdrawal; The Retaliation Trap; Redefining Freedom vs. Connection;
  The Integration Blueprint. Bonuses: workbooks, Emergency Toolkit, self-assessment quiz, partner guide,
  90-day follow-up module, private community (Freedom Paradox Circle). Free preview available.
  Headline: "Stop Chasing. Stop Withdrawing. Start Connecting." Course posts 1-2x per week max.
- Each caption ends with the article URL (or course URL). Slides say "on the blog at singles-life.app"
  rather than long URLs.

## Approval
Posts go into Metricool as DRAFTS (draft: true). The owner approves/publishes them in Metricool.

## Content pillars (rotate; never the same pillar two days running)
1. Home upkeep: seasonal checklists, quick fixes, what to keep on hand.
2. Money on one income: budgeting, bills, saving, splitting nothing with anyone.
3. Safety when you live alone: check-ins, emergency info, locks, letting someone know.
4. Solo routines & habits: cooking for one, weekly resets, keeping the place running.
5. Starting over: practical first steps after a breakup/divorce/move; tone is steady, never mopey.
6. Letting go / minimalism: owning less, decluttering, making space yours.

## Weekly format rhythm (America/Chicago)
- Mon, Wed, Fri, Sun: carousel (5-7 slides: cover, 3-4 point slides or a checklist, cta).
- Tue, Thu, Sat: single image (statement or checklist), sometimes a 2-3 slide mini carousel.
- Tie in the calendar where it is natural (season, month start = bills, holidays, daylight saving).

## Caption rules
- Hook line first, 3-6 short lines of value, then a soft CTA (save / share / singles-life.app).
- Instagram: 5-8 relevant hashtags at the end. Facebook: 0-2 hashtags.
- Same images go to both networks; captions are written once, hashtags trimmed for Facebook if posting
  as separate posts. When posting both in one Metricool post, use the Instagram caption with 5 hashtags.

## How a day is produced
1. Read `log.json` (newest last) so topics and hooks don't repeat within 30 days.
2. Write `posts/YYYY-MM-DD/spec.json` (see render.py docstring for slide types) and the caption.
3. `python3 render.py posts/YYYY-MM-DD/spec.json posts/YYYY-MM-DD` → JPEGs 1080x1350.
4. Look at the images; fix any overflow or awkward wrap before publishing.
5. Commit + push to main. Confirm each raw URL returns 200.
6. Schedule in Metricool with createScheduledPost: providers facebook + instagram, media = raw URLs in
   slide order, instagramData.type POST, facebookData.type POST, autoPublish true, at the best hour from
   getBestTimeToPostByNetwork (instagram) for that date, between 9 AM and 7 PM.
7. Append an entry to `log.json` and push.
