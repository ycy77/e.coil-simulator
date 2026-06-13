---
entity_id: "reaction.R02334"
entity_type: "reaction"
name: "[1,4-(N-acetyl-beta-D-glucosaminyl)]n glycanohydrolase"
source_database: "KEGG"
source_id: "R02334"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R02334"
---

# [1,4-(N-acetyl-beta-D-glucosaminyl)]n glycanohydrolase

`reaction.R02334`

## Static

- Type: `reaction`
- Source: `KEGG:R02334`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Chitin + H2O Chitobiose + Chitin

## Biological Role

Catalyzed by chiA (protein.P13656). Substrates: H2O (molecule.C00001), Chitin (molecule.C00461). Products: Chitin (molecule.C00461), Chitobiose (molecule.C01674).

## Annotation

Chitin + H2O <=> Chitobiose + Chitin

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P13656|protein.P13656]] `KEGG` `database` - via EC:3.2.1.14
- `is_product_of` <-- [[molecule.C00461|molecule.C00461]] `KEGG` `database` - C00461 + C00001 <=> C01674 + C00461
- `is_product_of` <-- [[molecule.C01674|molecule.C01674]] `KEGG` `database` - C00461 + C00001 <=> C01674 + C00461
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C00461 + C00001 <=> C01674 + C00461
- `is_substrate_of` <-- [[molecule.C00461|molecule.C00461]] `KEGG` `database` - C00461 + C00001 <=> C01674 + C00461

## External IDs

- `KEGG:R02334`

## Notes

EQUATION: C00461 + C00001 <=> C01674 + C00461
