<template>
  <div v-if="visible" class="pert-overlay" @click.self="$emit('close')">
    <div class="pert-modal">
      <header>
        <h3>扰动输入前门 · perturbation intake</h3>
        <button class="close" @click="$emit('close')">×</button>
      </header>
      <div class="pert-body">
        <p class="hint">
          用自然语言描述扰动(LLM 接地到图入口点,你确认后才运行)。
          例:<code>knock out recA, add 2mg/L ciprofloxacin</code>
        </p>
        <textarea v-model="text" rows="3" placeholder="knock out recA and add ciprofloxacin"></textarea>
        <div class="controls">
          <label><input type="checkbox" v-model="dryRun" /> 仅离线接地预览(不调 LLM)</label>
          <button class="primary" :disabled="parsing || !text.trim()" @click="doParse">
            {{ parsing ? '解析中…' : '解析' }}
          </button>
        </div>
        <p v-if="error" class="error">⚠ {{ error }}</p>

        <!-- dry-run grounding preview -->
        <section v-if="preview">
          <h4>离线接地候选</h4>
          <div v-for="(c, i) in preview.clauses" :key="i" class="clause">
            <div class="mention">"{{ c.mention }}"</div>
            <div v-if="!c.candidates.length" class="muted">(无候选 — 可能是外源物,LLM 会补 target)</div>
            <div v-for="cand in c.candidates" :key="cand.entity_id" class="cand clickable"
                 @click="$emit('select', cand.entity_id)">
              <code>{{ cand.entity_id }}</code> <span class="nm">{{ cand.name }}</span>
              <span class="via">via {{ cand.matched_via }}</span>
              <span v-if="cand.is_exogenous" class="exo">exogenous</span>
            </div>
          </div>
        </section>

        <!-- LLM proposal -->
        <section v-if="proposal">
          <h4>建议入口点(请确认)</h4>
          <div v-if="!proposal.perturbations.length" class="muted">(未接地任何入口点)</div>
          <div v-for="(p, i) in proposal.perturbations" :key="i" class="prop">
            <span class="kind" :data-kind="p.agent_kind">{{ p.agent_kind }}</span>
            <code class="clickable" @click="$emit('select', p.entity_id)">{{ p.entity_id }}</code>
            <span class="arrow">→</span>
            <span class="state">{{ p.target_state }}</span>
            <span class="conf">conf {{ (p.confidence || 0).toFixed(2) }}</span>
            <div class="from">from "{{ p.agent_mention }}"<span v-if="p.evidence"> · {{ p.evidence }}</span></div>
          </div>
          <div v-if="proposal.unresolved && proposal.unresolved.length" class="unresolved">
            <h4>未解析(需人工)</h4>
            <div v-for="(u, i) in proposal.unresolved" :key="i" class="muted">
              {{ u.mention || '?' }} — {{ u.reason || '' }}
            </div>
          </div>

          <div class="run-controls" v-if="proposal.perturbations.length">
            <label>rounds <input type="number" v-model.number="rounds" min="1" max="20" /></label>
            <label><input type="checkbox" v-model="useLlm" /> 用 LLM(取消则 mock,仅测管线)</label>
            <button class="primary run" :disabled="running" @click="doRun">
              {{ running ? '已提交…' : '确认并运行' }}
            </button>
          </div>
        </section>

        <p v-if="runResult" class="run-result">
          ✓ 已在后台启动 · log <code>{{ runResult.log_file }}</code> ·
          稍后在下方 run 列表选最新的 run 查看。
        </p>
      </div>
    </div>
  </div>
</template>

<script>
import { api } from '../api.js'

