"""Week of Oct 4-10, 2026: posts built from singles-life.app articles and The Freedom Paradox course.
Run: python3 plan/week-2026-10-04.py  -> writes posts/DATE/spec.json + caption.txt for each day."""
import json, pathlib
ROOT = pathlib.Path(__file__).resolve().parent.parent
COURSE = "bill-s-site-680c.thinkific.com/products/courses/the-freedom-paradox"

POSTS = [
 {"date": "2026-10-04", "slug": "2026-10-04-live-alone-safely", "source": "https://singles-life.app/live-alone-safely.html",
  "pillar": "Safety", "format": "carousel",
  "slides": [
   {"type": "cover", "theme": "pine", "kicker": "Living alone safely", "title": "Safe at home, on your own",
    "sub": "Not paranoid. Just prepared. Four small routines from our living-alone safety checklist."},
   {"type": "point", "theme": "chalk", "n": "1", "title": "The 30-second door routine",
    "body": "Lock it the moment you walk in. Keys in the same spot every time. One slow sweep before you leave: door, windows, appliances."},
   {"type": "point", "theme": "chalk", "n": "2", "title": "Make your address known",
    "body": "Emergency contacts as one-tap favorites. Your full address and building code written where you can find it fast."},
   {"type": "point", "theme": "chalk", "n": "3", "title": "Check in with someone daily",
    "body": "Agree on a loose window with one person, like a text by 9pm. Tell them when you travel and when you're back."},
   {"type": "statement", "theme": "highlight", "text": "Not the locks, but the quiet agreement that *someone* is paying attention to your normal."},
   {"type": "cta", "theme": "pine", "title": "Read the full checklist.",
    "body": "Six routines, including a plan for your first night alone. It's on the blog at singles-life.app"}],
  "caption": """Living alone safely isn't about being scared. It's about being set up.

From our living-alone safety checklist:
🔑 The 30-second door routine: lock it the moment you're in, keys in one spot
📍 Your address and emergency contacts one tap away
💬 A daily check-in with one person, even just "home safe" by 9pm

"You're not a person managing alone. You're a person managing, full stop."

Full checklist: singles-life.app/live-alone-safely.html

#livingalone #livingalonesafely #solohome #singlelife #safetytips"""},

 {"date": "2026-10-05", "slug": "2026-10-05-single-income-budget", "source": "https://singles-life.app/budgeting.html",
  "pillar": "Money", "format": "carousel",
  "slides": [
   {"type": "cover", "theme": "pine", "kicker": "One income", "title": "Budgeting on a single income",
    "sub": "No second paycheck to absorb the surprises. Here's how to build a budget that holds anyway."},
   {"type": "checklist", "theme": "chalk", "title": "Start with 50 / 30 / 20",
    "items": ["50% needs: rent, utilities, groceries", "30% wants: dining out, hobbies", "20% savings and debt payoff"],
    "note": "First, track what you really spend. Most people underestimate food and subscriptions."},
   {"type": "point", "theme": "chalk", "n": "1", "title": "Build the cushion first",
    "body": "Three to six months of essentials is the goal. If that feels far off, start with $500 to $1,000 so one bad week doesn't land on a credit card."},
   {"type": "point", "theme": "chalk", "n": "2", "title": "Pay yourself first",
    "body": "Set an automatic transfer to savings the day your paycheck lands. Don't wait to save whatever's left at month's end."},
   {"type": "point", "theme": "chalk", "n": "3", "title": "Hunt the recurring costs",
    "body": "Audit subscriptions every few months. Negotiate internet and insurance. Ask your utility about budget billing."},
   {"type": "cta", "theme": "pine", "title": "Small habits beat big moves.",
    "body": "All nine steps for a one-income household are on the blog at singles-life.app"}],
  "caption": """No second income to absorb the surprises? Then the budget has to do the work.

Start here:
• 50/30/20: needs, wants, savings and debt
• Build a $500–$1,000 cushion before anything else
• Pay yourself first, automatically, on payday
• Audit subscriptions and renegotiate fixed bills

"Small, consistent habits tend to matter more than any single big decision."

All nine steps: singles-life.app/budgeting.html

#singleincome #budgeting #moneytips #livingalone #singlelife"""},

 {"date": "2026-10-06", "slug": "2026-10-06-misdirected-destruction", "source": "https://singles-life.app/misdirected-destruction.html",
  "pillar": "Starting over", "format": "single", "label": "Misdirected destruction",
  "slides": [
   {"type": "statement", "theme": "pine",
    "text": "The relationship was never what was causing the feeling. It was just the *nearest thing* to break.",
    "attribution": "From Misdirected Destruction"}],
  "caption": """Ever blown up something that was actually working?

Sometimes it isn't the relationship. It's a pain inside that needs somewhere to go, and the relationship is simply the nearest thing to break. The sudden exit. The fault-finder. The chaos creator. The wall.

Sabotaging past relationships doesn't mean you're unlovable. It means you were trying to survive a pain you didn't yet understand.

Read it, then take the 2-minute quiz to find your pattern: singles-life.app/misdirected-destruction.html

#selfsabotage #relationshippatterns #healing #singleseason #singlelife"""},

 {"date": "2026-10-07", "slug": "2026-10-07-freedom-paradox", "source": "https://" + COURSE,
  "pillar": "Course", "format": "carousel", "footer": "The Freedom Paradox",
  "slides": [
   {"type": "cover", "theme": "pine", "kicker": "The Freedom Paradox", "title": "Come here. Go away.",
    "sub": "If you pull people close and then push them out, you're not broken. You're caught in a cycle, and cycles can be interrupted."},
   {"type": "statement", "theme": "highlight", "text": "Stop chasing. Stop withdrawing. *Start connecting.*"},
   {"type": "checklist", "theme": "chalk", "title": "Five modules",
    "items": ["The Invisible Wall", "The Roots of Withdrawal", "The Retaliation Trap", "Redefining Freedom vs. Connection", "The Integration Blueprint"]},
   {"type": "point", "theme": "chalk", "title": "Built from experience",
    "body": "\"The Freedom Paradox came out of my own struggle with these issues, not from studying them at a distance.\" Bill Burrows, course creator"},
   {"type": "cta", "theme": "pine", "title": "Watch the free preview.",
    "body": "Workbooks, an Emergency Toolkit, a 90-day follow-up module and a private community. Find it on Thinkific: The Freedom Paradox."}],
  "caption": f"""Pull them close. Push them away. Repeat.

If that "come here, go away" cycle sounds familiar, The Freedom Paradox was made for you. It's a 5-module course grounded in attachment and nervous-system research, turned into a practical, step-by-step path.

Inside: companion workbooks, an Emergency Toolkit, a self-assessment quiz, a guide to share with your partner, a 90-day follow-up module and a private community.

Freedom and closeness were never a trade-off.

Free preview: {COURSE}

#attachmentstyles #relationshiphealing #avoidantattachment #selfgrowth #thefreedomparadox"""},

 {"date": "2026-10-08", "slug": "2026-10-08-letting-go", "source": "https://singles-life.app/letting-go-of-things.html",
  "pillar": "Letting go", "format": "single", "label": "Letting go",
  "slides": [
   {"type": "checklist", "theme": "highlight", "title": "Start putting things down",
    "items": ["One drawer, closet or shelf", "Wait 30 days on non-essentials", "Unsubscribe from store emails", "One in, one out"],
    "note": "Before you buy, ask: is this for you, or for what someone else will think?"}],
  "caption": """You were born owning nothing, and you were still smiling.

More stuff rarely survives the week as a good feeling. Most things cost you twice: once to buy, then again to store, maintain and replace.

Four ways to start:
1. One drawer, closet or shelf
2. A 30-day wait on non-essentials
3. Unsubscribe from retail emails
4. One in, one out

What you get back isn't just space. It's peace.

singles-life.app/letting-go-of-things.html

#minimalism #declutter #simpleliving #livingalone #singlelife"""},

 {"date": "2026-10-09", "slug": "2026-10-09-habit-loop", "source": "https://singles-life.app/habits.html",
  "pillar": "Habits", "format": "carousel",
  "slides": [
   {"type": "cover", "theme": "pine", "kicker": "Habits", "title": "Why bad habits win when you're tired",
    "sub": "Every bad habit started as a choice. Repeat it enough and it starts choosing for you."},
   {"type": "checklist", "theme": "chalk", "title": "The habit loop",
    "items": ["Cue: stress, boredom, a time, a place", "Routine: the automatic behavior", "Reward: what your brain gets"],
    "note": "Willpower and decisions draw on the same limited tank. Tired = low tank."},
   {"type": "point", "theme": "chalk", "n": "1", "title": "Add friction",
    "body": "Make the bad routine harder to reach. Delete the app. Move the trigger out of sight."},
   {"type": "point", "theme": "chalk", "n": "2", "title": "Same cue, new routine",
    "body": "If stress is the cue, decide ahead of time what you'll do instead, so something better fires first."},
   {"type": "point", "theme": "chalk", "n": "3", "title": "Plan for low moments",
    "body": "Change your surroundings and decide your response to fatigue before you're tired. A reminder is a cue you place on purpose."},
   {"type": "cta", "theme": "pine", "title": "Change the loop, not your willpower.",
    "body": "The full breakdown is on the blog at singles-life.app"}],
  "caption": """Why do bad habits always win at 10pm?

Because willpower and decision-making draw on the same tank, and by the end of the day it's low. The habit doesn't need willpower. That's the whole point of a habit.

So stop fighting it head-on. Change the loop:
• Add friction to the bad routine
• Give the same cue a better routine
• Change your environment
• Decide your low-energy plan in advance

singles-life.app/habits.html

#habits #breakingbadhabits #selfimprovement #routine #singlelife"""},

 {"date": "2026-10-10", "slug": "2026-10-10-after-divorce", "source": "https://singles-life.app/after-divorce.html",
  "pillar": "Starting over", "format": "single", "label": "After divorce",
  "slides": [
   {"type": "statement", "theme": "pine",
    "text": "Keeping it together looks like showing up messy and *still showing up.*",
    "attribution": "Keeping your head together after divorce"}],
  "caption": """"Keeping it together" doesn't mean feeling nothing.

It's showing up messy and still showing up. Still eating. Still sleeping something close to normal.

A few things that help, from our divorce guide:
• Don't leave the first weekends blank. Plan one small ritual that's yours.
• Mute or unfollow. Don't rely on resisting at midnight.
• Rebuild structure: sleep, meals, movement.
• Reaching out isn't the weak move.

singles-life.app/after-divorce.html

#divorcerecovery #lifeafterdivorce #startingover #singleagain #singlelife"""},
]

if __name__ == "__main__":
    for p in POSTS:
        d = ROOT / "posts" / p["date"]; d.mkdir(parents=True, exist_ok=True)
        spec = {"slug": p["slug"], "label": p.get("label", "Tip of the day"), "footer": p.get("footer", "singles-life.app"), "slides": p["slides"]}
        (d / "spec.json").write_text(json.dumps(spec, indent=1, ensure_ascii=False))
        (d / "caption.txt").write_text(p["caption"])
    (ROOT / "plan" / "week-2026-10-04.json").write_text(json.dumps([{k: v for k, v in p.items() if k != "slides"} for p in POSTS], indent=1, ensure_ascii=False))
    print("ok")
