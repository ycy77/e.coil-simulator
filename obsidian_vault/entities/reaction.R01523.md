---
entity_id: "reaction.R01523"
entity_type: "reaction"
name: "ATP:D-ribulose-5-phosphate 1-phosphotransferase"
source_database: "KEGG"
source_id: "R01523"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R01523"
---

# ATP:D-ribulose-5-phosphate 1-phosphotransferase

`reaction.R01523`

## Static

- Type: `reaction`
- Source: `KEGG:R01523`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ATP + D-Ribulose 5-phosphate ADP + D-Ribulose 1,5-bisphosphate

## Biological Role

Catalyzed by prkB (protein.P0AEX5). Substrates: ATP (molecule.C00002), D-Ribulose 5-phosphate (molecule.C00199). Products: ADP (molecule.C00008), D-Ribulose 1,5-bisphosphate (molecule.C01182).

## Annotation

ATP + D-Ribulose 5-phosphate <=> ADP + D-Ribulose 1,5-bisphosphate

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P0AEX5|protein.P0AEX5]] `KEGG` `database` - via EC:2.7.1.19
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `KEGG` `database` - C00002 + C00199 <=> C00008 + C01182
- `is_product_of` <-- [[molecule.C01182|molecule.C01182]] `KEGG` `database` - C00002 + C00199 <=> C00008 + C01182
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `KEGG` `database` - C00002 + C00199 <=> C00008 + C01182
- `is_substrate_of` <-- [[molecule.C00199|molecule.C00199]] `KEGG` `database` - C00002 + C00199 <=> C00008 + C01182

## External IDs

- `KEGG:R01523`

## Notes

EQUATION: C00002 + C00199 <=> C00008 + C01182
