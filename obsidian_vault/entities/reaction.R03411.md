---
entity_id: "reaction.R03411"
entity_type: "reaction"
name: "S-adenosyl-L-methionine:unsaturated-phospholipid methyltransferase (cyclizing)"
source_database: "KEGG"
source_id: "R03411"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R03411"
---

# S-adenosyl-L-methionine:unsaturated-phospholipid methyltransferase (cyclizing)

`reaction.R03411`

## Static

- Type: `reaction`
- Source: `KEGG:R03411`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

S-Adenosyl-L-methionine + Phospholipid olefinic fatty acid S-Adenosyl-L-homocysteine + Phospholipid cyclopropane fatty acid

## Biological Role

Catalyzed by cfa (protein.P0A9H7). Substrates: S-Adenosyl-L-methionine (molecule.C00019). Products: S-Adenosyl-L-homocysteine (molecule.C00021).

## Annotation

S-Adenosyl-L-methionine + Phospholipid olefinic fatty acid <=> S-Adenosyl-L-homocysteine + Phospholipid cyclopropane fatty acid

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.P0A9H7|protein.P0A9H7]] `KEGG` `database` - via EC:2.1.1.79
- `is_product_of` <-- [[molecule.C00021|molecule.C00021]] `KEGG` `database` - C00019 + C01229 <=> C00021 + C04340
- `is_substrate_of` <-- [[molecule.C00019|molecule.C00019]] `KEGG` `database` - C00019 + C01229 <=> C00021 + C04340

## External IDs

- `KEGG:R03411`

## Notes

EQUATION: C00019 + C01229 <=> C00021 + C04340
