---
entity_id: "reaction.R07810"
entity_type: "reaction"
name: "R07810"
source_database: "KEGG"
source_id: "R07810"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R07810"
---

# R07810

`reaction.R07810`

## Static

- Type: `reaction`
- Source: `KEGG:R07810`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

G13073 + H2O G01391 + N-Acetyl-D-glucosamine 6-sulfate

## Biological Role

Catalyzed by nagZ (protein.P75949). Substrates: H2O (molecule.C00001).

## Annotation

G13073 + H2O <=> G01391 + N-Acetyl-D-glucosamine 6-sulfate

## Outgoing Edges (0)

_None._

## Incoming Edges (2)

- `catalyzes` <-- [[protein.P75949|protein.P75949]] `KEGG` `database` - via EC:3.2.1.52
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - G13073 + C00001 <=> G01391 + C04132

## External IDs

- `KEGG:R07810`

## Notes

EQUATION: G13073 + C00001 <=> G01391 + C04132
