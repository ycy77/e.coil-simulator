---
entity_id: "reaction.R00430"
entity_type: "reaction"
name: "GTP:pyruvate 2-O-phosphotransferase"
source_database: "KEGG"
source_id: "R00430"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00430"
---

# GTP:pyruvate 2-O-phosphotransferase

`reaction.R00430`

## Static

- Type: `reaction`
- Source: `KEGG:R00430`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

GTP + Pyruvate GDP + Phosphoenolpyruvate

## Biological Role

Catalyzed by pykF (protein.P0AD61), pykA (protein.P21599). Substrates: Pyruvate (molecule.C00022), GTP (molecule.C00044). Products: GDP (molecule.C00035), Phosphoenolpyruvate (molecule.C00074).

## Annotation

GTP + Pyruvate <=> GDP + Phosphoenolpyruvate

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P0AD61|protein.P0AD61]] `KEGG` `database` - via EC:2.7.1.40
- `catalyzes` <-- [[protein.P21599|protein.P21599]] `KEGG` `database` - via EC:2.7.1.40
- `is_product_of` <-- [[molecule.C00035|molecule.C00035]] `KEGG` `database` - C00044 + C00022 <=> C00035 + C00074
- `is_product_of` <-- [[molecule.C00074|molecule.C00074]] `KEGG` `database` - C00044 + C00022 <=> C00035 + C00074
- `is_substrate_of` <-- [[molecule.C00022|molecule.C00022]] `KEGG` `database` - C00044 + C00022 <=> C00035 + C00074
- `is_substrate_of` <-- [[molecule.C00044|molecule.C00044]] `KEGG` `database` - C00044 + C00022 <=> C00035 + C00074

## External IDs

- `KEGG:R00430`

## Notes

EQUATION: C00044 + C00022 <=> C00035 + C00074
