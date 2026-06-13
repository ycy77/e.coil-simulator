---
entity_id: "reaction.R00251"
entity_type: "reaction"
name: "5-oxo-L-proline amidohydrolase (ATP-hydrolysing)"
source_database: "KEGG"
source_id: "R00251"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00251"
---

# 5-oxo-L-proline amidohydrolase (ATP-hydrolysing)

`reaction.R00251`

## Static

- Type: `reaction`
- Source: `KEGG:R00251`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ATP + 5-Oxoproline + 2 H2O ADP + Orthophosphate + L-Glutamate

## Biological Role

Catalyzed by pxpB (protein.P0AAV4), pxpC (protein.P75745), pxpA (protein.P75746). Substrates: H2O (molecule.C00001), ATP (molecule.C00002), 5-Oxoproline (molecule.C01879). Products: ADP (molecule.C00008), Orthophosphate (molecule.C00009), L-Glutamate (molecule.C00025).

## Annotation

ATP + 5-Oxoproline + 2 H2O <=> ADP + Orthophosphate + L-Glutamate

## Outgoing Edges (0)

_None._

## Incoming Edges (9)

- `catalyzes` <-- [[protein.P0AAV4|protein.P0AAV4]] `KEGG` `database` - via EC:3.5.2.9
- `catalyzes` <-- [[protein.P75745|protein.P75745]] `KEGG` `database` - via EC:3.5.2.9
- `catalyzes` <-- [[protein.P75746|protein.P75746]] `KEGG` `database` - via EC:3.5.2.9
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `KEGG` `database` - C00002 + C01879 + 2 C00001 <=> C00008 + C00009 + C00025
- `is_product_of` <-- [[molecule.C00009|molecule.C00009]] `KEGG` `database` - C00002 + C01879 + 2 C00001 <=> C00008 + C00009 + C00025
- `is_product_of` <-- [[molecule.C00025|molecule.C00025]] `KEGG` `database` - C00002 + C01879 + 2 C00001 <=> C00008 + C00009 + C00025
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C00002 + C01879 + 2 C00001 <=> C00008 + C00009 + C00025
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `KEGG` `database` - C00002 + C01879 + 2 C00001 <=> C00008 + C00009 + C00025
- `is_substrate_of` <-- [[molecule.C01879|molecule.C01879]] `KEGG` `database` - C00002 + C01879 + 2 C00001 <=> C00008 + C00009 + C00025

## External IDs

- `KEGG:R00251`

## Notes

EQUATION: C00002 + C01879 + 2 C00001 <=> C00008 + C00009 + C00025
