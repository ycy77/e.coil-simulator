<template>
  <div class="detail">
    <div v-if="!entity" class="empty">
      <p>← 选一个实体</p>
    </div>
    <div v-else>
      <header class="header">
        <span class="type" :class="'type-' + entity.entity_type">{{ entity.entity_type }}</span>
        <h3>{{ entity.display_name || entity.name || entity.entity_id }}</h3>
        <code class="entity-id">{{ entity.entity_id }}</code>
        <span :class="['quality-badge', 'q-' + (entity.quality_label || 'unknown')]">
          {{ qualityIcon(entity.quality_label) }} {{ entity.quality_label || 'unknown' }}
        </span>
      </header>
      <section v-if="entity.enriched && (entity.enriched.summary || entity.enriched.functional_context)">
        <h4>enriched card</h4>
        <p v-if="entity.enriched.functional_context" class="func">{{ entity.enriched.functional_context }}</p>
        <pre v-if="entity.enriched.summary" class="summary">{{ truncateSummary(entity.enriched.summary, 600) }}</pre>
        <div v-if="entity.enriched.linked_entities && Object.keys(entity.enriched.linked_entities).length" class="linked">
          <span class="linked-label">linked_entities:</span>
          <span v-for="(value, key) in entity.enriched.linked_entities" :key="key" class="linked-pill">
            <span class="linked-key">{{ key }}:</span>
            <span v-if="value && value.entity_id" class="linked-id clickable" @click="$emit('select', value.entity_id)">
              {{ value.name || value.entity_id }} <code>{{ value.entity_id }}</code>
            </span>
            <span v-else class="linked-id">{{ JSON.stringify(value) }}</span>
          </span>
        </div>
        <div v-if="entity.enriched.evidence_sources && entity.enriched.evidence_sources.length" class="ev">
          <span class="ev-label">sources:</span>
          <span v-for="s in entity.enriched.evidence_sources" :key="s" class="ev-pill">{{ s }}</span>
        </div>
      </section>
      <section>
        <h4>raw annotation ({{ entity.annotation_length }} 字符)</h4>
        <pre v-if="entity.annotation" class="annotation">{{ entity.annotation }}</pre>
        <p v-else class="empty-text">⚠ 无 annotation</p>
      </section>
      <section>
        <h4>状态</h4>
        <p>默认: <code>{{ entity.default_state || '—' }}</code></p>
        <p>允许: <code>{{ entity.allowed_states.join(', ') || '—' }}</code></p>
        <p v-if="finalState">当前: <code>{{ finalState.state }}</code> / abundance: <code>{{ finalState.abundance_label || '—' }}</code> <span v-if="finalState.efficiency">/ efficiency: <code>{{ finalState.efficiency }}</code></span></p>
      </section>
      <section>
        <h4>来源</h4>
        <p>DB: <code>{{ entity.source_database || '—' }}</code></p>
        <p>external ids: <code>{{ entity.external_ids || '—' }}</code></p>
        <p>aliases: <span v-for="a in entity.aliases" :key="a" class="alias">{{ a }}</span></p>
      </section>
      <section>
        <h4>跨源对齐 (in/out 共 {{ entity.in_edges.length + entity.out_edges.length }})</h4>
        <table>
          <thead>
            <tr><th>source</th><th>→</th><th>target</th><th>relation</th><th>db</th></tr>
          </thead>
          <tbody>
            <tr v-for="(e, idx) in [...entity.in_edges, ...entity.out_edges].slice(0, 40)" :key="idx">
              <td><code>{{ e.source_id }}</code></td>
              <td>→</td>
              <td><code>{{ e.target_id }}</code></td>
              <td><code>{{ e.relation_type }}</code></td>
              <td><code>{{ e.source_database }}</code></td>
            </tr>
          </tbody>
        </table>
        <p v-if="entity.reconciliation.cross_source_conflicts.length" class="conflict">
          ⚠ {{ entity.reconciliation.cross_source_conflicts.length }} 对 (source,target) 跨源关系不一致:
        </p>
        <ul v-if="entity.reconciliation.cross_source_conflicts.length" class="conflict-list">
          <li v-for="(c, idx) in entity.reconciliation.cross_source_conflicts.slice(0, 6)" :key="idx">
            <code>{{ c.source_id }}</code> → <code>{{ c.target_id }}</code>:
            <span v-for="edge in c.conflicting_edges" :key="edge.source_record_id">
              <code>{{ edge.relation_type }}</code> ({{ edge.source_database }})
            </span>
          </li>
        </ul>
      </section>
      <section v-if="entity.same_name_siblings && entity.same_name_siblings.length">
        <h4>
          同名兄弟 ({{ entity.same_name_siblings.length + 1 }} 个 entity 共用此名)
        </h4>
        <p class="hint">EcoCyc 经常给同一 functional protein 不同 MONOMER id。点击切换看哪个最适合做 canonical handle。</p>
        <ul class="siblings">
          <li
            v-for="s in entity.same_name_siblings"
            :key="s.entity_id"
            class="sibling clickable"
            @click="$emit('select', s.entity_id)">
            <span class="type" :class="'type-' + s.entity_type">{{ s.entity_type }}</span>
            <code>{{ s.entity_id }}</code>
            <span class="db">{{ s.source_database || '?' }}</span>
            <span v-if="s.annotation_length" class="ann-len">{{ s.annotation_length }} 字</span>
          </li>
        </ul>
      </section>
      <section v-if="agentHistory && agentHistory.history && agentHistory.history.history && agentHistory.history.history.length">
        <h4>Run {{ run.run_id }} 状态历史</h4>
        <ul class="history">
          <li v-for="(item, idx) in agentHistory.history.history" :key="idx">
            <span class="round">round {{ item.round }}</span>
            <code>{{ item.state }}</code>
            <span v-if="item.abundance_label" class="abundance">abundance: <code>{{ item.abundance_label }}</code></span>
            <span v-if="item.efficiency" class="eff">efficiency: <code>{{ item.efficiency }}</code></span>
            <span v-if="item.changed" class="flag">·变化·</span>
            <p class="reason" v-if="item.reason">{{ item.reason }}</p>
          </li>
        </ul>
      </section>
    </div>
  </div>
