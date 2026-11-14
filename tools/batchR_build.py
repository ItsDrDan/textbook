"""Batch R (2026-11-13): the open items left after batch Q. DRAFT ONLY until the instructor says "publish".
Count-checked against pages/live (which matches the live book after batch Q).
Parts:
  A  the seven Rosa story edits held out of batch Q (instructor: "fix everything", 2026-11-13)
  B  small page fixes: 3.2 heading levels; new-tab links on 1.8 and 3.1 that still opened the old question filter;
     Try It titles on 6.1 and 12.2; accessibility statement (glossary pop-ups); About sentence on "Think about it"
  C  "Think about it" questions for the ten Valley Connection boxes that had none            (audit/edits/r_valley.json)
  D  one practice exercise for each section page that had none                              (audit/edits/r_exercises.json)
  E  Check steps for Chapter Guide examples in 1.9, 2.10, 3.9                               (audit/edits/r_checks.json)
  F  fact fixes from the rechecks                                                            (r_valley.json rechecks, r_checks.json facts)
  G  Try It selections that use the new bank questions (1.3 Lewis, 3.1 naming, 15.5 ketone bodies) and chapter caps
     on the cumulative mixes                                                                 (audit/edits/r_widgets.json)
Output: tools/batchR_2026-11-13.json {uploads, edits}, tools/batchR_sha_2026-11-13.json, audit/preview/<id>.html"""
import json, re, hashlib, os

L = 'pages/live/'
pages, edits, uploads, orig, skipped = {}, {}, [], {}, []


def page(p):
    p = str(p)
    if p not in pages:
        pages[p] = open(L + p + '.html', encoding='utf-8').read(); orig[p] = pages[p]
    return pages[p]


def e(p, old, new, note, n=1):
    p = str(p); t = page(p); assert t.count(old) == n, (p, note, t.count(old))
    assert old != new, (p, note)
    pages[p] = t.replace(old, new); edits.setdefault(p, []).append({'old': old, 'new': new, 'count': n, 'note': note})


def soft(p, old, new, note, n=1):
    if old and new and page(p).count(old) == n and old != new: e(p, old, new, note, n=n)
    else: skipped.append((str(p), note[:80], page(p).count(old) if old else 'no old'))


def load(f):
    return json.load(open(f, encoding='utf-8')) if os.path.exists(f) else None


# ---------------- A: held Rosa story edits ----------------
for x in json.load(open('audit/edits/rosa_valley.json', encoding='utf-8')):
    if x.get('skip'):
        soft(x['page_id'], x['old'], x['new'], 'A Rosa ' + str(x.get('section', ''))[:50] + ': ' + x.get('reason', '')[:180])

# ---------------- B: small page fixes ----------------
# 3.2: Example was h4 directly under an h2 (heading level skipped)
e('597079', '<h4 class="box-legend editable">Example \\(\\PageIndex{1}\\)</h4>', '<h3 class="box-legend editable">Example \\(\\PageIndex{1}\\)</h3>', 'B 3.2 heading order: Example h4 -> h3 (it sat directly under an h2)')
t = page('597079')
m = re.search(r'<h5 class="editable">Solution</h5>', t)
if m and t.count(m.group(0)) == 1:
    e('597079', m.group(0), '<h4 class="editable">Solution</h4>', 'B 3.2 heading order: Solution h5 -> h4')
else:
    skipped.append(('597079', 'Solution heading pattern', t.count('>Solution</h')))

# new-tab links that still opened the old loose question filter
for p in ('597061', '597078'):
    t = page(p)
    m = re.search(r'<iframe[^>]*src="(https://itsdrdan\.github\.io/textbook/practice\.html[^"]*)"[^>]*>.*?href="(https://itsdrdan\.github\.io/textbook/practice\.html[^"]*)"', t, flags=re.S)
    assert m and m.group(1) != m.group(2), p
    e(p, 'href="' + m.group(2) + '"', 'href="' + m.group(1) + '"', 'B "Open this practice in a new tab" opened the old question filter; now the same selection as the embedded box')

# Try It titles that promised a later section
for p, old_t, new_t, enc in (('597109', 'Naming acids and esters', 'Naming carboxylic acids', '%20'), ('597176', 'DNA structure and replication', 'DNA structure', '+')):
    t = page(p)
    a, b = 'title=' + old_t.replace(' ', enc), 'title=' + new_t.replace(' ', enc)
    if t.count(a): e(p, a, b, f'B Try It title: "{old_t}" -> "{new_t}" (the rest is taught in a later section)', n=t.count(a))
    for a, b in (('Try It: ' + old_t, 'Try It: ' + new_t),):
        if page(p).count(a): e(p, a, b, f'B Try It title text: "{old_t}" -> "{new_t}"', n=page(p).count(a))

# accessibility statement: say what the platform's glossary pop-ups need
old = 'the games have no required timed mode.'
if page('597270').count(old) == 1:
    e('597270', old, old + ' One limit comes from the platform, not from this book: the pop-up definitions that appear on glossary words open with a mouse or a touch only. The same definitions are on the Glossary page, which works with the keyboard and with screen readers.',
      'B accessibility statement: glossary pop-ups (added by LibreTexts) cannot be opened from the keyboard; the Glossary page is the accessible route')
else:
    skipped.append(('597270', 'accessibility sentence anchor', page('597270').count(old)))

# ---------------- C: Valley "Think about it" questions ----------------
V = load('audit/edits/r_valley.json')
n_valley = 0
keyadd = {}   # page -> list of (label, answer_html) to add to the print key


