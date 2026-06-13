---
entity_id: "reaction.R01528"
entity_type: "reaction"
name: "6-phospho-D-gluconate:NADP+ 2-oxidoreductase (decarboxylating)"
source_database: "KEGG"
source_id: "R01528"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R01528"
---

# 6-phospho-D-gluconate:NADP+ 2-oxidoreductase (decarboxylating)

`reaction.R01528`

## Static

- Type: `reaction`
- Source: `KEGG:R01528`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

6-Phospho-D-gluconate + NADP+ D-Ribulose 5-phosphate + CO2 + NADPH + H+

## Biological Role

Catalyzed by gnd (protein.P00350). Substrates: NADP+ (molecule.C00006), 6-Phospho-D-gluconate (molecule.C00345). Products: NADPH (molecule.C00005), CO2 (molecule.C00011), H+ (molecule.C00080), D-Ribulose 5-phosphate (molecule.C00199).

## Annotation

6-Phospho-D-gluconate + NADP+ <=> D-Ribulose 5-phosphate + CO2 + NADPH + H+

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[protein.P00350|protein.P00350]] `KEGG` `database` - via EC:1.1.1.44
- `is_product_of` <-- [[molecule.C00005|molecule.C00005]] `KEGG` `database` - C00345 + C00006 <=> C00199 + C00011 + C00005 + C00080
- `is_product_of` <-- [[molecule.C00011|molecule.C00011]] `KEGG` `database` - C00345 + C00006 <=> C00199 + C00011 + C00005 + C00080
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `KEGG` `database` - C00345 + C00006 <=> C00199 + C00011 + C00005 + C00080
- `is_product_of` <-- [[molecule.C00199|molecule.C00199]] `KEGG` `database` - C00345 + C00006 <=> C00199 + C00011 + C00005 + C00080
- `is_substrate_of` <-- [[molecule.C00006|molecule.C00006]] `KEGG` `database` - C00345 + C00006 <=> C00199 + C00011 + C00005 + C00080
- `is_substrate_of` <-- [[molecule.C00345|molecule.C00345]] `KEGG` `database` - C00345 + C00006 <=> C00199 + C00011 + C00005 + C00080

## External IDs

- `KEGG:R01528`

## Notes

EQUATION: C00345 + C00006 <=> C00199 + C00011 + C00005 + C00080
