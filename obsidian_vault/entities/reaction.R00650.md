---
entity_id: "reaction.R00650"
entity_type: "reaction"
name: "S-adenosyl-L-methionine:L-homocysteine S-methyltransferase"
source_database: "KEGG"
source_id: "R00650"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00650"
---

# S-adenosyl-L-methionine:L-homocysteine S-methyltransferase

`reaction.R00650`

## Static

- Type: `reaction`
- Source: `KEGG:R00650`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

S-Adenosyl-L-methionine + L-Homocysteine S-Adenosyl-L-homocysteine + L-Methionine

## Biological Role

Catalyzed by mmuM (protein.Q47690). Substrates: S-Adenosyl-L-methionine (molecule.C00019), L-Homocysteine (molecule.C00155). Products: S-Adenosyl-L-homocysteine (molecule.C00021), L-Methionine (molecule.C00073).

## Annotation

S-Adenosyl-L-methionine + L-Homocysteine <=> S-Adenosyl-L-homocysteine + L-Methionine

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.Q47690|protein.Q47690]] `KEGG` `database` - via EC:2.1.1.10
- `is_product_of` <-- [[molecule.C00021|molecule.C00021]] `KEGG` `database` - C00019 + C00155 <=> C00021 + C00073
- `is_product_of` <-- [[molecule.C00073|molecule.C00073]] `KEGG` `database` - C00019 + C00155 <=> C00021 + C00073
- `is_substrate_of` <-- [[molecule.C00019|molecule.C00019]] `KEGG` `database` - C00019 + C00155 <=> C00021 + C00073
- `is_substrate_of` <-- [[molecule.C00155|molecule.C00155]] `KEGG` `database` - C00019 + C00155 <=> C00021 + C00073

## External IDs

- `KEGG:R00650`

## Notes

EQUATION: C00019 + C00155 <=> C00021 + C00073
