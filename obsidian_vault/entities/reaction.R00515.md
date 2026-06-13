---
entity_id: "reaction.R00515"
entity_type: "reaction"
name: "CTP diphosphohydrolase (diphosphate-forming);"
source_database: "KEGG"
source_id: "R00515"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00515"
---

# CTP diphosphohydrolase (diphosphate-forming);

`reaction.R00515`

## Static

- Type: `reaction`
- Source: `KEGG:R00515`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CTP + H2O CMP + Diphosphate

## Biological Role

Catalyzed by mazG (protein.P0AEY3), nudG (protein.P77788). Substrates: H2O (molecule.C00001), CTP (molecule.C00063). Products: Diphosphate (molecule.C00013), CMP (molecule.C00055).

## Annotation

CTP + H2O <=> CMP + Diphosphate

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P0AEY3|protein.P0AEY3]] `KEGG` `database` - via EC:3.6.1.9
- `catalyzes` <-- [[protein.P77788|protein.P77788]] `KEGG` `database` - via EC:3.6.1.65
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `KEGG` `database` - C00063 + C00001 <=> C00055 + C00013
- `is_product_of` <-- [[molecule.C00055|molecule.C00055]] `KEGG` `database` - C00063 + C00001 <=> C00055 + C00013
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C00063 + C00001 <=> C00055 + C00013
- `is_substrate_of` <-- [[molecule.C00063|molecule.C00063]] `KEGG` `database` - C00063 + C00001 <=> C00055 + C00013

## External IDs

- `KEGG:R00515`

## Notes

EQUATION: C00063 + C00001 <=> C00055 + C00013
