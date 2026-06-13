---
entity_id: "reaction.R12624"
entity_type: "reaction"
name: "R12624"
source_database: "KEGG"
source_id: "R12624"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R12624"
---

# R12624

`reaction.R12624`

## Static

- Type: `reaction`
- Source: `KEGG:R12624`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Methylureidoacrylate + H2O Methylaminoacrylate + Carbamate

## Biological Role

Catalyzed by rutB (protein.P75897). Substrates: H2O (molecule.C00001). Products: Carbamate (molecule.C01563).

## Annotation

Methylureidoacrylate + H2O <=> Methylaminoacrylate + Carbamate

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.P75897|protein.P75897]] `KEGG` `database` - via EC:3.5.1.110
- `is_product_of` <-- [[molecule.C01563|molecule.C01563]] `KEGG` `database` - C20256 + C00001 <=> C20255 + C01563
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C20256 + C00001 <=> C20255 + C01563

## External IDs

- `KEGG:R12624`

## Notes

EQUATION: C20256 + C00001 <=> C20255 + C01563
