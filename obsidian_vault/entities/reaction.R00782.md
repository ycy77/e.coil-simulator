---
entity_id: "reaction.R00782"
entity_type: "reaction"
name: "L-cysteine hydrogen-sulfide-lyase (deaminating; pyruvate-forming)"
source_database: "KEGG"
source_id: "R00782"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00782"
---

# L-cysteine hydrogen-sulfide-lyase (deaminating; pyruvate-forming)

`reaction.R00782`

## Static

- Type: `reaction`
- Source: `KEGG:R00782`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

L-Cysteine + H2O Hydrogen sulfide + Pyruvate + Ammonia

## Biological Role

Catalyzed by metC (protein.P06721), malY (protein.P23256). Substrates: H2O (molecule.C00001), L-Cysteine (molecule.C00097). Products: Ammonia (molecule.C00014), Pyruvate (molecule.C00022), Hydrogen sulfide (molecule.C00283).

## Annotation

L-Cysteine + H2O <=> Hydrogen sulfide + Pyruvate + Ammonia

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[protein.P06721|protein.P06721]] `KEGG` `database` - via EC:4.4.1.13
- `catalyzes` <-- [[protein.P23256|protein.P23256]] `KEGG` `database` - via EC:4.4.1.13
- `is_product_of` <-- [[molecule.C00014|molecule.C00014]] `KEGG` `database` - C00097 + C00001 <=> C00283 + C00022 + C00014
- `is_product_of` <-- [[molecule.C00022|molecule.C00022]] `KEGG` `database` - C00097 + C00001 <=> C00283 + C00022 + C00014
- `is_product_of` <-- [[molecule.C00283|molecule.C00283]] `KEGG` `database` - C00097 + C00001 <=> C00283 + C00022 + C00014
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C00097 + C00001 <=> C00283 + C00022 + C00014
- `is_substrate_of` <-- [[molecule.C00097|molecule.C00097]] `KEGG` `database` - C00097 + C00001 <=> C00283 + C00022 + C00014

## External IDs

- `KEGG:R00782`

## Notes

EQUATION: C00097 + C00001 <=> C00283 + C00022 + C00014
