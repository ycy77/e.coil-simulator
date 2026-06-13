---
entity_id: "reaction.R01526"
entity_type: "reaction"
name: "ATP:D-ribulose 5-phosphotransferase"
source_database: "KEGG"
source_id: "R01526"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R01526"
---

# ATP:D-ribulose 5-phosphotransferase

`reaction.R01526`

## Static

- Type: `reaction`
- Source: `KEGG:R01526`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ATP + D-Ribulose ADP + D-Ribulose 5-phosphate

## Biological Role

Catalyzed by araB (protein.P08204). Substrates: ATP (molecule.C00002), D-Ribulose (molecule.C00309). Products: ADP (molecule.C00008), D-Ribulose 5-phosphate (molecule.C00199).

## Annotation

ATP + D-Ribulose <=> ADP + D-Ribulose 5-phosphate

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P08204|protein.P08204]] `KEGG` `database` - via EC:2.7.1.16
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `KEGG` `database` - C00002 + C00309 <=> C00008 + C00199
- `is_product_of` <-- [[molecule.C00199|molecule.C00199]] `KEGG` `database` - C00002 + C00309 <=> C00008 + C00199
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `KEGG` `database` - C00002 + C00309 <=> C00008 + C00199
- `is_substrate_of` <-- [[molecule.C00309|molecule.C00309]] `KEGG` `database` - C00002 + C00309 <=> C00008 + C00199

## External IDs

- `KEGG:R01526`

## Notes

EQUATION: C00002 + C00309 <=> C00008 + C00199
