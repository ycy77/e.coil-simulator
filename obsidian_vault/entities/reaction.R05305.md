---
entity_id: "reaction.R05305"
entity_type: "reaction"
name: "3-hydroxypimeloyl-CoA:NAD+ oxidoreductase"
source_database: "KEGG"
source_id: "R05305"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R05305"
---

# 3-hydroxypimeloyl-CoA:NAD+ oxidoreductase

`reaction.R05305`

## Static

- Type: `reaction`
- Source: `KEGG:R05305`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

3-Hydroxypimeloyl-CoA + NAD+ 3-Oxopimeloyl-CoA + NADH + H+

## Biological Role

Catalyzed by fadB (protein.P21177), fadJ (protein.P77399). Substrates: NAD+ (molecule.C00003), 3-Hydroxypimeloyl-CoA (molecule.C06714). Products: NADH (molecule.C00004), H+ (molecule.C00080), 3-Oxopimeloyl-CoA (molecule.C06715).

## Annotation

3-Hydroxypimeloyl-CoA + NAD+ <=> 3-Oxopimeloyl-CoA + NADH + H+

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[protein.P21177|protein.P21177]] `KEGG` `database` - via EC:1.1.1.35
- `catalyzes` <-- [[protein.P77399|protein.P77399]] `KEGG` `database` - via EC:1.1.1.35
- `is_product_of` <-- [[molecule.C00004|molecule.C00004]] `KEGG` `database` - C06714 + C00003 <=> C06715 + C00004 + C00080
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `KEGG` `database` - C06714 + C00003 <=> C06715 + C00004 + C00080
- `is_product_of` <-- [[molecule.C06715|molecule.C06715]] `KEGG` `database` - C06714 + C00003 <=> C06715 + C00004 + C00080
- `is_substrate_of` <-- [[molecule.C00003|molecule.C00003]] `KEGG` `database` - C06714 + C00003 <=> C06715 + C00004 + C00080
- `is_substrate_of` <-- [[molecule.C06714|molecule.C06714]] `KEGG` `database` - C06714 + C00003 <=> C06715 + C00004 + C00080

## External IDs

- `KEGG:R05305`

## Notes

EQUATION: C06714 + C00003 <=> C06715 + C00004 + C00080
