---
entity_id: "reaction.R07770"
entity_type: "reaction"
name: "R07770"
source_database: "KEGG"
source_id: "R07770"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R07770"
---

# R07770

`reaction.R07770`

## Static

- Type: `reaction`
- Source: `KEGG:R07770`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ATP + (R)-Lipoate Diphosphate + Lipoyl-AMP

## Biological Role

Catalyzed by lplA (protein.P32099). Substrates: ATP (molecule.C00002), (R)-Lipoate (molecule.C16241). Products: Diphosphate (molecule.C00013), Lipoyl-AMP (molecule.C16238).

## Annotation

ATP + (R)-Lipoate <=> Diphosphate + Lipoyl-AMP

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P32099|protein.P32099]] `KEGG` `database` - via EC:6.3.1.20
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `KEGG` `database` - C00002 + C16241 <=> C00013 + C16238
- `is_product_of` <-- [[molecule.C16238|molecule.C16238]] `KEGG` `database` - C00002 + C16241 <=> C00013 + C16238
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `KEGG` `database` - C00002 + C16241 <=> C00013 + C16238
- `is_substrate_of` <-- [[molecule.C16241|molecule.C16241]] `KEGG` `database` - C00002 + C16241 <=> C00013 + C16238

## External IDs

- `KEGG:R07770`

## Notes

EQUATION: C00002 + C16241 <=> C00013 + C16238
