---
entity_id: "reaction.R03778"
entity_type: "reaction"
name: "octanoyl-CoA:acetyl-CoA C-acyltransferase"
source_database: "KEGG"
source_id: "R03778"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R03778"
---

# octanoyl-CoA:acetyl-CoA C-acyltransferase

`reaction.R03778`

## Static

- Type: `reaction`
- Source: `KEGG:R03778`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Octanoyl-CoA + Acetyl-CoA CoA + 3-Oxodecanoyl-CoA

## Biological Role

Catalyzed by fadA (protein.P21151), fadI (protein.P76503). Substrates: Acetyl-CoA (molecule.C00024), Octanoyl-CoA (molecule.C01944). Products: CoA (molecule.C00010), 3-Oxodecanoyl-CoA (molecule.C05265).

## Annotation

Octanoyl-CoA + Acetyl-CoA <=> CoA + 3-Oxodecanoyl-CoA

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P21151|protein.P21151]] `KEGG` `database` - via EC:2.3.1.16
- `catalyzes` <-- [[protein.P76503|protein.P76503]] `KEGG` `database` - via EC:2.3.1.16
- `is_product_of` <-- [[molecule.C00010|molecule.C00010]] `KEGG` `database` - C01944 + C00024 <=> C00010 + C05265
- `is_product_of` <-- [[molecule.C05265|molecule.C05265]] `KEGG` `database` - C01944 + C00024 <=> C00010 + C05265
- `is_substrate_of` <-- [[molecule.C00024|molecule.C00024]] `KEGG` `database` - C01944 + C00024 <=> C00010 + C05265
- `is_substrate_of` <-- [[molecule.C01944|molecule.C01944]] `KEGG` `database` - C01944 + C00024 <=> C00010 + C05265

## External IDs

- `KEGG:R03778`

## Notes

EQUATION: C01944 + C00024 <=> C00010 + C05265
