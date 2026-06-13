---
entity_id: "reaction.R05837"
entity_type: "reaction"
name: "4-(phosphonooxy)threonine:NAD oxidoreductase"
source_database: "KEGG"
source_id: "R05837"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R05837"
---

# 4-(phosphonooxy)threonine:NAD oxidoreductase

`reaction.R05837`

## Static

- Type: `reaction`
- Source: `KEGG:R05837`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

O-Phospho-4-hydroxy-L-threonine + NAD+ 3-Amino-2-oxopropyl phosphate + NADH + H+ + CO2

## Biological Role

Catalyzed by pdxA (protein.P19624). Substrates: NAD+ (molecule.C00003), O-Phospho-4-hydroxy-L-threonine (molecule.C06055). Products: NADH (molecule.C00004), CO2 (molecule.C00011), H+ (molecule.C00080), 3-Amino-2-oxopropyl phosphate (molecule.C11638).

## Annotation

O-Phospho-4-hydroxy-L-threonine + NAD+ <=> 3-Amino-2-oxopropyl phosphate + NADH + H+ + CO2

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[protein.P19624|protein.P19624]] `KEGG` `database` - via EC:1.1.1.262
- `is_product_of` <-- [[molecule.C00004|molecule.C00004]] `KEGG` `database` - C06055 + C00003 <=> C11638 + C00004 + C00080 + C00011
- `is_product_of` <-- [[molecule.C00011|molecule.C00011]] `KEGG` `database` - C06055 + C00003 <=> C11638 + C00004 + C00080 + C00011
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `KEGG` `database` - C06055 + C00003 <=> C11638 + C00004 + C00080 + C00011
- `is_product_of` <-- [[molecule.C11638|molecule.C11638]] `KEGG` `database` - C06055 + C00003 <=> C11638 + C00004 + C00080 + C00011
- `is_substrate_of` <-- [[molecule.C00003|molecule.C00003]] `KEGG` `database` - C06055 + C00003 <=> C11638 + C00004 + C00080 + C00011
- `is_substrate_of` <-- [[molecule.C06055|molecule.C06055]] `KEGG` `database` - C06055 + C00003 <=> C11638 + C00004 + C00080 + C00011

## External IDs

- `KEGG:R05837`

## Notes

EQUATION: C06055 + C00003 <=> C11638 + C00004 + C00080 + C00011
