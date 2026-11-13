import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pathway import render  # Python port of pathway.js (no node needed)
# Print sizing (2026-11-13): font 17 / edge labels 14 so the maps print at about 7 pt; leaf text wraps at 19 characters.
# Each map: title, root, branches [(link, node, [(link, leaf),...]),...]
M = {
1:("Bonding review","Covalent molecules",[
  ("drawn as","Lewis structures",[("count","valence electrons"),("give each atom","its usual bonds + lone pairs")]),
  ("have","Shape (VSEPR)",[("2/3/4 groups","linear / trigonal planar / tetrahedral")]),
  ("have","Polarity",[("from","polar bonds (to N, O, halogens)"),("plus","asymmetric shape")]),
  ("attract by","IMFs",[("weakest","dispersion"),("then","dipole–dipole"),("strongest","hydrogen bonding")]),
  ("organic ones show","Functional groups",[("decide","properties + reactions")])]),
2:("Alkanes and cycloalkanes","Alkanes (C–C single bonds)",[
  ("named by","IUPAC rules",[("parent","longest chain"),("prefix","alkyl groups, halogens")]),
  ("form","Isomers",[("chain","skeletal"),("location","positional")]),
  ("are","Nonpolar",[("only","dispersion forces"),("so","insoluble in water")]),
  ("react by","Combustion",[("gives","CO2 + H2O + energy")]),
  ("react by","Halogenation",[("with light","substitution, X for H")]),
  ("ring form","Cycloalkanes",[("formula","CnH2n")])]),
3:("Alkenes, alkynes, aromatics","Unsaturated hydrocarbons",[
  ("C=C","Alkenes (-ene)",[("may be","cis or trans"),("undergo","addition reactions")]),
  ("C≡C","Alkynes (-yne)",[("shape","linear")]),
  ("addition","Four reactions",[("add","H2, X2, HX, H2O"),("HX, H2O follow","Markovnikov's rule")]),
  ("reverse","Elimination",[("major product","Zaitsev's rule")]),
  ("chains of","Addition polymers",[]),
  ("special ring","Benzene (aromatic)",[("reacts by","substitution, not addition")])]),
4:("Alcohols, phenols, ethers, thiols","C–O and C–S single bonds",[
  ("R–OH","Alcohols",[("classified","1°, 2°, 3°"),("hydrogen bond","high bp, small ones soluble")]),
  ("Ar–OH","Phenols",[("more acidic than","alcohols")]),
  ("R–O–R","Ethers",[("bp near","alkanes")]),
  ("R–SH","Thiols",[("oxidize to","disulfides")]),
  ("alcohols","React",[("dehydration","alkene (Zaitsev)"),("oxidation","aldehyde / ketone / acid")])]),
5:("Aldehydes and ketones","Carbonyl group C=O",[
  ("at chain end","Aldehydes (-al)",[("oxidize to","carboxylic acids"),("detected by","Tollens', Benedict's")]),
  ("inside chain","Ketones (-one)",[("do not","oxidize")]),
  ("reduce to","Alcohols",[("aldehyde","1° alcohol"),("ketone","2° alcohol")]),
  ("+ alcohol","Hemiacetal",[("+ alcohol","acetal"),("in one molecule","sugar rings")]),
  ("handedness","Chirality",[("4 different groups","chiral carbon"),("mirror images","enantiomers, D/L")])]),
6:("Carboxylic acids and esters","Acyl group C(=O)–",[
  ("–COOH","Carboxylic acids",[("weak acids","RCOO− in body"),("+ base","carboxylate salts")]),
  ("acid + alcohol","Esterification",[("condensation","loses H2O")]),
  ("–COO–","Esters",[("smell","fruity"),("no O–H","lower bp than acids")]),
  ("split by water","Hydrolysis",[("acid","acid + alcohol"),("base","carboxylate salt (saponification)")]),
  ("with phosphate","Phosphate esters",[("in","ATP, DNA")])]),
7:("Amines and amides","Organic nitrogen",[
  ("R–NH2","Amines",[("classified","1°, 2°, 3°, quaternary"),("are","weak bases")]),
  ("+ acid","Ammonium salts",[("soluble","drug hydrochlorides")]),
  ("–C(=O)N–","Amides",[("not","bases")]),
  ("acid + amine","Amidation",[("condensation","loses H2O")]),
  ("split by water","Amide hydrolysis",[("acid","acid + NH4+ salt"),("base","carboxylate + amine")]),
  ("in rings / body","Heterocycles, neurotransmitters",[])]),
8:("Carbohydrates","Sugars",[
  ("one unit","Monosaccharides",[("C=O type","aldose / ketose"),("drawn as","Fischer, D/L")]),
  ("cyclize to","Hemiacetal rings",[("anomers","α / β (Haworth)")]),
  ("redox","Sugar reactions",[("oxidized","reducing sugars, sugar acids"),("reduced","sugar alcohols")]),
  ("glycosidic bond","Disaccharides",[("examples","maltose, lactose, sucrose")]),
  ("many units","Polysaccharides",[("examples","starch, glycogen, cellulose")])]),
9:("Lipids","Lipids (dissolve in nonpolar solvents)",[
  ("hydrolyzable","Fatty acid esters",[("3 FA + glycerol","triacylglycerols"),("+ phosphate","phospholipids")]),
  ("building block","Fatty acids",[("cis C=C","lower mp"),("named","omega-3, omega-6")]),
  ("react","TAG reactions",[("H2","hydrogenation"),("NaOH","saponification (soap)")]),
  ("non-hydrolyzable","Steroids",[("examples","cholesterol, hormones, bile salts")]),
  ("form","Membranes",[("bilayer","transport: diffusion, facilitated, active")])]),
10:("Amino acids and proteins","Proteins",[
  ("built from","Amino acids",[("R groups","nonpolar, polar, acidic, basic"),("in water","zwitterions, pI")]),
  ("joined by","Peptide bonds",[("named","N- to C-terminus")]),
  ("1°","Sequence",[]),
  ("2°","Helix and sheet",[("held by","backbone H bonds")]),
  ("3° and 4°","Folding",[("held by","R-group interactions")]),
  ("lose shape","Denaturation",[("not","hydrolysis")])]),
11:("Enzymes and vitamins","Enzymes (protein catalysts)",[
  ("bind substrate at","Active site",[("models","lock-and-key, induced fit")]),
  ("sorted into","Six classes",[("e.g.","oxidoreductase, hydrolase")]),
  ("activity depends on","Conditions",[("optimum","37 °C, pH")]),
  ("slowed by","Inhibitors",[("types","competitive, noncompetitive, irreversible")]),
  ("need","Cofactors / coenzymes",[("from","B vitamins")]),
  ("regulated by","Control",[("fast","allosteric, feedback"),("slow","zymogens, genes")])]),
12:("Nucleic acids","DNA and RNA",[
  ("made of","Nucleotides",[("parts","base + sugar + phosphate")]),
  ("DNA","Double helix",[("pairs","A=T, G≡C")]),
  ("copied by","Replication",[("result","semiconservative")]),
  ("DNA → mRNA","Transcription",[]),
  ("mRNA → protein","Translation",[("read as","codons")]),
  ("changed by","Mutations",[("types","point, insertion, deletion")])]),
13:("Carbohydrate metabolism","Glucose",[
  ("digested from","Starch, sugars",[]),
  ("broken down by","Glycolysis",[("gives","2 pyruvate, 2 ATP, 2 NADH")]),
  ("pyruvate goes to","Acetyl CoA or lactate",[("with O2","acetyl CoA"),("without O2","lactate")]),
  ("stored as","Glycogen",[("made by","glycogenesis"),("broken by","glycogenolysis")]),
  ("made by","Gluconeogenesis",[("from","lactate, amino acids, glycerol")]),
  ("controlled by","Hormones",[("lower","insulin"),("raise","glucagon, epinephrine")])]),
14:("Metabolism and energy","Acetyl CoA",[
  ("enters","Citric acid cycle",[("per turn","3 NADH, 1 FADH2, 1 GTP, 2 CO2")]),
  ("NADH, FADH2 go to","Electron transport",[("ends at","O2 → H2O"),("pumps","H+ out of the matrix")]),
  ("H+ flows back through","ATP synthase",[("process","oxidative phosphorylation")]),
  ("total","ATP per glucose",[("liver","32"),("muscle, brain","30")])]),
15:("Lipid and protein metabolism","Fats and proteins as fuel",[
  ("fatty acids","β-Oxidation",[("per cycle","1 FADH2, 1 NADH, 1 acetyl CoA"),("palmitate","106 ATP")]),
  ("excess acetyl CoA","Ketone bodies",[("too many","ketoacidosis")]),
  ("reverse, in cytosol","Lipogenesis",[]),
  ("amino acids","Transamination",[("then","oxidative deamination")]),
  ("NH4+ removed by","Urea cycle",[]),
  ("carbon skeletons become","Pyruvate, acetyl CoA, cycle",[("sorted as","glucogenic or ketogenic")])])}

