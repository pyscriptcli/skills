---
name: prime-pitch-agy
description: >-
  All-in-one executive pitch deck creator for Antigravity (AGY). Unifies Socratic
  interviewing (grill-me), strict anti-slop editorial discipline, and the PRIME Philippines
  brand system to produce boardroom-ready presentations in interactive 16:9 HTML,
  1-to-1 clone PDF, and synchronized Markdown.
---

# PRIME Pitch AGY — Executive Deck Studio

`prime-pitch-agy` is an all-in-one skill that unifies **Socratic concept grilling**, **anti-slop editorial discipline**, and the **PRIME Philippines brand system** into an automated publishing engine.

It replaces the need to manually juggle `/grill-me`, `/anti-slop`, and `/prime-philippines-brand`, providing an end-to-end pipeline that takes raw project notes and turns them into a boardroom-ready executive pitch deck delivered simultaneously as:
1. **Interactive 16:9 HTML Presentation** (keyboard navigation, slide counter, responsive viewport).
2. **1-to-1 Vector-Sharp PDF Clone** (headless browser print with `@page { size: 16in 9in; margin: 0; }`).
3. **Synchronized Markdown Deck** (for plain-text review and documentation).

---

## The 4 Unified Pillars

```
+-----------------------------------------------------------------------------------------+
|                                  PRIME-PITCH-AGY                                        |
+--------------------------+------------------------------+-------------------------------+
| 1. GRILL-ME PROTOCOL     | 2. ACTIVE ANTI-SLOP          | 3. BRAND & VECTOR ENGINE      |
+--------------------------+------------------------------+-------------------------------+
| • Single-question flow   | • Active during execution    | • PRIME Blue & Warm White     |
| • Establishes 3 pillars  | • Strict 50-75 word budget   | • Cormorant / Bebas / Mont    |
| • Resolves market stance | • ZERO AI-generated faces    | • Sharp corners (radius: 0)   |
| • RE-GRILL on missing    | • Telegraphic bullet density | • Embedded Base64 logos       |
|   data (Never assume)    | • Strips corporate jargon    | • 16:9 HTML + Headless PDF    |
+--------------------------+------------------------------+-------------------------------+

```

---

## The 5-Step Workflow

### Step 1: Socratic Alignment (`grill-me` Protocol)
Before writing slides, interrogate the concept and user assumptions **one question at a time** using `ask_question`. Never generate a deck without completing this alignment.

#### Tone: Direct, High Level, No Bluff
- **Talk Straight:** Focus on practical reality—real numbers, time, money, and responsibilities. No bluffing, no corporate drama, no buzzwords.
- **Zero Cheerleading:** Never use conversational filler like *"Great idea!"* or *"I'd be glad to help!"*. Cut straight to the operational question.
- **High-Level Commercial Reality:** Focus on practical deal mechanics—who does the work, who takes the risk, who gets paid, and how many hours it actually takes.

#### Jargon to Use vs. Jargon to Avoid
| Category | Real Industry Terms (Use These) | Buzzwords & Fluff (Avoid) |
|---|---|---|
| **Commercial Real Estate** | TPV (Total Project Value), PCAB License (AAAA/AAA/AA), MEPFS, Bare Shell vs Warm Shell vs Fitted/Turnkey, Handover Condition, Dilapidations/Reinstatement, Tenant Rep, Landlord Rep, GFA, NLA, Net Effective Rent, Escalation Rate | *Ecosystem, Synergistic, Seamless, Holistic, Paradigm, Cutting-Edge, Game-Changing, Future-Proof, Forensic* |
| **Brokerage Economics** | Commission Split, Break-Even Yield, Advisor Hourly Rate, Hours Reclaimed, Deal Velocity, Carrying Cost, Pipeline Conversion, Milestone Escrow | *Empower, Supercharge, Unlock Potential, Transformative Journey, Next-Gen, Revolutionize* |
| **Procurement & Contracts** | Master Service Agreement (MSA), Vetting Due Diligence, SLA, Scope Handoff, Default Liability, Credit Risk, Escrow Milestone Gate, Tax Clearance | *Magic bullet, Thought leadership, North star, Deep dive, Telemetry* |

