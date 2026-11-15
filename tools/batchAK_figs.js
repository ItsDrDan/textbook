/* Batch AK (2026-11-15): carbonyl reduction drawn with [H] over the arrow (co-author: [O]/[H], so reduction is not confused with hydrogenation).
   node tools/batchAK_figs.js -> figures/pages/batchAK/*.svg */
const S=require('./scheme.js'),fs=require('fs');
const red=name=>S.want('reduction',r=>r.reactants[0].name===name,4000);
const out={
 'fig-p597105-1.svg':[red('propanal'),'Reduction: propanal gives 1-propanol'],
 'fig-p597105-2.svg':[red('propanone (acetone)'),'Reduction: propanone (acetone) gives 2-propanol (isopropyl alcohol)'],
 'fig-p597107-2.svg':[red('2-butanone'),'Reduction: 2-butanone gives 2-butanol'],
 'fig-p597105-red-butanal.svg':[red('butanal'),'Reduction: butanal gives 1-butanol'],
 'fig-p597105-red-cyclohexanone.svg':[red('cyclohexanone'),'Reduction: cyclohexanone gives cyclohexanol']};
for(const [f,[r,alt]] of Object.entries(out)){let svg=S.scheme(r,alt).replace(/ style="max-width:100%;height:auto;display:block;margin:0 auto"/,'');
 if(!/^<\?xml/.test(svg))svg='<?xml version="1.0" encoding="UTF-8"?>\n'+svg;fs.writeFileSync('figures/pages/batchAK/'+f,svg);
 console.log(f,r.reactants.map(x=>x.name||x.t).join(' + '),'--',r.cond,'->',r.products.map(x=>x.name).join(', '));}
fs.copyFileSync('figures/pages/batchAK/fig-p597107-2.svg','figures/pages/batchAK/fig-p597107-5.svg');
