# Diagnostic UI

## Layout

```
┌────────────┬──────────────────────────────┬──────────────┐
│ Entity     │  Subgraph                    │ Entity       │
│ search     │  (vis-network, hop=1)        │ detail       │
│            │                              │              │
├────────────┴──────────────────────────────┴──────────────┤
│  Run timeline (current run, per-round changes)            │
└───────────────────────────────────────────────────────────┘
```

## Ports

* Backend: `127.0.0.1:28932`
* Frontend (Vite dev server): `127.0.0.1:40211`
* Vite proxies `/api/*` to the backend.

Both ports are deliberately unusual to avoid collisions with common
dev services.

## Endpoints

| Method | Path | Returns |
|---|---|---|
| GET | `/api/health` | `{status, entities, edges}` |
| GET | `/api/stats` | type / source / relation distributions + enriched quality |
| GET | `/api/entities/search?q=...&limit=N` | List of matching entities |
| GET | `/api/entities/{id}` | Full overview: in/out edges, siblings, reconciliation |
| GET | `/api/entities/{id}/subgraph?hops=N&max_nodes=M` | nodes + edges for `vis-network` |
| GET | `/api/pathways` | All pathways |
| GET | `/api/diagnostics/duplicate-names` | Top duplicate-name groups |
| GET | `/api/runs` | List of simulation runs |
| GET | `/api/runs/{id}` | Run metadata |
| GET | `/api/runs/{id}/timeline` | Per-round new changes |
| GET | `/api/runs/{id}/agents/{entity_id}` | Per-Agent history |

## How uniqueness is guaranteed end-to-end

1. `entities.csv.display_name` is globally unique (verified by
   `scripts/verify_uniqueness.py`).
2. The backend serves `display_name` as the node label; no
   front-end rewriting.
3. The frontend `SubgraphView.vue` consumes that label verbatim and
   applies it as `nodes[i].label` in `vis-network`.
4. The frontend uses a request-sequence guard so an in-flight
   `/subgraph` response can never overwrite a newer selection.

## Subgraph extraction algorithm

`GraphService.subgraph(center, hops, max_nodes)` runs a BFS up to
`hops` edges, then trims to the closest `max_nodes` entities by hop
distance, with priority `protein > complex > reaction > small_molecule
> rna > gene > regulatory_region`. Edges are de-duplicated by
`(source_id, relation_type, target_id, source_database, source_record_id)`.

This guarantees the diagnostic view is interpretable for global
regulators (e.g. searching `lspA` no longer pulls in 198 unrelated
genes via sigma factors).

## Diagnostic views

* `EntitySearch.vue` shows each hit with its display name, type badge,
  duplicate-name badge, and enriched-quality icon
  (🟢 informative / 🟡 placeholder / 🔴 empty).
* `SubgraphView.vue` is the `vis-network` canvas. Default hop is `1`.
  The hop slider can grow to `3` but most queries look best at `1`.
* `EntityDetail.vue` shows the merged annotation, linked entities,
  in/out edges with their provenance, sibling entities (same name),
  and the Agent history (if a run is selected).
* `RunTimeline.vue` shows per-round change counts and round detail.
* `DuplicateReport.vue` lists the top duplicate-name offenders.

## Build

```bash
cd web/frontend
npm run dev          # http://127.0.0.1:40211
# or
npm run build        # dist/ for production (gitignored)
```