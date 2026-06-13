---
entity_id: "reaction.R00451"
entity_type: "reaction"
name: "meso-2,6-diaminoheptanedioate carboxy-lyase (L-lysine-forming)"
source_database: "KEGG"
source_id: "R00451"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00451"
---

# meso-2,6-diaminoheptanedioate carboxy-lyase (L-lysine-forming)

`reaction.R00451`

## Static

- Type: `reaction`
- Source: `KEGG:R00451`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

meso-2,6-Diaminoheptanedioate L-Lysine + CO2

## Biological Role

Catalyzed by lysA (protein.P00861). Substrates: meso-2,6-Diaminoheptanedioate (molecule.C00680). Products: CO2 (molecule.C00011), L-Lysine (molecule.C00047).

## Annotation

meso-2,6-Diaminoheptanedioate <=> L-Lysine + CO2

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[protein.P00861|protein.P00861]] `KEGG` `database` - via EC:4.1.1.20
- `is_product_of` <-- [[molecule.C00011|molecule.C00011]] `KEGG` `database` - C00680 <=> C00047 + C00011
- `is_product_of` <-- [[molecule.C00047|molecule.C00047]] `KEGG` `database` - C00680 <=> C00047 + C00011
- `is_substrate_of` <-- [[molecule.C00680|molecule.C00680]] `KEGG` `database` - C00680 <=> C00047 + C00011

## External IDs

- `KEGG:R00451`

## Notes

EQUATION: C00680 <=> C00047 + C00011
