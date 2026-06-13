---
entity_id: "reaction.R08210"
entity_type: "reaction"
name: "dimethylallyl diphosphate:ferredoxin oxidoreductase"
source_database: "KEGG"
source_id: "R08210"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R08210"
---

# dimethylallyl diphosphate:ferredoxin oxidoreductase

`reaction.R08210`

## Static

- Type: `reaction`
- Source: `KEGG:R08210`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Dimethylallyl diphosphate + 2 Oxidized ferredoxin + H2O 1-Hydroxy-2-methyl-2-butenyl 4-diphosphate + 2 Reduced ferredoxin + 2 H+

## Biological Role

Catalyzed by ispH (protein.P62623). Substrates: H2O (molecule.C00001), Dimethylallyl diphosphate (molecule.C00235). Products: H+ (molecule.C00080), 1-Hydroxy-2-methyl-2-butenyl 4-diphosphate (molecule.C11811).

## Annotation

Dimethylallyl diphosphate + 2 Oxidized ferredoxin + H2O <=> 1-Hydroxy-2-methyl-2-butenyl 4-diphosphate + 2 Reduced ferredoxin + 2 H+

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P62623|protein.P62623]] `KEGG` `database` - via EC:1.17.7.4
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `KEGG` `database` - C00235 + 2 C00139 + C00001 <=> C11811 + 2 C00138 + 2 C00080
- `is_product_of` <-- [[molecule.C11811|molecule.C11811]] `KEGG` `database` - C00235 + 2 C00139 + C00001 <=> C11811 + 2 C00138 + 2 C00080
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C00235 + 2 C00139 + C00001 <=> C11811 + 2 C00138 + 2 C00080
- `is_substrate_of` <-- [[molecule.C00235|molecule.C00235]] `KEGG` `database` - C00235 + 2 C00139 + C00001 <=> C11811 + 2 C00138 + 2 C00080

## External IDs

- `KEGG:R08210`

## Notes

EQUATION: C00235 + 2 C00139 + C00001 <=> C11811 + 2 C00138 + 2 C00080
