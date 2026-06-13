---
entity_id: "reaction.R06185"
entity_type: "reaction"
name: "R06185"
source_database: "KEGG"
source_id: "R06185"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R06185"
---

# R06185

`reaction.R06185`

## Static

- Type: `reaction`
- Source: `KEGG:R06185`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Starch + Orthophosphate 1,4-alpha-D-Glucan + D-Glucose 1-phosphate

## Biological Role

Catalyzed by malP (protein.P00490), glgP (protein.P0AC86). Substrates: Orthophosphate (molecule.C00009). Products: D-Glucose 1-phosphate (molecule.C00103).

## Annotation

Starch + Orthophosphate <=> 1,4-alpha-D-Glucan + D-Glucose 1-phosphate

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[protein.P00490|protein.P00490]] `KEGG` `database` - via EC:2.4.1.1
- `catalyzes` <-- [[protein.P0AC86|protein.P0AC86]] `KEGG` `database` - via EC:2.4.1.1
- `is_product_of` <-- [[molecule.C00103|molecule.C00103]] `KEGG` `database` - G10545 + C00009 <=> G10495 + C00103
- `is_substrate_of` <-- [[molecule.C00009|molecule.C00009]] `KEGG` `database` - G10545 + C00009 <=> G10495 + C00103

## External IDs

- `KEGG:R06185`

## Notes

EQUATION: G10545 + C00009 <=> G10495 + C00103
