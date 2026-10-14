'use strict';
// Review-only state. Nothing is persisted or sent to an LMS or a remote service.
const DATA = JSON.parse(document.getElementById('course-data').textContent);
const $ = id => document.getElementById(id);
const cache = new Map();
let moduleIndex = 0, screenIndex = 0;
const el = (tag, cls, text) => {const n = document.createElement(tag); if (cls) n.className = cls; if (text !== undefined) n.textContent = text; return n;};
// Only pre-sanitized *_html fields from the generator are inserted as HTML.
const rich = (value, cls = '') => {const n = el('div', cls); n.innerHTML = value || ''; return n;};
const button = (text, fn, cls = '') => {const b = el('button', cls, text); b.type = 'button'; b.addEventListener('click', fn); return b;};
const plainHTML = html => rich(html).textContent;
const assetURL = id => DATA.assets[(id || '').replace(/^<|>$/g, '')];

function media(id, alt) {
  const url = assetURL(id);
  if (url && /\.(png|jpe?g|webp|svg)$/i.test(url)) {
    const img = el('img'); img.src = url; img.alt = alt || ''; return img;
  }
  const box = el('div', 'asset-placeholder');
  box.append(el('strong', '', 'Asset pending'), el('div', '', id || 'No asset assigned'), el('p', '', alt || 'Production visual is not yet supplied.'));
  return box;
}

function feedbackBox() {const box = el('div', 'feedback'); box.setAttribute('role', 'status'); box.hidden = true; return box;}
function feedback(box, screen, correct, custom) {
  box.hidden = false; box.replaceChildren(el('strong', '', correct ? '✓ Correct for this draft' : '↻ Review this choice'));
  box.append(rich(custom || (screen.feedback || {})[correct ? 'correct_html' : 'incorrect_html'] || '<p>No authored feedback supplied.</p>'));
  box.append(el('small', 'result-note', 'Draft answer check only — no completion or LMS score is recorded.'));
}

function choiceQuestion(s) {
  const form = el('form');
  const options = s.type === 'true_false' ? [{id:'true', text_html:'True', correct:s.correct === true}, {id:'false', text_html:'False', correct:s.correct === false}] : s.options || [];
  const multi = s.multi_select || s.multi;
  const field = el('fieldset', 'options'); field.style.border = '0'; field.style.padding = '0';
  const legend = el('legend', 'result-note', s.type === 'poll' ? 'Reflection · unscored' : multi ? 'Select all that apply' : 'Choose one answer');
  field.append(legend);
  options.forEach((o, i) => {
    const label = el('label', 'option'); const input = el('input'); input.type = multi ? 'checkbox' : 'radio'; input.name = s.id; input.value = String(i);
    label.append(input, rich(o.text_html)); field.append(label);
  });
  form.append(field);
  if (s.allow_text) {const label = el('label', '', 'Optional reflection'); const text = el('textarea'); text.setAttribute('aria-label', 'Optional reflection'); label.append(text); form.append(label);}
  const box = feedbackBox(); const submit = el('button', 'submit', s.type === 'poll' ? 'Reflect' : 'Check draft answer'); submit.type = 'submit';
  form.append(submit, box);
  form.addEventListener('submit', event => {
    event.preventDefault(); const chosen = [...field.querySelectorAll('input:checked')].map(i => Number(i.value));
    if (!chosen.length) {box.hidden = false; box.textContent = 'Choose an option first.'; return;}
    if (s.type === 'poll') {box.hidden = false; box.replaceChildren(rich(s.reflection_html || '<p>Reflection selected. This poll is unscored.</p>')); return;}
    const correct = options.every((o, i) => Boolean(o.correct) === chosen.includes(i));
    const custom = chosen.length === 1 ? options[chosen[0]].feedback_html : null;
    feedback(box, s, correct, custom);
  });
  return form;
}

