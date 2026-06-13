---
entity_id: "reaction.R03758"
entity_type: "reaction"
name: "R03758"
source_database: "KEGG"
source_id: "R03758"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R03758"
---

# R03758

`reaction.R03758`

## Static

- Type: `reaction`
- Source: `KEGG:R03758`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Aminoacetone + CO2 L-2-Amino-3-oxobutanoic acid

## Biological Role

Catalyzed by ydfG (protein.P39831). Substrates: CO2 (molecule.C00011), Aminoacetone (molecule.C01888). Products: L-2-Amino-3-oxobutanoic acid (molecule.C03508).

## Annotation

Aminoacetone + CO2 <=> L-2-Amino-3-oxobutanoic acid

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[protein.P39831|protein.P39831]] `KEGG` `database` - via EC:1.1.1.381
- `is_product_of` <-- [[molecule.C03508|molecule.C03508]] `KEGG` `database` - C01888 + C00011 <=> C03508
- `is_substrate_of` <-- [[molecule.C00011|molecule.C00011]] `KEGG` `database` - C01888 + C00011 <=> C03508
- `is_substrate_of` <-- [[molecule.C01888|molecule.C01888]] `KEGG` `database` - C01888 + C00011 <=> C03508

## External IDs

- `KEGG:R03758`

## Notes

EQUATION: C01888 + C00011 <=> C03508
