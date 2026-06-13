---
entity_id: "reaction.R00307"
entity_type: "reaction"
name: "alpha-D-glucose aldose-ketose-isomerase"
source_database: "KEGG"
source_id: "R00307"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00307"
---

# alpha-D-glucose aldose-ketose-isomerase

`reaction.R00307`

## Static

- Type: `reaction`
- Source: `KEGG:R00307`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

alpha-D-Glucose alpha-D-Fructofuranose

## Biological Role

Catalyzed by xylA (protein.P00944). Substrates: alpha-D-Glucose (molecule.C00267).

## Annotation

alpha-D-Glucose <=> alpha-D-Fructofuranose

## Outgoing Edges (0)

_None._

## Incoming Edges (2)

- `catalyzes` <-- [[protein.P00944|protein.P00944]] `KEGG` `database` - via EC:5.3.1.5
- `is_substrate_of` <-- [[molecule.C00267|molecule.C00267]] `KEGG` `database` - C00267 <=> C22502

## External IDs

- `KEGG:R00307`

## Notes

EQUATION: C00267 <=> C22502
