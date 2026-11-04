#!/usr/bin/env python3
"""Run axe-core (WCAG 2.1 A/AA rules) over built page fragments and the practice widget.
   python3 tools/axe_scan.py pages/*.html [practice.html]  → prints violations per file, summary at the end."""
import sys, re, json, os, tempfile
from playwright.sync_api import sync_playwright
AXE = os.path.join(os.path.dirname(__file__), 'axe.min.js')
css = """body{font-family:Lato,Helvetica,Arial,sans-serif;font-size:16px;line-height:1.5;color:#222;margin:0;padding:24px;background:#fff}
.box-objectives,.box-note,.box-example,.box-exercise{border-left:6px solid #0e6ea8;background:#f4f8fb;padding:10px 16px;margin:14px 0}
.box-objectives{border-color:#2e8b57;background:#f1f8f3}.box-example{border-color:#c0392b;background:#fdf4f3}.box-exercise{border-color:#7a5c9b;background:#f6f3fa}
.boxtitle{font-weight:700}figcaption{font-size:.92em;color:#444}summary{color:#0e6ea8;font-weight:600}"""
def wrap(src):
    src = re.sub(r'<div class="mt-contentreuse-widget".*?</div>\s*', '', src, flags=re.S)  # transclusion placeholder
    src = re.sub(r'src="(?:/)?(Slide\d+\.png)"', r'src="file:///home/claude/textbook/figures/\1"', src)
    src = src.replace('src="https://itsdrdan.github.io/textbook/figures/', 'src="file:///home/claude/textbook/figures/')
    src = re.sub(r'<iframe[^>]*src="https://itsdrdan[^"]*"', lambda m: m.group(0).replace('https://itsdrdan.github.io/textbook/', 'file:///home/claude/textbook/'), src)
    return f'<!doctype html><html lang="en"><head><meta charset="utf-8"><title>page</title><style>{css}</style></head><body><main><h1>Page title</h1>{src}</main></body></html>'
tot = {}
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={'width': 1000, 'height': 900})
    for f in sys.argv[1:]:
        src = open(f).read()
        html = wrap(src) if not src.lstrip().lower().startswith('<!doctype') else src.replace('https://itsdrdan.github.io/textbook/', 'file:///home/claude/textbook/')
        tf = tempfile.NamedTemporaryFile('w', suffix='.html', delete=False, dir='/tmp'); tf.write(html); tf.close()
        pg.goto('file://' + tf.name); pg.wait_for_timeout(500)
        pg.add_script_tag(path=AXE)
        res = pg.evaluate("async () => await axe.run(document, {runOnly:{type:'tag',values:['wcag2a','wcag2aa','wcag21a','wcag21aa','best-practice']}, iframes:false})")
        os.unlink(tf.name)
        v = res['violations']
        if v:
            print(f'== {f}')
            for x in v:
                ids = [n['target'][0] for n in x['nodes'][:3]]
                print(f"  [{x['impact']}] {x['id']}: {x['help']} ({len(x['nodes'])} nodes) e.g. {ids}")
                tot[x['id']] = tot.get(x['id'], 0) + len(x['nodes'])
    b.close()
print('SUMMARY', json.dumps(tot))