export default {
  name: 'PerturbationPanel',
  props: { visible: { type: Boolean, default: false } },
  data() {
    return {
      text: '', dryRun: false, parsing: false, running: false,
      preview: null, proposal: null, runResult: null, error: '',
      rounds: 5, useLlm: true
    }
  },
  methods: {
    async doParse() {
      this.error = ''
      this.preview = null
      this.proposal = null
      this.runResult = null
      this.parsing = true
      try {
        const res = await api.perturbationParse(this.text, this.dryRun)
        if (this.dryRun) this.preview = res
        else this.proposal = res
      } catch (e) {
        this.error = e.message || String(e)
      } finally {
        this.parsing = false
      }
    },
    async doRun() {
      if (!this.proposal || !this.proposal.engine_changes.length) return
      this.error = ''
      this.running = true
      try {
        this.runResult = await api.perturbationRun(this.proposal.engine_changes, this.rounds, this.useLlm)
      } catch (e) {
        this.error = e.message || String(e)
      } finally {
        this.running = false
      }
    }
  }
}
</script>

<style scoped>
.pert-overlay {
  position: fixed; inset: 0; background: rgba(0, 0, 0, 0.55);
  display: flex; align-items: center; justify-content: center; z-index: 1000;
}
.pert-modal {
  background: var(--panel); border: 1px solid var(--border); border-radius: 6px;
  width: 720px; max-height: 84vh; display: flex; flex-direction: column;
}
.pert-modal header {
  display: flex; align-items: center; justify-content: space-between;
  padding: 12px 16px; border-bottom: 1px solid var(--border);
}
.pert-modal header h3 { margin: 0; font-size: 14px; }
.pert-modal header .close { background: none; border: none; color: var(--text); font-size: 20px; cursor: pointer; }
.pert-body { overflow-y: auto; padding: 12px 16px 16px; }
.hint { color: var(--muted); font-size: 12px; margin: 0 0 8px; }
.hint code { background: var(--panel-2); padding: 1px 6px; border-radius: 3px; }
textarea {
  width: 100%; background: var(--panel-2); color: var(--text);
  border: 1px solid var(--border); border-radius: 4px; padding: 8px;
  font-size: 13px; resize: vertical; box-sizing: border-box;
}
.controls { display: flex; align-items: center; justify-content: space-between; margin: 8px 0; font-size: 12px; color: var(--muted); }
button.primary {
  background: var(--accent); color: #1e1e2e; border: none; padding: 6px 16px;
  border-radius: 4px; font-weight: 600; cursor: pointer; font-size: 12px;
}
button.primary:disabled { opacity: 0.5; cursor: default; }
button.run { background: #7ad7a3; }
.error { color: #f0a36b; font-size: 12px; }
section { margin-top: 12px; }
section h4 { font-size: 12px; color: var(--muted); text-transform: uppercase; letter-spacing: 0.5px; margin: 8px 0 6px; }
.muted { color: var(--muted); font-size: 12px; }
.clause { margin-bottom: 8px; }
.clause .mention { font-size: 12px; color: var(--text); margin-bottom: 2px; }
.cand, .prop { background: var(--panel-2); border-radius: 4px; padding: 6px 8px; margin: 3px 0; font-size: 12px; }
.cand .nm { color: var(--text); margin: 0 4px; }
.cand .via { color: var(--muted); font-size: 11px; }
.cand .exo, .prop .kind[data-kind="exogenous"] { color: #f0a36b; }
.clickable { cursor: pointer; }
.clickable:hover { color: var(--accent); }
.prop .kind { font-size: 10px; padding: 1px 6px; border-radius: 3px; background: #3a3a4a; color: var(--muted); margin-right: 6px; }
.prop .arrow { color: var(--muted); margin: 0 4px; }
.prop .state { color: #7ad7a3; }
.prop .conf { color: var(--muted); font-size: 11px; margin-left: 6px; }
.prop .from { color: var(--muted); font-size: 11px; margin-top: 2px; }
.run-controls { display: flex; align-items: center; gap: 14px; margin-top: 12px; font-size: 12px; color: var(--muted); }
.run-controls input[type="number"] { width: 48px; background: var(--panel-2); color: var(--text); border: 1px solid var(--border); border-radius: 4px; padding: 2px 4px; }
.run-result { color: #7ad7a3; font-size: 12px; margin-top: 10px; }
.run-result code { background: var(--panel-2); padding: 1px 6px; border-radius: 3px; }
</style>
