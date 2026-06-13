---
entity_id: "reaction.R00621"
entity_type: "reaction"
name: "R00621"
source_database: "KEGG"
source_id: "R00621"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00621"
---

# R00621

`reaction.R00621`

## Static

- Type: `reaction`
- Source: `KEGG:R00621`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

2-Oxoglutarate + Thiamin diphosphate 3-Carboxy-1-hydroxypropyl-ThPP + CO2

## Biological Role

Catalyzed by sucA (protein.P0AFG3). Substrates: 2-Oxoglutarate (molecule.C00026), Thiamin diphosphate (molecule.C00068). Products: CO2 (molecule.C00011), 3-Carboxy-1-hydroxypropyl-ThPP (molecule.C05381).

## Annotation

2-Oxoglutarate + Thiamin diphosphate <=> 3-Carboxy-1-hydroxypropyl-ThPP + CO2

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P0AFG3|protein.P0AFG3]] `KEGG` `database` - via EC:1.2.4.2
- `is_product_of` <-- [[molecule.C00011|molecule.C00011]] `KEGG` `database` - C00026 + C00068 <=> C05381 + C00011
- `is_product_of` <-- [[molecule.C05381|molecule.C05381]] `KEGG` `database` - C00026 + C00068 <=> C05381 + C00011
- `is_substrate_of` <-- [[molecule.C00026|molecule.C00026]] `KEGG` `database` - C00026 + C00068 <=> C05381 + C00011
- `is_substrate_of` <-- [[molecule.C00068|molecule.C00068]] `KEGG` `database` - C00026 + C00068 <=> C05381 + C00011

## External IDs

- `KEGG:R00621`

## Notes

EQUATION: C00026 + C00068 <=> C05381 + C00011
