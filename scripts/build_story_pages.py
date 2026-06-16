import os

OUT_DIR = "/Users/josh/Projects/joshberrington-site/mockup/work"

STYLE = """
  :root {
    --bg: #fafafa;
    --bg-raised: #f0eee8;
    --text: #1f1d1c;
    --text-muted: #5c5855;
    --border: #d6d3d2;
    --accent: #d15010;
  }
  html.dark {
    --bg: #0a0908;
    --bg-raised: #161413;
    --text: #f5f3f0;
    --text-muted: #9c9690;
    --border: #2e2c2b;
    --accent: #ee6018;
  }
  * { box-sizing: border-box; }
  html, body { margin: 0; padding: 0; }
  body {
    background: var(--bg);
    color: var(--text);
    font-family: 'Geist', sans-serif;
    line-height: 1.6;
    transition: background-color 0.25s ease, color 0.25s ease;
  }
  h1, h2, h3 { font-family: 'Geist', sans-serif; font-weight: 600; letter-spacing: -0.02em; }
  .mono { font-family: 'Geist Mono', monospace; }
  a { color: inherit; }
  .container { max-width: 680px; margin: 0 auto; padding: 0 24px; }
  nav {
    position: sticky; top: 0; z-index: 50;
    background: var(--bg); border-bottom: 1px solid var(--border);
    transition: background-color 0.25s ease, border-color 0.25s ease;
  }
  .nav-inner {
    display: flex; align-items: center; justify-content: space-between;
    padding: 18px 24px; max-width: 920px; margin: 0 auto;
  }
  .nav-name { font-size: 1.05rem; font-weight: 600; text-decoration: none; }
  .nav-links { display: flex; align-items: center; gap: 28px; font-size: 0.88rem; color: var(--text-muted); }
  .nav-links a { text-decoration: none; transition: color 0.2s; }
  .nav-links a:hover { color: var(--text); }
  .theme-toggle {
    width: 42px; height: 24px; border-radius: 12px; background: var(--border);
    position: relative; cursor: pointer; border: none; padding: 0; flex-shrink: 0;
  }
  .theme-toggle::after {
    content: ""; position: absolute; top: 3px; left: 3px; width: 18px; height: 18px;
    border-radius: 50%; background: var(--bg); box-shadow: 0 1px 2px rgba(0,0,0,0.2);
    transition: transform 0.25s ease;
  }
  html.dark .theme-toggle::after { transform: translateX(18px); }

  .back-link {
    display: inline-flex; align-items: center; gap: 6px;
    font-size: 0.88rem; color: var(--text-muted); text-decoration: none;
    margin: 40px 0 28px;
  }
  .back-link:hover { color: var(--text); }

  .story-eyebrow {
    display: inline-flex; align-items: center;
    font-family: 'Geist Mono', monospace;
    font-size: 0.72rem; letter-spacing: 0.06em; text-transform: uppercase;
    color: var(--accent); background: var(--bg-raised); border: 1px solid var(--border);
    padding: 6px 12px; border-radius: 999px;
    margin-bottom: 18px; font-weight: 500;
  }
  .story-title { font-size: 2.3rem; line-height: 1.15; margin: 0 0 16px; }
  .story-meta { font-size: 0.92rem; color: var(--text-muted); margin: 0 0 36px; }

  .story-hero-img {
    width: 100%; aspect-ratio: 16/9; object-fit: cover;
    border-radius: 20px; margin-bottom: 40px;
  }
  .story-stat-hero {
    border-radius: 20px; margin-bottom: 40px; padding: 48px 32px;
    background: var(--bg-raised); border-left: 2px solid var(--accent);
    text-align: center;
  }
  .story-stat-hero .stat {
    font-family: 'Geist Mono', monospace; font-size: 2.2rem; color: var(--accent);
    margin: 0; letter-spacing: -0.01em;
  }

  .story-body { font-family: 'Newsreader', serif; font-size: 1.18rem; line-height: 1.75; }
  .story-body p { margin: 0 0 26px; }

  footer {
    border-top: 1px solid var(--border); padding: 40px 0; margin-top: 40px;
    font-size: 0.88rem; color: var(--text-muted);
    display: flex; justify-content: space-between; flex-wrap: wrap; gap: 12px;
  }
  footer a { text-decoration: none; }
  footer a:hover { color: var(--text); }
"""

SCRIPT = """
  const toggle = document.getElementById('themeToggle');
  const root = document.documentElement;
  const stored = localStorage.getItem('theme');
  if (stored === 'light') root.classList.remove('dark');
  else root.classList.add('dark');
  toggle.addEventListener('click', () => {
    root.classList.toggle('dark');
    localStorage.setItem('theme', root.classList.contains('dark') ? 'dark' : 'light');
  });
"""

