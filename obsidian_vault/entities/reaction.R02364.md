---
entity_id: "reaction.R02364"
entity_type: "reaction"
name: "NADPH2:quinone oxidoreductase"
source_database: "KEGG"
source_id: "R02364"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R02364"
---

# NADPH2:quinone oxidoreductase

`reaction.R02364`

## Static

- Type: `reaction`
- Source: `KEGG:R02364`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

2 Quinone + NADPH + H+ 2 Semiquinone + NADP+

## Biological Role

Catalyzed by qorA (protein.P28304). Substrates: NADPH (molecule.C00005), H+ (molecule.C00080). Products: NADP+ (molecule.C00006).

## Annotation

2 Quinone + NADPH + H+ <=> 2 Semiquinone + NADP+

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[protein.P28304|protein.P28304]] `KEGG` `database` - via EC:1.6.5.5
- `is_product_of` <-- [[molecule.C00006|molecule.C00006]] `KEGG` `database` - 2 C15602 + C00005 + C00080 <=> 2 C05309 + C00006
- `is_substrate_of` <-- [[molecule.C00005|molecule.C00005]] `KEGG` `database` - 2 C15602 + C00005 + C00080 <=> 2 C05309 + C00006
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `KEGG` `database` - 2 C15602 + C00005 + C00080 <=> 2 C05309 + C00006

## External IDs

- `KEGG:R02364`

## Notes

EQUATION: 2 C15602 + C00005 + C00080 <=> 2 C05309 + C00006
