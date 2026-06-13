---
entity_id: "reaction.R12583"
entity_type: "reaction"
name: "5-methylaminomethyl-2-(Se-phospho)selenouridine34 phosphohydrolase"
source_database: "KEGG"
source_id: "R12583"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R12583"
---

# 5-methylaminomethyl-2-(Se-phospho)selenouridine34 phosphohydrolase

`reaction.R12583`

## Static

- Type: `reaction`
- Source: `KEGG:R12583`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

5-Methylaminomethyl-2-(Se-phospho)selenouridine in tRNA + H2O 5-Methylaminomethyl-2-selenouridine in tRNA + Orthophosphate

## Biological Role

Catalyzed by selU (protein.P33667). Substrates: H2O (molecule.C00001). Products: Orthophosphate (molecule.C00009).

## Annotation

5-Methylaminomethyl-2-(Se-phospho)selenouridine in tRNA + H2O <=> 5-Methylaminomethyl-2-selenouridine in tRNA + Orthophosphate

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.P33667|protein.P33667]] `KEGG` `database` - via EC:2.9.1.3
- `is_product_of` <-- [[molecule.C00009|molecule.C00009]] `KEGG` `database` - C22267 + C00001 <=> C22268 + C00009
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C22267 + C00001 <=> C22268 + C00009

## External IDs

- `KEGG:R12583`

## Notes

EQUATION: C22267 + C00001 <=> C22268 + C00009
