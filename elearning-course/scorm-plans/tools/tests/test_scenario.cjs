// Generate screens first, then: node elearning-course/scorm-plans/tools/tests/test_scenario.cjs
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const {create, validate} = require('../screen_generator/scenario.js');
const copy = x => JSON.parse(JSON.stringify(x));
const fixture = {start_node_id:'a', nodes:[
  {id:'a', prompt_html:'First', choices:[
    {id:'left', text_html:'L', score_delta:1, goto_node_id:'b', feedback_html:'L feedback'},
    {id:'end', text_html:'End early', score_delta:-1, goto_node_id:null, feedback_html:'End feedback'}]},
  {id:'b', prompt_html:'Second', choices:[{id:'finish', text_html:'Finish', score_delta:2, goto_node_id:null, feedback_html:'Finish feedback'}]}
]};
const engine = create(fixture);
assert.throws(() => engine.advance(), /feedback/);
assert.throws(() => engine.choose('unknown'), /Unknown/);
assert.equal(engine.choose('left').total, 1);
assert.throws(() => engine.choose('left'), /once/);
assert.equal(engine.advance().node.id, 'b');
assert.equal(engine.choose('finish').total, 3);
assert.equal(engine.advance().finished, true);
assert.throws(() => engine.choose('finish'), /once/);
assert.equal(engine.reset().total, 0);
engine.choose('end'); assert.equal(engine.advance().finished, true);
assert.equal(engine.snapshot().total, -1);
const external = engine.snapshot(); external.trace.push({node_id:'forged'});
assert.equal(engine.snapshot().trace.length, 1, 'Snapshots must be isolated');
for (const mutate of [
  s => {s.start_node_id = 'missing';},
  s => {s.nodes[0].choices[0].goto_node_id = 'missing';},
  s => {s.nodes[1].choices[0].goto_node_id = 'a';},
  s => {s.nodes.push(copy(s.nodes[1]));},
  s => {s.nodes[0].choices.push(copy(s.nodes[0].choices[0]));},
  s => {delete s.nodes[0].choices[0].score_delta;},
  s => {s.nodes[0].choices[0].feedback_html = '';},
  s => {delete s.nodes[0].choices[0].goto_node_id;},
  s => {s.nodes[0].choices[0].goto_node_id = null;}
]) {const bad = copy(fixture); mutate(bad); assert.throws(() => validate(bad));}
const html = fs.readFileSync(path.resolve(__dirname, '../../../../.generated/screens/index.html'), 'utf8');
const data = JSON.parse(html.split('<script id="course-data" type="application/json">')[1].split('</script>')[0]);
const scenarios = data.modules.flatMap(m => m.screens).filter(s => s.type === 'decision_scenario' && s._mode === 'rendered');
assert.equal(scenarios.length, 4);
let paths = 0;
for (const spec of scenarios) {
  function walk(nodeId, chosen, total) {
    const node = spec.nodes.find(n => n.id === nodeId);
    for (const choice of node.choices) {
      const selections = [...chosen, choice.id], sum = total + choice.score_delta;
      if (choice.goto_node_id !== null) walk(choice.goto_node_id, selections, sum);
      else {
        const state = create(spec);
        for (const id of selections) {
          const selected = state.choose(id);
          assert.equal(selected.selected.feedback_html, selected.node.choices.find(c => c.id === id).feedback_html);
          state.advance();
        }
        assert.equal(state.snapshot().finished, true);
        assert.equal(state.snapshot().total, sum);
        assert.equal(state.snapshot().trace.length, selections.length);
        assert.equal(state.reset().trace.length, 0);
        paths++;
      }
    }
  }
  walk(spec.start_node_id, [], 0);
}
console.log(`PASS: scenario state guards, graph validation, reset and ${paths} authored paths across ${scenarios.length} scenarios.`);
