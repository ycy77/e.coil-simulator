---
entity_id: "reaction.R07809"
entity_type: "reaction"
name: "R07809"
source_database: "KEGG"
source_id: "R07809"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R07809"
---

# R07809

`reaction.R07809`

## Static

- Type: `reaction`
- Source: `KEGG:R07809`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

G13074 + H2O G01391 + N-Acetyl-D-glucosamine

## Biological Role

Catalyzed by nagZ (protein.P75949). Substrates: H2O (molecule.C00001). Products: N-Acetyl-D-glucosamine (molecule.C00140).

## Annotation

G13074 + H2O <=> G01391 + N-Acetyl-D-glucosamine

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.P75949|protein.P75949]] `KEGG` `database` - via EC:3.2.1.52
- `is_product_of` <-- [[molecule.C00140|molecule.C00140]] `KEGG` `database` - G13074 + C00001 <=> G01391 + C00140
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - G13074 + C00001 <=> G01391 + C00140

## External IDs

- `KEGG:R07809`

## Notes

EQUATION: G13074 + C00001 <=> G01391 + C00140
