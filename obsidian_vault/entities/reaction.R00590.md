---
entity_id: "reaction.R00590"
entity_type: "reaction"
name: "L-serine hydro-lyase"
source_database: "KEGG"
source_id: "R00590"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00590"
---

# L-serine hydro-lyase

`reaction.R00590`

## Static

- Type: `reaction`
- Source: `KEGG:R00590`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

L-Serine Dehydroalanine + H2O

## Biological Role

Catalyzed by sdaA (protein.P16095), sdaB (protein.P30744), tdcG (protein.P42630). Substrates: L-Serine (molecule.C00065). Products: H2O (molecule.C00001), Dehydroalanine (molecule.C02218).

## Annotation

L-Serine <=> Dehydroalanine + H2O

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P16095|protein.P16095]] `KEGG` `database` - via EC:4.3.1.17
- `catalyzes` <-- [[protein.P30744|protein.P30744]] `KEGG` `database` - via EC:4.3.1.17
- `catalyzes` <-- [[protein.P42630|protein.P42630]] `KEGG` `database` - via EC:4.3.1.17
- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C00065 <=> C02218 + C00001
- `is_product_of` <-- [[molecule.C02218|molecule.C02218]] `KEGG` `database` - C00065 <=> C02218 + C00001
- `is_substrate_of` <-- [[molecule.C00065|molecule.C00065]] `KEGG` `database` - C00065 <=> C02218 + C00001

## External IDs

- `KEGG:R00590`

## Notes

EQUATION: C00065 <=> C02218 + C00001
