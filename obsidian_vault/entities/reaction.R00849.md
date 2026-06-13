---
entity_id: "reaction.R00849"
entity_type: "reaction"
name: "sn-glycerol 3-phosphate:quinone oxidoreductase"
source_database: "KEGG"
source_id: "R00849"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00849"
---

# sn-glycerol 3-phosphate:quinone oxidoreductase

`reaction.R00849`

## Static

- Type: `reaction`
- Source: `KEGG:R00849`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

sn-Glycerol 3-phosphate + Quinone Glycerone phosphate + Hydroquinone

## Biological Role

Catalyzed by glpA (protein.P0A9C0), glpB (protein.P13033), glpD (protein.P13035). Substrates: sn-Glycerol 3-phosphate (molecule.C00093). Products: Glycerone phosphate (molecule.C00111).

## Annotation

sn-Glycerol 3-phosphate + Quinone <=> Glycerone phosphate + Hydroquinone

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P0A9C0|protein.P0A9C0]] `KEGG` `database` - via EC:1.1.5.3
- `catalyzes` <-- [[protein.P13033|protein.P13033]] `KEGG` `database` - via EC:1.1.5.3
- `catalyzes` <-- [[protein.P13035|protein.P13035]] `KEGG` `database` - via EC:1.1.5.3
- `is_product_of` <-- [[molecule.C00111|molecule.C00111]] `KEGG` `database` - C00093 + C15602 <=> C00111 + C15603
- `is_substrate_of` <-- [[molecule.C00093|molecule.C00093]] `KEGG` `database` - C00093 + C15602 <=> C00111 + C15603

## External IDs

- `KEGG:R00849`

## Notes

EQUATION: C00093 + C15602 <=> C00111 + C15603
