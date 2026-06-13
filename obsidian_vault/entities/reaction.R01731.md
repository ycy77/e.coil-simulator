---
entity_id: "reaction.R01731"
entity_type: "reaction"
name: "L-arogenate:2-oxoglutarate aminotransferase"
source_database: "KEGG"
source_id: "R01731"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R01731"
---

# L-arogenate:2-oxoglutarate aminotransferase

`reaction.R01731`

## Static

- Type: `reaction`
- Source: `KEGG:R01731`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Oxaloacetate + L-Arogenate L-Aspartate + Prephenate

## Biological Role

Catalyzed by tyrB (protein.P04693). Substrates: Oxaloacetate (molecule.C00036), L-Arogenate (molecule.C00826). Products: L-Aspartate (molecule.C00049), Prephenate (molecule.C00254).

## Annotation

Oxaloacetate + L-Arogenate <=> L-Aspartate + Prephenate

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P04693|protein.P04693]] `KEGG` `database` - via EC:2.6.1.57
- `is_product_of` <-- [[molecule.C00049|molecule.C00049]] `KEGG` `database` - C00036 + C00826 <=> C00049 + C00254
- `is_product_of` <-- [[molecule.C00254|molecule.C00254]] `KEGG` `database` - C00036 + C00826 <=> C00049 + C00254
- `is_substrate_of` <-- [[molecule.C00036|molecule.C00036]] `KEGG` `database` - C00036 + C00826 <=> C00049 + C00254
- `is_substrate_of` <-- [[molecule.C00826|molecule.C00826]] `KEGG` `database` - C00036 + C00826 <=> C00049 + C00254

## External IDs

- `KEGG:R01731`

## Notes

EQUATION: C00036 + C00826 <=> C00049 + C00254
