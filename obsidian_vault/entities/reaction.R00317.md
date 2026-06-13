---
entity_id: "reaction.R00317"
entity_type: "reaction"
name: "acetyl phosphate phosphohydrolase"
source_database: "KEGG"
source_id: "R00317"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00317"
---

# acetyl phosphate phosphohydrolase

`reaction.R00317`

## Static

- Type: `reaction`
- Source: `KEGG:R00317`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Acetyl phosphate + H2O Acetate + Orthophosphate

## Biological Role

Catalyzed by yccX (protein.P0AB65). Substrates: H2O (molecule.C00001), Acetyl phosphate (molecule.C00227). Products: Orthophosphate (molecule.C00009), Acetate (molecule.C00033).

## Annotation

Acetyl phosphate + H2O <=> Acetate + Orthophosphate

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P0AB65|protein.P0AB65]] `KEGG` `database` - via EC:3.6.1.7
- `is_product_of` <-- [[molecule.C00009|molecule.C00009]] `KEGG` `database` - C00227 + C00001 <=> C00033 + C00009
- `is_product_of` <-- [[molecule.C00033|molecule.C00033]] `KEGG` `database` - C00227 + C00001 <=> C00033 + C00009
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C00227 + C00001 <=> C00033 + C00009
- `is_substrate_of` <-- [[molecule.C00227|molecule.C00227]] `KEGG` `database` - C00227 + C00001 <=> C00033 + C00009

## External IDs

- `KEGG:R00317`

## Notes

EQUATION: C00227 + C00001 <=> C00033 + C00009
