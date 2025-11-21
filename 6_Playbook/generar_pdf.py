#!/usr/bin/env python3
import markdown, weasyprint, datetime

# Leer playbook.md
with open("playbook.md", "r", encoding="utf-8") as f:
    md = f.read()

css = """
<style>
body{font-family:Arial,Helvetica,sans-serif;margin:40px;line-height:1.6;color:#333}
h1{color:#005a9c;border-bottom:2px solid #005a9c}
h2{color:#0078d4}
pre{background:#f4f4f4;padding:10px;border-left:4px solid #0078d4;overflow-x:auto}
code{background:#e8e8e8;padding:2px 4px;border-radius:3px}
table{border-collapse:collapse;width:100%}
th,td{border:1px solid #ddd;padding:8px}
th{background-color:#f2f2f2}
</style>
"""

html = markdown.markdown(md, extensions=['extra', 'codehilite'])
full_html = f"<html><head><meta charset='utf-8'>{css}</head><body>{html}</body></html>"

weasyprint.HTML(string=full_html, base_url=".").write_pdf("playbook.pdf")
print("✅ PDF generado: playbook.pdf")