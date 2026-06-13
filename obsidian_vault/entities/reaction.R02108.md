---
entity_id: "reaction.R02108"
entity_type: "reaction"
name: "1,4-alpha-D-glucan glucanohydrolase"
source_database: "KEGG"
source_id: "R02108"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R02108"
---

# 1,4-alpha-D-glucan glucanohydrolase

`reaction.R02108`

## Static

- Type: `reaction`
- Source: `KEGG:R02108`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Starch + H2O Dextrin + Starch

## Biological Role

Catalyzed by malS (protein.P25718), amyA (protein.P26612). Substrates: H2O (molecule.C00001), Starch (molecule.C00369). Products: Starch (molecule.C00369), Dextrin (molecule.C00721).

## Annotation

Starch + H2O <=> Dextrin + Starch

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P25718|protein.P25718]] `KEGG` `database` - via EC:3.2.1.1
- `catalyzes` <-- [[protein.P26612|protein.P26612]] `KEGG` `database` - via EC:3.2.1.1
- `is_product_of` <-- [[molecule.C00369|molecule.C00369]] `KEGG` `database` - C00369 + C00001 <=> C00721 + C00369
- `is_product_of` <-- [[molecule.C00721|molecule.C00721]] `KEGG` `database` - C00369 + C00001 <=> C00721 + C00369
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C00369 + C00001 <=> C00721 + C00369
- `is_substrate_of` <-- [[molecule.C00369|molecule.C00369]] `KEGG` `database` - C00369 + C00001 <=> C00721 + C00369

## External IDs

- `KEGG:R02108`

## Notes

EQUATION: C00369 + C00001 <=> C00721 + C00369
