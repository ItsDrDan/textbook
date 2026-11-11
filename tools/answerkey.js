/* answerkey.js — print-friendly answers for the LibreTexts PDF (ledger R04).
   Online: every <details><summary>Answer</summary>…</details> stays where it is (click to reveal).
   PDF: those <details> get class "hideprint" (LibreTexts hides it in print) and a copy of every answer is
   appended at the end of the page in <div class="showprint answer-key"> (hidden on screen, shown in print),
   labelled with the box title ("Problem 5.2", "Exercise 4") or, outside a titled box, with the opening words
   of the question. The key is regenerated from the inline answers each run, so the two never drift apart:
   edit the inline answer, re-run, and the printed key follows.
   Usage (Node):  node tools/answerkey.js drafts/*.html      (rewrites files in place)
   Browser:       window.AnswerKey.answerKey(html) -> {html, n, labels}                                      */
(function (root) {
  // The full-book PDF compile does not load LibreTexts' .hideprint/.showprint rules (single-page print does), so each
  // keyed page carries its own print rule. LibreTexts keeps <style> in page bodies (wraps it in CDATA comments).
  const STYLE = '<style type="text/css">@media print { .hideprint, details.hideprint { display: none !important; } } @media screen { .showprint.answer-key { display: none !important; } }</style>\n';
  const stripStyle = b => b.replace(/^<style type="text\/css">(\/\*<!\[CDATA\[\*\/)?@media print \{ (\.hideprint, )?details\.hideprint[\s\S]*?<\/style>\n?/, '');
  function dropKey(b) {
    const s = b.indexOf('<div class="showprint answer-key">'); if (s < 0) return b;
    const re = /<\/?div\b[^>]*>/g; re.lastIndex = s; let d = 0, m;
    while ((m = re.exec(b))) { d += m[0][1] === '/' ? -1 : 1; if (d === 0) return b.slice(0, s).replace(/\n$/, '') + b.slice(m.index + m[0].length); }
    return b;
  }
  function answerKey(body) {
    body = stripStyle(body);
    body = dropKey(body);   // drop an earlier key (only that block: LibreTexts may add wrapper closings after it)
    const items = []; let k = 0;
    const out = body.replace(/<details\b([^>]*)>\s*<summary>Answer<\/summary>([\s\S]*?)<\/details>/g, (m, attrs, content, off) => {
      k++;
      const before = body.slice(Math.max(0, off - 4000), off);
      const bt = [...before.matchAll(/<p class="boxtitle">([\s\S]*?)<\/p>/g)].pop();
      const boxStart = before.lastIndexOf('<div class="box-');
      let label = bt && before.lastIndexOf(bt[0]) >= boxStart ? bt[1].replace(/<[^>]+>/g, '').trim() : '';
      if (!label) {
        const ps = [...before.matchAll(/<(p|li)\b[^>]*>([\s\S]*?)<\/\1>/g)].pop();
        const t = ps ? ps[2].replace(/<[^>]+>/g, '').replace(/\s+/g, ' ').trim() : '';
        const w = t.split(' ');
        label = t ? '&ldquo;' + w.slice(0, 9).join(' ') + (w.length > 9 ? '&hellip;' : '') + '&rdquo;' : 'Question ' + k;
      }
      items.push([label, content.trim()]);
      const cls = /class="/.test(attrs)
        ? attrs.replace(/class="([^"]*)"/, (x, c) => /\bhideprint\b/.test(c) ? x : `class="${c} hideprint"`)
        : attrs + ' class="hideprint"';
      return `<details${cls}><summary>Answer</summary>${content}</details>`;
    });
    // Wrap each answer in <div class="hideprint">: the full-book compile rewrites <details> that sit loose in section text
    // (not inside a problem box) and the class on <details> is lost, so the wrapper is what hides it in print.
    const wrapped = out
      .replace(/<div class="hideprint answer-inline">(<details\b[^>]*\bhideprint\b[^>]*>[\s\S]*?<\/details>)<\/div>/g, '$1')   // unwrap
      .replace(/<details\b[^>]*\bhideprint\b[^>]*>[\s\S]*?<\/details>/g, d => `<div class="hideprint answer-inline">${d}</div>`);
    if (!items.length) return { html: body, n: 0, labels: [] };
    const seen = {}; items.forEach(it => { seen[it[0]] = (seen[it[0]] || 0) + 1; }); const cnt = {};
    const key = '\n<div class="showprint answer-key"><h2>Answers</h2>\n' + items.map(([l, c]) => {
      let lab = l; if (seen[l] > 1) { cnt[l] = (cnt[l] || 0) + 1; lab = l + ' (' + String.fromCharCode(96 + cnt[l]) + ')'; }
      return `<div class="answer-key-item"><p><strong>${lab}</strong></p>${c}</div>`;
    }).join('\n') + '\n</div>\n';
    return { html: STYLE + wrapped.replace(/\s*$/, '') + key, n: items.length, labels: items.map(i => i[0]) };
  }
  const api = { answerKey };
  if (typeof module !== 'undefined' && module.exports) {
    module.exports = api;
    if (require.main === module) {
      const fs = require('fs'); let tot = 0;
      for (const f of process.argv.slice(2)) {
        const s = fs.readFileSync(f, 'utf8'); const r = answerKey(s);
        if (r.n && r.html !== s) { fs.writeFileSync(f, r.html); tot += r.n; console.log(f, r.n); }
      }
      console.log('answers keyed:', tot);
    }
  } else root.AnswerKey = api;
})(typeof window !== 'undefined' ? window : globalThis);
