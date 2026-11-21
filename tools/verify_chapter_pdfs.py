import sys,os,re,json,hashlib,pikepdf,fitz
from pikepdf import Array,Dictionary
sys.setrecursionlimit(20000)
FULL,OUT=sys.argv[1:3]; M=json.load(open(OUT+'/manifest.json')); G=fitz.open(FULL)
def counts(pdf):
    c={}; pagesset={p.obj.objgen:i for i,p in enumerate(pdf.pages)}; bad=0
    def w(e,pg):
        nonlocal bad
        if '/Pg' in e: pg=e.Pg.objgen
        if '/K' not in e: return
        for x in (list(e.K) if isinstance(e.K,Array) else [e.K]):
            if isinstance(x,Dictionary):
                t=str(x.get('/Type',''))
                if t=='/MCR':
                    p=x.Pg.objgen if '/Pg' in x else pg
                    if p in pagesset: c[pagesset[p]]=c.get(pagesset[p],0)+1
                    else: bad+=1
                elif t=='/OBJR': pass
                else: w(x,pg)
            else:
                if pg in pagesset: c[pagesset[pg]]=c.get(pagesset[pg],0)+1
                else: bad+=1
    k=pdf.Root.StructTreeRoot.K
    for t in (list(k) if isinstance(k,Array) else [k]): w(t,None)
    return c,bad
FP=pikepdf.open(FULL); FC,_=counts(FP)
tot=txt=pix=0; L=[]; prob=[]; size=0
for b,m in M.items():
    f=f'{OUT}/{b}.pdf'; d=fitz.open(f); size+=m['bytes']; a=m['first']
    if len(d)!=m['pages']: prob.append((b,'pages'))
    for i in range(len(d)):
        tot+=1; g=G[a-1+i]
        if d[i].get_text()==g.get_text(): txt+=1
        else: prob.append((b,'text',i+1))
        if hashlib.md5(d[i].get_pixmap(dpi=45,annots=False).samples).digest()==hashlib.md5(g.get_pixmap(dpi=45,annots=False).samples).digest(): pix+=1
        else: prob.append((b,'pix',i+1))
    C=' '.join(re.sub(r'\s+','',p.get_text()) for p in d); L+=re.findall(r'textbook/t/(\d+[a-z]*)',C)
    P=pikepdf.open(f); r=P.Root; c,bad=counts(P)
    tagmiss=sum(1 for i in range(len(d)) if c.get(i,0)!=FC.get(a-1+i,0))
    ext=sum(1 for p in d for l in p.get_links() if l['kind']==fitz.LINK_URI); internal=[l for p in d for l in p.get_links() if l['kind']==fitz.LINK_GOTO]
    badl=sum(1 for l in internal if not 0<=l['page']<len(d))
    err=P.check_pdf_syntax() if hasattr(P,'check_pdf_syntax') else P.check()
    ok=bool('/StructTreeRoot' in r and r.MarkInfo.Marked and str(r.Lang)=='en' and r.ViewerPreferences.DisplayDocTitle and d.metadata['title'])
    print(b[:24].ljust(25),len(d),'toc',len(d.get_toc()),'tags',ok,'tagpagesdiff',tagmiss,'foreign',bad,'uri',ext,'goto',len(internal),'badgoto',badl,'errors',len(err))
    if not ok or tagmiss or bad or badl or err: prob.append((b,'struct',str(err)[:120]))
print('pages',tot,'text same',txt,'pixels same',pix); print('QR',len(L),len(set(L)),'labs',len({x for x in L if x.endswith('lab')})); print('MB',round(size/1048576,1)); print('problems',len(prob),prob[:12])
