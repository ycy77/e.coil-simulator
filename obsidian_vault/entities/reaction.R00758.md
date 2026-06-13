---
entity_id: "reaction.R00758"
entity_type: "reaction"
name: "D-mannitol-1-phosphate:NAD+ 5-oxidoreductase"
source_database: "KEGG"
source_id: "R00758"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00758"
---

# D-mannitol-1-phosphate:NAD+ 5-oxidoreductase

`reaction.R00758`

## Static

- Type: `reaction`
- Source: `KEGG:R00758`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

D-Mannitol 1-phosphate + NAD+ D-Fructose 6-phosphate + NADH + H+

## Biological Role

Catalyzed by mtlD (protein.P09424). Substrates: NAD+ (molecule.C00003), D-Mannitol 1-phosphate (molecule.C00644). Products: NADH (molecule.C00004), H+ (molecule.C00080), D-Fructose 6-phosphate (molecule.C00085).

## Annotation

D-Mannitol 1-phosphate + NAD+ <=> D-Fructose 6-phosphate + NADH + H+

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P09424|protein.P09424]] `KEGG` `database` - via EC:1.1.1.17
- `is_product_of` <-- [[molecule.C00004|molecule.C00004]] `KEGG` `database` - C00644 + C00003 <=> C00085 + C00004 + C00080
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `KEGG` `database` - C00644 + C00003 <=> C00085 + C00004 + C00080
- `is_product_of` <-- [[molecule.C00085|molecule.C00085]] `KEGG` `database` - C00644 + C00003 <=> C00085 + C00004 + C00080
- `is_substrate_of` <-- [[molecule.C00003|molecule.C00003]] `KEGG` `database` - C00644 + C00003 <=> C00085 + C00004 + C00080
- `is_substrate_of` <-- [[molecule.C00644|molecule.C00644]] `KEGG` `database` - C00644 + C00003 <=> C00085 + C00004 + C00080

## External IDs

- `KEGG:R00758`

## Notes

EQUATION: C00644 + C00003 <=> C00085 + C00004 + C00080
