---
entity_id: "reaction.R00756"
entity_type: "reaction"
name: "ATP:D-fructose-6-phosphate 1-phosphotransferase"
source_database: "KEGG"
source_id: "R00756"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00756"
---

# ATP:D-fructose-6-phosphate 1-phosphotransferase

`reaction.R00756`

## Static

- Type: `reaction`
- Source: `KEGG:R00756`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ATP + D-Fructose 6-phosphate ADP + D-Fructose 1,6-bisphosphate

## Biological Role

Catalyzed by pfkB (protein.P06999), pfkA (protein.P0A796). Substrates: ATP (molecule.C00002), D-Fructose 6-phosphate (molecule.C00085). Products: ADP (molecule.C00008), D-Fructose 1,6-bisphosphate (molecule.C00354).

## Annotation

ATP + D-Fructose 6-phosphate <=> ADP + D-Fructose 1,6-bisphosphate

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P06999|protein.P06999]] `KEGG` `database` - via EC:2.7.1.11
- `catalyzes` <-- [[protein.P0A796|protein.P0A796]] `KEGG` `database` - via EC:2.7.1.11
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `KEGG` `database` - C00002 + C00085 <=> C00008 + C00354
- `is_product_of` <-- [[molecule.C00354|molecule.C00354]] `KEGG` `database` - C00002 + C00085 <=> C00008 + C00354
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `KEGG` `database` - C00002 + C00085 <=> C00008 + C00354
- `is_substrate_of` <-- [[molecule.C00085|molecule.C00085]] `KEGG` `database` - C00002 + C00085 <=> C00008 + C00354

## External IDs

- `KEGG:R00756`

## Notes

EQUATION: C00002 + C00085 <=> C00008 + C00354
