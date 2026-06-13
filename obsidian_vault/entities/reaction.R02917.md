---
entity_id: "reaction.R02917"
entity_type: "reaction"
name: "S-adenosyl-L-methionine:tRNA (guanosine-2'-O-)-methyltransferase"
source_database: "KEGG"
source_id: "R02917"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R02917"
---

# S-adenosyl-L-methionine:tRNA (guanosine-2'-O-)-methyltransferase

`reaction.R02917`

## Static

- Type: `reaction`
- Source: `KEGG:R02917`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

S-Adenosyl-L-methionine + tRNA guanine S-Adenosyl-L-homocysteine + tRNA containing 2'-O-methylguanosine

## Biological Role

Catalyzed by trmH (protein.P0AGJ2). Substrates: S-Adenosyl-L-methionine (molecule.C00019). Products: S-Adenosyl-L-homocysteine (molecule.C00021).

## Annotation

S-Adenosyl-L-methionine + tRNA guanine <=> S-Adenosyl-L-homocysteine + tRNA containing 2'-O-methylguanosine

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.P0AGJ2|protein.P0AGJ2]] `KEGG` `database` - via EC:2.1.1.34
- `is_product_of` <-- [[molecule.C00021|molecule.C00021]] `KEGG` `database` - C00019 + C01977 <=> C00021 + C04545
- `is_substrate_of` <-- [[molecule.C00019|molecule.C00019]] `KEGG` `database` - C00019 + C01977 <=> C00021 + C04545

## External IDs

- `KEGG:R02917`

## Notes

EQUATION: C00019 + C01977 <=> C00021 + C04545
