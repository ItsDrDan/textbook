"""Batch AK (2026-11-15): print a QR code for every Try It and Hands-on Lab box, like LibreTexts does for YouTube videos.
Author's request 2026-11-15: the "Not loading? Open this practice in a new tab" line prints in the PDF; use a QR code instead.

- Each box gets a short address, itsdrdan.github.io/textbook/t/<code> (a static page that forwards to the full practice or
  lab link), because the Try It links are 82-616 characters long and would make QR codes too dense to scan from paper.
- QR images: qr/<code>.svg (segno, error correction M), shown about 1 inch wide.
- On screen nothing changes. In print, the "Not loading?" line is hidden (wrapped in <div class="hideprint">; LibreTexts' PDF
  ignores hideprint on a plain <p> but honors it on a div, as the inline answers show) and a showprint block prints the QR
  code with the short address.
Run with the scratch venv python (needs segno). Output: t/*.html, qr/*.svg, tools/batchAK_2026-11-15.json,
tools/batchAK_sha_2026-11-15.json, audit/preview/<id>.html, audit/BATCH_AK_REVIEW.md"""
import glob, hashlib, html, json, os, re
import segno

BASE = 'https://itsdrdan.github.io/textbook/'
SHORT = 'itsdrdan.github.io/textbook/t/'
NOTLOAD = re.compile(r'<p( class="hideprint")? style="font-size:0\.9em;">Not loading\? <a [^>]*href="([^"]+)"[^>]*>(Open this (?:practice|lab) in a new tab)</a>\.</p>\n')
LABPRINT = re.compile(r'<p class="showprint" style="font-size:0\.9em;">This lab runs online: open this section in the web edition of the book, or play it in <em>([^<]+)</em> at itsdrdan\.github\.io\.</p>\n')
HBOND_PRINT = '<p class="showprint" style="font-size:0.9em;">The H-Bond Lab is in <em>Sticky Molecules</em> at itsdrdan.github.io; the web edition links to it.</p>\n'

os.makedirs('t', exist_ok=True)
os.makedirs('qr', exist_ok=True)


def make_short(code, target, label):
    t = html.escape(target)
    open('t/%s.html' % code, 'w', encoding='utf-8').write(
        '<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="robots" content="noindex">'
        '<meta name="viewport" content="width=device-width,initial-scale=1"><title>%s</title>'
        '<meta http-equiv="refresh" content="0; url=%s"><script>location.replace(%s)</script></head>'
        '<body style="font-family:system-ui,sans-serif;padding:24px"><p><a href="%s">%s</a></p></body></html>\n'
        % (html.escape(label), t, json.dumps(target), t, html.escape(label)))
    segno.make(BASE + 't/' + code, error='m').save('qr/%s.svg' % code, scale=4, border=2, dark='#1f2a44', xmldecl=False, svgns=True, omitsize=True)


def qr_block(code, sentence):
    return ('<div class="showprint" style="font-size:0.9em;overflow:hidden;">'
            '<img src="%sqr/%s.svg" alt="QR code for %s%s" width="96" height="96" style="float:right;width:96px;height:96px;margin:0 0 6px 12px;" />'
            '<p>%s Scan the QR code or go to <strong>%s%s</strong>.</p></div>\n') % (BASE, code, SHORT, code, sentence, SHORT, code)


h = lambda x: hashlib.sha256(x.encode()).hexdigest()
edits, sha, rows = {}, {}, []
for f in sorted(glob.glob('pages/live/*.html')):
    pid = os.path.basename(f)[:-5]
    page = open(f, encoding='utf-8').read()
    ms = list(NOTLOAD.finditer(page))
    is_hbond = HBOND_PRINT in page
    if not ms and not is_hbond:
        continue
    after, es, letters = page, [], iter('abcdefgh')
    for m in ms:
        old = m.group(0)
        target = html.unescape(m.group(2))
        is_lab = m.group(3).endswith('lab in a new tab')
        code = pid + ('lab' if is_lab else next(letters))
        # the visible line stays exactly as it is on screen; only the print behavior changes
        visible = old.replace(' class="hideprint"', '')
        new = '<div class="hideprint">\n' + visible + '</div>\n'
        if is_lab:
            lp = LABPRINT.search(after, after.find(old))
            assert lp, pid
            game = lp.group(1)
            old = after[after.find(old):lp.end()]
            new += qr_block(code, 'This lab runs online in <em>%s</em>.' % game)
            make_short(code, target, 'Open the lab')
        else:
            new += qr_block(code, 'This practice runs online.')
            make_short(code, target, 'Open the practice')
        assert after.count(old) == 1, (pid, code)
        after = after.replace(old, new)
        es.append({'old': old, 'new': new, 'count': 1, 'note': '%s: QR code in print (%s)' % (pid, code), 'why': 'Author request 2026-11-15'})
        rows.append((pid, code, target))
    if is_hbond:
        code = pid + 'hb'
        target = BASE.replace('textbook/', '') + 'IMF/?course=3B&mode=lab&view=lab'
        make_short(code, target, 'Open the H-Bond Lab')
        new = qr_block(code, 'The H-Bond Lab is in <em>Sticky Molecules</em>.')
        assert after.count(HBOND_PRINT) == 1
        after = after.replace(HBOND_PRINT, new)
        es.append({'old': HBOND_PRINT, 'new': new, 'count': 1, 'note': '%s: QR code in print (%s)' % (pid, code), 'why': 'Author request 2026-11-15'})
        rows.append((pid, code, target))
    edits[pid] = es
    sha[pid] = {'before': h(page), 'after': h(after)}
    open('audit/preview/%s.html' % pid, 'w', encoding='utf-8').write(after)

json.dump({'uploads': [], 'edits': edits}, open('tools/batchAK_2026-11-15.json', 'w'), ensure_ascii=False, indent=1)
json.dump(sha, open('tools/batchAK_sha_2026-11-15.json', 'w'))
out = ['# Batch AK review: QR codes in print for Try It and lab boxes (2026-11-15)', '',
       '%d boxes on %d pages. Screen view unchanged; in print the "Not loading?" line is hidden and a QR code with a short address prints instead.' % (len(rows), len(edits)), '',
       '| Page | Short address | Opens |', '|---|---|---|']
for pid, code, target in rows:
    out.append('| %s | %s%s | `%s` |' % (pid, SHORT, code, target if len(target) < 120 else target[:117] + '...'))
open('audit/BATCH_AK_REVIEW.md', 'w').write('\n'.join(out) + '\n')
print(len(rows), 'boxes on', len(edits), 'pages')
