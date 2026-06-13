---
entity_id: "reaction.R00847"
entity_type: "reaction"
name: "ATP:glycerol 3-phosphotransferase"
source_database: "KEGG"
source_id: "R00847"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00847"
---

# ATP:glycerol 3-phosphotransferase

`reaction.R00847`

## Static

- Type: `reaction`
- Source: `KEGG:R00847`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ATP + Glycerol ADP + sn-Glycerol 3-phosphate

## Biological Role

Catalyzed by glpK (protein.P0A6F3). Substrates: ATP (molecule.C00002), Glycerol (molecule.C00116). Products: ADP (molecule.C00008), sn-Glycerol 3-phosphate (molecule.C00093).

## Annotation

ATP + Glycerol <=> ADP + sn-Glycerol 3-phosphate

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P0A6F3|protein.P0A6F3]] `KEGG` `database` - via EC:2.7.1.30
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `KEGG` `database` - C00002 + C00116 <=> C00008 + C00093
- `is_product_of` <-- [[molecule.C00093|molecule.C00093]] `KEGG` `database` - C00002 + C00116 <=> C00008 + C00093
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `KEGG` `database` - C00002 + C00116 <=> C00008 + C00093
- `is_substrate_of` <-- [[molecule.C00116|molecule.C00116]] `KEGG` `database` - C00002 + C00116 <=> C00008 + C00093

## External IDs

- `KEGG:R00847`

## Notes

EQUATION: C00002 + C00116 <=> C00008 + C00093
