---
entity_id: "reaction.R00586"
entity_type: "reaction"
name: "acetyl-CoA:L-serine O-acetyltransferase"
source_database: "KEGG"
source_id: "R00586"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00586"
---

# acetyl-CoA:L-serine O-acetyltransferase

`reaction.R00586`

## Static

- Type: `reaction`
- Source: `KEGG:R00586`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

L-Serine + Acetyl-CoA O-Acetyl-L-serine + CoA

## Biological Role

Catalyzed by cysE (protein.P0A9D4). Substrates: Acetyl-CoA (molecule.C00024), L-Serine (molecule.C00065). Products: CoA (molecule.C00010), O-Acetyl-L-serine (molecule.C00979).

## Annotation

L-Serine + Acetyl-CoA <=> O-Acetyl-L-serine + CoA

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P0A9D4|protein.P0A9D4]] `KEGG` `database` - via EC:2.3.1.30
- `is_product_of` <-- [[molecule.C00010|molecule.C00010]] `KEGG` `database` - C00065 + C00024 <=> C00979 + C00010
- `is_product_of` <-- [[molecule.C00979|molecule.C00979]] `KEGG` `database` - C00065 + C00024 <=> C00979 + C00010
- `is_substrate_of` <-- [[molecule.C00024|molecule.C00024]] `KEGG` `database` - C00065 + C00024 <=> C00979 + C00010
- `is_substrate_of` <-- [[molecule.C00065|molecule.C00065]] `KEGG` `database` - C00065 + C00024 <=> C00979 + C00010

## External IDs

- `KEGG:R00586`

## Notes

EQUATION: C00065 + C00024 <=> C00979 + C00010
