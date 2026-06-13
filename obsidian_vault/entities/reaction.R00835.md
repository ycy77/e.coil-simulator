---
entity_id: "reaction.R00835"
entity_type: "reaction"
name: "D-glucose-6-phosphate:NADP+ 1-oxidoreductase"
source_database: "KEGG"
source_id: "R00835"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00835"
---

# D-glucose-6-phosphate:NADP+ 1-oxidoreductase

`reaction.R00835`

## Static

- Type: `reaction`
- Source: `KEGG:R00835`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

D-Glucose 6-phosphate + NADP+ D-Glucono-1,5-lactone 6-phosphate + NADPH + H+

## Biological Role

Catalyzed by zwf (protein.P0AC53). Substrates: NADP+ (molecule.C00006), D-Glucose 6-phosphate (molecule.C00092). Products: NADPH (molecule.C00005), H+ (molecule.C00080), D-Glucono-1,5-lactone 6-phosphate (molecule.C01236).

## Annotation

D-Glucose 6-phosphate + NADP+ <=> D-Glucono-1,5-lactone 6-phosphate + NADPH + H+

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P0AC53|protein.P0AC53]] `KEGG` `database` - via EC:1.1.1.49
- `is_product_of` <-- [[molecule.C00005|molecule.C00005]] `KEGG` `database` - C00092 + C00006 <=> C01236 + C00005 + C00080
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `KEGG` `database` - C00092 + C00006 <=> C01236 + C00005 + C00080
- `is_product_of` <-- [[molecule.C01236|molecule.C01236]] `KEGG` `database` - C00092 + C00006 <=> C01236 + C00005 + C00080
- `is_substrate_of` <-- [[molecule.C00006|molecule.C00006]] `KEGG` `database` - C00092 + C00006 <=> C01236 + C00005 + C00080
- `is_substrate_of` <-- [[molecule.C00092|molecule.C00092]] `KEGG` `database` - C00092 + C00006 <=> C01236 + C00005 + C00080

## External IDs

- `KEGG:R00835`

## Notes

EQUATION: C00092 + C00006 <=> C01236 + C00005 + C00080
