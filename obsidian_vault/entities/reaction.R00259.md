---
entity_id: "reaction.R00259"
entity_type: "reaction"
name: "acetyl-CoA:L-glutamate N-acetyltransferase"
source_database: "KEGG"
source_id: "R00259"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00259"
---

# acetyl-CoA:L-glutamate N-acetyltransferase

`reaction.R00259`

## Static

- Type: `reaction`
- Source: `KEGG:R00259`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Acetyl-CoA + L-Glutamate CoA + N-Acetyl-L-glutamate

## Biological Role

Catalyzed by argA (protein.P0A6C5). Substrates: Acetyl-CoA (molecule.C00024), L-Glutamate (molecule.C00025). Products: CoA (molecule.C00010), N-Acetyl-L-glutamate (molecule.C00624).

## Annotation

Acetyl-CoA + L-Glutamate <=> CoA + N-Acetyl-L-glutamate

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P0A6C5|protein.P0A6C5]] `KEGG` `database` - via EC:2.3.1.1
- `is_product_of` <-- [[molecule.C00010|molecule.C00010]] `KEGG` `database` - C00024 + C00025 <=> C00010 + C00624
- `is_product_of` <-- [[molecule.C00624|molecule.C00624]] `KEGG` `database` - C00024 + C00025 <=> C00010 + C00624
- `is_substrate_of` <-- [[molecule.C00024|molecule.C00024]] `KEGG` `database` - C00024 + C00025 <=> C00010 + C00624
- `is_substrate_of` <-- [[molecule.C00025|molecule.C00025]] `KEGG` `database` - C00024 + C00025 <=> C00010 + C00624

## External IDs

- `KEGG:R00259`

## Notes

EQUATION: C00024 + C00025 <=> C00010 + C00624
