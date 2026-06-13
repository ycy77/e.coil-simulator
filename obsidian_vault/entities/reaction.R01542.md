---
entity_id: "reaction.R01542"
entity_type: "reaction"
name: "2-dehydro-3-deoxy-D-gluconate:NAD+ 5-oxidoreductase"
source_database: "KEGG"
source_id: "R01542"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R01542"
---

# 2-dehydro-3-deoxy-D-gluconate:NAD+ 5-oxidoreductase

`reaction.R01542`

## Static

- Type: `reaction`
- Source: `KEGG:R01542`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

2-Dehydro-3-deoxy-D-gluconate + NAD+ (4S)-4,6-Dihydroxy-2,5-dioxohexanoate + NADH + H+

## Biological Role

Catalyzed by kduD (protein.P37769). Substrates: NAD+ (molecule.C00003), 2-Dehydro-3-deoxy-D-gluconate (molecule.C00204). Products: NADH (molecule.C00004), H+ (molecule.C00080), (4S)-4,6-Dihydroxy-2,5-dioxohexanoate (molecule.C04349).

## Annotation

2-Dehydro-3-deoxy-D-gluconate + NAD+ <=> (4S)-4,6-Dihydroxy-2,5-dioxohexanoate + NADH + H+

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P37769|protein.P37769]] `KEGG` `database` - via EC:1.1.1.127
- `is_product_of` <-- [[molecule.C00004|molecule.C00004]] `KEGG` `database` - C00204 + C00003 <=> C04349 + C00004 + C00080
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `KEGG` `database` - C00204 + C00003 <=> C04349 + C00004 + C00080
- `is_product_of` <-- [[molecule.C04349|molecule.C04349]] `KEGG` `database` - C00204 + C00003 <=> C04349 + C00004 + C00080
- `is_substrate_of` <-- [[molecule.C00003|molecule.C00003]] `KEGG` `database` - C00204 + C00003 <=> C04349 + C00004 + C00080
- `is_substrate_of` <-- [[molecule.C00204|molecule.C00204]] `KEGG` `database` - C00204 + C00003 <=> C04349 + C00004 + C00080

## External IDs

- `KEGG:R01542`

## Notes

EQUATION: C00204 + C00003 <=> C04349 + C00004 + C00080