function pairedQuestion(s) {
  const form = el('form'); const rows = s.type === 'matching' ? s.pairs : s.items;
  const choices = s.type === 'matching' ? [...new Set(s.pairs.map(p => p.right_html))].sort().map(text => ({id:text, label_html:text})) : s.targets;
  const controls = [];
  rows.forEach((item, i) => {
    const row = el('div', 'answer-row'); const label = el('label'); label.htmlFor = `answer-${s.id}-${i}`; label.append(rich(item.left_html || item.text_html));
    const select = el('select'); select.id = label.htmlFor;
    const placeholder = el('option', '', 'Choose a match'); placeholder.value = ''; select.append(placeholder);
    choices.forEach(c => {const option = el('option', '', plainHTML(c.label_html)); option.value = c.id; select.append(option);});
    row.append(label, select); form.append(row); controls.push(select);
  });
  const box = feedbackBox(); const submit = el('button', 'submit', 'Check draft answer'); submit.type = 'submit'; form.append(submit, box);
  form.addEventListener('submit', event => {
    event.preventDefault(); if (controls.some(c => !c.value)) {box.hidden = false; box.textContent = 'Complete every match first.'; return;}
    feedback(box, s, rows.every((r, i) => controls[i].value === (s.type === 'matching' ? r.right_html : r.correct_target_id)));
  });
  return form;
}

function fillQuestion(s) {
  const form = el('form'); const controls = [];
  s.blanks.forEach(b => {const label = el('label', 'answer-row'); label.append(el('span', '', `Answer · ${b.id}`)); const input = el('input'); input.type = 'text'; input.autocomplete = 'off'; label.append(input); controls.push(input); form.append(label);});
  const box = feedbackBox(); const submit = el('button', 'submit', 'Check draft answer'); submit.type = 'submit'; form.append(submit, box);
  form.addEventListener('submit', event => {
    event.preventDefault(); const norm = value => s.case_sensitive ? value.trim() : value.trim().toLowerCase();
    if (controls.some(c => !c.value.trim())) {box.hidden = false; box.textContent = 'Complete every answer first.'; return;}
    feedback(box, s, s.blanks.every((b, i) => b.accepted.some(a => norm(String(a)) === norm(controls[i].value))));
  });
  return form;
}

function decisionScenario(s) {
  const root = el('div', 'scenario-player');
  let engine;
  try {engine = MyClinicScenario.create(s);} catch (error) {
    root.append(el('div', 'review-only', 'Scenario wiring pending: ' + error.message), reviewContent(s));
    return root;
  }
  const banner = el('div', 'review-only', 'Fictional draft scenario · policies and answer keys still require SME approval. No LMS score or pass is recorded.');
  const content = el('div'); root.append(banner, content);
  function draw(focus = false) {
    const state = engine.snapshot(); content.replaceChildren();
    const heading = el('h3', '', state.finished ? 'Draft scenario review complete' : `Decision ${state.trace.length + (state.selected ? 0 : 1)} · ${state.node.id}`);
    heading.tabIndex = -1; content.append(heading);
    if (state.finished) {
      content.append(el('p', 'result-note', `Authored branch total: ${state.total}${Number.isFinite(s.pass_score) ? ' · authored scenario threshold: ' + s.pass_score : ''}. This is not a course score or approval.`));
      const log = el('ol'); state.trace.forEach(t => log.append(el('li', '', `${t.node_id} → ${t.choice_id} · authored delta ${t.score_delta}`))); content.append(log);
      content.append(button('Reset draft scenario', () => {engine.reset(); draw(true);}));
    } else {
      content.append(rich(state.node.prompt_html, 'prompt'));
      if (state.node.image_asset_id) {const scene = el('div', 'scenario-scene'); scene.append(media(state.node.image_asset_id, state.node.image_alt)); content.append(scene);}
      const choices = el('div', 'options');
      state.node.choices.forEach(choice => {
        const b = button('', () => {engine.choose(choice.id); draw(true);}, 'scenario-choice');
        b.append(rich(choice.text_html)); b.disabled = Boolean(state.selected);
        if (state.selected && state.selected.id === choice.id) b.setAttribute('aria-pressed', 'true');
        choices.append(b);
      }); content.append(choices);
      if (state.selected) {
        const box = feedbackBox(); box.hidden = false;
        box.append(el('strong', '', 'Authored draft feedback'), rich(state.selected.feedback_html));
        content.append(box, button(state.selected.goto_node_id === null ? 'Review draft outcome' : 'Continue scenario', () => {engine.advance(); draw(true);}, 'submit'));
      }
      content.append(button('Reset draft scenario', () => {engine.reset(); draw(true);}, 'scenario-reset'));
    }
    if (focus) heading.focus();
  }
  draw(); return root;
}

