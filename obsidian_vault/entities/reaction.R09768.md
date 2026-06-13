---
entity_id: "reaction.R09768"
entity_type: "reaction"
name: "D-glycero-D-manno-heptose 7-phosphate aldose-ketose-isomerase"
source_database: "KEGG"
source_id: "R09768"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R09768"
---

# D-glycero-D-manno-heptose 7-phosphate aldose-ketose-isomerase

`reaction.R09768`

## Static

- Type: `reaction`
- Source: `KEGG:R09768`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Sedoheptulose 7-phosphate D-glycero-D-manno-Heptose 7-phosphate

## Biological Role

Catalyzed by gmhA (protein.P63224). Substrates: Sedoheptulose 7-phosphate (molecule.C05382).

## Annotation

Sedoheptulose 7-phosphate <=> D-glycero-D-manno-Heptose 7-phosphate

## Outgoing Edges (0)

_None._

## Incoming Edges (2)

- `catalyzes` <-- [[protein.P63224|protein.P63224]] `KEGG` `database` - via EC:5.3.1.28
- `is_substrate_of` <-- [[molecule.C05382|molecule.C05382]] `KEGG` `database` - C05382 <=> C19882

## External IDs

- `KEGG:R09768`

## Notes

EQUATION: C05382 <=> C19882
