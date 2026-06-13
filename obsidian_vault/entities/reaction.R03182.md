---
entity_id: "reaction.R03182"
entity_type: "reaction"
name: "7,8-diaminononanoate:carbon-dioxide cyclo-ligase"
source_database: "KEGG"
source_id: "R03182"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R03182"
---

# 7,8-diaminononanoate:carbon-dioxide cyclo-ligase

`reaction.R03182`

## Static

- Type: `reaction`
- Source: `KEGG:R03182`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ATP + 7,8-Diaminononanoate + CO2 ADP + Orthophosphate + Dethiobiotin

## Biological Role

Catalyzed by bioD2 (protein.P0A6E9), bioD1 (protein.P13000). Substrates: ATP (molecule.C00002), CO2 (molecule.C00011), 7,8-Diaminononanoate (molecule.C01037). Products: ADP (molecule.C00008), Orthophosphate (molecule.C00009), Dethiobiotin (molecule.C01909).

## Annotation

ATP + 7,8-Diaminononanoate + CO2 <=> ADP + Orthophosphate + Dethiobiotin

## Outgoing Edges (0)

_None._

## Incoming Edges (8)

- `catalyzes` <-- [[protein.P0A6E9|protein.P0A6E9]] `KEGG` `database` - via EC:6.3.3.3
- `catalyzes` <-- [[protein.P13000|protein.P13000]] `KEGG` `database` - via EC:6.3.3.3
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `KEGG` `database` - C00002 + C01037 + C00011 <=> C00008 + C00009 + C01909
- `is_product_of` <-- [[molecule.C00009|molecule.C00009]] `KEGG` `database` - C00002 + C01037 + C00011 <=> C00008 + C00009 + C01909
- `is_product_of` <-- [[molecule.C01909|molecule.C01909]] `KEGG` `database` - C00002 + C01037 + C00011 <=> C00008 + C00009 + C01909
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `KEGG` `database` - C00002 + C01037 + C00011 <=> C00008 + C00009 + C01909
- `is_substrate_of` <-- [[molecule.C00011|molecule.C00011]] `KEGG` `database` - C00002 + C01037 + C00011 <=> C00008 + C00009 + C01909
- `is_substrate_of` <-- [[molecule.C01037|molecule.C01037]] `KEGG` `database` - C00002 + C01037 + C00011 <=> C00008 + C00009 + C01909

## External IDs

- `KEGG:R03182`

## Notes

EQUATION: C00002 + C01037 + C00011 <=> C00008 + C00009 + C01909
