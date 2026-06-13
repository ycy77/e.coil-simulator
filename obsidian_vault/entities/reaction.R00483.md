---
entity_id: "reaction.R00483"
entity_type: "reaction"
name: "L-aspartate:ammonia ligase (AMP-forming)"
source_database: "KEGG"
source_id: "R00483"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00483"
---

# L-aspartate:ammonia ligase (AMP-forming)

`reaction.R00483`

## Static

- Type: `reaction`
- Source: `KEGG:R00483`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ATP + L-Aspartate + Ammonia AMP + Diphosphate + L-Asparagine

## Biological Role

Catalyzed by asnA (protein.P00963), asnB (protein.P22106). Substrates: ATP (molecule.C00002), Ammonia (molecule.C00014), L-Aspartate (molecule.C00049). Products: Diphosphate (molecule.C00013), AMP (molecule.C00020), L-Asparagine (molecule.C00152).

## Annotation

ATP + L-Aspartate + Ammonia <=> AMP + Diphosphate + L-Asparagine

## Outgoing Edges (0)

_None._

## Incoming Edges (8)

- `catalyzes` <-- [[protein.P00963|protein.P00963]] `KEGG` `database` - via EC:6.3.1.1
- `catalyzes` <-- [[protein.P22106|protein.P22106]] `KEGG` `database` - via EC:6.3.5.4
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `KEGG` `database` - C00002 + C00049 + C00014 <=> C00020 + C00013 + C00152
- `is_product_of` <-- [[molecule.C00020|molecule.C00020]] `KEGG` `database` - C00002 + C00049 + C00014 <=> C00020 + C00013 + C00152
- `is_product_of` <-- [[molecule.C00152|molecule.C00152]] `KEGG` `database` - C00002 + C00049 + C00014 <=> C00020 + C00013 + C00152
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `KEGG` `database` - C00002 + C00049 + C00014 <=> C00020 + C00013 + C00152
- `is_substrate_of` <-- [[molecule.C00014|molecule.C00014]] `KEGG` `database` - C00002 + C00049 + C00014 <=> C00020 + C00013 + C00152
- `is_substrate_of` <-- [[molecule.C00049|molecule.C00049]] `KEGG` `database` - C00002 + C00049 + C00014 <=> C00020 + C00013 + C00152

## External IDs

- `KEGG:R00483`

## Notes

EQUATION: C00002 + C00049 + C00014 <=> C00020 + C00013 + C00152
