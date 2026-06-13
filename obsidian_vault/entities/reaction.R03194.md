---
entity_id: "reaction.R03194"
entity_type: "reaction"
name: "S-adenosyl-L-methionine:uroporphyrinogen-III C-methyltransferase"
source_database: "KEGG"
source_id: "R03194"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R03194"
---

# S-adenosyl-L-methionine:uroporphyrinogen-III C-methyltransferase

`reaction.R03194`

## Static

- Type: `reaction`
- Source: `KEGG:R03194`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

2 S-Adenosyl-L-methionine + Uroporphyrinogen III 2 S-Adenosyl-L-homocysteine + Precorrin 2

## Biological Role

Catalyzed by hemX (protein.P09127), cysG (protein.P0AEA8). Substrates: S-Adenosyl-L-methionine (molecule.C00019), Uroporphyrinogen III (molecule.C01051). Products: S-Adenosyl-L-homocysteine (molecule.C00021), Precorrin 2 (molecule.C02463).

## Annotation

2 S-Adenosyl-L-methionine + Uroporphyrinogen III <=> 2 S-Adenosyl-L-homocysteine + Precorrin 2

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P09127|protein.P09127]] `KEGG` `database` - via EC:2.1.1.107
- `catalyzes` <-- [[protein.P0AEA8|protein.P0AEA8]] `KEGG` `database` - via EC:2.1.1.107
- `is_product_of` <-- [[molecule.C00021|molecule.C00021]] `KEGG` `database` - 2 C00019 + C01051 <=> 2 C00021 + C02463
- `is_product_of` <-- [[molecule.C02463|molecule.C02463]] `KEGG` `database` - 2 C00019 + C01051 <=> 2 C00021 + C02463
- `is_substrate_of` <-- [[molecule.C00019|molecule.C00019]] `KEGG` `database` - 2 C00019 + C01051 <=> 2 C00021 + C02463
- `is_substrate_of` <-- [[molecule.C01051|molecule.C01051]] `KEGG` `database` - 2 C00019 + C01051 <=> 2 C00021 + C02463

## External IDs

- `KEGG:R03194`

## Notes

EQUATION: 2 C00019 + C01051 <=> 2 C00021 + C02463
