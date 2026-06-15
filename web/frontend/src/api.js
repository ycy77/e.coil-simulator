// Thin fetch wrapper around the FastAPI backend.
// All endpoints go through the Vite proxy at /api → 127.0.0.1:28932.

const base = ''

async function request(path, params) {
  let url = base + path
  if (params) {
    const qs = Object.entries(params)
      .filter(([, v]) => v !== undefined && v !== null && v !== '')
      .map(([k, v]) => encodeURIComponent(k) + '=' + encodeURIComponent(v))
      .join('&')
    if (qs) url += '?' + qs
  }
  const response = await fetch(url, {
    headers: { 'Accept': 'application/json' }
  })
  if (!response.ok) {
    let detail = response.statusText
    try {
      const body = await response.json()
      detail = body.detail || detail
    } catch (e) {
      // fall through with statusText
    }
    throw new Error(detail)
  }
  return response.json()
}

async function post(path, body) {
  const response = await fetch(base + path, {
    method: 'POST',
    headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' },
    body: JSON.stringify(body || {})
  })
  if (!response.ok) {
    let detail = response.statusText
    try {
      const b = await response.json()
      detail = b.detail || detail
    } catch (e) { /* keep statusText */ }
    throw new Error(detail)
  }
  return response.json()
}

export const api = {
  health() { return request('/api/health') },
  stats() { return request('/api/stats') },
  perturbagens(limit = 200, search = '') {
    return request('/api/perturbagens', { limit, search })
  },
  searchEntities(query, limit = 20) { return request('/api/entities/search', { q: query, limit }) },
  entityDetail(id) { return request('/api/entities/' + encodeURIComponent(id)) },
  subgraph(id, hops = 1, maxNodes = 200) {
    return request('/api/entities/' + encodeURIComponent(id) + '/subgraph', { hops, max_nodes: maxNodes })
  },
  pathways() { return request('/api/pathways') },
  duplicateNames(minCount = 2, limit = 50) {
    return request('/api/diagnostics/duplicate-names', { min_count: minCount, limit })
  },
  runs() { return request('/api/runs') },
  runMeta(runId) { return request('/api/runs/' + encodeURIComponent(runId)) },
  runTimeline(runId) { return request('/api/runs/' + encodeURIComponent(runId) + '/timeline') },
  runReport(runId) { return request('/api/runs/' + encodeURIComponent(runId) + '/report') },
  runAgent(runId, entityId) {
    return request('/api/runs/' + encodeURIComponent(runId) + '/agents/' + encodeURIComponent(entityId))
  },
  literatureEdges() { return request('/api/literature/edges') },
  kgValidation() { return request('/api/validation/kg') },
  scorecards() { return request('/api/scorecard') },
  scorecard(ts = 'latest') { return request('/api/scorecard/' + encodeURIComponent(ts)) },
  perturbationParse(text, dryRun = false) { return post('/api/perturbation/parse', { text, dry_run: dryRun }) },
  perturbationRun(changes, rounds = 5, useLlm = true) {
    return post('/api/perturbation/run', { changes, rounds, use_llm: useLlm })
  }
}
