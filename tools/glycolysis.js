/* Glycolysis figures with structures (intro biochemistry level).
   node tools/glycolysis.js            -> writes figures/pathways/glycolysis/{full-investment,full-payoff,step1..step10}.svg
                                          and figures/pathways/glycolysis/glycolysis_svgs.json (for the games)
   Plain SVG only (no <style>, no <marker>, no ids), so LibreTexts and inline use in games both work.
   Conventions: Haworth rings with H atoms on ring carbons left off; Ⓟ = phosphate group (–PO₃²⁻);
   3-carbon compounds drawn as short vertical chains. Changed groups get a yellow highlight. */
const fs = require('fs'), path = require('path');
const FONT = 'Nunito,Helvetica,Arial,sans-serif', INK = '#2d3f4b', P_FILL = '#ffe1c2', P_STROKE = '#d9822b', HL = '#fff0a8', HL_ST = '#e8c547';
const BLUE = '#2c5f9c', RED = '#9c3346', GREEN = '#23704f', MUTED = '#5a6478';
const r1 = n => Math.round(n * 10) / 10;

/* ---------- text with subscripts, superscripts and Ⓟ ---------- */
// tokens: "_2" subscript digit run, "^-" superscript, "Ⓟ" phosphate
function lex(s) { const out = []; let i = 0;
  while (i < s.length) { const c = s[i];
    if (c === 'Ⓟ') { out.push({ t: 'P' }); i++; continue; }
    if (c === '_') { let j = i + 1; while (j < s.length && /[0-9a-z]/.test(s[j])) j++; out.push({ t: 'sub', v: s.slice(i + 1, j) }); i = j; continue; }
    if (c === '^') { let j = i + 1; while (j < s.length && /[0-9+\-−]/.test(s[j])) j++; out.push({ t: 'sup', v: s.slice(i + 1, j).replace('-', '−') }); i = j; continue; }
    let j = i; while (j < s.length && !'Ⓟ_^'.includes(s[j])) j++; out.push({ t: 'txt', v: s.slice(i, j) }); i = j; }
  return out; }
const CW = { txt: .62, sub: .45, sup: .45 };
const chW = c => /[A-Z]/.test(c) ? (c === 'I' ? .3 : /[MW]/.test(c) ? .86 : .72) : /[a-z]/.test(c) ? (/[il]/.test(c) ? .28 : /[mw]/.test(c) ? .88 : .58) : /[0-9]/.test(c) ? .58 : c === ' ' ? .3 : /[+−–=]/.test(c) ? .6 : .38;
const runW = (v, f) => [...v].reduce((a, c) => a + chW(c) * f, 0);
function textW(s, fs) { return lex(s).reduce((w, k) => w + (k.t === 'P' ? fs * 1.2 : runW(k.v, k.t === 'txt' ? fs : fs * .72)), 0); }
/* first-char width, so a bond can point at the first atom of a label */
function firstW(s, fs) { const k = lex(s)[0]; return k.t === 'P' ? fs * 1.2 : chW(k.v[0]) * fs; }
function label(x, y, s, fs = 16, o = {}) {
  const w = textW(s, fs); let x0 = o.anchor === 'middle' ? x - w / 2 : o.anchor === 'end' ? x - w : x;
  const col = o.color || INK, wt = o.weight || 700; let out = '', run = '', rx = x0;
  const flush = () => { if (run) { out += `<text x="${r1(rx)}" y="${r1(y + fs * .35)}" font-family="${FONT}" font-size="${fs}" font-weight="${wt}" fill="${col}"${o.italic ? ' font-style="italic"' : ''}>${run}</text>`; run = ''; } };
  let cx = x0;
  for (const k of lex(s)) {
    if (k.t === 'P') { flush(); const r = fs * .5; out += `<circle cx="${r1(cx + fs * .62)}" cy="${r1(y)}" r="${r1(r)}" fill="${P_FILL}" stroke="${P_STROKE}" stroke-width="1.6"/><text x="${r1(cx + fs * .62)}" y="${r1(y + fs * .3)}" text-anchor="middle" font-family="${FONT}" font-size="${r1(fs * .78)}" font-weight="900" fill="#8a4a0e">P</text>`; cx += fs * 1.2; rx = cx; continue; }
    if (!run) rx = cx;
    if (k.t === 'txt') run += esc(k.v);
    else run += `<tspan font-size="${r1(fs * .72)}" dy="${k.t === 'sub' ? r1(fs * .28) : r1(-fs * .4)}">${esc(k.v)}</tspan><tspan dy="${k.t === 'sub' ? r1(-fs * .28) : r1(fs * .4)}">&#8203;</tspan>`;
    cx += runW(k.v, k.t === 'txt' ? fs : fs * .72);
  }
  flush(); return { svg: out, x0, x1: x0 + w, w };
}
const esc = s => String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
const line = (x1, y1, x2, y2, w = 2.2, c = INK) => `<line x1="${r1(x1)}" y1="${r1(y1)}" x2="${r1(x2)}" y2="${r1(y2)}" stroke="${c}" stroke-width="${w}" stroke-linecap="round"/>`;
const hlRect = (x, y, w, h) => `<rect x="${r1(x)}" y="${r1(y)}" width="${r1(w)}" height="${r1(h)}" rx="9" fill="${HL}" stroke="${HL_ST}" stroke-width="1.4"/>`;
function dbl(x1, y1, x2, y2, gap = 3.4) { const dx = x2 - x1, dy = y2 - y1, L = Math.hypot(dx, dy), px = -dy / L * gap, py = dx / L * gap; return line(x1 + px, y1 + py, x2 + px, y2 + py) + line(x1 - px, y1 - py, x2 - px, y2 - py); }

