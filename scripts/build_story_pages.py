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

  .story-topbar {
    display: flex; align-items: center; justify-content: space-between;
    flex-wrap: wrap; gap: 12px 16px; margin: 40px 0 28px;
  }
  .back-link {
    display: inline-flex; align-items: center; gap: 6px;
    font-size: 0.88rem; color: var(--text-muted); text-decoration: none;
  }
  .back-link:hover { color: var(--text); }

  .story-eyebrow {
    display: inline-flex; align-items: center;
    font-family: 'Geist Mono', monospace;
    font-size: 0.72rem; letter-spacing: 0.06em; text-transform: uppercase;
    color: var(--accent); background: var(--bg-raised); border: 1px solid var(--border);
    padding: 6px 12px; border-radius: 999px;
    font-weight: 500;
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

  .story-gallery-wrap { margin: 40px 0 0; }
  .story-gallery {
    display: flex; align-items: flex-end; justify-content: center; gap: 26px;
  }
  .story-gallery img { display: block; height: auto; cursor: zoom-in; transition: opacity 0.2s ease; }
  .story-gallery img:hover { opacity: 0.88; }
  .story-gallery .gallery-desktop {
    width: 62%; border-radius: 12px; border: 1px solid var(--border);
    box-shadow: 0 10px 34px rgba(0,0,0,0.20);
  }
  .story-gallery .gallery-mobile { width: 28%; }
  .story-caption {
    font-family: 'Geist Mono', monospace; font-size: 0.76rem; letter-spacing: 0.03em;
    color: var(--text-muted); text-align: center; margin: 18px 0 0;
  }
  @media (max-width: 560px) { .story-gallery { gap: 14px; } }

  .lightbox {
    position: fixed; inset: 0; z-index: 100;
    display: flex; align-items: center; justify-content: center;
    padding: 5vmin;
    background: rgba(10, 9, 8, 0.25);
    -webkit-backdrop-filter: blur(8px) saturate(120%);
    backdrop-filter: blur(8px) saturate(120%);
    opacity: 0; visibility: hidden;
    transition: opacity 0.32s ease, visibility 0.32s ease;
    cursor: zoom-out;
  }
  .lightbox.open { opacity: 1; visibility: visible; }
  .lightbox img {
    max-width: 100%; max-height: 100%;
    transform: scale(0.94);
    transition: transform 0.32s cubic-bezier(0.22, 1, 0.36, 1);
    cursor: default;
  }
  .lightbox img.is-desktop {
    border-radius: 16px;
    box-shadow: 0 24px 70px rgba(0, 0, 0, 0.45);
  }
  .lightbox.open img { transform: scale(1); }
  .lightbox-close {
    position: fixed; top: 22px; right: 26px;
    width: 42px; height: 42px; border-radius: 50%;
    border: 1px solid var(--border);
    background: var(--bg-raised); color: var(--text);
    font-size: 1.4rem; line-height: 1; cursor: pointer;
    display: flex; align-items: center; justify-content: center;
    transition: border-color 0.2s ease, transform 0.2s ease;
  }
  .lightbox-close:hover { border-color: var(--text-muted); transform: scale(1.06); }

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

  (function () {
    const imgs = document.querySelectorAll('.story-gallery img');
    if (!imgs.length) return;
    const box = document.createElement('div');
    box.className = 'lightbox';
    box.innerHTML = '<button class="lightbox-close" aria-label="Close">&times;</button><img alt="" />';
    document.body.appendChild(box);
    const big = box.querySelector('img');
    const openBox = (src, alt, isDesktop) => {
      big.src = src; big.alt = alt || '';
      big.className = isDesktop ? 'is-desktop' : '';
      box.classList.add('open');
      document.body.style.overflow = 'hidden';
    };
    const closeBox = () => {
      box.classList.remove('open');
      document.body.style.overflow = '';
    };
    imgs.forEach((im) => {
      im.addEventListener('click', () => openBox(im.currentSrc || im.src, im.alt, im.classList.contains('gallery-desktop')));
    });
    box.addEventListener('click', (e) => { if (e.target !== big) closeBox(); });
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape' && box.classList.contains('open')) closeBox();
    });
  })();
