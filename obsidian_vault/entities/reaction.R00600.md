---
entity_id: "reaction.R00600"
entity_type: "reaction"
name: "S-adenosyl-L-methionine:tRNA guanine N7-methyltransferase;"
source_database: "KEGG"
source_id: "R00600"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00600"
---

# S-adenosyl-L-methionine:tRNA guanine N7-methyltransferase;

`reaction.R00600`

## Static

- Type: `reaction`
- Source: `KEGG:R00600`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

S-Adenosyl-L-methionine + tRNA guanine S-Adenosyl-L-homocysteine + tRNA containing N7-methylguanine

## Biological Role

Catalyzed by trmB (protein.P0A8I5). Substrates: S-Adenosyl-L-methionine (molecule.C00019). Products: S-Adenosyl-L-homocysteine (molecule.C00021).

## Annotation

S-Adenosyl-L-methionine + tRNA guanine <=> S-Adenosyl-L-homocysteine + tRNA containing N7-methylguanine

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.P0A8I5|protein.P0A8I5]] `KEGG` `database` - via EC:2.1.1.33
- `is_product_of` <-- [[molecule.C00021|molecule.C00021]] `KEGG` `database` - C00019 + C01977 <=> C00021 + C04160
- `is_substrate_of` <-- [[molecule.C00019|molecule.C00019]] `KEGG` `database` - C00019 + C01977 <=> C00021 + C04160

## External IDs

- `KEGG:R00600`

## Notes

EQUATION: C00019 + C01977 <=> C00021 + C04160
