---
entity_id: "reaction.R00572"
entity_type: "reaction"
name: "CTP:pyruvate 2-O-phosphotransferase"
source_database: "KEGG"
source_id: "R00572"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00572"
---

# CTP:pyruvate 2-O-phosphotransferase

`reaction.R00572`

## Static

- Type: `reaction`
- Source: `KEGG:R00572`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CTP + Pyruvate CDP + Phosphoenolpyruvate

## Biological Role

Catalyzed by pykF (protein.P0AD61), pykA (protein.P21599). Substrates: Pyruvate (molecule.C00022), CTP (molecule.C00063). Products: Phosphoenolpyruvate (molecule.C00074), CDP (molecule.C00112).

## Annotation

CTP + Pyruvate <=> CDP + Phosphoenolpyruvate

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P0AD61|protein.P0AD61]] `KEGG` `database` - via EC:2.7.1.40
- `catalyzes` <-- [[protein.P21599|protein.P21599]] `KEGG` `database` - via EC:2.7.1.40
- `is_product_of` <-- [[molecule.C00074|molecule.C00074]] `KEGG` `database` - C00063 + C00022 <=> C00112 + C00074
- `is_product_of` <-- [[molecule.C00112|molecule.C00112]] `KEGG` `database` - C00063 + C00022 <=> C00112 + C00074
- `is_substrate_of` <-- [[molecule.C00022|molecule.C00022]] `KEGG` `database` - C00063 + C00022 <=> C00112 + C00074
- `is_substrate_of` <-- [[molecule.C00063|molecule.C00063]] `KEGG` `database` - C00063 + C00022 <=> C00112 + C00074

## External IDs

- `KEGG:R00572`

## Notes

EQUATION: C00063 + C00022 <=> C00112 + C00074
