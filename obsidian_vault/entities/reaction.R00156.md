---
entity_id: "reaction.R00156"
entity_type: "reaction"
name: "ATP:UDP phosphotransferase"
source_database: "KEGG"
source_id: "R00156"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00156"
---

# ATP:UDP phosphotransferase

`reaction.R00156`

## Static

- Type: `reaction`
- Source: `KEGG:R00156`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ATP + UDP ADP + UTP

## Biological Role

Catalyzed by ndk (protein.P0A763). Substrates: ATP (molecule.C00002), UDP (molecule.C00015). Products: ADP (molecule.C00008), UTP (molecule.C00075).

## Annotation

ATP + UDP <=> ADP + UTP

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P0A763|protein.P0A763]] `KEGG` `database` - via EC:2.7.4.6
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `KEGG` `database` - C00002 + C00015 <=> C00008 + C00075
- `is_product_of` <-- [[molecule.C00075|molecule.C00075]] `KEGG` `database` - C00002 + C00015 <=> C00008 + C00075
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `KEGG` `database` - C00002 + C00015 <=> C00008 + C00075
- `is_substrate_of` <-- [[molecule.C00015|molecule.C00015]] `KEGG` `database` - C00002 + C00015 <=> C00008 + C00075

## External IDs

- `KEGG:R00156`

## Notes

EQUATION: C00002 + C00015 <=> C00008 + C00075
