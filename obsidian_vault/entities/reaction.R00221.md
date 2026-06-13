---
entity_id: "reaction.R00221"
entity_type: "reaction"
name: "D-serine ammonia-lyase"
source_database: "KEGG"
source_id: "R00221"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00221"
---

# D-serine ammonia-lyase

`reaction.R00221`

## Static

- Type: `reaction`
- Source: `KEGG:R00221`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

D-Serine Pyruvate + Ammonia

## Biological Role

Catalyzed by dsdA (protein.P00926). Substrates: D-Serine (molecule.C00740). Products: Ammonia (molecule.C00014), Pyruvate (molecule.C00022).

## Annotation

D-Serine <=> Pyruvate + Ammonia

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[protein.P00926|protein.P00926]] `KEGG` `database` - via EC:4.3.1.18
- `is_product_of` <-- [[molecule.C00014|molecule.C00014]] `KEGG` `database` - C00740 <=> C00022 + C00014
- `is_product_of` <-- [[molecule.C00022|molecule.C00022]] `KEGG` `database` - C00740 <=> C00022 + C00014
- `is_substrate_of` <-- [[molecule.C00740|molecule.C00740]] `KEGG` `database` - C00740 <=> C00022 + C00014

## External IDs

- `KEGG:R00221`

## Notes

EQUATION: C00740 <=> C00022 + C00014
