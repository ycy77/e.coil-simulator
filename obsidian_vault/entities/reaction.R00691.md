---
entity_id: "reaction.R00691"
entity_type: "reaction"
name: "L-arogenate hydro-lyase (decarboxylating; L-phenylalanine-forming)"
source_database: "KEGG"
source_id: "R00691"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00691"
---

# L-arogenate hydro-lyase (decarboxylating; L-phenylalanine-forming)

`reaction.R00691`

## Static

- Type: `reaction`
- Source: `KEGG:R00691`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

L-Arogenate L-Phenylalanine + H2O + CO2

## Biological Role

Catalyzed by pheA (protein.P0A9J8). Substrates: L-Arogenate (molecule.C00826). Products: H2O (molecule.C00001), CO2 (molecule.C00011), L-Phenylalanine (molecule.C00079).

## Annotation

L-Arogenate <=> L-Phenylalanine + H2O + CO2

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P0A9J8|protein.P0A9J8]] `KEGG` `database` - via EC:4.2.1.51
- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C00826 <=> C00079 + C00001 + C00011
- `is_product_of` <-- [[molecule.C00011|molecule.C00011]] `KEGG` `database` - C00826 <=> C00079 + C00001 + C00011
- `is_product_of` <-- [[molecule.C00079|molecule.C00079]] `KEGG` `database` - C00826 <=> C00079 + C00001 + C00011
- `is_substrate_of` <-- [[molecule.C00826|molecule.C00826]] `KEGG` `database` - C00826 <=> C00079 + C00001 + C00011

## External IDs

- `KEGG:R00691`

## Notes

EQUATION: C00826 <=> C00079 + C00001 + C00011
