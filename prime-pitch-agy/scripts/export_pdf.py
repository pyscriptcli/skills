#!/usr/bin/env python3
"""
PRIME Pitch AGY - Headless PDF Export Utility
Converts an interactive 16:9 presentation HTML file into a 1-to-1 clone PDF.
"""

import os
import sys
import subprocess

def find_browser():
    candidates = [
        r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
    ]
    for c in candidates:
        if os.path.exists(c):
            return c
    return None

def export_to_pdf(html_path, pdf_path=None):
    if not os.path.exists(html_path):
        print(f"Error: HTML file not found: {html_path}")
        sys.exit(1)

    if not pdf_path:
        base, _ = os.path.splitext(html_path)
        pdf_path = f"{base}.pdf"

    browser = find_browser()
    if not browser:
        print("Error: Neither Microsoft Edge nor Google Chrome was found for headless printing.")
        sys.exit(1)

    abs_html = os.path.abspath(html_path)
    abs_pdf = os.path.abspath(pdf_path)
    file_url = "file:///" + abs_html.replace("\\", "/")

    cmd = [
        browser,
        "--headless=new",
        "--disable-gpu",
        "--no-pdf-header-footer",
        f"--print-to-pdf={abs_pdf}",
        file_url
    ]

    print(f"Compiling PDF via {os.path.basename(browser)}...")
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode != 0:
        print("Browser error:", res.stderr)
        sys.exit(res.returncode)

    if os.path.exists(abs_pdf):
        print(f"Success: Wrote 1-to-1 PDF clone to {abs_pdf} ({os.path.getsize(abs_pdf)} bytes)")
    else:
        print("Error: PDF file was not created.")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python export_pdf.py <path_to_html_file> [path_to_output_pdf]")
        sys.exit(1)
    
    html_arg = sys.argv[1]
    pdf_arg = sys.argv[2] if len(sys.argv) > 2 else None
    export_to_pdf(html_arg, pdf_arg)
