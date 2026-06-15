<template>
  <div id="layout">
    <header class="topbar">
      <div class="title">E.coil 诊断控制台</div>
      <div class="stats" v-if="stats">
        <span class="badge badge-source" :title="stats.data_source || ''">
          {{ stats.data_source || '_v2' }}
        </span>
        <span class="badge">baseline {{ stats.entity_count }} ent</span>
        <span class="badge">baseline {{ stats.edge_count }} edge</span>
        <span class="badge badge-perturbagen" v-if="stats.perturbagen"
              :title="perturbagenSummary">
          perturbagen {{ stats.perturbagen.entities }}
        </span>
        <span class="badge badge-quarantine" v-if="stats.quarantine_count > 0">
          quarantine {{ stats.quarantine_count }}
        </span>
        <span class="badge">pathway {{ stats.pathway_count }}</span>
        <span class="badge">空 annotation {{ stats.empty_annotation_count }}</span>
        <span class="badge" v-for="(count, db) in stats.source_database_distribution" :key="db">
          {{ db }}: {{ count }}
        </span>
        <button class="diagnostic-btn" @click="showDuplicates = !showDuplicates">
          {{ showDuplicates ? '隐藏' : '查看' }} 重复名诊断
        </button>
        <button class="perturbagen-btn" @click="showPerturbagens = !showPerturbagens"
                v-if="stats.perturbagen">
          {{ showPerturbagens ? '隐藏' : '查看' }} 扰动池
        </button>
        <button class="insights-btn" @click="showInsights = !showInsights">
          {{ showInsights ? '隐藏' : '查看' }} 验证看板
        </button>
        <button class="intake-btn" @click="showIntake = !showIntake">
          + 扰动
        </button>
      </div>
    </header>
    <div class="grid">
      <EntitySearch class="col-search" @select="onSelect" />
      <SubgraphView class="col-graph" :center="center" @select="onSelect" />
      <EntityDetail class="col-detail" :entity="detail" :run="run" :agentHistory="agentHistory" @select="onSelect" />
      <RunTimeline class="col-timeline" :run="run" :center="center" @select="onRunSelect" />
    </div>
    <DuplicateReport :visible="showDuplicates" @close="showDuplicates = false" @select="onSelect" />
    <InsightsPanel :visible="showInsights" @close="showInsights = false" @select="onInsightSelect" />
    <PerturbationPanel :visible="showIntake" @close="showIntake = false" @select="onInsightSelect" />
    <div v-if="showPerturbagens" class="perturbagen-overlay" @click.self="showPerturbagens = false">
      <div class="perturbagen-modal">
        <header>
          <h3>perturbagen pool ({{ perturbagens.length }})</h3>
          <button @click="showPerturbagens = false">x</button>
        </header>
        <div class="perturbagen-list">
          <div v-for="p in perturbagens" :key="p.entity_id" class="perturbagen-row">
            <span class="type-tag" :data-type="p.entity_type">{{ p.entity_type }}</span>
            <span class="name" @click="onSelect(p.entity_id); showPerturbagens=false">{{ p.name }}</span>
            <span class="display-name" v-if="p.display_name && p.display_name !== p.name">
              {{ p.display_name }}
            </span>
            <span class="db">{{ p.source_database }}</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { api } from './api.js'
import EntitySearch from './components/EntitySearch.vue'
import SubgraphView from './components/SubgraphView.vue'
import EntityDetail from './components/EntityDetail.vue'
import RunTimeline from './components/RunTimeline.vue'
import DuplicateReport from './components/DuplicateReport.vue'
import InsightsPanel from './components/InsightsPanel.vue'
import PerturbationPanel from './components/PerturbationPanel.vue'

export default {
  name: 'App',
  components: { EntitySearch, SubgraphView, EntityDetail, RunTimeline, DuplicateReport, InsightsPanel, PerturbationPanel },
  data() {
    return {
      stats: null,
      center: '',
      detail: null,
      run: null,
      agentHistory: null,
      showDuplicates: false,
      showPerturbagens: false,
      showInsights: false,
      showIntake: false,
      perturbagens: []
    }
  },
  computed: {
    perturbagenSummary() {
      const p = this.stats && this.stats.perturbagen
      if (!p) return ''
      const parts = []
      for (const [t, n] of Object.entries(p.by_type || {})) {
        parts.push(`${t}: ${n}`)
      }
      return 'exogenous perturbagen pool: ' + parts.join(', ')
    }
  },
  watch: {
    showPerturbagens(v) {
      if (v && this.perturbagens.length === 0) this.loadPerturbagens()
    }
  },
  mounted() {
    this.loadStats()
  },
  methods: {
    async loadStats() {
      try {
        this.stats = await api.stats()
      } catch (err) {
        console.error('failed to load stats', err)
      }
    },
    async loadPerturbagens() {
      try {
        const data = await api.perturbagens(200)
        this.perturbagens = data.results || []
      } catch (e) {
        console.error('failed to load perturbagens', e)
        this.perturbagens = []
      }
    },
    async onSelect(id) {
      if (!id) return
      this.center = id
      try {
        this.detail = await api.entityDetail(id)
      } catch (err) {
        console.error('entity detail failed', err)
        this.detail = null
      }
      if (this.run && this.run.run_id) {
        await this.loadAgentHistory(id)
      } else {
        this.agentHistory = null
      }
    },
    async onInsightSelect(id) {
      this.showInsights = false
      await this.onSelect(id)
    },
    async onRunSelect(payload) {
      // RunTimeline emits either a run object (the run picker) or an
      // entity id string (the "→ 看实体" buttons inside a round detail).
      if (typeof payload === 'string') {
        await this.onSelect(payload)
        return
      }
      if (payload && payload.run_id) {
        this.run = payload
        if (this.center) await this.loadAgentHistory(this.center)
      }
    },
    async loadAgentHistory(entityId) {
      if (!this.run || !this.run.run_id || !entityId) {
        this.agentHistory = null
        return
      }
      try {
        this.agentHistory = await api.runAgent(this.run.run_id, entityId)
      } catch (err) {
        // Not every entity has agent history in a given run; that's fine.
        this.agentHistory = null
      }
    }
  }
}
</script>

