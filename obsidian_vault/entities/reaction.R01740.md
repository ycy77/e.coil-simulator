---
entity_id: "reaction.R01740"
entity_type: "reaction"
name: "D-gluconate:NADP+ 5-oxidoreductase"
source_database: "KEGG"
source_id: "R01740"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R01740"
---

# D-gluconate:NADP+ 5-oxidoreductase

`reaction.R01740`

## Static

- Type: `reaction`
- Source: `KEGG:R01740`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

D-Gluconic acid + NADP+ 5-Dehydro-D-gluconate + NADPH + H+

## Biological Role

Catalyzed by idnO (protein.P0A9P9). Substrates: NADP+ (molecule.C00006), D-Gluconic acid (molecule.C00257). Products: NADPH (molecule.C00005), H+ (molecule.C00080).

## Annotation

D-Gluconic acid + NADP+ <=> 5-Dehydro-D-gluconate + NADPH + H+

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P0A9P9|protein.P0A9P9]] `KEGG` `database` - via EC:1.1.1.69
- `is_product_of` <-- [[molecule.C00005|molecule.C00005]] `KEGG` `database` - C00257 + C00006 <=> C01062 + C00005 + C00080
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `KEGG` `database` - C00257 + C00006 <=> C01062 + C00005 + C00080
- `is_substrate_of` <-- [[molecule.C00006|molecule.C00006]] `KEGG` `database` - C00257 + C00006 <=> C01062 + C00005 + C00080
- `is_substrate_of` <-- [[molecule.C00257|molecule.C00257]] `KEGG` `database` - C00257 + C00006 <=> C01062 + C00005 + C00080

## External IDs

- `KEGG:R01740`

## Notes

EQUATION: C00257 + C00006 <=> C01062 + C00005 + C00080
