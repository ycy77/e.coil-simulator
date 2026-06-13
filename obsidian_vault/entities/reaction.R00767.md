---
entity_id: "reaction.R00767"
entity_type: "reaction"
name: "CTP:D-fructose-6-phosphate 1-phosphotransferase"
source_database: "KEGG"
source_id: "R00767"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00767"
---

# CTP:D-fructose-6-phosphate 1-phosphotransferase

`reaction.R00767`

## Static

- Type: `reaction`
- Source: `KEGG:R00767`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CTP + D-Fructose 6-phosphate CDP + D-Fructose 1,6-bisphosphate

## Biological Role

Catalyzed by pfkB (protein.P06999), pfkA (protein.P0A796). Substrates: CTP (molecule.C00063), D-Fructose 6-phosphate (molecule.C00085). Products: CDP (molecule.C00112), D-Fructose 1,6-bisphosphate (molecule.C00354).

## Annotation

CTP + D-Fructose 6-phosphate <=> CDP + D-Fructose 1,6-bisphosphate

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P06999|protein.P06999]] `KEGG` `database` - via EC:2.7.1.11
- `catalyzes` <-- [[protein.P0A796|protein.P0A796]] `KEGG` `database` - via EC:2.7.1.11
- `is_product_of` <-- [[molecule.C00112|molecule.C00112]] `KEGG` `database` - C00063 + C00085 <=> C00112 + C00354
- `is_product_of` <-- [[molecule.C00354|molecule.C00354]] `KEGG` `database` - C00063 + C00085 <=> C00112 + C00354
- `is_substrate_of` <-- [[molecule.C00063|molecule.C00063]] `KEGG` `database` - C00063 + C00085 <=> C00112 + C00354
- `is_substrate_of` <-- [[molecule.C00085|molecule.C00085]] `KEGG` `database` - C00063 + C00085 <=> C00112 + C00354

## External IDs

- `KEGG:R00767`

## Notes

EQUATION: C00063 + C00085 <=> C00112 + C00354
