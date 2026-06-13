---
entity_id: "reaction.R00625"
entity_type: "reaction"
name: "primary_alcohol:NADP+ oxidoreductase"
source_database: "KEGG"
source_id: "R00625"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00625"
---

# primary_alcohol:NADP+ oxidoreductase

`reaction.R00625`

## Static

- Type: `reaction`
- Source: `KEGG:R00625`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Primary alcohol + NADP+ Aldehyde + NADPH + H+

## Biological Role

Catalyzed by ahr (protein.P27250), yahK (protein.P75691). Substrates: NADP+ (molecule.C00006), Primary alcohol (molecule.C00226). Products: NADPH (molecule.C00005), Aldehyde (molecule.C00071), H+ (molecule.C00080).

## Annotation

Primary alcohol + NADP+ <=> Aldehyde + NADPH + H+

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[protein.P27250|protein.P27250]] `KEGG` `database` - via EC:1.1.1.2
- `catalyzes` <-- [[protein.P75691|protein.P75691]] `KEGG` `database` - via EC:1.1.1.2
- `is_product_of` <-- [[molecule.C00005|molecule.C00005]] `KEGG` `database` - C00226 + C00006 <=> C00071 + C00005 + C00080
- `is_product_of` <-- [[molecule.C00071|molecule.C00071]] `KEGG` `database` - C00226 + C00006 <=> C00071 + C00005 + C00080
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `KEGG` `database` - C00226 + C00006 <=> C00071 + C00005 + C00080
- `is_substrate_of` <-- [[molecule.C00006|molecule.C00006]] `KEGG` `database` - C00226 + C00006 <=> C00071 + C00005 + C00080
- `is_substrate_of` <-- [[molecule.C00226|molecule.C00226]] `KEGG` `database` - C00226 + C00006 <=> C00071 + C00005 + C00080

## External IDs

- `KEGG:R00625`

## Notes

EQUATION: C00226 + C00006 <=> C00071 + C00005 + C00080
