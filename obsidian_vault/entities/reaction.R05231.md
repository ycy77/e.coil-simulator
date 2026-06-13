---
entity_id: "reaction.R05231"
entity_type: "reaction"
name: "6-hydroxyhexanoate:NADP+ oxidoreductase"
source_database: "KEGG"
source_id: "R05231"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R05231"
---

# 6-hydroxyhexanoate:NADP+ oxidoreductase

`reaction.R05231`

## Static

- Type: `reaction`
- Source: `KEGG:R05231`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

6-Hydroxyhexanoic acid + NADP+ Adipate semialdehyde + NADPH + H+

## Biological Role

Catalyzed by ahr (protein.P27250), yahK (protein.P75691). Substrates: NADP+ (molecule.C00006), 6-Hydroxyhexanoic acid (molecule.C06103). Products: NADPH (molecule.C00005), H+ (molecule.C00080), Adipate semialdehyde (molecule.C06102).

## Annotation

6-Hydroxyhexanoic acid + NADP+ <=> Adipate semialdehyde + NADPH + H+

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[protein.P27250|protein.P27250]] `KEGG` `database` - via EC:1.1.1.2
- `catalyzes` <-- [[protein.P75691|protein.P75691]] `KEGG` `database` - via EC:1.1.1.2
- `is_product_of` <-- [[molecule.C00005|molecule.C00005]] `KEGG` `database` - C06103 + C00006 <=> C06102 + C00005 + C00080
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `KEGG` `database` - C06103 + C00006 <=> C06102 + C00005 + C00080
- `is_product_of` <-- [[molecule.C06102|molecule.C06102]] `KEGG` `database` - C06103 + C00006 <=> C06102 + C00005 + C00080
- `is_substrate_of` <-- [[molecule.C00006|molecule.C00006]] `KEGG` `database` - C06103 + C00006 <=> C06102 + C00005 + C00080
- `is_substrate_of` <-- [[molecule.C06103|molecule.C06103]] `KEGG` `database` - C06103 + C00006 <=> C06102 + C00005 + C00080

## External IDs

- `KEGG:R05231`

## Notes

EQUATION: C06103 + C00006 <=> C06102 + C00005 + C00080
