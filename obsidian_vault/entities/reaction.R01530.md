---
entity_id: "reaction.R01530"
entity_type: "reaction"
name: "D-arabinose-5-phosphate aldose-ketose-isomerase"
source_database: "KEGG"
source_id: "R01530"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R01530"
---

# D-arabinose-5-phosphate aldose-ketose-isomerase

`reaction.R01530`

## Static

- Type: `reaction`
- Source: `KEGG:R01530`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

D-Arabinose 5-phosphate D-Ribulose 5-phosphate

## Biological Role

Catalyzed by gutQ (protein.P17115), kdsD (protein.P45395). Substrates: D-Arabinose 5-phosphate (molecule.C01112). Products: D-Ribulose 5-phosphate (molecule.C00199).

## Annotation

D-Arabinose 5-phosphate <=> D-Ribulose 5-phosphate

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[protein.P17115|protein.P17115]] `KEGG` `database` - via EC:5.3.1.13
- `catalyzes` <-- [[protein.P45395|protein.P45395]] `KEGG` `database` - via EC:5.3.1.13
- `is_product_of` <-- [[molecule.C00199|molecule.C00199]] `KEGG` `database` - C01112 <=> C00199
- `is_substrate_of` <-- [[molecule.C01112|molecule.C01112]] `KEGG` `database` - C01112 <=> C00199

## External IDs

- `KEGG:R01530`

## Notes

EQUATION: C01112 <=> C00199
