/* ---- repair-print: fix R01 (hidden atom labels) and R02 (⯑ charges) on the live LibreTexts book ----
   How to run: sign in to chem.libretexts.org, open any page of the book, open the browser console,
   paste the WHOLE of tools/repair-print.js (printfix + this runner), press Enter.

   Default is a DRY RUN: nothing is changed. It walks every page of the book, checks the page HTML and every
   .svg file attached to the page, prints a table of what it would fix, and downloads a backup JSON of the
   originals of everything it would touch.
   To apply: run   window.REPAIR_APPLY = true   in the console first, then paste the script again.
   Apply also downloads the backup first. Re-running is safe: fixed figures are marked data-printfix="1"
   and skipped, and fixed text has no superscript characters left.
   Only SVG files and page text that actually need the fix are written. Nothing is deleted. */
(async () => {
  const PF = window.PrintFix, ROOT = 488223, APPLY = !!window.REPAIR_APPLY, LIMIT = window.REPAIR_LIMIT || Infinity; // REPAIR_LIMIT = 1 → pilot: write only the first item
  const sleep = ms => new Promise(r => setTimeout(r, ms));
  // LibreTexts throttles bursts (fetch then fails with no response): pause between calls and retry.
  const get = async (url, o) => { for (let k = 0; ; k++) { try { await sleep(150); const r = await fetch(url, o); if (r.status === 429 || r.status >= 500) throw new Error('HTTP ' + r.status); return r; } catch (e) { if (k >= 4) throw e; await sleep(1500 * (k + 1)); } } };
  const api = (p, o) => get('/@api/deki/' + p, Object.assign({ credentials: 'include' }, o || {}));
  const j = async (p) => (await api(p + (p.includes('?') ? '&' : '?') + 'dream.out.format=json')).json();
  const arr = x => [].concat(x || []);
  const me = await j('users/current'); console.log('Signed in as', me.username || me['@id'], APPLY ? '— APPLY MODE' : '— dry run');

  // 1. every page in the book
  const ids = [], seen = new Set();
  async function walk(id) { if (seen.has(id)) return; seen.add(id); ids.push(id);
    for (const s of arr((await j('pages/' + id + '/subpages'))['page.subpage'])) await walk(s['@id']); }
  await walk(ROOT); console.log(ids.length, 'pages in the book');

  const log = [], backup = { taken: new Date().toISOString(), pages: {}, files: {} }, todo = [];
  let n = 0;
  for (const id of ids) {
    n++; if (n % 25 === 0) console.log('scanned', n, '/', ids.length);
    // 2a. page HTML (charges written as ⁺/⁻, and any inline SVG labels)
    // JSON format splits the HTML into an object tree, so read the XML form and take <body> text.
    const xml = await (await api('pages/' + id + '/contents?mode=edit&format=html')).text();
    const bEl = new DOMParser().parseFromString(xml, 'application/xml').querySelector('body');
    const body = bEl ? bEl.textContent : '';
    const a = PF.audit(body);
    if (body && (a.haloLabels || a.superscriptRuns)) {
      const fixed = PF.fixHtml(body);
      backup.pages[id] = body; todo.push({ kind: 'page', id, fixed });
      log.push({ page: id, item: 'page text', haloLabels: a.haloLabels, charges: a.superscriptRuns });
    }
    // 2b. attached SVG figure files
    const files = arr((await j('pages/' + id + '/files'))['file']).filter(f => /\.svg$/i.test(f.filename));
    for (const f of files) {
      // Recently viewed files redirect to a cache the browser blocks; record them and move on (re-run later).
      let src = null; try { const r = await fetch(f.contents['@href'], { credentials: 'include' }); if (r.ok) src = await r.text(); } catch (e) {}
      if (src === null) { log.push({ page: id, item: f.filename, haloLabels: '?', charges: 'UNREADABLE — re-run later' }); continue; }
      const fa = PF.audit(src);
      if (!fa.haloLabels && !fa.superscriptRuns) continue;
      backup.files[id + '/' + f.filename] = src; todo.push({ kind: 'file', id, name: f.filename, fixed: PF.fixSvg(src) });
      log.push({ page: id, item: f.filename, haloLabels: fa.haloLabels, charges: fa.superscriptRuns });
    }
  }
  console.table(log);
  console.log(todo.filter(t => t.kind === 'file').length, 'figure files and', todo.filter(t => t.kind === 'page').length, 'pages need the fix.');

  // 3. backup of the originals (always)
  /* backup: LibreTexts keeps each file's previous revision and page history, so this download is optional */
  const blob = new Blob([JSON.stringify(backup)], { type: 'application/json' }), aEl = document.createElement('a');
  aEl.href = URL.createObjectURL(blob); aEl.download = 'chem3b-print-repair-backup-' + backup.taken.slice(0, 10) + '.json'; aEl.click();
  if (!APPLY) { console.log('Dry run only — nothing changed. Backup downloaded. To apply: window.REPAIR_APPLY = true, then paste again.'); return; }

  // 4. apply
  const res = [];
  for (const t of todo.slice(0, LIMIT)) {
    let r;
    if (t.kind === 'file') r = await api('pages/' + t.id + '/files/=' + encodeURIComponent(t.name), { method: 'PUT', headers: { 'Content-Type': 'image/svg+xml' }, body: t.fixed });
    else r = await api('pages/' + t.id + '/contents?edittime=now', { method: 'POST', headers: { 'Content-Type': 'text/plain; charset=utf-8' }, body: t.fixed });
    res.push({ page: t.id, item: t.kind === 'file' ? t.name : 'page text', status: r.status });
  }
  console.table(res);
  const bad = res.filter(r => !(r.status >= 200 && r.status < 300));
  console.log(bad.length ? bad.length + ' writes FAILED — see table; the backup file has the originals.' : 'All writes OK. Re-export the PDF to check.');
})();
