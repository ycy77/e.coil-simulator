---
entity_id: "reaction.R02134"
entity_type: "reaction"
name: "ATP:thiamine phosphotransferase"
source_database: "KEGG"
source_id: "R02134"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R02134"
---

# ATP:thiamine phosphotransferase

`reaction.R02134`

## Static

- Type: `reaction`
- Source: `KEGG:R02134`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ATP + Thiamine ADP + Thiamin monophosphate

## Biological Role

Catalyzed by thiK (protein.P75948). Substrates: ATP (molecule.C00002), Thiamine (molecule.C00378). Products: ADP (molecule.C00008), Thiamin monophosphate (molecule.C01081).

## Annotation

ATP + Thiamine <=> ADP + Thiamin monophosphate

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P75948|protein.P75948]] `KEGG` `database` - via EC:2.7.1.89
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `KEGG` `database` - C00002 + C00378 <=> C00008 + C01081
- `is_product_of` <-- [[molecule.C01081|molecule.C01081]] `KEGG` `database` - C00002 + C00378 <=> C00008 + C01081
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `KEGG` `database` - C00002 + C00378 <=> C00008 + C01081
- `is_substrate_of` <-- [[molecule.C00378|molecule.C00378]] `KEGG` `database` - C00002 + C00378 <=> C00008 + C01081

## External IDs

- `KEGG:R02134`

## Notes

EQUATION: C00002 + C00378 <=> C00008 + C01081
