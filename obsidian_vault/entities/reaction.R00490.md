---
entity_id: "reaction.R00490"
entity_type: "reaction"
name: "L-aspartate ammonia-lyase (fumarate-forming)"
source_database: "KEGG"
source_id: "R00490"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00490"
---

# L-aspartate ammonia-lyase (fumarate-forming)

`reaction.R00490`

## Static

- Type: `reaction`
- Source: `KEGG:R00490`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

L-Aspartate Fumarate + Ammonia

## Biological Role

Catalyzed by aspA (protein.P0AC38). Substrates: L-Aspartate (molecule.C00049). Products: Ammonia (molecule.C00014), Fumarate (molecule.C00122).

## Annotation

L-Aspartate <=> Fumarate + Ammonia

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[protein.P0AC38|protein.P0AC38]] `KEGG` `database` - via EC:4.3.1.1
- `is_product_of` <-- [[molecule.C00014|molecule.C00014]] `KEGG` `database` - C00049 <=> C00122 + C00014
- `is_product_of` <-- [[molecule.C00122|molecule.C00122]] `KEGG` `database` - C00049 <=> C00122 + C00014
- `is_substrate_of` <-- [[molecule.C00049|molecule.C00049]] `KEGG` `database` - C00049 <=> C00122 + C00014

## External IDs

- `KEGG:R00490`

## Notes

EQUATION: C00049 <=> C00122 + C00014
