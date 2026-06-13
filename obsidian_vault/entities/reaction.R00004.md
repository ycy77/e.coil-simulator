---
entity_id: "reaction.R00004"
entity_type: "reaction"
name: "diphosphate phosphohydrolase;"
source_database: "KEGG"
source_id: "R00004"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00004"
---

# diphosphate phosphohydrolase;

`reaction.R00004`

## Static

- Type: `reaction`
- Source: `KEGG:R00004`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Diphosphate + H2O 2 Orthophosphate

## Biological Role

Catalyzed by ppa (protein.P0A7A9). Substrates: H2O (molecule.C00001), Diphosphate (molecule.C00013). Products: Orthophosphate (molecule.C00009).

## Annotation

Diphosphate + H2O <=> 2 Orthophosphate

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[protein.P0A7A9|protein.P0A7A9]] `KEGG` `database` - via EC:3.6.1.1
- `is_product_of` <-- [[molecule.C00009|molecule.C00009]] `KEGG` `database` - C00013 + C00001 <=> 2 C00009
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C00013 + C00001 <=> 2 C00009
- `is_substrate_of` <-- [[molecule.C00013|molecule.C00013]] `KEGG` `database` - C00013 + C00001 <=> 2 C00009

## External IDs

- `KEGG:R00004`

## Notes

EQUATION: C00013 + C00001 <=> 2 C00009
