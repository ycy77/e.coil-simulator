---
entity_id: "reaction.R05506"
entity_type: "reaction"
name: "R05506"
source_database: "KEGG"
source_id: "R05506"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R05506"
---

# R05506

`reaction.R05506`

## Static

- Type: `reaction`
- Source: `KEGG:R05506`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Benzoylacetyl-CoA + CoA Benzoyl-CoA + Acetyl-CoA

## Biological Role

Catalyzed by fadA (protein.P21151), fadI (protein.P76503). Substrates: CoA (molecule.C00010). Products: Acetyl-CoA (molecule.C00024), Benzoyl-CoA (molecule.C00512).

## Annotation

Benzoylacetyl-CoA + CoA <=> Benzoyl-CoA + Acetyl-CoA

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P21151|protein.P21151]] `KEGG` `database` - via EC:2.3.1.16
- `catalyzes` <-- [[protein.P76503|protein.P76503]] `KEGG` `database` - via EC:2.3.1.16
- `is_product_of` <-- [[molecule.C00024|molecule.C00024]] `KEGG` `database` - C07118 + C00010 <=> C00512 + C00024
- `is_product_of` <-- [[molecule.C00512|molecule.C00512]] `KEGG` `database` - C07118 + C00010 <=> C00512 + C00024
- `is_substrate_of` <-- [[molecule.C00010|molecule.C00010]] `KEGG` `database` - C07118 + C00010 <=> C00512 + C00024

## External IDs

- `KEGG:R05506`

## Notes

EQUATION: C07118 + C00010 <=> C00512 + C00024
