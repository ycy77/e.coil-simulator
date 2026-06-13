---
entity_id: "reaction.R00426"
entity_type: "reaction"
name: "GTP diphosphohydrolase (diphosphate-forming);"
source_database: "KEGG"
source_id: "R00426"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00426"
---

# GTP diphosphohydrolase (diphosphate-forming);

`reaction.R00426`

## Static

- Type: `reaction`
- Source: `KEGG:R00426`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

GTP + H2O GMP + Diphosphate

## Biological Role

Catalyzed by mazG (protein.P0AEY3). Substrates: H2O (molecule.C00001), GTP (molecule.C00044). Products: Diphosphate (molecule.C00013), GMP (molecule.C00144).

## Annotation

GTP + H2O <=> GMP + Diphosphate

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P0AEY3|protein.P0AEY3]] `KEGG` `database` - via EC:3.6.1.9
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `KEGG` `database` - C00044 + C00001 <=> C00144 + C00013
- `is_product_of` <-- [[molecule.C00144|molecule.C00144]] `KEGG` `database` - C00044 + C00001 <=> C00144 + C00013
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C00044 + C00001 <=> C00144 + C00013
- `is_substrate_of` <-- [[molecule.C00044|molecule.C00044]] `KEGG` `database` - C00044 + C00001 <=> C00144 + C00013

## External IDs

- `KEGG:R00426`

## Notes

EQUATION: C00044 + C00001 <=> C00144 + C00013
