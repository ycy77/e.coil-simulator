---
entity_id: "reaction.R05332"
entity_type: "reaction"
name: "acetyl-CoA:D-glucosamine-1-phosphate N-acetyltransferase"
source_database: "KEGG"
source_id: "R05332"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R05332"
---

# acetyl-CoA:D-glucosamine-1-phosphate N-acetyltransferase

`reaction.R05332`

## Static

- Type: `reaction`
- Source: `KEGG:R05332`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Acetyl-CoA + alpha-D-Glucosamine 1-phosphate CoA + N-Acetyl-alpha-D-glucosamine 1-phosphate

## Biological Role

Catalyzed by glmU (protein.P0ACC7). Substrates: Acetyl-CoA (molecule.C00024), alpha-D-Glucosamine 1-phosphate (molecule.C06156). Products: CoA (molecule.C00010), N-Acetyl-alpha-D-glucosamine 1-phosphate (molecule.C04501).

## Annotation

Acetyl-CoA + alpha-D-Glucosamine 1-phosphate <=> CoA + N-Acetyl-alpha-D-glucosamine 1-phosphate

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P0ACC7|protein.P0ACC7]] `KEGG` `database` - via EC:2.3.1.157
- `is_product_of` <-- [[molecule.C00010|molecule.C00010]] `KEGG` `database` - C00024 + C06156 <=> C00010 + C04501
- `is_product_of` <-- [[molecule.C04501|molecule.C04501]] `KEGG` `database` - C00024 + C06156 <=> C00010 + C04501
- `is_substrate_of` <-- [[molecule.C00024|molecule.C00024]] `KEGG` `database` - C00024 + C06156 <=> C00010 + C04501
- `is_substrate_of` <-- [[molecule.C06156|molecule.C06156]] `KEGG` `database` - C00024 + C06156 <=> C00010 + C04501

## External IDs

- `KEGG:R05332`

## Notes

EQUATION: C00024 + C06156 <=> C00010 + C04501
