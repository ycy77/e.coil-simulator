---
entity_id: "reaction.R08219"
entity_type: "reaction"
name: "selenophosphate:L-seryl-tRNASec selenium transferase"
source_database: "KEGG"
source_id: "R08219"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R08219"
---

# selenophosphate:L-seryl-tRNASec selenium transferase

`reaction.R08219`

## Static

- Type: `reaction`
- Source: `KEGG:R08219`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

L-Seryl-tRNA(Sec) + Selenophosphoric acid L-Selenocysteinyl-tRNA(Sec) + Orthophosphate

## Biological Role

Catalyzed by selA (protein.P0A821). Substrates: Selenophosphoric acid (molecule.C05172), L-Seryl-tRNA(Sec) (molecule.C06481). Products: Orthophosphate (molecule.C00009), L-Selenocysteinyl-tRNA(Sec) (molecule.C06482).

## Annotation

L-Seryl-tRNA(Sec) + Selenophosphoric acid <=> L-Selenocysteinyl-tRNA(Sec) + Orthophosphate

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P0A821|protein.P0A821]] `KEGG` `database` - via EC:2.9.1.1
- `is_product_of` <-- [[molecule.C00009|molecule.C00009]] `KEGG` `database` - C06481 + C05172 <=> C06482 + C00009
- `is_product_of` <-- [[molecule.C06482|molecule.C06482]] `KEGG` `database` - C06481 + C05172 <=> C06482 + C00009
- `is_substrate_of` <-- [[molecule.C05172|molecule.C05172]] `KEGG` `database` - C06481 + C05172 <=> C06482 + C00009
- `is_substrate_of` <-- [[molecule.C06481|molecule.C06481]] `KEGG` `database` - C06481 + C05172 <=> C06482 + C00009

## External IDs

- `KEGG:R08219`

## Notes

EQUATION: C06481 + C05172 <=> C06482 + C00009
