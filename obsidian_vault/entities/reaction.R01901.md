---
entity_id: "reaction.R01901"
entity_type: "reaction"
name: "ATP:L-xylulose 5-phosphotransferase"
source_database: "KEGG"
source_id: "R01901"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R01901"
---

# ATP:L-xylulose 5-phosphotransferase

`reaction.R01901`

## Static

- Type: `reaction`
- Source: `KEGG:R01901`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ATP + L-Xylulose ADP + L-Xylulose 5-phosphate

## Biological Role

Catalyzed by lyx (protein.P37677). Substrates: ATP (molecule.C00002), L-Xylulose (molecule.C00312). Products: ADP (molecule.C00008), L-Xylulose 5-phosphate (molecule.C03291).

## Annotation

ATP + L-Xylulose <=> ADP + L-Xylulose 5-phosphate

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P37677|protein.P37677]] `KEGG` `database` - via EC:2.7.1.53
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `KEGG` `database` - C00002 + C00312 <=> C00008 + C03291
- `is_product_of` <-- [[molecule.C03291|molecule.C03291]] `KEGG` `database` - C00002 + C00312 <=> C00008 + C03291
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `KEGG` `database` - C00002 + C00312 <=> C00008 + C03291
- `is_substrate_of` <-- [[molecule.C00312|molecule.C00312]] `KEGG` `database` - C00002 + C00312 <=> C00008 + C03291

## External IDs

- `KEGG:R01901`

## Notes

EQUATION: C00002 + C00312 <=> C00008 + C03291
