#!/usr/bin/env python3
"""
PRIME Philippines - Automated Proposal Deck Generator
Generates clean, branded, editable PowerPoint (.pptx) proposal presentations
from structured JSON or dictionary data.
"""

import os
import sys
import json
import argparse
from pathlib import Path
from PIL import Image
import pptx
from pptx.util import Inches
from pptx.enum.shapes import MSO_SHAPE_TYPE

# Default paths relative to script directory
SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parent
DEFAULT_TEMPLATE = REPO_ROOT / "templates" / "prime_proposal_template.pptx"
DEFAULT_BRANDING = REPO_ROOT / "branding.json"

def load_json(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)

def set_text_preserve_format(paragraph, text):
    """Sets text on a paragraph while preserving font styling of the first run if present."""
    if not paragraph.runs:
        paragraph.text = text
        return
    
    first_run = paragraph.runs[0]
    font_name = first_run.font.name
    font_size = first_run.font.size
    bold = first_run.font.bold
    italic = first_run.font.italic
    color = first_run.font.color
    
    paragraph.text = text
    if paragraph.runs:
        r = paragraph.runs[0]
        if font_name: r.font.name = font_name
        if font_size: r.font.size = font_size
        if bold is not None: r.font.bold = bold
        if italic is not None: r.font.italic = italic
        if color and color.type == pptx.enum.dml.MSO_COLOR_TYPE.RGB:
            r.font.color.rgb = color.rgb

def update_table_cells(table, row_data, start_row=1):
    """
    Updates key-value table cells cleanly.
    row_data: list of tuples or lists [(label, value), ...]
    """
    for idx, item in enumerate(row_data):
        r_idx = start_row + idx
        if r_idx >= len(table.rows):
            break
        col_count = len(table.columns)
        if col_count >= 2:
            cell_key = table.cell(r_idx, 0)
            cell_val = table.cell(r_idx, 1)
            
            key_text = str(item[0]) if len(item) > 0 else ""
            val_text = str(item[1]) if len(item) > 1 else ""
            
            if cell_key.text_frame.paragraphs:
                set_text_preserve_format(cell_key.text_frame.paragraphs[0], key_text)
            else:
                cell_key.text = key_text
                
            if cell_val.text_frame.paragraphs:
                set_text_preserve_format(cell_val.text_frame.paragraphs[0], val_text)
            else:
                cell_val.text = val_text

def replace_picture_shape(shape, image_path):
    """Replaces the image blob in a picture shape with a new image."""
    if not os.path.exists(image_path):
        print(f"  [Warning] Image file not found: {image_path}")
        return False
        
    try:
        with open(image_path, "rb") as f:
            new_blob = f.read()
            
        shape.image._blob = new_blob
        embed_rId = shape._element.xpath('.//a:blip/@r:embed')
        if embed_rId:
            shape.part.related_part(embed_rId[0])._blob = new_blob
        return True
    except Exception as e:
        print(f"  [Warning] Failed to replace picture {shape.name}: {e}")
        return False

def delete_slide_clean(prs, slide_index):
    """Deletes a slide at given index and cleans up its part relationship."""
    slide = prs.slides[slide_index]
    slide_id = slide.slide_id
    slide_part = slide.part
    
    # Remove from slide ID list
    for sldId in prs.slides._sldIdLst:
        if sldId.id == slide_id:
            prs.slides._sldIdLst.remove(sldId)
            break
            
    # Drop relationship from presentation package
    for rId, rel in list(prs.part.rels.items()):
        if rel.target_part == slide_part:
            prs.part.drop_rel(rId)
            break

