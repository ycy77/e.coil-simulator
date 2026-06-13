---
entity_id: "reaction.R05724"
entity_type: "reaction"
name: "nitric oxide,NAD(P)H2:oxygen oxidoreductase"
source_database: "KEGG"
source_id: "R05724"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R05724"
---

# nitric oxide,NAD(P)H2:oxygen oxidoreductase

`reaction.R05724`

## Static

- Type: `reaction`
- Source: `KEGG:R05724`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

2 Nitric oxide + 2 Oxygen + NADH + H+ 2 Nitrate + NAD+

## Biological Role

Catalyzed by hmp (protein.P24232). Substrates: NADH (molecule.C00004), Oxygen (molecule.C00007), H+ (molecule.C00080), Nitric oxide (molecule.C00533). Products: NAD+ (molecule.C00003), Nitrate (molecule.C00244).

## Annotation

2 Nitric oxide + 2 Oxygen + NADH + H+ <=> 2 Nitrate + NAD+

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[protein.P24232|protein.P24232]] `KEGG` `database` - via EC:1.14.12.17
- `is_product_of` <-- [[molecule.C00003|molecule.C00003]] `KEGG` `database` - 2 C00533 + 2 C00007 + C00004 + C00080 <=> 2 C00244 + C00003
- `is_product_of` <-- [[molecule.C00244|molecule.C00244]] `KEGG` `database` - 2 C00533 + 2 C00007 + C00004 + C00080 <=> 2 C00244 + C00003
- `is_substrate_of` <-- [[molecule.C00004|molecule.C00004]] `KEGG` `database` - 2 C00533 + 2 C00007 + C00004 + C00080 <=> 2 C00244 + C00003
- `is_substrate_of` <-- [[molecule.C00007|molecule.C00007]] `KEGG` `database` - 2 C00533 + 2 C00007 + C00004 + C00080 <=> 2 C00244 + C00003
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `KEGG` `database` - 2 C00533 + 2 C00007 + C00004 + C00080 <=> 2 C00244 + C00003
- `is_substrate_of` <-- [[molecule.C00533|molecule.C00533]] `KEGG` `database` - 2 C00533 + 2 C00007 + C00004 + C00080 <=> 2 C00244 + C00003

## External IDs

- `KEGG:R05724`

## Notes

EQUATION: 2 C00533 + 2 C00007 + C00004 + C00080 <=> 2 C00244 + C00003
