---
entity_id: "reaction.R10221"
entity_type: "reaction"
name: "6-phospho-D-gluconate:NAD+ 2-oxidoreductase (decarboxylating)"
source_database: "KEGG"
source_id: "R10221"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R10221"
---

# 6-phospho-D-gluconate:NAD+ 2-oxidoreductase (decarboxylating)

`reaction.R10221`

## Static

- Type: `reaction`
- Source: `KEGG:R10221`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

6-Phospho-D-gluconate + NAD+ D-Ribulose 5-phosphate + CO2 + NADH + H+

## Biological Role

Catalyzed by gnd (protein.P00350). Substrates: NAD+ (molecule.C00003), 6-Phospho-D-gluconate (molecule.C00345). Products: NADH (molecule.C00004), CO2 (molecule.C00011), H+ (molecule.C00080), D-Ribulose 5-phosphate (molecule.C00199).

## Annotation

6-Phospho-D-gluconate + NAD+ <=> D-Ribulose 5-phosphate + CO2 + NADH + H+

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[protein.P00350|protein.P00350]] `KEGG` `database` - via EC:1.1.1.343
- `is_product_of` <-- [[molecule.C00004|molecule.C00004]] `KEGG` `database` - C00345 + C00003 <=> C00199 + C00011 + C00004 + C00080
- `is_product_of` <-- [[molecule.C00011|molecule.C00011]] `KEGG` `database` - C00345 + C00003 <=> C00199 + C00011 + C00004 + C00080
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `KEGG` `database` - C00345 + C00003 <=> C00199 + C00011 + C00004 + C00080
- `is_product_of` <-- [[molecule.C00199|molecule.C00199]] `KEGG` `database` - C00345 + C00003 <=> C00199 + C00011 + C00004 + C00080
- `is_substrate_of` <-- [[molecule.C00003|molecule.C00003]] `KEGG` `database` - C00345 + C00003 <=> C00199 + C00011 + C00004 + C00080
- `is_substrate_of` <-- [[molecule.C00345|molecule.C00345]] `KEGG` `database` - C00345 + C00003 <=> C00199 + C00011 + C00004 + C00080

## External IDs

- `KEGG:R10221`

## Notes

EQUATION: C00345 + C00003 <=> C00199 + C00011 + C00004 + C00080
