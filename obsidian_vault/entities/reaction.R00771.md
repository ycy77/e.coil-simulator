---
entity_id: "reaction.R00771"
entity_type: "reaction"
name: "D-glucose-6-phosphate aldose-ketose-isomerase"
source_database: "KEGG"
source_id: "R00771"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00771"
---

# D-glucose-6-phosphate aldose-ketose-isomerase

`reaction.R00771`

## Static

- Type: `reaction`
- Source: `KEGG:R00771`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

D-Glucose 6-phosphate D-Fructose 6-phosphate

## Biological Role

Catalyzed by pgi (protein.P0A6T1). Substrates: D-Glucose 6-phosphate (molecule.C00092). Products: D-Fructose 6-phosphate (molecule.C00085).

## Annotation

D-Glucose 6-phosphate <=> D-Fructose 6-phosphate

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.P0A6T1|protein.P0A6T1]] `KEGG` `database` - via EC:5.3.1.9
- `is_product_of` <-- [[molecule.C00085|molecule.C00085]] `KEGG` `database` - C00092 <=> C00085
- `is_substrate_of` <-- [[molecule.C00092|molecule.C00092]] `KEGG` `database` - C00092 <=> C00085

## External IDs

- `KEGG:R00771`

## Notes

EQUATION: C00092 <=> C00085