<style>
:root {
  --bg: #1e1e2e;
  --panel: #252537;
  --panel-2: #2d2d44;
  --text: #e6e6f0;
  --muted: #a0a0b8;
  --accent: #7c9eff;
  --border: #383850;
}

* { box-sizing: border-box; }

body, html, #app {
  margin: 0;
  padding: 0;
  height: 100%;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'PingFang SC', 'Microsoft YaHei', sans-serif;
  background: var(--bg);
  color: var(--text);
}

#layout {
  display: flex;
  flex-direction: column;
  height: 100vh;
}

.topbar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 8px 16px;
  background: var(--panel);
  border-bottom: 1px solid var(--border);
  flex-wrap: wrap;
  gap: 8px;
}

.title {
  font-weight: 600;
  font-size: 16px;
}

.stats {
  display: flex;
  gap: 6px;
  flex-wrap: wrap;
}

.badge {
  background: var(--panel-2);
  color: var(--muted);
  padding: 2px 8px;
  border-radius: 4px;
  font-size: 12px;
}
.diagnostic-btn {
  background: #f0a36b;
  color: #1e1e2e;
  border: none;
  padding: 4px 12px;
  border-radius: 4px;
  font-size: 12px;
  font-weight: 600;
  cursor: pointer;
}
.diagnostic-btn:hover { background: #ffba8a; }

.grid {
  display: grid;
  grid-template-columns: 280px 1fr 360px;
  grid-template-rows: 1fr 240px;
  grid-template-areas:
    "search graph detail"
    "timeline timeline detail";
  flex: 1;
  min-height: 0;
}

.col-search { grid-area: search; border-right: 1px solid var(--border); min-height: 0; }
.col-graph { grid-area: graph; min-height: 0; }
.col-detail { grid-area: detail; border-left: 1px solid var(--border); min-height: 0; overflow: auto; }
.col-timeline { grid-area: timeline; border-top: 1px solid var(--border); min-height: 0; }

.col-search, .col-graph, .col-timeline, .col-detail {
  background: var(--panel);
}
.badge-source { background: #2d2d44; color: #8fe0d0; font-family: monospace; font-size: 11px; }
.badge-perturbagen { background: #4a3a3a; color: #f0a36b; }
.badge-quarantine { background: #3a3a4a; color: #a0a0b8; }
.perturbagen-btn {
  background: #4a3a3a;
  color: #f0a36b;
  border: none;
  padding: 4px 12px;
  border-radius: 4px;
  font-size: 12px;
  font-weight: 600;
  cursor: pointer;
  margin-left: 8px;
}
.perturbagen-btn:hover { background: #5a4a4a; }
.insights-btn {
  background: #2a4a3a;
  color: #7ad7a3;
  border: none;
  padding: 4px 12px;
  border-radius: 4px;
  font-size: 12px;
  font-weight: 600;
  cursor: pointer;
  margin-left: 8px;
}
.insights-btn:hover { background: #36604a; }
.intake-btn {
  background: var(--accent);
  color: #1e1e2e;
  border: none;
  padding: 4px 12px;
  border-radius: 4px;
  font-size: 12px;
  font-weight: 600;
  cursor: pointer;
  margin-left: 8px;
}
.intake-btn:hover { background: #9bb4ff; }
.perturbagen-overlay {
  position: fixed;
  inset: 0;
  background: rgba(0, 0, 0, 0.55);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1000;
}
.perturbagen-modal {
  background: var(--panel);
  border: 1px solid var(--border);
  border-radius: 6px;
  width: 720px;
  max-height: 80vh;
  display: flex;
  flex-direction: column;
}
.perturbagen-modal header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 12px 16px;
  border-bottom: 1px solid var(--border);
}
.perturbagen-modal header h3 { margin: 0; font-size: 14px; }
.perturbagen-modal header button {
  background: none;
  border: none;
  color: var(--text);
  font-size: 20px;
  cursor: pointer;
}
.perturbagen-list {
  overflow-y: auto;
  padding: 8px 0;
}
.perturbagen-row {
  display: grid;
  grid-template-columns: 90px 160px 1fr 80px;
  gap: 12px;
  align-items: center;
  padding: 6px 16px;
  font-size: 12px;
  border-bottom: 1px solid var(--border);
}
.perturbagen-row:hover { background: var(--panel-2); }
.perturbagen-row .name { color: var(--text); cursor: pointer; }
.perturbagen-row .name:hover { color: var(--accent); }
.perturbagen-row .display-name { color: var(--muted); }
.perturbagen-row .db { color: var(--muted); font-family: monospace; }
.perturbagen-row .type-tag {
  display: inline-block;
  padding: 1px 6px;
  border-radius: 3px;
  font-size: 10px;
  text-align: center;
  background: var(--panel-2);
  color: var(--muted);
}
.perturbagen-row .type-tag[data-type="small_molecule"] { background: #2a4a3a; color: #7ad7a3; }
.perturbagen-row .type-tag[data-type="reaction"] { background: #3a3a3a; color: #c4c4c4; }
.perturbagen-row .type-tag[data-type="protein"] { background: #4a3a2a; color: #f0a36b; }
.perturbagen-row .type-tag[data-type="complex"] { background: #3a3a2a; color: #e8d36b; }
</style>
