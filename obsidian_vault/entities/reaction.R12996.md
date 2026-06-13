---
entity_id: "reaction.R12996"
entity_type: "reaction"
name: "6-deoxy-6-sulfo-D-glucopyranose isomerase (2-epimerizing);"
source_database: "KEGG"
source_id: "R12996"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R12996"
---

# 6-deoxy-6-sulfo-D-glucopyranose isomerase (2-epimerizing);

`reaction.R12996`

## Static

- Type: `reaction`
- Source: `KEGG:R12996`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

6-Sulfo-beta-D-quinovose 6-Sulfo-D-rhamnose

## Biological Role

Catalyzed by yihS (protein.P32140). Substrates: 6-Sulfo-beta-D-quinovose (molecule.C22078).

## Annotation

6-Sulfo-beta-D-quinovose <=> 6-Sulfo-D-rhamnose

## Outgoing Edges (0)

_None._

## Incoming Edges (2)

- `catalyzes` <-- [[protein.P32140|protein.P32140]] `KEGG` `database` - via EC:5.3.1.31
- `is_substrate_of` <-- [[molecule.C22078|molecule.C22078]] `KEGG` `database` - C22078 <=> C22507

## External IDs

- `KEGG:R12996`

## Notes

EQUATION: C22078 <=> C22507