def page(slug, title, eyebrow, meta, paragraphs, hero_img=None, hero_alt="", stat=None, back_anchor="#work", back_label="Back to work"):
    body_html = "\n".join(f"      <p>{p}</p>" for p in paragraphs)
    if hero_img:
        hero_html = f'<img class="story-hero-img" src="{hero_img}" alt="{hero_alt}" />'
    else:
        hero_html = f'<div class="story-stat-hero"><p class="stat">{stat}</p></div>'
    return f"""<!DOCTYPE html>
<html lang="en" class="dark">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>{title} — Josh Berrington</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Newsreader:ital,opsz,wght@0,6..72,300;0,6..72,400;0,6..72,500;0,6..72,600;1,6..72,400&family=Geist:wght@300;400;500;600;700&family=Geist+Mono:wght@400;500;600&display=swap" rel="stylesheet">
<style>{STYLE}</style>
</head>
<body>

<nav>
  <div class="nav-inner">
    <a class="nav-name" href="../index.html">Josh Berrington</a>
    <div class="nav-links">
      <a href="../index.html#work">Work</a>
      <a href="../index.html#experience">Experience</a>
      <a href="../index.html#ai-work">AI Work</a>
      <a href="#" aria-disabled="true">Writing</a>
      <button class="theme-toggle" id="themeToggle" aria-label="Toggle dark mode"></button>
    </div>
  </div>
</nav>

<div class="container">
  <a class="back-link" href="../index.html{back_anchor}">&larr; {back_label}</a>

  <div class="story-eyebrow">{eyebrow}</div>
  <h1 class="story-title">{title}</h1>
  <p class="story-meta">{meta}</p>

  {hero_html}

  <div class="story-body">
{body_html}
  </div>
</div>

<footer>
  <div class="container" style="display:flex; justify-content:space-between; flex-wrap:wrap; gap:12px; width:100%; max-width:920px;">
    <span>&copy; 2026 Josh Berrington</span>
    <span><a href="https://www.linkedin.com/in/joshberrington" target="_blank" rel="noopener">LinkedIn</a></span>
  </div>
</footer>

<script>{SCRIPT}</script>
</body>
</html>
"""

