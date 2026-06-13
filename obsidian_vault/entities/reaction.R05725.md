---
entity_id: "reaction.R05725"
entity_type: "reaction"
name: "nitric oxide,NADPH2:oxygen oxidoreductase"
source_database: "KEGG"
source_id: "R05725"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R05725"
---

# nitric oxide,NADPH2:oxygen oxidoreductase

`reaction.R05725`

## Static

- Type: `reaction`
- Source: `KEGG:R05725`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

2 Nitric oxide + 2 Oxygen + NADPH + H+ 2 Nitrate + NADP+

## Biological Role

Catalyzed by hmp (protein.P24232). Substrates: NADPH (molecule.C00005), Oxygen (molecule.C00007), H+ (molecule.C00080), Nitric oxide (molecule.C00533). Products: NADP+ (molecule.C00006), Nitrate (molecule.C00244).

## Annotation

2 Nitric oxide + 2 Oxygen + NADPH + H+ <=> 2 Nitrate + NADP+

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[protein.P24232|protein.P24232]] `KEGG` `database` - via EC:1.14.12.17
- `is_product_of` <-- [[molecule.C00006|molecule.C00006]] `KEGG` `database` - 2 C00533 + 2 C00007 + C00005 + C00080 <=> 2 C00244 + C00006
- `is_product_of` <-- [[molecule.C00244|molecule.C00244]] `KEGG` `database` - 2 C00533 + 2 C00007 + C00005 + C00080 <=> 2 C00244 + C00006
- `is_substrate_of` <-- [[molecule.C00005|molecule.C00005]] `KEGG` `database` - 2 C00533 + 2 C00007 + C00005 + C00080 <=> 2 C00244 + C00006
- `is_substrate_of` <-- [[molecule.C00007|molecule.C00007]] `KEGG` `database` - 2 C00533 + 2 C00007 + C00005 + C00080 <=> 2 C00244 + C00006
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `KEGG` `database` - 2 C00533 + 2 C00007 + C00005 + C00080 <=> 2 C00244 + C00006
- `is_substrate_of` <-- [[molecule.C00533|molecule.C00533]] `KEGG` `database` - 2 C00533 + 2 C00007 + C00005 + C00080 <=> 2 C00244 + C00006

## External IDs

- `KEGG:R05725`

## Notes

EQUATION: 2 C00533 + 2 C00007 + C00005 + C00080 <=> 2 C00244 + C00006
