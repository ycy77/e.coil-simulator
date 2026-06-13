---
entity_id: "reaction.R01323"
entity_type: "reaction"
name: "acetyl-CoA:citrate CoA-transferase"
source_database: "KEGG"
source_id: "R01323"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R01323"
---

# acetyl-CoA:citrate CoA-transferase

`reaction.R01323`

## Static

- Type: `reaction`
- Source: `KEGG:R01323`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Acetyl-CoA + Citrate Acetate + (3S)-Citryl-CoA

## Biological Role

Catalyzed by citF (protein.P75726). Substrates: Acetyl-CoA (molecule.C00024), Citrate (molecule.C00158). Products: Acetate (molecule.C00033), (3S)-Citryl-CoA (molecule.C00566).

## Annotation

Acetyl-CoA + Citrate <=> Acetate + (3S)-Citryl-CoA

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P75726|protein.P75726]] `KEGG` `database` - via EC:2.8.3.10
- `is_product_of` <-- [[molecule.C00033|molecule.C00033]] `KEGG` `database` - C00024 + C00158 <=> C00033 + C00566
- `is_product_of` <-- [[molecule.C00566|molecule.C00566]] `KEGG` `database` - C00024 + C00158 <=> C00033 + C00566
- `is_substrate_of` <-- [[molecule.C00024|molecule.C00024]] `KEGG` `database` - C00024 + C00158 <=> C00033 + C00566
- `is_substrate_of` <-- [[molecule.C00158|molecule.C00158]] `KEGG` `database` - C00024 + C00158 <=> C00033 + C00566

## External IDs

- `KEGG:R01323`

## Notes

EQUATION: C00024 + C00158 <=> C00033 + C00566
