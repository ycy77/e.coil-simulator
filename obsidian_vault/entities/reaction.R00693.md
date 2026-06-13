---
entity_id: "reaction.R00693"
entity_type: "reaction"
name: "acetyl-CoA:L-phenylalanine N-acetyltransferase"
source_database: "KEGG"
source_id: "R00693"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00693"
---

# acetyl-CoA:L-phenylalanine N-acetyltransferase

`reaction.R00693`

## Static

- Type: `reaction`
- Source: `KEGG:R00693`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Acetyl-CoA + L-Phenylalanine CoA + N-Acetyl-L-phenylalanine

## Biological Role

Catalyzed by aaaT (protein.P46854). Substrates: Acetyl-CoA (molecule.C00024), L-Phenylalanine (molecule.C00079). Products: CoA (molecule.C00010), N-Acetyl-L-phenylalanine (molecule.C03519).

## Annotation

Acetyl-CoA + L-Phenylalanine <=> CoA + N-Acetyl-L-phenylalanine

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P46854|protein.P46854]] `KEGG` `database` - via EC:2.3.1.53
- `is_product_of` <-- [[molecule.C00010|molecule.C00010]] `KEGG` `database` - C00024 + C00079 <=> C00010 + C03519
- `is_product_of` <-- [[molecule.C03519|molecule.C03519]] `KEGG` `database` - C00024 + C00079 <=> C00010 + C03519
- `is_substrate_of` <-- [[molecule.C00024|molecule.C00024]] `KEGG` `database` - C00024 + C00079 <=> C00010 + C03519
- `is_substrate_of` <-- [[molecule.C00079|molecule.C00079]] `KEGG` `database` - C00024 + C00079 <=> C00010 + C03519

## External IDs

- `KEGG:R00693`

## Notes

EQUATION: C00024 + C00079 <=> C00010 + C03519