</template>

<script>
export default {
  name: 'EntityDetail',
  props: {
    entity: { type: Object, default: null },
    run: { type: Object, default: null },
    agentHistory: { type: Object, default: null }
  },
  computed: {
    finalState() {
      if (!this.agentHistory) return null
      return this.agentHistory.final_state || null
    }
  },
  methods: {
    qualityIcon(quality) {
      if (quality === 'informative') return '🟢'
      if (quality === 'placeholder') return '🟡'
      if (quality === 'empty') return '🔴'
      return '⚪'
    },
    truncateSummary(text, max) {
      if (!text) return ''
      if (text.length <= max) return text
      return text.substring(0, max) + '…'
    }
  }
}
</script>

<style scoped>
.detail { padding: 12px; font-size: 12px; }
.empty { color: var(--muted); padding: 24px; text-align: center; }
.header { display: flex; align-items: center; gap: 8px; flex-wrap: wrap; margin-bottom: 12px; }
.header h3 { margin: 0; font-size: 15px; }
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
.entity-id { background: var(--panel-2); padding: 1px 6px; border-radius: 3px; font-size: 11px; }
section { margin-bottom: 16px; }
section h4 { font-size: 12px; color: var(--muted); text-transform: uppercase; margin: 0 0 6px 0; letter-spacing: 0.5px; }
.annotation {
  background: var(--panel-2);
  padding: 8px;
  border-radius: 4px;
  font-size: 11px;
  max-height: 200px;
  overflow: auto;
  white-space: pre-wrap;
  margin: 0;
}
.empty-text { color: #f0a36b; }
.alias { display: inline-block; background: var(--panel-2); padding: 1px 6px; border-radius: 3px; margin: 2px 2px 0 0; font-size: 11px; }
table { width: 100%; border-collapse: collapse; font-size: 11px; }
th, td { padding: 3px 4px; text-align: left; border-bottom: 1px solid var(--border); }
th { color: var(--muted); font-weight: 500; }
.conflict { color: #f0a36b; }
.conflict-list { list-style: none; padding: 0; margin: 4px 0; }
.conflict-list li { padding: 4px 6px; background: var(--panel-2); border-radius: 3px; margin: 2px 0; font-size: 11px; }
.siblings { list-style: none; padding: 0; margin: 4px 0; }
.sibling {
  display: flex;
  align-items: center;
  gap: 6px;
  padding: 4px 6px;
  background: var(--panel-2);
  border-radius: 3px;
  margin: 2px 0;
  font-size: 11px;
}
.sibling.clickable { cursor: pointer; }
.sibling.clickable:hover { background: #3a3a5a; }
.sibling .db { color: var(--muted); font-size: 10px; }
.sibling .ann-len { color: #7ad7a3; font-size: 10px; margin-left: auto; }
.hint { color: var(--muted); font-size: 11px; margin: 0 0 6px 0; }
.history { list-style: none; padding: 0; margin: 0; }
.history li { padding: 6px 8px; background: var(--panel-2); border-radius: 3px; margin: 4px 0; font-size: 11px; }
.history .round { color: var(--muted); margin-right: 6px; }
.history .flag { color: #f0a36b; margin-left: 6px; }
.history .reason { margin: 4px 0 0 0; color: var(--muted); font-style: italic; }
.history .abundance, .history .eff { color: var(--muted); margin-left: 6px; }
</style>
