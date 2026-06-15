<template>
  <div class="subgraph">
    <div class="toolbar">
      <span class="center-label" v-if="center">中心: <code>{{ center }}</code></span>
      <span class="center-label muted" v-else>← 左侧搜索一个实体</span>
      <div class="hops">
        <label>hop</label>
        <input type="range" min="1" max="3" v-model.number="hops" @change="load" />
        <span>{{ hops }}</span>
      </div>
      <div class="filters">
        <label v-for="t in TYPES" :key="t" :class="{ active: enabled[t] }">
          <input type="checkbox" v-model="enabled[t]" @change="applyLocalFilter" />
          {{ t }}
        </label>
        <label :class="{ active: hideIsolated }" :title="hideIsolated ? '隐藏过滤后无可见边的节点' : '保留孤立节点'">
          <input type="checkbox" v-model="hideIsolated" @change="applyLocalFilter" />
          隐藏孤立点
        </label>
      </div>
    </div>
    <div ref="container" class="canvas"></div>
    <div class="footer" v-if="data">
      节点 {{ visibleNodes.length }} / {{ data.nodes.length }} · 边 {{ visibleEdges.length }} / {{ data.edges.length }}
      <span v-if="data.truncated" class="warn">已截断 (max_nodes)</span>
    </div>
  </div>
</template>

<script>
import { Network } from "vis-network/standalone/esm/vis-network"
import { api } from "../api.js"

// Reactions are no longer entities -- they were flattened into
// ``produces`` / ``consumes`` edge payloads by
// scripts/flatten_reactions.py. The graph now shows
// protein-catalyst -> product / substrate directly, so we omit
// "reaction" from the per-type filter here.
const TYPES = ["gene", "protein", "small_molecule", "rna", "complex", "regulatory_region"]

const RELATION_COLORS = {
  activates: "#7ad7a3",
  represses: "#f0a36b",
  inhibits: "#e06b6b",
  encodes: "#7c9eff",
  is_substrate_of: "#a0a0b8",
  is_product_of: "#a0a0b8",
  catalyzes: "#d59af1",
  participates_in: "#c4c4c4",
  binds: "#8fe0d0",
  is_component_of: "#5a5a7a",
  transports: "#e8d36b"
}

// Build a node row that fully specifies every visible field. We
// avoid vis-network's DataSet entirely and pass a plain array to
// `new Network(...)` because re-using a DataSet after HMR caused the
// engine to keep stale fields (e.g. the previous center's `label`)
// on the canvas. The new Network instance is recreated on every
// applyLocalFilter() (see createNetwork) to flush that state.
function buildNodeRow(n) {
  return {
    id: n.id,
    // Prefer the short name (e.g. "lspA") on the canvas. The full
    // display_name with the "(id #N)" suffix is preserved in
    // `n.label` and is still surfaced via the node tooltip and the
    // detail panel.
    label: String((n.name || n.label) == null ? "" : (n.name || n.label)),
    shape: String(n.shape || "box"),
    color: n.annotation_empty
      ? { background: "#4a3a3a", border: "#7a3a3a" }
      : { background: String(n.color || "#5a5a7a"), border: "#ffffff22" },
    font: { color: "#e6e6f0", size: 10 },
    group: n.entity_type,
    title: n.summary_excerpt || ""
  }
}

function buildEdgeRow(e, idx) {
  // Edge weight drives the visual width: 0.20 -> 1px,
  // 0.90 -> 5px. The simulation influence_score will reuse
  // this same number, so what the user sees on the canvas
  // matches what the agent will use downstream.
  const w = typeof e.edge_weight === "number" ? e.edge_weight : parseFloat(e.edge_weight || "0.4")
  const width = Math.max(1, Math.min(6, 0.5 + w * 5))
  // STRING channel tints experimental/database in a
  // separate colour from the curated regulates/binds palette
  // so PPI edges read as "data-driven" vs "curated".
  let color = RELATION_COLORS[e.relation_type] || "#5a5a7a"
  if (e.string_channel === "experimental") color = "#9b7ad0"
  else if (e.string_channel === "database") color = "#6a9b8e"
  else if (e.string_channel === "coexpression") color = "#a89878"
  return {
    id: [e.source_id, e.relation_type, e.target_id, e.source_database || idx].join("::"),
    from: e.source_id,
    to: e.target_id,
    label: e.relation_type,
    color: { color },
    dashes: e.relation_type === "represses" || e.relation_type === "inhibits",
    arrows: { to: { enabled: true } },
    width,
    // The simulation's influence_score and the report can
    // re-use the weight; expose it on the row for tooltip
    title: `weight=${(w || 0).toFixed(2)}` + (e.string_channel ? `  (${e.string_channel})` : "")
  }
}