/* ---------- molecule drawers: return {svg, w, h} drawn with top-left at (0,0) ---------- */
function shift(m, dx, dy) { return `<g transform="translate(${r1(dx)} ${r1(dy)})">${m.svg}</g>`; }

/* pyranose (glucose): ring with substituents; c6 = label on C5 (up); hl = set of keys to highlight */
function pyranose({ c6 = 'CH_2OH', hl = [] }) {
  const ox = 20, oy = 46; const V = { C5: [ox + 30, oy], O: [ox + 92, oy], C1: [ox + 120, oy + 24], C2: [ox + 92, oy + 48], C3: [ox + 30, oy + 48], C4: [ox + 2, oy + 24] };
  let bg = '', o = '';
  const sub = (C, dir, s, key) => { const [x, y] = V[C], y2 = y + dir * 26, fs = 15; o += line(x, y + dir * 2, x, y2);
    const lab = label(x - firstW(s, fs) / 2, y2 + dir * 10, s, fs); if (hl.includes(key)) bg += hlRect(lab.x0 - 5, y2 + dir * 10 - 12, lab.w + 10, 24); o += lab.svg; };
  const ring = [['C5', 'O'], ['O', 'C1'], ['C1', 'C2'], ['C2', 'C3'], ['C3', 'C4'], ['C4', 'C5']];
  ring.forEach(([a, b]) => { if (a === 'O' || b === 'O') { const [x1, y1] = V[a], [x2, y2] = V[b]; const t = a === 'O' ? [x1 + 9, y1 + 7] : [x1, y1]; const u = b === 'O' ? [x2 - 9, y2] : [x2, y2]; o += line(a === 'O' ? x1 + 7 : x1, a === 'O' ? y1 + 5 : y1, b === 'O' ? x2 - 9 : x2, y2, 2.2); }
    else { const front = ['C1C2', 'C2C3', 'C3C4'].includes(a + b); o += line(...V[a], ...V[b], front ? 5 : 2.2); } });
  o += label(V.O[0], V.O[1], 'O', 16, { anchor: 'middle', color: RED }).svg;
  sub('C5', -1, c6, 'c6'); sub('C1', 1, 'OH', 'c1'); sub('C2', 1, 'OH', 'c2'); sub('C3', -1, 'OH', 'c3'); sub('C4', 1, 'OH', 'c4');
  return { svg: bg + o, w: ox + 150, h: oy + 100 };
}
/* furanose (fructose): c6 on C5 up, c1 on C2 down, OH on C2 up */
function furanose({ c6 = 'CH_2OⓅ', c1 = 'CH_2OH', hl = [] }) {
  const ox = 24, oy = 50; const V = { O: [ox + 70, oy - 2], C2: [ox + 132, oy + 26], C3: [ox + 110, oy + 72], C4: [ox + 32, oy + 72], C5: [ox + 10, oy + 26] };
  let bg = '', o = '';
  const sub = (C, dir, s, key, dx = 0) => { const [x, y] = V[C], y2 = y + dir * (C === 'C3' ? 22 : 26), fs = 15; o += line(x, y + dir * 2, x + dx, y2);
    const lab = s === 'HO' ? label(x + dx + chW('O') * fs / 2, y2 + dir * 10, s, fs, { anchor: 'end' }) : label(x + dx - firstW(s, fs) / 2, y2 + dir * 10, s, fs); if (hl.includes(key)) bg += hlRect(lab.x0 - 5, y2 + dir * 10 - 12, lab.w + 10, 24); o += lab.svg; };
  o += line(V.C5[0], V.C5[1], V.O[0] - 9, V.O[1] + 3) + line(V.O[0] + 9, V.O[1] + 3, V.C2[0], V.C2[1]);
  o += line(...V.C2, ...V.C3, 3.6) + line(...V.C3, ...V.C4, 5) + line(...V.C4, ...V.C5, 3.6);
  o += label(V.O[0], V.O[1], 'O', 16, { anchor: 'middle', color: RED }).svg;
  sub('C5', -1, c6, 'c6'); sub('C2', -1, 'OH', 'c2oh', 18); sub('C2', 1, c1, 'c1', 22); sub('C3', -1, 'HO', 'c3'); sub('C4', 1, 'OH', 'c4');
  return { svg: bg + o, w: ox + 210, h: oy + 122 };
}
/* three-carbon chain drawn vertically. rows: [{c:'C', top:'O'(double up), r:'H', l:'H', rd:'O' (double right), hl:[...keys], dn:true (double bond to next)}]
   or {lab:'CH_2OⓅ'} for a whole-label row */
