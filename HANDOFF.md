# Handoff — joshberrington.com personal site

_Last updated: 2026-06-24_

## What this is
Static personal/portfolio site. Hand-written HTML/CSS, no build step. Type system:
Geist + Geist Mono + Newsreader (serif body on story pages). Images hosted on Cloudinary.
Repo: `joshberrington-git/joshberrington-site`. Deployed via **GitHub Pages** (classic,
"deploy from `main`", served from repo root).

## Hosting / domain
- Primary URL (once DNS finishes propagating): **https://joshberrington.com** (apex primary; `www` redirects to apex)
- GitHub Pages URL: https://joshberrington-git.github.io/joshberrington-site/
- DNS at **Network Solutions**: apex `A` → `185.199.108.153` / `.109` / `.110` / `.111`; `www` `CNAME` → `joshberrington-git.github.io`
- `CNAME` file in repo root = `joshberrington.com`
- **Status (2026-06-24 night):** authoritative DNS is correct; waiting on the old Squarespace
  2-hour TTL to expire in public caches (incl. GitHub's resolver). Once it does, GitHub
  verifies the domain and auto-issues HTTPS. Then enable **Enforce HTTPS** in Settings → Pages.
- Domain was moved off **Squarespace** (Squarespace site still exists in the account, just no longer pointed).

## Structure
- `index.html` — homepage (hero, brand/GTM work grid, experience timeline, Selected AI works terminal)
- `work/` — 5 case studies: `alexa-smart-home`, `amazon-aware`, `amazon-essentials`, `dove-body-wash`, `sheamoisture-men`
- `ai/` — 3 linked AI works: `dictate`, `multi-agent-system`, `agent-marketplace`
  (`messaging-pipeline` file still exists but is dropped, see "Dropped" below)
- `assets/cloudinary_manifest.json` — uploaded image URLs
- `scripts/upload_to_cloudinary.py` — uploads + appends to manifest (reads `.env` `CLOUDINARY_URL`); `build_story_pages.py` — generates story pages
- `.env` (gitignored) — `CLOUDINARY_URL`

## Conventions (established this session)
- **No em dashes in prose** (use commas / colons / periods). En dashes OK in date ranges. The
  `— Josh Berrington` `<title>` delimiter is intentionally kept site-wide.
- Concrete, active **"I did X"** voice. Avoid AI-slop openers, humble-brags, and vague or
  over-claimed metrics (prefer benchmark-relative figures over raw numbers without context).
- **Editorial treatment** for image-rich pages — SheaMoisture is the reference: hero + inline
  `figure.story-fig` with mono captions, pull quotes / press clippings; lightbox via the
  `.zoomable` class (all story pages now use this unified lightbox).
- **impeccable hook noise to ignore:** `overused-font` (Geist/Geist Mono/Newsreader is the
  deliberate type system) and `broken-image` on the lightbox's runtime `<img>` template (false positive).
- Adding images: download → clear filename → `python3 scripts/upload_to_cloudinary.py`-style
  append to manifest → reference via Cloudinary folder URL `…/joshberrington-site/<name>`.

## Done this session
- All 5 work subpages refined (copy + editorial + em-dash scrub; zoomable heroes).
- Alexa page: added **Selected wins** section (repeatable `<article class="case">` blocks) —
  Smart Home Starter Kit + Fall 2025 announce, both image-rich. Elevated the agentic-transformation framing.
- Homepage: experience titles updated; AI-works list rewritten (concrete descriptions, removed
  right-column stats, removed messaging-pipeline from the list).
- Dictate + Agent Marketplace: dropped headline graphics, scrubbed em dashes, reframed weak lines.
- Moved site `mockup/` → repo root; added `CNAME`; pointed the domain.

## TODO / open items
1. Confirm `joshberrington.com` resolves with valid **HTTPS**; tick **Enforce HTTPS**.
2. Homepage experience **descriptions** still reference old framing (Alexa desc mentions
   "six-agent AI system / self-serve agent platform") — align with the elevated framing if desired.
3. Optional polish: favicon, OG/social meta tags, custom 404 page.

## Dropped
- `ai/messaging-pipeline.html` — Josh decided to bag this one (2026-07-08). File still exists in
  the repo but stays unlinked from the homepage; not on the roadmap for a rework.

## Case-study facts (keep accurate)
- **SheaMoisture** — "a celebration, not a turnaround"; #DefineYourBeard; 5x revenue, 4x'd
  points of distribution; coverage: NY Mag (The Strategist), Bossip, xoNecole, Drugstore News.
- **Amazon Aware** — 0-to-1, S-Team/CEO-level, COVID supply-chain; "PRFAQ" (no slash);
  3–4x vs. private-label averages; benchmark framing (no raw 34%/29%).
- **Dove** — "brand lead for Dove's new body wash formats" (no formal title). Shower Foam
  (lighter) and Shower Mousse (whipped) are **distinct** products.
- **Amazon Essentials** — Global Marketing Lead; agency AKQA Amsterdam; developed the creator
  pitch + built the creator-program strategy/scaffolding.
- **Alexa Starter Kit** — existing components bundled into a hard bundle; 4.6★; gen-AI/CGI
  creative; all organic. **Announce:** Sept 2025 (fall 2025), NYC, **Alexa+ Smart Home portion only**;
  Echo × Ring + Fire TV × Ring camera AI features.
