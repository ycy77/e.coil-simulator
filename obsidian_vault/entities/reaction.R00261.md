---
entity_id: "reaction.R00261"
entity_type: "reaction"
name: "L-glutamate 1-carboxy-lyase (4-aminobutanoate-forming)"
source_database: "KEGG"
source_id: "R00261"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00261"
---

# L-glutamate 1-carboxy-lyase (4-aminobutanoate-forming)

`reaction.R00261`

## Static

- Type: `reaction`
- Source: `KEGG:R00261`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

L-Glutamate 4-Aminobutanoate + CO2

## Biological Role

Catalyzed by gadA (protein.P69908), gadB (protein.P69910). Substrates: L-Glutamate (molecule.C00025). Products: CO2 (molecule.C00011), 4-Aminobutanoate (molecule.C00334).

## Annotation

L-Glutamate <=> 4-Aminobutanoate + CO2

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P69908|protein.P69908]] `KEGG` `database` - via EC:4.1.1.15
- `catalyzes` <-- [[protein.P69910|protein.P69910]] `KEGG` `database` - via EC:4.1.1.15
- `is_product_of` <-- [[molecule.C00011|molecule.C00011]] `KEGG` `database` - C00025 <=> C00334 + C00011
- `is_product_of` <-- [[molecule.C00334|molecule.C00334]] `KEGG` `database` - C00025 <=> C00334 + C00011
- `is_substrate_of` <-- [[molecule.C00025|molecule.C00025]] `KEGG` `database` - C00025 <=> C00334 + C00011

## External IDs

- `KEGG:R00261`

## Notes

EQUATION: C00025 <=> C00334 + C00011
