---
entity_id: "reaction.R00089"
entity_type: "reaction"
name: "ATP diphosphate-lyase (cyclizing; 3',5'-cyclic-AMP-forming)"
source_database: "KEGG"
source_id: "R00089"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00089"
---

# ATP diphosphate-lyase (cyclizing; 3',5'-cyclic-AMP-forming)

`reaction.R00089`

## Static

- Type: `reaction`
- Source: `KEGG:R00089`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ATP 3',5'-Cyclic AMP + Diphosphate

## Biological Role

Catalyzed by cyaA (protein.P00936). Substrates: ATP (molecule.C00002). Products: Diphosphate (molecule.C00013), 3',5'-Cyclic AMP (molecule.C00575).

## Annotation

ATP <=> 3',5'-Cyclic AMP + Diphosphate

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[protein.P00936|protein.P00936]] `KEGG` `database` - via EC:4.6.1.1
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `KEGG` `database` - C00002 <=> C00575 + C00013
- `is_product_of` <-- [[molecule.C00575|molecule.C00575]] `KEGG` `database` - C00002 <=> C00575 + C00013
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `KEGG` `database` - C00002 <=> C00575 + C00013

## External IDs

- `KEGG:R00089`

## Notes

EQUATION: C00002 <=> C00575 + C00013
