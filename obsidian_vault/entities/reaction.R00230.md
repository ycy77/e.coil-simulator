---
entity_id: "reaction.R00230"
entity_type: "reaction"
name: "acetyl-CoA:phosphate acetyltransferase"
source_database: "KEGG"
source_id: "R00230"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00230"
---

# acetyl-CoA:phosphate acetyltransferase

`reaction.R00230`

## Static

- Type: `reaction`
- Source: `KEGG:R00230`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Acetyl-CoA + Orthophosphate CoA + Acetyl phosphate

## Biological Role

Catalyzed by pta (protein.P0A9M8). Substrates: Orthophosphate (molecule.C00009), Acetyl-CoA (molecule.C00024). Products: CoA (molecule.C00010), Acetyl phosphate (molecule.C00227).

## Annotation

Acetyl-CoA + Orthophosphate <=> CoA + Acetyl phosphate

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P0A9M8|protein.P0A9M8]] `KEGG` `database` - via EC:2.3.1.8
- `is_product_of` <-- [[molecule.C00010|molecule.C00010]] `KEGG` `database` - C00024 + C00009 <=> C00010 + C00227
- `is_product_of` <-- [[molecule.C00227|molecule.C00227]] `KEGG` `database` - C00024 + C00009 <=> C00010 + C00227
- `is_substrate_of` <-- [[molecule.C00009|molecule.C00009]] `KEGG` `database` - C00024 + C00009 <=> C00010 + C00227
- `is_substrate_of` <-- [[molecule.C00024|molecule.C00024]] `KEGG` `database` - C00024 + C00009 <=> C00010 + C00227

## External IDs

- `KEGG:R00230`

## Notes

EQUATION: C00024 + C00009 <=> C00010 + C00227