#### The 6 Alignment Questions:
1. **Audience:** Who is in the room and what is their practical hesitation?
2. **Deal Economics:** What is the fee split, TPV basis, payment schedule, and who carries default risk?
3. **Time & Capacity:** How many hours does the team lose doing this manually, and what does that cost in lost deals?
4. **3 Core Outcomes:** Exactly three practical results (e.g., specialized contractor access, advisor hours saved, higher net commission).
5. **The Hard Objection:** What is the main argument against this (e.g., *"Why pay 20% if I can do it myself?"*), and what is the direct, no-bluff answer?
6. **Slide Budget:** Enforce an 8- to 10-slide limit. Pacing: Blue title/conclusion anchors with Warm White analytical core.

#### The "Never Assume — Re-Grill" Protocol (Continuous Grill-Me)
**Assumption is fatal in institutional advisory.** When executing requests, the agent must never invent or guess missing inputs:
- **Zero Asset Fabrication:** If the user asks to add photos, financial figures, lease contracts, or corporate data points, and they **cannot be verified or found in official records**, **NEVER GENERATE OR FABRICATE THEM**. (Generating synthetic AI portraits or hallucinated metrics is a **BIG NO** and strictly unacceptable).
- **Mandatory Re-Grill Trigger:** The moment an asset or data point is missing:
  1. **Pause immediately.** Do not commit assumed or synthetic content to the deck.
  2. **Trigger `ask_question` (re-grill the user):** State the exact factual gap transparently (e.g., *"We found verified media photos for Person A, but Persons B, C, and D have no public media photos on record"*).
  3. **Present concrete options:** Ask the user how to handle the gap (e.g., provide private photo files, use clean architectural monogram badges, or omit images).
  4. **Only proceed once the user decides.** Never assume the user wants AI-generated filler.

---


### Step 2: Anti-Slop & Strict Word Economy (Active During Execution)
Executive slides are **decision surfaces, not reading memos**. Anti-slop is continuously active during creation, not an afterthought:

#### 0. Active Anti-Slop During Execution
- **Strip Conversational Bloat:** Never cheerlead, apologize, or restate prompts.
- **No Decorative Junk:** Never add faux-status badges, redundant divider cards, or empty containers just to fill layout space.
- **No Unsolicited Subtitles:** Never invent overlines or kickers unless explicitly mandated.
- **Truth Over Fill:** If data does not exist, leave clean negative space or report it. Never manufacture placeholder claims.

#### 1. Hard Word Limits Per Slide
- **Total Slide Copy:** Strict cap of **50 to 75 words per slide maximum** (excluding numeric table cells and UI mockups). If a slide looks like a reading document, it fails.
- **Headlines:** 4 to 7 words maximum. Declarative and commercial (e.g. *Consumption-Based Economics vs. Per-Seat Waste*).
- **Subtitles:** 1 single sentence, max 14 words, or omit entirely.
- **Card / Pillar Headers:** 2 to 4 words.
- **Bullet Points:** Maximum 1 to 2 lines per bullet, capped at **10 to 14 words per bullet**.
- **Zero Narrative Paragraphs:** Never dump 3+ line explanatory paragraphs onto slides or cards. If text requires a paragraph, convert it into a metric stat callout or a comparison row.


#### 2. Telegraphic Density (Subject → Metric → Result)
Strip conversational padding, auxiliary verbs, and passive explanations.
- *Too Wordy (Slop):* "An automated multi-key failover system ensures that if the free API hits rate limits during heavy usage, our pipeline will instantly and automatically route jobs to paid compute."
- *Punchy (PRIME):* "Groq Free (₱0/hr) primary; instant HTTP 429 failover to Groq Turbo (₱2.34/hr)."

#### 3. Visual Data Over Text
Every slide must prioritize visual structure over text blocks:
- **Bebas Neue Impact Stats:** Giant numbers (`46–64px`) with tight 2-line uppercase labels.
- **Side-by-Side Comparison Tables:** Crisp feature/cost columns instead of descriptive bullet points.
- **Vector UI Mockups:** Show real screen fragments, micro-labels, and data cards rather than explaining features in prose.

