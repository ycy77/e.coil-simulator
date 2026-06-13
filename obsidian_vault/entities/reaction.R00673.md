---
entity_id: "reaction.R00673"
entity_type: "reaction"
name: "L-tryptophan indole-lyase (deaminating; pyruvate-forming)"
source_database: "KEGG"
source_id: "R00673"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00673"
---

# L-tryptophan indole-lyase (deaminating; pyruvate-forming)

`reaction.R00673`

## Static

- Type: `reaction`
- Source: `KEGG:R00673`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

L-Tryptophan + H2O Indole + Pyruvate + Ammonia

## Biological Role

Catalyzed by tnaA (protein.P0A853). Substrates: H2O (molecule.C00001), L-Tryptophan (molecule.C00078). Products: Ammonia (molecule.C00014), Pyruvate (molecule.C00022), Indole (molecule.C00463).

## Annotation

L-Tryptophan + H2O <=> Indole + Pyruvate + Ammonia

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P0A853|protein.P0A853]] `KEGG` `database` - via EC:4.1.99.1
- `is_product_of` <-- [[molecule.C00014|molecule.C00014]] `KEGG` `database` - C00078 + C00001 <=> C00463 + C00022 + C00014
- `is_product_of` <-- [[molecule.C00022|molecule.C00022]] `KEGG` `database` - C00078 + C00001 <=> C00463 + C00022 + C00014
- `is_product_of` <-- [[molecule.C00463|molecule.C00463]] `KEGG` `database` - C00078 + C00001 <=> C00463 + C00022 + C00014
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C00078 + C00001 <=> C00463 + C00022 + C00014
- `is_substrate_of` <-- [[molecule.C00078|molecule.C00078]] `KEGG` `database` - C00078 + C00001 <=> C00463 + C00022 + C00014

## External IDs

- `KEGG:R00673`

## Notes

EQUATION: C00078 + C00001 <=> C00463 + C00022 + C00014