function panel(item) {
  const box = el('div', 'panel');
  if (item.image_asset_id) box.append(media(item.image_asset_id, item.image_alt));
  box.append(rich(item.body_html)); return box;
}

function tabs(s) {
  const root = el('div'); const row = el('div', 'tabs-row'); const content = el('div');
  const buttons = s.tabs.map((tab, i) => button(tab.label, () => activate(i)));
  function activate(i) {buttons.forEach((b, j) => b.setAttribute('aria-pressed', String(i === j))); content.replaceChildren(panel(s.tabs[i]));}
  row.append(...buttons); root.append(row, content); activate(0); return root;
}

function accordion(s) {
  const root = el('div'); s.items.forEach(item => {const d = el('details', 'accordion-item'); d.append(el('summary', '', item.title), panel(item)); root.append(d);}); return root;
}

function flashcards(s) {
  const root = el('div', 'card-grid'); s.cards.forEach(c => {
    let back = false; const b = button('', () => {back = !back; update();}, 'flashcard');
    function update() {b.setAttribute('aria-pressed', String(back)); b.replaceChildren(el('small', '', back ? 'BACK · select to return' : 'FRONT · select to reveal'), rich(back ? c.back_html : c.front_html));}
    update(); root.append(b);
  }); return root;
}

// Complex production interactions are shown as structured authored content, never
// silently replaced with an invented working assessment or inferred answer key.
function reviewContent(s) {
  const root = el('div'); root.append(el('div', 'review-only', 'Interaction storyboard preview — production logic, scoring and media alignment are not implemented.'));
  function itemCard(item, index) {
    const box = el('div', 'step');
    box.append(el('h3', '', item.title || item.id || `Step ${index + 1}`));
    for (const key of ['prompt_html', 'instruction_html', 'action_html', 'text_html', 'label_html', 'body_html', 'rationale_html', 'hint_html', 'explain_html', 'scaffold_html']) if (item[key]) box.append(rich(item[key]));
    if (item.image_asset_id) box.append(media(item.image_asset_id, item.image_alt));
    for (const key of ['choices', 'options', 'regions']) {
      if (Array.isArray(item[key])) {
        const list = el('ul'); item[key].forEach(c => {const li = el('li'); li.append(rich(c.text_html || c.label_html || c.id)); if (c.feedback_html) {const d = el('details'); d.append(el('summary', '', 'Authored feedback'), rich(c.feedback_html)); li.append(d);} list.append(li);}); box.append(list);
      }
    }
    return box;
  }
  for (const key of ['nodes', 'steps', 'items', 'regions', 'labels', 'rounds']) {
    if (Array.isArray(s[key])) s[key].forEach((item, i) => root.append(itemCard(item, i)));
  }
  if (s.image_asset_id) root.append(media(s.image_asset_id, s.image_alt));
  if (root.children.length === 1) root.append(el('p', '', s._brief || 'No production interaction detail supplied. Review the source JSON below.'));
  return root;
}

