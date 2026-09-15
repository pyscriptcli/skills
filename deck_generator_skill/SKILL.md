---
name: prime-proposal-deck
description: >-
  Create branded, templated commercial and warehouse property proposal decks for PRIME Philippines
  from unstructured screenshots, photos, existing slides, or scattered notes. Generates fully editable,
  pixel-clean PowerPoint (.pptx) presentations using standard PRIME branding.
---

# PRIME Philippines - Proposal Deck Generator Skill

This skill enables any AI assistant (Antigravity, Claude Code, Cursor, Windsurf, or custom agents) to transform messy, scattered property data—such as broker text messages, listing screenshots, spec sheets, or old slide decks—into pristine, editable Microsoft PowerPoint (`.pptx`) presentations matching the official PRIME Philippines corporate template.

---

## Slide Architecture

The standard proposal follows PRIME Philippines' executive 3-phase flow:
1. **Title & Transmittal Phase**:
   - **Slide 1: Cover Page** — Proposal title (e.g. *Available Properties*), Target Region (e.g. *South Luzon* / *Cavite & Laguna*), and PRIME branding.
   - **Slide 2: Transmittal** — Prepared By (PRIME Leasing Advisor details), Prepared For (Client name, title, company), and Proposal header.
2. **Properties to Offer Phase** (Repeated for each property, up to 6 properties):
   - **Slide A: Property Overview & Commercials** — Property name, location, Available Units table (Covered, Open Yard, Total Area), Lease Terms & Conditions table (Rental rates, CUSA, escalation, advance, deposit), and main exterior/facade photo.
   - **Slide B: Property Details & Accessibility** — Technical specifications table (Loading docks, Apex height, shoulder height, vehicle capacity, power load, fire safety), Accessibility table (distance to highways, exits, ports), and interior/bay photos.
   - *(Optional)* **Slide C: Site Layout / Photos** — Large site development plan or photo collage.
3. **CTA / Closing Phase**:
   - **Slide 18: Contact & Next Steps** — Direct contact information for the Leasing Advisor and Senior Head, viewing schedule invitation.
   - **Slide 19: Back Cover** — PRIME Philippines closing branding.

---

## Agent Procedure: How to Run This Skill

When a user asks for a proposal deck or provides screenshots/notes:

### Step 1: Ingest & Structure the Scattered Data
Read the user's provided input (screenshots, image attachments, paste notes, or text files). Extract the unstructured details into a JSON object conforming to the schema below.

```json
{
  "proposal_title": "Available Warehouse Properties",
  "subtitle": "Cavite & Laguna Logistics Corridor",
  "proposal_header": "WAREHOUSE FACILITIES PROPOSAL FOR",
  "client_name": "Client Representative Name",
  "client_title": "Title (e.g., Supply Chain Director)",
  "client_company": "Client Company Name Inc.",
  "prepared_by": {
    "name": "Cedtrix Rena",
    "title": "Sr. Leasing Advisor",
    "division": "Retail and Industrial Markets",
    "company": "PRIME Philippines",
    "phone": "+63 917 625 3353",
    "email_primary": "cedtrix.rena@primephilippines.com"
  },
  "contact_supervisor": {
    "name": "Sondi Tuazon",
    "title": "Sr. Head",
    "phone": "+63 917 843 6128",
    "email": "sondituazon.primecorp@gmail.com"
  },
  "include_site_development_plan": false,
  "include_site_layout": false,
  "properties": [
    {
      "name": "Property Name (e.g., Apex Logistics Park)",
      "location": "City, Province (e.g., Carmona, Cavite)",
      "facade_image": "path/to/facade_or_screenshot.jpg",
      "interior_image": "path/to/interior_photo.jpg",
      "available_units": [
        ["Covered Area", "10,500 sqm"],
        ["Open Yard / Parking", "2,200 sqm"],
        ["TOTAL LEASABLE AREA", "12,700 sqm"]
      ],
      "lease_terms": [
        ["Rental Rate (Covered)", "Php 380.00/sqm + VAT"],
        ["Rental Rate (Open)", "Php 120.00/sqm"],
        ["CUSA", "Php 35.00/sqm"],
        ["Rental Escalation", "5% Annually"],
        ["Min. Lease Term", "5 Years"],
        ["Advance Rent", "3 Months"],
        ["Security Deposit", "3 Months"]
      ],
      "specifications": [
        ["Loading Area", "12 Elevated Docks with Dock Levelers"],
        ["APEX Height", "14.5 meters"],
        ["Shoulder Height", "12.0 meters"],
        ["Vehicle Capacity", "Up to 40-ft container trucks"],
        ["Electrical Load", "Three-Phase 400 KVA"],
        ["Fire Protection", "FDAS & ESFR Sprinklers"],
        ["Ideal Use", "FMCG / Logistics / Storage"]
      ],
      "accessibility": [
        ["National Highway", "400 meters"],
        ["Expressway Exit", "1.8 km"],
        ["Port / Hub", "38 km"]
      ]
    }
  ]
}
```

> **Note on Images & Screenshots**: If the user dropped image files or screenshots into the workspace/chat, reference their local paths in `facade_image` or `interior_image`. The generator will cleanly swap them into the slide's picture placeholders while maintaining exact layout geometry.

### Step 2: Save the Structured JSON
Write the JSON structure to a file (e.g., `proposal_data.json` or `examples/my_proposal.json`).

### Step 3: Run the Generator
Execute the Python script:
```bash
python scripts/generate_proposal.py --data proposal_data.json --output "Proposal_ClientName.pptx"
```

The script will:
- Load the master template `templates/prime_proposal_template.pptx`.
- Populate Title, Subtitle, Client Transmittal, and Advisor contacts.
- Populate each property's Overview and Details slides with exact formatted tables.
- Replace placeholder pictures with user screenshots/photos if provided.
- Automatically prune any unused property slides so the deck ends cleanly at the CTA slide.
- Save the final editable `.pptx`.

### Step 4: Present Result to User
Provide the user with a clickable link to the generated `.pptx` file (e.g. `[Proposal_ClientName.pptx](file:///absolute/path/to/Proposal_ClientName.pptx)`).

---

## Utility Scripts

- **`scripts/generate_proposal.py`**: The primary PPTX generator. Accepts `--data` (JSON path), `--template` (optional custom PPTX), and `--output` (target PPTX).
- **`scripts/parse_inputs.py`**: CLI extractor for unstructured text notes or extracting slides/images from an existing `.pptx`.
  - Usage on text notes: `python scripts/parse_inputs.py --input notes.txt --output proposal.json`
  - Usage on existing PPTX: `python scripts/parse_inputs.py --input old_deck.pptx --output extracted.json`
- **`scripts/inspect_template.py`**: Inspects all shapes, tables, and images of any PowerPoint template.

---

## Brand System Reference (`branding.json`)

- **Primary Colors**:
  - PRIME Navy: `#021A3D` / `#003464`
  - PRIME Gold: `#EEBA2B` / `#C9A84C`
  - Slate: `#272828`
  - White: `#FFFFFF`
- **Typography**: `Montserrat`, `Century Gothic`, `Cormorant Garamond`, `DM Sans`
