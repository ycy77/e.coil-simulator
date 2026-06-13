---
entity_id: "reaction.R00022"
entity_type: "reaction"
name: "chitobiose N-acetylglucosaminohydrolase"
source_database: "KEGG"
source_id: "R00022"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00022"
---

# chitobiose N-acetylglucosaminohydrolase

`reaction.R00022`

## Static

- Type: `reaction`
- Source: `KEGG:R00022`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Chitobiose + H2O 2 N-Acetyl-D-glucosamine

## Biological Role

Catalyzed by nagZ (protein.P75949). Substrates: H2O (molecule.C00001), Chitobiose (molecule.C01674). Products: N-Acetyl-D-glucosamine (molecule.C00140).

## Annotation

Chitobiose + H2O <=> 2 N-Acetyl-D-glucosamine

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[protein.P75949|protein.P75949]] `KEGG` `database` - via EC:3.2.1.52
- `is_product_of` <-- [[molecule.C00140|molecule.C00140]] `KEGG` `database` - C01674 + C00001 <=> 2 C00140
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C01674 + C00001 <=> 2 C00140
- `is_substrate_of` <-- [[molecule.C01674|molecule.C01674]] `KEGG` `database` - C01674 + C00001 <=> 2 C00140

## External IDs

- `KEGG:R00022`

## Notes

EQUATION: C01674 + C00001 <=> 2 C00140
