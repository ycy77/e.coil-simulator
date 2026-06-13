---
entity_id: "reaction.R00659"
entity_type: "reaction"
name: "UTP:pyruvate 2-O-phosphotransferase"
source_database: "KEGG"
source_id: "R00659"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00659"
---

# UTP:pyruvate 2-O-phosphotransferase

`reaction.R00659`

## Static

- Type: `reaction`
- Source: `KEGG:R00659`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

UTP + Pyruvate UDP + Phosphoenolpyruvate

## Biological Role

Catalyzed by pykF (protein.P0AD61), pykA (protein.P21599). Substrates: Pyruvate (molecule.C00022), UTP (molecule.C00075). Products: UDP (molecule.C00015), Phosphoenolpyruvate (molecule.C00074).

## Annotation

UTP + Pyruvate <=> UDP + Phosphoenolpyruvate

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P0AD61|protein.P0AD61]] `KEGG` `database` - via EC:2.7.1.40
- `catalyzes` <-- [[protein.P21599|protein.P21599]] `KEGG` `database` - via EC:2.7.1.40
- `is_product_of` <-- [[molecule.C00015|molecule.C00015]] `KEGG` `database` - C00075 + C00022 <=> C00015 + C00074
- `is_product_of` <-- [[molecule.C00074|molecule.C00074]] `KEGG` `database` - C00075 + C00022 <=> C00015 + C00074
- `is_substrate_of` <-- [[molecule.C00022|molecule.C00022]] `KEGG` `database` - C00075 + C00022 <=> C00015 + C00074
- `is_substrate_of` <-- [[molecule.C00075|molecule.C00075]] `KEGG` `database` - C00075 + C00022 <=> C00015 + C00074

## External IDs

- `KEGG:R00659`

## Notes

EQUATION: C00075 + C00022 <=> C00015 + C00074