function chain(rows) {
  const cx = 70, top = rows[0].top ? 44 : 18, gap = 46; let bg = '', o = ''; let minx = 1e9, maxx = -1e9;
  const H = (r) => (r.hl || []);
  rows.forEach((r, i) => { const y = top + i * gap, fs = 16;
    if (i > 0) { const yp = y - gap; if (rows[i - 1].dn) o += dbl(cx, yp + 11, cx, y - 11); else o += line(cx, yp + 11, cx, y - 11); }
    if (r.lab) { const L = label(cx - firstW(r.lab, fs) / 2, y, r.lab, fs); if (H(r).includes('all')) bg += hlRect(L.x0 - 5, y - 13, L.w + 10, 26); o += L.svg; minx = Math.min(minx, L.x0); maxx = Math.max(maxx, L.x1); return; }
    o += label(cx, y, 'C', fs, { anchor: 'middle' }).svg;
    if (r.top) { o += dbl(cx, y - 11, cx, y - 30); const L = label(cx, y - 40, r.top, fs, { anchor: 'middle', color: RED }); if (H(r).includes('top')) bg += hlRect(cx - 12, y - 53, 24, 26); o += L.svg; }
    if (r.r) { o += line(cx + 9, y, cx + 30, y); const L = label(cx + 34, y, r.r, fs, { color: /O/.test(r.r) ? INK : INK }); if (H(r).includes('r')) bg += hlRect(cx + 29, y - 13, L.w + 10, 26); o += L.svg; maxx = Math.max(maxx, L.x1); }
    if (r.rd) { o += dbl(cx + 9, y, cx + 30, y); const L = label(cx + 34, y, r.rd, fs, { color: RED }); if (H(r).includes('rd')) bg += hlRect(cx + 7, y - 13, L.w + 33, 26); o += L.svg; maxx = Math.max(maxx, L.x1); }
    if (r.l) { o += line(cx - 9, y, cx - 30, y); const L = label(cx - 34, y, r.l, fs, { anchor: 'end' }); if (H(r).includes('l')) bg += hlRect(L.x0 - 5, y - 13, L.w + 10, 26); o += L.svg; minx = Math.min(minx, L.x0); }
    if (H(r).includes('c')) bg += hlRect(cx - 12, y - 13, 24, 26);
  });
  return { svg: bg + o, w: 175, h: top + (rows.length - 1) * gap + 22 };
}
/* ---------- the 11 compounds ---------- */
const COO = (hl) => ({ c: 'C', top: 'O', r: 'O^−', hl });
const MOL = {
  glc: { name: 'Glucose', n: '6 C', draw: hl => pyranose({ hl }) },
  g6p: { name: 'Glucose 6-phosphate', draw: hl => pyranose({ c6: 'CH_2OⓅ', hl }) },
  f6p: { name: 'Fructose 6-phosphate', draw: hl => furanose({ c1: 'CH_2OH', hl }) },
  fbp: { name: 'Fructose 1,6-bisphosphate', draw: hl => furanose({ c1: 'CH_2OⓅ', hl }) },
  dhap: { name: 'Dihydroxyacetone phosphate (DHAP)', short: 'DHAP', draw: hl => chain([{ lab: 'CH_2OH', hl: hl.includes('c1') ? ['all'] : [] }, { c: 'C', rd: 'O', hl: hl.includes('co') ? ['rd'] : [] }, { lab: 'CH_2OⓅ' }]) },
  g3p: { name: 'Glyceraldehyde 3-phosphate', draw: hl => chain([{ c: 'C', top: 'O', r: 'H', hl: hl.includes('ald') ? ['top', 'r'] : [] }, { c: 'C', l: 'H', r: 'OH', hl: hl.includes('c2') ? ['r'] : [] }, { lab: 'CH_2OⓅ' }]) },
  bpg: { name: '1,3-Bisphosphoglycerate', draw: hl => chain([{ c: 'C', top: 'O', r: 'OⓅ', hl: hl.includes('c1') ? ['r'] : [] }, { c: 'C', l: 'H', r: 'OH' }, { lab: 'CH_2OⓅ' }]) },
  pg3: { name: '3-Phosphoglycerate', draw: hl => chain([COO(hl.includes('c1') ? ['r'] : []), { c: 'C', l: 'H', r: 'OH', hl: hl.includes('c2') ? ['r'] : [] }, { lab: 'CH_2OⓅ', hl: hl.includes('c3') ? ['all'] : [] }]) },
  pg2: { name: '2-Phosphoglycerate', draw: hl => chain([COO([]), { c: 'C', l: 'H', r: 'OⓅ', hl: hl.includes('c2') ? ['r', 'l'] : [] }, { lab: 'CH_2OH', hl: hl.includes('c3') ? ['all'] : [] }]) },
  pep: { name: 'Phosphoenolpyruvate (PEP)', short: 'PEP', draw: hl => chain([COO([]), { c: 'C', r: 'OⓅ', dn: true, hl: hl.includes('c2') ? ['r'] : [] }, { lab: 'CH_2', hl: hl.includes('c3') ? ['all'] : [] }]) },
  pyr: { name: 'Pyruvate', n: '3 C', draw: hl => chain([COO([]), { c: 'C', rd: 'O', hl: hl.includes('c2') ? ['rd'] : [] }, { lab: 'CH_3', hl: hl.includes('c3') ? ['all'] : [] }]) }
};
/* ---------- steps: reactant(s) → product(s), with side molecules ---------- */
const STEPS = {
  1: { from: ['glc', []], to: [['g6p', ['c6']]], inn: 'ATP', out: 'ADP', enz: 'hexokinase', what: 'A phosphate from ATP is added to carbon 6.' },
  2: { from: ['g6p', []], to: [['f6p', []]], enz: 'phosphoglucose isomerase', what: 'The 6-membered glucose ring becomes a 5-membered fructose ring. Same atoms, rearranged.' },
  3: { from: ['f6p', []], to: [['fbp', ['c1']]], inn: 'ATP', out: 'ADP', enz: 'phosphofructokinase', what: 'A second phosphate from ATP is added, now on carbon 1.' },
  4: { from: ['fbp', []], to: [['dhap', []], ['g3p', []]], enz: 'aldolase', what: 'The 6-carbon sugar splits into two 3-carbon pieces.' },
  5: { from: ['dhap', ['c1', 'co']], to: [['g3p', ['ald', 'c2']]], enz: 'triose phosphate isomerase', what: 'DHAP is rearranged into glyceraldehyde 3-phosphate. Same atoms, rearranged.' },
  6: { from: ['g3p', ['ald']], to: [['bpg', ['c1']]], inn: 'NAD^+', out: 'NADH + H^+', below: 'Ⓟ_i', enz: 'glyceraldehyde 3-phosphate dehydrogenase', what: 'The aldehyde is oxidized (NAD⁺ takes the H) and a phosphate is added.' },
  7: { from: ['bpg', ['c1']], to: [['pg3', ['c1']]], inn: 'ADP', out: 'ATP', enz: 'phosphoglycerate kinase', what: 'The phosphate on carbon 1 is handed to ADP, making ATP.' },
  8: { from: ['pg3', ['c2', 'c3']], to: [['pg2', ['c2', 'c3']]], enz: 'phosphoglycerate mutase', what: 'The phosphate moves from carbon 3 to carbon 2. Same atoms, rearranged.' },
  9: { from: ['pg2', ['c2', 'c3']], to: [['pep', ['c2', 'c3']]], outOnly: 'H_2O', enz: 'enolase', what: 'Water is removed, leaving a C=C double bond.' },
  10: { from: ['pep', ['c2', 'c3']], to: [['pyr', ['c2', 'c3']]], inn: 'ADP', out: 'ATP', enz: 'pyruvate kinase', what: 'The phosphate is handed to ADP, making ATP.' }
};
const COEF = { 6: 2, 7: 2, 8: 2, 9: 2, 10: 2 };
/* arrowhead as a filled path */
const head = (x, y, ang, c = INK, s = 11) => { const a = ang * Math.PI / 180, p = (d, t) => [x + d * Math.cos(a + t), y + d * Math.sin(a + t)]; const [x1, y1] = p(-s, .42), [x2, y2] = p(-s, -.42); return `<path d="M${r1(x)} ${r1(y)}L${r1(x1)} ${r1(y1)}L${r1(x2)} ${r1(y2)}z" fill="${c}"/>`; };
const sideColor = s => /NAD/.test(s) ? BLUE : /ATP|ADP/.test(s) ? '#8a5a00' : /H_2O/.test(s) ? GREEN : '#8a4a0e';

