/* Draw one structure or a reaction scheme as inline SVG for the textbook pages.
   node tools/draw.js struct "<SMILES>" [skeletal|condensed|expanded] [scale]      → SVG of one molecule
   node tools/draw.js rxn <TPLkey> "<regex on first reactant name>" [altText]      → reaction scheme SVG (reactants → products, with conditions)
   node tools/draw.js rxnlist                                                      → the TPL keys you can use
   node tools/draw.js lib                                                          → compound names in the library (for the regex)
   Output goes to stdout; wrap it in <figure class="figure">…<figcaption>…</figcaption></figure>. */
const S=require('./scheme.js'), E=S.E;
const [mode,a,b,c]=process.argv.slice(2);
if(mode==='struct'){ const style=b||'skeletal'; let svg;
  if(style==='expanded'){ svg=E.expandedSVG(E.parseSmi(a),{scale:+(c||0.9)}); if(!svg){ console.error('expanded drawing not available for rings/multi-part SMILES; falling back to skeletal'); svg=E.structHTML(a,'skeletal'); } }
  else if(style==='condensed'){ process.stdout.write(E.condHTML(E.condensedStr(E.parseSmi(a)))); process.exit(0); }
  else svg=E.structHTML(a,'skeletal');
  process.stdout.write((/xmlns=/.test(svg)?svg:svg.replace('<svg ','<svg xmlns="http://www.w3.org/2000/svg" ')).replace('<svg ','<svg style="max-width:100%;height:auto" ')); }
else if(mode==='rxn'){ const r=S.want(a,x=>new RegExp(b,'i').test(x.reactants[0].name||'')); process.stdout.write(S.scheme(r,c||(r.type+': '+r.reactants.filter(p=>p.smi).map(p=>p.name).join(' + ')+' gives '+r.products.filter(p=>p.smi).map(p=>p.name).join(' + ')))); }
else if(mode==='rxnlist'){ console.log(Object.keys(E.TPL).join(' ')); }
else if(mode==='lib'){ console.log('Library generators (lib.alkane(n), lib.alcohol(n,p) …) are functions; the reaction templates pick from them. For a figure just pass a SMILES to `struct`. Common SMILES: ethanol CCO, 2-propanol CC(C)O, acetone CC(=O)C, acetic acid CC(=O)O, ethyl acetate CC(=O)OCC, phenol Oc1ccccc1 (write as OC1=CC=CC=C1), benzene C1=CC=CC=C1, cyclohexane C1CCCCC1, glucose open-chain O=CC(O)C(O)C(O)C(O)CO, lactic acid CC(O)C(=O)O, pyruvic acid CC(=O)C(=O)O, glycerol OCC(O)CO, ethylamine CCN, acetamide CC(=O)N, methanethiol CS, dimethyl ether COC.'); }
else { console.log('see header of tools/draw.js'); }