#### 4. Ultra-Concise Chat Responses
- When presenting deliverables to the user, keep accompanying chat messages under **150 words total**.
- Provide direct markdown file links to HTML, PDF, and MD deliverables.
- Do NOT re-narrate or summarize every slide in chat. Highlight only the core metric and 1–2 open decisions for user sign-off.

---

### Step 3: PRIME Brand System Compliance
Apply the "Palette of Sovereign Intelligence" and architectural geometry:
- **The Two-Background Rule:** Every surface is strictly **PRIME Blue (`#003366`)** or **PRIME Warm White (`#FFFCFB`)**. Pure black (`#000000`) and pure white (`#FFFFFF`) are forbidden for brand surfaces.
- **Apex Accent:** **PRIME Gold (`#C9A84C`)** is reserved strictly for thin rules, signature moments, and numeral highlights. *Never use Gold as a large background fill.*
- **Typography:**
  - **Display Hero:** *Cormorant Garamond*, Light 300, Italic (Headlines only, 44–72px+).
  - **Impact / Data:** *Bebas Neue*, Regular (Big numbers, stats, metrics, 46–64px).
  - **Labels / UI Caps:** *Montserrat*, Medium 500, ALL CAPS (+0.25em tracking, 9–11px).
  - **Body Copy:** *Montserrat*, Regular (11–13px, max 1.45 line-height).
- **Sharp Geometry:** `border-radius: 0 !important;` on every card, button, table, input, and container.
- **Zero-Failure Base64 Logos:** Always embed official PRIME logos (`white_prime_logo.png` on Blue surfaces, `blue_prime_logo.png` on Warm White surfaces) as inline Base64 data URIs so slides never suffer from broken images in iframes, standalone browsers, or PDF exports.
- **STRICT BAN: Zero AI-Generated Portraits (Big NO):** Never use AI image generation (`generate_image`, DALL-E, Midjourney, etc.) to fabricate portraits, executive headshots, or fake human faces. This is **strictly unacceptable**. Institutional advisory requires authentic due diligence:
  - Use **only** verified, authentic public media photographs from official press/governance archives when available.
  - If no verified authentic photo exists, use clean architectural initials/monogram badges (`KNC`, `AOU`, `DMC`) or corporate logo icons. **Never synthesize a human likeness.**


---

### Step 4: Vector UI / Persona Mockups (Proof Over Claims)
When illustrating product value, do not rely on bullet points alone. Code crisp vector UI mockups representing the core stakeholder roles:
1. **Studio / Lead View:** Recording status, live waveform, speaker turn attribution, and immediate action buttons.
2. **Publishing Gate View:** Target Space & List selectors, confidentiality toggles (`🔒 Personal List`), and SSOT synchronization status.
3. **Ask Echo Retrieval View:** Bounded user query with verified inline citations `[1]` linked to ground-truth task records.
- **Standard Disclaimer:** Always place a subtle italic disclaimer beneath prototype mockups:  
  `* For visualization purposes only`

---

### Step 5: Twin-Engine Publishing (HTML + 1-to-1 PDF Clone)
Generate both deliverables to guarantee immediate interactive viewing and board-ready print exports:
1. **Interactive HTML:**
   - 16:9 fixed ratio container (`1200x675` viewport preview).
   - Keyboard listener (`ArrowRight`, `ArrowLeft`, `Space`) and button controls.
   - Live slide counter (`SLIDE X / Y`).
