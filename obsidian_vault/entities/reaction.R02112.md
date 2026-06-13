---
entity_id: "reaction.R02112"
entity_type: "reaction"
name: "1,4-alpha-D-glucan maltohydrolase"
source_database: "KEGG"
source_id: "R02112"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R02112"
---

# 1,4-alpha-D-glucan maltohydrolase

`reaction.R02112`

## Static

- Type: `reaction`
- Source: `KEGG:R02112`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Starch Dextrin + Maltose

## Biological Role

Catalyzed by malS (protein.P25718), amyA (protein.P26612). Substrates: Starch (molecule.C00369). Products: Maltose (molecule.C00208), Dextrin (molecule.C00721).

## Annotation

Starch <=> Dextrin + Maltose

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P25718|protein.P25718]] `KEGG` `database` - via EC:3.2.1.1
- `catalyzes` <-- [[protein.P26612|protein.P26612]] `KEGG` `database` - via EC:3.2.1.1
- `is_product_of` <-- [[molecule.C00208|molecule.C00208]] `KEGG` `database` - C00369 <=> C00721 + C00208
- `is_product_of` <-- [[molecule.C00721|molecule.C00721]] `KEGG` `database` - C00369 <=> C00721 + C00208
- `is_substrate_of` <-- [[molecule.C00369|molecule.C00369]] `KEGG` `database` - C00369 <=> C00721 + C00208

## External IDs

- `KEGG:R02112`

## Notes

EQUATION: C00369 <=> C00721 + C00208
