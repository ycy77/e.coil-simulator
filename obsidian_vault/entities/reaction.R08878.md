---
entity_id: "reaction.R08878"
entity_type: "reaction"
name: "2-dehydro-L-idonate:NADP+ 5-oxidoreductase"
source_database: "KEGG"
source_id: "R08878"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R08878"
---

# 2-dehydro-L-idonate:NADP+ 5-oxidoreductase

`reaction.R08878`

## Static

- Type: `reaction`
- Source: `KEGG:R08878`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

2-Dehydro-L-idonate + NADP+ 2,5-Didehydro-D-gluconate + NADPH + H+

## Biological Role

Catalyzed by dkgB (protein.P30863), dkgA (protein.Q46857). Substrates: NADP+ (molecule.C00006). Products: NADPH (molecule.C00005), H+ (molecule.C00080).

## Annotation

2-Dehydro-L-idonate + NADP+ <=> 2,5-Didehydro-D-gluconate + NADPH + H+

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P30863|protein.P30863]] `KEGG` `database` - via EC:1.1.1.346
- `catalyzes` <-- [[protein.Q46857|protein.Q46857]] `KEGG` `database` - via EC:1.1.1.346
- `is_product_of` <-- [[molecule.C00005|molecule.C00005]] `KEGG` `database` - C15673 + C00006 <=> C02780 + C00005 + C00080
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `KEGG` `database` - C15673 + C00006 <=> C02780 + C00005 + C00080
- `is_substrate_of` <-- [[molecule.C00006|molecule.C00006]] `KEGG` `database` - C15673 + C00006 <=> C02780 + C00005 + C00080

## External IDs

- `KEGG:R08878`

## Notes

EQUATION: C15673 + C00006 <=> C02780 + C00005 + C00080
