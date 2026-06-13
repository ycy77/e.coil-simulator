---
entity_id: "reaction.R02331"
entity_type: "reaction"
name: "ATP:dUDP phosphotransferase"
source_database: "KEGG"
source_id: "R02331"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R02331"
---

# ATP:dUDP phosphotransferase

`reaction.R02331`

## Static

- Type: `reaction`
- Source: `KEGG:R02331`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ATP + dUDP ADP + dUTP

## Biological Role

Catalyzed by ndk (protein.P0A763). Substrates: ATP (molecule.C00002), dUDP (molecule.C01346). Products: ADP (molecule.C00008), dUTP (molecule.C00460).

## Annotation

ATP + dUDP <=> ADP + dUTP

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P0A763|protein.P0A763]] `KEGG` `database` - via EC:2.7.4.6
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `KEGG` `database` - C00002 + C01346 <=> C00008 + C00460
- `is_product_of` <-- [[molecule.C00460|molecule.C00460]] `KEGG` `database` - C00002 + C01346 <=> C00008 + C00460
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `KEGG` `database` - C00002 + C01346 <=> C00008 + C00460
- `is_substrate_of` <-- [[molecule.C01346|molecule.C01346]] `KEGG` `database` - C00002 + C01346 <=> C00008 + C00460

## External IDs

- `KEGG:R02331`

## Notes

EQUATION: C00002 + C01346 <=> C00008 + C00460
