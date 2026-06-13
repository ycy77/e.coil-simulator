---
entity_id: "reaction.R00173"
entity_type: "reaction"
name: "pyridoxal-5'-phosphate phosphohydrolase"
source_database: "KEGG"
source_id: "R00173"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00173"
---

# pyridoxal-5'-phosphate phosphohydrolase

`reaction.R00173`

## Static

- Type: `reaction`
- Source: `KEGG:R00173`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Pyridoxal phosphate + H2O Pyridoxal + Orthophosphate

## Biological Role

Catalyzed by ybhA (protein.P21829), yigL (protein.P27848). Substrates: H2O (molecule.C00001), Pyridoxal phosphate (molecule.C00018). Products: Orthophosphate (molecule.C00009), Pyridoxal (molecule.C00250).

## Annotation

Pyridoxal phosphate + H2O <=> Pyridoxal + Orthophosphate

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P21829|protein.P21829]] `KEGG` `database` - via EC:3.1.3.74
- `catalyzes` <-- [[protein.P27848|protein.P27848]] `KEGG` `database` - via EC:3.1.3.74
- `is_product_of` <-- [[molecule.C00009|molecule.C00009]] `KEGG` `database` - C00018 + C00001 <=> C00250 + C00009
- `is_product_of` <-- [[molecule.C00250|molecule.C00250]] `KEGG` `database` - C00018 + C00001 <=> C00250 + C00009
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C00018 + C00001 <=> C00250 + C00009
- `is_substrate_of` <-- [[molecule.C00018|molecule.C00018]] `KEGG` `database` - C00018 + C00001 <=> C00250 + C00009

## External IDs

- `KEGG:R00173`

## Notes

EQUATION: C00018 + C00001 <=> C00250 + C00009
