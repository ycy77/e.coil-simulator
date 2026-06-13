---
entity_id: "reaction.R00508"
entity_type: "reaction"
name: "3'-phospho-5'-adenylyl sulfate 3'-phosphohydrolase"
source_database: "KEGG"
source_id: "R00508"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00508"
---

# 3'-phospho-5'-adenylyl sulfate 3'-phosphohydrolase

`reaction.R00508`

## Static

- Type: `reaction`
- Source: `KEGG:R00508`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

3'-Phosphoadenylyl sulfate + H2O Adenylyl sulfate + Orthophosphate

## Biological Role

Catalyzed by cysQ (protein.P22255). Substrates: H2O (molecule.C00001), 3'-Phosphoadenylyl sulfate (molecule.C00053). Products: Orthophosphate (molecule.C00009), Adenylyl sulfate (molecule.C00224).

## Annotation

3'-Phosphoadenylyl sulfate + H2O <=> Adenylyl sulfate + Orthophosphate

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P22255|protein.P22255]] `KEGG` `database` - via EC:3.1.3.7
- `is_product_of` <-- [[molecule.C00009|molecule.C00009]] `KEGG` `database` - C00053 + C00001 <=> C00224 + C00009
- `is_product_of` <-- [[molecule.C00224|molecule.C00224]] `KEGG` `database` - C00053 + C00001 <=> C00224 + C00009
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C00053 + C00001 <=> C00224 + C00009
- `is_substrate_of` <-- [[molecule.C00053|molecule.C00053]] `KEGG` `database` - C00053 + C00001 <=> C00224 + C00009

## External IDs

- `KEGG:R00508`

## Notes

EQUATION: C00053 + C00001 <=> C00224 + C00009
