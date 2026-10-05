# Singles Life — daily social playbook

This repo holds the images and videos for Singles Life's social posts (Facebook, Instagram, TikTok, YouTube), scheduled through Metricool
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
  breaking-the-cycles.html, life-harvest.html, going-in-the-right-direction.html, truth-makes-you-free.html,
  single-life-research.html (added 2026-10-03) (blog index: singles-life.app/blog.html — check for new ones).
- The Freedom Paradox course (Thinkific, $129): bill-s-site-680c.thinkific.com/products/courses/the-freedom-paradox
  Modules: The Invisible Wall; The Roots of Withdrawal; The Retaliation Trap; Redefining Freedom vs. Connection;
  The Integration Blueprint. Bonuses: workbooks, Emergency Toolkit, self-assessment quiz, partner guide,
  90-day follow-up module, private community (Freedom Paradox Circle). Free preview available.
  Headline: "Stop Chasing. Stop Withdrawing. Start Connecting." Course posts 1-2x per week max.
- Each caption ends with the article URL (or course URL) followed by "(link in bio)" — the Instagram bio links to singles-life.app/blog.html. Slides say "on the blog at singles-life.app"
  rather than long URLs.

## Networks (from 2026-10-03: Claude runs the whole Metricool brand)
- Connected in Metricool: Facebook Page, Instagram (singleslife71), TikTok (singles.life4), YouTube.
- Every slot gets TWO Metricool posts at the same hour:
  1. Image post -> facebook + instagram (slides as a carousel/single image).
  2. Video post -> tiktok + youtube (Short): `python3 make_video.py posts/X` turns the same slides into a
     1080x1920 MP4 (4s per slide, crossfade, silent track). Caption = hook + 2-3 lines + "singles-life.app" +
     5 hashtags (no long URLs; they aren't clickable there). youtubeData: type short, privacy public,
     title = hook (<= 90 chars) + " #shorts", 5-8 tags, category PEOPLE_BLOGS, madeForKids false.
     tiktokData: PUBLIC_TO_EVERYONE, commercialContentOwnBrand true, title = short hook, autoAddMusic false.
  Also add instagram to the video post as a TRIAL REEL (instagramData {"type":"TRIAL_REEL","isAiGenerated":false};
     shown to non-followers first, so it finds new people without repeating the feed post to followers).
     If Metricool rejects TRIAL_REEL, drop instagram from the video post and note it in the run report.
     2026-10-05: Instagram rejected the Oct 4 trial reels at publish time ("does not meet the trial reel follower
     requirement"). Until the account grows, do NOT add instagram to new video posts (video = tiktok + youtube only).
  3. Story (MAIN slot only) -> instagram + facebook, 1 hour after the main post: media = the cover slide (01.jpg),
     instagramData {"type":"STORY"}, facebookData {"type":"STORY"}, and NO text field (stories have no caption).
- First comment: on every image post (facebook + instagram) set firstCommentText to
  "Read the full piece: <article or course URL>" so Facebook gets a clickable link right under the post.
- Threads / LinkedIn / Pinterest: not connected yet. When getBrandSettings shows threads or linkedin, add them
  to the image post. Pinterest needs a board name written here first.

## Weekly report (Mondays)
Pull the last 7 days for facebook, instagram, tiktok and youtube with getAnalyticsAvailableMetrics /
getAnalyticsDataByMetrics. Write reports/YYYY-MM-DD.md: followers gained, reach/views, engagement, top 3 posts
and why, what to do more/less of. Update "What's working" at the bottom of this file. Never invent numbers.
Put a 5-line plain-English summary at the top of that run's final report (the owner gets it as a push notification).

## Approval
Owner switched to AUTO-POSTING on 2026-10-03: posts are created with draft false, autoPublish true.
The owner can still edit or delete anything in the Metricool planner before it goes out.

## Cadence
- FLOOD (runs through 2026-10-15, posts through 2026-10-16): 2 posts per day.
  Morning main post (carousel or single, ~9-12 AM best hour) + evening post (~6-8 PM best hour):
  a single statement, checklist or 2-3 slide mini carousel from a DIFFERENT source than that day's main post.
- WEEKLY (from Friday 2026-10-16): every Friday, fill the next 7 days with 1 post per day.

## Content pillars (rotate; never the same pillar two days running)
1. Home upkeep: seasonal checklists, quick fixes, what to keep on hand.
2. Money on one income: budgeting, bills, saving, splitting nothing with anyone.
3. Safety when you live alone: check-ins, emergency info, locks, letting someone know.
4. Solo routines & habits: cooking for one, weekly resets, keeping the place running.
5. Starting over: practical first steps after a breakup/divorce/move; tone is steady, never mopey.
6. Letting go / minimalism: owning less, decluttering, making space yours.

## Weekly format rhythm for main posts (America/Chicago)
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

## What's working
- 2026-10-05: Not enough data yet (first posts went live Oct 4). Facebook/Instagram image posts, stories and
  TikTok/YouTube Shorts all publish fine; Instagram Trial Reels fail (follower requirement). Report: reports/2026-10-05.md
