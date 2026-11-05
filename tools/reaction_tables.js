/* Reaction summary tables (Ch 2-7) and the cumulative Reaction Roadmap.
   node tools/reaction_tables.js  -> sections/reactions/chNN.html, roadmap_table.html, reactions.json
   Rows: [key, test on first reactant name, display name, what happens, section]. Examples are drawn by the Bond Voyage engine (tools/scheme.js). */
const S=require('./scheme.js'),fs=require('fs');
const nm=re=>r=>re.test(r.reactants[0].name||'');
const ROWS={
2:[['combustion',nm(/^propane$/),'Combustion','An alkane burns in O<sub>2</sub> to CO<sub>2</sub> and H<sub>2</sub>O, releasing energy.','2.7'],
   ['substitution',r=>r.reactants[0].name==='ethane'&&/Cl/.test(r.reactants[1].t),'Halogenation (substitution)','Light (h&nu;) and X<sub>2</sub>: one H on the alkane is replaced by a halogen; HX is the by-product.','2.7']],
3:[['hydrogenation',nm(/^propene$/),'Hydrogenation','H<sub>2</sub> with a Pt or Ni catalyst adds across the C=C; the alkene becomes an alkane.','3.4'],
   ['halogenAdd',r=>/ethene/.test(r.reactants[0].name)&&/Br/.test(r.reactants[1].t),'Halogenation (addition)','X<sub>2</sub> adds across the C=C, one halogen on each carbon (a dihaloalkane).','3.4'],
   ['hydrohalogenation',r=>r.reactants[0].name==='propene'&&/HCl/.test(r.reactants[1].t),'Hydrohalogenation','HX adds across the C=C: H on one carbon, X on the other (an alkyl halide).','3.4'],
   ['hydration',nm(/^1-butene$/),'Hydration','H<sub>2</sub>O with an acid catalyst adds across the C=C as H and OH, making an alcohol.','3.4']],
4:[['dehydration',nm(/cyclohexanol/),'Dehydration','H<sub>2</sub>SO<sub>4</sub> and heat remove OH and an H from the neighboring carbon as H<sub>2</sub>O; a C=C forms (the reverse of hydration).','4.5'],
   ['ox1Ald',nm(/^ethanol$/),'Oxidation of a 1&deg; alcohol','Mild [O]: a primary alcohol becomes an aldehyde.','4.5'],
   ['ox1Acid',nm(/^ethanol$/),'Oxidation of a 1&deg; alcohol (excess [O])','Excess oxidizing agent: primary alcohol &rarr; aldehyde &rarr; carboxylic acid.','4.5'],
   ['ox2',nm(/^2-propanol/),'Oxidation of a 2&deg; alcohol','[O]: a secondary alcohol becomes a ketone. A tertiary alcohol does not react.','4.5']],
5:[['oxAldAcid',nm(/acetaldehyde/),'Oxidation of an aldehyde','[O] (including Tollens&rsquo; and Benedict&rsquo;s reagents): &ndash;CHO becomes &ndash;COOH. Ketones do not react.','5.4'],
   ['reduction',nm(/^2-butanone$/),'Reduction','H<sub>2</sub> with Ni adds across the C=O: an aldehyde gives a 1&deg; alcohol, a ketone gives a 2&deg; alcohol.','5.4'],
   ['hemiacetal',r=>/acetaldehyde/.test(r.reactants[0].name)&&r.reactants[1].name==='methanol','Hemiacetal formation','One alcohol adds across the C=O; the carbon ends up with &ndash;OH and &ndash;OR.','5.3'],
   ['acetal',r=>/acetaldehyde/.test(r.reactants[0].name)&&r.reactants[1].name==='methanol','Acetal formation','Two alcohols react with the C=O (acid catalyst); the carbon ends up with two &ndash;OR groups, and H<sub>2</sub>O is released.','5.3']],
6:[['esterification',r=>/acetic acid/.test(r.reactants[0].name)&&r.reactants[1].name==='ethanol','Esterification','Carboxylic acid + alcohol, acid catalyst and heat: a condensation that makes an ester and H<sub>2</sub>O.','6.7'],
   ['esterHydrolysis',r=>/ethyl (ethanoate|acetate)/.test(r.reactants[0].name),'Acid hydrolysis of an ester','Water and acid split the ester back into a carboxylic acid and an alcohol.','6.8'],
   ['saponification',r=>/ethyl (ethanoate|acetate)/.test(r.reactants[0].name),'Saponification','NaOH and heat split the ester into a carboxylate salt and an alcohol.','6.8'],
   ['neutralAcid',nm(/^propanoic acid$/),'Neutralization of a carboxylic acid','A base (NaOH) removes the acidic H: carboxylate ion + water.','6.4']],
7:[['neutralAmine',nm(/^ethylamine$/),'Amine as a base','An amine accepts H<sup>+</sup> from an acid: an ammonium ion (amine salt).','7.3'],
   ['amidation',r=>/acetic acid/.test(r.reactants[0].name)&&r.reactants[1].name==='methylamine','Amidation','Carboxylic acid + amine (or NH<sub>3</sub>) with heat: a condensation that makes an amide and H<sub>2</sub>O.','7.6'],
   ['amideHydrolysis',nm(/acetamide/),'Acid hydrolysis of an amide','Water and acid break the C&ndash;N bond: carboxylic acid + ammonium ion.','7.7'],
   ['amideBase',nm(/./),'Base hydrolysis of an amide','NaOH breaks the C&ndash;N bond: carboxylate salt + amine (or NH<sub>3</sub>).','7.7']]};
