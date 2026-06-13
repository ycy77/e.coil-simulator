---
entity_id: "reaction.R00594"
entity_type: "reaction"
name: "S-adenosyl-L-methionine:tRNA uracil 5-methyltransferase;"
source_database: "KEGG"
source_id: "R00594"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00594"
---

# S-adenosyl-L-methionine:tRNA uracil 5-methyltransferase;

`reaction.R00594`

## Static

- Type: `reaction`
- Source: `KEGG:R00594`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

S-Adenosyl-L-methionine + tRNA containing uridine at position 54 S-Adenosyl-L-homocysteine + tRNA containing ribothymidine at position 54

## Biological Role

Catalyzed by trmA (protein.P23003). Substrates: S-Adenosyl-L-methionine (molecule.C00019). Products: S-Adenosyl-L-homocysteine (molecule.C00021).

## Annotation

S-Adenosyl-L-methionine + tRNA containing uridine at position 54 <=> S-Adenosyl-L-homocysteine + tRNA containing ribothymidine at position 54

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.P23003|protein.P23003]] `KEGG` `database` - via EC:2.1.1.35
- `is_product_of` <-- [[molecule.C00021|molecule.C00021]] `KEGG` `database` - C00019 + C01764 <=> C00021 + C03446
- `is_substrate_of` <-- [[molecule.C00019|molecule.C00019]] `KEGG` `database` - C00019 + C01764 <=> C00021 + C03446

## External IDs

- `KEGG:R00594`

## Notes

EQUATION: C00019 + C01764 <=> C00021 + C03446
