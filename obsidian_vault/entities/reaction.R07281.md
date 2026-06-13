---
entity_id: "reaction.R07281"
entity_type: "reaction"
name: "D-ribulose 5-phosphate formate-lyase (L-3,4-dihydroxybutan-2-one 4-phosphate-forming)"
source_database: "KEGG"
source_id: "R07281"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R07281"
---

# D-ribulose 5-phosphate formate-lyase (L-3,4-dihydroxybutan-2-one 4-phosphate-forming)

`reaction.R07281`

## Static

- Type: `reaction`
- Source: `KEGG:R07281`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

D-Ribulose 5-phosphate L-3,4-Dihydroxybutan-2-one 4-phosphate + Formate

## Biological Role

Catalyzed by ribB (protein.P0A7J0). Substrates: D-Ribulose 5-phosphate (molecule.C00199). Products: Formate (molecule.C00058), L-3,4-Dihydroxybutan-2-one 4-phosphate (molecule.C15556).

## Annotation

D-Ribulose 5-phosphate <=> L-3,4-Dihydroxybutan-2-one 4-phosphate + Formate

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[protein.P0A7J0|protein.P0A7J0]] `KEGG` `database` - via EC:4.1.99.12
- `is_product_of` <-- [[molecule.C00058|molecule.C00058]] `KEGG` `database` - C00199 <=> C15556 + C00058
- `is_product_of` <-- [[molecule.C15556|molecule.C15556]] `KEGG` `database` - C00199 <=> C15556 + C00058
- `is_substrate_of` <-- [[molecule.C00199|molecule.C00199]] `KEGG` `database` - C00199 <=> C15556 + C00058

## External IDs

- `KEGG:R07281`

## Notes

EQUATION: C00199 <=> C15556 + C00058
