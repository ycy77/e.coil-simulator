---
entity_id: "reaction.R00371"
entity_type: "reaction"
name: "acetyl-CoA:glycine C-acetyltransferase"
source_database: "KEGG"
source_id: "R00371"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00371"
---

# acetyl-CoA:glycine C-acetyltransferase

`reaction.R00371`

## Static

- Type: `reaction`
- Source: `KEGG:R00371`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Acetyl-CoA + Glycine CoA + L-2-Amino-3-oxobutanoic acid

## Biological Role

Catalyzed by kbl (protein.P0AB77). Substrates: Acetyl-CoA (molecule.C00024), Glycine (molecule.C00037). Products: CoA (molecule.C00010), L-2-Amino-3-oxobutanoic acid (molecule.C03508).

## Annotation

Acetyl-CoA + Glycine <=> CoA + L-2-Amino-3-oxobutanoic acid

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P0AB77|protein.P0AB77]] `KEGG` `database` - via EC:2.3.1.29
- `is_product_of` <-- [[molecule.C00010|molecule.C00010]] `KEGG` `database` - C00024 + C00037 <=> C00010 + C03508
- `is_product_of` <-- [[molecule.C03508|molecule.C03508]] `KEGG` `database` - C00024 + C00037 <=> C00010 + C03508
- `is_substrate_of` <-- [[molecule.C00024|molecule.C00024]] `KEGG` `database` - C00024 + C00037 <=> C00010 + C03508
- `is_substrate_of` <-- [[molecule.C00037|molecule.C00037]] `KEGG` `database` - C00024 + C00037 <=> C00010 + C03508

## External IDs

- `KEGG:R00371`

## Notes

EQUATION: C00024 + C00037 <=> C00010 + C03508
