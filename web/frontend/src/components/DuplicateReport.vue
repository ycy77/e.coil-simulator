<template>
  <div class="dup-report" v-if="visible">
    <div class="header">
      <h3>重复名诊断</h3>
      <span class="meta">
        涉及 {{ report.affected_entity_count }} 个 entity，
        按出现次数排前 {{ report.groups_returned }} 名
      </span>
      <button @click="$emit('close')" class="close">×</button>
    </div>
    <div class="body">
      <p class="hint">
        EcoCyc 给同一 functional protein 多个 MONOMER id 是主要来源。
        也可能是同 name 跨 entity_type (reaction / complex / protein)，
        或同 name 跨 data source。
        点击 → 跳到该 entity。
      </p>
      <table>
        <thead>
          <tr>
            <th>name</th>
            <th>×</th>
            <th>types</th>
            <th>db</th>
            <th>sample ids</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="group in report.groups" :key="group.name" class="row">
            <td class="name-cell">{{ group.name }}</td>
            <td><span class="count">{{ group.entity_count }}</span></td>
            <td>
              <span v-for="t in group.entity_types" :key="t" class="type" :class="'type-' + t">{{ t }}</span>
            </td>
            <td>
              <span v-for="d in group.source_databases" :key="d" class="db">{{ d }}</span>
            </td>
            <td class="ids">
              <code v-for="eid in group.sample_ids" :key="eid"
                    class="clickable"
                    @click="$emit('select', eid)">{{ eid }}</code>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
import { api } from '../api.js'

export default {
  name: 'DuplicateReport',
  props: { visible: { type: Boolean, default: false } },
  data() {
    return {
      report: {
        affected_entity_count: 0,
        groups_returned: 0,
        groups: []
      }
    }
  },
  async mounted() {
    if (this.visible) this.load()
  },
  watch: {
    visible(v) { if (v) this.load() }
  },
  methods: {
    async load() {
      try {
        this.report = await api.duplicateNames(2, 50)
      } catch (err) {
        console.error('duplicate report load failed', err)
      }
    }
  }
}
</script>

<style scoped>
.dup-report {
  position: absolute;
  top: 48px;
  right: 16px;
  width: 800px;
  max-height: calc(100vh - 64px);
  background: var(--panel);
  border: 1px solid var(--border);
  border-radius: 6px;
  box-shadow: 0 8px 32px rgba(0,0,0,0.4);
  z-index: 50;
  display: flex;
  flex-direction: column;
}
.header {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 8px 12px;
  border-bottom: 1px solid var(--border);
}
.header h3 { margin: 0; font-size: 14px; }
.meta { color: var(--muted); font-size: 11px; flex: 1; }
.close {
  background: var(--panel-2);
  border: none;
  color: var(--text);
  width: 24px;
  height: 24px;
  border-radius: 4px;
  cursor: pointer;
  font-size: 16px;
}
.close:hover { background: #4a4a6a; }
.body { padding: 8px 12px; overflow: auto; }
.hint { color: var(--muted); font-size: 11px; margin: 0 0 8px 0; }
table { width: 100%; border-collapse: collapse; font-size: 11px; }
th, td { padding: 4px 6px; text-align: left; border-bottom: 1px solid var(--border); }
th { color: var(--muted); font-weight: 500; }
tr:hover { background: var(--panel-2); }
.name-cell { color: var(--text); }
.count {
  background: #f0a36b;
  color: #1e1e2e;
  padding: 1px 6px;
  border-radius: 3px;
  font-weight: 600;
  font-size: 10px;
}
.type {
  display: inline-block;
  padding: 1px 4px;
  border-radius: 3px;
  font-size: 9px;
  margin-right: 2px;
  text-transform: uppercase;
}
.type-gene { background: #4a5572; }
.type-protein { background: #6a4a2a; }
.type-small_molecule { background: #2a6a4a; }
.type-rna { background: #4a2a6a; }
.type-complex { background: #6a6a2a; }
.type-reaction { background: #4a4a4a; }
.db { display: inline-block; margin-right: 4px; color: var(--muted); font-size: 10px; }
.ids code { display: inline-block; margin-right: 4px; font-size: 10px; }
.ids code.clickable { cursor: pointer; }
.ids code.clickable:hover { color: var(--accent); }
</style>
