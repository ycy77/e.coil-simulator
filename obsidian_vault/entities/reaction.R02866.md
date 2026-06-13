---
entity_id: "reaction.R02866"
entity_type: "reaction"
name: "sorbitol-6-phosphate phosphohydrolase"
source_database: "KEGG"
source_id: "R02866"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R02866"
---

# sorbitol-6-phosphate phosphohydrolase

`reaction.R02866`

## Static

- Type: `reaction`
- Source: `KEGG:R02866`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Sorbitol 6-phosphate + H2O D-Sorbitol + Orthophosphate

## Biological Role

Catalyzed by hxpB (protein.P77247), hxpA (protein.P77625). Substrates: H2O (molecule.C00001), Sorbitol 6-phosphate (molecule.C01096). Products: Orthophosphate (molecule.C00009), D-Sorbitol (molecule.C00794).

## Annotation

Sorbitol 6-phosphate + H2O <=> D-Sorbitol + Orthophosphate

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P77247|protein.P77247]] `KEGG` `database` - via EC:3.1.3.50
- `catalyzes` <-- [[protein.P77625|protein.P77625]] `KEGG` `database` - via EC:3.1.3.50
- `is_product_of` <-- [[molecule.C00009|molecule.C00009]] `KEGG` `database` - C01096 + C00001 <=> C00794 + C00009
- `is_product_of` <-- [[molecule.C00794|molecule.C00794]] `KEGG` `database` - C01096 + C00001 <=> C00794 + C00009
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C01096 + C00001 <=> C00794 + C00009
- `is_substrate_of` <-- [[molecule.C01096|molecule.C01096]] `KEGG` `database` - C01096 + C00001 <=> C00794 + C00009

## External IDs

- `KEGG:R02866`

## Notes

EQUATION: C01096 + C00001 <=> C00794 + C00009
