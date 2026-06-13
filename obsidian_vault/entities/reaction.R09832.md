---
entity_id: "reaction.R09832"
entity_type: "reaction"
name: "8-oxo-dGTP diphosphohydrolase"
source_database: "KEGG"
source_id: "R09832"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R09832"
---

# 8-oxo-dGTP diphosphohydrolase

`reaction.R09832`

## Static

- Type: `reaction`
- Source: `KEGG:R09832`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

8-Oxo-dGTP + H2O 8-Oxo-dGMP + Diphosphate

## Biological Role

Catalyzed by mutT (protein.P08337). Substrates: H2O (molecule.C00001). Products: Diphosphate (molecule.C00013).

## Annotation

8-Oxo-dGTP + H2O <=> 8-Oxo-dGMP + Diphosphate

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.P08337|protein.P08337]] `KEGG` `database` - via EC:3.6.1.55
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `KEGG` `database` - C19967 + C00001 <=> C19968 + C00013
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C19967 + C00001 <=> C19968 + C00013

## External IDs

- `KEGG:R09832`

## Notes

EQUATION: C19967 + C00001 <=> C19968 + C00013
