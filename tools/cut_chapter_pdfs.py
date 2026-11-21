"""Cut tagged chapter PDFs from a full-book PDF: keep tags, language, title, bookmarks; drop links to pages not in the file."""
import sys,os,json,time,pikepdf,fitz,pypdf
from pikepdf import Name,Array,Dictionary,OutlineItem
sys.setrecursionlimit(20000)
FULL,OLD,OUT=sys.argv[1:4]; only=sys.argv[4:] 
F=[('00_FrontMatter',1,24),('Ch01_BondingReview',25,147),('Ch02_AlkanesAndCycloalkanes',148,226),('Ch03_AlkenesAlkynesAndAromaticCompounds',227,306),('Ch04_AlcoholsPhenolsEthersAndThiols',307,393),('Ch05_AldehydesAndKetones',394,469),('Ch06_CarboxylicAcidsAndEsters',470,547),('Ch07_AminesAndAmides',548,634),('Ch08_Carbohydrates',635,717),('Ch09_Lipids',718,800),('Ch10_AminoAcidsAndProteins',801,892),('Ch11_EnzymesAndVitamins',893,970),('Ch12_NucleicAcidsAndProteinSynthesis',971,1066),('Ch13_CarbohydrateMetabolism',1067,1179),('Ch14_MetabolismAndEnergyProduction',1180,1252),('Ch15_MetabolismOfLipidsAndProteins',1253,1342),('16_BackMatter',1343,1378)]
TOC=fitz.open(FULL).get_toc()
def og(o): return o.objgen
def names(node,out):
    if '/Names' in node:
        a=node.Names
        for i in range(0,len(a),2): out[bytes(a[i])]=a[i+1]
    if '/Kids' in node:
        for k in node.Kids: names(k,out)
def destarr(d,N,C):
    if isinstance(d,Dictionary) and '/D' in d: d=d.D
    if isinstance(d,Array): return d
    if isinstance(d,pikepdf.String): v=N.get(bytes(d))
    elif isinstance(d,Name): v=C.get(str(d)) if C is not None else None
    else: v=None
    if isinstance(v,Dictionary) and '/D' in v: v=v.D
    return v if isinstance(v,Array) else None
def prune_kids(e,pg,keep,gone):
    if '/Pg' in e: pg=og(e.Pg)
    if '/K' not in e: return not (pg is not None and pg not in keep)
    k=e.K; items=list(k) if isinstance(k,Array) else [k]; new=[]
    for x in items:
        if isinstance(x,int) or (isinstance(x,pikepdf.Object) and x._type_name=='integer'):
            if pg in keep: new.append(x)
        elif isinstance(x,Dictionary):
            t=str(x.get('/Type',''))
            if t=='/MCR':
                if (og(x.Pg) if '/Pg' in x else pg) in keep: new.append(x)
            elif t=='/OBJR':
                p=og(x.Pg) if '/Pg' in x else pg
                if p in keep and og(x.Obj) not in gone: new.append(x)
            elif prune_kids(x,pg,keep,gone): new.append(x)
    if not new: return False
    e.K=new[0] if len(new)==1 else Array(new)
    return True