def spec(ch, title, root, br):
    n=len(br); cols=max(n,3)
    nodes=[{"id":"r","label":root,"col":(cols-1)/2,"row":0,"kind":"start"}]; edges=[]
    for i,(lk,lab,leaves) in enumerate(br):
        nid=f"b{i}"; nodes.append({"id":nid,"label":lab,"col":i,"row":1.25,"kind":"mol"})
        edges.append({"from":"r","to":nid,"label":lk,"labelPos":0.74})
        if leaves:
            txt="\n".join("• "+wrap((ll+": "+lf.replace("\n"," ")),16).replace("\n","\n   ") for ll,lf in leaves)
            nodes.append({"id":f"l{i}","label":txt,"col":i,"row":2.8,"kind":"note"})
            edges.append({"from":nid,"to":f"l{i}","kind":"side"})
    return {"title":f"Chapter {ch} concept map: {title}","colw":205,"rowh":100,"font":17,"edgefont":14,"pad":18,"nodes":nodes,"edges":edges}

def wrap(s, w=19):
    out=[];line=''
    for word in s.split():
        if len(line)+len(word)+1>w and line: out.append(line); line=word
        else: line=(line+' '+word).strip()
    out.append(line); return '\n'.join(out)

alts={}
for ch,(title,root,br) in M.items():
    br2=[(lk,wrap(lab),[(ll,wrap(lf)) for ll,lf in lv]) for lk,lab,lv in br]
    sp=spec(ch,title,wrap(root,24),br2)
    # alt text
    parts=[]
    for lk,lab,lv in br:
        s=f"{root} {lk} {lab}"
        if lv: s+=" ("+"; ".join(f"{ll}: {lf}" for ll,lf in lv)+")"
        parts.append(s)
    alt=f"Concept map for Chapter {ch}, {title}. "+". ".join(parts)+"."
    sp["alt"]=alt; alts[ch]=alt
    open(f"figures/conceptmaps/ch{ch:02d}.svg","w").write(render(sp))
json.dump(alts,open("/tmp/cm_alts.json","w"),ensure_ascii=False,indent=0)
print("done", len(os.listdir("figures/conceptmaps")))
