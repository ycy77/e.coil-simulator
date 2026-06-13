---
entity_id: "reaction.R00844"
entity_type: "reaction"
name: "sn-glycerol-3-phosphate:NADP+ 2-oxidoreductase"
source_database: "KEGG"
source_id: "R00844"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00844"
---

# sn-glycerol-3-phosphate:NADP+ 2-oxidoreductase

`reaction.R00844`

## Static

- Type: `reaction`
- Source: `KEGG:R00844`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

sn-Glycerol 3-phosphate + NADP+ Glycerone phosphate + NADPH + H+

## Biological Role

Catalyzed by gpsA (protein.P0A6S7). Substrates: NADP+ (molecule.C00006), sn-Glycerol 3-phosphate (molecule.C00093). Products: NADPH (molecule.C00005), H+ (molecule.C00080), Glycerone phosphate (molecule.C00111).

## Annotation

sn-Glycerol 3-phosphate + NADP+ <=> Glycerone phosphate + NADPH + H+

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P0A6S7|protein.P0A6S7]] `KEGG` `database` - via EC:1.1.1.94
- `is_product_of` <-- [[molecule.C00005|molecule.C00005]] `KEGG` `database` - C00093 + C00006 <=> C00111 + C00005 + C00080
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `KEGG` `database` - C00093 + C00006 <=> C00111 + C00005 + C00080
- `is_product_of` <-- [[molecule.C00111|molecule.C00111]] `KEGG` `database` - C00093 + C00006 <=> C00111 + C00005 + C00080
- `is_substrate_of` <-- [[molecule.C00006|molecule.C00006]] `KEGG` `database` - C00093 + C00006 <=> C00111 + C00005 + C00080
- `is_substrate_of` <-- [[molecule.C00093|molecule.C00093]] `KEGG` `database` - C00093 + C00006 <=> C00111 + C00005 + C00080

## External IDs

- `KEGG:R00844`

## Notes

EQUATION: C00093 + C00006 <=> C00111 + C00005 + C00080
