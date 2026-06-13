---
entity_id: "reaction.R00669"
entity_type: "reaction"
name: "N2-acetyl-L-ornithine amidohydrolase"
source_database: "KEGG"
source_id: "R00669"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00669"
---

# N2-acetyl-L-ornithine amidohydrolase

`reaction.R00669`

## Static

- Type: `reaction`
- Source: `KEGG:R00669`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

N-Acetylornithine + H2O Acetate + L-Ornithine

## Biological Role

Catalyzed by argE (protein.P23908). Substrates: H2O (molecule.C00001), N-Acetylornithine (molecule.C00437). Products: Acetate (molecule.C00033), L-Ornithine (molecule.C00077).

## Annotation

N-Acetylornithine + H2O <=> Acetate + L-Ornithine

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P23908|protein.P23908]] `KEGG` `database` - via EC:3.5.1.16
- `is_product_of` <-- [[molecule.C00033|molecule.C00033]] `KEGG` `database` - C00437 + C00001 <=> C00033 + C00077
- `is_product_of` <-- [[molecule.C00077|molecule.C00077]] `KEGG` `database` - C00437 + C00001 <=> C00033 + C00077
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C00437 + C00001 <=> C00033 + C00077
- `is_substrate_of` <-- [[molecule.C00437|molecule.C00437]] `KEGG` `database` - C00437 + C00001 <=> C00033 + C00077

## External IDs

- `KEGG:R00669`

## Notes

EQUATION: C00437 + C00001 <=> C00033 + C00077
