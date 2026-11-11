import pdfplumber,sys,json,collections
W=lambda c: c in ((1.0,),(1,),(1.0,1.0,1.0),(1,1,1)) or c==[1] or c==[1,1,1]
res=collections.OrderedDict()
with pdfplumber.open('Full.pdf') as pdf:
  for i,pg in enumerate(pdf.pages):
    cs=pg.chars; hid=[]
    for c in cs:
      if W(c.get('stroking_color')) and not W(c.get('non_stroking_color')) and c.get('non_stroking_color') is not None:
        # is there a copy at same spot without white stroke?
        ok=any(d is not c and d['text']==c['text'] and abs(d['x0']-c['x0'])<.3 and abs(d['top']-c['top'])<.3 and not W(d.get('stroking_color')) and not W(d.get('non_stroking_color')) for d in cs)
        if not ok: hid.append(c['text'])
    if hid: res[i+1]=''.join(hid)
json.dump(res,open('hidden.json','w'),ensure_ascii=False)
print(len(res),'pages', sum(len(v) for v in res.values()),'hidden glyphs')