function screenContent(s) {
  const body = el('div');
  if (s.prompt_html || s.intro_html) body.append(rich(s.prompt_html || s.intro_html, 'prompt'));
  if (s._mode === 'brief') {
    body.append(el('div', 'review-only', 'Build detail pending — this is an authored visual brief, not a functional interaction.'));
    if (s.body_html) body.append(rich(s.body_html, 'content'));
    body.append(el('div', 'brief', s._brief || 'No on-screen content supplied.'));
    return body;
  }
  switch (s.type) {
    case 'content_slide': case 'summary': {
      const content = rich(s.body_html, 'content'); const id = s.media_asset_id || s.image_asset_id;
      if (id) {const layout = el('div', 'media-layout'); const image = el('div', 'media'); image.append(media(id, s.media_alt || s.image_alt)); layout.append(content, image); body.append(layout);} else body.append(content);
      break;
    }
    case 'mcq': case 'true_false': case 'poll': body.append(choiceQuestion(s)); break;
    case 'matching': case 'drag_drop': body.append(pairedQuestion(s)); break;
    case 'fill_blank': body.append(fillQuestion(s)); break;
    case 'decision_scenario': body.append(decisionScenario(s)); break;
    case 'tabs': body.append(tabs(s)); break;
    case 'accordion': body.append(accordion(s)); break;
    case 'flashcards': body.append(flashcards(s)); break;
    case 'timeline': s.events.forEach(e => {const box = el('div', 'timeline-event'); box.append(el('small', '', e.date), el('h3', '', e.title), rich(e.body_html)); body.append(box);}); break;
    case 'worked_example':
      s.steps.forEach((step, i) => {const box = el('div', 'step'); box.append(el('small', 'eyebrow', `STEP ${i + 1}`), rich(step.action_html)); const d = el('details'); d.append(el('summary', '', 'Why this step?'), rich(step.rationale_html)); box.append(d); body.append(box);});
      if (s.self_explanation_prompt_html) {body.append(rich(s.self_explanation_prompt_html)); const text = el('textarea'); text.setAttribute('aria-label', 'Unscored reflection'); body.append(text);} break;
    case 'results_breakdown':
      body.append(el('div', 'review-only', 'Results layout only. This preview does not calculate a course score or grant a pass.'), rich(s.body_html));
      s.sections.forEach(section => {const d = el('details', 'accordion-item'); d.append(el('summary', '', section.title), el('p', 'result-note', `Evidence: ${(section.screen_ids || []).join(', ')}`), rich(section.advice_html)); body.append(d);}); break;
    default: body.append(reviewContent(s));
  }
  return body;
}

function buildScreen(m, s) {
  if (s.type === 'title_slide') {
    const title = el('div', 'title-screen'); const logo = el('img', 'logo'); logo.src = assetURL('brand-logo-horizontal-white'); logo.alt = 'My Clinic';
    title.append(logo, el('span', 'module-chip', m.id.slice(0, 2) + ' · ' + (s.section || 'Welcome')), el('h2', '', s.title));
    title.append(el('p', 'subtitle', s.subtitle || s._brief || ''));
    title.append(el('p', 'tagline', DATA.brand.logo.tagline)); return title;
  }
  const root = el('div'); const header = el('div', 'screen-header'); const logo = el('img'); logo.src = assetURL('brand-logo-horizontal-navy'); logo.alt = 'My Clinic';
  header.append(logo, el('span', '', s.section || ''));
  const content = el('div', 'screen-body'); content.append(el('h2', '', s.title), screenContent(s));
  const foot = el('div', 'screen-footer'); foot.append(el('span', '', DATA.brand.logo.tagline), el('span', '', s.id)); root.append(header, content, foot); return root;
}

function outline() {
  const m = DATA.modules[moduleIndex]; const query = $('search').value.toLowerCase(); const nav = $('outline'); nav.replaceChildren(); let section = null;
  m.screens.forEach((s, i) => {
    if (!`${s.id} ${s.title}`.toLowerCase().includes(query)) return;
    if (s.section !== section) {section = s.section; nav.append(el('div', 'section-label', section || 'Screens'));}
    const b = button('', () => navigate(moduleIndex, i), 'screen-link');
    b.append(el('span', '', s.title), el('small', '', `${s.id} · ${s.type}${s.points ? ' · scored draft' : ''}`));
    if (i === screenIndex) b.setAttribute('aria-current', 'page'); nav.append(b);
  });
  if (!nav.children.length) nav.append(el('p', '', 'No matching screens.'));
}

