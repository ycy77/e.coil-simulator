---
entity_id: "reaction.R00829"
entity_type: "reaction"
name: "succinyl-CoA:acetyl-CoA C-acyltransferase;"
source_database: "KEGG"
source_id: "R00829"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00829"
---

# succinyl-CoA:acetyl-CoA C-acyltransferase;

`reaction.R00829`

## Static

- Type: `reaction`
- Source: `KEGG:R00829`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Succinyl-CoA + Acetyl-CoA CoA + 3-Oxoadipyl-CoA

## Biological Role

Catalyzed by paaJ (protein.P0C7L2), fadA (protein.P21151), fadI (protein.P76503). Substrates: Acetyl-CoA (molecule.C00024), Succinyl-CoA (molecule.C00091). Products: CoA (molecule.C00010), 3-Oxoadipyl-CoA (molecule.C02232).

## Annotation

Succinyl-CoA + Acetyl-CoA <=> CoA + 3-Oxoadipyl-CoA

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[protein.P0C7L2|protein.P0C7L2]] `KEGG` `database` - via EC:2.3.1.174
- `catalyzes` <-- [[protein.P21151|protein.P21151]] `KEGG` `database` - via EC:2.3.1.16
- `catalyzes` <-- [[protein.P76503|protein.P76503]] `KEGG` `database` - via EC:2.3.1.16
- `is_product_of` <-- [[molecule.C00010|molecule.C00010]] `KEGG` `database` - C00091 + C00024 <=> C00010 + C02232
- `is_product_of` <-- [[molecule.C02232|molecule.C02232]] `KEGG` `database` - C00091 + C00024 <=> C00010 + C02232
- `is_substrate_of` <-- [[molecule.C00024|molecule.C00024]] `KEGG` `database` - C00091 + C00024 <=> C00010 + C02232
- `is_substrate_of` <-- [[molecule.C00091|molecule.C00091]] `KEGG` `database` - C00091 + C00024 <=> C00010 + C02232

## External IDs

- `KEGG:R00829`

## Notes

EQUATION: C00091 + C00024 <=> C00010 + C02232
