---
entity_id: "reaction.R05747"
entity_type: "reaction"
name: "glutharedoxin:arsenate oxidoreductase"
source_database: "KEGG"
source_id: "R05747"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R05747"
---

# glutharedoxin:arsenate oxidoreductase

`reaction.R05747`

## Static

- Type: `reaction`
- Source: `KEGG:R05747`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Arsenate ion + Glutaredoxin Arsenite + Glutaredoxin disulfide

## Biological Role

Catalyzed by yfjU (gene.b2638), arsC (protein.P0AB96), yfgD (protein.P76569).

## Annotation

Arsenate ion + Glutaredoxin <=> Arsenite + Glutaredoxin disulfide

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[gene.b2638|gene.b2638]] `KEGG` `database` - via EC:1.20.4.1
- `catalyzes` <-- [[protein.P0AB96|protein.P0AB96]] `KEGG` `database` - via EC:1.20.4.1
- `catalyzes` <-- [[protein.P76569|protein.P76569]] `KEGG` `database` - via EC:1.20.4.1

## External IDs

- `KEGG:R05747`

## Notes

EQUATION: C11215 + C07292 <=> C06697 + C07293
