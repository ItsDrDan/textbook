#!/usr/bin/env python3
"""Render a LibreTexts page fragment (our drafts) to a PNG so you can look at it.
   python3 tools/preview.py page.html out.png [width=900] [maxheight=6000]
   Boxes get LibreTexts-like styling; iframes are replaced by grey placeholders."""
import sys, re
from playwright.sync_api import sync_playwright
src = open(sys.argv[1]).read()
out = sys.argv[2]; width = int(sys.argv[3]) if len(sys.argv) > 3 else 900; maxh = int(sys.argv[4]) if len(sys.argv) > 4 else 6000
src = re.sub(r'<iframe[^>]*></iframe>', '<div style="background:#eee;border:1px dashed #aaa;padding:40px;text-align:center;color:#777">[embedded widget]</div>', src)
src = re.sub(r'src="(?:/)?(Slide\d+\.png)"', r'src="file:///home/claude/textbook/figures/\1"', src)
src = src.replace('src="https://itsdrdan.github.io/textbook/figures/', 'src="file:///home/claude/textbook/figures/')
css = """
body{font-family:Lato,Helvetica,Arial,sans-serif;font-size:16px;line-height:1.5;color:#222;margin:0;padding:24px;background:#fff}
h2{font-size:1.5em;border-bottom:1px solid #ddd;padding-bottom:4px;margin-top:1.4em}h3{font-size:1.2em;margin-top:1.2em}
table{border-collapse:collapse;margin:10px 0}th,td{border:1px solid #ccc;padding:6px 10px;vertical-align:top}th{background:#f3f3f3}
.box-objectives,.box-note,.box-example,.box-exercise{border-left:6px solid #0e6ea8;background:#f4f8fb;padding:10px 16px;margin:14px 0;border-radius:4px}
.box-objectives{border-color:#2e8b57;background:#f1f8f3}.box-example{border-color:#c0392b;background:#fdf4f3}.box-exercise{border-color:#7a5c9b;background:#f6f3fa}
.boxtitle{font-weight:700;font-size:1.05em;margin:0 0 6px}
figure.figure{margin:14px auto;text-align:center;max-width:100%}figcaption{font-size:.92em;color:#444;margin-top:6px;text-align:left}
details{margin-top:6px}summary{cursor:pointer;font-weight:600;color:#0e6ea8}
img{max-width:100%}svg{max-width:100%;height:auto}
"""
html = f'<!doctype html><meta charset="utf-8"><style>{css}</style><body><div style="max-width:{width-48}px">{src}</div></body>'
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={'width': width, 'height': 900})
    import tempfile, os
    tf = tempfile.NamedTemporaryFile('w', suffix='.html', delete=False, dir='/tmp'); tf.write(html); tf.close()
    pg.goto('file://' + tf.name); pg.wait_for_timeout(400); os.unlink(tf.name)
    h = min(pg.evaluate('document.body.scrollHeight'), maxh)
    pg.set_viewport_size({'width': width, 'height': h}); pg.screenshot(path=out, full_page=False); b.close()
print('wrote', out, 'height', h)
