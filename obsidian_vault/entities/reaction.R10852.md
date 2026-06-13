---
entity_id: "reaction.R10852"
entity_type: "reaction"
name: "L-allo-threonine:NADP+ 3-oxidoreductase (decarboxylating)"
source_database: "KEGG"
source_id: "R10852"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R10852"
---

# L-allo-threonine:NADP+ 3-oxidoreductase (decarboxylating)

`reaction.R10852`

## Static

- Type: `reaction`
- Source: `KEGG:R10852`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

L-Allothreonine + NADP+ Aminoacetone + CO2 + NADPH + H+

## Biological Role

Catalyzed by ydfG (protein.P39831). Substrates: NADP+ (molecule.C00006), L-Allothreonine (molecule.C05519). Products: NADPH (molecule.C00005), CO2 (molecule.C00011), H+ (molecule.C00080), Aminoacetone (molecule.C01888).

## Annotation

L-Allothreonine + NADP+ <=> Aminoacetone + CO2 + NADPH + H+

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[protein.P39831|protein.P39831]] `KEGG` `database` - via EC:1.1.1.381
- `is_product_of` <-- [[molecule.C00005|molecule.C00005]] `KEGG` `database` - C05519 + C00006 <=> C01888 + C00011 + C00005 + C00080
- `is_product_of` <-- [[molecule.C00011|molecule.C00011]] `KEGG` `database` - C05519 + C00006 <=> C01888 + C00011 + C00005 + C00080
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `KEGG` `database` - C05519 + C00006 <=> C01888 + C00011 + C00005 + C00080
- `is_product_of` <-- [[molecule.C01888|molecule.C01888]] `KEGG` `database` - C05519 + C00006 <=> C01888 + C00011 + C00005 + C00080
- `is_substrate_of` <-- [[molecule.C00006|molecule.C00006]] `KEGG` `database` - C05519 + C00006 <=> C01888 + C00011 + C00005 + C00080
- `is_substrate_of` <-- [[molecule.C05519|molecule.C05519]] `KEGG` `database` - C05519 + C00006 <=> C01888 + C00011 + C00005 + C00080

## External IDs

- `KEGG:R10852`

## Notes

EQUATION: C05519 + C00006 <=> C01888 + C00011 + C00005 + C00080
