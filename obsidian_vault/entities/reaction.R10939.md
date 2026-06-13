---
entity_id: "reaction.R10939"
entity_type: "reaction"
name: "(4S)-4-hydroxy-5-phosphooxypentane-2,3-dione aldose-ketose-isomerase"
source_database: "KEGG"
source_id: "R10939"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R10939"
---

# (4S)-4-hydroxy-5-phosphooxypentane-2,3-dione aldose-ketose-isomerase

`reaction.R10939`

## Static

- Type: `reaction`
- Source: `KEGG:R10939`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

(4S)-4-Hydroxy-5-phosphooxypentane-2,3-dione 3-Hydroxy-5-phosphooxypentane-2,4-dione

## Biological Role

Catalyzed by lsrG (protein.P64461). Substrates: (4S)-4-Hydroxy-5-phosphooxypentane-2,3-dione (molecule.C20959).

## Annotation

(4S)-4-Hydroxy-5-phosphooxypentane-2,3-dione <=> 3-Hydroxy-5-phosphooxypentane-2,4-dione

## Outgoing Edges (0)

_None._

## Incoming Edges (2)

- `catalyzes` <-- [[protein.P64461|protein.P64461]] `KEGG` `database` - via EC:5.3.1.32
- `is_substrate_of` <-- [[molecule.C20959|molecule.C20959]] `KEGG` `database` - C20959 <=> C20960

## External IDs

- `KEGG:R10939`

## Notes

EQUATION: C20959 <=> C20960
