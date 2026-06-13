---
entity_id: "reaction.R10949"
entity_type: "reaction"
name: "R10949"
source_database: "KEGG"
source_id: "R10949"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R10949"
---

# R10949

`reaction.R10949`

## Static

- Type: `reaction`
- Source: `KEGG:R10949`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Ammonia + Carboxyphosphate Carbamate + Orthophosphate

## Biological Role

Catalyzed by carB (protein.P00968), carA (protein.P0A6F1). Substrates: Ammonia (molecule.C00014). Products: Orthophosphate (molecule.C00009), Carbamate (molecule.C01563).

## Annotation

Ammonia + Carboxyphosphate <=> Carbamate + Orthophosphate

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P00968|protein.P00968]] `KEGG` `database` - via EC:6.3.5.5
- `catalyzes` <-- [[protein.P0A6F1|protein.P0A6F1]] `KEGG` `database` - via EC:6.3.5.5
- `is_product_of` <-- [[molecule.C00009|molecule.C00009]] `KEGG` `database` - C00014 + C20969 <=> C01563 + C00009
- `is_product_of` <-- [[molecule.C01563|molecule.C01563]] `KEGG` `database` - C00014 + C20969 <=> C01563 + C00009
- `is_substrate_of` <-- [[molecule.C00014|molecule.C00014]] `KEGG` `database` - C00014 + C20969 <=> C01563 + C00009

## External IDs

- `KEGG:R10949`

## Notes

EQUATION: C00014 + C20969 <=> C01563 + C00009