def cut(base,a,b):
    pdf=pikepdf.open(FULL); root=pdf.Root; keep={og(pdf.pages[i].obj) for i in range(a-1,b)}
    N={}
    if '/Names' in root and '/Dests' in root.Names: names(root.Names.Dests,N)
    C=root.Dests if '/Dests' in root else None
    gone=set(); stats=[0,0]
    for i in range(a-1,b):
        pg=pdf.pages[i].obj
        if '/Annots' not in pg: continue
        out=[]
        for an in pg.Annots:
            if an.get('/Subtype')!=Name.Link: out.append(an); continue
            act=an.get('/A'); d=an.get('/Dest')
            if act is not None and act.get('/S')==Name.GoTo: d=act.D
            elif act is not None: out.append(an); continue
            arr=destarr(d,N,C) if d is not None else None
            if arr is not None and len(arr) and og(arr[0]) in keep:
                if '/A' in an: del an['/A']
                an.Dest=pdf.make_indirect(Array(list(arr))); out.append(an); stats[0]+=1
            else: gone.add(og(an)); stats[1]+=1
        pg.Annots=Array(out)
    sr=root.StructTreeRoot
    k=sr.K; tops=list(k) if isinstance(k,Array) else [k]
    tops=[t for t in tops if prune_kids(t,None,keep,gone)]
    sr.K=tops[0] if len(tops)==1 else Array(tops)
    alive=set()
    def mark(e):
        alive.add(og(e))
        if '/K' in e:
            for x in (list(e.K) if isinstance(e.K,Array) else [e.K]):
                if isinstance(x,Dictionary) and str(x.get('/Type','')) not in('/MCR','/OBJR'): mark(x)
    for t in tops: mark(t)
    PT={}
    def ptree(n):
        if '/Nums' in n:
            a_=n.Nums
            for i in range(0,len(a_),2): PT[int(a_[i])]=a_[i+1]
        if '/Kids' in n:
            for x in n.Kids: ptree(x)
    ptree(sr.ParentTree)
    used=set()
    for i in range(a-1,b):
        pg=pdf.pages[i].obj
        if '/StructParents' in pg: used.add(int(pg.StructParents))
        if '/Annots' in pg:
            for an in pg.Annots:
                if '/StructParent' in an: used.add(int(an.StructParent))
    nums=[]
    for key in sorted(used):
        v=PT.get(key)
        if v is None: continue
        if isinstance(v,Array): v=pdf.make_indirect(Array([x if isinstance(x,Dictionary) and og(x) in alive else None for x in v]))
        elif not(isinstance(v,Dictionary) and og(v) in alive): continue
        nums+= [key,v]
    sr.ParentTree=pdf.make_indirect(Dictionary(Nums=Array(nums)))
    if '/IDTree' in sr: del sr['/IDTree']
    for key in ('/Dests','/Outlines','/PageLabels'):
        if key in root: del root[key]
    if '/Names' in root and '/Dests' in root.Names: del root.Names['/Dests']
    if '/PageMode' in root: del root['/PageMode']
    for i in range(len(pdf.pages)-1,-1,-1):
        if not(a-1<=i<b): del pdf.pages[i]
    ent=[x for x in TOC if a<=x[2]<=b]
    if ent:
        low=min(x[0] for x in ent)
        with pdf.open_outline() as ol:
            st=[(low-1,ol.root)]
            for lv,title,p,*_ in ent:
                it=OutlineItem(title,p-a)
                while st[-1][0]>=lv and len(st)>1: st.pop()
                (st[-1][1] if st[-1][1] is ol.root else st[-1][1].children).append(it); st.append((lv,it))
        root.PageMode=Name.UseOutlines
    o=pypdf.PdfReader(os.path.join(OLD,base+'.pdf')).metadata
    T,A,Sb=o.title,o.author,o.subject
    with pdf.open_metadata(set_pikepdf_as_editor=False) as m:
        m['dc:title']=T; m['dc:creator']=[A]; m['dc:description']=Sb
    pdf.docinfo['/Title']=T; pdf.docinfo['/Author']=A; pdf.docinfo['/Subject']=Sb
    dst=os.path.join(OUT,base+'.pdf')
    pdf.save(dst,object_stream_mode=pikepdf.ObjectStreamMode.generate,compress_streams=True,linearize=False)
    return os.path.getsize(dst),stats
M={}
for base,a,b in F:
    if only and base not in only: continue
    t=time.time(); s,st=cut(base,a,b); M[base]={'first':a,'last':b,'pages':b-a+1,'bytes':s,'internal_links':st[0],'links_removed':st[1]}
    print(base,b-a+1,'pp',round(s/1048576,2),'MB links kept',st[0],'removed',st[1],round(time.time()-t,1),'s',flush=True)
if not only: json.dump(M,open(os.path.join(OUT,'manifest.json'),'w'),indent=1)
