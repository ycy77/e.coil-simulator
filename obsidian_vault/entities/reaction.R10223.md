---
entity_id: "reaction.R10223"
entity_type: "reaction"
name: "tRNA(adenine34) aminohydrolase"
source_database: "KEGG"
source_id: "R10223"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R10223"
---

# tRNA(adenine34) aminohydrolase

`reaction.R10223`

## Static

- Type: `reaction`
- Source: `KEGG:R10223`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

tRNA adenine + H2O tRNA hypoxanthine + Ammonia

## Biological Role

Catalyzed by tadA (protein.P68398). Substrates: H2O (molecule.C00001). Products: Ammonia (molecule.C00014).

## Annotation

tRNA adenine + H2O <=> tRNA hypoxanthine + Ammonia

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.P68398|protein.P68398]] `KEGG` `database` - via EC:3.5.4.33
- `is_product_of` <-- [[molecule.C00014|molecule.C00014]] `KEGG` `database` - C17324 + C00001 <=> C20451 + C00014
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C17324 + C00001 <=> C20451 + C00014

## External IDs

- `KEGG:R10223`

## Notes

EQUATION: C17324 + C00001 <=> C20451 + C00014
