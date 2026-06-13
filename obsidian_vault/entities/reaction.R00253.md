---
entity_id: "reaction.R00253"
entity_type: "reaction"
name: "L-glutamate:ammonia ligase (ADP-forming)"
source_database: "KEGG"
source_id: "R00253"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00253"
---

# L-glutamate:ammonia ligase (ADP-forming)

`reaction.R00253`

## Static

- Type: `reaction`
- Source: `KEGG:R00253`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ATP + L-Glutamate + Ammonia ADP + Orthophosphate + L-Glutamine

## Biological Role

Catalyzed by glnA (protein.P0A9C5). Substrates: ATP (molecule.C00002), Ammonia (molecule.C00014), L-Glutamate (molecule.C00025). Products: ADP (molecule.C00008), Orthophosphate (molecule.C00009), L-Glutamine (molecule.C00064).

## Annotation

ATP + L-Glutamate + Ammonia <=> ADP + Orthophosphate + L-Glutamine

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[protein.P0A9C5|protein.P0A9C5]] `KEGG` `database` - via EC:6.3.1.2
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `KEGG` `database` - C00002 + C00025 + C00014 <=> C00008 + C00009 + C00064
- `is_product_of` <-- [[molecule.C00009|molecule.C00009]] `KEGG` `database` - C00002 + C00025 + C00014 <=> C00008 + C00009 + C00064
- `is_product_of` <-- [[molecule.C00064|molecule.C00064]] `KEGG` `database` - C00002 + C00025 + C00014 <=> C00008 + C00009 + C00064
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `KEGG` `database` - C00002 + C00025 + C00014 <=> C00008 + C00009 + C00064
- `is_substrate_of` <-- [[molecule.C00014|molecule.C00014]] `KEGG` `database` - C00002 + C00025 + C00014 <=> C00008 + C00009 + C00064
- `is_substrate_of` <-- [[molecule.C00025|molecule.C00025]] `KEGG` `database` - C00002 + C00025 + C00014 <=> C00008 + C00009 + C00064

## External IDs

- `KEGG:R00253`

## Notes

EQUATION: C00002 + C00025 + C00014 <=> C00008 + C00009 + C00064
