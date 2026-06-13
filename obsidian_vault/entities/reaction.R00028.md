---
entity_id: "reaction.R00028"
entity_type: "reaction"
name: "maltose glucohydrolase"
source_database: "KEGG"
source_id: "R00028"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00028"
---

# maltose glucohydrolase

`reaction.R00028`

## Static

- Type: `reaction`
- Source: `KEGG:R00028`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Maltose + H2O 2 D-Glucose

## Biological Role

Catalyzed by malZ (protein.P21517). Substrates: H2O (molecule.C00001), Maltose (molecule.C00208). Products: D-Glucose (molecule.C00031).

## Annotation

Maltose + H2O <=> 2 D-Glucose

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[protein.P21517|protein.P21517]] `KEGG` `database` - via EC:3.2.1.20
- `is_product_of` <-- [[molecule.C00031|molecule.C00031]] `KEGG` `database` - C00208 + C00001 <=> 2 C00031
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C00208 + C00001 <=> 2 C00031
- `is_substrate_of` <-- [[molecule.C00208|molecule.C00208]] `KEGG` `database` - C00208 + C00001 <=> 2 C00031

## External IDs

- `KEGG:R00028`

## Notes

EQUATION: C00208 + C00001 <=> 2 C00031
