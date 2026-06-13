---
entity_id: "reaction.R00391"
entity_type: "reaction"
name: "acyl-CoA:acetyl-CoA C-acyltransferase"
source_database: "KEGG"
source_id: "R00391"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00391"
---

# acyl-CoA:acetyl-CoA C-acyltransferase

`reaction.R00391`

## Static

- Type: `reaction`
- Source: `KEGG:R00391`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Acyl-CoA + Acetyl-CoA CoA + 3-Oxoacyl-CoA

## Biological Role

Catalyzed by fadA (protein.P21151), fadI (protein.P76503). Substrates: Acetyl-CoA (molecule.C00024), Acyl-CoA (molecule.C00040). Products: CoA (molecule.C00010).

## Annotation

Acyl-CoA + Acetyl-CoA <=> CoA + 3-Oxoacyl-CoA

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P21151|protein.P21151]] `KEGG` `database` - via EC:2.3.1.16
- `catalyzes` <-- [[protein.P76503|protein.P76503]] `KEGG` `database` - via EC:2.3.1.16
- `is_product_of` <-- [[molecule.C00010|molecule.C00010]] `KEGG` `database` - C00040 + C00024 <=> C00010 + C00264
- `is_substrate_of` <-- [[molecule.C00024|molecule.C00024]] `KEGG` `database` - C00040 + C00024 <=> C00010 + C00264
- `is_substrate_of` <-- [[molecule.C00040|molecule.C00040]] `KEGG` `database` - C00040 + C00024 <=> C00010 + C00264

## External IDs

- `KEGG:R00391`

## Notes

EQUATION: C00040 + C00024 <=> C00010 + C00264
