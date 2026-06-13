---
entity_id: "reaction.R01529"
entity_type: "reaction"
name: "D-ribulose-5-phosphate 3-epimerase"
source_database: "KEGG"
source_id: "R01529"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R01529"
---

# D-ribulose-5-phosphate 3-epimerase

`reaction.R01529`

## Static

- Type: `reaction`
- Source: `KEGG:R01529`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

D-Ribulose 5-phosphate D-Xylulose 5-phosphate

## Biological Role

Catalyzed by rpe (protein.P0AG07). Substrates: D-Ribulose 5-phosphate (molecule.C00199). Products: D-Xylulose 5-phosphate (molecule.C00231).

## Annotation

D-Ribulose 5-phosphate <=> D-Xylulose 5-phosphate

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.P0AG07|protein.P0AG07]] `KEGG` `database` - via EC:5.1.3.1
- `is_product_of` <-- [[molecule.C00231|molecule.C00231]] `KEGG` `database` - C00199 <=> C00231
- `is_substrate_of` <-- [[molecule.C00199|molecule.C00199]] `KEGG` `database` - C00199 <=> C00231

## External IDs

- `KEGG:R01529`

## Notes

EQUATION: C00199 <=> C00231