pages = {
    "amazon-aware.html": dict(
        title="Zero to Market in Nine Months",
        eyebrow="Amazon · Private Brands · 2021–2024",
        meta="A CEO-level priority, a global pandemic, and a brand built from nothing.",
        hero_img="https://res.cloudinary.com/dflbkiog6/image/upload/joshberrington-site/AA_H_HomeRefresh_2x1_V05_Full.jpg",
        hero_alt="Amazon Aware campaign imagery",
        paragraphs=[
            "Amazon Aware wasn't a side project or a slide in someone else's strategy deck &mdash; it was an S-Team level priority, a CEO-driven initiative to launch Amazon's first sustainability-led brand, and it had to go from PR/FAQ to in-market reality in nine months. I was the founding go-to-market marketing lead, which meant the brand didn't exist yet when I started, and the clock was already running.",
            "The timing made it harder, not easier. We were still in the middle of COVID, working through supply chain disruptions on top of everything else that comes with inventing a brand from nothing &mdash; positioning, sourcing, packaging, channel strategy, all of it standing up at once, on a deadline set well above my level.",
            "We tested loudly instead of waiting for certainty: messaging, positioning, and channel strategy iterated against real purchase behavior rather than research decks. By the end of year one, Amazon Aware was overindexing 3&ndash;4x against Amazon's private label averages, pulling 34% of glance views and 29% of revenue through marketing-driven channels alone.",
            "The lesson that stuck with me: speed and credibility aren't actually in tension if you're willing to test in public and adjust faster than the constraints around you change.",
        ],
    ),
    "amazon-essentials.html": dict(
        title="Repositioning the Largest Brand in the Portfolio",
        eyebrow="Amazon · Private Brands · 2021–2024",
        meta="Brand strategy, research, and a total repositioning for Amazon's largest softlines brand.",
        hero_img="https://res.cloudinary.com/dflbkiog6/image/upload/joshberrington-site/DG_FW21_Womens_On_Dresses_Shot20_190_FINAL.jpg",
        hero_alt="Amazon Essentials campaign imagery",
        paragraphs=[
            "Amazon Essentials is the largest softlines brand on Amazon.com, generating well into the hundreds of millions in annual revenue. I came on as the global marketing lead for the brand with a clear mandate: reposition it, refresh it, and make the strategy underneath it as strong as the business it was supporting.",
            "That meant starting from the ground up &mdash; foundational customer research, a new brand strategy, and selecting the global creative agency of record we'd build the next chapter with. It also meant work that never became visible externally: evaluating how Essentials sat alongside sister brands in the Private Brands portfolio, and building the case to consolidate investment behind Essentials specifically rather than spreading it thin.",
            "The repositioning itself touched every layer of the brand: identity, voice and tone, the entire visual language, messaging and positioning strategy, and merchandising and storefront presentation. Not a refresh of one piece &mdash; a complete rebuild of how the brand shows up everywhere a customer encounters it.",
            "What I'm proudest of isn't the creative people eventually saw &mdash; it's the strategic groundwork underneath it that made that creative inevitable rather than a guess.",
        ],
    ),
    "dove-body-wash.html": dict(
        title="The Brand That Wrote the Playbook",
        eyebrow="Unilever · Dove · 2018–2019",
        meta="Landing at the brand that shaped how I think about marketing, right out of business school.",
        hero_img="https://res.cloudinary.com/dflbkiog6/image/upload/joshberrington-site/SR_Dream_Y3_campaign_181022.jpg",
        hero_alt="Dove campaign imagery",
        paragraphs=[
            "Dove was a brand I admired long before I worked there &mdash; even before business school, I thought of it as the brand that had written the playbook for what best-in-class CPG marketing actually looks like. Landing there in 2018, straight out of business school, felt less like a job and more like getting to study inside the textbook.",
            "My role was global marketing lead for Dove's new formats &mdash; everything outside the core body wash and bar business: shower foams, bath bombs, and the formats that came after. I owned the five-year innovation roadmap for that portfolio, including Dove Shower Foam, which had recently launched and was already finding real traction in market.",
            "Working inside a &euro;2 billion global business teaches you a specific kind of discipline &mdash; every decision sits inside a much longer roadmap than the campaign in front of you, and getting that balance right, on a brand this influential, was the best classroom I could have asked for early in my career.",
        ],
    ),
    "sheamoisture-men.html": dict(
        title="A Brand Rebuilt on Cultural Truth",
        eyebrow="Unilever · SheaMoisture · 2019–2021",
        meta="What happens when deep cultural understanding meets real marketing rigor.",
        hero_img="https://res.cloudinary.com/dflbkiog6/image/upload/joshberrington-site/Ross_Moisturizing_Shampoo_056%2B%25281%2529.jpg",
        hero_alt="SheaMoisture Men campaign imagery",
        paragraphs=[
            "I joined SheaMoisture Men about two years into my time at Unilever, stepping into a business and a community I deeply respected and admired &mdash; but wasn't from. The brand had been neglected: revenue was declining, shelf space was eroding, and a stale innovation pipeline was losing ground to P&amp;G and a wave of upstart challengers.",
            "I could have approached the turnaround as a pure numbers problem. Instead, the real work was understanding the culture this brand actually belonged to &mdash; not as a demographic to target, but as a community to genuinely understand, with real curiosity and respect for an experience that wasn't mine. I built the five-year innovation roadmap, then rebuilt positioning, channel strategy, messaging, and the full content plan around that understanding.",
            "The business results followed: revenue grew roughly 5x in under eighteen months, alongside real gains in distribution and social reach. Several campaigns were recognized in Ad Age and other outlets for resonating authentically within the community, and the products themselves picked up industry awards for their formulations.",
            "But the growth was the output, not the point. The story I actually wanted to tell was about what happens when a brand is built on cultural appreciation and celebration instead of a generic playbook applied to a new audience &mdash; the business case turned out to be the proof, not the motivation.",
        ],
    ),
}

AI_OUT_DIR = "/Users/josh/Projects/joshberrington-site/mockup/ai"

