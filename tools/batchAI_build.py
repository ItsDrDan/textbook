"""Batch AI (2026-11-14): "Written by Daniel Kwasniewski" on adapted pages that are at least half his own writing.
Author's rule (2026-11-14): he curated every edited page; pages he wrote mainly, or mostly, should say written by him.
Selection: tools/authorship_share_2026-11-14.tsv, share >= 50% (see audit/AUTHORSHIP_SHARE_2026-11-14.md). Source book,
authors and license per section come from the Source Attributions page (597271). Only the existing credit line under the
Lecture Connection changes. Output: tools/batchAI_2026-11-14.json, tools/batchAI_sha_2026-11-14.json, audit/BATCH_AI_REVIEW.md"""
import json, hashlib, re, html, collections
OLD = 'Lecture Connection by Daniel Kwasniewski, Fresno City College, CC BY 4.0; the section text above keeps its own license and attribution.'
SHORT = {'David W. Ball, John W. Hill and Rhonda J. Scott (Saylor Foundation edition, on LibreTexts)': 'David W. Ball, John W. Hill and Rhonda J. Scott',
         'Muhammad Arif Malik (LibreTexts)': 'Muhammad Arif Malik', 'LibreTexts': 'LibreTexts'}
s = open('pages/live/597271.html', encoding='utf-8').read()
src = collections.defaultdict(list)
for r in re.findall(r'<tr>(.*?)</tr>', s, re.S)[1:]:
    c = [re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', '', x))).strip() for x in re.findall(r'<t[dh][^>]*>(.*?)</t[dh]>', r, re.S)]
    if len(c) >= 5: src[c[0].split(':')[0]].append((c[2], c[3], c[4]))
snap = open('pages/LIVE_SNAPSHOT.md').read()
title = {p: html.unescape(t) for p, t in re.findall(r'\| \[(\d+)\]\(live/\d+\.html\) \| (.*?) \|', snap)}
rows = [l.rstrip('\n').split('\t') for l in open('tools/authorship_share_2026-11-14.tsv')]
sel = [r for r in rows if int(r[6]) >= 50]
esc = lambda t: html.escape(t, quote=False)
edits, sha = {}, {}
h = lambda x: hashlib.sha256(x.encode()).hexdigest()
for r in sel:
    pid = r[0]; sec = title[pid].split(':')[0]
    (book, auth, lic), = src[sec]
    new = ('Written by Daniel Kwasniewski, Fresno City College, with text adapted from <em>%s</em> (%s; %s). '
           'The original material on this page, including the Lecture Connection, is CC BY 4.0; the adapted text keeps its source license.') % (esc(book), esc(SHORT.get(auth, auth)), esc(lic))
    page = open('pages/live/%s.html' % pid, encoding='utf-8').read()
    assert page.count(OLD) == 1, pid
    after = page.replace(OLD, new)
    edits[pid] = [{'old': OLD, 'new': new, 'count': 1, 'note': '%s: credit line to "Written by" (%s%% own words)' % (title[pid], r[6]), 'why': 'Author rule 2026-11-14'}]
    sha[pid] = {'before': h(page), 'after': h(after)}
    open('audit/preview/%s.html' % pid, 'w', encoding='utf-8').write(after)
json.dump({'uploads': [], 'edits': edits}, open('tools/batchAI_2026-11-14.json', 'w'), ensure_ascii=False, indent=1)
json.dump(sha, open('tools/batchAI_sha_2026-11-14.json', 'w'))
out = ['# Batch AI review: "Written by" line (2026-11-14)', '', 'Pages at 50% or more own words (estimate in audit/AUTHORSHIP_SHARE_2026-11-14.md). Old line on every page:', '', '> ' + OLD, '', '| Page | Own words | New line |', '|---|---|---|']
for pid, es in edits.items():
    out.append('| %s | %s | %s |' % (es[0]['note'].split(': credit')[0], es[0]['note'].split('(')[-1].rstrip(')'), html.unescape(re.sub(r'<[^>]+>', '', es[0]['new']))))
open('audit/BATCH_AI_REVIEW.md', 'w').write('\n'.join(out) + '\n')
print(len(edits), 'pages')
