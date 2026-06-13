---
entity_id: "reaction.R01532"
entity_type: "reaction"
name: "nucleoside-triphosphate diphosphohydrolase"
source_database: "KEGG"
source_id: "R01532"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R01532"
---

# nucleoside-triphosphate diphosphohydrolase

`reaction.R01532`

## Static

- Type: `reaction`
- Source: `KEGG:R01532`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Nucleoside triphosphate + H2O Nucleotide + Diphosphate

## Biological Role

Catalyzed by mazG (protein.P0AEY3). Substrates: H2O (molecule.C00001). Products: Diphosphate (molecule.C00013).

## Annotation

Nucleoside triphosphate + H2O <=> Nucleotide + Diphosphate

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.P0AEY3|protein.P0AEY3]] `KEGG` `database` - via EC:3.6.1.9
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `KEGG` `database` - C00201 + C00001 <=> C00215 + C00013
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C00201 + C00001 <=> C00215 + C00013

## External IDs

- `KEGG:R01532`

## Notes

EQUATION: C00201 + C00001 <=> C00215 + C00013
