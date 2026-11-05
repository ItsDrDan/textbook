// Build "enzyme name hidden" (n) and "enzyme name + coenzymes hidden" (nc) variants of the
// Metabolic Marathon structure close-ups. Usage: node tools/struct_hide.js <metabolism index.html> <out.json>
const fs = require('fs');
const { chromium } = require('playwright');
const src = fs.readFileSync(process.argv[2], 'utf8');
const i = src.indexOf('const RXN_SVG = '), j = src.indexOf('\n', i);
const FIGS = JSON.parse(src.slice(i + 16, j).trim().replace(/;$/, ''));
const CO_FILLS = ['#2c5f9c', '#23704f', '#8a5a00', '#5b4790'];
const CO_WORDS = /NADP?H?\s*(\+\s*H)?[⁺+]?|FADH?₂?2?|ATP|ADP|AMP|CoA–SH|HS–CoA|coenzyme A|PLP/g;

(async () => {
  const b = await chromium.launch();
  const pg = await b.newPage();
  const out = {};
  for (const [key, svg] of Object.entries(FIGS)) {
    await pg.setContent(`<html><body>${svg}</body></html>`);
    const res = await pg.evaluate(({ CO_FILLS }) => {
      const s = document.querySelector('svg');
      // 1. drop the italic enzyme-name caption
      s.querySelectorAll('text[font-style="italic"]').forEach(t => t.remove());
      const n = s.outerHTML;
      // 2. cover coenzyme labels with "?" chips
      const labels = [...s.querySelectorAll('text')].filter(t => CO_FILLS.includes(t.getAttribute('fill')) && t.getAttribute('font-weight') === '800' && t.getAttribute('font-size') === '16');
      const groups = new Map();
      for (const t of labels) { const p = t.parentNode; if (!groups.has(p)) groups.set(p, []); const bb = t.getBBox(); groups.get(p).push({ x: bb.x, y: bb.y, w: bb.width, h: bb.height }); }
      // also pull in phosphate circles / "i" sitting between label pieces on the same line
      let count = 0;
      for (const [p, boxes] of groups) {
        boxes.sort((a, b) => a.x - b.x);
        const merged = [];
        for (const bx of boxes) {
          const last = merged[merged.length - 1];
          if (last && Math.abs((last.y + last.h / 2) - (bx.y + bx.h / 2)) < 10 && bx.x - (last.x + last.w) < 34) { const r = Math.max(last.x + last.w, bx.x + bx.w); last.y = Math.min(last.y, bx.y); last.h = Math.max(last.h, bx.h); last.w = r - last.x; }
          else merged.push({ ...bx });
        }
        for (const m of merged) {
          const pad = 4, x = m.x - pad, y = m.y - pad + 1, w = Math.max(m.w + 2 * pad, 34), h = m.h + 2 * pad - 2;
          const NS = 'http://www.w3.org/2000/svg';
          const r = document.createElementNS(NS, 'rect');
          Object.entries({ x: x.toFixed(1), y: y.toFixed(1), width: w.toFixed(1), height: h.toFixed(1), rx: 7, fill: '#eef1f7', stroke: '#8a93a6', 'stroke-width': 1.5, 'stroke-dasharray': '4 3' }).forEach(([k, v]) => r.setAttribute(k, v));
          const q = document.createElementNS(NS, 'text');
          Object.entries({ x: (x + w / 2).toFixed(1), y: (y + h / 2 + 6).toFixed(1), 'text-anchor': 'middle', 'font-family': 'Nunito,Helvetica,Arial,sans-serif', 'font-size': 17, 'font-weight': 900, fill: '#4a5368' }).forEach(([k, v]) => q.setAttribute(k, v));
          q.textContent = '?';
          p.appendChild(r); p.appendChild(q); count++;
        }
      }
      return { n, nc: s.outerHTML, count };
    }, { CO_FILLS });
    const aria = (svg.match(/aria-label="([^"]*)"/) || [])[1] || '';
    const ariaNc = aria.replace(CO_WORDS, 'a coenzyme').replace(/(a coenzyme)(\s*(→|\+|and)\s*a coenzyme)+/g, '$1') + (res.count ? ' The coenzyme labels on the arrow are hidden.' : '');
    out[key] = { n: res.n, nc: res.count ? res.nc.replace(/aria-label="[^"]*"/, `aria-label="${ariaNc.replace(/"/g, '&quot;')}"`) : '', hid: res.count };
  }
  await b.close();
  fs.writeFileSync(process.argv[3], JSON.stringify(out));
  console.log(Object.keys(out).length, 'figures;', Object.values(out).filter(v => v.hid).length, 'with coenzyme labels hidden');
})();
