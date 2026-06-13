---
entity_id: "reaction.R00330"
entity_type: "reaction"
name: "ATP:GDP phosphotransferase"
source_database: "KEGG"
source_id: "R00330"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00330"
---

# ATP:GDP phosphotransferase

`reaction.R00330`

## Static

- Type: `reaction`
- Source: `KEGG:R00330`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ATP + GDP ADP + GTP

## Biological Role

Catalyzed by ndk (protein.P0A763). Substrates: ATP (molecule.C00002), GDP (molecule.C00035). Products: ADP (molecule.C00008), GTP (molecule.C00044).

## Annotation

ATP + GDP <=> ADP + GTP

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P0A763|protein.P0A763]] `KEGG` `database` - via EC:2.7.4.6
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `KEGG` `database` - C00002 + C00035 <=> C00008 + C00044
- `is_product_of` <-- [[molecule.C00044|molecule.C00044]] `KEGG` `database` - C00002 + C00035 <=> C00008 + C00044
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `KEGG` `database` - C00002 + C00035 <=> C00008 + C00044
- `is_substrate_of` <-- [[molecule.C00035|molecule.C00035]] `KEGG` `database` - C00002 + C00035 <=> C00008 + C00044

## External IDs

- `KEGG:R00330`

## Notes

EQUATION: C00002 + C00035 <=> C00008 + C00044
