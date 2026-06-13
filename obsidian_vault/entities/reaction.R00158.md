---
entity_id: "reaction.R00158"
entity_type: "reaction"
name: "ATP:UMP phosphotransferase"
source_database: "KEGG"
source_id: "R00158"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00158"
---

# ATP:UMP phosphotransferase

`reaction.R00158`

## Static

- Type: `reaction`
- Source: `KEGG:R00158`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ATP + UMP ADP + UDP

## Biological Role

Catalyzed by pyrH (protein.P0A7E9). Substrates: ATP (molecule.C00002), UMP (molecule.C00105). Products: ADP (molecule.C00008), UDP (molecule.C00015).

## Annotation

ATP + UMP <=> ADP + UDP

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P0A7E9|protein.P0A7E9]] `KEGG` `database` - via EC:2.7.4.22
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `KEGG` `database` - C00002 + C00105 <=> C00008 + C00015
- `is_product_of` <-- [[molecule.C00015|molecule.C00015]] `KEGG` `database` - C00002 + C00105 <=> C00008 + C00015
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `KEGG` `database` - C00002 + C00105 <=> C00008 + C00015
- `is_substrate_of` <-- [[molecule.C00105|molecule.C00105]] `KEGG` `database` - C00002 + C00105 <=> C00008 + C00015

## External IDs

- `KEGG:R00158`

## Notes

EQUATION: C00002 + C00105 <=> C00008 + C00015
