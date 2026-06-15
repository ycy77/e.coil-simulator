<template>
  <div class="timeline">
    <div class="toolbar">
      <span class="label">Run:</span>
      <select v-model="selectedRunId" @change="selectRun">
        <option value="">— 选一个 run —</option>
        <option v-for="run in runs" :key="run.run_id" :value="run.run_id">
          {{ run.run_id }} ({{ run.round_count }} 轮, {{ run.perturbations.length }} 扰动)
        </option>
      </select>
      <span v-if="timeline.length" class="meta">
        共 {{ timeline.length }} 轮,
        合计变化 {{ totalChanges }} 个 agent
      </span>
    </div>
    <div v-if="feedback" class="feedback-banner">
      <span class="fb-icon">↺</span>
      <span v-if="feedback.closed.length">
        反馈闭合：级联绕回了被扰动的
        <code v-for="(id, i) in feedback.closed" :key="id" class="fb-node" @click="selectEntity(id)">{{ id }}</code>
      </span>
      <span v-else>检测到 {{ feedback.reactivated }} 个节点多轮重复激活（震荡/反馈）</span>
    </div>
    <div class="chart">
      <div v-for="(point, idx) in timeline" :key="idx"
           class="point"
           :class="{ selected: selectedRound === point.round }"
           :title="`round ${point.round} · 候选 ${point.candidate_agents} · 变化 ${point.new_changed_agents}`"
           @click="toggleRound(point)">
        <div class="bar" :style="{ height: barHeight(point) + 'px' }"></div>
        <span class="round-label">R{{ point.round }}</span>
        <span class="change">{{ point.new_changed_agents }}</span>
      </div>
    </div>
    <div v-if="selectedRoundData" class="round-detail">
      <h4>Round {{ selectedRoundData.round }} · 变化 {{ selectedRoundData.new_changed_agents }} 个</h4>
      <ul>
        <li v-for="change in selectedRoundData.new_changes.slice(0, 12)" :key="change.entity_id">
          <code>{{ change.entity_id }}</code>:
          <code>{{ change.state }}</code>
          <span v-if="change.abundance_label">abundance: <code>{{ change.abundance_label }}</code></span>
          <span v-if="change.efficiency">efficiency: <code>{{ change.efficiency }}</code></span>
          <span v-if="change.changed" class="flag">·变化·</span>
          <button @click="selectEntity(change.entity_id)" class="btn-link">→ 看实体</button>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
import { api } from '../api.js'

export default {
  name: 'RunTimeline',
  props: {
    run: { type: Object, default: null },
    center: { type: String, default: '' }
  },
  data() {
    return {
      runs: [],
      selectedRunId: '',
      timeline: [],
      selectedRound: null,
      selectedRoundData: null,
      report: null
    }
  },
  computed: {
    totalChanges() {
      return this.timeline.reduce((acc, p) => acc + p.new_changed_agents, 0)
    },
    maxChanges() {
      return this.timeline.reduce((m, p) => Math.max(m, p.new_changed_agents), 0) || 1
    },
    feedback() {
      const fb = this.report && this.report.feedback_loops
      if (!fb || !fb.has_feedback) return null
      return {
        closed: (fb.closed_on_source || []).map(x => x.entity_id),
        reactivated: (fb.reactivations || []).length
      }
    }
  },
  watch: {
    run() {
      if (this.run) {
        this.selectedRunId = this.run.run_id
        this.loadTimeline()
      }
    }
  },
  async mounted() {
    try {
      const data = await api.runs()
      this.runs = data.runs || []
      if (this.run) {
        this.selectedRunId = this.run.run_id
        this.loadTimeline()
      }
    } catch (err) {
      console.error('runs load failed', err)
    }
  },
  methods: {
    barHeight(point) {
      return Math.max(2, Math.round(60 * point.new_changed_agents / this.maxChanges))
    },
    async selectRun() {
      const run = this.runs.find(r => r.run_id === this.selectedRunId)
      if (run) this.$emit('select', run)
      this.loadTimeline()
    },
    async loadTimeline() {
      if (!this.selectedRunId) {
        this.timeline = []
        this.selectedRoundData = null
        return
      }
      try {
        const data = await api.runTimeline(this.selectedRunId)
        this.timeline = data.timeline || []
        this.selectedRound = null
        this.selectedRoundData = null
      } catch (err) {
        console.error('timeline load failed', err)
      }
      this.report = await api.runReport(this.selectedRunId).catch(() => null)
    },
    toggleRound(point) {
      if (this.selectedRound === point.round) {
        this.selectedRound = null
        this.selectedRoundData = null
      } else {
        this.selectedRound = point.round
        this.selectedRoundData = point
      }
    },
    selectEntity(entityId) {
      this.$emit('select', entityId)
    }
  }
}
</script>

<style scoped>
.timeline { display: flex; flex-direction: column; height: 100%; }
.feedback-banner {
  display: flex; align-items: center; gap: 8px; margin: 6px 0;
  padding: 6px 10px; border-radius: 4px; font-size: 12px;
  background: #3a2e1a; color: #f0c987; border: 1px solid #5a4422;
}
.feedback-banner .fb-icon { font-size: 14px; }
.feedback-banner .fb-node { cursor: pointer; color: #f0a36b; margin-left: 4px; }
.feedback-banner .fb-node:hover { text-decoration: underline; }
.toolbar {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 8px 12px;
  border-bottom: 1px solid var(--border);
  font-size: 12px;
}
.label { color: var(--muted); }
select { background: var(--panel-2); color: var(--text); border: 1px solid var(--border); border-radius: 4px; padding: 4px 8px; }
.meta { color: var(--muted); }
.chart {
  display: flex;
  align-items: flex-end;
  gap: 4px;
  padding: 8px 12px;
  flex: 1;
  overflow-x: auto;
  min-height: 80px;
}
.point {
  display: flex;
  flex-direction: column;
  align-items: center;
  cursor: pointer;
  padding: 4px;
  border-radius: 4px;
  min-width: 50px;
}
.point:hover { background: var(--panel-2); }
.point.selected { background: #3a3a5a; }
.bar {
  width: 18px;
  background: var(--accent);
  border-radius: 2px 2px 0 0;
  margin-bottom: 2px;
  transition: height 0.3s;
}
.round-label { font-size: 10px; color: var(--muted); }
.change { font-size: 11px; color: var(--text); }
.round-detail {
  padding: 8px 12px;
  border-top: 1px solid var(--border);
  font-size: 11px;
  max-height: 120px;
  overflow: auto;
}
.round-detail h4 { margin: 0 0 6px 0; font-size: 12px; }
.round-detail ul { list-style: none; padding: 0; margin: 0; }
.round-detail li { padding: 2px 0; }
.flag { color: #f0a36b; margin-left: 4px; }
.btn-link {
  background: none;
  border: none;
  color: var(--accent);
  cursor: pointer;
  margin-left: 6px;
  font-size: 11px;
}
</style>
