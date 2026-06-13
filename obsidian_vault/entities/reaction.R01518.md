---
entity_id: "reaction.R01518"
entity_type: "reaction"
name: "D-phosphoglycerate 2,3-phosphomutase"
source_database: "KEGG"
source_id: "R01518"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R01518"
---

# D-phosphoglycerate 2,3-phosphomutase

`reaction.R01518`

## Static

- Type: `reaction`
- Source: `KEGG:R01518`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

2-Phospho-D-glycerate 3-Phospho-D-glycerate

## Biological Role

Catalyzed by gpmB (protein.P0A7A2), gpmI (protein.P37689), gpmA (protein.P62707). Substrates: 2-Phospho-D-glycerate (molecule.C00631). Products: 3-Phospho-D-glycerate (molecule.C00197).

## Annotation

2-Phospho-D-glycerate <=> 3-Phospho-D-glycerate

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P0A7A2|protein.P0A7A2]] `KEGG` `database` - via EC:5.4.2.11
- `catalyzes` <-- [[protein.P37689|protein.P37689]] `KEGG` `database` - via EC:5.4.2.12
- `catalyzes` <-- [[protein.P62707|protein.P62707]] `KEGG` `database` - via EC:5.4.2.11
- `is_product_of` <-- [[molecule.C00197|molecule.C00197]] `KEGG` `database` - C00631 <=> C00197
- `is_substrate_of` <-- [[molecule.C00631|molecule.C00631]] `KEGG` `database` - C00631 <=> C00197

## External IDs

- `KEGG:R01518`

## Notes

EQUATION: C00631 <=> C00197