2. **1-to-1 PDF Compilation:**
   - Run Microsoft Edge or Chrome in headless mode with `--print-to-pdf` and `--no-pdf-header-footer`.
   - Apply print CSS that guarantees multi-page breakout:
     ```css
     @page { size: 16in 9in; margin: 0; }
     * { -webkit-print-color-adjust: exact !important; print-color-adjust: exact !important; }
     @media print {
       html, body {
         background: transparent !important;
         margin: 0 !important;
         padding: 0 !important;
         width: 16in !important;
         height: auto !important;
         overflow: visible !important;
       }
       .controls, .nav-controls, .keyboard-hint { display: none !important; }
       .deck-viewport { padding: 0 !important; margin: 0 !important; height: auto !important; display: block !important; }
       .deck-container {
         width: 16in !important;
         height: auto !important;
         border: none !important;
         box-shadow: none !important;
         overflow: visible !important;
         display: block !important;
         position: static !important;
       }
       .slide {
         display: flex !important;
         position: relative !important;
         top: auto !important;
         left: auto !important;
         width: 16in !important;
         height: 9in !important;
         min-height: 9in !important;
         max-height: 9in !important;
         opacity: 1 !important;
         visibility: visible !important;
         page-break-after: always !important;
         break-after: page !important;
         page-break-inside: avoid !important;
         break-inside: avoid !important;
         padding: 0.75in 0.9in 0.65in 0.9in !important;
       }
       .slide:last-child {
         page-break-after: avoid !important;
         break-after: avoid !important;
       }
     }
     ```
3. **Markdown Deck Sync:** Maintain an identical `.md` file in the artifact directory.

---

## Standard Slide Architecture (6 to 9 Slides)

| Slide | Surface | Role / Content |
|---|---|---|
| **01. Title** | PRIME Blue (`#003366`) | White PRIME logo, Cormorant italic title, gold subtitle, 3 crisp core pillars. |
| **02. The Friction** | Warm White (`#FFFCFB`) | 3 big stat cards (Bebas Neue) showing carrying cost, idle bleed, and manual time loss. |
| **03. Economic Shift** | Warm White (`#FFFCFB`) | 2-column comparison card: Per-seat recurring SaaS vs. Pay-as-you-go compute. |
| **04. Feature Pillar 1**| Warm White (`#FFFCFB`) | Studio AI Notetaker: 3 cards covering dual capture, domain taxonomy, and action extraction. |
| **05. Feature Pillar 2**| Warm White (`#FFFCFB`) | ClickUp SSOT: 3 cards covering OAuth governance, space/list mapping, and confidential relocation. |
| **06. Feature Pillar 3**| Warm White (`#FFFCFB`) | Storage & Failover: Dedicated SharePoint ($0) + 3-tier transcription failover table. |
| **07. TCO Proof** | Warm White (`#FFFCFB`) | 4-column structured matrix comparing Fireflies vs. Otter vs. Project Echo (98.9% cost reduction). |
| **08. Persona Mockups**| Warm White (`#FFFCFB`) | 3 vector UI windows showing Studio Recorder, ClickUp Publishing Gate, and Ask Echo Drawer. |
| **09. Roadmap** | PRIME Blue (`#003366`) | 3-phase rollout roadmap closing with *"We Advise. You Advance."* |

---

## Quality Checklist Before Output

- [ ] Was the concept grilled one question at a time before generating the deck?
- [ ] If any requested assets or data points were missing, did I pause and re-grill the user via ask_question instead of assuming or synthesizing them?
- [ ] Was Anti-Slop actively enforced during creation (zero fluff, zero decorative clutter, zero corporate buzzwords)?
- [ ] Is total slide copy strictly under 75 words per slide (excluding table numbers)?
- [ ] Are bullet points telegraphic (under 14 words each) with zero narrative paragraphs?
- [ ] Are corporate buzzwords (*seamless, synergistic, robust, holistic*) stripped?
- [ ] Are slide backgrounds restricted strictly to PRIME Blue and Warm White?
- [ ] Is `border-radius: 0 !important;` enforced on every element?
- [ ] Are brand logos embedded as Base64 data URIs?
- [ ] Are AI-generated portraits strictly avoided? (Big NO: Never synthesize faces; use verified real press photos or initials/monogram badges only).
- [ ] Do prototype mockups include the italicized `* For visualization purposes only` caption?
- [ ] Does the generated PDF have the exact matching page count, 16:9 aspect ratio, and full-bleed backgrounds?
- [ ] Does the companion Markdown file match the slide structure?
- [ ] Is the agent's chat response concise (under 150 words) with clickable file links?


