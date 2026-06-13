---
entity_id: "reaction.R02616"
entity_type: "reaction"
name: "acyl-CoA:beta-D-galactoside 6-acetyltransferase"
source_database: "KEGG"
source_id: "R02616"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R02616"
---

# acyl-CoA:beta-D-galactoside 6-acetyltransferase

`reaction.R02616`

## Static

- Type: `reaction`
- Source: `KEGG:R02616`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Acetyl-CoA + beta-D-Galactoside CoA + 6-Acetyl-beta-D-galactoside

## Biological Role

Catalyzed by lacA (protein.P07464). Substrates: Acetyl-CoA (molecule.C00024). Products: CoA (molecule.C00010).

## Annotation

Acetyl-CoA + beta-D-Galactoside <=> CoA + 6-Acetyl-beta-D-galactoside

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.P07464|protein.P07464]] `KEGG` `database` - via EC:2.3.1.18
- `is_product_of` <-- [[molecule.C00010|molecule.C00010]] `KEGG` `database` - C00024 + C00602 <=> C00010 + C03773
- `is_substrate_of` <-- [[molecule.C00024|molecule.C00024]] `KEGG` `database` - C00024 + C00602 <=> C00010 + C03773

## External IDs

- `KEGG:R02616`

## Notes

EQUATION: C00024 + C00602 <=> C00010 + C03773
