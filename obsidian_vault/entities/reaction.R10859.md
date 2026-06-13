---
entity_id: "reaction.R10859"
entity_type: "reaction"
name: "(E)-4-hydroxy-3-methylbut-2-en-1-yl-diphosphate:oxidized flavodoxin oxidoreductase"
source_database: "KEGG"
source_id: "R10859"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R10859"
---

# (E)-4-hydroxy-3-methylbut-2-en-1-yl-diphosphate:oxidized flavodoxin oxidoreductase

`reaction.R10859`

## Static

- Type: `reaction`
- Source: `KEGG:R10859`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

1-Hydroxy-2-methyl-2-butenyl 4-diphosphate + H2O + Oxidized flavodoxin 2-C-Methyl-D-erythritol 2,4-cyclodiphosphate + Reduced flavodoxin

## Biological Role

Catalyzed by ispG (protein.P62620). Substrates: H2O (molecule.C00001), 1-Hydroxy-2-methyl-2-butenyl 4-diphosphate (molecule.C11811). Products: 2-C-Methyl-D-erythritol 2,4-cyclodiphosphate (molecule.C11453).

## Annotation

1-Hydroxy-2-methyl-2-butenyl 4-diphosphate + H2O + Oxidized flavodoxin <=> 2-C-Methyl-D-erythritol 2,4-cyclodiphosphate + Reduced flavodoxin

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[protein.P62620|protein.P62620]] `KEGG` `database` - via EC:1.17.7.3
- `is_product_of` <-- [[molecule.C11453|molecule.C11453]] `KEGG` `database` - C11811 + C00001 + C02869 <=> C11453 + C02745
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C11811 + C00001 + C02869 <=> C11453 + C02745
- `is_substrate_of` <-- [[molecule.C11811|molecule.C11811]] `KEGG` `database` - C11811 + C00001 + C02869 <=> C11453 + C02745

## External IDs

- `KEGG:R10859`

## Notes

EQUATION: C11811 + C00001 + C02869 <=> C11453 + C02745