const TITLE={2:'Alkanes',3:'Alkenes',4:'Alcohols',5:'Aldehydes and Ketones',6:'Carboxylic Acids and Esters',7:'Amines and Amides'};
const out={};
const row=(x,link)=>`<tr><td><strong>${x[2]}</strong></td><td>${x[3]}</td><td>${link(x[4])}</td></tr>`;
const ex=x=>{const r=S.want(x[0],x[1]);const alt=r.type+': '+r.reactants.filter(p=>p.smi).map(p=>(p.coef>1?p.coef+' ':'')+p.name).join(' + ')+' gives '+r.products.filter(p=>p.smi).map(p=>p.name).join(' + ');return `<p style="margin:.8em 0 .2em"><strong>${x[2]}</strong></p>`+S.scheme(r,alt);};
const sec=n=>`Section ${n}`; // linked in the browser step (ids known there)
for(const ch of Object.keys(ROWS)){
 const R=ROWS[ch];
 out['ch'+ch]=`<div class="mt-section reaction-summary"><h2 class="editable">Reactions at a Glance: ${TITLE[ch]}</h2>
<p>Every reaction in this chapter that you are expected to write. Learn each one as a pattern: what reacts, what is added, what changes.</p>
<table class="mt-responsive-table"><thead><tr><th scope="col">Reaction</th><th scope="col">What happens</th><th scope="col">Taught in</th></tr></thead><tbody>
${R.map(x=>row(x,sec)).join('\n')}
</tbody></table>
<details><summary>Show a drawn example of each reaction</summary><div>
${R.map(ex).join('\n')}
</div></details>
<p style="font-size:0.9em;color:#555;">Reaction examples drawn with the Bond Voyage! engine (ItsDrDan), CC BY-NC-SA 4.0. All the organic reactions in Chapters 2&ndash;7 are combined in the Reaction Roadmap at the end of Chapter 7.</p></div>`;
}
const all=Object.keys(ROWS).flatMap(ch=>ROWS[ch]);
out.roadmap_table=`<table class="mt-responsive-table"><thead><tr><th scope="col">Reaction</th><th scope="col">What happens</th><th scope="col">Taught in</th></tr></thead><tbody>
${all.map(x=>row(x,sec)).join('\n')}
</tbody></table>`;
fs.writeFileSync(__dirname+'/../sections/reactions/reactions.json',JSON.stringify(out));
for(const [k,v] of Object.entries(out)) fs.writeFileSync(__dirname+'/../sections/reactions/'+k+'.html',v);
console.log(Object.keys(out).join(' '), JSON.stringify(out).length);
