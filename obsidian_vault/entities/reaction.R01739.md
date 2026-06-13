---
entity_id: "reaction.R01739"
entity_type: "reaction"
name: "D-gluconate:NADP+ 2-oxidoreductase"
source_database: "KEGG"
source_id: "R01739"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R01739"
---

# D-gluconate:NADP+ 2-oxidoreductase

`reaction.R01739`

## Static

- Type: `reaction`
- Source: `KEGG:R01739`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

D-Gluconic acid + NADP+ 2-Keto-D-gluconic acid + NADPH + H+

## Biological Role

Catalyzed by ghrB (protein.P37666). Substrates: NADP+ (molecule.C00006), D-Gluconic acid (molecule.C00257). Products: NADPH (molecule.C00005), H+ (molecule.C00080), 2-Keto-D-gluconic acid (molecule.C06473).

## Annotation

D-Gluconic acid + NADP+ <=> 2-Keto-D-gluconic acid + NADPH + H+

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P37666|protein.P37666]] `KEGG` `database` - via EC:1.1.1.215
- `is_product_of` <-- [[molecule.C00005|molecule.C00005]] `KEGG` `database` - C00257 + C00006 <=> C06473 + C00005 + C00080
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `KEGG` `database` - C00257 + C00006 <=> C06473 + C00005 + C00080
- `is_product_of` <-- [[molecule.C06473|molecule.C06473]] `KEGG` `database` - C00257 + C00006 <=> C06473 + C00005 + C00080
- `is_substrate_of` <-- [[molecule.C00006|molecule.C00006]] `KEGG` `database` - C00257 + C00006 <=> C06473 + C00005 + C00080
- `is_substrate_of` <-- [[molecule.C00257|molecule.C00257]] `KEGG` `database` - C00257 + C00006 <=> C06473 + C00005 + C00080

## External IDs

- `KEGG:R01739`

## Notes

EQUATION: C00257 + C00006 <=> C06473 + C00005 + C00080
