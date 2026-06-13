---
entity_id: "reaction.R10948"
entity_type: "reaction"
name: "ATP:HCO3- phosphotransferase"
source_database: "KEGG"
source_id: "R10948"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R10948"
---

# ATP:HCO3- phosphotransferase

`reaction.R10948`

## Static

- Type: `reaction`
- Source: `KEGG:R10948`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ATP + HCO3- ADP + Carboxyphosphate

## Biological Role

Catalyzed by carB (protein.P00968), carA (protein.P0A6F1). Substrates: ATP (molecule.C00002), HCO3- (molecule.C00288). Products: ADP (molecule.C00008).

## Annotation

ATP + HCO3- <=> ADP + Carboxyphosphate

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P00968|protein.P00968]] `KEGG` `database` - via EC:6.3.5.5
- `catalyzes` <-- [[protein.P0A6F1|protein.P0A6F1]] `KEGG` `database` - via EC:6.3.5.5
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `KEGG` `database` - C00002 + C00288 <=> C00008 + C20969
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `KEGG` `database` - C00002 + C00288 <=> C00008 + C20969
- `is_substrate_of` <-- [[molecule.C00288|molecule.C00288]] `KEGG` `database` - C00002 + C00288 <=> C00008 + C20969

## External IDs

- `KEGG:R10948`

## Notes

EQUATION: C00002 + C00288 <=> C00008 + C20969
