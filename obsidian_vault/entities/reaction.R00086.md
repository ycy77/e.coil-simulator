---
entity_id: "reaction.R00086"
entity_type: "reaction"
name: "ATP phosphohydrolase"
source_database: "KEGG"
source_id: "R00086"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00086"
---

# ATP phosphohydrolase

`reaction.R00086`

## Static

- Type: `reaction`
- Source: `KEGG:R00086`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ATP + H2O ADP + Orthophosphate

## Biological Role

Catalyzed by atpA (protein.P0ABB0), atpD (protein.P0ABB4). Substrates: H2O (molecule.C00001), ATP (molecule.C00002). Products: ADP (molecule.C00008), Orthophosphate (molecule.C00009).

## Annotation

ATP + H2O <=> ADP + Orthophosphate

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P0ABB0|protein.P0ABB0]] `KEGG` `database` - via EC:7.1.2.2
- `catalyzes` <-- [[protein.P0ABB4|protein.P0ABB4]] `KEGG` `database` - via EC:7.1.2.2
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `KEGG` `database` - C00002 + C00001 <=> C00008 + C00009
- `is_product_of` <-- [[molecule.C00009|molecule.C00009]] `KEGG` `database` - C00002 + C00001 <=> C00008 + C00009
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C00002 + C00001 <=> C00008 + C00009
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `KEGG` `database` - C00002 + C00001 <=> C00008 + C00009

## External IDs

- `KEGG:R00086`

## Notes

EQUATION: C00002 + C00001 <=> C00008 + C00009
