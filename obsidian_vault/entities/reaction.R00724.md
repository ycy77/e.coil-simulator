---
entity_id: "reaction.R00724"
entity_type: "reaction"
name: "ITP:pyruvate 2-O-phosphotransferase"
source_database: "KEGG"
source_id: "R00724"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00724"
---

# ITP:pyruvate 2-O-phosphotransferase

`reaction.R00724`

## Static

- Type: `reaction`
- Source: `KEGG:R00724`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ITP + Pyruvate IDP + Phosphoenolpyruvate

## Biological Role

Catalyzed by pykF (protein.P0AD61), pykA (protein.P21599). Substrates: Pyruvate (molecule.C00022), ITP (molecule.C00081). Products: Phosphoenolpyruvate (molecule.C00074), IDP (molecule.C00104).

## Annotation

ITP + Pyruvate <=> IDP + Phosphoenolpyruvate

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P0AD61|protein.P0AD61]] `KEGG` `database` - via EC:2.7.1.40
- `catalyzes` <-- [[protein.P21599|protein.P21599]] `KEGG` `database` - via EC:2.7.1.40
- `is_product_of` <-- [[molecule.C00074|molecule.C00074]] `KEGG` `database` - C00081 + C00022 <=> C00104 + C00074
- `is_product_of` <-- [[molecule.C00104|molecule.C00104]] `KEGG` `database` - C00081 + C00022 <=> C00104 + C00074
- `is_substrate_of` <-- [[molecule.C00022|molecule.C00022]] `KEGG` `database` - C00081 + C00022 <=> C00104 + C00074
- `is_substrate_of` <-- [[molecule.C00081|molecule.C00081]] `KEGG` `database` - C00081 + C00022 <=> C00104 + C00074

## External IDs

- `KEGG:R00724`

## Notes

EQUATION: C00081 + C00022 <=> C00104 + C00074
