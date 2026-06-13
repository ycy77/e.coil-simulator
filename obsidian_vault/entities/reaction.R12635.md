---
entity_id: "reaction.R12635"
entity_type: "reaction"
name: "N4-acetylcytidine amidohydrolase"
source_database: "KEGG"
source_id: "R12635"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R12635"
---

# N4-acetylcytidine amidohydrolase

`reaction.R12635`

## Static

- Type: `reaction`
- Source: `KEGG:R12635`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

N4-Acetylcytidine + H2O Cytidine + Acetate

## Biological Role

Catalyzed by yqfB (protein.P67603). Substrates: H2O (molecule.C00001). Products: Acetate (molecule.C00033), Cytidine (molecule.C00475).

## Annotation

N4-Acetylcytidine + H2O <=> Cytidine + Acetate

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[protein.P67603|protein.P67603]] `KEGG` `database` - via EC:3.5.1.135
- `is_product_of` <-- [[molecule.C00033|molecule.C00033]] `KEGG` `database` - C22293 + C00001 <=> C00475 + C00033
- `is_product_of` <-- [[molecule.C00475|molecule.C00475]] `KEGG` `database` - C22293 + C00001 <=> C00475 + C00033
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C22293 + C00001 <=> C00475 + C00033

## External IDs

- `KEGG:R12635`

## Notes

EQUATION: C22293 + C00001 <=> C00475 + C00033
