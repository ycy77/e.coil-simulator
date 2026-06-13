---
entity_id: "reaction.R04162"
entity_type: "reaction"
name: "1-alkyl-2-acyl-sn-glycero-3-phosphate phosphohydrolase"
source_database: "KEGG"
source_id: "R04162"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R04162"
---

# 1-alkyl-2-acyl-sn-glycero-3-phosphate phosphohydrolase

`reaction.R04162`

## Static

- Type: `reaction`
- Source: `KEGG:R04162`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

2-Acyl-1-alkyl-sn-glycero-3-phosphate + H2O 1-Alkyl-2-acylglycerol + Orthophosphate

## Biological Role

Catalyzed by pgpB (protein.P0A924). Substrates: H2O (molecule.C00001), 2-Acyl-1-alkyl-sn-glycero-3-phosphate (molecule.C05977). Products: Orthophosphate (molecule.C00009), 1-Alkyl-2-acylglycerol (molecule.C03201).

## Annotation

2-Acyl-1-alkyl-sn-glycero-3-phosphate + H2O <=> 1-Alkyl-2-acylglycerol + Orthophosphate

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P0A924|protein.P0A924]] `KEGG` `database` - via EC:3.1.3.4
- `is_product_of` <-- [[molecule.C00009|molecule.C00009]] `KEGG` `database` - C05977 + C00001 <=> C03201 + C00009
- `is_product_of` <-- [[molecule.C03201|molecule.C03201]] `KEGG` `database` - C05977 + C00001 <=> C03201 + C00009
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C05977 + C00001 <=> C03201 + C00009
- `is_substrate_of` <-- [[molecule.C05977|molecule.C05977]] `KEGG` `database` - C05977 + C00001 <=> C03201 + C00009

## External IDs

- `KEGG:R04162`

## Notes

EQUATION: C05977 + C00001 <=> C03201 + C00009
