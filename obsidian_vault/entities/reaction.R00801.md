---
entity_id: "reaction.R00801"
entity_type: "reaction"
name: "sucrose glucohydrolase"
source_database: "KEGG"
source_id: "R00801"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00801"
---

# sucrose glucohydrolase

`reaction.R00801`

## Static

- Type: `reaction`
- Source: `KEGG:R00801`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Sucrose + H2O D-Fructose + D-Glucose

## Biological Role

Catalyzed by malZ (protein.P21517). Substrates: H2O (molecule.C00001), Sucrose (molecule.C00089). Products: D-Glucose (molecule.C00031), D-Fructose (molecule.C00095).

## Annotation

Sucrose + H2O <=> D-Fructose + D-Glucose

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P21517|protein.P21517]] `KEGG` `database` - via EC:3.2.1.20
- `is_product_of` <-- [[molecule.C00031|molecule.C00031]] `KEGG` `database` - C00089 + C00001 <=> C00095 + C00031
- `is_product_of` <-- [[molecule.C00095|molecule.C00095]] `KEGG` `database` - C00089 + C00001 <=> C00095 + C00031
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C00089 + C00001 <=> C00095 + C00031
- `is_substrate_of` <-- [[molecule.C00089|molecule.C00089]] `KEGG` `database` - C00089 + C00001 <=> C00095 + C00031

## External IDs

- `KEGG:R00801`

## Notes

EQUATION: C00089 + C00001 <=> C00095 + C00031
