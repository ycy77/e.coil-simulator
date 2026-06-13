---
entity_id: "reaction.R02603"
entity_type: "reaction"
name: "2-hydroxy-6-oxonona-2,4-diene-1,9-dioate succinylhydrolase"
source_database: "KEGG"
source_id: "R02603"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R02603"
---

# 2-hydroxy-6-oxonona-2,4-diene-1,9-dioate succinylhydrolase

`reaction.R02603`

## Static

- Type: `reaction`
- Source: `KEGG:R02603`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

2-Hydroxy-2,4-pentadienoate + Succinate 2-Hydroxy-6-oxonona-2,4-diene-1,9-dioate + H2O

## Biological Role

Catalyzed by mhpC (protein.P77044). Substrates: Succinate (molecule.C00042), 2-Hydroxy-2,4-pentadienoate (molecule.C00596). Products: H2O (molecule.C00001), 2-Hydroxy-6-oxonona-2,4-diene-1,9-dioate (molecule.C04479).

## Annotation

2-Hydroxy-2,4-pentadienoate + Succinate <=> 2-Hydroxy-6-oxonona-2,4-diene-1,9-dioate + H2O

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P77044|protein.P77044]] `KEGG` `database` - via EC:3.7.1.14
- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C00596 + C00042 <=> C04479 + C00001
- `is_product_of` <-- [[molecule.C04479|molecule.C04479]] `KEGG` `database` - C00596 + C00042 <=> C04479 + C00001
- `is_substrate_of` <-- [[molecule.C00042|molecule.C00042]] `KEGG` `database` - C00596 + C00042 <=> C04479 + C00001
- `is_substrate_of` <-- [[molecule.C00596|molecule.C00596]] `KEGG` `database` - C00596 + C00042 <=> C04479 + C00001

## External IDs

- `KEGG:R02603`

## Notes

EQUATION: C00596 + C00042 <=> C04479 + C00001
