"""Batch Z2 (2026-11-13): stop the phone hint line from printing.
The 21:06 full compile printed "Swipe sideways to see the whole figure." on 34 of the 66 batch Z pages, although the
figures themselves printed at full width. On those pages the batch Z style block sat at the very top of the page;
the earlier phone batches (W, X, Y), whose style blocks sit next to their figure, printed correctly.
Two changes per page, each enough on its own:
  1. the hint carries an inline style="display:none" (the phone rule's !important still shows it below 600 px);
  2. the batch Z style block moves from the top of the page to just before the first scroll box or hint
     (or before its paragraph, since LibreTexts closes a <p> that contains a <style>).
Output: tools/batchZ2_2026-11-13.json, tools/batchZ2_sha_2026-11-13.json, audit/preview/<id>.html"""
import json, hashlib, re
Z = json.load(open('tools/batchZ_2026-11-13.json'))['edits']
h = lambda s: hashlib.sha256(s.encode()).hexdigest()
edits, sha = {}, {}
for pid in Z:
    t = open('pages/live/%s.html' % pid, encoding='utf-8').read()
    m = re.match(r'<style type="text/css">/\*<!\[CDATA\[\*/\.fig-scroll-hint \{ display: none !important; \}.*?</style>', t, flags=re.S)
    assert m, pid
    style = m.group(0); n = t[len(style):]
    # hint: inline display:none
    n2 = n.replace('<span class="fig-scroll-hint">', '<span class="fig-scroll-hint" style="display:none">').replace('<p class="fig-scroll-hint">', '<p class="fig-scroll-hint" style="display:none">')
    assert n2.count('class="fig-scroll-hint" style="display:none"') == 1, (pid, n2.count('class="fig-scroll-hint"'))
    # style block before the first hint or scroll box, whichever comes first
    i = min(x for x in (n2.find('<span class="fig-scroll-hint"'), n2.find('<p class="fig-scroll-hint"'), n2.find('<div class="fig-scroll"'), n2.find('<span class="fig-scroll"')) if x >= 0)
    # LibreTexts will not keep a <style> inside a <p>: it closes the paragraph early. Put the block before that <p>.
    o = max(n2.rfind('<p>', 0, i), n2.rfind('<p ', 0, i)); c = n2.rfind('</p>', 0, i)
    if o > c: i = o
    new = n2[:i] + style + n2[i:]
    edits[pid] = [{'old': t, 'new': new, 'count': 'whole', 'note': 'phone hint hidden inline; style block moved next to the first scroll box'}]
    sha[pid] = {'before': h(t), 'after': h(new)}
    open('audit/preview/%s.html' % pid, 'w', encoding='utf-8').write(new)
json.dump(sha, open('tools/batchZ2_sha_2026-11-13.json', 'w'))
json.dump({'pages': list(edits)}, open('tools/batchZ2_2026-11-13.json', 'w'))
print(len(edits), 'pages')
