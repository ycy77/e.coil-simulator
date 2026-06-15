<template>
  <div v-if="visible" class="insights-overlay" @click.self="$emit('close')">
    <div class="insights-modal">
      <header>
        <h3>验证看板 · validation & literature</h3>
        <button class="close" @click="$emit('close')">×</button>
      </header>
      <div class="insights-body">
        <!-- KG validation vs RegulonDB -->
        <section>
          <h4>KG 验证 vs RegulonDB <span v-if="kg && kg.doc" class="doc">{{ kg.doc }}</span></h4>
          <div v-if="kg && kg.available && kg.parsed" class="metric-grid">
            <div v-for="m in kgMetrics" :key="m.key" class="metric">
              <div class="metric-val" :class="{ good: m.key === 'sign_accuracy' && m.pct >= 100 }">
                {{ m.pct }}%
              </div>
              <div class="metric-label">{{ m.label }}</div>
              <div class="metric-frac">{{ m.count }} / {{ m.total }}</div>
            </div>
          </div>
          <p v-else class="muted">无 KG 验证报告(运行 scripts/validate_kg.py 后生成)。</p>
        </section>

        <!-- Phenotype scorecard -->
        <section>
          <h4>表型 scorecard <span v-if="scorecard" class="doc">{{ scorecard.timestamp }} · {{ scorecard.config || '' }}</span></h4>
          <table v-if="scoreRows.length" class="score-table">
            <thead>
              <tr><th>level</th><th v-for="mode in scoreModes" :key="mode">{{ mode }}</th></tr>
            </thead>
            <tbody>
              <tr v-for="row in scoreRows" :key="row.level">
                <td class="lvl">{{ row.level }}</td>
                <td v-for="mode in scoreModes" :key="mode">
                  <span v-if="row[mode]">{{ row[mode].mean.toFixed(2) }} <span class="n">n={{ row[mode].n }}</span></span>
                  <span v-else class="muted">—</span>
                </td>
              </tr>
            </tbody>
          </table>
          <p v-else class="muted">无 scorecard(运行 scripts/score_phenotypes.py 后生成)。</p>
        </section>

        <!-- Literature overlay edges -->
        <section>
          <h4>
            文献接地边 <span v-if="lit && lit.overlap" class="doc">
              novel {{ lit.overlap.novel }} / in-graph {{ lit.overlap.in_base_graph }}
              <span v-if="lit.overlap.unresolved_endpoints"> · 未解析端点 {{ lit.overlap.unresolved_endpoints }}</span>
            </span>
          </h4>
          <div v-if="lit && lit.available && lit.edges.length" class="lit-list">
            <div v-for="(e, idx) in lit.edges" :key="idx" class="lit-row"
                 :class="{ 'in-base': e.in_base_graph }">
              <span class="rel" :data-rel="e.relation_type">{{ e.relation_type }}</span>
              <span class="ep clickable" @click="$emit('select', e.source_id)">{{ e.source_name }}</span>
              <span class="arrow">→</span>
              <span class="ep clickable" @click="$emit('select', e.target_id)">{{ e.target_name }}</span>
              <span class="tag" :class="e.in_base_graph ? 'tag-base' : 'tag-novel'">
                {{ e.in_base_graph ? 'in-graph' : 'novel' }}
              </span>
              <a v-if="e.doi" class="doi" :href="'https://doi.org/' + e.doi" target="_blank" rel="noopener">{{ e.doi }}</a>
              <span class="note" :title="e.notes">{{ e.notes }}</span>
            </div>
          </div>
          <p v-else class="muted">无文献 overlay(data/literature/literature_edges.overlay.csv 缺失)。</p>
        </section>
      </div>
    </div>
  </div>
</template>

<script>
import { api } from '../api.js'

