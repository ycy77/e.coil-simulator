---
entity_id: "reaction.R00571"
entity_type: "reaction"
name: "UTP:ammonia ligase (ADP-forming)"
source_database: "KEGG"
source_id: "R00571"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00571"
---

# UTP:ammonia ligase (ADP-forming)

`reaction.R00571`

## Static

- Type: `reaction`
- Source: `KEGG:R00571`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ATP + UTP + Ammonia ADP + Orthophosphate + CTP

## Biological Role

Catalyzed by pyrG (protein.P0A7E5). Substrates: ATP (molecule.C00002), Ammonia (molecule.C00014), UTP (molecule.C00075). Products: ADP (molecule.C00008), Orthophosphate (molecule.C00009), CTP (molecule.C00063).

## Annotation

ATP + UTP + Ammonia <=> ADP + Orthophosphate + CTP

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[protein.P0A7E5|protein.P0A7E5]] `KEGG` `database` - via EC:6.3.4.2
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `KEGG` `database` - C00002 + C00075 + C00014 <=> C00008 + C00009 + C00063
- `is_product_of` <-- [[molecule.C00009|molecule.C00009]] `KEGG` `database` - C00002 + C00075 + C00014 <=> C00008 + C00009 + C00063
- `is_product_of` <-- [[molecule.C00063|molecule.C00063]] `KEGG` `database` - C00002 + C00075 + C00014 <=> C00008 + C00009 + C00063
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `KEGG` `database` - C00002 + C00075 + C00014 <=> C00008 + C00009 + C00063
- `is_substrate_of` <-- [[molecule.C00014|molecule.C00014]] `KEGG` `database` - C00002 + C00075 + C00014 <=> C00008 + C00009 + C00063
- `is_substrate_of` <-- [[molecule.C00075|molecule.C00075]] `KEGG` `database` - C00002 + C00075 + C00014 <=> C00008 + C00009 + C00063

## External IDs

- `KEGG:R00571`

## Notes

EQUATION: C00002 + C00075 + C00014 <=> C00008 + C00009 + C00063
