---
entity_id: "reaction.R02111"
entity_type: "reaction"
name: "1,4-alpha-D-glucan:orthophosphate alpha-D-glucosyltransferase"
source_database: "KEGG"
source_id: "R02111"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R02111"
---

# 1,4-alpha-D-glucan:orthophosphate alpha-D-glucosyltransferase

`reaction.R02111`

## Static

- Type: `reaction`
- Source: `KEGG:R02111`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Starch + Orthophosphate Amylose + D-Glucose 1-phosphate

## Biological Role

Catalyzed by malP (protein.P00490), glgP (protein.P0AC86). Substrates: Orthophosphate (molecule.C00009), Starch (molecule.C00369). Products: D-Glucose 1-phosphate (molecule.C00103), Amylose (molecule.C00718).

## Annotation

Starch + Orthophosphate <=> Amylose + D-Glucose 1-phosphate

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P00490|protein.P00490]] `KEGG` `database` - via EC:2.4.1.1
- `catalyzes` <-- [[protein.P0AC86|protein.P0AC86]] `KEGG` `database` - via EC:2.4.1.1
- `is_product_of` <-- [[molecule.C00103|molecule.C00103]] `KEGG` `database` - C00369 + C00009 <=> C00718 + C00103
- `is_product_of` <-- [[molecule.C00718|molecule.C00718]] `KEGG` `database` - C00369 + C00009 <=> C00718 + C00103
- `is_substrate_of` <-- [[molecule.C00009|molecule.C00009]] `KEGG` `database` - C00369 + C00009 <=> C00718 + C00103
- `is_substrate_of` <-- [[molecule.C00369|molecule.C00369]] `KEGG` `database` - C00369 + C00009 <=> C00718 + C00103

## External IDs

- `KEGG:R02111`

## Notes

EQUATION: C00369 + C00009 <=> C00718 + C00103