export default {
  name: 'InsightsPanel',
  props: { visible: { type: Boolean, default: false } },
  data() {
    return { kg: null, scorecard: null, lit: null, loaded: false }
  },
  computed: {
    kgMetrics() {
      if (!this.kg || !this.kg.parsed) return []
      const labels = {
        recall: '召回 (graph edge)',
        sign_accuracy: '符号准确率',
        regulators_mappable: '调控子可映射',
        targets_mappable: '靶基因可映射',
        both_mappable: '两端可映射'
      }
      const order = ['recall', 'sign_accuracy', 'regulators_mappable', 'targets_mappable', 'both_mappable']
      return order
        .filter(k => this.kg.parsed[k])
        .map(k => ({ key: k, label: labels[k], ...this.kg.parsed[k] }))
    },
    scoreModes() {
      if (!this.scorecard || !this.scorecard.by_level) return []
      return Object.keys(this.scorecard.by_level)
    },
    scoreRows() {
      if (!this.scorecard || !this.scorecard.by_level) return []
      const levels = new Set()
      for (const mode of this.scoreModes) {
        for (const lvl of Object.keys(this.scorecard.by_level[mode] || {})) levels.add(lvl)
      }
      const sorted = Array.from(levels).sort()
      return sorted.map(level => {
        const row = { level }
        for (const mode of this.scoreModes) {
          const cell = this.scorecard.by_level[mode] && this.scorecard.by_level[mode][level]
          if (cell) row[mode] = { mean: cell.mean_score, n: cell.n }
        }
        return row
      })
    }
  },
  watch: {
    visible(v) {
      if (v && !this.loaded) this.loadAll()
    }
  },
  methods: {
    async loadAll() {
      this.loaded = true
      const [kg, sc, lit] = await Promise.all([
        api.kgValidation().catch(() => null),
        api.scorecard('latest').catch(() => null),
        api.literatureEdges().catch(() => null)
      ])
      this.kg = kg
      this.scorecard = sc
      this.lit = lit
    }
  }
}
</script>

<style scoped>
.insights-overlay {
  position: fixed; inset: 0; background: rgba(0, 0, 0, 0.55);
  display: flex; align-items: center; justify-content: center; z-index: 1000;
}
.insights-modal {
  background: var(--panel); border: 1px solid var(--border); border-radius: 6px;
  width: 860px; max-height: 84vh; display: flex; flex-direction: column;
}
.insights-modal header {
  display: flex; align-items: center; justify-content: space-between;
  padding: 12px 16px; border-bottom: 1px solid var(--border);
}
.insights-modal header h3 { margin: 0; font-size: 14px; }
.insights-modal header .close { background: none; border: none; color: var(--text); font-size: 20px; cursor: pointer; }
.insights-body { overflow-y: auto; padding: 8px 16px 16px; }
section { margin: 14px 0; }
section h4 {
  font-size: 12px; color: var(--muted); text-transform: uppercase;
  letter-spacing: 0.5px; margin: 0 0 8px 0;
}
section h4 .doc { text-transform: none; color: #8fe0d0; font-family: monospace; font-size: 11px; margin-left: 8px; }
.muted { color: var(--muted); font-size: 12px; }
.metric-grid { display: flex; gap: 10px; flex-wrap: wrap; }
.metric {
  background: var(--panel-2); border-radius: 6px; padding: 10px 14px;
  min-width: 120px; text-align: center;
}
.metric-val { font-size: 20px; font-weight: 600; color: var(--accent); }
.metric-val.good { color: #7ad7a3; }
.metric-label { font-size: 11px; color: var(--text); margin-top: 2px; }
.metric-frac { font-size: 10px; color: var(--muted); font-family: monospace; margin-top: 2px; }
.score-table { width: 100%; border-collapse: collapse; font-size: 12px; }
.score-table th, .score-table td { padding: 4px 8px; text-align: left; border-bottom: 1px solid var(--border); }
.score-table th { color: var(--muted); font-weight: 500; }
.score-table .lvl { font-family: monospace; color: var(--accent); }
.score-table .n { color: var(--muted); font-size: 10px; }
.lit-list { display: flex; flex-direction: column; gap: 4px; }
.lit-row {
  display: flex; align-items: center; gap: 8px; padding: 6px 8px;
  background: var(--panel-2); border-radius: 4px; font-size: 12px;
}
.lit-row.in-base { opacity: 0.65; }
.lit-row .rel {
  font-family: monospace; font-size: 10px; padding: 1px 6px; border-radius: 3px;
  background: #3a3a4a; color: var(--muted);
}
.lit-row .rel[data-rel="represses"] { background: #4a3a2a; color: #f0a36b; }
.lit-row .rel[data-rel="activates"] { background: #2a4a3a; color: #7ad7a3; }
.lit-row .ep { color: var(--text); }
.lit-row .ep.clickable { cursor: pointer; }
.lit-row .ep.clickable:hover { color: var(--accent); }
.lit-row .arrow { color: var(--muted); }
.lit-row .tag { font-size: 10px; padding: 1px 6px; border-radius: 3px; }
.lit-row .tag-novel { background: #2a4a3a; color: #7ad7a3; }
.lit-row .tag-base { background: #3a3a4a; color: var(--muted); }
.lit-row .doi { color: #7c9eff; font-family: monospace; font-size: 10px; text-decoration: none; }
.lit-row .doi:hover { text-decoration: underline; }
.lit-row .note {
  color: var(--muted); font-size: 11px; overflow: hidden; text-overflow: ellipsis;
  white-space: nowrap; flex: 1; min-width: 0;
}
</style>
