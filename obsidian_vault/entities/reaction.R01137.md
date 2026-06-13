---
entity_id: "reaction.R01137"
entity_type: "reaction"
name: "ATP:dADP phosphotransferase"
source_database: "KEGG"
source_id: "R01137"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R01137"
---

# ATP:dADP phosphotransferase

`reaction.R01137`

## Static

- Type: `reaction`
- Source: `KEGG:R01137`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ATP + dADP ADP + dATP

## Biological Role

Catalyzed by ndk (protein.P0A763). Substrates: ATP (molecule.C00002), dADP (molecule.C00206). Products: ADP (molecule.C00008), dATP (molecule.C00131).

## Annotation

ATP + dADP <=> ADP + dATP

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P0A763|protein.P0A763]] `KEGG` `database` - via EC:2.7.4.6
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `KEGG` `database` - C00002 + C00206 <=> C00008 + C00131
- `is_product_of` <-- [[molecule.C00131|molecule.C00131]] `KEGG` `database` - C00002 + C00206 <=> C00008 + C00131
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `KEGG` `database` - C00002 + C00206 <=> C00008 + C00131
- `is_substrate_of` <-- [[molecule.C00206|molecule.C00206]] `KEGG` `database` - C00002 + C00206 <=> C00008 + C00131

## External IDs

- `KEGG:R01137`

## Notes

EQUATION: C00002 + C00206 <=> C00008 + C00131
