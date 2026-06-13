---
entity_id: "reaction.R02853"
entity_type: "reaction"
name: "D-O-phosphoserine phosphohydrolase"
source_database: "KEGG"
source_id: "R02853"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R02853"
---

# D-O-phosphoserine phosphohydrolase

`reaction.R02853`

## Static

- Type: `reaction`
- Source: `KEGG:R02853`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

O-Phospho-D-serine + H2O D-Serine + Orthophosphate

## Biological Role

Catalyzed by serB (protein.P0AGB0). Substrates: H2O (molecule.C00001). Products: Orthophosphate (molecule.C00009), D-Serine (molecule.C00740).

## Annotation

O-Phospho-D-serine + H2O <=> D-Serine + Orthophosphate

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[protein.P0AGB0|protein.P0AGB0]] `KEGG` `database` - via EC:3.1.3.3
- `is_product_of` <-- [[molecule.C00009|molecule.C00009]] `KEGG` `database` - C02532 + C00001 <=> C00740 + C00009
- `is_product_of` <-- [[molecule.C00740|molecule.C00740]] `KEGG` `database` - C02532 + C00001 <=> C00740 + C00009
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C02532 + C00001 <=> C00740 + C00009

## External IDs

- `KEGG:R02853`

## Notes

EQUATION: C02532 + C00001 <=> C00740 + C00009
