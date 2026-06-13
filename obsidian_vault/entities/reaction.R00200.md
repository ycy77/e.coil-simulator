---
entity_id: "reaction.R00200"
entity_type: "reaction"
name: "ATP:pyruvate 2-O-phosphotransferase"
source_database: "KEGG"
source_id: "R00200"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00200"
---

# ATP:pyruvate 2-O-phosphotransferase

`reaction.R00200`

## Static

- Type: `reaction`
- Source: `KEGG:R00200`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ATP + Pyruvate ADP + Phosphoenolpyruvate

## Biological Role

Catalyzed by pykF (protein.P0AD61), pykA (protein.P21599). Substrates: ATP (molecule.C00002), Pyruvate (molecule.C00022). Products: ADP (molecule.C00008), Phosphoenolpyruvate (molecule.C00074).

## Annotation

ATP + Pyruvate <=> ADP + Phosphoenolpyruvate

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P0AD61|protein.P0AD61]] `KEGG` `database` - via EC:2.7.1.40
- `catalyzes` <-- [[protein.P21599|protein.P21599]] `KEGG` `database` - via EC:2.7.1.40
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `KEGG` `database` - C00002 + C00022 <=> C00008 + C00074
- `is_product_of` <-- [[molecule.C00074|molecule.C00074]] `KEGG` `database` - C00002 + C00022 <=> C00008 + C00074
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `KEGG` `database` - C00002 + C00022 <=> C00008 + C00074
- `is_substrate_of` <-- [[molecule.C00022|molecule.C00022]] `KEGG` `database` - C00002 + C00022 <=> C00008 + C00074

## External IDs

- `KEGG:R00200`

## Notes

EQUATION: C00002 + C00022 <=> C00008 + C00074
