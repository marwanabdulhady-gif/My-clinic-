const { chromium } = require('playwright');
(async () => {
  const ver = process.argv[2]; const dir = ver === '1.2' ? 's12' : 's2004';
  const b = await chromium.launch(); const p = await (await b.newContext()).newPage();
  await p.goto('http://127.0.0.1:8765/harness.html#' + dir + '/index.html'); await p.waitForTimeout(2500);
  const f = () => p.frames().find(x => x !== p.mainFrame() && x.url().includes('index.html'));
  const cur = () => f().evaluate(() => (document.querySelector('.screen:not([aria-hidden="true"])')||{}).dataset.screenId);
  for (let i = 0; i < 13; i++) {
    const id = await cur();
    await f().evaluate(async (id) => {
      const s = document.querySelector(`.screen[data-screen-id="${id}"]`); const sleep = ms => new Promise(r => setTimeout(r, ms));
      if (id === 'mcs-011') for (const c of s.querySelectorAll('.fc-card, .flashcard, [class*="fc-"] button, .fc')) { c.click(); await sleep(60); }
      if (id === 'mcs-012') { s.querySelector('[data-node="n1"] .scen-choice[data-choice="a"]').click(); await sleep(400);
        s.querySelector('[data-node="n1"] .scen-next').click(); await sleep(400);
        const c2 = s.querySelector('[data-node="n2"] .scen-choice[data-choice="a"]'); if (c2) c2.click(); await sleep(400);
        s.querySelector('[data-node="n2"] .scen-next').click(); await sleep(300); }
      if (id === 'mcs-020') for (const r of s.querySelectorAll('.hotspot-region')) { r.click(); await sleep(60); }
      if (id === 'mcs-022') { const list = s.querySelector('.sorting'); for (const k of ['r','a','c','e']) list.appendChild(list.querySelector(`[data-item="${k}"]`)); s.querySelector('.btn-check').click(); }
      if (id === 'mcs-023') { s.querySelector('.opt[data-opt="a"]').click(); s.querySelector('.btn-check').click(); }
      if (id === 'mcs-031') { const map = {i1:'m1',i2:'m2',i3:'m3',i4:'m4',i5:'m5'};
        for (const [it, tg] of Object.entries(map)) s.querySelector(`.drop-target[data-target="${tg}"] .drop-zone`).appendChild(s.querySelector(`.drag-item[data-item="${it}"]`));
        s.querySelector('.btn-check').click(); }
    }, id);
    await p.waitForTimeout(900);
    await f().evaluate(() => { const n = document.getElementById('btnNext'); n.disabled = false; n.click(); });
    await p.waitForTimeout(900);
  }
  await p.waitForTimeout(2000);
  const shown = await f().evaluate(() => { const e = document.querySelector('.summary-score'); return e ? e.textContent : null; });
  await p.screenshot({ path: `/tmp/claude-0/shots/pass-${ver}.png` });
  await p.evaluate(() => { document.getElementById('c').src = 'about:blank'; }); await p.waitForTimeout(1200);
  const st = JSON.parse(await p.evaluate(() => sessionStorage.getItem('cmi')));
  const pick = Object.fromEntries(Object.entries(st).filter(([k]) => /lesson_status|completion_status|success_status|score\.raw|score\.scaled|objectives\.\d\.(status|success_status)|interactions\.\d+\.(id|result)$/.test(k)));
  console.log(JSON.stringify({ version: ver, summary_score_shown: shown, final: pick }, null, 1));
  await b.close();
})();
