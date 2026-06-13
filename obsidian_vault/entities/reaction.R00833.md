---
entity_id: "reaction.R00833"
entity_type: "reaction"
name: "(R)-methylmalonyl-CoA CoA-carbonylmutase"
source_database: "KEGG"
source_id: "R00833"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00833"
---

# (R)-methylmalonyl-CoA CoA-carbonylmutase

`reaction.R00833`

## Static

- Type: `reaction`
- Source: `KEGG:R00833`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

(R)-Methylmalonyl-CoA Succinyl-CoA

## Biological Role

Catalyzed by scpA (protein.P27253). Substrates: (R)-Methylmalonyl-CoA (molecule.C01213). Products: Succinyl-CoA (molecule.C00091).

## Annotation

(R)-Methylmalonyl-CoA <=> Succinyl-CoA

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.P27253|protein.P27253]] `KEGG` `database` - via EC:5.4.99.2
- `is_product_of` <-- [[molecule.C00091|molecule.C00091]] `KEGG` `database` - C01213 <=> C00091
- `is_substrate_of` <-- [[molecule.C01213|molecule.C01213]] `KEGG` `database` - C01213 <=> C00091

## External IDs

- `KEGG:R00833`

## Notes

EQUATION: C01213 <=> C00091
