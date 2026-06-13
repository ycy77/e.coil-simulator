---
entity_id: "reaction.R11527"
entity_type: "reaction"
name: "1-acyl-sn-glycerol 3-phosphate phosphohydrolase"
source_database: "KEGG"
source_id: "R11527"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R11527"
---

# 1-acyl-sn-glycerol 3-phosphate phosphohydrolase

`reaction.R11527`

## Static

- Type: `reaction`
- Source: `KEGG:R11527`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

1-Acyl-sn-glycerol 3-phosphate + H2O 1-Acylglycerol + Orthophosphate

## Biological Role

Catalyzed by appA (protein.P07102), aphA (protein.P0AE22). Substrates: H2O (molecule.C00001), 1-Acyl-sn-glycerol 3-phosphate (molecule.C00681). Products: Orthophosphate (molecule.C00009), 1-Acylglycerol (molecule.C01885).

## Annotation

1-Acyl-sn-glycerol 3-phosphate + H2O <=> 1-Acylglycerol + Orthophosphate

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P07102|protein.P07102]] `KEGG` `database` - via EC:3.1.3.2
- `catalyzes` <-- [[protein.P0AE22|protein.P0AE22]] `KEGG` `database` - via EC:3.1.3.2
- `is_product_of` <-- [[molecule.C00009|molecule.C00009]] `KEGG` `database` - C00681 + C00001 <=> C01885 + C00009
- `is_product_of` <-- [[molecule.C01885|molecule.C01885]] `KEGG` `database` - C00681 + C00001 <=> C01885 + C00009
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C00681 + C00001 <=> C01885 + C00009
- `is_substrate_of` <-- [[molecule.C00681|molecule.C00681]] `KEGG` `database` - C00681 + C00001 <=> C01885 + C00009

## External IDs

- `KEGG:R11527`

## Notes

EQUATION: C00681 + C00001 <=> C01885 + C00009
