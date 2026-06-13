---
entity_id: "reaction.R00601"
entity_type: "reaction"
name: "S-adenosyl-L-methionine:tRNA 5-methylaminomethyl-2-thiouridine methyltransferase;"
source_database: "KEGG"
source_id: "R00601"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00601"
---

# S-adenosyl-L-methionine:tRNA 5-methylaminomethyl-2-thiouridine methyltransferase;

`reaction.R00601`

## Static

- Type: `reaction`
- Source: `KEGG:R00601`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

S-Adenosyl-L-methionine + tRNA containing 5-(aminomethyl)-2-thiouridine S-Adenosyl-L-homocysteine + tRNA containing 5-[(methylamino)methyl]-2-thiouridylate

## Biological Role

Catalyzed by mnmC (protein.P77182). Substrates: S-Adenosyl-L-methionine (molecule.C00019). Products: S-Adenosyl-L-homocysteine (molecule.C00021).

## Annotation

S-Adenosyl-L-methionine + tRNA containing 5-(aminomethyl)-2-thiouridine <=> S-Adenosyl-L-homocysteine + tRNA containing 5-[(methylamino)methyl]-2-thiouridylate

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.P77182|protein.P77182]] `KEGG` `database` - via EC:2.1.1.61
- `is_product_of` <-- [[molecule.C00021|molecule.C00021]] `KEGG` `database` - C00019 + C11478 <=> C00021 + C04728
- `is_substrate_of` <-- [[molecule.C00019|molecule.C00019]] `KEGG` `database` - C00019 + C11478 <=> C00021 + C04728

## External IDs

- `KEGG:R00601`

## Notes

EQUATION: C00019 + C11478 <=> C00021 + C04728
