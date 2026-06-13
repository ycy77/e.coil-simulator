---
entity_id: "reaction.R09771"
entity_type: "reaction"
name: "D-glycero-alpha-D-manno-heptose 1,7-bisphosphate 7-phosphohydrolase"
source_database: "KEGG"
source_id: "R09771"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R09771"
---

# D-glycero-alpha-D-manno-heptose 1,7-bisphosphate 7-phosphohydrolase

`reaction.R09771`

## Static

- Type: `reaction`
- Source: `KEGG:R09771`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

D-glycero-alpha-D-manno-Heptose 1,7-bisphosphate + H2O D-glycero-alpha-D-manno-Heptose 1-phosphate + Orthophosphate

## Biological Role

Catalyzed by gmhB (protein.P63228). Substrates: H2O (molecule.C00001), D-glycero-alpha-D-manno-Heptose 1,7-bisphosphate (molecule.C19879). Products: Orthophosphate (molecule.C00009), D-glycero-alpha-D-manno-Heptose 1-phosphate (molecule.C19880).

## Annotation

D-glycero-alpha-D-manno-Heptose 1,7-bisphosphate + H2O <=> D-glycero-alpha-D-manno-Heptose 1-phosphate + Orthophosphate

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P63228|protein.P63228]] `KEGG` `database` - via EC:3.1.3.83
- `is_product_of` <-- [[molecule.C00009|molecule.C00009]] `KEGG` `database` - C19879 + C00001 <=> C19880 + C00009
- `is_product_of` <-- [[molecule.C19880|molecule.C19880]] `KEGG` `database` - C19879 + C00001 <=> C19880 + C00009
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C19879 + C00001 <=> C19880 + C00009
- `is_substrate_of` <-- [[molecule.C19879|molecule.C19879]] `KEGG` `database` - C19879 + C00001 <=> C19880 + C00009

## External IDs

- `KEGG:R09771`

## Notes

EQUATION: C19879 + C00001 <=> C19880 + C00009
