---
entity_id: "reaction.R00589"
entity_type: "reaction"
name: "serine racemase"
source_database: "KEGG"
source_id: "R00589"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00589"
---

# serine racemase

`reaction.R00589`

## Static

- Type: `reaction`
- Source: `KEGG:R00589`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

L-Serine D-Serine

## Biological Role

Catalyzed by ygeA (protein.P03813). Substrates: L-Serine (molecule.C00065). Products: D-Serine (molecule.C00740).

## Annotation

L-Serine <=> D-Serine

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.P03813|protein.P03813]] `KEGG` `database` - via EC:5.1.1.10
- `is_product_of` <-- [[molecule.C00740|molecule.C00740]] `KEGG` `database` - C00065 <=> C00740
- `is_substrate_of` <-- [[molecule.C00065|molecule.C00065]] `KEGG` `database` - C00065 <=> C00740

## External IDs

- `KEGG:R00589`

## Notes

EQUATION: C00065 <=> C00740
