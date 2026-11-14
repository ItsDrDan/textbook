/* Regression check for the Try It widget's spoken structure labels (js/fbx.js).
   node tools/check_struct_labels.js   -> exits 1 if any question has two structure choices with the same label, or a label fails to build. */
const fs = require('fs'), path = require('path'), vm = require('vm');
const root = path.join(__dirname, '..');
const sandbox = { window: {}, document: { addEventListener() {}, querySelector() { return null; }, createElement() { return { style: {}, appendChild() {} }; } }, localStorage: { getItem() { return null; }, setItem() {} }, console };
sandbox.window.document = sandbox.document; sandbox.self = sandbox.window;
vm.createContext(sandbox);
vm.runInContext(fs.readFileSync(path.join(root, 'js/fbx.js'), 'utf8'), sandbox);
const FBX = sandbox.window.FBX || sandbox.FBX;
if (!FBX || !FBX.optLabels) { console.error('FBX.optLabels not found'); process.exit(1); }
let items = 0, dup = 0, bad = 0, mols = 0;
for (const f of fs.readdirSync(path.join(root, 'bank')).filter(f => f.endsWith('.json'))) {
  for (const q of JSON.parse(fs.readFileSync(path.join(root, 'bank', f)))) {
    for (const m of [...(q.cs || []), ...(Array.isArray(q.s) ? q.s : [])]) if (m && m.a) { mols++; const d = FBX.molDesc(m); if (!d || /undefined|NaN/.test(d)) { bad++; console.log('bad label', q.id, d); } }
    if (!q.cs || !q.c.some(c => String(c).startsWith('§'))) continue;
    items++;
    const d = FBX.optLabels(q).filter(x => x !== null);
    if (new Set(d).size < d.length) { dup++; console.log('duplicate labels', q.id); }
  }
}
console.log(`${mols} drawings described; ${items} structure-choice questions; ${dup} with duplicate labels; ${bad} bad labels`);
process.exit(dup || bad ? 1 : 0);