export default {
  name: "SubgraphView",
  props: { center: { type: String, default: "" } },
  data() {
    return {
      TYPES,
      hops: 1,
      data: null,
      network: null,
      enabled: TYPES.reduce((acc, t) => { acc[t] = true; return acc }, {}),
      visibleNodes: [],
      visibleEdges: [],
      // When true, drop any node whose only edges in the BFS
      // neighborhood pass through a filtered-out type. The data is
      // multi-partite (gene↔protein↔gene), so toggling off a type
      // severs most cross-type paths and leaves many floating
      // singletons. Hiding them keeps the canvas readable. The user
      // can opt back in via the toolbar checkbox.
      hideIsolated: true,
      loadSeq: 0
    }
  },
  watch: {
    center() { this.load() },
    hops() { this.load() }
  },
  mounted() {
    this.initNetwork()
    this.load()
  },
  activated() { this.load() },
  beforeDestroy() {
    if (this.network) {
      try { this.network.destroy() } catch (e) { /* ignore */ }
      this.network = null
    }
  },
  methods: {
    initNetwork() {
      this.createNetwork([], [])
    },
    // Always destroy the existing Network instance and build a brand-new
    // one with the supplied rows. This is the only reliable way to
    // defeat vis-network 9.1.9's HMR / re-render bug where the engine
    // keeps the previous center's `label` field on the canvas after a
    // plain `setData({...})` call. Destroying and rebuilding the
    // Network is the only way to flush that stale state.
    createNetwork(nodes, edges) {
      if (this.network) {
        try { this.network.destroy() } catch (e) { /* ignore */ }
        this.network = null
      }
      this.network = new Network(this.$refs.container, { nodes, edges }, {
        physics: { stabilization: { iterations: 120 } },
        nodes: { borderWidth: 1, shadow: false, font: { color: "#e6e6f0", size: 11 } },
        edges: { arrows: { to: { enabled: true, scaleFactor: 0.4 } }, color: { color: "#5a5a7a" }, smooth: false, font: { size: 9, color: "#a0a0b8", strokeWidth: 0 } },
        interaction: { hover: true, tooltipDelay: 150 }
      })
      this.network.on("selectNode", params => {
        const id = params.nodes[0]
        if (id) this.$emit("select", id)
      })
    },
    async load() {
      const requestId = ++this.loadSeq
      if (!this.center) {
        // Force a full rebuild (not setData) so any stale label from
        // a previous center cannot survive.
        this.data = { nodes: [], edges: [] }
        this.applyLocalFilter()
        return
      }
      try {
        const center = this.center
        const hops = this.hops
        const data = await api.subgraph(center, hops, 200)
        if (requestId !== this.loadSeq || center !== this.center || hops !== this.hops) return
        this.data = data
        this.applyLocalFilter()
      } catch (err) {
        console.error("subgraph failed", err)
      }
    },
    applyLocalFilter() {
      if (!this.data) return
      const allowed = new Set(this.TYPES.filter(t => this.enabled[t]))
      this.visibleNodes = this.data.nodes.filter(n => allowed.has(n.entity_type))
      const nodeIds = new Set(this.visibleNodes.map(n => n.id))
      this.visibleEdges = this.data.edges.filter(e => nodeIds.has(e.source_id) && nodeIds.has(e.target_id))

      // Optional: drop nodes that the type filter severed from
      // every neighbor. A node "has a visible edge" iff at least
      // one of the kept edges touches it.
      if (this.hideIsolated && this.visibleNodes.length > 0) {
        const touched = new Set()
        for (const e of this.visibleEdges) {
          touched.add(e.source_id)
          touched.add(e.target_id)
        }
        this.visibleNodes = this.visibleNodes.filter(n => touched.has(n.id))
        const tightIds = new Set(this.visibleNodes.map(n => n.id))
        this.visibleEdges = this.visibleEdges.filter(e => tightIds.has(e.source_id) && tightIds.has(e.target_id))
      }

      const nodeRows = this.visibleNodes.map(buildNodeRow)
      const edgeRows = this.visibleEdges.map(buildEdgeRow)

      // Destroy + recreate the Network (see createNetwork) so a
      // previous query's `label` field can never leak onto the new
      // canvas.
      this.createNetwork(nodeRows, edgeRows)
      this.$nextTick(() => {
        if (!this.network) return
        this.network.fit({ animation: false })
      })
    }
  }
}
</script>

<style scoped>
.subgraph { display: flex; flex-direction: column; height: 100%; }
.toolbar {
  display: flex;
  align-items: center;
  gap: 16px;
  padding: 8px 12px;
  border-bottom: 1px solid var(--border);
  font-size: 12px;
  flex-wrap: wrap;
}
.center-label { color: var(--text); }
.center-label.muted { color: var(--muted); }
.center-label code { background: var(--panel-2); padding: 1px 6px; border-radius: 3px; }
.hops { display: flex; align-items: center; gap: 6px; }
.hops input { width: 100px; }
.filters { display: flex; gap: 4px; flex-wrap: wrap; }
.filters label {
  padding: 2px 6px;
  background: var(--panel-2);
  border-radius: 3px;
  cursor: pointer;
  font-size: 11px;
  color: var(--muted);
}
.filters label.active { color: var(--text); background: #3a3a5a; }
.filters input { display: none; }
.canvas { flex: 1; min-height: 0; background: #1a1a28; }
.footer {
  padding: 4px 12px;
  border-top: 1px solid var(--border);
  font-size: 11px;
  color: var(--muted);
}
.warn { color: #f0a36b; margin-left: 8px; }
</style>
