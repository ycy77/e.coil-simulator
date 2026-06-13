---
entity_id: "reaction.R00269"
entity_type: "reaction"
name: "2-oxoglutaramate amidohydrolase"
source_database: "KEGG"
source_id: "R00269"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00269"
---

# 2-oxoglutaramate amidohydrolase

`reaction.R00269`

## Static

- Type: `reaction`
- Source: `KEGG:R00269`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

2-Oxoglutaramate + H2O 2-Oxoglutarate + Ammonia

## Biological Role

Catalyzed by yafV (protein.Q47679). Substrates: H2O (molecule.C00001), 2-Oxoglutaramate (molecule.C00940). Products: Ammonia (molecule.C00014), 2-Oxoglutarate (molecule.C00026).

## Annotation

2-Oxoglutaramate + H2O <=> 2-Oxoglutarate + Ammonia

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.Q47679|protein.Q47679]] `KEGG` `database` - via EC:3.5.1.3
- `is_product_of` <-- [[molecule.C00014|molecule.C00014]] `KEGG` `database` - C00940 + C00001 <=> C00026 + C00014
- `is_product_of` <-- [[molecule.C00026|molecule.C00026]] `KEGG` `database` - C00940 + C00001 <=> C00026 + C00014
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C00940 + C00001 <=> C00026 + C00014
- `is_substrate_of` <-- [[molecule.C00940|molecule.C00940]] `KEGG` `database` - C00940 + C00001 <=> C00026 + C00014

## External IDs

- `KEGG:R00269`

## Notes

EQUATION: C00940 + C00001 <=> C00026 + C00014
