---
entity_id: "reaction.R01010"
entity_type: "reaction"
name: "glycerone phosphate phosphohydrolase"
source_database: "KEGG"
source_id: "R01010"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R01010"
---

# glycerone phosphate phosphohydrolase

`reaction.R01010`

## Static

- Type: `reaction`
- Source: `KEGG:R01010`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Glycerone phosphate + H2O Glycerone + Orthophosphate

## Biological Role

Catalyzed by phoA (protein.P00634), appA (protein.P07102), aphA (protein.P0AE22). Substrates: H2O (molecule.C00001), Glycerone phosphate (molecule.C00111). Products: Orthophosphate (molecule.C00009), Glycerone (molecule.C00184).

## Annotation

Glycerone phosphate + H2O <=> Glycerone + Orthophosphate

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[protein.P00634|protein.P00634]] `KEGG` `database` - via EC:3.1.3.1
- `catalyzes` <-- [[protein.P07102|protein.P07102]] `KEGG` `database` - via EC:3.1.3.2
- `catalyzes` <-- [[protein.P0AE22|protein.P0AE22]] `KEGG` `database` - via EC:3.1.3.2
- `is_product_of` <-- [[molecule.C00009|molecule.C00009]] `KEGG` `database` - C00111 + C00001 <=> C00184 + C00009
- `is_product_of` <-- [[molecule.C00184|molecule.C00184]] `KEGG` `database` - C00111 + C00001 <=> C00184 + C00009
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C00111 + C00001 <=> C00184 + C00009
- `is_substrate_of` <-- [[molecule.C00111|molecule.C00111]] `KEGG` `database` - C00111 + C00001 <=> C00184 + C00009

## External IDs

- `KEGG:R01010`

## Notes

EQUATION: C00111 + C00001 <=> C00184 + C00009
