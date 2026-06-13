---
entity_id: "reaction.R02887"
entity_type: "reaction"
name: "1,4-beta-D-glucan glucohydrolase"
source_database: "KEGG"
source_id: "R02887"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R02887"
---

# 1,4-beta-D-glucan glucohydrolase

`reaction.R02887`

## Static

- Type: `reaction`
- Source: `KEGG:R02887`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Cellodextrin + (n-2) H2O (n-2) D-Glucose + Cellobiose

## Biological Role

Catalyzed by bglX (protein.P33363). Substrates: H2O (molecule.C00001), Cellodextrin (molecule.C01898). Products: D-Glucose (molecule.C00031), Cellobiose (molecule.C00185).

## Annotation

Cellodextrin + (n-2) H2O <=> (n-2) D-Glucose + Cellobiose

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P33363|protein.P33363]] `KEGG` `database` - via EC:3.2.1.21
- `is_product_of` <-- [[molecule.C00031|molecule.C00031]] `KEGG` `database` - C01898 + (n-2) C00001 <=> (n-2) C00031 + C00185
- `is_product_of` <-- [[molecule.C00185|molecule.C00185]] `KEGG` `database` - C01898 + (n-2) C00001 <=> (n-2) C00031 + C00185
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C01898 + (n-2) C00001 <=> (n-2) C00031 + C00185
- `is_substrate_of` <-- [[molecule.C01898|molecule.C01898]] `KEGG` `database` - C01898 + (n-2) C00001 <=> (n-2) C00031 + C00185

## External IDs

- `KEGG:R02887`

## Notes

EQUATION: C01898 + (n-2) C00001 <=> (n-2) C00031 + C00185
