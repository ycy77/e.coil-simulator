---
entity_id: "reaction.R00124"
entity_type: "reaction"
name: "ATP:ADP phosphatransferase"
source_database: "KEGG"
source_id: "R00124"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00124"
---

# ATP:ADP phosphatransferase

`reaction.R00124`

## Static

- Type: `reaction`
- Source: `KEGG:R00124`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ATP + ADP ADP + ATP

## Biological Role

Catalyzed by ndk (protein.P0A763). Substrates: ATP (molecule.C00002), ADP (molecule.C00008). Products: ATP (molecule.C00002), ADP (molecule.C00008).

## Annotation

ATP + ADP <=> ADP + ATP

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P0A763|protein.P0A763]] `KEGG` `database` - via EC:2.7.4.6
- `is_product_of` <-- [[molecule.C00002|molecule.C00002]] `KEGG` `database` - C00002 + C00008 <=> C00008 + C00002
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `KEGG` `database` - C00002 + C00008 <=> C00008 + C00002
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `KEGG` `database` - C00002 + C00008 <=> C00008 + C00002
- `is_substrate_of` <-- [[molecule.C00008|molecule.C00008]] `KEGG` `database` - C00002 + C00008 <=> C00008 + C00002

## External IDs

- `KEGG:R00124`

## Notes

EQUATION: C00002 + C00008 <=> C00008 + C00002
