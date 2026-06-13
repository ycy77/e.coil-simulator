---
entity_id: "reaction.R00275"
entity_type: "reaction"
name: "superoxide:superoxide oxidoreductase"
source_database: "KEGG"
source_id: "R00275"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00275"
---

# superoxide:superoxide oxidoreductase

`reaction.R00275`

## Static

- Type: `reaction`
- Source: `KEGG:R00275`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

2 Superoxide + 2 H+ Hydrogen peroxide + Oxygen

## Biological Role

Catalyzed by sodA (protein.P00448), sodC (protein.P0AGD1), sodB (protein.P0AGD3). Substrates: H+ (molecule.C00080). Products: Oxygen (molecule.C00007), Hydrogen peroxide (molecule.C00027).

## Annotation

2 Superoxide + 2 H+ <=> Hydrogen peroxide + Oxygen

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P00448|protein.P00448]] `KEGG` `database` - via EC:1.15.1.1
- `catalyzes` <-- [[protein.P0AGD1|protein.P0AGD1]] `KEGG` `database` - via EC:1.15.1.1
- `catalyzes` <-- [[protein.P0AGD3|protein.P0AGD3]] `KEGG` `database` - via EC:1.15.1.1
- `is_product_of` <-- [[molecule.C00007|molecule.C00007]] `KEGG` `database` - 2 C00704 + 2 C00080 <=> C00027 + C00007
- `is_product_of` <-- [[molecule.C00027|molecule.C00027]] `KEGG` `database` - 2 C00704 + 2 C00080 <=> C00027 + C00007
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `KEGG` `database` - 2 C00704 + 2 C00080 <=> C00027 + C00007

## External IDs

- `KEGG:R00275`

## Notes

EQUATION: 2 C00704 + 2 C00080 <=> C00027 + C00007
