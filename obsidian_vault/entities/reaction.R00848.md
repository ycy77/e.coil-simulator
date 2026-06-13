---
entity_id: "reaction.R00848"
entity_type: "reaction"
name: "sn-glycerol-3-phosphate:(acceptor) 2-oxidoreductase"
source_database: "KEGG"
source_id: "R00848"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00848"
---

# sn-glycerol-3-phosphate:(acceptor) 2-oxidoreductase

`reaction.R00848`

## Static

- Type: `reaction`
- Source: `KEGG:R00848`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

sn-Glycerol 3-phosphate + FAD Glycerone phosphate + FADH2

## Biological Role

Catalyzed by glpA (protein.P0A9C0), glpB (protein.P13033), glpD (protein.P13035). Substrates: FAD (molecule.C00016), sn-Glycerol 3-phosphate (molecule.C00093). Products: Glycerone phosphate (molecule.C00111), FADH2 (molecule.C01352).

## Annotation

sn-Glycerol 3-phosphate + FAD <=> Glycerone phosphate + FADH2

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[protein.P0A9C0|protein.P0A9C0]] `KEGG` `database` - via EC:1.1.5.3
- `catalyzes` <-- [[protein.P13033|protein.P13033]] `KEGG` `database` - via EC:1.1.5.3
- `catalyzes` <-- [[protein.P13035|protein.P13035]] `KEGG` `database` - via EC:1.1.5.3
- `is_product_of` <-- [[molecule.C00111|molecule.C00111]] `KEGG` `database` - C00093 + C00016 <=> C00111 + C01352
- `is_product_of` <-- [[molecule.C01352|molecule.C01352]] `KEGG` `database` - C00093 + C00016 <=> C00111 + C01352
- `is_substrate_of` <-- [[molecule.C00016|molecule.C00016]] `KEGG` `database` - C00093 + C00016 <=> C00111 + C01352
- `is_substrate_of` <-- [[molecule.C00093|molecule.C00093]] `KEGG` `database` - C00093 + C00016 <=> C00111 + C01352

## External IDs

- `KEGG:R00848`

## Notes

EQUATION: C00093 + C00016 <=> C00111 + C01352
