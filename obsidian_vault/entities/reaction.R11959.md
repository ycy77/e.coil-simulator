---
entity_id: "reaction.R11959"
entity_type: "reaction"
name: "2-O-(alpha-D-glucopyranosyl)-D-glycerate:phosphate alpha-D-glucosyltransferase (configuration-retaining)"
source_database: "KEGG"
source_id: "R11959"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R11959"
---

# 2-O-(alpha-D-glucopyranosyl)-D-glycerate:phosphate alpha-D-glucosyltransferase (configuration-retaining)

`reaction.R11959`

## Static

- Type: `reaction`
- Source: `KEGG:R11959`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

2-O-(alpha-D-Glucopyranosyl)-D-glycerate + Orthophosphate D-Glucose 1-phosphate + D-Glycerate

## Biological Role

Catalyzed by ycjM (protein.P76041). Substrates: Orthophosphate (molecule.C00009). Products: D-Glucose 1-phosphate (molecule.C00103), D-Glycerate (molecule.C00258).

## Annotation

2-O-(alpha-D-Glucopyranosyl)-D-glycerate + Orthophosphate <=> D-Glucose 1-phosphate + D-Glycerate

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[protein.P76041|protein.P76041]] `KEGG` `database` - via EC:2.4.1.352
- `is_product_of` <-- [[molecule.C00103|molecule.C00103]] `KEGG` `database` - C19792 + C00009 <=> C00103 + C00258
- `is_product_of` <-- [[molecule.C00258|molecule.C00258]] `KEGG` `database` - C19792 + C00009 <=> C00103 + C00258
- `is_substrate_of` <-- [[molecule.C00009|molecule.C00009]] `KEGG` `database` - C19792 + C00009 <=> C00103 + C00258

## External IDs

- `KEGG:R11959`

## Notes

EQUATION: C19792 + C00009 <=> C00103 + C00258
