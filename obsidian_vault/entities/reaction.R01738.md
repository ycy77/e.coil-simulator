---
entity_id: "reaction.R01738"
entity_type: "reaction"
name: "D-gluconate:NAD+ 5-oxidoreductase"
source_database: "KEGG"
source_id: "R01738"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R01738"
---

# D-gluconate:NAD+ 5-oxidoreductase

`reaction.R01738`

## Static

- Type: `reaction`
- Source: `KEGG:R01738`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

D-Gluconic acid + NAD+ 5-Dehydro-D-gluconate + NADH + H+

## Biological Role

Catalyzed by idnO (protein.P0A9P9). Substrates: NAD+ (molecule.C00003), D-Gluconic acid (molecule.C00257). Products: NADH (molecule.C00004), H+ (molecule.C00080).

## Annotation

D-Gluconic acid + NAD+ <=> 5-Dehydro-D-gluconate + NADH + H+

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P0A9P9|protein.P0A9P9]] `KEGG` `database` - via EC:1.1.1.69
- `is_product_of` <-- [[molecule.C00004|molecule.C00004]] `KEGG` `database` - C00257 + C00003 <=> C01062 + C00004 + C00080
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `KEGG` `database` - C00257 + C00003 <=> C01062 + C00004 + C00080
- `is_substrate_of` <-- [[molecule.C00003|molecule.C00003]] `KEGG` `database` - C00257 + C00003 <=> C01062 + C00004 + C00080
- `is_substrate_of` <-- [[molecule.C00257|molecule.C00257]] `KEGG` `database` - C00257 + C00003 <=> C01062 + C00004 + C00080

## External IDs

- `KEGG:R01738`

## Notes

EQUATION: C00257 + C00003 <=> C01062 + C00004 + C00080
