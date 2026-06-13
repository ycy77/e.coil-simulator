---
entity_id: "reaction.R08879"
entity_type: "reaction"
name: "5-dehydro-D-gluconate:NADP+ 2-oxidoreductase"
source_database: "KEGG"
source_id: "R08879"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R08879"
---

# 5-dehydro-D-gluconate:NADP+ 2-oxidoreductase

`reaction.R08879`

## Static

- Type: `reaction`
- Source: `KEGG:R08879`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

5-Dehydro-D-gluconate + NADP+ 2,5-Didehydro-D-gluconate + NADPH + H+

## Biological Role

Catalyzed by ghrB (protein.P37666). Substrates: NADP+ (molecule.C00006). Products: NADPH (molecule.C00005), H+ (molecule.C00080).

## Annotation

5-Dehydro-D-gluconate + NADP+ <=> 2,5-Didehydro-D-gluconate + NADPH + H+

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[protein.P37666|protein.P37666]] `KEGG` `database` - via EC:1.1.1.215
- `is_product_of` <-- [[molecule.C00005|molecule.C00005]] `KEGG` `database` - C01062 + C00006 <=> C02780 + C00005 + C00080
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `KEGG` `database` - C01062 + C00006 <=> C02780 + C00005 + C00080
- `is_substrate_of` <-- [[molecule.C00006|molecule.C00006]] `KEGG` `database` - C01062 + C00006 <=> C02780 + C00005 + C00080

## External IDs

- `KEGG:R08879`

## Notes

EQUATION: C01062 + C00006 <=> C02780 + C00005 + C00080
