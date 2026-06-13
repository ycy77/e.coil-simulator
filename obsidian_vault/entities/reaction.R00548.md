---
entity_id: "reaction.R00548"
entity_type: "reaction"
name: "riboflavin-5-phosphate phosphohydrolase"
source_database: "KEGG"
source_id: "R00548"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00548"
---

# riboflavin-5-phosphate phosphohydrolase

`reaction.R00548`

## Static

- Type: `reaction`
- Source: `KEGG:R00548`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

FMN + H2O Riboflavin + Orthophosphate

## Biological Role

Catalyzed by appA (protein.P07102), yigB (protein.P0ADP0), aphA (protein.P0AE22), ybjI (protein.P75809). Substrates: H2O (molecule.C00001), FMN (molecule.C00061). Products: Orthophosphate (molecule.C00009), Riboflavin (molecule.C00255).

## Annotation

FMN + H2O <=> Riboflavin + Orthophosphate

## Outgoing Edges (0)

_None._

## Incoming Edges (8)

- `catalyzes` <-- [[protein.P07102|protein.P07102]] `KEGG` `database` - via EC:3.1.3.2
- `catalyzes` <-- [[protein.P0ADP0|protein.P0ADP0]] `KEGG` `database` - via EC:3.1.3.102
- `catalyzes` <-- [[protein.P0AE22|protein.P0AE22]] `KEGG` `database` - via EC:3.1.3.2
- `catalyzes` <-- [[protein.P75809|protein.P75809]] `KEGG` `database` - via EC:3.1.3.102
- `is_product_of` <-- [[molecule.C00009|molecule.C00009]] `KEGG` `database` - C00061 + C00001 <=> C00255 + C00009
- `is_product_of` <-- [[molecule.C00255|molecule.C00255]] `KEGG` `database` - C00061 + C00001 <=> C00255 + C00009
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C00061 + C00001 <=> C00255 + C00009
- `is_substrate_of` <-- [[molecule.C00061|molecule.C00061]] `KEGG` `database` - C00061 + C00001 <=> C00255 + C00009

## External IDs

- `KEGG:R00548`

## Notes

EQUATION: C00061 + C00001 <=> C00255 + C00009
