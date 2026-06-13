---
entity_id: "reaction.R00104"
entity_type: "reaction"
name: "ATP:NAD+ 2'-phosphotransferase"
source_database: "KEGG"
source_id: "R00104"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00104"
---

# ATP:NAD+ 2'-phosphotransferase

`reaction.R00104`

## Static

- Type: `reaction`
- Source: `KEGG:R00104`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ATP + NAD+ ADP + NADP+

## Biological Role

Catalyzed by nadK (protein.P0A7B3). Substrates: ATP (molecule.C00002), NAD+ (molecule.C00003). Products: NADP+ (molecule.C00006), ADP (molecule.C00008).

## Annotation

ATP + NAD+ <=> ADP + NADP+

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P0A7B3|protein.P0A7B3]] `KEGG` `database` - via EC:2.7.1.23
- `is_product_of` <-- [[molecule.C00006|molecule.C00006]] `KEGG` `database` - C00002 + C00003 <=> C00008 + C00006
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `KEGG` `database` - C00002 + C00003 <=> C00008 + C00006
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `KEGG` `database` - C00002 + C00003 <=> C00008 + C00006
- `is_substrate_of` <-- [[molecule.C00003|molecule.C00003]] `KEGG` `database` - C00002 + C00003 <=> C00008 + C00006

## External IDs

- `KEGG:R00104`

## Notes

EQUATION: C00002 + C00003 <=> C00008 + C00006
