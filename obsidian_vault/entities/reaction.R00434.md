---
entity_id: "reaction.R00434"
entity_type: "reaction"
name: "GTP diphosphate-lyase (cyclizing; 3',5'-cyclic-GMP-forming)"
source_database: "KEGG"
source_id: "R00434"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00434"
---

# GTP diphosphate-lyase (cyclizing; 3',5'-cyclic-GMP-forming)

`reaction.R00434`

## Static

- Type: `reaction`
- Source: `KEGG:R00434`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

GTP 3',5'-Cyclic GMP + Diphosphate

## Biological Role

Catalyzed by cyaA (protein.P00936). Substrates: GTP (molecule.C00044). Products: Diphosphate (molecule.C00013), 3',5'-Cyclic GMP (molecule.C00942).

## Annotation

GTP <=> 3',5'-Cyclic GMP + Diphosphate

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[protein.P00936|protein.P00936]] `KEGG` `database` - via EC:4.6.1.1
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `KEGG` `database` - C00044 <=> C00942 + C00013
- `is_product_of` <-- [[molecule.C00942|molecule.C00942]] `KEGG` `database` - C00044 <=> C00942 + C00013
- `is_substrate_of` <-- [[molecule.C00044|molecule.C00044]] `KEGG` `database` - C00044 <=> C00942 + C00013

## External IDs

- `KEGG:R00434`

## Notes

EQUATION: C00044 <=> C00942 + C00013
