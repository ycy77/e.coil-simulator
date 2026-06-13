---
entity_id: "reaction.R09769"
entity_type: "reaction"
name: "D-glycero-alpha-D-manno-heptose 7-phosphate aldose-ketose-isomerase"
source_database: "KEGG"
source_id: "R09769"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R09769"
---

# D-glycero-alpha-D-manno-heptose 7-phosphate aldose-ketose-isomerase

`reaction.R09769`

## Static

- Type: `reaction`
- Source: `KEGG:R09769`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Sedoheptulose 7-phosphate D-glycero-alpha-D-manno-Heptose 7-phosphate

## Biological Role

Catalyzed by gmhA (protein.P63224). Substrates: Sedoheptulose 7-phosphate (molecule.C05382). Products: D-glycero-alpha-D-manno-Heptose 7-phosphate (molecule.C19878).

## Annotation

Sedoheptulose 7-phosphate <=> D-glycero-alpha-D-manno-Heptose 7-phosphate

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.P63224|protein.P63224]] `KEGG` `database` - via EC:5.3.1.28
- `is_product_of` <-- [[molecule.C19878|molecule.C19878]] `KEGG` `database` - C05382 <=> C19878
- `is_substrate_of` <-- [[molecule.C05382|molecule.C05382]] `KEGG` `database` - C05382 <=> C19878

## External IDs

- `KEGG:R09769`

## Notes

EQUATION: C05382 <=> C19878
