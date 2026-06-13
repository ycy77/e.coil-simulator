---
entity_id: "reaction.R01138"
entity_type: "reaction"
name: "dATP:pyruvate 2-O-phosphotransferase"
source_database: "KEGG"
source_id: "R01138"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R01138"
---

# dATP:pyruvate 2-O-phosphotransferase

`reaction.R01138`

## Static

- Type: `reaction`
- Source: `KEGG:R01138`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

dATP + Pyruvate dADP + Phosphoenolpyruvate

## Biological Role

Catalyzed by pykF (protein.P0AD61), pykA (protein.P21599). Substrates: Pyruvate (molecule.C00022), dATP (molecule.C00131). Products: Phosphoenolpyruvate (molecule.C00074), dADP (molecule.C00206).

## Annotation

dATP + Pyruvate <=> dADP + Phosphoenolpyruvate

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P0AD61|protein.P0AD61]] `KEGG` `database` - via EC:2.7.1.40
- `catalyzes` <-- [[protein.P21599|protein.P21599]] `KEGG` `database` - via EC:2.7.1.40
- `is_product_of` <-- [[molecule.C00074|molecule.C00074]] `KEGG` `database` - C00131 + C00022 <=> C00206 + C00074
- `is_product_of` <-- [[molecule.C00206|molecule.C00206]] `KEGG` `database` - C00131 + C00022 <=> C00206 + C00074
- `is_substrate_of` <-- [[molecule.C00022|molecule.C00022]] `KEGG` `database` - C00131 + C00022 <=> C00206 + C00074
- `is_substrate_of` <-- [[molecule.C00131|molecule.C00131]] `KEGG` `database` - C00131 + C00022 <=> C00206 + C00074

## External IDs

- `KEGG:R01138`

## Notes

EQUATION: C00131 + C00022 <=> C00206 + C00074
