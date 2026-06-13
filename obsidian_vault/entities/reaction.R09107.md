---
entity_id: "reaction.R09107"
entity_type: "reaction"
name: "N-acetyl-L-citrulline amidohydrolase"
source_database: "KEGG"
source_id: "R09107"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R09107"
---

# N-acetyl-L-citrulline amidohydrolase

`reaction.R09107`

## Static

- Type: `reaction`
- Source: `KEGG:R09107`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

N-Acetyl-L-citrulline + H2O Acetate + L-Citrulline

## Biological Role

Catalyzed by argE (protein.P23908). Substrates: H2O (molecule.C00001), N-Acetyl-L-citrulline (molecule.C15532). Products: Acetate (molecule.C00033), L-Citrulline (molecule.C00327).

## Annotation

N-Acetyl-L-citrulline + H2O <=> Acetate + L-Citrulline

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P23908|protein.P23908]] `KEGG` `database` - via EC:3.5.1.16
- `is_product_of` <-- [[molecule.C00033|molecule.C00033]] `KEGG` `database` - C15532 + C00001 <=> C00033 + C00327
- `is_product_of` <-- [[molecule.C00327|molecule.C00327]] `KEGG` `database` - C15532 + C00001 <=> C00033 + C00327
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C15532 + C00001 <=> C00033 + C00327
- `is_substrate_of` <-- [[molecule.C15532|molecule.C15532]] `KEGG` `database` - C15532 + C00001 <=> C00033 + C00327

## External IDs

- `KEGG:R09107`

## Notes

EQUATION: C15532 + C00001 <=> C00033 + C00327
