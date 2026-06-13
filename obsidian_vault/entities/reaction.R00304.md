---
entity_id: "reaction.R00304"
entity_type: "reaction"
name: "D-glucose-1-phosphate phosphohydrolase"
source_database: "KEGG"
source_id: "R00304"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00304"
---

# D-glucose-1-phosphate phosphohydrolase

`reaction.R00304`

## Static

- Type: `reaction`
- Source: `KEGG:R00304`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

D-Glucose 1-phosphate + H2O D-Glucose + Orthophosphate

## Biological Role

Catalyzed by yihX (protein.P0A8Y3), agp (protein.P19926). Substrates: H2O (molecule.C00001), D-Glucose 1-phosphate (molecule.C00103). Products: Orthophosphate (molecule.C00009), D-Glucose (molecule.C00031).

## Annotation

D-Glucose 1-phosphate + H2O <=> D-Glucose + Orthophosphate

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P0A8Y3|protein.P0A8Y3]] `KEGG` `database` - via EC:3.1.3.10
- `catalyzes` <-- [[protein.P19926|protein.P19926]] `KEGG` `database` - via EC:3.1.3.10
- `is_product_of` <-- [[molecule.C00009|molecule.C00009]] `KEGG` `database` - C00103 + C00001 <=> C00031 + C00009
- `is_product_of` <-- [[molecule.C00031|molecule.C00031]] `KEGG` `database` - C00103 + C00001 <=> C00031 + C00009
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C00103 + C00001 <=> C00031 + C00009
- `is_substrate_of` <-- [[molecule.C00103|molecule.C00103]] `KEGG` `database` - C00103 + C00001 <=> C00031 + C00009

## External IDs

- `KEGG:R00304`

## Notes

EQUATION: C00103 + C00001 <=> C00031 + C00009
