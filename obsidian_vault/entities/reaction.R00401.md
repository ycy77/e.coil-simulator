---
entity_id: "reaction.R00401"
entity_type: "reaction"
name: "alanine racemase"
source_database: "KEGG"
source_id: "R00401"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00401"
---

# alanine racemase

`reaction.R00401`

## Static

- Type: `reaction`
- Source: `KEGG:R00401`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

L-Alanine D-Alanine

## Biological Role

Catalyzed by alr (protein.P0A6B4), dadX (protein.P29012). Substrates: L-Alanine (molecule.C00041). Products: D-Alanine (molecule.C00133).

## Annotation

L-Alanine <=> D-Alanine

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[protein.P0A6B4|protein.P0A6B4]] `KEGG` `database` - via EC:5.1.1.1
- `catalyzes` <-- [[protein.P29012|protein.P29012]] `KEGG` `database` - via EC:5.1.1.1
- `is_product_of` <-- [[molecule.C00133|molecule.C00133]] `KEGG` `database` - C00041 <=> C00133
- `is_substrate_of` <-- [[molecule.C00041|molecule.C00041]] `KEGG` `database` - C00041 <=> C00133

## External IDs

- `KEGG:R00401`

## Notes

EQUATION: C00041 <=> C00133
