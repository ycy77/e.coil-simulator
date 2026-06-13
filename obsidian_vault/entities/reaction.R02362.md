---
entity_id: "reaction.R02362"
entity_type: "reaction"
name: "pectin pectylhydrolase"
source_database: "KEGG"
source_id: "R02362"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R02362"
---

# pectin pectylhydrolase

`reaction.R02362`

## Static

- Type: `reaction`
- Source: `KEGG:R02362`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Pectin + n H2O n Methanol + Pectate

## Biological Role

Catalyzed by ybhC (protein.P46130). Substrates: H2O (molecule.C00001), Pectin (molecule.C00714). Products: Methanol (molecule.C00132), Pectate (molecule.C00470).

## Annotation

Pectin + n H2O <=> n Methanol + Pectate

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P46130|protein.P46130]] `KEGG` `database` - via EC:3.1.1.11
- `is_product_of` <-- [[molecule.C00132|molecule.C00132]] `KEGG` `database` - C00714 + n C00001 <=> n C00132 + C00470
- `is_product_of` <-- [[molecule.C00470|molecule.C00470]] `KEGG` `database` - C00714 + n C00001 <=> n C00132 + C00470
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C00714 + n C00001 <=> n C00132 + C00470
- `is_substrate_of` <-- [[molecule.C00714|molecule.C00714]] `KEGG` `database` - C00714 + n C00001 <=> n C00132 + C00470

## External IDs

- `KEGG:R02362`

## Notes

EQUATION: C00714 + n C00001 <=> n C00132 + C00470
