---
entity_id: "reaction.R00238"
entity_type: "reaction"
name: "acetyl-CoA:acetyl-CoA C-acetyltransferase"
source_database: "KEGG"
source_id: "R00238"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00238"
---

# acetyl-CoA:acetyl-CoA C-acetyltransferase

`reaction.R00238`

## Static

- Type: `reaction`
- Source: `KEGG:R00238`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

2 Acetyl-CoA CoA + Acetoacetyl-CoA

## Biological Role

Catalyzed by fadA (protein.P21151), atoB (protein.P76461), fadI (protein.P76503), yqeF (protein.Q46939). Substrates: Acetyl-CoA (molecule.C00024). Products: CoA (molecule.C00010), Acetoacetyl-CoA (molecule.C00332).

## Annotation

2 Acetyl-CoA <=> CoA + Acetoacetyl-CoA

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[protein.P21151|protein.P21151]] `KEGG` `database` - via EC:2.3.1.16
- `catalyzes` <-- [[protein.P76461|protein.P76461]] `KEGG` `database` - via EC:2.3.1.9
- `catalyzes` <-- [[protein.P76503|protein.P76503]] `KEGG` `database` - via EC:2.3.1.16
- `catalyzes` <-- [[protein.Q46939|protein.Q46939]] `KEGG` `database` - via EC:2.3.1.9
- `is_product_of` <-- [[molecule.C00010|molecule.C00010]] `KEGG` `database` - 2 C00024 <=> C00010 + C00332
- `is_product_of` <-- [[molecule.C00332|molecule.C00332]] `KEGG` `database` - 2 C00024 <=> C00010 + C00332
- `is_substrate_of` <-- [[molecule.C00024|molecule.C00024]] `KEGG` `database` - 2 C00024 <=> C00010 + C00332

## External IDs

- `KEGG:R00238`

## Notes

EQUATION: 2 C00024 <=> C00010 + C00332