def add_key_items(p, items):
    """append print-key entries (create the key if the page has none). The page ends with a run of closing </div>
    tags; the entries (or the new key) go just before that run."""
    t = page(p)
    html_items = ''.join('<div class="answer-key-item"><p style="page-break-after:avoid;break-after:avoid"><strong>' + lab + '</strong></p><div>' + ans + '</div></div>\n' for lab, ans in items)
    m = re.search(r'(?:\s*</div>)+\s*$', t)
    head, tail = t[:m.start()], t[m.start():]
    anchor = head[-90:] + tail
    if t.count(anchor) != 1:
        skipped.append((p, 'page tail not unique; key entries not added', anchor[-60:])); return
    if 'showprint answer-key' in t:
        # the key is the last block on the page: the first two closing divs of the run close its last entry
        k = re.match(r'\s*</div>\s*</div>', tail)
        assert k and t.rfind('answer-key-item') > t.rfind('showprint answer-key'), p
        e(p, anchor, head[-90:] + tail[:k.end()] + '\n' + html_items.rstrip('\n') + tail[k.end():], 'print key: ' + ', '.join(l for l, _ in items))
    else:
        key = '\n\n<div class="showprint answer-key"><div class="mt-section"><h2 class="editable">Answers</h2>\n' + html_items + '</div></div>'
        e(p, anchor, head[-90:] + key + tail, 'print-only answer key added: ' + ', '.join(l for l, _ in items))


if V:
    for x in V.get('questions', []):
        if x.get('skip'): continue
        before = len(edits.get(str(x['page_id']), []))
        soft(x['page_id'], x['old'], x['new'], 'C Valley Connection ' + str(x['section']) + ': "Think about it" question added (the box had none)')
        if len(edits.get(str(x['page_id']), [])) > before:
            n_valley += 1
            q = re.sub(r'<[^>]+>', '', x.get('question_text', ''))
            lab = '&ldquo;Think about it: ' + ' '.join(q.split()[:6]) + '&hellip;&rdquo;'
            keyadd.setdefault(str(x['page_id']), []).append((lab, x['answer_text']))
    # About This Book: the sentence softened in batch Q is true again
    if n_valley == 10:
        soft('597270', 'Each one cites its sources, and the longer ones end with a &ldquo;Think about it&rdquo; question:', 'Each one cites its sources and ends with a &ldquo;Think about it&rdquo; question:', 'C About This Book: every Valley box has a question again')
    for x in V.get('rechecks', []):
        pe = x.get('proposed_edit')
        if pe and not x.get('skip'):
            soft(pe.get('page_id', x.get('page_id')), pe['old'], pe['new'], 'F Valley recheck ' + str(x.get('item', ''))[:60] + ' (' + str(x.get('source_url', ''))[:90] + ')')

# ---------------- D: practice exercises for sections that had none ----------------
X = load('audit/edits/r_exercises.json')
n_ex = 0
if X:
    for x in X:
        if x.get('skip'): continue
        p = str(x['page_id']); sec = x['section']
        block = ('<div class="box-exercise">\n<p class="boxtitle">Practice ' + sec + '</p>\n' + x['question_html'] +
                 '\n<div class="hideprint answer-inline"><details class="hideprint"><summary>Answer</summary><div>' + x['answer_html'] + '</div></details></div>\n</div>\n')
        before = len(edits.get(p, []))
        soft(p, x['anchor_old'], block + x['anchor_old'], 'D ' + sec + ': practice exercise added (the section had none): ' + x.get('objective_practised', '')[:120])
        if len(edits.get(p, [])) > before:
            n_ex += 1; keyadd.setdefault(p, []).append(('Practice ' + sec, x['answer_html']))

for p, items in keyadd.items():
    add_key_items(p, items)

# ---------------- E: Check steps; F: fact fixes ----------------
K = load('audit/edits/r_checks.json')
if K:
    for x in K.get('checks', []):
        if x.get('skip'): continue
        soft(x['page_id'], x['old'], x['new'], 'E Chapter Guide ' + str(x.get('example', '')) + ': Check step added')
    for x in K.get('facts', []):
        pe = x.get('proposed_edit')
        if pe and not x.get('skip'):
            soft(x['page_id'], pe['old'], pe['new'], 'F ' + str(x.get('item', ''))[:70] + ': ' + str(x.get('verdict', '')) + ' (' + str(x.get('source_url', ''))[:90] + ')')
        ae = x.get('additional_edit')
        if ae and not x.get('skip'):
            soft(x['page_id'], ae['old'], ae['new'], 'F ' + str(x.get('item', ''))[:70] + ' (second edit)')

# ---------------- G: widget selections that depend on the new bank questions / chapter caps ----------------
W = load('audit/edits/r_widgets.json')
if W:
    for x in W:
        if x.get('skip'): continue
        soft(x['page_id'], x['old'], x['new'], 'G ' + x['note'], n=x.get('count', 1))

sha = {p: {'before': hashlib.sha256(orig[p].encode()).hexdigest(), 'after': hashlib.sha256(pages[p].encode()).hexdigest()} for p in edits}
json.dump(sha, open('tools/batchR_sha_2026-11-13.json', 'w'), indent=0)
json.dump({'uploads': uploads, 'edits': edits}, open('tools/batchR_2026-11-13.json', 'w'), ensure_ascii=False, indent=1)
os.makedirs('audit/preview', exist_ok=True)
for f in os.listdir('audit/preview'): os.remove('audit/preview/' + f)
for p in edits: open(f'audit/preview/{p}.html', 'w', encoding='utf-8').write(pages[p])
print(len(uploads), 'uploads;', sum(len(v) for v in edits.values()), 'edits on', len(edits), 'pages; valley questions', n_valley, '; exercises', n_ex)
print('skipped:', skipped)
