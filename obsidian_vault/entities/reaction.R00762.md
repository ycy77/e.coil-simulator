---
entity_id: "reaction.R00762"
entity_type: "reaction"
name: "D-fructose-1,6-bisphosphate 1-phosphohydrolase"
source_database: "KEGG"
source_id: "R00762"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00762"
---

# D-fructose-1,6-bisphosphate 1-phosphohydrolase

`reaction.R00762`

## Static

- Type: `reaction`
- Source: `KEGG:R00762`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

D-Fructose 1,6-bisphosphate + H2O D-Fructose 6-phosphate + Orthophosphate

## Biological Role

Catalyzed by fbp (protein.P0A993), glpX (protein.P0A9C9), yggF (protein.P21437). Substrates: H2O (molecule.C00001), D-Fructose 1,6-bisphosphate (molecule.C00354). Products: Orthophosphate (molecule.C00009), D-Fructose 6-phosphate (molecule.C00085).

## Annotation

D-Fructose 1,6-bisphosphate + H2O <=> D-Fructose 6-phosphate + Orthophosphate

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[protein.P0A993|protein.P0A993]] `KEGG` `database` - via EC:3.1.3.11
- `catalyzes` <-- [[protein.P0A9C9|protein.P0A9C9]] `KEGG` `database` - via EC:3.1.3.11
- `catalyzes` <-- [[protein.P21437|protein.P21437]] `KEGG` `database` - via EC:3.1.3.11
- `is_product_of` <-- [[molecule.C00009|molecule.C00009]] `KEGG` `database` - C00354 + C00001 <=> C00085 + C00009
- `is_product_of` <-- [[molecule.C00085|molecule.C00085]] `KEGG` `database` - C00354 + C00001 <=> C00085 + C00009
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C00354 + C00001 <=> C00085 + C00009
- `is_substrate_of` <-- [[molecule.C00354|molecule.C00354]] `KEGG` `database` - C00354 + C00001 <=> C00085 + C00009

## External IDs

- `KEGG:R00762`

## Notes

EQUATION: C00354 + C00001 <=> C00085 + C00009
