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
          <div v-if="scoreChart" class="score-chart">
            <div class="legend">
              <span v-for="lg in scoreChart.legend" :key="lg.m" class="lg">
                <span class="sw" :style="{ background: lg.color }"></span>{{ lg.m }}
              </span>
              <span class="thesis">L2 = conflict = 论点：模型在此应胜过规则</span>
            </div>
            <svg :viewBox="'0 0 ' + scoreChart.W + ' ' + scoreChart.H" width="100%" role="img"
                 aria-label="phenotype accuracy by signal level, mock vs LLM">
              <line v-for="g in scoreChart.grid" :key="'g'+g.v" :x1="scoreChart.padL" :x2="scoreChart.W"
                    :y1="g.y" :y2="g.y" stroke="var(--border)" stroke-width="1" />
              <text v-for="g in scoreChart.grid" :key="'gt'+g.v" :x="scoreChart.padL - 6" :y="g.y + 3"
                    text-anchor="end" class="ax">{{ g.v.toFixed(1) }}</text>
              <rect v-for="b in scoreChart.bars" :key="b.key" :x="b.x" :y="b.y" :width="b.w" :height="b.h"
                    :fill="b.color" rx="2" />
              <text v-for="b in scoreChart.bars" :key="'t'+b.key" :x="b.lx" :y="b.ly" text-anchor="middle"
                    class="bval">{{ b.label }}</text>
              <text v-for="l in scoreChart.labels" :key="'l'+l.text" :x="l.x" :y="l.y" text-anchor="middle"
                    class="ax">{{ l.text }}</text>
            </svg>
          </div>
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
    },
    scoreChart() {
      const rows = this.scoreRows, modes = this.scoreModes
      if (!rows.length || !modes.length) return null
      const W = 800, H = 196, padL = 34, padB = 30, padT = 16
      const baseY = H - padB, plotH = H - padB - padT
      const groupW = (W - padL) / rows.length
      const barW = Math.min(30, (groupW - 14) / modes.length)
      const palette = { mock: '#8a9099', rules: '#8a9099', llm: 'var(--accent)' }
      const colorFor = (m, i) => palette[m] || (i === 0 ? '#8a9099' : 'var(--accent)')
      const bars = [], labels = []
      rows.forEach((row, gi) => {
        const gx = padL + gi * groupW + (groupW - barW * modes.length) / 2
        modes.forEach((m, mi) => {
          const cell = row[m]
          const mean = cell ? cell.mean : 0
          const h = Math.max(0, mean * plotH)
          const x = gx + mi * barW
          bars.push({ key: row.level + m, x, y: baseY - h, w: Math.max(2, barW - 2), h,
                      color: colorFor(m, mi), label: cell ? mean.toFixed(2) : '',
                      lx: x + (barW - 2) / 2, ly: baseY - h - 3 })
        })
        labels.push({ text: row.level, x: padL + gi * groupW + groupW / 2, y: baseY + 14 })
      })
      const grid = [0, 0.5, 1].map(v => ({ v, y: baseY - v * plotH }))
      const legend = modes.map((m, i) => ({ m, color: colorFor(m, i) }))
      return { W, H, padL, baseY, bars, labels, grid, legend }
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
.score-chart { margin-bottom: 10px; }
.score-chart .legend { display: flex; align-items: center; gap: 14px; font-size: 11px; color: var(--muted); margin-bottom: 4px; }
.score-chart .legend .lg { display: inline-flex; align-items: center; gap: 5px; }
.score-chart .legend .sw { width: 11px; height: 11px; border-radius: 2px; display: inline-block; }
.score-chart .legend .thesis { margin-left: auto; color: #8fe0d0; }
.score-chart .ax { fill: var(--muted); font-size: 11px; font-family: monospace; }
.score-chart .bval { fill: var(--text); font-size: 11px; font-family: monospace; }
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
