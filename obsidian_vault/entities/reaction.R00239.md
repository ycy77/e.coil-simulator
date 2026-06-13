---
entity_id: "reaction.R00239"
entity_type: "reaction"
name: "ATP:L-glutamate 5-phosphotransferase"
source_database: "KEGG"
source_id: "R00239"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00239"
---

# ATP:L-glutamate 5-phosphotransferase

`reaction.R00239`

## Static

- Type: `reaction`
- Source: `KEGG:R00239`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ATP + L-Glutamate ADP + L-Glutamyl 5-phosphate

## Biological Role

Catalyzed by proB (protein.P0A7B5). Substrates: ATP (molecule.C00002), L-Glutamate (molecule.C00025). Products: ADP (molecule.C00008), L-Glutamyl 5-phosphate (molecule.C03287).

## Annotation

ATP + L-Glutamate <=> ADP + L-Glutamyl 5-phosphate

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P0A7B5|protein.P0A7B5]] `KEGG` `database` - via EC:2.7.2.11
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `KEGG` `database` - C00002 + C00025 <=> C00008 + C03287
- `is_product_of` <-- [[molecule.C03287|molecule.C03287]] `KEGG` `database` - C00002 + C00025 <=> C00008 + C03287
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `KEGG` `database` - C00002 + C00025 <=> C00008 + C03287
- `is_substrate_of` <-- [[molecule.C00025|molecule.C00025]] `KEGG` `database` - C00002 + C00025 <=> C00008 + C03287

## External IDs

- `KEGG:R00239`

## Notes

EQUATION: C00002 + C00025 <=> C00008 + C03287
