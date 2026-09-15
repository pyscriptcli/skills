#!/usr/bin/env python3
"""
PRIME Philippines - Input Parser & Content Extractor
Parses unstructured notes or extracts content from existing PPTX decks
to produce a clean, structured proposal JSON ready for generate_proposal.py.
"""

import os
import sys
import json
import re
import argparse
from pathlib import Path

def extract_from_pptx(pptx_path, output_dir=None):
    """
    Extracts text, tables, and embedded images from an existing PowerPoint presentation.
    """
    import pptx
    from pptx.enum.shapes import MSO_SHAPE_TYPE

    prs = pptx.Presentation(pptx_path)
    extracted = {
        "source_file": str(pptx_path),
        "total_slides": len(prs.slides),
        "slides": []
    }

    if output_dir:
        img_dir = Path(output_dir) / "extracted_images"
        img_dir.mkdir(parents=True, exist_ok=True)
    else:
        img_dir = None

    for idx, slide in enumerate(prs.slides):
        slide_info = {
            "slide_number": idx + 1,
            "text": [],
            "tables": [],
            "images": []
        }

        for s_idx, shape in enumerate(slide.shapes):
            if shape.has_text_frame:
                txt = shape.text_frame.text.strip()
                if txt:
                    slide_info["text"].append(txt)

            if shape.has_table:
                tbl_data = []
                for row in shape.table.rows:
                    row_vals = [cell.text.strip() for cell in row.cells]
                    tbl_data.append(row_vals)
                slide_info["tables"].append(tbl_data)

            if shape.shape_type == MSO_SHAPE_TYPE.PICTURE and img_dir:
                try:
                    img_filename = f"slide_{idx+1}_img_{s_idx+1}.jpg"
                    img_path = img_dir / img_filename
                    with open(img_path, "wb") as f:
                        f.write(shape.image.blob)
                    slide_info["images"].append(str(img_path))
                except Exception:
                    pass

        extracted["slides"].append(slide_info)

    return extracted

def parse_unstructured_notes(text):
    """
    Heuristically extracts property details from unstructured text / notes.
    """
    proposal = {
        "proposal_title": "Available Warehouse Properties",
        "subtitle": "Strategic Logistics Locations",
        "proposal_header": "WAREHOUSE FACILITIES PROPOSAL FOR",
        "client_name": "Valued Client",
        "client_title": "Logistics & Supply Chain Management",
        "client_company": "Client Company Inc.",
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
        "include_site_development_plan": False,
        "include_site_layout": False,
        "properties": []
    }

    # Detect client name / company
    client_match = re.search(r"(?:for|client|prepared for)[:\s]+([^\n,]+)(?:,\s*([^\n]+))?", text, re.IGNORECASE)
    if client_match:
        if client_match.group(2):
            proposal["client_name"] = client_match.group(1).strip()
            proposal["client_company"] = client_match.group(2).strip()
        else:
            proposal["client_company"] = client_match.group(1).strip()

    # Split text into property blocks by keywords or numbered items
    blocks = re.split(r"(?:^|\n)(?=(?:Property\s*\d+|Warehouse\s*\d+|\bOption\s*\d+|\bSite\s*\d+))", text, flags=re.IGNORECASE)
    if len(blocks) <= 1:
        blocks = [text]

    for block in blocks:
        if not block.strip():
            continue
        
        # Name
        name_match = re.search(r"(?:name|property|warehouse|option|site)[:\s]*([^\n]+)", block, re.IGNORECASE)
        prop_name = name_match.group(1).strip() if name_match else "Prime Warehouse Facility"

        # Location
        loc_match = re.search(r"(?:location|city|address|area)[:\s]*([^\n]+)", block, re.IGNORECASE)
        prop_loc = loc_match.group(1).strip() if loc_match else "Laguna, Philippines"

        # Available Area
        area_match = re.search(r"(?:covered area|area|size|total area)[:\s]*([^\n]+)", block, re.IGNORECASE)
        cov_area = area_match.group(1).strip() if area_match else "5,000 sqm"

        # Rental Rate
        rate_match = re.search(r"(?:rental rate|rate|rent|price)[:\s]*([^\n]+)", block, re.IGNORECASE)
        rent_rate = rate_match.group(1).strip() if rate_match else "Php 350.00/sqm + VAT"

        prop_obj = {
            "name": prop_name,
            "location": prop_loc,
            "available_units": [
                ["Covered Area", cov_area],
                ["Open Yard", "1,000 sqm"],
                ["TOTAL LEASABLE AREA", cov_area]
            ],
            "lease_terms": [
                ["Rental Rate (Covered)", rent_rate],
                ["Rental Escalation", "5% Yearly"],
                ["Min. Lease Term", "3 Years"],
                ["Advance Rent", "3 Months"],
                ["Security Deposit", "3 Months"]
            ],
            "specifications": [
                ["Loading Area", "Elevated loading bays"],
                ["APEX Height", "12-14 meters"],
                ["Vehicle Capacity", "Up to 40 ft. trucks"],
                ["Electrical Load", "Three Phase Ready"],
                ["Ideal Use", "Storage / Logistics / Distribution"]
            ],
            "accessibility": [
                ["National Highway", "1.0 km"],
                ["Expressway Exit", "3.5 km"],
                ["Manila Port", "45 km"]
            ]
        }
        proposal["properties"].append(prop_obj)

    return proposal

def main():
    parser = argparse.ArgumentParser(description="PRIME Input Parser")
    parser.add_argument("--input", "-i", required=True, help="Path to input text file or existing .pptx")
    parser.add_argument("--output", "-o", default="parsed_proposal.json", help="Path to output JSON")
    args = parser.parse_args()

    in_path = Path(args.input)
    if in_path.suffix.lower() in [".pptx", ".ppt"]:
        print(f"[*] Extracting from PPTX: {in_path}")
        result = extract_from_pptx(in_path, output_dir=in_path.parent)
    else:
        print(f"[*] Parsing unstructured notes from: {in_path}")
        with open(in_path, "r", encoding="utf-8") as f:
            text = f.read()
        result = parse_unstructured_notes(text)

    with open(args.output, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2)

    print(f"[SUCCESS] Parsed output saved to {args.output}")

if __name__ == "__main__":
    main()
