---
entity_id: "reaction.R00112"
entity_type: "reaction"
name: "NADPH:NAD+ oxidoreductase"
source_database: "KEGG"
source_id: "R00112"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00112"
---

# NADPH:NAD+ oxidoreductase

`reaction.R00112`

## Static

- Type: `reaction`
- Source: `KEGG:R00112`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

NADPH + NAD+ NADP+ + NADH

## Biological Role

Catalyzed by sthA (protein.P27306). Substrates: NAD+ (molecule.C00003), NADPH (molecule.C00005). Products: NADH (molecule.C00004), NADP+ (molecule.C00006).

## Annotation

NADPH + NAD+ <=> NADP+ + NADH

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P27306|protein.P27306]] `KEGG` `database` - via EC:1.6.1.1
- `is_product_of` <-- [[molecule.C00004|molecule.C00004]] `KEGG` `database` - C00005 + C00003 <=> C00006 + C00004
- `is_product_of` <-- [[molecule.C00006|molecule.C00006]] `KEGG` `database` - C00005 + C00003 <=> C00006 + C00004
- `is_substrate_of` <-- [[molecule.C00003|molecule.C00003]] `KEGG` `database` - C00005 + C00003 <=> C00006 + C00004
- `is_substrate_of` <-- [[molecule.C00005|molecule.C00005]] `KEGG` `database` - C00005 + C00003 <=> C00006 + C00004

## External IDs

- `KEGG:R00112`

## Notes

EQUATION: C00005 + C00003 <=> C00006 + C00004
