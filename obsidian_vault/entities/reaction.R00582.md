---
entity_id: "reaction.R00582"
entity_type: "reaction"
name: "O-phospho-L-serine phosphohydrolase"
source_database: "KEGG"
source_id: "R00582"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00582"
---

# O-phospho-L-serine phosphohydrolase

`reaction.R00582`

## Static

- Type: `reaction`
- Source: `KEGG:R00582`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

O-Phospho-L-serine + H2O L-Serine + Orthophosphate

## Biological Role

Catalyzed by serB (protein.P0AGB0). Substrates: H2O (molecule.C00001), O-Phospho-L-serine (molecule.C01005). Products: Orthophosphate (molecule.C00009), L-Serine (molecule.C00065).

## Annotation

O-Phospho-L-serine + H2O <=> L-Serine + Orthophosphate

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P0AGB0|protein.P0AGB0]] `KEGG` `database` - via EC:3.1.3.3
- `is_product_of` <-- [[molecule.C00009|molecule.C00009]] `KEGG` `database` - C01005 + C00001 <=> C00065 + C00009
- `is_product_of` <-- [[molecule.C00065|molecule.C00065]] `KEGG` `database` - C01005 + C00001 <=> C00065 + C00009
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C01005 + C00001 <=> C00065 + C00009
- `is_substrate_of` <-- [[molecule.C01005|molecule.C01005]] `KEGG` `database` - C01005 + C00001 <=> C00065 + C00009

## External IDs

- `KEGG:R00582`

## Notes

EQUATION: C01005 + C00001 <=> C00065 + C00009
