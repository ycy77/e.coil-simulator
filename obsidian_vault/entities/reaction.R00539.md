---
entity_id: "reaction.R00539"
entity_type: "reaction"
name: "acyl phosphate phosphohydrolase"
source_database: "KEGG"
source_id: "R00539"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00539"
---

# acyl phosphate phosphohydrolase

`reaction.R00539`

## Static

- Type: `reaction`
- Source: `KEGG:R00539`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Acyl phosphate + H2O Carboxylate + Orthophosphate

## Biological Role

Catalyzed by yccX (protein.P0AB65). Substrates: H2O (molecule.C00001), Acyl phosphate (molecule.C02133). Products: Orthophosphate (molecule.C00009).

## Annotation

Acyl phosphate + H2O <=> Carboxylate + Orthophosphate

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[protein.P0AB65|protein.P0AB65]] `KEGG` `database` - via EC:3.6.1.7
- `is_product_of` <-- [[molecule.C00009|molecule.C00009]] `KEGG` `database` - C02133 + C00001 <=> C00060 + C00009
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C02133 + C00001 <=> C00060 + C00009
- `is_substrate_of` <-- [[molecule.C02133|molecule.C02133]] `KEGG` `database` - C02133 + C00001 <=> C00060 + C00009

## External IDs

- `KEGG:R00539`

## Notes

EQUATION: C02133 + C00001 <=> C00060 + C00009
