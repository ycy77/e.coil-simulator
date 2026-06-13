---
entity_id: "reaction.R00842"
entity_type: "reaction"
name: "sn-glycerol-3-phosphate:NAD+ 2-oxidoreductase"
source_database: "KEGG"
source_id: "R00842"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00842"
---

# sn-glycerol-3-phosphate:NAD+ 2-oxidoreductase

`reaction.R00842`

## Static

- Type: `reaction`
- Source: `KEGG:R00842`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

sn-Glycerol 3-phosphate + NAD+ Glycerone phosphate + NADH + H+

## Biological Role

Catalyzed by gpsA (protein.P0A6S7). Substrates: NAD+ (molecule.C00003), sn-Glycerol 3-phosphate (molecule.C00093). Products: NADH (molecule.C00004), H+ (molecule.C00080), Glycerone phosphate (molecule.C00111).

## Annotation

sn-Glycerol 3-phosphate + NAD+ <=> Glycerone phosphate + NADH + H+

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P0A6S7|protein.P0A6S7]] `KEGG` `database` - via EC:1.1.1.94
- `is_product_of` <-- [[molecule.C00004|molecule.C00004]] `KEGG` `database` - C00093 + C00003 <=> C00111 + C00004 + C00080
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `KEGG` `database` - C00093 + C00003 <=> C00111 + C00004 + C00080
- `is_product_of` <-- [[molecule.C00111|molecule.C00111]] `KEGG` `database` - C00093 + C00003 <=> C00111 + C00004 + C00080
- `is_substrate_of` <-- [[molecule.C00003|molecule.C00003]] `KEGG` `database` - C00093 + C00003 <=> C00111 + C00004 + C00080
- `is_substrate_of` <-- [[molecule.C00093|molecule.C00093]] `KEGG` `database` - C00093 + C00003 <=> C00111 + C00004 + C00080

## External IDs

- `KEGG:R00842`

## Notes

EQUATION: C00093 + C00003 <=> C00111 + C00004 + C00080
