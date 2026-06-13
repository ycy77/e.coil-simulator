---
entity_id: "reaction.R00462"
entity_type: "reaction"
name: "L-lysine carboxy-lyase (cadaverine-forming)"
source_database: "KEGG"
source_id: "R00462"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00462"
---

# L-lysine carboxy-lyase (cadaverine-forming)

`reaction.R00462`

## Static

- Type: `reaction`
- Source: `KEGG:R00462`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

L-Lysine Cadaverine + CO2

## Biological Role

Catalyzed by cadA (protein.P0A9H3), ldcC (protein.P52095). Substrates: L-Lysine (molecule.C00047). Products: CO2 (molecule.C00011), Cadaverine (molecule.C01672).

## Annotation

L-Lysine <=> Cadaverine + CO2

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P0A9H3|protein.P0A9H3]] `KEGG` `database` - via EC:4.1.1.18
- `catalyzes` <-- [[protein.P52095|protein.P52095]] `KEGG` `database` - via EC:4.1.1.18
- `is_product_of` <-- [[molecule.C00011|molecule.C00011]] `KEGG` `database` - C00047 <=> C01672 + C00011
- `is_product_of` <-- [[molecule.C01672|molecule.C01672]] `KEGG` `database` - C00047 <=> C01672 + C00011
- `is_substrate_of` <-- [[molecule.C00047|molecule.C00047]] `KEGG` `database` - C00047 <=> C01672 + C00011

## External IDs

- `KEGG:R00462`

## Notes

EQUATION: C00047 <=> C01672 + C00011
