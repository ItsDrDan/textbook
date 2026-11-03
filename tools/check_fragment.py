#!/usr/bin/env python3
"""Sanity checks for a LibreTexts HTML fragment: python3 tools/check_fragment.py file.html [--guide|--section|--problems]"""
import sys, re, html
from html.parser import HTMLParser
path = sys.argv[1]; kind = sys.argv[2] if len(sys.argv) > 2 else ''
src = open(path).read()
errs, warns = [], []
VOID = {'br','img','hr','input','meta','link','col','wbr','source'}
class P(HTMLParser):
    def __init__(s): super().__init__(); s.stack=[]; s.n=0
    def handle_starttag(s, t, a):
        s.n+=1
        if t in VOID: return
        s.stack.append((t, s.getpos()))
        d=dict(a)
        if t=='img' and not d.get('alt'): errs.append(f'img without alt at {s.getpos()}')
        if t=='svg' and not (d.get('aria-label') or d.get('role')): warns.append(f'svg without aria-label at {s.getpos()}')
        if t=='img' and d.get('src','').startswith('http') and 'itsdrdan.github.io' not in d.get('src',''): errs.append(f'external image {d.get("src")}')
        if t=='script': errs.append('script tag (will be stripped)')
        if t=='iframe' and not d.get('title'): warns.append('iframe without title')
    def handle_endtag(s, t):
        if t in VOID: return
        if s.stack and s.stack[-1][0]==t: s.stack.pop()
        else:
            # tolerate </p> auto-closing
            if any(x[0]==t for x in s.stack):
                while s.stack and s.stack[-1][0]!=t:
                    bad=s.stack.pop(); errs.append(f'unclosed <{bad[0]}> opened at {bad[1]} (closed by </{t}> at {s.getpos()})')
                s.stack.pop()
            else: errs.append(f'stray </{t}> at {s.getpos()}')
p=P(); p.feed(src)
for t,pos in p.stack: errs.append(f'unclosed <{t}> opened at {pos}')
# headings order
levels=[int(m.group(1)) for m in re.finditer(r'<h([1-6])', src)]
if levels and min(levels)<2: errs.append('h1 used (page title is the h1 in LibreTexts)')
prev=1
for l in levels:
    if l>prev+1: warns.append(f'heading skip h{prev}->h{l}')
    prev=l
if re.search(r'<html|<body|<head', src): errs.append('full document tags present; fragment expected')
figs=re.findall(r'<figure[^>]*>.*?</figure>', src, re.S)
for f in figs:
    if '<figcaption>' not in f: errs.append('figure without figcaption')
    elif not re.search(r'<figcaption>Figure \d+\.\d+:', f): warns.append('figcaption not in "Figure N.x:" form: '+re.sub(r'<[^>]+>','',f)[:60])
if kind=='--guide':
    for h in ['<h2>Key Ideas</h2>','<h2>Worked Examples</h2>','<h2>Practice</h2>']:
        if h not in src: errs.append('missing required heading '+h)
if kind=='--section':
    for h in ['<h2>Summary</h2>','<h2>Exercises</h2>','box-objectives','Attribution']:
        if h not in src: errs.append('missing required part '+h)
if kind=='--problems':
    nums=[int(m.group(1)) for m in re.finditer(r'Problem \d+\.(\d+)', src)]
    if nums!=list(range(1,len(nums)+1)): errs.append(f'problem numbering not continuous: {nums[:5]}…{nums[-5:]}')
    nd=len(re.findall(r'<details>', src)); nb=len(re.findall(r'box-exercise', src))
    if nd<nb: errs.append(f'{nb-nd} problems without <details> answer')
words=len(re.sub(r'<[^>]+>',' ',src).split())
print(f'{path}: {words} words, {len(figs)} figures, {len(re.findall("box-exercise",src))} exercises, {len(re.findall("box-example",src))} examples')
for w in warns: print('  WARN', w)
for e in errs: print('  ERROR', e)
sys.exit(1 if errs else 0)
