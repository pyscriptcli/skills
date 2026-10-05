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
| 1. GRILL-ME PROTOCOL     | 2. ANTI-SLOP EDITORIAL       | 3. BRAND & VECTOR ENGINE      |
+--------------------------+------------------------------+-------------------------------+
| • Single-question flow   | • Strips corporate jargon    | • PRIME Blue & Warm White     |
| • Establishes 3 pillars  | • Zero conversational fluff  | • Cormorant / Bebas / Mont    |
| • Resolves market stance | • No phantom kickers         | • Sharp corners (radius: 0)   |
| • Enforces slide budget  | • High signal-to-noise ratio | • Embedded Base64 logos       |
|                          |                              | • 16:9 HTML + Headless PDF    |
+--------------------------+------------------------------+-------------------------------+
```

---

## The 5-Step Workflow

### Step 1: Socratic Alignment (`grill-me` Protocol)
Before writing slides, interview the user **one question at a time** using `ask_question`. Resolve these dependencies sequentially:
1. **Audience & Mandate:** Who is in the room (C-suite, investment committee, corporate occupier)?
2. **Core Strategic Opportunity:** Is this a competitive differentiator to win exclusive mandates, a standalone software upsell, or an operational efficiency tool?
3. **The 3 Value Pillars:** Group client benefits into exactly three concrete outcomes (e.g., *Transparency, Decision Making, Risk Mitigation*).
4. **Internal Operational Outcome:** What repetitive bottleneck does this eliminate for the brokerage/internal team (e.g., *eliminating manual slide deck and spreadsheet re-exports*)?
5. **Slide Budget:** Enforce an 8- to 10-slide hard ceiling.

### Step 2: Anti-Slop Editorial Filter
Apply a ruthless zero-fluff editorial standard to every sentence:
- **Zero Throat-Clearing:** Never say "Sure!", "Here is your deck", or repeat the user's prompt.
- **Strip Buzzwords:** Disallow pseudo-intellectual filler: *"seamless", "synergistic", "cutting-edge", "game-changing", "holistic", "robust", "paradigm", "telemetry", "ecosystem"*.
- **No Phantom Kickers:** Never invent overline meta-labels or explanatory subtitles unless explicitly commanded.
- **Active Authoritative Voice:** Write like an exclusive commercial real estate advisory delivering board-level counsel.

### Step 3: PRIME Brand System Compliance
Apply the "Palette of Sovereign Intelligence" and architectural geometry:
- **The Two-Background Rule:** Every surface is strictly **PRIME Blue (`#003366`)** or **PRIME Warm White (`#FFFCFB`)**. Pure black (`#000000`) and pure white (`#FFFFFF`) are forbidden for brand surfaces.
- **Apex Accent:** **PRIME Gold (`#C9A84C`)** is reserved strictly for thin rules, signature moments, and numeral highlights. *Never use Gold as a large background fill.*
- **Typography:**
  - **Display Hero:** *Cormorant Garamond*, Light 300, Italic (Headlines only, 72–96px+).
  - **Impact / Data:** *Bebas Neue*, Regular (Big numbers, stats, metrics).
  - **Labels / UI Caps:** *Montserrat*, Medium 500, ALL CAPS (+0.25em tracking).
  - **Body Copy:** *Montserrat*, Regular.
- **Sharp Geometry:** `border-radius: 0 !important;` on every card, button, table, input, and container.
- **Zero-Failure Base64 Logos:** Always embed official PRIME logos (`white_prime_logo.png` on Blue surfaces, `blue_prime_logo.png` on Warm White surfaces) as inline Base64 data URIs so slides never suffer from broken images in iframes, standalone browsers, or PDF exports.

### Step 4: Vector UI / Persona Mockups (Proof Over Claims)
When illustrating product value, do not rely on bullet points alone. Code crisp vector UI mockups representing the core stakeholder roles:
1. **Project Lead View:** Portfolio command, stage tracking, team allocation, and the **Client Publishing Gate**.
2. **Project Team View:** Interactive property mapping, shortlist curation specs, and inspection checklists.
3. **External Client Portal:** Branded occupier view showing approved properties, stage progress, and audit-ready scoring.
- **Standard Disclaimer:** Always place a subtle italic disclaimer beneath prototype mockups:  
  `* For visualization purposes only`

### Step 5: Twin-Engine Publishing (HTML + 1-to-1 PDF Clone)
Generate both deliverables to guarantee immediate interactive viewing and board-ready print exports:
1. **Interactive HTML:**
   - 16:9 fixed ratio container (`1200x675` viewport preview).
   - Keyboard listener (`ArrowRight`, `ArrowLeft`, `Space`) and button controls.
   - Live slide counter (`SLIDE X / Y`).
2. **1-to-1 PDF Compilation:**
   - Run Microsoft Edge or Chrome in headless mode with `--print-to-pdf` and `--no-pdf-header-footer`.
   - Apply print CSS:
     ```css
     @page { size: 16in 9in; margin: 0; }
     * { -webkit-print-color-adjust: exact !important; print-color-adjust: exact !important; }
     @media print {
       .controls { display: none !important; }
       .deck-container { width: 16in !important; height: auto !important; border: none !important; box-shadow: none !important; }
       .slide { display: flex !important; width: 16in !important; height: 9in !important; page-break-after: always !important; break-after: page !important; }
     }
     ```
3. **Markdown Deck Sync:** Maintain an identical `.md` file in the artifact directory.

---

## Standard Slide Architecture (6 to 9 Slides)

| Slide | Surface | Role / Content |
|---|---|---|
| **01. Title** | PRIME Blue (`#003366`) | White PRIME logo (top-left), large italic Cormorant title, gold subtitle, brief executive summary. |
| **02. The Opportunity** | Warm White (`#FFFCFB`) | Market shift, traditional brokerage bottleneck, and the PRIME advantage. |
| **03. Value Pillars** | Warm White (`#FFFCFB`) | 3-column table comparing client pain points against platform solutions (*Transparency, Decision Making, Risk Mitigation*). |
| **04. Market Positioning**| Warm White (`#FFFCFB`) | Fiduciary transparency vs. traditional "black box"; modern occupier experience. |
| **05. Operating Leverage**| Warm White (`#FFFCFB`) | Eliminating manual reporting; broker time reallocated to negotiation and advisory. |
| **06. Lead Prototype** | Warm White (`#FFFCFB`) | Vector UI mockup of Lead Broker Command & Publishing Gate (`* For visualization purposes only`). |
| **07. Team Prototype** | Warm White (`#FFFCFB`) | Vector UI mockup of Property Map & Shortlist Curation (`* For visualization purposes only`). |
| **08. Client Prototype** | Warm White (`#FFFCFB`) | Vector UI mockup of Branded Client Workspace Portal (`* For visualization purposes only`). |
| **09. Commercialization**| Warm White (`#FFFCFB`) | Mandate win rates, advisory premium retainers, and TRS service menu packaging tiers. |

---

## Quality Checklist Before Output

- [ ] Was the concept grilled one question at a time before generating the deck?
- [ ] Are corporate buzzwords (*seamless, synergistic, robust, holistic*) stripped?
- [ ] Are slide backgrounds restricted strictly to PRIME Blue and Warm White?
- [ ] Is `border-radius: 0 !important;` enforced on every element?
- [ ] Are brand logos embedded as Base64 data URIs?
- [ ] Do prototype mockups include the italicized `* For visualization purposes only` caption?
- [ ] Does the generated PDF have the exact matching page count, 16:9 aspect ratio, and full-bleed backgrounds?
- [ ] Does the companion Markdown file match the slide structure?
