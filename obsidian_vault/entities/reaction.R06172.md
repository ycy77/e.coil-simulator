---
entity_id: "reaction.R06172"
entity_type: "reaction"
name: "R06172"
source_database: "KEGG"
source_id: "R06172"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R06172"
---

# R06172

`reaction.R06172`

## Static

- Type: `reaction`
- Source: `KEGG:R06172`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

G10551 + UDP-N-acetyl-D-glucosamine G10550 + UDP

## Biological Role

Catalyzed by murG (protein.P17443).

## Annotation

G10551 + UDP-N-acetyl-D-glucosamine <=> G10550 + UDP

## Outgoing Edges (0)

_None._

## Incoming Edges (1)

- `catalyzes` <-- [[protein.P17443|protein.P17443]] `KEGG` `database` - via EC:2.4.1.227

## External IDs

- `KEGG:R06172`

## Notes

EQUATION: G10551 + G10610 <=> G10550 + G10619
