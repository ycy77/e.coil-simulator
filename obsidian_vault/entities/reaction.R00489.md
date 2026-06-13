---
entity_id: "reaction.R00489"
entity_type: "reaction"
name: "L-aspartate 1-carboxy-lyase (beta-alanine-forming)"
source_database: "KEGG"
source_id: "R00489"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00489"
---

# L-aspartate 1-carboxy-lyase (beta-alanine-forming)

`reaction.R00489`

## Static

- Type: `reaction`
- Source: `KEGG:R00489`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

L-Aspartate beta-Alanine + CO2

## Biological Role

Catalyzed by panD (protein.P0A790), gadA (protein.P69908), gadB (protein.P69910). Substrates: L-Aspartate (molecule.C00049). Products: CO2 (molecule.C00011), beta-Alanine (molecule.C00099).

## Annotation

L-Aspartate <=> beta-Alanine + CO2

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P0A790|protein.P0A790]] `KEGG` `database` - via EC:4.1.1.11
- `catalyzes` <-- [[protein.P69908|protein.P69908]] `KEGG` `database` - via EC:4.1.1.15
- `catalyzes` <-- [[protein.P69910|protein.P69910]] `KEGG` `database` - via EC:4.1.1.15
- `is_product_of` <-- [[molecule.C00011|molecule.C00011]] `KEGG` `database` - C00049 <=> C00099 + C00011
- `is_product_of` <-- [[molecule.C00099|molecule.C00099]] `KEGG` `database` - C00049 <=> C00099 + C00011
- `is_substrate_of` <-- [[molecule.C00049|molecule.C00049]] `KEGG` `database` - C00049 <=> C00099 + C00011

## External IDs

- `KEGG:R00489`

## Notes

EQUATION: C00049 <=> C00099 + C00011
