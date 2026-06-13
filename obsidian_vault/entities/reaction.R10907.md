---
entity_id: "reaction.R10907"
entity_type: "reaction"
name: "beta-D-glucose-6-phosphate:NAD+ 1-oxidoreductase"
source_database: "KEGG"
source_id: "R10907"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R10907"
---

# beta-D-glucose-6-phosphate:NAD+ 1-oxidoreductase

`reaction.R10907`

## Static

- Type: `reaction`
- Source: `KEGG:R10907`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

beta-D-Glucose 6-phosphate + NAD+ D-Glucono-1,5-lactone 6-phosphate + NADH + H+

## Biological Role

Catalyzed by zwf (protein.P0AC53). Substrates: NAD+ (molecule.C00003), beta-D-Glucose 6-phosphate (molecule.C01172). Products: NADH (molecule.C00004), H+ (molecule.C00080), D-Glucono-1,5-lactone 6-phosphate (molecule.C01236).

## Annotation

beta-D-Glucose 6-phosphate + NAD+ <=> D-Glucono-1,5-lactone 6-phosphate + NADH + H+

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P0AC53|protein.P0AC53]] `KEGG` `database` - via EC:1.1.1.363
- `is_product_of` <-- [[molecule.C00004|molecule.C00004]] `KEGG` `database` - C01172 + C00003 <=> C01236 + C00004 + C00080
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `KEGG` `database` - C01172 + C00003 <=> C01236 + C00004 + C00080
- `is_product_of` <-- [[molecule.C01236|molecule.C01236]] `KEGG` `database` - C01172 + C00003 <=> C01236 + C00004 + C00080
- `is_substrate_of` <-- [[molecule.C00003|molecule.C00003]] `KEGG` `database` - C01172 + C00003 <=> C01236 + C00004 + C00080
- `is_substrate_of` <-- [[molecule.C01172|molecule.C01172]] `KEGG` `database` - C01172 + C00003 <=> C01236 + C00004 + C00080

## External IDs

- `KEGG:R10907`

## Notes

EQUATION: C01172 + C00003 <=> C01236 + C00004 + C00080
