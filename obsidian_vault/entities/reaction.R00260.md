---
entity_id: "reaction.R00260"
entity_type: "reaction"
name: "glutamate racemase"
source_database: "KEGG"
source_id: "R00260"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00260"
---

# glutamate racemase

`reaction.R00260`

## Static

- Type: `reaction`
- Source: `KEGG:R00260`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

L-Glutamate D-Glutamate

## Biological Role

Catalyzed by murI (protein.P22634). Substrates: L-Glutamate (molecule.C00025). Products: D-Glutamate (molecule.C00217).

## Annotation

L-Glutamate <=> D-Glutamate

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.P22634|protein.P22634]] `KEGG` `database` - via EC:5.1.1.3
- `is_product_of` <-- [[molecule.C00217|molecule.C00217]] `KEGG` `database` - C00025 <=> C00217
- `is_substrate_of` <-- [[molecule.C00025|molecule.C00025]] `KEGG` `database` - C00025 <=> C00217

## External IDs

- `KEGG:R00260`

## Notes

EQUATION: C00025 <=> C00217
