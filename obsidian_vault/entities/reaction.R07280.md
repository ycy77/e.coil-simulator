---
entity_id: "reaction.R07280"
entity_type: "reaction"
name: "5-amino-6-(5-phospho-D-ribitylamino)uracil phosphohydrolase"
source_database: "KEGG"
source_id: "R07280"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R07280"
---

# 5-amino-6-(5-phospho-D-ribitylamino)uracil phosphohydrolase

`reaction.R07280`

## Static

- Type: `reaction`
- Source: `KEGG:R07280`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

5-Amino-6-(5'-phospho-D-ribitylamino)uracil + H2O 5-Amino-6-(1-D-ribitylamino)uracil + Orthophosphate

## Biological Role

Catalyzed by yigB (protein.P0ADP0), ybjI (protein.P75809). Substrates: H2O (molecule.C00001), 5-Amino-6-(5'-phospho-D-ribitylamino)uracil (molecule.C04454). Products: Orthophosphate (molecule.C00009), 5-Amino-6-(1-D-ribitylamino)uracil (molecule.C04732).

## Annotation

5-Amino-6-(5'-phospho-D-ribitylamino)uracil + H2O <=> 5-Amino-6-(1-D-ribitylamino)uracil + Orthophosphate

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P0ADP0|protein.P0ADP0]] `KEGG` `database` - via EC:3.1.3.104
- `catalyzes` <-- [[protein.P75809|protein.P75809]] `KEGG` `database` - via EC:3.1.3.104
- `is_product_of` <-- [[molecule.C00009|molecule.C00009]] `KEGG` `database` - C04454 + C00001 <=> C04732 + C00009
- `is_product_of` <-- [[molecule.C04732|molecule.C04732]] `KEGG` `database` - C04454 + C00001 <=> C04732 + C00009
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C04454 + C00001 <=> C04732 + C00009
- `is_substrate_of` <-- [[molecule.C04454|molecule.C04454]] `KEGG` `database` - C04454 + C00001 <=> C04732 + C00009

## External IDs

- `KEGG:R07280`

## Notes

EQUATION: C04454 + C00001 <=> C04732 + C00009
