---
entity_id: "reaction.R00570"
entity_type: "reaction"
name: "ATP:CDP phosphotransferase"
source_database: "KEGG"
source_id: "R00570"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00570"
---

# ATP:CDP phosphotransferase

`reaction.R00570`

## Static

- Type: `reaction`
- Source: `KEGG:R00570`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ATP + CDP ADP + CTP

## Biological Role

Catalyzed by ndk (protein.P0A763). Substrates: ATP (molecule.C00002), CDP (molecule.C00112). Products: ADP (molecule.C00008), CTP (molecule.C00063).

## Annotation

ATP + CDP <=> ADP + CTP

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P0A763|protein.P0A763]] `KEGG` `database` - via EC:2.7.4.6
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `KEGG` `database` - C00002 + C00112 <=> C00008 + C00063
- `is_product_of` <-- [[molecule.C00063|molecule.C00063]] `KEGG` `database` - C00002 + C00112 <=> C00008 + C00063
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `KEGG` `database` - C00002 + C00112 <=> C00008 + C00063
- `is_substrate_of` <-- [[molecule.C00112|molecule.C00112]] `KEGG` `database` - C00002 + C00112 <=> C00008 + C00063

## External IDs

- `KEGG:R00570`

## Notes

EQUATION: C00002 + C00112 <=> C00008 + C00063
