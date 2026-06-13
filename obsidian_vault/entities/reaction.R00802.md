---
entity_id: "reaction.R00802"
entity_type: "reaction"
name: "sucrose alpha-glucohydrolase"
source_database: "KEGG"
source_id: "R00802"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00802"
---

# sucrose alpha-glucohydrolase

`reaction.R00802`

## Static

- Type: `reaction`
- Source: `KEGG:R00802`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Sucrose + H2O beta-D-Fructose + alpha-D-Glucose

## Biological Role

Catalyzed by malZ (protein.P21517). Substrates: H2O (molecule.C00001), Sucrose (molecule.C00089). Products: alpha-D-Glucose (molecule.C00267).

## Annotation

Sucrose + H2O <=> beta-D-Fructose + alpha-D-Glucose

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[protein.P21517|protein.P21517]] `KEGG` `database` - via EC:3.2.1.20
- `is_product_of` <-- [[molecule.C00267|molecule.C00267]] `KEGG` `database` - C00089 + C00001 <=> C02336 + C00267
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C00089 + C00001 <=> C02336 + C00267
- `is_substrate_of` <-- [[molecule.C00089|molecule.C00089]] `KEGG` `database` - C00089 + C00001 <=> C02336 + C00267

## External IDs

- `KEGG:R00802`

## Notes

EQUATION: C00089 + C00001 <=> C02336 + C00267
