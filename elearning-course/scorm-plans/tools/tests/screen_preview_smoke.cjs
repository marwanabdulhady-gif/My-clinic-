// Optional browser gate. Supply Playwright and a Chromium binary; see generator docs.
const assert = require('node:assert/strict');
const { chromium } = require(process.env.PLAYWRIGHT_MODULE || 'playwright');
(async () => {
  const launch = {headless:true};
  if (process.env.CHROMIUM_MODULE) {
    const imported = await import(process.env.CHROMIUM_MODULE);
    const binary = imported.default || imported;
    launch.executablePath = await binary.executablePath(); launch.args = binary.args;
  } else if (process.env.CHROMIUM_EXECUTABLE) launch.executablePath = process.env.CHROMIUM_EXECUTABLE;
  const browser = await chromium.launch(launch);
  try {
    const page = await browser.newPage({viewport:{width:1440,height:1000}});
    const errors = [], failed = [];
    page.on('pageerror', e => errors.push(e.message));
    page.on('response', r => {if (r.status() >= 400) failed.push(r.url());});
    const base = process.env.PREVIEW_URL || 'http://127.0.0.1:8000';
    await page.goto(base);
    const modules = await page.evaluate(() => JSON.parse(document.getElementById('course-data').textContent).modules);
    async function go(mid, sid) {
      await page.evaluate(hash => {location.hash = hash;}, `#${mid}/${sid}`);
      await page.waitForFunction(id => document.getElementById('position').textContent.endsWith(id), sid);
    }
    let count = 0;
    for (const module of modules) for (const screen of module.screens) {
      await go(module.id, screen.id);
      assert(await page.locator('#stage').innerText(), screen.id);
      assert.equal(await page.locator('#screen-name').innerText(), screen.title);
      count++;
    }
    await go('02_health-and-safety-2', 'hs2-030');
    assert.equal(await page.locator('#stage .planned-scene-list .panel').count(), 6, 'Full drill requires six visible scene slots');
    assert.match(await page.locator('#stage').innerText(), /hs2-img-drill-6/);
    await go('08_it-ehr-consultation', 'ehr-031');
    assert.equal(await page.locator('#stage .planned-scene-list .panel').count(), 6, 'Medication simulation requires six capture slots');
    await go('08_it-ehr-consultation', 'ehr-011');
    assert.match(await page.locator('#stage').innerText(), /ehr-shot-form/);
    const hr = '03_hr-employee-induction';
    await go(hr, 'hr-013');
    await page.locator('#stage input[value="0"]').check();
    await page.getByRole('button', {name:'Check draft answer', exact:true}).click();
    assert.match(await page.locator('#stage .feedback').innerText(), /Correct for this draft/);
    await go(hr, 'hr-010');
    await page.getByRole('button', {name:'Caring', exact:true}).click();
    assert.match(await page.locator('#stage .panel').innerText(), /Putting empathy first/);
    await go(hr, 'hr-013');
    assert.equal(await page.locator('#stage input[value="0"]').isChecked(), true, 'Navigation should preserve in-memory choices');
    await go(hr, 'hr-011');
    const expected = ['Responsible','Collaborative','Caring','Ambitious','Collaborative','Responsible'];
    for (let i = 0; i < expected.length; i++) await page.locator('#stage select').nth(i).selectOption(expected[i]);
    await page.getByRole('button', {name:'Check draft answer', exact:true}).click();
    assert.match(await page.locator('#stage .feedback').innerText(), /Correct for this draft/);
    await go(hr, 'hr-052');
    await page.locator('#stage input').fill('731.25');
    await page.getByRole('button', {name:'Check draft answer', exact:true}).click();
    assert.match(await page.locator('#stage .feedback').innerText(), /Correct for this draft/);
    await go('07_quality-safety-and-risk', 'qsr-032');
    assert.equal(await page.locator('#stage .submit').count(), 0, 'Pending risk band must not be graded');
    await go(hr, 'hr-031');
    for (const index of [1, 0, 1]) {
      const choice = page.locator('#stage .scenario-choice').nth(index);
      await choice.focus(); await page.keyboard.press('Enter');
      assert.equal(await page.locator('#stage .scenario-choice:not(:disabled)').count(), 0);
      assert.match(await page.locator('#stage .feedback').innerText(), /Authored draft feedback/);
      const next = page.getByRole('button', {name: /Continue scenario|Review draft outcome/});
      await next.focus(); await page.keyboard.press('Enter');
    }
    assert.match(await page.locator('#stage').innerText(), /Authored branch total: 3/);
    await page.getByRole('button', {name:'Reset draft scenario', exact:true}).click();
    assert.equal(await page.locator('#stage .scenario-choice:not(:disabled)').count(), 3);
    assert.match(await page.locator('#stage').innerText(), /Decision 1/);
    await go('07_quality-safety-and-risk', 'qsr-021');
    await page.locator('#stage .scenario-choice').first().click();
    assert.match(await page.locator('#stage .feedback').innerText(), /PENDING B4/);
    await go(hr, 'hr-061');
    assert.match(await page.locator('#stage').innerText(), /production logic/i);
    await go(hr, 'hr-001');
    await page.setViewportSize({width:390,height:844});
    assert(await page.evaluate(() => document.documentElement.scrollWidth <= window.innerWidth), 'Mobile page must not overflow horizontally');
    await page.locator('#search').fill('no-such-screen');
    assert.match(await page.locator('#outline').innerText(), /No matching screens/);
    assert.deepEqual(errors, []); assert.deepEqual(failed, []);
    console.log(`PASS: ${count} screens, answer checks, tabs, pending keys, navigation state and 390px mobile; no browser errors or missing requests.`);
  } finally {await browser.close();}
})().catch(e => {console.error(e); process.exitCode = 1;});
