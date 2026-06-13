---
entity_id: "reaction.R12603"
entity_type: "reaction"
name: "lipoyl:hydroperoxide oxidoreductase"
source_database: "KEGG"
source_id: "R12603"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R12603"
---

# lipoyl:hydroperoxide oxidoreductase

`reaction.R12603`

## Static

- Type: `reaction`
- Source: `KEGG:R12603`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Enzyme N6-(dihydrolipoyl)lysine + ROOH Enzyme N6-(lipoyl)lysine + H2O + ROH

## Biological Role

Catalyzed by osmC (protein.P0C0L2). Substrates: Enzyme N6-(dihydrolipoyl)lysine (molecule.C15973). Products: H2O (molecule.C00001), Enzyme N6-(lipoyl)lysine (molecule.C15972).

## Annotation

Enzyme N6-(dihydrolipoyl)lysine + ROOH <=> Enzyme N6-(lipoyl)lysine + H2O + ROH

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[protein.P0C0L2|protein.P0C0L2]] `KEGG` `database` - via EC:1.11.1.28
- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C15973 + C15498 <=> C15972 + C00001 + C01335
- `is_product_of` <-- [[molecule.C15972|molecule.C15972]] `KEGG` `database` - C15973 + C15498 <=> C15972 + C00001 + C01335
- `is_substrate_of` <-- [[molecule.C15973|molecule.C15973]] `KEGG` `database` - C15973 + C15498 <=> C15972 + C00001 + C01335

## External IDs

- `KEGG:R12603`

## Notes

EQUATION: C15973 + C15498 <=> C15972 + C00001 + C01335
