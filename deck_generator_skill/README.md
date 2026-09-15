# PRIME Philippines Proposal Deck Generator (AI Skill)

> **Eliminate the friction of scattered, unstructured real estate data.** Transform listing notes, WhatsApp messages, broker flyers, and property screenshots into executive, 100% editable Microsoft PowerPoint (`.pptx`) proposals formatted with official **PRIME Philippines** branding.

Designed as a **Universal AI Assistant Skill** (`SKILL.md` at root). Usable directly inside **Google Antigravity**, **Claude Code**, **Cursor**, **Windsurf**, or as a standalone Python CLI.

---

## 🎯 The Problem This Solves

Commercial real estate advisors and brokers spend hours re-typing specs, copying rental tables, and manually pasting screenshots from messy client chats or scattered PDFs into PowerPoint. 

With this skill:
1. Drop your raw notes, screenshots, or old slides into chat.
2. The AI structures the data (Available Units, Commercial Lease Terms, Specifications, Accessibility).
3. The generator produces a clean, executive, 16:9 `.pptx` presentation in seconds.

---

## 📁 Repository Structure

```text
prime-deck-skill/
├── SKILL.md                 # Universal Skill definition (Antigravity, Claude, Cursor)
├── README.md                # Documentation & quickstart guide
├── requirements.txt         # Minimal dependencies (python-pptx, pillow)
├── branding.json            # Official PRIME Philippines color palette, fonts & advisor info
├── templates/
│   └── prime_proposal_template.pptx   # Master 16:9 template with vector branding & tables
├── scripts/
│   ├── generate_proposal.py # Core PowerPoint generator
│   ├── parse_inputs.py      # Extract text & tables from notes or existing PPTX
│   └── inspect_template.py  # Diagnostic inspection tool for slide shapes
└── examples/
    ├── sample_notes.txt     # Realistic unstructured broker notes
    ├── sample_proposal.json # Formatted schema ready for generator
    └── generated_sample_deck.pptx # Demo output deck
```

---

## 🚀 Quickstart & Installation

### 1. Clone Locally

```bash
git clone https://github.com/<YOUR_USERNAME>/prime-deck-skill.git
cd prime-deck-skill
pip install -r requirements.txt
```

### 2. Using with AI Assistants

#### In Google Antigravity
Clone directly into your project's agent skills folder:
```bash
git clone https://github.com/<YOUR_USERNAME>/prime-deck-skill.git .agents/skills/prime-deck-skill
```
Or for global availability across all projects:
```bash
git clone https://github.com/<YOUR_USERNAME>/prime-deck-skill.git ~/.gemini/config/skills/prime-deck-skill
```
*Antigravity will automatically detect `SKILL.md` and activate it whenever you ask to create a proposal deck or share property screenshots!*

#### In Claude Code / Cursor / Windsurf
Add or symlink this folder into your project's skill or rules directory. The root `SKILL.md` contains step-by-step instructions that any multimodal LLM will immediately understand and follow.

---

## 💻 Standalone CLI Usage

You can also run the generator directly without an AI assistant:

### Generate from structured JSON:
```bash
python scripts/generate_proposal.py --data examples/sample_proposal.json --output "My_Proposal.pptx"
```

### Parse raw text notes into JSON:
```bash
python scripts/parse_inputs.py --input examples/sample_notes.txt --output "parsed.json"
python scripts/generate_proposal.py --data "parsed.json" --output "Proposal_From_Notes.pptx"
```

### Extract content from an existing PPTX:
```bash
python scripts/parse_inputs.py --input "old_deck.pptx" --output "extracted.json"
```

---

## 📊 Presentation Flow & Layouts

Every generated proposal follows the official PRIME Philippines structure:

| Slide # | Slide Type | Description |
| :--- | :--- | :--- |
| **Slide 1** | **Cover Page** | Title (*Available Properties*), Region (*South Luzon* / *Cavite*), PRIME vector branding |
| **Slide 2** | **Transmittal** | Prepared By (Advisor details), Prepared For (Client name, company, title) |
| **Slide 3** | **Property Overview** | Property Name & City, Available Units Table, Lease Terms Table, Exterior Photo |
| **Slide 4** | **Property Details** | Technical Specifications Table, Accessibility Table, Interior/Bay Photo |
| *Repeat* | *Properties 2 to 6* | Cleanly adds additional property pairs; prunes unused slides automatically |
| **Slide 18** | **CTA / Contact** | Contact cards for Leasing Advisor and Senior Head, viewing invitation |
| **Slide 19** | **Back Cover** | PRIME Philippines logo & official closing |

---

## 🎨 Branding & Customization (`branding.json`)

To update default advisors, phone numbers, or corporate details, simply edit `branding.json`:

```json
{
  "company_name": "PRIME Philippines",
  "colors": {
    "navy_primary": "#021A3D",
    "gold_accent": "#EEBA2B",
    "dark_slate": "#272828",
    "pure_white": "#FFFFFF"
  },
  "default_prepared_by": {
    "name": "Your Name",
    "title": "Sr. Leasing Advisor",
    "phone": "+63 917 XXX XXXX",
    "email_primary": "yourname@primephilippines.com"
  }
}
```

---

## 📄 License
MIT License. Created for PRIME Philippines property proposal generation.