def build_proposal_deck(data, template_path=None, output_path=None):
    """
    Main engine to construct the proposal deck.
    """
    if template_path is None:
        template_path = DEFAULT_TEMPLATE
    if output_path is None:
        client_clean = data.get("client_company", "Client").replace(" ", "_")
        output_path = REPO_ROOT / f"Proposal_{client_clean}.pptx"
        
    print(f"[*] Loading template: {template_path}")
    prs = pptx.Presentation(str(template_path))
    
    # 1. Update Cover Slide (Slide 0)
    cover_slide = prs.slides[0]
    title = data.get("proposal_title", "Available Properties")
    subtitle = data.get("subtitle", "South Luzon")
    for shp in cover_slide.shapes:
        if shp.has_text_frame:
            txt = shp.text_frame.text.strip()
            if "Available Properties" in txt or shp.name == "TextBox 10":
                shp.text_frame.text = title
            elif "South Luzon" in txt or shp.name == "TextBox 12":
                shp.text_frame.text = subtitle

    # 2. Update Transmittal Slide (Slide 1)
    trans_slide = prs.slides[1]
    client_name = data.get("client_name", "Ryan Alvin")
    client_title = data.get("client_title", "Regional Area Manager")
    client_company = data.get("client_company", "SF Express Philippines Inc.")
    prepared_by = data.get("prepared_by", {})
    advisor_name = prepared_by.get("name", "Cedtrix Rena")
    advisor_title = prepared_by.get("title", "Sr. Leasing Advisor")
    advisor_company = prepared_by.get("company", "PRIME Philippines")
    proposal_for = data.get("proposal_header", "WAREHOUSE FACILITIES PROPOSAL FOR")

    for shp in trans_slide.shapes:
        if shp.has_text_frame:
            txt = shp.text_frame.text.strip()
            if "Cedtrix Rena" in txt or "Sr. Leasing Advisor" in txt:
                shp.text_frame.text = f"{advisor_name}\n{advisor_title}\n{advisor_company}"
            elif "WAREHOUSE FACILITIES PROPOSAL" in txt:
                shp.text_frame.text = proposal_for
            elif "Ryan Alvin" in txt or "SF Express" in txt:
                shp.text_frame.text = f"{client_name}\n{client_title}\n{client_company}"
            elif txt == "SF EXPRESS PHILIPPINES  INC.":
                shp.text_frame.text = client_company.upper()

    # 3. Process Properties
    properties = data.get("properties", [])
    num_props = len(properties)
    print(f"[*] Processing {num_props} property offerings...")

    prop_pairs = [
        (2, 3),   # Prop 1: Paciano
        (4, 5),   # Prop 2: Binan
        (6, 7),   # Prop 3: Timbao
        (8, 9),   # Prop 4: JDH
        (12, 13), # Prop 5: Silang
        (14, 15)  # Prop 6: Sta Rosa
    ]

    for p_idx, prop in enumerate(properties[:6]):
        if p_idx >= len(prop_pairs):
            break
        s_overview_idx, s_details_idx = prop_pairs[p_idx]
        s_overview = prs.slides[s_overview_idx]
        s_details = prs.slides[s_details_idx]
        
        prop_name = prop.get("name", f"Property {p_idx+1}")
        prop_loc = prop.get("location", "")
        
        # A) Update Overview Slide
        for shp in s_overview.shapes:
            if shp.has_text_frame:
                txt = shp.text_frame.text.strip()
                # Precise title & subtitle detection
                if shp.name == "TextBox 15" or (shp.top < Inches(0.8) and txt):
                    shp.text_frame.text = prop_name
                elif shp.name == "TextBox 16" or (Inches(0.8) <= shp.top < Inches(1.5) and txt):
                    shp.text_frame.text = prop_loc
            if shp.has_table:
                tbl = shp.table
                header_text = tbl.cell(0, 0).text.strip().upper()
                if "AVAILABLE" in header_text or "AREA" in header_text:
                    units_data = prop.get("available_units", [])
                    if units_data:
                        update_table_cells(tbl, units_data, start_row=2)
                elif "LEASE" in header_text or "TERMS" in header_text:
                    terms_data = prop.get("lease_terms", [])
                    if terms_data:
                        update_table_cells(tbl, terms_data, start_row=1)
            elif shp.shape_type == MSO_SHAPE_TYPE.PICTURE:
                facade_img = prop.get("facade_image") or prop.get("main_image")
                if facade_img:
                    replace_picture_shape(shp, facade_img)

        # B) Update Details Slide
        for shp in s_details.shapes:
            if shp.has_text_frame:
                if prop.get("custom_details_title"):
                    shp.text_frame.text = prop["custom_details_title"]
            if shp.has_table:
                tbl = shp.table
                header_text = tbl.cell(0, 0).text.strip().upper()
                if "SPECIFICATION" in header_text:
                    specs_data = prop.get("specifications", [])
                    if specs_data:
                        update_table_cells(tbl, specs_data, start_row=1)
                elif "ACCESSIBILITY" in header_text:
                    access_data = prop.get("accessibility", [])
                    if access_data:
                        update_table_cells(tbl, access_data, start_row=2)
            elif shp.shape_type == MSO_SHAPE_TYPE.PICTURE:
                interior_img = prop.get("interior_image") or prop.get("details_image")
                if interior_img:
                    replace_picture_shape(shp, interior_img)

    # 4. Update CTA / Contact Slide (Slide 17 in original)
    cta_slide = prs.slides[17]
    advisor_contact = prepared_by.get("contact_card") or (
        f"{advisor_name}\n"
        f"{advisor_title} – {prepared_by.get('division', 'Retail and Industrial Markets')}\n"
        f"{prepared_by.get('phone', '+63 917 625 3353')}\n"
        f"{prepared_by.get('email_primary', 'cedtrix.rena@primephilippines.com')}"
    )
    
    head_info = data.get("contact_supervisor", {})
    head_name = head_info.get("name", "Sondi Tuazon")
    head_title = head_info.get("title", "Sr. Head")
    head_phone = head_info.get("phone", "+63 917 843 6128")
    head_email = head_info.get("email", "sondituazon.primecorp@gmail.com")
    head_contact = (
        f"{head_name}\n"
        f"{head_title} – Retail and Industrial Markets\n"
        f"{head_phone}\n"
        f"{head_email}"
    )

    for shp in cta_slide.shapes:
        if shp.has_text_frame:
            txt = shp.text_frame.text.strip()
            if "Cedtrix Rena" in txt or "Sr. Leasing Advisor" in txt:
                shp.text_frame.text = advisor_contact
            elif "Sondi Tuazon" in txt or "Sr.Head" in txt:
                shp.text_frame.text = head_contact

    # 5. Clean up unused slides if properties < 6
    slides_to_delete = []
    
    if not data.get("include_site_development_plan", False):
        slides_to_delete.extend([10, 11]) # Site Dev & Other Photos
    if not data.get("include_site_layout", False):
        slides_to_delete.append(16) # Site Layout

    for p_idx in range(num_props, 6):
        if p_idx < len(prop_pairs):
            s_over, s_det = prop_pairs[p_idx]
            slides_to_delete.extend([s_over, s_det])

    slides_to_delete = sorted(list(set(slides_to_delete)), reverse=True)
    print(f"[*] Cleaning up {len(slides_to_delete)} unused template slides...")
    for s_idx in slides_to_delete:
        delete_slide_clean(prs, s_idx)

    # 6. Save presentation
    os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
    prs.save(str(output_path))
    print(f"[SUCCESS] Proposal successfully generated: {output_path} ({len(prs.slides)} slides)")
    return output_path

def main():
    parser = argparse.ArgumentParser(description="PRIME Proposal Deck Generator")
    parser.add_argument("--data", "-d", required=True, help="Path to proposal JSON data file")
    parser.add_argument("--template", "-t", default=None, help="Custom PPTX template path (optional)")
    parser.add_argument("--output", "-o", default=None, help="Output PPTX filepath (optional)")
    args = parser.parse_args()

    data = load_json(args.data)
    build_proposal_deck(data, template_path=args.template, output_path=args.output)

if __name__ == "__main__":
    main()
