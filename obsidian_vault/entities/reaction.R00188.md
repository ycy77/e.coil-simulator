---
entity_id: "reaction.R00188"
entity_type: "reaction"
name: "adenosine-3',5'-bisphosphate 3'-phosphohydrolase"
source_database: "KEGG"
source_id: "R00188"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00188"
---

# adenosine-3',5'-bisphosphate 3'-phosphohydrolase

`reaction.R00188`

## Static

- Type: `reaction`
- Source: `KEGG:R00188`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Adenosine 3',5'-bisphosphate + H2O AMP + Orthophosphate

## Biological Role

Catalyzed by cysQ (protein.P22255), rnm (protein.P77766). Substrates: H2O (molecule.C00001), Adenosine 3',5'-bisphosphate (molecule.C00054). Products: Orthophosphate (molecule.C00009), AMP (molecule.C00020).

## Annotation

Adenosine 3',5'-bisphosphate + H2O <=> AMP + Orthophosphate

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P22255|protein.P22255]] `KEGG` `database` - via EC:3.1.3.7
- `catalyzes` <-- [[protein.P77766|protein.P77766]] `KEGG` `database` - via EC:3.1.3.97
- `is_product_of` <-- [[molecule.C00009|molecule.C00009]] `KEGG` `database` - C00054 + C00001 <=> C00020 + C00009
- `is_product_of` <-- [[molecule.C00020|molecule.C00020]] `KEGG` `database` - C00054 + C00001 <=> C00020 + C00009
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C00054 + C00001 <=> C00020 + C00009
- `is_substrate_of` <-- [[molecule.C00054|molecule.C00054]] `KEGG` `database` - C00054 + C00001 <=> C00020 + C00009

## External IDs

- `KEGG:R00188`

## Notes

EQUATION: C00054 + C00001 <=> C00020 + C00009
