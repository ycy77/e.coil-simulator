---
entity_id: "reaction.R00765"
entity_type: "reaction"
name: "D-glucosamine-6-phosphate aminohydrolase (ketol isomerizing);"
source_database: "KEGG"
source_id: "R00765"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00765"
---

# D-glucosamine-6-phosphate aminohydrolase (ketol isomerizing);

`reaction.R00765`

## Static

- Type: `reaction`
- Source: `KEGG:R00765`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

D-Glucosamine 6-phosphate + H2O D-Fructose 6-phosphate + Ammonia

## Biological Role

Catalyzed by nagB (protein.P0A759). Substrates: H2O (molecule.C00001), D-Glucosamine 6-phosphate (molecule.C00352). Products: Ammonia (molecule.C00014), D-Fructose 6-phosphate (molecule.C00085).

## Annotation

D-Glucosamine 6-phosphate + H2O <=> D-Fructose 6-phosphate + Ammonia

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P0A759|protein.P0A759]] `KEGG` `database` - via EC:3.5.99.6
- `is_product_of` <-- [[molecule.C00014|molecule.C00014]] `KEGG` `database` - C00352 + C00001 <=> C00085 + C00014
- `is_product_of` <-- [[molecule.C00085|molecule.C00085]] `KEGG` `database` - C00352 + C00001 <=> C00085 + C00014
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C00352 + C00001 <=> C00085 + C00014
- `is_substrate_of` <-- [[molecule.C00352|molecule.C00352]] `KEGG` `database` - C00352 + C00001 <=> C00085 + C00014

## External IDs

- `KEGG:R00765`

## Notes

EQUATION: C00352 + C00001 <=> C00085 + C00014
