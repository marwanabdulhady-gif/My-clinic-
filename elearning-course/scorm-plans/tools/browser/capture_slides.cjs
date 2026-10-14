#!/usr/bin/env node
'use strict';
// Actual browser captures, never generated mock pictures. Serve ONLY the generated preview.
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const crypto = require('node:crypto');
const {execFileSync} = require('node:child_process');
const {launchBrowser, repo} = require('./runtime.cjs');

const args = process.argv.slice(2);
const options = {url: 'http://127.0.0.1:8000', out: path.join(repo, '.generated/screens')};
for (let i = 0; i < args.length; i += 2) {
  const key = args[i].replace(/^--/, '');
  if (!['url', 'out'].includes(key) || !args[i + 1]) throw new Error('Usage: capture_slides.cjs [--url URL] [--out .generated/preview]');
  options[key] = args[i + 1];
}
options.out = path.resolve(options.out);
const generated = path.join(repo, '.generated') + path.sep;
if (!options.out.startsWith(generated)) throw new Error('Capture output must be a preview directory under .generated/');
if (!fs.existsSync(path.join(options.out, 'generation-report.json'))) throw new Error('Generate the selected draft batch before capturing it.');
const base = options.url.replace(/\/$/, '');
const hash = value => crypto.createHash('sha256').update(value).digest('hex');
const escape = value => String(value).replace(/[&<>"']/g, ch => ({'&':'&amp;', '<':'&lt;', '>':'&gt;', '"':'&quot;', "'":'&#39;'}[ch]));
const screenshotDir = path.join(options.out, 'review/screens');
fs.mkdirSync(screenshotDir, {recursive: true});

(async () => {
  const browser = await launchBrowser();
  try {
    const page = await browser.newPage({viewport: {width: 1440, height: 1100}, deviceScaleFactor: 1, reducedMotion: 'reduce'});
    const errors = [], failed = [], external = [];
    page.on('pageerror', error => errors.push(error.message));
    page.on('response', response => {if (response.status() >= 400) failed.push(response.url());});
    await page.route('**/*', route => {
      if (new URL(route.request().url()).origin !== new URL(base).origin) {
        external.push(route.request().url()); return route.abort();
      }
      return route.continue();
    });
    await page.goto(base + '/index.html');
    await page.evaluate(() => document.fonts.ready);
    const data = await page.evaluate(() => JSON.parse(document.getElementById('course-data').textContent));
    assert.equal(hash(fs.readFileSync(path.join(options.out, 'index.html'))), hash(await (await page.request.get(base + '/index.html')).body()), 'The served preview must match --out');
    const fonts = await page.evaluate(async () => {
      await document.fonts.load('400 16px Montserrat');
      await document.fonts.load('700 16px Montserrat');
      await document.fonts.load('400 16px Tajawal', 'مرحبا');
      return {montserrat: document.fonts.check('400 16px Montserrat') && document.fonts.check('700 16px Montserrat'),
              tajawal: document.fonts.check('400 16px Tajawal', 'مرحبا')};
    });
    assert(fonts.montserrat && fonts.tajawal, 'Bundled fonts must load');
    const captures = [];
    async function go(module, screen) {
      await page.evaluate(hash => {location.hash = hash;}, `#${module.id}/${screen.id}`);
      await page.waitForFunction(id => document.getElementById('position').textContent.endsWith(id), screen.id);
      await page.evaluate(() => document.fonts.ready);
      await page.locator('#stage img').evaluateAll(images => Promise.all(images.map(image => image.decode())));
      assert.equal(await page.locator('#stage .slide').getAttribute('data-layout'), screen._layout.id);
      assert.equal(await page.locator('#screen-name').innerText(), screen.title);
    }
    async function capture(module, screen, state = 'initial') {
      const filename = screen.id + (state === 'initial' ? '' : '-' + state) + '.png';
      const stage = page.locator('#stage');
      const dimensions = await stage.boundingBox();
      assert.equal(Math.round(dimensions.width), parseInt(data.report.layout_contract.metrics['canvas-width']), 'Canonical desktop width');
      assert(await stage.evaluate(node => node.scrollWidth <= node.clientWidth + 1), `Horizontal slide overflow: ${screen.id}`);
      const file = path.join(screenshotDir, filename);
      await stage.screenshot({path: file, animations: 'disabled'});
      captures.push({module: module.id, screen_id: screen.id, title: screen.title, state,
        layout: screen._layout.id, reference: screen._layout.reference_image, mode: screen._mode,
        width: Math.round(dimensions.width), height: Math.round(dimensions.height),
        full_height: dimensions.height > parseInt(data.report.layout_contract.metrics['canvas-height']) + 1,
        pending_decisions: screen._pending, unresolved_assets: screen._unresolved,
        image: 'review/screens/' + filename, sha256: hash(fs.readFileSync(file))});
    }
    for (const module of data.modules) {
      assert.equal(module.contract.alignment, module.contract.issues.length ? 'review-required' : 'matched', module.id + ' must expose unresolved plan alignment, not pretend approval');
      assert.deepEqual(module.contract.actual, module.contract.expected, module.id + ' immutable count/score/point baseline');
      for (const screen of module.screens) {await go(module, screen); await capture(module, screen);}
    }
    const hr = data.modules.find(m => m.id === '03_hr-employee-induction');
    const qsr = data.modules.find(m => m.id === '07_quality-safety-and-risk');
    if (hr) {
      let screen = hr.screens.find(s => s.id === 'hr-013'); await go(hr, screen);
      const correct = screen.options.findIndex(o => o.correct);
      await page.locator(`#stage input[value="${correct}"]`).check();
      await page.getByRole('button', {name: 'Check draft answer', exact: true}).click();
      assert.match(await page.locator('#stage .feedback').innerText(), /Correct for this draft/);
      const colors = await page.locator('#stage .submit').evaluate(node => ({background:getComputedStyle(node).backgroundColor, foreground:getComputedStyle(node).color}));
      assert.notEqual(colors.background, 'rgb(244, 247, 250)', 'Hover must not make white button text disappear on the pale canvas');
      await capture(hr, screen, 'feedback');
      screen = hr.screens.find(s => s.id === 'hr-010'); await go(hr, screen);
      await page.getByRole('button', {name: 'Caring', exact: true}).click();
      assert.match(await page.locator('#stage .panel').innerText(), /Putting empathy first/);
      await capture(hr, screen, 'caring-tab');
      screen = hr.screens.find(s => s.id === 'hr-031'); await go(hr, screen);
      await page.locator('#stage .scenario-choice').nth(1).click();
      assert.match(await page.locator('#stage .feedback').innerText(), /Authored draft feedback/);
      await capture(hr, screen, 'feedback');
    }
    if (hr) {
      await go(hr, hr.screens.find(s => s.id === 'hr-022'));
      assert.match(await page.locator('#stage').innerText(), /Chief Executive Officer/);
      assert.match(await page.locator('#stage').innerText(), /identifying caption withheld/);
      assert.doesNotMatch(await page.locator('#stage').innerText(), /Abdullah Alghamdi|Richard Thompson/);
      await go(hr, hr.screens.find(s => s.id === 'hr-051'));
      assert.equal(await page.locator('#stage .worked-artifact').count(), 1, 'Authored worked-example artifact must be shown');
    }
    if (qsr) {
      await go(qsr, qsr.screens.find(s => s.id === 'qsr-050'));
      assert.match(await page.locator('#stage').innerText(), /What to report/);
      await go(qsr, qsr.screens.find(s => s.id === 'qsr-091'));
      await page.getByRole('button', {name:'Reflect',exact:true}).click();
      assert.match(await page.locator('#stage .feedback').innerText(), /PENDING NEW-01/);
      const pending = qsr.screens.find(s => s.id === 'qsr-032'); await go(qsr, pending);
      assert.equal(await page.locator('#stage .submit').count(), 0, 'Do not grade the pending risk-band key');
      assert.match(await page.locator('#stage').innerText(), /PENDING B6/);
      const results = qsr.screens.find(s => s.id === 'qsr-090'); await go(qsr, results);
      assert.equal(await page.locator('#stage .empty-score-ring').innerText(), '—\nNOT SCORED');
      const bars = page.locator('#stage .unscored-bar');
      assert.equal(await bars.count(), results.sections.length);
      for (const bar of await bars.all()) assert(await bar.isVisible(), 'Unscored bars must be visible even before advice is expanded');
    }
    // No script, unsupported policy or hidden long content is approved by this smoke gate.
    await page.setViewportSize({width: 390, height: 844});
    let mobileChecks = 0;
    for (const module of data.modules) for (const screen of module.screens) {
      await go(module, screen);
      assert(await page.evaluate(() => document.documentElement.scrollWidth <= window.innerWidth), 'Mobile overflow: ' + screen.id);
      mobileChecks++;
    }
    assert.deepEqual(errors, [], 'Browser errors'); assert.deepEqual(failed, [], 'Missing HTTP assets'); assert.deepEqual(external, [], 'Offline preview must not request external assets');
    const phaseTitle = data.report.phase ? `Phase ${data.report.phase.id} · ${data.report.phase.title}` : 'Current-content draft';
    const featuredIds = qsr && hr ? [
      ['qsr-000', 'initial'], ['qsr-001', 'initial'], ['hr-001', 'initial'], ['hr-013', 'feedback'],
      ['hr-031', 'initial'], ['qsr-090', 'initial'], ['hr-000', 'initial'], ['qsr-040', 'initial'],
    ] : captures.filter(c => c.state === 'initial').slice(0, 8).map(c => [c.screen_id, c.state]);
    const featured = featuredIds.map(([sid, state]) => captures.find(c => c.screen_id === sid && c.state === state));
    const comparisons = featured.map((capture, i) => ({capture, reference: qsr && hr ? data.report.layout_contract.references[i] : data.report.layout_contract.references.find(r => r.image === capture.reference)}));
    const cards = entries => entries.map(c => `<article class="capture-card"><div class="card-label"><span>${escape(c.layout)} / ${escape(c.screen_id)}</span><b>${escape(c.state === 'initial' ? c.mode + ' draft' : c.state)}</b></div><a href="${escape(c.image)}"><img src="${escape(c.image)}" alt="Browser capture of ${escape(c.title)}"></a><h3>${escape(c.title)}</h3><p>${c.width} × ${c.height}${c.full_height ? ' · full-height capture; dense content preserved' : ' · 16:9 canvas'}</p><a class="text-link" href="index.html#${escape(c.module)}/${escape(c.screen_id)}">Open interactive draft →</a></article>`).join('\n');
    const html = `<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>My Clinic · ${escape(phaseTitle)} screenshots</title><link rel="stylesheet" href="style.css"><style>
      body{background:#edf1f5}main.gallery{max-width:1280px;padding:32px 40px}#overview{padding:28px;background:#edf1f5}.gallery-header{display:flex;align-items:center;justify-content:space-between;gap:20px;padding:0 0 20px;border-bottom:1px solid #d9e1e8;margin-bottom:22px}.gallery-header img{width:140px;height:48px;object-fit:contain}.gallery-header small{font-size:10px;letter-spacing:1px;color:#7C0041}.gallery h1{font-size:30px;margin:8px 0}.intro{font-size:13px;color:#5B6B7B;max-width:900px}.gallery-nav{display:flex;flex-wrap:wrap;gap:20px;font-size:12px;margin:20px 0}.featured-grid,.screens-grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:20px}.capture-card{background:white;border:1px solid #d9e1e8;border-radius:8px;overflow:hidden;padding:14px}.card-label{display:flex;justify-content:space-between;gap:10px;font-size:10px;color:#5B6B7B;margin-bottom:10px}.card-label b{color:#652D8C;font-size:9px;text-transform:uppercase}.capture-card img{display:block;width:100%;height:290px;object-fit:contain;background:#f8fafc}.capture-card h3{font-size:16px;margin:12px 0 4px}.capture-card p{font-size:10px;color:#5B6B7B;margin:0 0 8px}.text-link{font-size:10px}.gallery h2{margin-top:34px;font-size:24px}.comparison{padding:18px;border:1px solid #d9e1e8;background:white;margin:18px 0}.comparison h3{margin:0 0 12px;font-size:16px}.comparison-grid{display:grid;grid-template-columns:1fr 1fr;gap:18px}.comparison figure{margin:0}.comparison img{width:100%;height:310px;object-fit:contain;background:#f8fafc}.comparison figcaption{font-size:10px;color:#5B6B7B;margin-bottom:10px}.screens-grid{grid-template-columns:repeat(3,minmax(0,1fr))}.screens-grid img{height:210px}.screens-grid h3{font-size:14px}.review-note{background:white;border-left:4px solid #9D3293;padding:14px 18px;font-size:12px;color:#5B6B7B;margin:20px 0}.gallery footer{padding:20px 0}@media(max-width:700px){main.gallery{padding:18px}#overview{padding:0}.featured-grid,.screens-grid,.comparison-grid{grid-template-columns:1fr}.capture-card img{height:auto}.gallery h1{font-size:26px}}
    </style></head><body><main class="gallery"><section id="overview"><header class="gallery-header"><img src="assets/brand-logo-horizontal-navy.png" alt="My Clinic"><small>INTERNAL REVIEW · KICKOFF DRAFT v0.1 · 14 OCT 2026</small></header><span class="eyebrow">BROWSER-RENDERED SLIDES · CURRENT CONTENT</span><h1>${escape(phaseTitle)}</h1><p class="intro">${data.report.screen_count} slides from the current storyboards, visual/narration plans and required production worksheets. ${captures.length} real browser captures include ${captures.length - data.report.screen_count} interaction states. No SCORM, final audio, policy approval or learner completion is implied.</p><div class="featured-grid">${cards(featured)}</div><div class="review-note">Montserrat is loaded locally. Existing companion art is review resolution (G6 pending). Missing scenes remain placeholders. Policy markers stay visible. Dense screens are captured at full height, not cropped or shrunk to unreadable type. Mockup content, sample answer keys and the sample 86% pass result are never copied.</div></section><nav class="gallery-nav"><a href="index.html">Open slide studio →</a><a href="#comparison">Eight mockup comparisons ↓</a><a href="#all-screens">All slide captures ↓</a><a href="review/capture-report.json">Capture & QA report</a></nav><h2 id="comparison">Reference layouts → current-content draft</h2><p class="intro">The supplied reference PNGs are on the left; actual browser captures are on the right. Geometry comes from mockups.html. This is a review comparison, not pixel-identical content or a claim of visual approval.</p>${comparisons.map(({capture,reference}) => `<section class="comparison"><h3>${escape(path.basename(reference.image, '.png'))} · ${escape(capture.screen_id)}</h3><div class="comparison-grid"><figure><figcaption>SUPPLIED MOCKUP · reference content only</figcaption><img src="${escape(reference.image)}" alt="${escape(reference.id)} supplied layout reference"></figure><figure><figcaption>ACTUAL DRAFT · ${escape(capture.title)} · ${escape(capture.state)}</figcaption><a href="${escape(capture.image)}"><img src="${escape(capture.image)}" alt="Actual browser-rendered draft"></a></figure></div></section>`).join('')}<h2 id="all-screens">All ${data.report.screen_count} slides · original order</h2><div class="screens-grid">${cards(captures.filter(c => c.state === 'initial'))}</div><h2>Additional interaction states</h2><div class="screens-grid">${cards(captures.filter(c => c.state !== 'initial'))}</div><footer>Internal draft · D9 LMS / D10 voices / D11 Marketing and package-specific SME/DPO decisions remain open.</footer></main></body></html>`;
    fs.writeFileSync(path.join(options.out, 'review.html'), html);
    const report = {kind: 'real-browser-draft-captures', production_ready: false,
      phase: data.report.phase, source_commit: execFileSync('git', ['rev-parse', 'HEAD'], {cwd: repo, encoding: 'utf8'}).trim(),
      working_tree_dirty: Boolean(execFileSync('git', ['status', '--porcelain'], {cwd: repo, encoding: 'utf8'}).trim()),
      shared_inputs: data.report.shared_inputs, layout_source: data.report.layout_contract.source,
      font_provenance: data.report.font_provenance,
      browser: browser.version(), viewport: {width:1440, height:1100}, fonts,
      slide_count: data.report.screen_count, capture_count: captures.length, mobile_checks: mobileChecks,
      generation_report_sha256: hash(fs.readFileSync(path.join(options.out, 'generation-report.json'))),
      inputs: data.modules.flatMap(m => m.contract.inputs),
      qa: {browser_errors: errors, failed_requests: failed, external_requests: external,
           desktop_width_matches_mockup: true, mobile_horizontal_overflow: false,
           scope: 'Smoke/geometry/capture verification only; not SME approval, full accessibility, SCORM/LMS, production interaction or delivery QA'},
      captures};
    fs.writeFileSync(path.join(options.out, 'review/capture-report.json'), JSON.stringify(report, null, 2) + '\n');
    await page.setViewportSize({width:1280, height:1100});
    await page.goto(base + '/review.html');
    await page.evaluate(() => document.fonts.ready);
    await page.locator('#overview img').evaluateAll(images => Promise.all(images.map(image => image.decode())));
    await page.locator('#overview').screenshot({path: path.join(options.out, 'review/phase-overview.png'), animations:'disabled'});
    assert.deepEqual(errors, []); assert.deepEqual(failed, []); assert.deepEqual(external, []);
    console.log(`PASS: ${report.slide_count} slides, ${report.capture_count} real PNGs, ${mobileChecks} mobile checks, local fonts, no browser errors/missing/external requests.`);
    console.log('Gallery: ' + path.join(options.out, 'review.html'));
    console.log('Overview: ' + path.join(options.out, 'review/phase-overview.png'));
  } finally {await browser.close();}
})().catch(error => {console.error(error); process.exitCode = 1;});