ai_pages = {
    "multi-agent-system.html": dict(
        title="A Team of Six, and Only One of Me",
        eyebrow="Amazon · Alexa Smart Home · 2024–Present",
        meta="6 agents, 10 reusable skills, and a marketing org's output from a single IC.",
        stat="6 agents · 10 skills",
        paragraphs=[
            "At some point I stopped asking whether AI could help with one task and started asking what a marketing team built entirely out of agents would actually look like. The answer became a six-agent system &mdash; a copywriter, a GTM strategist, an executive writer, a researcher, and a data analyst, each one scoped tightly enough to be reliable, coordinated tightly enough to act like a team.",
            "The point was never novelty. It was throughput. Ten reusable skills sit underneath the agents, so the same system that drafts a competitive briefing this week can turn around an executive narrative next week, without being rebuilt each time. Work that used to take a team weeks &mdash; messaging development, competitive intelligence, executive reporting &mdash; now moves in hours, run by one person.",
            "What surprised me wasn't that the agents could do the work. It was how much of my own job turned out to be orchestration once I stopped doing the writing myself &mdash; deciding what good output looks like, catching where a model's confidence outruns its judgment, and building the scaffolding that makes six independent agents behave like a single accountable system.",
        ],
    ),
    "agent-marketplace.html": dict(
        title="Built Once, Used by Everyone",
        eyebrow="Amazon · Alexa Smart Home · 2024–Present",
        meta="A self-serve platform that took AI adoption from days of setup to immediate use.",
        stat="Division-wide",
        paragraphs=[
            "Every time I built something useful with AI, the next question was always the same: can someone else on the team use this without me. That question became the Agent Marketplace &mdash; an internal, self-serve platform of pre-configured agents, skills, and workflows that anyone could download, configure locally, and run immediately.",
            "The design constraint I cared most about was zero dependency. If a tool only works because the person who built it is on standby to support it, it doesn't scale &mdash; it just relocates the bottleneck. So every agent in the marketplace had to stand on its own, with onboarding for tools like Kiro and Claude Code dropping from days of manual configuration to something closer to instant.",
            "It's now in active use across SDE, design, and GTM in a multi-hundred-person division &mdash; people I've never spoken to, running tools I built, without needing me in the loop. That's the outcome I was actually optimizing for.",
        ],
    ),
    "ai-enablement.html": dict(
        title="From One Proposal to a Self-Sustaining Program",
        eyebrow="Amazon · Alexa Smart Home · 2024–Present",
        meta="A capability gap, a VP-approved proposal, and a program that no longer needs me.",
        stat="9 &rarr; 18 &rarr; self-sustaining",
        paragraphs=[
            "I noticed the gap before there was a program to fix it: the org was excited about AI in the abstract but had no structured way to actually build fluency at scale. So I wrote the proposal myself &mdash; not a request for resources, but a specific plan for a cross-org AI enablement initiative &mdash; and took it to VP-level approval.",
            "The core team grew from 9 to 18 people within a year, but the number that actually mattered came later: roughly a dozen colleagues now independently lead org-wide weekly trainings, and SDE, design, and GTM teams build and deploy their own AI tools without any ongoing support from the original team. I also designed the division's first AI adoption measurement system &mdash; tracking attitudes, usage, and impact on a quarterly cadence &mdash; so the program's success wouldn't rely on anecdote.",
            "A program that still needs its founder a year in hasn't actually succeeded. The best evidence this one worked is how little anyone needs me for it now.",
        ],
    ),
    "messaging-pipeline.html": dict(
        title="One Command, Where an Agency Used to Be",
        eyebrow="Amazon · Alexa Smart Home · 2024–Present",
        meta="A five-stage pipeline that replaced a four-week, agency-dependent process.",
        stat="4 weeks &rarr; one command",
        paragraphs=[
            "The old way of developing messaging looked like this: brief an agency, wait, review, revise, wait again &mdash; roughly four weeks from kickoff to usable output, every time, for every brief. I wanted to know how much of that timeline was actually necessary versus just how the process had always worked.",
            "The answer became a five-stage automated pipeline: brief intake, concept generation, synthetic consumer testing, research synthesis, and optimized output &mdash; triggered by a single command. It doesn't replace human judgment at the end of the process, but it replaces the weeks of back-and-forth that used to happen before a human ever saw a real option to react to.",
            "It's now in active use across the team. The bigger shift wasn't the time saved on any one brief &mdash; it was that messaging development stopped being a scheduling problem dependent on an outside partner's calendar, and became something we could run again the moment new information came in.",
        ],
    ),
}

os.makedirs(OUT_DIR, exist_ok=True)
for filename, content in pages.items():
    html = page(
        slug=filename,
        title=content["title"],
        eyebrow=content["eyebrow"],
        meta=content["meta"],
        hero_img=content["hero_img"],
        hero_alt=content["hero_alt"],
        paragraphs=content["paragraphs"],
    )
    with open(os.path.join(OUT_DIR, filename), "w") as f:
        f.write(html)
    print(f"wrote work/{filename}")

os.makedirs(AI_OUT_DIR, exist_ok=True)
for filename, content in ai_pages.items():
    html = page(
        slug=filename,
        title=content["title"],
        eyebrow=content["eyebrow"],
        meta=content["meta"],
        stat=content["stat"],
        paragraphs=content["paragraphs"],
        back_anchor="#ai-work",
        back_label="Back to AI work",
    )
    with open(os.path.join(AI_OUT_DIR, filename), "w") as f:
        f.write(html)
    print(f"wrote ai/{filename}")
