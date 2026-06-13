---
entity_id: "reaction.R00010"
entity_type: "reaction"
name: "alpha,alpha-trehalose glucohydrolase"
source_database: "KEGG"
source_id: "R00010"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00010"
---

# alpha,alpha-trehalose glucohydrolase

`reaction.R00010`

## Static

- Type: `reaction`
- Source: `KEGG:R00010`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

alpha,alpha-Trehalose + H2O 2 D-Glucose

## Biological Role

Catalyzed by treA (protein.P13482), treF (protein.P62601). Substrates: H2O (molecule.C00001), alpha,alpha-Trehalose (molecule.C01083). Products: D-Glucose (molecule.C00031).

## Annotation

alpha,alpha-Trehalose + H2O <=> 2 D-Glucose

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P13482|protein.P13482]] `KEGG` `database` - via EC:3.2.1.28
- `catalyzes` <-- [[protein.P62601|protein.P62601]] `KEGG` `database` - via EC:3.2.1.28
- `is_product_of` <-- [[molecule.C00031|molecule.C00031]] `KEGG` `database` - C01083 + C00001 <=> 2 C00031
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C01083 + C00001 <=> 2 C00031
- `is_substrate_of` <-- [[molecule.C01083|molecule.C01083]] `KEGG` `database` - C01083 + C00001 <=> 2 C00031

## External IDs

- `KEGG:R00010`

## Notes

EQUATION: C01083 + C00001 <=> 2 C00031
