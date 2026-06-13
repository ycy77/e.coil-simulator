---
entity_id: "reaction.R00220"
entity_type: "reaction"
name: "L-serine ammonia-lyase"
source_database: "KEGG"
source_id: "R00220"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00220"
---

# L-serine ammonia-lyase

`reaction.R00220`

## Static

- Type: `reaction`
- Source: `KEGG:R00220`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

L-Serine Pyruvate + Ammonia

## Biological Role

Catalyzed by ilvA (protein.P04968), tdcB (protein.P0AGF6), sdaA (protein.P16095), sdaB (protein.P30744), tdcG (protein.P42630). Substrates: L-Serine (molecule.C00065). Products: Ammonia (molecule.C00014), Pyruvate (molecule.C00022).

## Annotation

L-Serine <=> Pyruvate + Ammonia

## Outgoing Edges (0)

_None._

## Incoming Edges (8)

- `catalyzes` <-- [[protein.P04968|protein.P04968]] `KEGG` `database` - via EC:4.3.1.19
- `catalyzes` <-- [[protein.P0AGF6|protein.P0AGF6]] `KEGG` `database` - via EC:4.3.1.19
- `catalyzes` <-- [[protein.P16095|protein.P16095]] `KEGG` `database` - via EC:4.3.1.17
- `catalyzes` <-- [[protein.P30744|protein.P30744]] `KEGG` `database` - via EC:4.3.1.17
- `catalyzes` <-- [[protein.P42630|protein.P42630]] `KEGG` `database` - via EC:4.3.1.17
- `is_product_of` <-- [[molecule.C00014|molecule.C00014]] `KEGG` `database` - C00065 <=> C00022 + C00014
- `is_product_of` <-- [[molecule.C00022|molecule.C00022]] `KEGG` `database` - C00065 <=> C00022 + C00014
- `is_substrate_of` <-- [[molecule.C00065|molecule.C00065]] `KEGG` `database` - C00065 <=> C00022 + C00014

## External IDs

- `KEGG:R00220`

## Notes

EQUATION: C00065 <=> C00022 + C00014
