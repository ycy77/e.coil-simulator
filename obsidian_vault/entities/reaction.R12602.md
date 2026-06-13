---
entity_id: "reaction.R12602"
entity_type: "reaction"
name: "lipoyl:hydroperoxide oxidoreductase"
source_database: "KEGG"
source_id: "R12602"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R12602"
---

# lipoyl:hydroperoxide oxidoreductase

`reaction.R12602`

## Static

- Type: `reaction`
- Source: `KEGG:R12602`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

[Protein]-N6-[(R)-dihydrolipoyl]-L-lysine + ROOH Protein N6-(lipoyl)lysine + H2O + ROH

## Biological Role

Catalyzed by osmC (protein.P0C0L2). Products: H2O (molecule.C00001).

## Annotation

[Protein]-N6-[(R)-dihydrolipoyl]-L-lysine + ROOH <=> Protein N6-(lipoyl)lysine + H2O + ROH

## Outgoing Edges (0)

_None._

## Incoming Edges (2)

- `catalyzes` <-- [[protein.P0C0L2|protein.P0C0L2]] `KEGG` `database` - via EC:1.11.1.28
- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C16832 + C15498 <=> C16237 + C00001 + C01335

## External IDs

- `KEGG:R12602`

## Notes

EQUATION: C16832 + C15498 <=> C16237 + C00001 + C01335