"""

def page(slug, title, eyebrow, meta, paragraphs, hero_img=None, hero_alt="", stat=None, back_anchor="#work", back_label="Back to work", gallery=None):
    body_html = "\n".join(f"      <p>{p}</p>" for p in paragraphs)
    if hero_img:
        hero_html = f'<img class="story-hero-img" src="{hero_img}" alt="{hero_alt}" />'
    else:
        hero_html = f'<div class="story-stat-hero"><p class="stat">{stat}</p></div>'
    if gallery:
        gallery_html = f"""
  <figure class="story-gallery-wrap">
    <div class="story-gallery">
      <img class="gallery-desktop" src="{gallery['desktop']}" alt="{gallery['desktop_alt']}" />
      <img class="gallery-mobile" src="{gallery['mobile']}" alt="{gallery['mobile_alt']}" />
    </div>
    <figcaption class="story-caption">{gallery['caption']}</figcaption>
  </figure>"""
    else:
        gallery_html = ""
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
      <button class="theme-toggle" id="themeToggle" aria-label="Toggle dark mode"></button>
    </div>
  </div>
</nav>

<div class="container">
  <div class="story-topbar">
    <a class="back-link" href="../index.html{back_anchor}">&larr; {back_label}</a>
    <div class="story-eyebrow">{eyebrow}</div>
  </div>
  <h1 class="story-title">{title}</h1>
  <p class="story-meta">{meta}</p>

  {hero_html}

  <div class="story-body">
{body_html}
  </div>{gallery_html}
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
        hero_img="https://res.cloudinary.com/dflbkiog6/image/upload/joshberrington-site/DG_FW21_Womens_On_Dresses_Shot20_190_FINAL.jpg",
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
        meta="Six months of research, a creator-led collaboration model, and a total repositioning for Amazon's largest softlines brand.",
        hero_img="https://res.cloudinary.com/dflbkiog6/image/upload/joshberrington-site/AA_H_HomeRefresh_2x1_V05_Full.jpg",
        hero_alt="Amazon Essentials campaign imagery",
        paragraphs=[
            "One of the hardest marketing assignments isn't rescuing a failing brand &mdash; it's inheriting one that looks healthy on the surface while quietly losing ground underneath. That was the situation I stepped into as Global Marketing Lead for Amazon Essentials. By top-line measures the brand was performing, but a closer read of the data told a more complicated story: a brand in need of repositioning, modernization, and a genuine creative identity.",
            "The central tension was knowing how much change to introduce without eroding what was already working. Refreshes fail when they overcorrect &mdash; when the pursuit of newness breaks the trust customers have already extended. The discipline isn't boldness alone; it's knowing exactly where to be bold and where to hold steady. To answer that, we invested over six months in deep customer and brand research &mdash; understanding where Essentials was delighting customers, where it was falling short, and where it had no real right to compete at all. That became the strategic foundation: a clear map of where to pivot, where to double down, and where to deliberately step back.",
            "From there we wrote the brief that went to our agency, AKQA Amsterdam &mdash; and the work extended well beyond a visual rebrand. This was a holistic reconsidering of the brand: product strategy, hero SKU and ASIN prioritization, and creator and cultural strategy. We weren't just refreshing an identity; we were building the infrastructure for a brand that could grow.",
            "One of the most significant outputs was the concept of celebrity and creator-led collaborations. I helped lead the pitch for a partnership with a major creator and cultural tastemaker with genuine resonance in the brand's space. It exceeded expectations on every dimension, and more importantly it proved a repeatable model: what began as a single partnership evolved into a new business unit, enabling a broader slate of creator-led drops and collaborations going forward.",
            "The before-and-after is stark. Amazon Essentials was originally built out of commercial necessity &mdash; a private label play offering quality basics under the Amazon umbrella. It launched with a logo and a typeface, but without a soul: no narrative, no world-building, no emotional architecture for customers to connect with. What exists now is a fully considered brand &mdash; a visual identity, a clear point of view, a storytelling framework, and a cultural calendar anchored by seasonal drops, fabric stories, and texture narratives. In a category that's crowded, commoditized, and largely undifferentiated at the brand level, that depth gives Essentials a position that feels both credibly rooted in the category and distinctly its own &mdash; the kind of thing that's hard to replicate and durable over time.",
        ],
        gallery=dict(
            desktop="https://res.cloudinary.com/dflbkiog6/image/upload/joshberrington-site/ae_desktop.png",
            desktop_alt="Repositioned Amazon Essentials storefront on desktop",
            mobile="https://res.cloudinary.com/dflbkiog6/image/upload/joshberrington-site/ae_mobile.png",
            mobile_alt="Repositioned Amazon Essentials storefront on mobile",
            caption="The repositioned storefront, live across desktop and mobile.",
        ),
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
    "alexa-smart-home.html": dict(
        title="Leading GTM for AI-Powered Smart Home",
        eyebrow="Amazon · Alexa Smart Home · 2024–Now",
        meta="The launch narrative for Alexa+ Smart Home, and the agent infrastructure built to support it.",
        hero_img="https://res.cloudinary.com/dflbkiog6/image/upload/joshberrington-site/alexa-smart-home.png",
        hero_alt="Alexa smart home devices and services",
        paragraphs=[
            "I lead go-to-market strategy for Alexa Smart Home's AI-powered hardware and software features &mdash; the layer of the business where the devices people already trust in their homes start getting genuinely smarter. That includes owning the launch narrative for Alexa+ Smart Home, the division's flagship AI moment at CES 2026, where the story had to land with press, partners, and customers all at once.",
            "Bringing an AI-native product to market requires a different motion than a traditional hardware launch: the value isn't a spec sheet, it's a behavior change, and the narrative has to make an invisible, evolving capability feel concrete enough to want. That meant rebuilding the GTM playbook itself &mdash; positioning, proof points, and sequencing &mdash; for a product that keeps getting smarter after it ships.",
            "The work didn't stop at the narrative. To move at the speed AI products demand, I built a six-agent AI system to compress my own workflow, then rebuilt it as a self-serve agent platform so SDE, design, and GTM teams across the division could do the same. What started as a personal productivity tool is now infrastructure other teams build on.",
            "The thread connecting both: in an AI-native world, marketing leaders can't just narrate the transformation &mdash; they have to be early, credible practitioners of it.",
        ],
    ),
}

AI_OUT_DIR = "/Users/josh/Projects/joshberrington-site/mockup/ai"

ai_pages = {
    "dictate.html": dict(
        title="Speak It, Ship It",
        eyebrow="Amazon · Alexa Smart Home · 2024–Present",
        meta="A local, privacy-first voice-to-text tool for Windows &mdash; built in two days with Claude Code, by a non-engineer.",
        stat="Built in 2 days",
        paragraphs=[
            "At home, on my personal Mac, I'd gotten used to speaking my prompts to Claude Code instead of typing them. Conversational, paragraph-long instructions are faster to say than to type, and a tool called Wispr Flow made it effortless. Then I'd sit down at my Windows machine at work and that entire workflow vanished &mdash; there was no local, PC-native equivalent. So instead of filing it under things I wished existed, I built one.",
            "Dictate lives in the system tray: double-tap Alt to start, tap to stop, and the transcription drops straight into whatever window is in front of you &mdash; a terminal, an editor, a chat box. The thing I cared about most is that it all runs on the machine. Audio never leaves the PC; it's transcribed locally. That's the difference between a tool you can actually use for sensitive work and one that's a compliance problem from day one. It ships as a single installer with nothing else to wrangle.",
            "Here's the part I keep coming back to: I'm a product marketer, not a software engineer, and this is a native app written in Rust, talking to low-level Windows APIs, running a local speech model as a subprocess. I didn't write that code &mdash; Claude Code did. My job was the product: what it should do, where it should be sharp, what to leave out. Two days from idea to a working installer. The barrier to building real software used to be knowing how. Increasingly, it's just knowing what you want and being willing to direct it.",
        ],
        gallery=dict(
            desktop="https://res.cloudinary.com/dflbkiog6/image/upload/joshberrington-site/dictate_desktop.png",
            desktop_alt="Dictate landing page on desktop",
            mobile="https://res.cloudinary.com/dflbkiog6/image/upload/joshberrington-site/dictate_mobile.png",
            mobile_alt="Dictate landing page on mobile",
            caption="The Dictate landing page, across desktop and mobile.",
        ),
    ),
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
        gallery=content.get("gallery"),
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
        gallery=content.get("gallery"),
    )
    with open(os.path.join(AI_OUT_DIR, filename), "w") as f:
        f.write(html)
    print(f"wrote ai/{filename}")
