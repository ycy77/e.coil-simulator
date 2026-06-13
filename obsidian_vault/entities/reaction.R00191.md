---
entity_id: "reaction.R00191"
entity_type: "reaction"
name: "adenosine 3',5'-phosphate 5'-nucleotidohydrolase"
source_database: "KEGG"
source_id: "R00191"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00191"
---

# adenosine 3',5'-phosphate 5'-nucleotidohydrolase

`reaction.R00191`

## Static

- Type: `reaction`
- Source: `KEGG:R00191`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

3',5'-Cyclic AMP + H2O AMP

## Biological Role

Catalyzed by cpdA (protein.P0AEW4). Substrates: H2O (molecule.C00001), 3',5'-Cyclic AMP (molecule.C00575). Products: AMP (molecule.C00020).

## Annotation

3',5'-Cyclic AMP + H2O <=> AMP

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[protein.P0AEW4|protein.P0AEW4]] `KEGG` `database` - via EC:3.1.4.53
- `is_product_of` <-- [[molecule.C00020|molecule.C00020]] `KEGG` `database` - C00575 + C00001 <=> C00020
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C00575 + C00001 <=> C00020
- `is_substrate_of` <-- [[molecule.C00575|molecule.C00575]] `KEGG` `database` - C00575 + C00001 <=> C00020

## External IDs

- `KEGG:R00191`

## Notes

EQUATION: C00575 + C00001 <=> C00020
