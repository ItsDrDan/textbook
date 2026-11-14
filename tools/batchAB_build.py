"""Batch AB (2026-11-13): "Use of AI tools" section in About This Book (page 597270), after the sources statement.
Wording approved by the author: review sentence = "approved each set ... read a sample of each set closely".
Output: tools/batchAB_2026-11-13.json, tools/batchAB_sha_2026-11-13.json, audit/preview/597270.html"""
import json, hashlib
p = '597270'; t = open('pages/live/%s.html' % p, encoding='utf-8').read()
old = '</div><div class="mt-section" id="section_5"><h2 class="editable">Licensing</h2>'
assert t.count(old) == 1
SECTION = ('</div><div class="mt-section" id="section_ai"><h2 class="editable">Use of AI tools</h2>\n'
  '<p>The author used AI tools, mainly Claude (Anthropic), while building and revising this book. They were used to:</p>\n'
  '<ul>\n'
  '<li>draft and revise some explanations, practice exercises, answer keys, and &ldquo;Think about it&rdquo; questions;</li>\n'
  '<li>write and check practice and ADAPT questions, with their hints and feedback;</li>\n'
  '<li>compare the book with the course outline, flag chemistry and answer-key errors, and check facts against published sources;</li>\n'
  '<li>draw and redraw figures, and size their labels so they can be read in print and on phones;</li>\n'
  '<li>improve accessibility (image descriptions, heading order, color contrast) and layouts for phones and tablets;</li>\n'
  '<li>code the Try It boxes and study games, and format the web and PDF versions.</li>\n'
  '</ul>\n'
  '<p>The author decided what went into the book, approved each set of AI-drafted changes before it was published, read a sample of each set closely, and corrected what was wrong. The author is responsible for the accuracy of everything in it. If you find an error, please report it (see Reviews, errata and acknowledgments below).</p>\n\n')
new = SECTION + old
n = t.replace(old, new)
assert '—' not in SECTION and '&mdash;' not in SECTION
h = lambda s: hashlib.sha256(s.encode()).hexdigest()
json.dump({'uploads': [], 'edits': {p: [{'old': old, 'new': new, 'count': 1, 'note': 'About This Book: Use of AI tools section'}]}}, open('tools/batchAB_2026-11-13.json', 'w'), ensure_ascii=False, indent=1)
json.dump({p: {'before': h(t), 'after': h(n)}}, open('tools/batchAB_sha_2026-11-13.json', 'w'))
open('audit/preview/%s.html' % p, 'w', encoding='utf-8').write(n)
print('1 edit')
