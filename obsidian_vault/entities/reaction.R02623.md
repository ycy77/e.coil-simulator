---
entity_id: "reaction.R02623"
entity_type: "reaction"
name: "S-adenosyl-L-methionine:protein-L-glutamate O-methyltransferase"
source_database: "KEGG"
source_id: "R02623"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R02623"
---

# S-adenosyl-L-methionine:protein-L-glutamate O-methyltransferase

`reaction.R02623`

## Static

- Type: `reaction`
- Source: `KEGG:R02623`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

S-Adenosyl-L-methionine + Protein glutamate S-Adenosyl-L-homocysteine + Protein glutamate methyl ester

## Biological Role

Catalyzed by cheR (protein.P07364). Substrates: S-Adenosyl-L-methionine (molecule.C00019). Products: S-Adenosyl-L-homocysteine (molecule.C00021).

## Annotation

S-Adenosyl-L-methionine + Protein glutamate <=> S-Adenosyl-L-homocysteine + Protein glutamate methyl ester

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.P07364|protein.P07364]] `KEGG` `database` - via EC:2.1.1.80
- `is_product_of` <-- [[molecule.C00021|molecule.C00021]] `KEGG` `database` - C00019 + C00614 <=> C00021 + C04142
- `is_substrate_of` <-- [[molecule.C00019|molecule.C00019]] `KEGG` `database` - C00019 + C00614 <=> C00021 + C04142

## External IDs

- `KEGG:R02623`

## Notes

EQUATION: C00019 + C00614 <=> C00021 + C04142
