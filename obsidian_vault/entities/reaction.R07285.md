---
entity_id: "reaction.R07285"
entity_type: "reaction"
name: "tRNA:phosphate nucleotidyltransferase"
source_database: "KEGG"
source_id: "R07285"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R07285"
---

# tRNA:phosphate nucleotidyltransferase

`reaction.R07285`

## Static

- Type: `reaction`
- Source: `KEGG:R07285`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

tRNA + Orthophosphate tRNA + NDP

## Biological Role

Catalyzed by rph (gene.b3643). Substrates: Orthophosphate (molecule.C00009).

## Annotation

tRNA + Orthophosphate <=> tRNA + NDP

## Outgoing Edges (0)

_None._

## Incoming Edges (2)

- `catalyzes` <-- [[gene.b3643|gene.b3643]] `KEGG` `database` - via EC:2.7.7.56
- `is_substrate_of` <-- [[molecule.C00009|molecule.C00009]] `KEGG` `database` - C00066 + C00009 <=> C00066 + C00454

## External IDs

- `KEGG:R07285`

## Notes

EQUATION: C00066 + C00009 <=> C00066 + C00454
