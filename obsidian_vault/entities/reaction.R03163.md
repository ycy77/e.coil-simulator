---
entity_id: "reaction.R03163"
entity_type: "reaction"
name: "L-fucose aldose-ketose-isomerase"
source_database: "KEGG"
source_id: "R03163"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R03163"
---

# L-fucose aldose-ketose-isomerase

`reaction.R03163`

## Static

- Type: `reaction`
- Source: `KEGG:R03163`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

L-Fucose L-Fuculose

## Biological Role

Catalyzed by fucI (protein.P69922). Substrates: L-Fucose (molecule.C01019). Products: L-Fuculose (molecule.C01721).

## Annotation

L-Fucose <=> L-Fuculose

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.P69922|protein.P69922]] `KEGG` `database` - via EC:5.3.1.25
- `is_product_of` <-- [[molecule.C01721|molecule.C01721]] `KEGG` `database` - C01019 <=> C01721
- `is_substrate_of` <-- [[molecule.C01019|molecule.C01019]] `KEGG` `database` - C01019 <=> C01721

## External IDs

- `KEGG:R03163`

## Notes

EQUATION: C01019 <=> C01721
