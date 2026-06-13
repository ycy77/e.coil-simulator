---
entity_id: "reaction.R00479"
entity_type: "reaction"
name: "isocitrate glyoxylate-lyase (succinate-forming)"
source_database: "KEGG"
source_id: "R00479"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00479"
---

# isocitrate glyoxylate-lyase (succinate-forming)

`reaction.R00479`

## Static

- Type: `reaction`
- Source: `KEGG:R00479`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Isocitrate Succinate + Glyoxylate

## Biological Role

Catalyzed by aceA (protein.P0A9G6). Substrates: Isocitrate (molecule.C00311). Products: Succinate (molecule.C00042), Glyoxylate (molecule.C00048).

## Annotation

Isocitrate <=> Succinate + Glyoxylate

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[protein.P0A9G6|protein.P0A9G6]] `KEGG` `database` - via EC:4.1.3.1
- `is_product_of` <-- [[molecule.C00042|molecule.C00042]] `KEGG` `database` - C00311 <=> C00042 + C00048
- `is_product_of` <-- [[molecule.C00048|molecule.C00048]] `KEGG` `database` - C00311 <=> C00042 + C00048
- `is_substrate_of` <-- [[molecule.C00311|molecule.C00311]] `KEGG` `database` - C00311 <=> C00042 + C00048

## External IDs

- `KEGG:R00479`

## Notes

EQUATION: C00311 <=> C00042 + C00048
