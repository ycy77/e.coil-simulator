---
entity_id: "reaction.R00354"
entity_type: "reaction"
name: "(3S)-citryl-CoA oxaloacetate-lyase (acetyl-CoA-forming)"
source_database: "KEGG"
source_id: "R00354"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00354"
---

# (3S)-citryl-CoA oxaloacetate-lyase (acetyl-CoA-forming)

`reaction.R00354`

## Static

- Type: `reaction`
- Source: `KEGG:R00354`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

(3S)-Citryl-CoA Acetyl-CoA + Oxaloacetate

## Biological Role

Catalyzed by citE (protein.P0A9I1). Substrates: (3S)-Citryl-CoA (molecule.C00566). Products: Acetyl-CoA (molecule.C00024), Oxaloacetate (molecule.C00036).

## Annotation

(3S)-Citryl-CoA <=> Acetyl-CoA + Oxaloacetate

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[protein.P0A9I1|protein.P0A9I1]] `KEGG` `database` - via EC:4.1.3.34
- `is_product_of` <-- [[molecule.C00024|molecule.C00024]] `KEGG` `database` - C00566 <=> C00024 + C00036
- `is_product_of` <-- [[molecule.C00036|molecule.C00036]] `KEGG` `database` - C00566 <=> C00024 + C00036
- `is_substrate_of` <-- [[molecule.C00566|molecule.C00566]] `KEGG` `database` - C00566 <=> C00024 + C00036

## External IDs

- `KEGG:R00354`

## Notes

EQUATION: C00566 <=> C00024 + C00036
