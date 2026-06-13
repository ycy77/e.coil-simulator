---
entity_id: "reaction.R00485"
entity_type: "reaction"
name: "L-asparagine amidohydrolase"
source_database: "KEGG"
source_id: "R00485"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00485"
---

# L-asparagine amidohydrolase

`reaction.R00485`

## Static

- Type: `reaction`
- Source: `KEGG:R00485`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

L-Asparagine + H2O L-Aspartate + Ammonia

## Biological Role

Catalyzed by ansB (protein.P00805), ansA (protein.P0A962), iaaA (protein.P37595). Substrates: H2O (molecule.C00001), L-Asparagine (molecule.C00152). Products: Ammonia (molecule.C00014), L-Aspartate (molecule.C00049).

## Annotation

L-Asparagine + H2O <=> L-Aspartate + Ammonia

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[protein.P00805|protein.P00805]] `KEGG` `database` - via EC:3.5.1.1
- `catalyzes` <-- [[protein.P0A962|protein.P0A962]] `KEGG` `database` - via EC:3.5.1.1
- `catalyzes` <-- [[protein.P37595|protein.P37595]] `KEGG` `database` - via EC:3.5.1.1
- `is_product_of` <-- [[molecule.C00014|molecule.C00014]] `KEGG` `database` - C00152 + C00001 <=> C00049 + C00014
- `is_product_of` <-- [[molecule.C00049|molecule.C00049]] `KEGG` `database` - C00152 + C00001 <=> C00049 + C00014
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C00152 + C00001 <=> C00049 + C00014
- `is_substrate_of` <-- [[molecule.C00152|molecule.C00152]] `KEGG` `database` - C00152 + C00001 <=> C00049 + C00014

## External IDs

- `KEGG:R00485`

## Notes

EQUATION: C00152 + C00001 <=> C00049 + C00014
