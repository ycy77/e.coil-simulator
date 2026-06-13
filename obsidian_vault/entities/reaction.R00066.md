---
entity_id: "reaction.R00066"
entity_type: "reaction"
name: "6,7-dimethyl-8-(1-D-ribityl)lumazine:6,7-dimethyl-8-(1-D-ribityl)lumazine 2,3-butanediyltransferase"
source_database: "KEGG"
source_id: "R00066"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00066"
---

# 6,7-dimethyl-8-(1-D-ribityl)lumazine:6,7-dimethyl-8-(1-D-ribityl)lumazine 2,3-butanediyltransferase

`reaction.R00066`

## Static

- Type: `reaction`
- Source: `KEGG:R00066`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

2 6,7-Dimethyl-8-(D-ribityl)lumazine Riboflavin + 5-Amino-6-(1-D-ribitylamino)uracil

## Biological Role

Catalyzed by ribC (protein.P0AFU8). Substrates: 6,7-Dimethyl-8-(D-ribityl)lumazine (molecule.C04332). Products: Riboflavin (molecule.C00255), 5-Amino-6-(1-D-ribitylamino)uracil (molecule.C04732).

## Annotation

2 6,7-Dimethyl-8-(D-ribityl)lumazine <=> Riboflavin + 5-Amino-6-(1-D-ribitylamino)uracil

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[protein.P0AFU8|protein.P0AFU8]] `KEGG` `database` - via EC:2.5.1.9
- `is_product_of` <-- [[molecule.C00255|molecule.C00255]] `KEGG` `database` - 2 C04332 <=> C00255 + C04732
- `is_product_of` <-- [[molecule.C04732|molecule.C04732]] `KEGG` `database` - 2 C04332 <=> C00255 + C04732
- `is_substrate_of` <-- [[molecule.C04332|molecule.C04332]] `KEGG` `database` - 2 C04332 <=> C00255 + C04732

## External IDs

- `KEGG:R00066`

## Notes

EQUATION: 2 C04332 <=> C00255 + C04732
