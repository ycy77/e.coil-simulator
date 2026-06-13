---
entity_id: "reaction.R00512"
entity_type: "reaction"
name: "ATP:CMP phosphotransferase"
source_database: "KEGG"
source_id: "R00512"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00512"
---

# ATP:CMP phosphotransferase

`reaction.R00512`

## Static

- Type: `reaction`
- Source: `KEGG:R00512`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ATP + CMP ADP + CDP

## Biological Role

Catalyzed by cmk (protein.P0A6I0). Substrates: ATP (molecule.C00002), CMP (molecule.C00055). Products: ADP (molecule.C00008), CDP (molecule.C00112).

## Annotation

ATP + CMP <=> ADP + CDP

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P0A6I0|protein.P0A6I0]] `KEGG` `database` - via EC:2.7.4.25
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `KEGG` `database` - C00002 + C00055 <=> C00008 + C00112
- `is_product_of` <-- [[molecule.C00112|molecule.C00112]] `KEGG` `database` - C00002 + C00055 <=> C00008 + C00112
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `KEGG` `database` - C00002 + C00055 <=> C00008 + C00112
- `is_substrate_of` <-- [[molecule.C00055|molecule.C00055]] `KEGG` `database` - C00002 + C00055 <=> C00008 + C00112

## External IDs

- `KEGG:R00512`

## Notes

EQUATION: C00002 + C00055 <=> C00008 + C00112