/* horizontal reaction arrow from x0 to x1 at y, with curved arrows above (in → out), optional below-in, or out only */
function hArrow(x0, x1, y, st, opt = {}) {
  let o = line(x0, y, x1 - 4, y, 3.4) + head(x1, y, 0, INK, 14);
  const xm = (x0 + x1) / 2, lift = 46;
  if (st.inn) { const a = xm - 46, b = xm + 46; o += `<path d="M${r1(a)} ${r1(y - lift + 6)} C ${r1(a + 6)} ${r1(y + 12)}, ${r1(b - 6)} ${r1(y + 12)}, ${r1(b)} ${r1(y - lift + 10)}" fill="none" stroke="${MUTED}" stroke-width="2.4"/>` + head(b, y - lift + 6, -62, MUTED, 10);
    o += label(a, y - lift - 6, st.inn, 16, { anchor: 'middle', color: sideColor(st.inn), weight: 800 }).svg + label(b + 4, y - lift - 6, st.out, 16, { anchor: 'middle', color: sideColor(st.out), weight: 800 }).svg; }
  if (st.outOnly) { const b = xm + 44; o += `<path d="M${r1(xm - 10)} ${r1(y - 2)} C ${r1(xm + 4)} ${r1(y - 22)}, ${r1(b - 14)} ${r1(y - lift + 8)}, ${r1(b)} ${r1(y - lift + 8)}" fill="none" stroke="${MUTED}" stroke-width="2.4"/>` + head(b + 2, y - lift + 8, 0, MUTED, 10) + label(b + 8, y - lift + 8, st.outOnly, 16, { color: sideColor(st.outOnly), weight: 800 }).svg; }
  if (st.below) { const a = xm - 58; o += `<path d="M${r1(a)} ${r1(y + 46)} C ${r1(a + 30)} ${r1(y + 46)}, ${r1(xm - 14)} ${r1(y + 30)}, ${r1(xm - 3)} ${r1(y + 6)}" fill="none" stroke="${MUTED}" stroke-width="2.4"/>` + head(xm - 2, y + 3, -70, MUTED, 10) + label(a - 6, y + 46, st.below, 16, { anchor: 'end', color: sideColor(st.below), weight: 800 }).svg; }
  if (opt.enz) o += label(xm, y + (st.below ? 74 : 24), opt.enz, 13, { anchor: 'middle', color: MUTED, weight: 600, italic: true }).svg;
  return o;
}
/* vertical version for the full pathway: arrow from y0 down to y1 at x; side arrows to the right */
function vArrow(x, y0, y1, st, k, coef) {
  let o = line(x, y0, x, y1 - 4, 3) + head(x, y1, 90, INK, 12);
  const ym = (y0 + y1) / 2, c = coef ? coef + ' ' : '';
  o += `<circle cx="${r1(x - 26)}" cy="${r1(ym)}" r="12" fill="#eef2f8" stroke="#9fb0c8" stroke-width="1.4"/>` + label(x - 26, ym, String(k), 13, { anchor: 'middle', color: MUTED, weight: 900 }).svg;
  if (st.inn) { const a = ym - 22, b = ym + 22, rx = x + 46;
    o += `<path d="M${r1(rx)} ${r1(a)} C ${r1(x + 4)} ${r1(a + 6)}, ${r1(x + 4)} ${r1(b - 6)}, ${r1(rx - 4)} ${r1(b)}" fill="none" stroke="${MUTED}" stroke-width="2.2"/>` + head(rx, b + 1, 15, MUTED, 9);
    o += label(rx + 6, a - 2, c + st.inn, 15, { color: sideColor(st.inn), weight: 800 }).svg + label(rx + 6, b + 2, c + st.out, 15, { color: sideColor(st.out), weight: 800 }).svg; }
  if (st.below) o += label(x + 70, ym, '+ ' + (coef ? coef + ' ' : '') + st.below, 15, { color: sideColor(st.below), weight: 800 }).svg;
  if (st.outOnly) { const rx = x + 46; o += `<path d="M${r1(x + 2)} ${r1(ym - 4)} C ${r1(x + 14)} ${r1(ym + 4)}, ${r1(rx - 16)} ${r1(ym + 10)}, ${r1(rx - 2)} ${r1(ym + 10)}" fill="none" stroke="${MUTED}" stroke-width="2.2"/>` + head(rx, ym + 10, 0, MUTED, 9) + label(rx + 6, ym + 10, c + st.outOnly, 15, { color: sideColor(st.outOnly), weight: 800 }).svg; }
  return o;
}
const svgWrap = (w, h, body, aria) => `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 ${Math.ceil(w)} ${Math.ceil(h)}" width="${Math.ceil(w)}" height="${Math.ceil(h)}" style="max-width:100%;height:auto" role="img" aria-label="${esc(aria)}"><rect width="100%" height="100%" fill="#ffffff"/>${body}</svg>`;
const nameText = (x, y, m, fs = 14) => label(x, y, m.name, fs, { anchor: 'middle', weight: 800, color: '#3b4a63' }).svg;
const KEY = (x, y) => label(x, y, 'Ⓟ = phosphate group (–PO_3^2−)', 13, { color: MUTED, weight: 700 }).svg;

