---
entity_id: "reaction.R06179"
entity_type: "reaction"
name: "R06179"
source_database: "KEGG"
source_id: "R06179"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R06179"
---

# R06179

`reaction.R06179`

## Static

- Type: `reaction`
- Source: `KEGG:R06179`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

G10553 + G10554(n) di-trans,poly-cis-Undecaprenyl diphosphate + G10554(n+1)

## Biological Role

Catalyzed by mrcA (protein.P02918), mrcB (protein.P02919), ftsW (protein.P0ABG4), mrdB (protein.P0ABG7), mtgA (protein.P46022), pbpC (protein.P76577). Products: di-trans,poly-cis-Undecaprenyl diphosphate (molecule.C04574).

## Annotation

G10553 + G10554(n) <=> di-trans,poly-cis-Undecaprenyl diphosphate + G10554(n+1)

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[protein.P02918|protein.P02918]] `KEGG` `database` - via EC:2.4.99.28
- `catalyzes` <-- [[protein.P02919|protein.P02919]] `KEGG` `database` - via EC:2.4.99.28
- `catalyzes` <-- [[protein.P0ABG4|protein.P0ABG4]] `KEGG` `database` - via EC:2.4.99.28
- `catalyzes` <-- [[protein.P0ABG7|protein.P0ABG7]] `KEGG` `database` - via EC:2.4.99.28
- `catalyzes` <-- [[protein.P46022|protein.P46022]] `KEGG` `database` - via EC:2.4.99.28
- `catalyzes` <-- [[protein.P76577|protein.P76577]] `KEGG` `database` - via EC:2.4.99.28
- `is_product_of` <-- [[molecule.C04574|molecule.C04574]] `KEGG` `database` - G10553 + G10554(n) <=> C04574 + G10554(n+1)

## External IDs

- `KEGG:R06179`

## Notes

EQUATION: G10553 + G10554(n) <=> C04574 + G10554(n+1)
