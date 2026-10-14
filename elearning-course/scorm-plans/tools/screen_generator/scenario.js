/* Deterministic review-only scenario state. No LMS, persistence or inferred policy. */
(function (root, factory) {
  const api = factory();
  if (typeof module === 'object' && module.exports) module.exports = api;
  else root.MyClinicScenario = api;
})(typeof globalThis !== 'undefined' ? globalThis : this, function () {
  'use strict';
  function validate(spec) {
    if (!Array.isArray(spec.nodes) || !spec.nodes.length) throw new Error('Scenario nodes are required');
    const nodes = new Map();
    for (const node of spec.nodes) {
      if (typeof node.id !== 'string' || !node.id || nodes.has(node.id)) throw new Error('Node IDs must be unique');
      if (typeof node.prompt_html !== 'string' || !node.prompt_html || !Array.isArray(node.choices) || !node.choices.length) throw new Error(`Incomplete node: ${node.id}`);
      const ids = new Set();
      for (const choice of node.choices) {
        if (typeof choice.id !== 'string' || !choice.id || ids.has(choice.id)) throw new Error(`Duplicate or missing choice ID: ${node.id}`);
        ids.add(choice.id);
        if (typeof choice.text_html !== 'string' || !choice.text_html || typeof choice.feedback_html !== 'string' || !choice.feedback_html) throw new Error(`Incomplete choice: ${choice.id}`);
        if (!Number.isFinite(choice.score_delta)) throw new Error(`Missing score delta: ${choice.id}`);
        if (choice.goto_node_id !== null && typeof choice.goto_node_id !== 'string') throw new Error(`Missing branch target: ${choice.id}`);
      }
      nodes.set(node.id, node);
    }
    if (!nodes.has(spec.start_node_id)) throw new Error('Invalid start node');
    for (const node of nodes.values()) for (const choice of node.choices) {
      if (choice.goto_node_id !== null && !nodes.has(choice.goto_node_id)) throw new Error(`Unknown branch target: ${choice.goto_node_id}`);
    }
    // This preview only supports finite acyclic authored scenarios; no inferred retry limits.
    const visiting = new Set(), visited = new Set();
    function visit(id) {
      if (visiting.has(id)) throw new Error('Cyclic scenario requires explicit production retry logic');
      if (visited.has(id)) return;
      visiting.add(id);
      for (const choice of nodes.get(id).choices) if (choice.goto_node_id !== null) visit(choice.goto_node_id);
      visiting.delete(id); visited.add(id);
    }
    visit(spec.start_node_id);
    if (visited.size !== nodes.size) throw new Error('Unreachable scenario nodes');
    return nodes;
  }
  function create(spec) {
    // Keep caller changes and read-only UI snapshots from mutating authored data/state.
    const authored = JSON.parse(JSON.stringify(spec));
    const nodes = validate(authored);
    let current, selected, total, trace, finished;
    const copy = value => JSON.parse(JSON.stringify(value));
    function reset() {current = authored.start_node_id; selected = null; total = 0; trace = []; finished = false; return snapshot();}
    function snapshot() {return copy({node: finished ? null : nodes.get(current), selected, total, trace, finished});}
    function choose(id) {
      if (finished || selected) throw new Error('Choose only once per decision');
      const choice = nodes.get(current).choices.find(c => c.id === id);
      if (!choice) throw new Error('Unknown choice');
      selected = choice; total += choice.score_delta;
      trace.push({node_id: current, choice_id: choice.id, score_delta: choice.score_delta});
      return snapshot();
    }
    function advance() {
      if (finished || !selected) throw new Error('Review choice feedback before continuing');
      if (selected.goto_node_id === null) finished = true;
      else current = selected.goto_node_id;
      selected = null;
      return snapshot();
    }
    reset();
    return {snapshot, choose, advance, reset};
  }
  return {validate, create};
});