/* ---------- close-up of one step ---------- */
function stepSVG(k) {
  const st = STEPS[k], [fid, fhl] = st.from, A = MOL[fid].draw(fhl);
  const prods = st.to.map(([id, hl]) => ({ id, m: MOL[id].draw(hl) }));
  const topPad = 64, arrowW = 190, gapP = 40;
  const H = Math.max(A.h, ...prods.map(p => p.m.h)) + topPad + 70 + (st.below ? 24 : 0);
  let o = '', x = 14; const midY = topPad + Math.max(A.h, ...prods.map(p => p.m.h)) / 2; const nfs = k === 4 ? 12.5 : 14;
  const slot = (m, id) => Math.max(m.w, textW(MOL[id].name, nfs) + 12);
  o += label(14, 22, `Step ${k}`, 18, { weight: 900, color: '#5b4790' }).svg + (COEF[k] ? label(90, 22, '(happens twice per glucose)', 13, { color: MUTED, weight: 600 }).svg : '');
  { const sw = slot(A, fid); o += shift(A, x + (sw - A.w) / 2, midY - A.h / 2); o += nameText(x + sw / 2, midY + A.h / 2 + 14, MOL[fid], nfs); x += sw + 8; }
  o += hArrow(x, x + arrowW, midY, st, { enz: st.enz }); x += arrowW + 14;
  prods.forEach((p, i) => { if (i) { o += label(x - 4, midY, '+', 24, { anchor: 'middle', weight: 800 }).svg; x += 16; }
    const sw = slot(p.m, p.id); o += shift(p.m, x + (sw - p.m.w) / 2, midY - p.m.h / 2) + nameText(x + sw / 2, midY + p.m.h / 2 + 14, MOL[p.id], nfs); x += sw + (i < prods.length - 1 ? gapP : 0); });
  const W = x + 18; o += KEY(14, H - 12);
  return svgWrap(W, H, o, `Glycolysis step ${k}: ${MOL[fid].name} to ${st.to.map(t => MOL[t[0]].name).join(' and ')}. ${st.what}`);
}
/* ---------- full pathway in two panels ---------- */
function stepCircle(x, y, k) { return `<circle cx="${r1(x)}" cy="${r1(y)}" r="12" fill="#eef2f8" stroke="#9fb0c8" stroke-width="1.4"/>` + label(x, y, String(k), 13, { anchor: 'middle', color: MUTED, weight: 900 }).svg; }
const italic = (x, y, t, anchor) => label(x, y, t, 13, { color: MUTED, weight: 700, italic: true, anchor }).svg;
function investSVG() {
  const colX = 30, W = 600; let o = '', y = 58;
  o += label(16, 26, 'Glycolysis, part 1: energy investment (steps 1–5)', 18, { weight: 900, color: '#5b4790' }).svg;
  const ids = ['glc', 'g6p', 'f6p', 'fbp'], AX = colX + 102;
  ids.forEach((id, i) => { const m = MOL[id].draw([]); o += shift(m, colX, y) + label(colX + 250, y + m.h / 2, MOL[id].name, 15, { weight: 800, color: '#3b4a63' }).svg;
    if (i < 3) { const y0 = y + m.h + 10, y1 = y0 + 78; o += vArrow(AX, y0, y1, STEPS[i + 1], i + 1); if (i === 1) o += italic(AX + 16, (y0 + y1) / 2, 'rearranged (isomer)'); y = y1 + 10; } else y += m.h; });
  const sy = y + 10, L = AX;
  o += stepCircle(L - 26, sy + 34, 4) + line(L, sy, L, sy + 28, 3) + line(L, sy + 28, L - 40, sy + 74, 3) + head(L - 44, sy + 79, 131, INK, 12) + line(L, sy + 28, L + 200, sy + 74, 3) + head(L + 206, sy + 75, 13, INK, 12) + italic(L + 22, sy + 18, 'splits into two 3-carbon pieces');
  const d = MOL.dhap.draw([]), g = MOL.g3p.draw([]), by = sy + 86, dx = colX, gx = colX + 250;
  o += shift(d, dx, by + (g.h - d.h)) + label(dx + 70, by + g.h + 18, 'DHAP', 14, { anchor: 'middle', weight: 800, color: '#3b4a63' }).svg;
  o += shift(g, gx, by) + label(gx + 70, by + g.h + 18, 'Glyceraldehyde 3-phosphate', 14, { anchor: 'middle', weight: 800, color: '#3b4a63' }).svg;
  const ay = by + g.h - 46; o += line(dx + 160, ay, gx + 6, ay, 3) + head(gx + 12, ay, 0, INK, 12) + stepCircle((dx + 160 + gx) / 2 + 3, ay - 22, 5) + italic((dx + 160 + gx) / 2 + 3, ay + 20, 'rearranged', 'middle');
  const ry = by + g.h + 48; o += label(W / 2, ry, 'Result: 2 glyceraldehyde 3-phosphate (3 C each) go on to part 2', 14.5, { anchor: 'middle', weight: 900, color: '#5b4790' }).svg;
  const H = ry + 38; o += KEY(16, H - 12);
  return svgWrap(W, H, o, 'Glycolysis part 1, steps 1 to 5 with structures: glucose is phosphorylated by ATP, rearranged to fructose 6-phosphate, phosphorylated again by ATP, split into DHAP and glyceraldehyde 3-phosphate, and DHAP is rearranged into a second glyceraldehyde 3-phosphate.');
}
function payoffSVG() {
  const colX = 30, W = 600; let o = '', y = 66;
  o += label(16, 26, 'Glycolysis, part 2: energy payoff (steps 6–10)', 18, { weight: 900, color: '#5b4790' }).svg;
  o += label(16, 48, 'Each step happens twice per glucose (one for each 3-carbon piece).', 13, { color: MUTED, weight: 700 }).svg;
  const ids = ['g3p', 'bpg', 'pg3', 'pg2', 'pep', 'pyr'], AX = colX + 70;
  ids.forEach((id, i) => { const m = MOL[id].draw([]); o += shift(m, colX, y) + label(colX + 250, y + m.h / 2, MOL[id].name, 15, { weight: 800, color: '#3b4a63' }).svg;
    if (i < 5) { const y0 = y + m.h + 12, y1 = y0 + 80; o += vArrow(AX, y0, y1, STEPS[i + 6], i + 6, 2); if (i === 2) o += italic(AX + 16, (y0 + y1) / 2, 'phosphate moves to carbon 2 (isomer)'); y = y1 + 12 + (MOL[ids[i + 1]].draw([]).h > 0 ? 0 : 0); } else y += m.h; });
  const H = y + 44; o += KEY(16, H - 12);
  return svgWrap(W, H, o, 'Glycolysis part 2, steps 6 to 10 with structures, each happening twice per glucose: glyceraldehyde 3-phosphate is oxidized by NAD+ and gains a phosphate, the phosphate is passed to ADP to make ATP, the phosphate moves from carbon 3 to carbon 2, water is removed to make phosphoenolpyruvate, and its phosphate goes to ADP to make ATP and pyruvate.');
}
module.exports = { stepSVG, investSVG, payoffSVG, STEPS, MOL };
if (require.main === module) {
  const dir = path.join(__dirname, '..', 'figures', 'pathways', 'glycolysis'); fs.mkdirSync(dir, { recursive: true });
  const out = { invest: investSVG(), payoff: payoffSVG() };
  for (let k = 1; k <= 10; k++) out['s' + k] = stepSVG(k);
  for (const [k, v] of Object.entries(out)) fs.writeFileSync(path.join(dir, (k[0] === 's' ? 'step' + k.slice(1) : 'full-' + (k === 'invest' ? 'investment' : 'payoff')) + '.svg'), v);
  fs.writeFileSync(path.join(dir, 'glycolysis_svgs.json'), JSON.stringify(out));
  console.log('wrote', Object.keys(out).length, 'figures; total', Object.values(out).reduce((a, b) => a + b.length, 0), 'bytes');
}
