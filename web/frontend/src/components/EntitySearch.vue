<template>
  <div class="search">
    <input
      v-model="query"
      @input="onSearch"
      placeholder="搜索实体: lacI, FtsZ, glucose, cAMP..."
      class="search-input"
    />
    <div class="results">
      <div v-if="!results.length && !loading" class="empty">
        <p>试试搜 <code>lacI</code> / <code>glucose</code> / <code>crp</code></p>
        <p class="hint">命中按: 完全 id &gt; 名称 &gt; 别名 &gt; token &gt; annotation 文本</p>
      </div>
      <div v-for="entity in results" :key="entity.entity_id"
           class="result"
           :class="{ active: entity.entity_id === value }"
           @click="$emit('select', entity.entity_id)">
        <div class="result-row">
          <span class="type" :class="'type-' + entity.entity_type">{{ entity.entity_type }}</span>
          <span class="name">{{ entity.display_name || entity.name || entity.entity_id }}</span>
          <span v-if="nameCounts[entity.name] > 1" class="dup-badge" :title="`共 ${nameCounts[entity.name]} 个 entity 共用此名`">×{{ nameCounts[entity.name] }}</span>
          <span :class="['quality', 'q-' + (entity.quality_label || 'unknown')]" :title="entity.quality_label">
            {{ qualityIcon(entity.quality_label) }}
          </span>
        </div>
        <div class="entity-id">{{ entity.entity_id }}</div>
        <div v-if="entity.annotation_empty && entity.quality_label === 'placeholder'" class="warn">⚠ 无 annotation</div>
      </div>
    </div>
  </div>
</template>

<script>
import { api } from '../api.js'

export default {
  name: 'EntitySearch',
  props: { value: { type: String, default: '' } },
  data() {
    return {
      query: '',
      results: [],
      nameCounts: {},
      loading: false,
      debounceTimer: null
    }
  },
  methods: {
    onSearch() {
      if (this.debounceTimer) clearTimeout(this.debounceTimer)
      const q = this.query.trim()
      this.debounceTimer = setTimeout(() => this.runSearch(q), 250)
    },
    qualityIcon(quality) {
      if (quality === 'informative') return '🟢'
      if (quality === 'placeholder') return '🟡'
      if (quality === 'empty') return '🔴'
      return '⚪'
    },
    async runSearch(q) {
      if (!q) {
        this.results = []
        return
      }
      this.loading = true
      try {
        const data = await api.searchEntities(q, 30)
        this.results = data.results || []
        // Tally how many distinct entity_ids share each name. The user
        // sees a badge like "×3" so they know the same name is reused
        // across multiple ids and can jump to the diagnostic panel.
        const counts = {}
        for (const r of this.results) {
          counts[r.name] = (counts[r.name] || 0) + 1
        }
        this.nameCounts = counts
      } catch (err) {
        console.error('search failed', err)
        this.results = []
      } finally {
        this.loading = false
      }
    }
  }
}
</script>

<style scoped>
.search { display: flex; flex-direction: column; height: 100%; }
.search-input {
  margin: 12px;
  padding: 8px 12px;
  background: var(--panel-2);
  color: var(--text);
  border: 1px solid var(--border);
  border-radius: 4px;
  outline: none;
  font-size: 13px;
}
.search-input:focus { border-color: var(--accent); }
.results { flex: 1; overflow: auto; padding: 0 8px 12px; }
.empty { padding: 12px; color: var(--muted); font-size: 12px; }
.empty code { background: var(--panel-2); padding: 1px 6px; border-radius: 3px; }
.hint { font-size: 11px; opacity: 0.6; }
.result {
  padding: 8px 10px;
  margin: 4px 0;
  border-radius: 4px;
  cursor: pointer;
  background: var(--panel-2);
  transition: background 0.15s;
}
.result:hover { background: #353550; }
.result.active { background: #3a3a5a; border-left: 3px solid var(--accent); }
.result-row { display: flex; align-items: center; gap: 6px; }
.name { font-weight: 500; font-size: 13px; }
.entity-id { font-size: 11px; color: var(--muted); margin-top: 2px; }
.warn { font-size: 10px; color: #f0a36b; margin-top: 2px; }
.type {
  display: inline-block;
  padding: 1px 6px;
  border-radius: 3px;
  font-size: 10px;
  background: #4a4a6a;
  color: var(--text);
  text-transform: uppercase;
  letter-spacing: 0.5px;
}
.type-gene { background: #4a5572; }
.type-protein { background: #6a4a2a; }
.type-small_molecule { background: #2a6a4a; }
.type-rna { background: #4a2a6a; }
.type-complex { background: #6a6a2a; }
.type-reaction { background: #4a4a4a; }
.dup-badge {
  background: #f0a36b;
  color: #1e1e2e;
  padding: 1px 6px;
  border-radius: 3px;
  font-size: 10px;
  font-weight: 600;
  margin-left: 4px;
}
</style>
