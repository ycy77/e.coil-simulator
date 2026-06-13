---
entity_id: "reaction.R00658"
entity_type: "reaction"
name: "2-phospho-D-glycerate hydro-lyase (phosphoenolpyruvate-forming)"
source_database: "KEGG"
source_id: "R00658"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00658"
---

# 2-phospho-D-glycerate hydro-lyase (phosphoenolpyruvate-forming)

`reaction.R00658`

## Static

- Type: `reaction`
- Source: `KEGG:R00658`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

2-Phospho-D-glycerate Phosphoenolpyruvate + H2O

## Biological Role

Catalyzed by eno (protein.P0A6P9). Substrates: 2-Phospho-D-glycerate (molecule.C00631). Products: H2O (molecule.C00001), Phosphoenolpyruvate (molecule.C00074).

## Annotation

2-Phospho-D-glycerate <=> Phosphoenolpyruvate + H2O

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[protein.P0A6P9|protein.P0A6P9]] `KEGG` `database` - via EC:4.2.1.11
- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C00631 <=> C00074 + C00001
- `is_product_of` <-- [[molecule.C00074|molecule.C00074]] `KEGG` `database` - C00631 <=> C00074 + C00001
- `is_substrate_of` <-- [[molecule.C00631|molecule.C00631]] `KEGG` `database` - C00631 <=> C00074 + C00001

## External IDs

- `KEGG:R00658`

## Notes

EQUATION: C00631 <=> C00074 + C00001
