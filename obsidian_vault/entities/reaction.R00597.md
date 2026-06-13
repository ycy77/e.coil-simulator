---
entity_id: "reaction.R00597"
entity_type: "reaction"
name: "S-adenosyl-L-methionine:tRNA guanine N1-methyltransferase;"
source_database: "KEGG"
source_id: "R00597"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00597"
---

# S-adenosyl-L-methionine:tRNA guanine N1-methyltransferase;

`reaction.R00597`

## Static

- Type: `reaction`
- Source: `KEGG:R00597`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

S-Adenosyl-L-methionine + tRNA guanine S-Adenosyl-L-homocysteine + tRNA containing N1-methylguanine

## Biological Role

Catalyzed by trmD (protein.P0A873). Substrates: S-Adenosyl-L-methionine (molecule.C00019). Products: S-Adenosyl-L-homocysteine (molecule.C00021).

## Annotation

S-Adenosyl-L-methionine + tRNA guanine <=> S-Adenosyl-L-homocysteine + tRNA containing N1-methylguanine

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.P0A873|protein.P0A873]] `KEGG` `database` - via EC:2.1.1.228
- `is_product_of` <-- [[molecule.C00021|molecule.C00021]] `KEGG` `database` - C00019 + C01977 <=> C00021 + C04157
- `is_substrate_of` <-- [[molecule.C00019|molecule.C00019]] `KEGG` `database` - C00019 + C01977 <=> C00021 + C04157

## External IDs

- `KEGG:R00597`

## Notes

EQUATION: C00019 + C01977 <=> C00021 + C04157
