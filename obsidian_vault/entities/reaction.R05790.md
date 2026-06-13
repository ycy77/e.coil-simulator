---
entity_id: "reaction.R05790"
entity_type: "reaction"
name: "alpha-D-mannosyl-3-phosphoglycerate phosphohydrolase"
source_database: "KEGG"
source_id: "R05790"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R05790"
---

# alpha-D-mannosyl-3-phosphoglycerate phosphohydrolase

`reaction.R05790`

## Static

- Type: `reaction`
- Source: `KEGG:R05790`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

2-(alpha-D-Mannosyl)-3-phosphoglycerate + H2O 2-O-(alpha-D-Mannosyl)-D-glycerate + Orthophosphate

## Biological Role

Catalyzed by yedP (protein.P76329). Substrates: H2O (molecule.C00001), 2-(alpha-D-Mannosyl)-3-phosphoglycerate (molecule.C11516). Products: Orthophosphate (molecule.C00009), 2-O-(alpha-D-Mannosyl)-D-glycerate (molecule.C11544).

## Annotation

2-(alpha-D-Mannosyl)-3-phosphoglycerate + H2O <=> 2-O-(alpha-D-Mannosyl)-D-glycerate + Orthophosphate

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P76329|protein.P76329]] `KEGG` `database` - via EC:3.1.3.70
- `is_product_of` <-- [[molecule.C00009|molecule.C00009]] `KEGG` `database` - C11516 + C00001 <=> C11544 + C00009
- `is_product_of` <-- [[molecule.C11544|molecule.C11544]] `KEGG` `database` - C11516 + C00001 <=> C11544 + C00009
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C11516 + C00001 <=> C11544 + C00009
- `is_substrate_of` <-- [[molecule.C11516|molecule.C11516]] `KEGG` `database` - C11516 + C00001 <=> C11544 + C00009

## External IDs

- `KEGG:R05790`

## Notes

EQUATION: C11516 + C00001 <=> C11544 + C00009
