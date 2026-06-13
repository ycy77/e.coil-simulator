# Architecture

## Data flow

```
                ┌──────────────────────────────────────────────┐
                │   EcoCyc .dat / KEGG / NCBI / UniProt /     │
                │   RegulonDB flat files (data/raw/...)       │
                └────────────────────┬─────────────────────────┘
                                     │
              scripts/parse_ecocyc.py, build_*.py
                                     │
                                     ▼
                ┌──────────────────────────────────────────────┐
                │  data/normalized/                            │
                │    entities.csv    edges.csv    pathways.csv │
                └────────────────────┬─────────────────────────┘
                                     │
              scripts/audit_entities.py  (vLLM strict, no fallback)
                                     │
                                     ▼
                ┌──────────────────────────────────────────────┐
                │  data/audit/decisions/<type>.jsonl           │
                │  data/audit/ambiguous/<type>.jsonl           │
                │  data/audit/reports/<type>.report.md         │
                └────────────────────┬─────────────────────────┘
                                     │
              scripts/canonicalize_v2.py  (audit + rules)
                                     │
                                     ▼
                ┌──────────────────────────────────────────────┐
                │  data/normalized/_v2/                        │
                │    entities.csv (with is_exogenous,          │
                │                   family_key, display_name)  │
                │    edges.csv    pathways.csv                 │
                │    canonical_entity_map_v2.csv               │
                └────────────────────┬─────────────────────────┘
                                     │
              scripts/enrich_entities_v2.py  (multi-source)
                                     │
                                     ▼
                ┌──────────────────────────────────────────────┐
                │  data/enriched/_v2/                          │
                │    entities_enriched_v2.jsonl                │
                │    entities_enriched_v2_lite.jsonl           │
                │    enrichment_report_v2.json                 │
                └────────────────────┬─────────────────────────┘
                                     │
        ┌────────────────────────────┴───────────────────────────┐
        │                                                         │
        ▼                                                         ▼
┌───────────────────────┐                              ┌──────────────────────┐
│  SimulationEngine     │                              │  Diagnostic UI       │
│  (ecoil_sim/sim/)     │                              │  (web/backend +      │
│  ─ reads entities/edges│                             │   web/frontend)      │
│  ─ uses rule_registry │                              │  ─ /api/entities     │
│  ─ prompt_builder     │                              │  ─ /api/edges        │
│  ─ LLM client         │                              │  ─ /api/audit        │
│  ─ action_interpreter │                              │  ─ vis-network       │
└────────┬──────────────┘                              └──────────┬───────────┘
         │                                                         │
         ▼                                                         ▼
┌───────────────────────┐                              ┌──────────────────────┐
│  runs/<ts>/           │                              │  Browser             │
│    rounds/*.json      │                              │  http://...:40211    │
│    agents/*.json      │                              │                      │
│    meta.json          │                              │                      │
└───────────────────────┘                              └──────────────────────┘
```

## Module map

| Package | Responsibility |
|---|---|
| `ecoil_sim/graph` | Static graph models (Entity, Edge, Pathway). Pure data classes. |
| `ecoil_sim/state` | Runtime `AgentState` (state / efficiency / abundance). |
| `ecoil_sim/agents/prompt_builder.py` | Builds the LLM prompt for a given Agent; consumes `EnrichedService`. |
| `ecoil_sim/agents/llm.py` | `AsyncVLLMClient` and `RuleBasedMockLLM`. |
| `ecoil_sim/llm/name_resolver.py` | Bi-directional id ↔ public name resolution. |
| `ecoil_sim/sim/engine.py` | The BFS scheduler. Wakes Agents, calls the prompt builder, applies actions. |
| `ecoil_sim/sim/enriched_service.py` | Side-car index of `entities_enriched_v2_lite.jsonl` keyed by entity_id. |
| `ecoil_sim/sim/perturbation.py` | Natural-language perturbation parsing. |
| `ecoil_sim/actions/interpreter.py` | Applies an LLM action to an `AgentState`. |
| `ecoil_sim/validation/action_validator.py` | Rejects malformed actions before they reach the interpreter. |
| `ecoil_sim/registry/rule_registry.py` | Loads `data/registry/native_rules.jsonl`. |
| `ecoil_sim/retrieval/` | Temporal Graph-RAG: per-round retrieval of relevant rules / entities. |
| `ecoil_sim/storage/simulation_store.py` | Round-by-round JSONL persistence under `runs/`. |
| `ecoil_sim/report/reporter.py` | Human-readable stage reports (`display_name` + first-mention `[id]`). |

## Frontend / backend split

* `web/backend/` is FastAPI. It mounts `DataLoader` (`entities.csv`),
  `EnrichedLoader` (`entities_enriched_v2_lite.jsonl`),
  `GraphService` (subgraph extraction), and `RunService` (round
  history). CORS is permissive (`*`) because the diagnostic is
  local-only. Port `28932` is hardcoded.
* `web/frontend/` is Vue 2.7 + Vite 4.5 + vis-network 9.1.
  `SubgraphView.vue` consumes `/api/entities/{id}/subgraph`. The
  default hop is `1`. Concurrent responses are guarded by a per-mount
  request sequence so an in-flight `/subgraph` response cannot
  overwrite a newer selection.

## Why the audit and the simulator share the same models

The Qwen3.5-9B model running on `http://127.0.0.1:8000` is the same
model the Agents will eventually reason with during a perturbation.
This is deliberate: when the audit says "this is an exogenous drug",
the Agent that sees it during a simulation should also classify it
the same way. We will not introduce a second model mid-pipeline.