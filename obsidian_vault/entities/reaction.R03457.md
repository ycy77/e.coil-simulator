---
entity_id: "reaction.R03457"
entity_type: "reaction"
name: "D-erythro-1-(imidazol-4-yl)glycerol 3-phosphate hydro-lyase"
source_database: "KEGG"
source_id: "R03457"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R03457"
---

# D-erythro-1-(imidazol-4-yl)glycerol 3-phosphate hydro-lyase

`reaction.R03457`

## Static

- Type: `reaction`
- Source: `KEGG:R03457`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

D-erythro-1-(Imidazol-4-yl)glycerol 3-phosphate 3-(Imidazol-4-yl)-2-oxopropyl phosphate + H2O

## Biological Role

Catalyzed by hisB (protein.P06987). Substrates: D-erythro-1-(Imidazol-4-yl)glycerol 3-phosphate (molecule.C04666). Products: H2O (molecule.C00001), 3-(Imidazol-4-yl)-2-oxopropyl phosphate (molecule.C01267).

## Annotation

D-erythro-1-(Imidazol-4-yl)glycerol 3-phosphate <=> 3-(Imidazol-4-yl)-2-oxopropyl phosphate + H2O

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[protein.P06987|protein.P06987]] `KEGG` `database` - via EC:4.2.1.19
- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C04666 <=> C01267 + C00001
- `is_product_of` <-- [[molecule.C01267|molecule.C01267]] `KEGG` `database` - C04666 <=> C01267 + C00001
- `is_substrate_of` <-- [[molecule.C04666|molecule.C04666]] `KEGG` `database` - C04666 <=> C01267 + C00001

## External IDs

- `KEGG:R03457`

## Notes

EQUATION: C04666 <=> C01267 + C00001
