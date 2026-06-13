---
entity_id: "reaction.R07771"
entity_type: "reaction"
name: "R07771"
source_database: "KEGG"
source_id: "R07771"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R07771"
---

# R07771

`reaction.R07771`

## Static

- Type: `reaction`
- Source: `KEGG:R07771`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Lipoyl-AMP + [Lipoyl-carrier protein]-L-lysine Protein N6-(lipoyl)lysine + AMP

## Biological Role

Catalyzed by lplA (protein.P32099). Substrates: Lipoyl-AMP (molecule.C16238). Products: AMP (molecule.C00020).

## Annotation

Lipoyl-AMP + [Lipoyl-carrier protein]-L-lysine <=> Protein N6-(lipoyl)lysine + AMP

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.P32099|protein.P32099]] `KEGG` `database` - via EC:6.3.1.20
- `is_product_of` <-- [[molecule.C00020|molecule.C00020]] `KEGG` `database` - C16238 + C16240 <=> C16237 + C00020
- `is_substrate_of` <-- [[molecule.C16238|molecule.C16238]] `KEGG` `database` - C16238 + C16240 <=> C16237 + C00020

## External IDs

- `KEGG:R07771`

## Notes

EQUATION: C16238 + C16240 <=> C16237 + C00020
