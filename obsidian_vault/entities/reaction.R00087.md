---
entity_id: "reaction.R00087"
entity_type: "reaction"
name: "ATP diphosphohydrolase (diphosphate-forming);"
source_database: "KEGG"
source_id: "R00087"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00087"
---

# ATP diphosphohydrolase (diphosphate-forming);

`reaction.R00087`

## Static

- Type: `reaction`
- Source: `KEGG:R00087`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ATP + H2O AMP + Diphosphate

## Biological Role

Catalyzed by mazG (protein.P0AEY3). Substrates: H2O (molecule.C00001), ATP (molecule.C00002). Products: Diphosphate (molecule.C00013), AMP (molecule.C00020).

## Annotation

ATP + H2O <=> AMP + Diphosphate

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P0AEY3|protein.P0AEY3]] `KEGG` `database` - via EC:3.6.1.9
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `KEGG` `database` - C00002 + C00001 <=> C00020 + C00013
- `is_product_of` <-- [[molecule.C00020|molecule.C00020]] `KEGG` `database` - C00002 + C00001 <=> C00020 + C00013
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C00002 + C00001 <=> C00020 + C00013
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `KEGG` `database` - C00002 + C00001 <=> C00020 + C00013

## External IDs

- `KEGG:R00087`

## Notes

EQUATION: C00002 + C00001 <=> C00020 + C00013
