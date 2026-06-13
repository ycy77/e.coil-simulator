---
entity_id: "reaction.R01902"
entity_type: "reaction"
name: "ATP:L-xylulose 1-phosphotransferase"
source_database: "KEGG"
source_id: "R01902"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R01902"
---

# ATP:L-xylulose 1-phosphotransferase

`reaction.R01902`

## Static

- Type: `reaction`
- Source: `KEGG:R01902`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ATP + L-Xylulose ADP + L-Xylulose 1-phosphate

## Biological Role

Catalyzed by rhaB (protein.P32171). Substrates: ATP (molecule.C00002), L-Xylulose (molecule.C00312). Products: ADP (molecule.C00008), L-Xylulose 1-phosphate (molecule.C06441).

## Annotation

ATP + L-Xylulose <=> ADP + L-Xylulose 1-phosphate

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P32171|protein.P32171]] `KEGG` `database` - via EC:2.7.1.5
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `KEGG` `database` - C00002 + C00312 <=> C00008 + C06441
- `is_product_of` <-- [[molecule.C06441|molecule.C06441]] `KEGG` `database` - C00002 + C00312 <=> C00008 + C06441
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `KEGG` `database` - C00002 + C00312 <=> C00008 + C06441
- `is_substrate_of` <-- [[molecule.C00312|molecule.C00312]] `KEGG` `database` - C00002 + C00312 <=> C00008 + C06441

## External IDs

- `KEGG:R01902`

## Notes

EQUATION: C00002 + C00312 <=> C00008 + C06441
