---
entity_id: "reaction.R00996"
entity_type: "reaction"
name: "L-threonine ammonia-lyase (2-oxobutanoate-forming)"
source_database: "KEGG"
source_id: "R00996"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00996"
---

# L-threonine ammonia-lyase (2-oxobutanoate-forming)

`reaction.R00996`

## Static

- Type: `reaction`
- Source: `KEGG:R00996`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

L-Threonine 2-Oxobutanoate + Ammonia

## Biological Role

Catalyzed by ilvA (protein.P04968), tdcB (protein.P0AGF6). Substrates: L-Threonine (molecule.C00188). Products: Ammonia (molecule.C00014), 2-Oxobutanoate (molecule.C00109).

## Annotation

L-Threonine <=> 2-Oxobutanoate + Ammonia

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P04968|protein.P04968]] `KEGG` `database` - via EC:4.3.1.19
- `catalyzes` <-- [[protein.P0AGF6|protein.P0AGF6]] `KEGG` `database` - via EC:4.3.1.19
- `is_product_of` <-- [[molecule.C00014|molecule.C00014]] `KEGG` `database` - C00188 <=> C00109 + C00014
- `is_product_of` <-- [[molecule.C00109|molecule.C00109]] `KEGG` `database` - C00188 <=> C00109 + C00014
- `is_substrate_of` <-- [[molecule.C00188|molecule.C00188]] `KEGG` `database` - C00188 <=> C00109 + C00014

## External IDs

- `KEGG:R00996`

## Notes

EQUATION: C00188 <=> C00109 + C00014