function render() {
  const m = DATA.modules[moduleIndex], s = m.screens[screenIndex];
  document.documentElement.style.setProperty('--secondary', m.color);
  $('module').value = String(moduleIndex); $('module-name').textContent = m.title; $('screen-name').textContent = s.title;
  $('mode').textContent = ({rendered:'RENDERED DRAFT', brief:'BUILD DETAIL PENDING', review:'INTERACTION REVIEW'})[s._mode];
  const key = `${m.id}/${s.id}`; if (!cache.has(key)) cache.set(key, buildScreen(m, s));
  $('stage').replaceChildren(cache.get(key));
  $('position').textContent = `${screenIndex + 1} / ${m.screens.length} · ${s.id}`;
  $('prev').disabled = screenIndex === 0; $('next').disabled = screenIndex === m.screens.length - 1;
  const warnings = [];
  if (s._missing.length) warnings.push('Missing build fields: ' + s._missing.join(', '));
  if (s._unresolved.length) warnings.push('Assets pending: ' + s._unresolved.join(', '));
  if (s.notes && /char-/.test(s.notes)) warnings.push('Companion placement remains in authoring notes; full-size approved art/layout not yet wired.');
  $('warnings').textContent = warnings.join('\n');
  $('transcript').textContent = s.narration_text || 'No narration supplied.';
  $('audio').replaceChildren(); const url = assetURL(s.narration_asset_id);
  if (url && /\.(mp3|wav|ogg)$/i.test(url)) {const a = el('audio'); a.controls = true; a.preload = 'none'; a.src = url; $('audio').append(a);}
  $('metadata').textContent = `${m.source}\nScreen: ${s.id} · Type: ${s.type} · Planned points: ${s.points || 0}\nObjectives: ${(s.objective_ids || []).join(', ') || 'none'}\nEvidence: ${(s.evidence_screen_ids || []).join(', ') || 'none'}\n${s.notes || ''}`;
  $('visual').textContent = s._visual;
  $('spec').textContent = JSON.stringify(Object.fromEntries(Object.entries(s).filter(([key]) => !key.startsWith('_'))), null, 2);
  document.title = `${s.id} · My Clinic screen review`; outline();
}

function navigate(mi, si) {
  moduleIndex = mi; screenIndex = si;
  const hash = '#' + DATA.modules[mi].id + '/' + DATA.modules[mi].screens[si].id;
  // Replace avoids duplicating course-navigation state in browser history.
  if (location.hash !== hash) {location.hash = hash;} else render();
}
function route() {
  const [mid, sid] = location.hash.slice(1).split('/');
  const mi = DATA.modules.findIndex(m => m.id === mid);
  moduleIndex = mi >= 0 ? mi : 0;
  const si = DATA.modules[moduleIndex].screens.findIndex(s => s.id === sid); screenIndex = si >= 0 ? si : 0;
  render();
}
DATA.modules.forEach((m, i) => {const o = el('option', '', m.title); o.value = String(i); $('module').append(o);});
$('module').addEventListener('change', () => {$('search').value = ''; navigate(Number($('module').value), 0);});
$('search').addEventListener('input', outline);
$('prev').addEventListener('click', () => navigate(moduleIndex, Math.max(0, screenIndex - 1)));
$('next').addEventListener('click', () => navigate(moduleIndex, Math.min(DATA.modules[moduleIndex].screens.length - 1, screenIndex + 1)));
window.addEventListener('hashchange', () => {document.querySelectorAll('audio').forEach(a => a.pause()); route();});
route();
