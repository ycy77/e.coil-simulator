---
entity_id: "reaction.R00760"
entity_type: "reaction"
name: "ATP:D-fructose 6-phosphotransferase"
source_database: "KEGG"
source_id: "R00760"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00760"
---

# ATP:D-fructose 6-phosphotransferase

`reaction.R00760`

## Static

- Type: `reaction`
- Source: `KEGG:R00760`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ATP + D-Fructose ADP + D-Fructose 6-phosphate

## Biological Role

Catalyzed by mak (protein.P23917). Substrates: ATP (molecule.C00002), D-Fructose (molecule.C00095). Products: ADP (molecule.C00008), D-Fructose 6-phosphate (molecule.C00085).

## Annotation

ATP + D-Fructose <=> ADP + D-Fructose 6-phosphate

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P23917|protein.P23917]] `KEGG` `database` - via EC:2.7.1.4
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `KEGG` `database` - C00002 + C00095 <=> C00008 + C00085
- `is_product_of` <-- [[molecule.C00085|molecule.C00085]] `KEGG` `database` - C00002 + C00095 <=> C00008 + C00085
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `KEGG` `database` - C00002 + C00095 <=> C00008 + C00085
- `is_substrate_of` <-- [[molecule.C00095|molecule.C00095]] `KEGG` `database` - C00002 + C00095 <=> C00008 + C00085

## External IDs

- `KEGG:R00760`

## Notes

EQUATION: C00002 + C00095 <=> C00008 + C00085
