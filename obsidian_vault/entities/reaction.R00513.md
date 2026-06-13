---
entity_id: "reaction.R00513"
entity_type: "reaction"
name: "ATP:cytidine 5'-phosphotransferase"
source_database: "KEGG"
source_id: "R00513"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00513"
---

# ATP:cytidine 5'-phosphotransferase

`reaction.R00513`

## Static

- Type: `reaction`
- Source: `KEGG:R00513`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ATP + Cytidine ADP + CMP

## Biological Role

Catalyzed by udk (protein.P0A8F4). Substrates: ATP (molecule.C00002), Cytidine (molecule.C00475). Products: ADP (molecule.C00008), CMP (molecule.C00055).

## Annotation

ATP + Cytidine <=> ADP + CMP

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P0A8F4|protein.P0A8F4]] `KEGG` `database` - via EC:2.7.1.48
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `KEGG` `database` - C00002 + C00475 <=> C00008 + C00055
- `is_product_of` <-- [[molecule.C00055|molecule.C00055]] `KEGG` `database` - C00002 + C00475 <=> C00008 + C00055
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `KEGG` `database` - C00002 + C00475 <=> C00008 + C00055
- `is_substrate_of` <-- [[molecule.C00475|molecule.C00475]] `KEGG` `database` - C00002 + C00475 <=> C00008 + C00055

## External IDs

- `KEGG:R00513`

## Notes

EQUATION: C00002 + C00475 <=> C00008 + C00055
