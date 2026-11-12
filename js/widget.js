/* Textbook "Try it" widget. Two engines:
   1) Exam bank:  practice.html?t=alcohols,carbonyls&n=8      (Final Boss 3B questions, by topic)
                  &fresh=1   new random set each visit, spread evenly across the listed topics (cumulative mixes)
                  practice.html?ids=fb-3B-0019,fb-3B-0020      (hand-picked questions)
                  practice.html?t=hydrocarbons&q=hydrogenation|addition   (regex filter on the question text)
   2) Reaction lab: practice.html?rxn=hydration,hydrohalogenation&mode=product   (generated from Bond Voyage templates)
      modes: identify | product | reactant | name | mix
   Common: &title=...&kicker=...&game=orgrxn|origins|carbs|peptides|finalboss|lewis|flash|lipidlab|enzyme|helix|marathon&key=storage-suffix */
(function(){
"use strict";
const P=new URLSearchParams(location.search);
const $=s=>document.querySelector(s);
/* small helpers kept here so each mode loads only the script it needs: bank mode -> fbx.js, reaction lab -> engine.js */
const esc=s=>String(s).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const shuf=a=>{a=a.slice();for(let i=a.length-1;i>0;i--){const j=Math.floor(Math.random()*(i+1));[a[i],a[j]]=[a[j],a[i]]}return a};
const pick=a=>a[Math.floor(Math.random()*a.length)];
const load=(src,ready)=>ready()?Promise.resolve():new Promise((res,rej)=>{const s=document.createElement('script');s.src=src;s.onload=()=>ready()?res():rej(new Error(src+' did not initialise'));s.onerror=()=>rej(new Error('Could not load '+src));document.head.appendChild(s)});
const loadFail=e=>{console.error(e);$('#host').innerHTML='<div class="rl-card">Sorry, the practice questions could not load. Please refresh the page.</div>'};
let E=null; /* window.ENGINE, set once engine.js has loaded (reaction lab only) */
const GAMES={orgrxn:['Bond Voyage! Organic Reactions','https://itsdrdan.github.io/organicreactions/'],origins:['Organic Origins','https://itsdrdan.github.io/functionalgroups/'],
 carbs:['Sweet Structures','https://itsdrdan.github.io/carbohydrates/'],peptides:['Peptide Party','https://itsdrdan.github.io/aminoacids/'],finalboss:['Final Boss','https://itsdrdan.github.io/finalexam/?course=3B'],
 lewis:['Lewis Structure Studio','https://itsdrdan.github.io/lewisstructures/?course=3B'],flash:['Functional Group Flashcards','https://itsdrdan.github.io/organic/'],hub:['the Study Hub','https://itsdrdan.github.io/games/3b.html'],
 lipidlab:['Lipid Lab','https://itsdrdan.github.io/lipids/'],enzyme:['Enzyme Engine','https://itsdrdan.github.io/enzymes/'],helix:['Helix Hustle','https://itsdrdan.github.io/nucleicacids/'],marathon:['Metabolic Marathon','https://itsdrdan.github.io/metabolism/']};
const TOPICS=[['structure','Structure & Functional Groups','🧩'],['hydrocarbons','Alkanes, Alkenes & Alkynes','⛓️'],['aromatic','Aromatic Compounds','💍'],['isomers','Isomers','🪞'],['chirality','Chirality','🤲'],
 ['properties','IMFs, Polarity & Acid–Base','🧲'],['alcohols','Alcohols, Phenols, Thiols & Ethers','🍷'],['carbonyls','Aldehydes & Ketones','🍋'],['acids_esters','Carboxylic Acids & Esters','🍌'],['amines','Amines & Amides','🐟'],
 ['carbs','Carbohydrates','🍬'],['lipids','Lipids','🫧'],['proteins','Amino Acids & Proteins','🧶'],['enzymes','Enzymes & Vitamins','⚙️'],['nucleic','Nucleic Acids','🧬'],['metabolism','Metabolism','⚡']];
const title=P.get('title'),kicker=P.get('kicker');
if(title)$('#title').textContent=title;if(kicker)$('#kicker').textContent=kicker;
const g=GAMES[P.get('game')];if(g){const a=$('#gameLink');a.href=g[1];a.textContent='Play '+g[0]+' ↗';a.hidden=false}
document.title=(title||'Practice')+' — CHEM 3B';
const track=(mode,topic,correct)=>{try{if(window.ddTrack)ddTrack({game:'textbook',course:'3B',mode,topic,correct:!!correct})}catch(e){}};
const keyFull=P.get('key')||[...P.entries()].filter(([k])=>['t','ids','q','rxn','mode'].includes(k)).map(([k,v])=>k+'='+v).join('&');
const keySuffix=keyFull.slice(0,80); /* kept as before: seeds the stable sample below */
/* storage key: unchanged for suffixes up to 80 chars (keeps saved progress); longer ones get a hash so different widgets no longer collide */
const storeSuffix=keyFull.length<=80?keyFull:keyFull.slice(0,40)+'~'+hash(keyFull).toString(36);

/* ---------- 1) exam bank ---------- */
async function bankMode(){
 const host=$('#host');host.innerHTML='<div class="rl-card">Loading questions…</div>';
 const ids=(P.get('ids')||'').split(',').filter(Boolean);
 let topics=(P.get('t')||'').split(',').filter(Boolean);
 if(!topics.length&&ids.length){/* ids alone: we don't know their topics, so load everything (cached by the browser) */topics=TOPICS.map(t=>t[0])}
 const fbxReady=load('js/fbx.js',()=>window.FBX);
 /* fetch all topic files at once; concatenating in the listed order keeps the result identical to the old one-by-one loop */
 const lists=await Promise.all(topics.map(t=>fetch('bank/'+t+'.json').then(r=>r.ok?r.json():[]).catch(e=>{console.error(e);return []})));
 let items=[].concat(...lists);
 if(ids.length){const want=new Set(ids);items=items.filter(q=>want.has(q.id))}
 const rx=P.get('q');if(rx){let re;try{re=new RegExp(rx,'i')}catch(e){re=null}if(re)items=items.filter(q=>re.test(q.q+' '+q.c.join(' ')+' '+q.w))}
 const dmax=+P.get('dmax');if(dmax)items=items.filter(q=>!q.d||q.d<=dmax);
 const n=+P.get('n');
 if(n&&items.length>n&&P.get('fresh')){/* fresh=1: a new random set on every visit, spread evenly across the listed topics (used by the Cumulative Review mixes) */
  const by={};for(const q of items){(by[q.t]=by[q.t]||[]).push(q)}const keys=shuf(Object.keys(by));for(const k of keys)by[k]=shuf(by[k]);
  const pick=[];let i=0;while(pick.length<n&&keys.some(k=>by[k].length)){const k=keys[i%keys.length];i++;if(by[k].length)pick.push(by[k].shift())}
  items=shuf(pick)}
 else if(n&&items.length>n){/* stable sample so the same widget shows the same set each visit */items=items.map((q,i)=>[q,hash(q.id+keySuffix)]).sort((a,b)=>a[1]-b[1]).slice(0,n).map(a=>a[0])}
 if(!items.length){host.innerHTML='<div class="rl-card">No questions matched this widget. (Check the ?t= / ?ids= settings.)</div>';return}
 try{await fbxReady}catch(e){return loadFail(e)}
 host.innerHTML='';
 window.FBX.mount(host,items,{topics:TOPICS,storageKey:'tb-fbx-'+storeSuffix,onAnswer:(q,first,info)=>track('Try it (bank)',info.topic,first)});
 if(topics.length===1){const s=host.querySelector('.fbx-tsel');if(s)s.hidden=true}
}
function hash(s){let h=2166136261;for(let i=0;i<s.length;i++){h^=s.charCodeAt(i);h=Math.imul(h,16777619)}return h>>>0}

/* ---------- 2) reaction lab ---------- */
function rxnLab(){
 const keys=(P.get('rxn')||'').split(',').filter(k=>E.TPL[k]);
 const modeParam=P.get('mode')||'mix';
 const host=$('#host');
 host.innerHTML=`<div class="rl-card"><div class="rl-top"><div class="rl-pills"><span class="rl-pill ok" id="rlOk" aria-live="polite">✅ 0 / 0 first try</span><span class="rl-pill st" id="rlSt">🔥 Streak 0</span></div><span class="rl-pill" id="rlMode"></span></div>
 <div id="rlRxn"></div><div class="rl-prompt" id="rlPrompt"></div><div id="rlAns"></div>
 <div class="rl-btns"><button class="rl-btn" id="rlCheck">Check</button><button class="rl-btn hint" id="rlHint">💡 Hint</button><button class="rl-btn next" id="rlNext">New Question ▸</button></div>
 <div class="rl-hint" id="rlHintBox" hidden></div><div class="rl-fb" id="rlFb" role="status" aria-live="polite"></div><div class="rl-ref" id="rlRef"></div></div>`;
 const S={n:0,first:0,streak:0,q:null,sel:null,tries:0,done:false,hinted:false};
 const stats=()=>{$('#rlOk').textContent=`✅ ${S.first} / ${S.n} first try`;$('#rlSt').textContent=`🔥 Streak ${S.streak}`};
 const fb=(k,h)=>{const f=$('#rlFb');f.className='rl-fb '+k;f.innerHTML=h};
 const carbons=smi=>E.parseSmi(smi).atoms.filter(a=>a.el==='C').length;
 /* distractor pool: organic molecules from other reactions, preferring the same carbon count */
 function distractors(correct,avoid,wantN){const seen=new Set([correct.name,...avoid.map(p=>p.name)]),same=[],other=[],cn=carbons(correct.smi);
  for(let i=0;i<60&&same.length<wantN+3;i++){const r=E.TPL[pick(Object.keys(E.TPL))]();[...r.reactants,...r.products].filter(p=>p.smi&&!seen.has(p.name)).forEach(p=>{seen.add(p.name);(carbons(p.smi)===cn?same:other).push(p)})}
  return shuf(same).concat(shuf(other)).slice(0,wantN)}
 /* explanation for a wrong structure choice: name it and say why it does not fit */
 function wrongStruct(d,role){return role==='product'
  ?`That structure is <b>${esc(d.name)}</b>. Apply this reaction to the starting materials shown: it does not produce ${esc(d.name)}.`
  :`That structure is <b>${esc(d.name)}</b>. Run this reaction on ${esc(d.name)} and you would not get the product shown.`}
 function newQ(){
  let mode=modeParam==='mix'?pick(['identify','product','name','reactant']):modeParam;
  const ok=r=>mode==='identify'?true:mode==='product'?!!r.draw:mode==='name'?!!r.draw:(r.rev&&!r.rev.alts&&r.rev.idx.length===1);
  let r=E.genRxn(ok,keys);if(!r){mode='identify';r=E.genRxn(null,keys)}
  if(!r){$('#rlPrompt').textContent='No reactions set for this widget (check ?rxn=).';return}
  S.q={r,mode};S.lastWhy='';S.sel=null;S.tries=0;S.done=false;S.hinted=false;$('#rlHintBox').hidden=true;fb('','');$('#rlRef').innerHTML='';$('#rlNext').classList.remove('go');$('#rlCheck').disabled=false;$('#rlHint').disabled=false;
  const ans=$('#rlAns');
  if(mode==='identify'){const mc=E.mcType(r);S.q.mc=mc;$('#rlMode').textContent='Identify the reaction';$('#rlRxn').innerHTML=E.rxnHTML(r,{re:'struct',pr:'struct'});$('#rlPrompt').textContent=mc.prompt;
   S.q.opts=mc.options.map(o=>({html:o.html,ok:o.key===mc.answer,why:o.key===mc.answer||!mc.whyNot?'':mc.whyNot(o.key)}));S.q.hint=mc.hint;S.q.why=mc.why}
  else if(mode==='product'){const i=r.draw[0],p=r.products[i];$('#rlMode').textContent='Predict the product';$('#rlRxn').innerHTML=E.rxnHTML(r,{re:'struct',pr:'hidden'});
   $('#rlPrompt').textContent=(r.draw.length>1?'Which structure is the organic product that replaces the “?” (one of the two organic products)?':'Which structure is the organic product (the “?”)?');
   S.q.opts=shuf([{html:E.structHTML(p.smi),ok:true},...distractors(p,r.products.filter(x=>x.smi),3).map(d=>({html:E.structHTML(d.smi),ok:false,why:wrongStruct(d,'product')}))]);S.q.hint=r.hint;S.q.why=`<b>${esc(p.name)}</b>. ${r.rule}`}
  else if(mode==='reactant'){const i=r.rev.idx[0],p=r.reactants[i];$('#rlMode').textContent='Find the reactant';$('#rlRxn').innerHTML=E.rxnHTML(r,{re:'hidden',pr:'struct',hideIdx:[i]});
   $('#rlPrompt').textContent='Which starting material (the “?”) gives the product shown?';
   S.q.opts=shuf([{html:E.structHTML(p.smi),ok:true},...distractors(p,r.reactants.filter(x=>x.smi),3).map(d=>({html:E.structHTML(d.smi),ok:false,why:wrongStruct(d,'reactant')}))]);S.q.hint=r.hint;S.q.why=`<b>${esc(p.name)}</b>. ${r.rule}`}
  else{const i=pick(r.draw),p=r.products[i];S.q.comp=p;$('#rlMode').textContent='Name the product';$('#rlRxn').innerHTML=E.rxnHTML(r,{re:'bare',pr:'bare'});
   $('#rlPrompt').textContent=`Type the name of the ${r.draw.length>1?E.groupWord(p)+' product':'organic product'}.`;S.q.hint=E.nameHintFor(p);S.q.why=r.rule}
  if(S.q.opts){ans.innerHTML=`<div class="rl-opts">${S.q.opts.map((o,k)=>`<button class="rl-opt" data-k="${k}" aria-pressed="false"><span class="rl-L">${'ABCD'[k]}</span><span class="rl-ot">${o.html}</span></button>`).join('')}</div>`}
  else{ans.innerHTML=`<div class="rl-name"><input id="rlInput" type="text" autocomplete="off" autocapitalize="off" spellcheck="false" placeholder="e.g. 2-propanol" aria-label="Your answer"></div>`;const inp=$('#rlInput');inp.addEventListener('keydown',e=>{if(e.key==='Enter')check()})}
  stats()}
 function finish(solved){const first=solved&&S.tries===0;S.done=true;S.n++;if(first){S.first++;S.streak++}else S.streak=0;
  document.querySelectorAll('.rl-opt').forEach(b=>{b.disabled=true;if(S.q.opts[+b.dataset.k].ok){b.classList.add('right');b.classList.remove('sel')}});
  const ansTxt=S.q.comp?` The name is <b>${esc(S.q.comp.name)}</b>.`:'';
  fb(solved?'good':'info',(first?'✅ <b>Correct!</b> ':solved?'✅ <b>Got it.</b> ':'👀 <b>Here is the answer.</b>'+ansTxt+' '+(S.lastWhy?S.lastWhy+' ':''))+S.q.why);
  $('#rlRef').innerHTML=`<b>Reaction type:</b> ${esc(S.q.r.type)} (${esc(S.q.r.cls.toLowerCase())})`;
  $('#rlCheck').disabled=true;$('#rlHint').disabled=true;$('#rlNext').classList.add('go');stats();track('Try it (reaction lab)',S.q.r.type,first)}
 function check(){if(S.done||!S.q)return;
  if(S.q.opts){if(S.sel==null){fb('bad','👆 Tap an answer first, then press Check.');return}
   if(S.q.opts[S.sel].ok)return finish(true);
   const b=document.querySelector(`.rl-opt[data-k="${S.sel}"]`);b.classList.remove('sel');b.classList.add('wrong');b.disabled=true;S.sel=null;
   const why=S.q.opts[+b.dataset.k].why||'';S.lastWhy=why;
   if(S.tries===0){S.tries=1;fb('bad','🔎 Not quite. '+(why?why+' ':'')+'Try again!'+(S.hinted?'':' Stuck? Tap 💡 Hint.'));return}S.tries=2;return finish(false)}
  const v=$('#rlInput').value,res=E.checkName(v,S.q.comp);
  if(res.ok){if(res.note)$('#rlRef').innerHTML=res.note;return finish(true)}
  if(S.tries===0){S.tries=1;fb('bad','🔎 '+res.msg+' Try once more.');return}S.tries=2;finish(false)}
 host.addEventListener('click',e=>{const o=e.target.closest('.rl-opt');if(o&&!S.done&&!o.disabled){S.sel=+o.dataset.k;document.querySelectorAll('.rl-opt').forEach(x=>{const on=x===o;x.classList.toggle('sel',on);x.setAttribute('aria-pressed',on)});return}
  if(e.target.id==='rlCheck')check();else if(e.target.id==='rlHint'){if(S.done)return;S.hinted=true;const h=$('#rlHintBox');h.innerHTML='💡 '+S.q.hint;h.hidden=false;$('#rlHint').disabled=true}else if(e.target.id==='rlNext')newQ()});
 newQ()}

if(P.get('rxn'))load('js/engine.js',()=>window.ENGINE).then(()=>{E=window.ENGINE;rxnLab()}).catch(loadFail);else bankMode().catch(loadFail);
})();
